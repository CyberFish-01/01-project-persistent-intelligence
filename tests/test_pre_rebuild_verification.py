import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from one_core.pre_rebuild_verification import (
    CURRENT_PHASE,
    NON_EXECUTION_INVARIANTS,
    REPO_ROOT,
    build_pre_rebuild_verification_report,
    render_pre_rebuild_verification_report,
)


class PreRebuildVerificationTests(unittest.TestCase):
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
                    "pre-rebuild-verification",
                    *args,
                ],
                cwd=REPO_ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )

    def test_report_contains_required_sections(self):
        report = build_pre_rebuild_verification_report(lang="en")

        self.assertEqual(report["report_id"], "pre_rebuild_verification_suite_v0.1")
        self.assertEqual(report["current_phase"], CURRENT_PHASE)
        for key in (
            "verification_summary",
            "gate_results",
            "required_artifacts",
            "phase_index_status",
            "index_status",
            "readme_status",
            "forbidden_pattern_status",
            "markdown_link_status",
            "read_only_cli_status",
            "boundary_status",
            "ctm_temporal_status",
            "tool_first_status",
            "non_execution_invariants",
        ):
            self.assertIn(key, report)

    def test_report_passes_when_p151_docs_are_present(self):
        report = build_pre_rebuild_verification_report(lang="en")

        self.assertEqual(report["verification_summary"]["status"], "pass")
        self.assertTrue(report["verification_summary"]["ready_for_final_verification_report"])
        self.assertFalse(report["verification_summary"]["ready_for_rebuild"])
        for gate in report["gate_results"]:
            self.assertEqual(gate["status"], "pass", gate)

    def test_required_artifacts_include_p151_and_future_artifacts_are_not_required_now(self):
        report = build_pre_rebuild_verification_report(lang="zh")
        required = {row["phase"]: row for row in report["required_artifacts"]}
        future = {row["phase"]: row for row in report["future_artifacts"]}

        self.assertEqual(required["P151"]["status"], "present")
        self.assertEqual(required["P151"]["en_path"], "PRE_REBUILD_VERIFICATION_SUITE.md")
        self.assertEqual(required["P151"]["zh_path"], "PRE_REBUILD_VERIFICATION_SUITE_ZH.md")
        for row in future.values():
            self.assertFalse(row["required_now"])
            self.assertIn(row["status"], {"pending_future_phase", "present"})

    def test_forbidden_patterns_and_boundaries_are_clear(self):
        report = build_pre_rebuild_verification_report(lang="en")

        self.assertEqual(report["forbidden_pattern_status"]["status"], "pass")
        self.assertEqual(report["forbidden_pattern_status"]["matches"], [])
        self.assertEqual(report["boundary_status"]["status"], "pass")
        for key, expected in NON_EXECUTION_INVARIANTS.items():
            self.assertEqual(report["non_execution_invariants"][key], expected)
            self.assertEqual(report[key], expected)

    def test_read_only_cli_status_checks_existing_builders(self):
        report = build_pre_rebuild_verification_report(lang="zh")
        status = report["read_only_cli_status"]

        self.assertEqual(status["status"], "pass")
        self.assertIn("foundation_observatory_report", status["checked_reports"])
        self.assertIn("harness_source_inventory", status["checked_reports"])
        self.assertIn("harness_dry_run_en", status["checked_reports"])
        self.assertIn("harness_dry_run_zh", status["checked_reports"])
        self.assertTrue(status["read_only_builder_mode"])
        self.assertFalse(status["subprocess_executed"])
        self.assertFalse(status["external_io_performed"])

    def test_markdown_and_json_render(self):
        report = build_pre_rebuild_verification_report(lang="zh")
        markdown = render_pre_rebuild_verification_report(report, "markdown")
        parsed = json.loads(render_pre_rebuild_verification_report(report, "json"))

        self.assertIn("# 重构前验证套件报告", markdown)
        self.assertIn("Verification Summary", markdown)
        self.assertIn("Non-Execution Invariants", markdown)
        self.assertIn("rebuild_started: false", markdown)
        self.assertEqual(parsed["report_id"], report["report_id"])
        self.assertEqual(parsed["verification_summary"]["status"], "pass")

    def test_cli_markdown_en_runs(self):
        result = self.run_cli("--format", "markdown", "--lang", "en")

        self.assertIn("# Pre-Rebuild Verification Suite Report", result.stdout)
        self.assertIn("Gate Results", result.stdout)
        self.assertIn("pre_rebuild_verification_report_only: true", result.stdout)
        self.assertIn("rebuild_started: false", result.stdout)

    def test_cli_json_zh_runs(self):
        result = self.run_cli("--format", "json", "--lang", "zh")
        report = json.loads(result.stdout)

        self.assertEqual(report["lang"], "zh")
        self.assertEqual(report["verification_summary"]["display_name"], "重构前验证摘要")
        self.assertEqual(report["verification_summary"]["status"], "pass")
        self.assertFalse(report["rebuild_started"])

    def test_output_writes_only_report_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            output_path = Path(tmp) / "pre_rebuild.md"
            before = sorted(Path(tmp).rglob("*"))

            result = self.run_cli("--output", str(output_path), state_dir=state_dir)

            after = sorted(Path(tmp).rglob("*"))
            self.assertEqual(result.stdout, "")
            self.assertTrue(output_path.exists())
            self.assertFalse(state_dir.exists())
            self.assertEqual(after, before + [output_path])

    def test_cli_does_not_modify_existing_state_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            state_dir.mkdir()
            marker = state_dir / "marker.txt"
            marker.write_text("unchanged", encoding="utf-8")
            before = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}

            self.run_cli("--format", "json", "--lang", "en", state_dir=state_dir)

            after = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}
            self.assertEqual(after, before)
            self.assertEqual(marker.read_text(encoding="utf-8"), "unchanged")


if __name__ == "__main__":
    unittest.main()
