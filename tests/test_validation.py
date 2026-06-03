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

    def test_context_builder_requires_policy_and_trace_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["context_builder"]["policy"]["budgets"].pop("source_attribution")
            state["context_builder"]["policy"].pop("signal_weights")
            state["context_builder"]["activation_traces"].append(
                {"trace_id": "trace_missing_metadata"}
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn(
                "context_builder.policy.budgets.source_attribution",
                paths,
            )
            self.assertIn("context_builder.policy.signal_weights", paths)
            self.assertIn(
                "context_builder.activation_traces[0].context_package_id",
                paths,
            )

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

    def test_claim_graph_requires_links_and_review_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["claim_graph"]["claims"].append(
                {
                    "claim_id": "claim_bad_review",
                    "timestamp": state["created_at"],
                    "claim_type": "false_memory_injection",
                    "statement": "Unsupported claim.",
                    "status": "quarantined",
                    "evidence": ["episode_1"],
                    "provenance": [{"type": "unit_test"}],
                    "dependencies": ["episode_1"],
                    "revision_policy": {"mode": "minimal_change_preview"},
                    "resolution": {
                        "status": "quarantined",
                        "requires_review": False,
                    },
                    "last_review_decision_id": "claim_decision_missing",
                }
            )
            state["claim_graph"]["links"].append(
                {
                    "from": "episode_1",
                    "to": "memory_stores.semantic_memory",
                    "type": "invalid_link_type",
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("claim_graph.claims[0].review_history", paths)
            self.assertIn("claim_graph.claims[0].resolution.patch_preview", paths)
            self.assertIn("claim_graph.links[0].link_id", paths)
            self.assertIn("claim_graph.links[0].type", paths)
            self.assertIn("claim_graph.links[0]", paths)

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
                    "review_status": "approved",
                    "last_review_decision_id": "procedural_decision_missing",
                }
            )
            state["task_hub"]["procedural_memory"].append(
                {
                    "memory_id": "proc_mem_bad",
                    "workflow": "record_episode",
                    "status": "draft",
                }
            )
            state["task_hub"]["procedural_review_decisions"].append(
                {
                    "decision_id": "procedural_decision_bad",
                    "candidate_id": "proc_bad",
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("task_hub.action_trace[0].trace_id", paths)
            self.assertIn("task_hub.action_trace[0].timestamp", paths)
            self.assertIn("task_hub.procedural_candidates[0].evidence", paths)
            self.assertIn("task_hub.procedural_candidates[0].review_history", paths)
            self.assertIn("task_hub.procedural_memory[0].steps", paths)
            self.assertIn("task_hub.procedural_memory[0].status", paths)
            self.assertIn(
                "task_hub.procedural_review_decisions[0].workflow",
                paths,
            )

    def test_failure_reflection_requires_metadata(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["task_hub"]["reflection_log"].append(
                {
                    "reflection_id": "reflection_bad",
                    "timestamp": state["created_at"],
                    "reflection_type": "general",
                    "workflow": "tool_use",
                    "observation": "Observed something.",
                }
            )
            state["task_hub"]["reflection_guidance_queue"].append(
                {
                    "guidance_item_id": "reflection_guidance_bad",
                    "reflection_id": "reflection_bad",
                    "workflow": "tool_use",
                    "review_priority": "high",
                    "recommended_review_mode": "cautionary_review_only",
                    "evidence": ["action_bad"],
                    "review_status": "acknowledged",
                    "execution_prohibited": False,
                    "executable_policy_created": True,
                    "identity_mutation_allowed": True,
                    "last_review_decision_id": "reflection_guidance_decision_missing",
                    "review_history": [],
                    "provenance": [],
                }
            )
            state["task_hub"]["reflection_guidance_decisions"].append(
                {
                    "decision_id": "reflection_guidance_decision_bad",
                    "timestamp": state["created_at"],
                    "guidance_item_id": "reflection_guidance_bad",
                    "reflection_id": "reflection_bad",
                    "workflow": "tool_use",
                    "reviewer": "unit_test",
                    "action": "acknowledge",
                    "result": "approved",
                    "snapshot_id": "snapshot_bad",
                    "execution_prohibited": False,
                    "executable_policy_created": True,
                    "identity_mutation_allowed": True,
                }
            )
            state["task_hub"]["failure_reflections"].append(
                {
                    "reflection_id": "failure_reflection_bad",
                    "workflow": "tool_use",
                    "summary": "Tool failed.",
                }
            )
            state["task_hub"]["cautionary_procedural_candidates"].append(
                {
                    "candidate_id": "caution_bad",
                    "workflow": "tool_use",
                    "statement": "Avoid repeating failure.",
                    "review_status": "approved",
                    "last_review_decision_id": "cautionary_decision_missing",
                }
            )
            state["task_hub"]["cautionary_procedural_memory"].append(
                {
                    "memory_id": "caution_mem_bad",
                    "workflow": "tool_use",
                    "statement": "Avoid repeating failure.",
                    "avoid": "Missing required input.",
                    "status": "archived",
                    "executable_policy": True,
                }
            )
            state["task_hub"]["cautionary_review_decisions"].append(
                {
                    "decision_id": "cautionary_decision_bad",
                    "candidate_id": "caution_bad",
                    "workflow": "tool_use",
                    "reviewer": "unit_test",
                    "action": "approve",
                    "result": "approved",
                    "snapshot_id": "snapshot_bad",
                    "executable_policy_created": True,
                }
            )
            state["task_hub"]["cautionary_lifecycle_decisions"].append(
                {
                    "decision_id": "cautionary_lifecycle_bad",
                    "timestamp": state["created_at"],
                    "memory_id": "caution_mem_bad",
                    "workflow": "tool_use",
                    "reviewer": "unit_test",
                    "action": "archive",
                    "result": "approved",
                    "snapshot_id": "snapshot_bad",
                    "executable_policy_created": True,
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("task_hub.failure_reflections[0].lesson", paths)
            self.assertIn("task_hub.failure_reflections[0].evidence", paths)
            self.assertIn("task_hub.reflection_log[0].lesson", paths)
            self.assertIn("task_hub.reflection_log[0].expected_behavior", paths)
            self.assertIn("task_hub.reflection_log[0].verification_history", paths)
            self.assertIn(
                "task_hub.reflection_guidance_queue[0].execution_prohibited",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_queue[0].executable_policy_created",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_queue[0].identity_mutation_allowed",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_queue[0].review_history",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_decisions[0].result",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_decisions[0].execution_prohibited",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_decisions[0].executable_policy_created",
                paths,
            )
            self.assertIn(
                "task_hub.reflection_guidance_decisions[0].identity_mutation_allowed",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_candidates[0].avoid",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_candidates[0].source_reflection_id",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_candidates[0].review_history",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_memory[0].evidence",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_memory[0].executable_policy",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_memory[0].lifecycle.lifecycle_decision_id",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_procedural_memory[0].lifecycle_history",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_review_decisions[0].timestamp",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_review_decisions[0].executable_policy_created",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_lifecycle_decisions[0].result",
                paths,
            )
            self.assertIn(
                "task_hub.cautionary_lifecycle_decisions[0].executable_policy_created",
                paths,
            )

    def test_procedural_lifecycle_requires_valid_result(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["task_hub"]["procedural_lifecycle_decisions"].append(
                {
                    "decision_id": "procedural_lifecycle_bad",
                    "timestamp": state["created_at"],
                    "memory_id": "proc_mem_bad",
                    "workflow": "record_episode",
                    "reviewer": "unit_test",
                    "action": "archive",
                    "result": "approved",
                    "snapshot_id": "snapshot_bad",
                }
            )

            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn(
                "task_hub.procedural_lifecycle_decisions[0].result",
                paths,
            )

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

    def test_dream_artifact_requires_package_fields(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            report = validate_state(
                state,
                store.list_episodes(),
                dream_artifacts=[
                    {
                        "artifact_id": "dream_artifact_bad",
                        "dream_id": "dream_bad",
                        "input_manifest": {},
                        "decision_log": [],
                        "rollback_metadata": {},
                        "package_completeness": {
                            "has_input_manifest": True,
                            "has_review_queue": False,
                        },
                    }
                ],
            )

            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("dream_artifacts[0].artifact_version", paths)
            self.assertIn("dream_artifacts[0].review", paths)
            self.assertIn("dream_artifacts[0].input_manifest.items", paths)
            self.assertIn("dream_artifacts[0].decision_log", paths)
            self.assertIn("dream_artifacts[0].rollback_metadata.affected_ids", paths)
            self.assertIn(
                "dream_artifacts[0].package_completeness.has_review_queue",
                paths,
            )


if __name__ == "__main__":
    unittest.main()
