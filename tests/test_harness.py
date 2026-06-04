import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from one_core.harness import (
    BOUNDARY_MONITOR,
    NON_EXECUTION_INVARIANTS,
    build_harness_dry_run_report,
)


REPO_ROOT = Path(__file__).resolve().parents[1]


class HarnessDryRunTests(unittest.TestCase):
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
                    "harness-dry-run",
                    "--input",
                    "We should pressure test 01 Core without writing memory.",
                    *args,
                ],
                cwd=REPO_ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )

    def test_cli_markdown_en_runs(self):
        result = self.run_cli("--format", "markdown", "--lang", "en")

        self.assertIn("# Minimal CLI Harness Dry-Run Report", result.stdout)
        self.assertIn("intake_preview", result.stdout)
        self.assertIn("context_package_preview", result.stdout)
        self.assertIn("candidate_preview", result.stdout)
        self.assertIn("review_queue_preview", result.stdout)
        self.assertIn("boundary_monitor", result.stdout)
        self.assertIn("observatory_snapshot", result.stdout)

    def test_cli_markdown_zh_runs(self):
        result = self.run_cli("--format", "markdown", "--lang", "zh")

        self.assertIn("最小 CLI 试验台 Dry-Run 报告", result.stdout)
        for label in (
            "输入预览",
            "上下文包预览",
            "候选项预览",
            "审查队列预览",
            "边界监视器",
            "观察台快照",
            "非执行边界",
        ):
            self.assertIn(label, result.stdout)

    def test_cli_json_en_runs(self):
        result = self.run_cli("--format", "json", "--lang", "en")
        report = json.loads(result.stdout)

        self.assertEqual(report["lang"], "en")
        self.assertEqual(report["intake_preview"]["platform_ref"], "cli_dry_run")
        self.assertTrue(report["intake_preview"]["no_write"])

    def test_cli_json_zh_runs(self):
        result = self.run_cli("--format", "json", "--lang", "zh")
        report = json.loads(result.stdout)

        self.assertEqual(report["lang"], "zh")
        self.assertIn("身份核心", report["context_package_preview"]["identity_refs"])
        self.assertEqual(report["observatory_snapshot"]["current_phase"], "P100 最小 CLI 试验台 dry-run")

    def test_output_writes_temp_file_without_state(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            output_path = Path(tmp) / "harness.md"
            before = sorted(Path(tmp).rglob("*"))

            result = self.run_cli("--output", str(output_path), state_dir=state_dir)

            after = sorted(Path(tmp).rglob("*"))
            self.assertEqual(result.stdout, "")
            self.assertTrue(output_path.exists())
            self.assertFalse(state_dir.exists())
            self.assertEqual(after, before + [output_path])

    def test_state_directory_unchanged_after_run(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            state_dir.mkdir()
            marker = state_dir / "marker.txt"
            marker.write_text("unchanged", encoding="utf-8")
            before = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}

            self.run_cli("--format", "json", state_dir=state_dir)

            after = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}
            self.assertEqual(after, before)
            self.assertEqual(marker.read_text(encoding="utf-8"), "unchanged")

    def test_report_contains_required_sections(self):
        report = build_harness_dry_run_report(user_message="Hello 01")

        for key in (
            "intake_preview",
            "context_package_preview",
            "candidate_preview",
            "review_queue_preview",
            "boundary_monitor",
            "observatory_snapshot",
            "non_execution_invariants",
        ):
            self.assertIn(key, report)

    def test_all_candidates_remain_preview_only(self):
        report = build_harness_dry_run_report(user_message="Hello 01")

        expected_types = {
            "memory_candidate",
            "claim_candidate",
            "growth_candidate_review",
            "meaning_shift_candidate",
            "recall_event_candidate",
            "task_update_candidate",
        }
        self.assertEqual({row["candidate_type"] for row in report["candidate_preview"]}, expected_types)
        for candidate in report["candidate_preview"]:
            self.assertTrue(candidate["preview_only"])
            self.assertFalse(candidate["promoted"])
            self.assertFalse(candidate["persisted"])

    def test_forbidden_boundaries_are_disabled(self):
        report = build_harness_dry_run_report(user_message="Hello 01")

        for key, expected in BOUNDARY_MONITOR.items():
            self.assertEqual(report["boundary_monitor"][key], expected)
            self.assertEqual(report[key], expected)

        for key in (
            "identity_core_mutated",
            "memory_rewrite_executed",
            "recall_mutation_executed",
            "growth_engine_executed",
            "temporal_event_executed",
            "tool_execution_enabled",
            "policy_executor_enabled",
            "companion_feature_enabled",
            "adapter_integration_required",
            "harness_write_enabled",
        ):
            self.assertFalse(report[key])
        self.assertTrue(report["state_unchanged"])

    def test_non_execution_invariants_are_explicit(self):
        report = build_harness_dry_run_report(user_message="Hello 01")

        for key, expected in NON_EXECUTION_INVARIANTS.items():
            self.assertEqual(report["non_execution_invariants"][key], expected)
            self.assertEqual(report[key], expected)


if __name__ == "__main__":
    unittest.main()
