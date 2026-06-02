import unittest

from one_core.evaluation import run_foundation_evaluation


class FoundationEvaluationTests(unittest.TestCase):
    def test_foundation_evaluation_passes(self):
        report = run_foundation_evaluation()
        self.assertEqual(report["suite"], "foundation")
        self.assertEqual(report["state_mode"], "temporary")
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed"], 0)
        self.assertGreaterEqual(report["passed"], 4)

        check_names = {check["name"] for check in report["checks"]}
        self.assertIn("continuity_anchors", check_names)
        self.assertIn("dry_run_is_non_mutating", check_names)
        self.assertIn("adapter_event_deduplication", check_names)
        self.assertIn("identity_overwrite_is_gated", check_names)


if __name__ == "__main__":
    unittest.main()
