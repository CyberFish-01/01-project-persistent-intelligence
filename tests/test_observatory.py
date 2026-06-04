import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from one_core.observatory import (
    NON_EXECUTION_INVARIANTS,
    READINESS_CATEGORIES,
    build_observatory_report,
    render_observatory_report,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class ObservatoryReportTests(unittest.TestCase):
    def run_cli(self, *args, state_dir=None):
        with tempfile.TemporaryDirectory() as tmp:
            state_path = Path(state_dir) if state_dir else Path(tmp) / "state"
            env = dict(os.environ)
            env["PYTHONDONTWRITEBYTECODE"] = "1"
            return subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "one_core.cli",
                    "--state-dir",
                    str(state_path),
                    "foundation-observatory-report",
                    *args,
                ],
                cwd=REPO_ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )

    def test_cli_runs_with_markdown_output(self):
        result = self.run_cli()

        self.assertIn("# Foundation Observatory Report", result.stdout)
        for section in (
            "founder_snapshot",
            "main_axes_map",
            "readiness_matrix",
            "boundary_status",
            "risk_heatmap",
            "next_step_recommendations",
            "what_not_to_build_yet",
            "non_execution_invariants",
        ):
            self.assertIn(section, result.stdout)

    def test_json_output_contains_required_keys(self):
        result = self.run_cli("--format", "json")
        report = json.loads(result.stdout)

        for key in (
            "founder_snapshot",
            "main_axes_map",
            "readiness_matrix",
            "boundary_status",
            "risk_heatmap",
            "next_step_recommendations",
            "what_not_to_build_yet",
            "non_execution_invariants",
        ):
            self.assertIn(key, report)
        self.assertEqual(report["readiness_categories"], READINESS_CATEGORIES)
        for key, expected in NON_EXECUTION_INVARIANTS.items():
            self.assertEqual(report[key], expected)
            self.assertEqual(report["non_execution_invariants"][key], expected)

    def test_zh_output_uses_chinese_display_names(self):
        markdown = self.run_cli("--lang", "zh").stdout
        report = build_observatory_report(lang="zh")

        self.assertIn("地基观察台报告", markdown)
        self.assertIn("创始人快照", markdown)
        self.assertIn("身份核心", markdown)
        self.assertIn("时间感知", markdown)
        self.assertIn("地基观察台", markdown)
        readiness_names = {row["display_name"] for row in report["readiness_matrix"]}
        self.assertIn("身份核心", readiness_names)
        self.assertIn("地基观察台", readiness_names)

    def test_report_marks_rfc_only_concepts_correctly(self):
        report = build_observatory_report()
        matrix = {row["internal_key"]: row for row in report["readiness_matrix"]}

        self.assertEqual(matrix["Stateful Memory"]["status"], "rfc_only")
        self.assertEqual(matrix["Growth Candidate Review"]["status"], "rfc_only")
        self.assertEqual(matrix["Temporal Awareness"]["status"], "rfc_only")
        self.assertEqual(matrix["Tool-First Self-Evolution"]["status"], "rfc_only")
        self.assertEqual(matrix["Temporal Coherence"]["status"], "evaluation_only")
        self.assertEqual(matrix["Event Log"]["status"], "implemented")
        self.assertEqual(matrix["Foundation Observatory"]["status"], "implemented")

    def test_boundary_status_keeps_forbidden_items_disabled(self):
        report = build_observatory_report()
        boundaries = {row["internal_key"]: row for row in report["boundary_status"]}

        for boundary in (
            "identity mutation",
            "memory rewrite",
            "recall event write",
            "growth engine",
            "temporal runtime",
            "CTM runtime",
            "tool execution",
            "tool promotion",
            "policy executor",
            "companion layer",
            "UI / AstrBot / adapter",
            "reconstruction reducer",
            "event compaction",
        ):
            self.assertIn(boundary, boundaries)
            self.assertFalse(boundaries[boundary]["enabled"])

        self.assertFalse(report["identity_core_mutated"])
        self.assertFalse(report["memory_rewrite_executed"])
        self.assertFalse(report["recall_mutation_executed"])
        self.assertFalse(report["growth_engine_executed"])
        self.assertFalse(report["temporal_event_executed"])
        self.assertFalse(report["tool_execution_enabled"])
        self.assertFalse(report["policy_executor_enabled"])
        self.assertFalse(report["companion_feature_enabled"])
        self.assertFalse(report["adapter_integration_required"])

    def test_render_json_and_markdown_are_deterministic_shapes(self):
        report = build_observatory_report(lang="en")
        markdown = render_observatory_report(report, "markdown")
        parsed = json.loads(render_observatory_report(report, "json"))

        self.assertIn("observatory_report_only: true", markdown)
        self.assertIn("execution_prohibited: true", markdown)
        self.assertIn("state_unchanged: true", markdown)
        self.assertEqual(parsed["report_id"], report["report_id"])
        self.assertEqual(parsed["observatory_scope"], "read_only_static_report")

    def test_no_state_file_changed_after_running_cli(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            output_path = Path(tmp) / "observatory.md"
            before = sorted(Path(tmp).rglob("*"))

            result = self.run_cli("--output", str(output_path), state_dir=state_dir)

            after = sorted(Path(tmp).rglob("*"))
            self.assertEqual(result.stdout, "")
            self.assertTrue(output_path.exists())
            self.assertFalse(state_dir.exists())
            self.assertEqual(after, before + [output_path])


if __name__ == "__main__":
    unittest.main()
