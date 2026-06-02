import tempfile
import unittest
from pathlib import Path

from one_core.state import StateStore
from one_core.validation import validate_state


class StateValidationTests(unittest.TestCase):
    def test_initialized_state_passes_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "passed")
            self.assertEqual(report["issue_count"], 0)

    def test_missing_continuity_anchor_fails_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["working_state"]["context_anchors"].pop("who_am_i")
            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("working_state.context_anchors.who_am_i", paths)

    def test_adapter_event_index_must_point_to_episode(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["adapter_event_index"] = {
                "local_generic_adapter": {
                    "event-1": {
                        "adapter_id": "local_generic_adapter",
                        "event_id": "event-1",
                        "episode_id": "missing_episode",
                        "recorded_at": state["created_at"],
                        "channel": "local",
                    }
                }
            }
            report = validate_state(state, [{"id": "episode_present"}])
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn(
                "adapter_event_index.local_generic_adapter.event-1.episode_id",
                paths,
            )

    def test_durable_memory_requires_lifecycle_and_provenance(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            memory = state["memory_stores"]["semantic_memory"][0]
            memory.pop("lifecycle")
            memory.pop("provenance")
            memory.pop("update_history")

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("memory_stores.semantic_memory[0].lifecycle", paths)
            self.assertIn("memory_stores.semantic_memory[0].provenance", paths)
            self.assertIn("memory_stores.semantic_memory[0].update_history", paths)

    def test_snapshot_requires_rollback_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["snapshots"].append(
                {
                    "snapshot_id": "snapshot_missing_rollback",
                    "timestamp": state["created_at"],
                    "actor": "unit_test",
                    "operation": "promote_candidate",
                    "target_path": "memory_stores.semantic_memory",
                    "state_version": state["state_version"],
                    "rollback": {},
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("snapshots[0].rollback.reversible", paths)

    def test_claim_graph_requires_provenance_evidence_and_resolution(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["claim_graph"]["claims"].append(
                {
                    "claim_id": "claim_bad",
                    "timestamp": state["created_at"],
                    "claim_type": "false_memory_injection",
                    "statement": "Unsupported claim.",
                    "status": "open",
                    "evidence": [],
                    "provenance": [],
                    "resolution": {},
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("claim_graph.claims[0].evidence", paths)
            self.assertIn("claim_graph.claims[0].provenance", paths)
            self.assertIn("claim_graph.claims[0].resolution", paths)

    def test_task_hub_requires_action_and_procedural_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["task_hub"]["action_trace"].append(
                {
                    "action_id": "action_bad",
                    "workflow": "record_episode",
                }
            )
            state["task_hub"]["procedural_candidates"].append(
                {
                    "candidate_id": "proc_bad",
                    "workflow": "record_episode",
                    "evidence": [],
                    "review_status": "pending",
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("task_hub.action_trace[0].trace_id", paths)
            self.assertIn("task_hub.action_trace[0].timestamp", paths)
            self.assertIn("task_hub.procedural_candidates[0].evidence", paths)

    def test_identity_update_gate_requires_proposal_gate_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["identity_update_gate"]["proposals"].append(
                {
                    "proposal_id": "identity_proposal_bad",
                    "statement": "Unsupported identity update.",
                    "target_path": "identity_core",
                    "evidence": [],
                    "review_status": "pending",
                    "may_update_identity_core": True,
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("identity_update_gate.proposals[0].gate_result", paths)
            self.assertIn("identity_update_gate.proposals[0].drift_score", paths)
            self.assertIn("identity_update_gate.proposals[0].non_claims_check", paths)
            self.assertIn(
                "identity_update_gate.proposals[0].may_update_identity_core",
                paths,
            )

    def test_event_log_requires_valid_update_reference(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            report = validate_state(
                state,
                store.list_episodes(),
                events=[
                    {
                        "event_id": "event_bad",
                        "sequence": 1,
                        "timestamp": state["created_at"],
                        "event_type": "state_transition",
                        "workflow": "record_episode",
                        "trace_id": "trace_bad",
                        "update_id": "missing_update",
                        "operation": "append",
                        "target_path": "memory_stores.episodic_memory",
                    }
                ],
            )

            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("events[0].update_id", paths)


if __name__ == "__main__":
    unittest.main()
