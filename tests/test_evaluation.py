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
        self.assertEqual(report["passed"], 4)
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

        metrics = report["metrics_summary"]
        self.assertEqual(metrics["total_scenarios"], 4)
        self.assertEqual(metrics["failed_scenarios"], 0)
        self.assertEqual(metrics["boundary_violation_count"], 0)
        self.assertEqual(metrics["archived_memory_retrieval_count"], 0)
        self.assertGreaterEqual(metrics["claim_count"], 1)
        self.assertEqual(metrics["unreviewed_memory_mutation_count"], 0)
        self.assertEqual(metrics["task_resume_score"], 1.0)


if __name__ == "__main__":
    unittest.main()
