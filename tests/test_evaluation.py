import unittest

from one_core.evaluation import run_foundation_evaluation, run_scenario_evaluation


class FoundationEvaluationTests(unittest.TestCase):
    def test_foundation_evaluation_passes(self):
        report = run_foundation_evaluation()
        self.assertEqual(report["suite"], "foundation")
        self.assertEqual(report["state_mode"], "temporary")
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed"], 0)
        self.assertGreaterEqual(report["passed"], 7)

        check_names = {check["name"] for check in report["checks"]}
        self.assertIn("state_invariants", check_names)
        self.assertIn("continuity_anchors", check_names)
        self.assertIn("dry_run_is_non_mutating", check_names)
        self.assertIn("adapter_event_deduplication", check_names)
        self.assertIn("identity_overwrite_is_gated", check_names)
        self.assertIn(
            "false_memory_injection_is_quarantined_or_not_promoted",
            check_names,
        )
        self.assertIn(
            "preference_change_creates_candidate_not_stale_overwrite",
            check_names,
        )

    def test_scenario_evaluation_passes(self):
        report = run_scenario_evaluation()
        self.assertEqual(report["suite"], "scenarios")
        self.assertEqual(report["state_mode"], "temporary")
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed"], 0)
        self.assertEqual(report["passed"], 13)
        self.assertEqual(
            report["baselines"]["system_under_test"],
            "state_transfer_system",
        )
        self.assertIn(
            "retrieval_only_baseline",
            report["baselines"]["tracked_baselines"],
        )

        scenario_names = {scenario["name"] for scenario in report["scenarios"]}
        self.assertIn("interrupted_project_resume", scenario_names)
        self.assertIn("multi_user_boundary", scenario_names)
        self.assertIn("lifecycle_retrieval_suppression", scenario_names)
        self.assertIn("claim_graph_conflict_provenance", scenario_names)
        self.assertIn("claim_graph_review_patch_preview", scenario_names)
        self.assertIn("task_hub_action_resume", scenario_names)
        self.assertIn("procedural_memory_review", scenario_names)
        self.assertIn("failure_reflection", scenario_names)
        self.assertIn("procedural_lifecycle_retention", scenario_names)
        self.assertIn("identity_update_gate_review", scenario_names)
        self.assertIn("event_log_replay_rollback", scenario_names)
        self.assertIn("dream_artifact_package", scenario_names)
        self.assertIn("context_builder_policy_trace", scenario_names)

        metrics = report["metrics_summary"]
        self.assertEqual(metrics["total_scenarios"], 13)
        self.assertEqual(metrics["failed_scenarios"], 0)
        self.assertEqual(metrics["boundary_violation_count"], 0)
        self.assertEqual(metrics["archived_memory_retrieval_count"], 0)
        self.assertGreaterEqual(metrics["claim_count"], 1)
        self.assertEqual(metrics["unreviewed_memory_mutation_count"], 0)
        self.assertEqual(metrics["task_resume_score"], 1.0)
        self.assertEqual(metrics["task_hub_resume_score"], 1.0)
        self.assertGreaterEqual(metrics["procedural_candidate_count"], 1)
        self.assertEqual(metrics["procedural_review_score"], 1.0)
        self.assertGreaterEqual(metrics["procedural_memory_count"], 1)
        self.assertGreaterEqual(metrics["procedural_review_decision_count"], 1)
        self.assertEqual(metrics["procedural_identity_mutation_count"], 0)
        self.assertEqual(metrics["failure_reflection_score"], 1.0)
        self.assertGreaterEqual(metrics["failure_reflection_count"], 1)
        self.assertGreaterEqual(metrics["failure_caution_count"], 1)
        self.assertEqual(metrics["failure_identity_mutation_count"], 0)
        self.assertEqual(metrics["procedural_lifecycle_score"], 1.0)
        self.assertGreaterEqual(metrics["procedural_lifecycle_decision_count"], 1)
        self.assertGreaterEqual(metrics["procedural_archived_count"], 1)
        self.assertEqual(metrics["procedural_active_context_count"], 0)
        self.assertEqual(metrics["identity_gate_score"], 1.0)
        self.assertEqual(metrics["approved_identity_updates"], 1)
        self.assertEqual(metrics["identity_core_mutation_count"], 0)
        self.assertEqual(metrics["identity_gate_quarantine_count"], 1)
        self.assertEqual(metrics["event_log_replay_score"], 1.0)
        self.assertGreaterEqual(metrics["event_count"], 5)
        self.assertGreaterEqual(metrics["event_coverage_count"], 5)
        self.assertEqual(metrics["rollback_preview_count"], 1)
        self.assertEqual(metrics["rollback_mutation_count"], 0)
        self.assertEqual(metrics["dream_artifact_package_score"], 1.0)
        self.assertGreaterEqual(metrics["dream_artifact_count"], 1)
        self.assertGreaterEqual(metrics["dream_review_queue_count"], 1)
        self.assertEqual(metrics["dream_package_validation_failures"], 0)
        self.assertEqual(metrics["claim_review_score"], 1.0)
        self.assertGreaterEqual(metrics["claim_link_count"], 2)
        self.assertGreaterEqual(metrics["claim_review_decision_count"], 1)
        self.assertEqual(metrics["claim_patch_mutation_count"], 0)
        self.assertEqual(metrics["context_builder_score"], 1.0)
        self.assertGreaterEqual(metrics["context_activation_trace_count"], 1)
        self.assertGreaterEqual(metrics["context_signal_count"], 1)


if __name__ == "__main__":
    unittest.main()
