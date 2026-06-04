import tempfile
import unittest
import json
import os
import subprocess
import sys
from pathlib import Path

from one_core.source_loader import (
    NON_EXECUTION_INVARIANTS,
    PRESSURE_SOURCE_IDS,
    REPO_ROOT,
    SOURCE_WHITELIST,
    build_source_inventory_report,
    load_source_inventory,
    load_source_record,
    render_source_inventory_report,
    source_refs_for_pressure,
    validate_source_whitelist,
)


class SourceLoaderTests(unittest.TestCase):
    def run_inventory_cli(self, *args, state_dir=None):
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
                    "harness-source-inventory",
                    *args,
                ],
                cwd=REPO_ROOT,
                env=env,
                capture_output=True,
                text=True,
                check=True,
            )

    def test_load_source_inventory_en_and_zh(self):
        en_sources = load_source_inventory(lang="en")
        zh_sources = load_source_inventory(lang="zh")

        self.assertEqual(len(en_sources), len(SOURCE_WHITELIST))
        self.assertEqual(len(zh_sources), len(SOURCE_WHITELIST))
        self.assertEqual(en_sources[0]["source_id"], "phase_index")
        self.assertEqual(zh_sources[0]["source_id"], "phase_index")
        self.assertTrue(en_sources[0]["path"].endswith(".md"))
        self.assertTrue(zh_sources[0]["path"].endswith("_ZH.md"))

    def test_whitelist_paths_are_root_relative_markdown(self):
        for spec in SOURCE_WHITELIST:
            for path in (spec.en_path, spec.zh_path):
                candidate = Path(path)
                self.assertFalse(candidate.is_absolute())
                self.assertEqual(candidate.suffix, ".md")
                self.assertEqual(len(candidate.parts), 1)
                self.assertFalse(any(part.startswith(".") or part == ".." for part in candidate.parts))
                self.assertEqual((REPO_ROOT / candidate).resolve().parent, REPO_ROOT)

    def test_load_source_record_rejects_unknown_id(self):
        with self.assertRaises(ValueError):
            load_source_record("../README.md")

        with self.assertRaises(ValueError):
            load_source_record("missing_source")

    def test_pressure_mappings_are_distinct_and_read_only(self):
        pressure_records = {}
        for pressure in PRESSURE_SOURCE_IDS:
            refs = source_refs_for_pressure(pressure, lang="en")
            pressure_records[pressure] = tuple(ref["source_id"] for ref in refs)
            self.assertGreater(len(refs), 0)
            for ref in refs:
                self.assertEqual(ref["read_mode"], "read_only")
                self.assertEqual(ref["source_status"], "approved_whitelist")

        self.assertNotEqual(pressure_records["temporal_pressure"], pressure_records["capability_evolution_pressure"])
        self.assertIn("ctm_temporal_dynamics", pressure_records["temporal_pressure"])
        self.assertIn("capability_evolution_boundary", pressure_records["capability_evolution_pressure"])
        self.assertIn("reconstruction_reducer_contract", pressure_records["reconstruction_pressure"])

    def test_source_inventory_report_contains_boundaries(self):
        report = build_source_inventory_report(lang="en")

        self.assertEqual(report["report_id"], "harness_source_inventory_v0.1")
        self.assertEqual(report["scope"], "read_only_whitelisted_markdown")
        self.assertEqual(report["source_count"], len(SOURCE_WHITELIST))
        self.assertEqual(report["safety_status"], "pass")
        self.assertEqual(report["safety_issues"], [])
        self.assertIn("work_01_state", report["disallowed_sources"])
        for key, expected in NON_EXECUTION_INVARIANTS.items():
            self.assertEqual(report["non_execution_invariants"][key], expected)

    def test_validate_source_whitelist_passes_without_io_or_writes(self):
        safety = validate_source_whitelist()

        self.assertEqual(safety["status"], "pass")
        self.assertEqual(safety["issues"], [])
        self.assertEqual(safety["checked_source_count"], len(SOURCE_WHITELIST))
        self.assertEqual(safety["read_mode"], "metadata_validation_only")
        self.assertFalse(safety["writes_performed"])
        self.assertFalse(safety["external_io_performed"])

    def test_render_source_inventory_markdown_and_json(self):
        report = build_source_inventory_report(lang="zh")
        markdown = render_source_inventory_report(report, "markdown")
        json_output = render_source_inventory_report(report, "json")

        self.assertIn("Harness Source Inventory", markdown)
        self.assertIn("Pressure Mappings", markdown)
        self.assertIn("safety_status", markdown)
        self.assertIn("issue_count: 0", markdown)
        self.assertIn("source_loader_write_enabled: false", markdown)
        self.assertIn('"report_id": "harness_source_inventory_v0.1"', json_output)
        self.assertIn('"safety_status": "pass"', json_output)

    def test_invalid_lang_and_format_rejected(self):
        with self.assertRaises(ValueError):
            load_source_inventory(lang="jp")
        with self.assertRaises(ValueError):
            render_source_inventory_report(build_source_inventory_report(), "html")

    def test_loader_does_not_change_state_or_sources(self):
        source_path = REPO_ROOT / "PHASE_INDEX.md"
        before_source = source_path.stat().st_mtime_ns
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            state_dir.mkdir()
            marker = state_dir / "marker.txt"
            marker.write_text("unchanged", encoding="utf-8")
            before_state = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}

            build_source_inventory_report(lang="en")
            source_refs_for_pressure("temporal_pressure", lang="zh")

            after_state = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}
            self.assertEqual(after_state, before_state)
            self.assertEqual(marker.read_text(encoding="utf-8"), "unchanged")
        self.assertEqual(source_path.stat().st_mtime_ns, before_source)

    def test_source_inventory_cli_markdown_en_runs(self):
        result = self.run_inventory_cli("--format", "markdown", "--lang", "en")

        self.assertIn("# Harness Source Inventory", result.stdout)
        self.assertIn("Pressure Mappings", result.stdout)
        self.assertIn("Non-Execution Invariants", result.stdout)
        self.assertIn("source_loader_write_enabled: false", result.stdout)

    def test_source_inventory_cli_json_zh_contains_safety_and_boundaries(self):
        result = self.run_inventory_cli("--format", "json", "--lang", "zh")
        report = json.loads(result.stdout)

        self.assertEqual(report["report_id"], "harness_source_inventory_v0.1")
        self.assertEqual(report["lang"], "zh")
        self.assertEqual(report["safety_status"], "pass")
        self.assertEqual(report["source_count"], len(SOURCE_WHITELIST))
        self.assertIn("temporal_pressure", report["pressure_mappings"])
        for key, expected in NON_EXECUTION_INVARIANTS.items():
            self.assertEqual(report["non_execution_invariants"][key], expected)

    def test_source_inventory_cli_output_writes_only_report_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            output_path = Path(tmp) / "inventory.md"
            before = sorted(Path(tmp).rglob("*"))

            result = self.run_inventory_cli("--output", str(output_path), state_dir=state_dir)

            after = sorted(Path(tmp).rglob("*"))
            self.assertEqual(result.stdout, "")
            self.assertTrue(output_path.exists())
            self.assertFalse(state_dir.exists())
            self.assertEqual(after, before + [output_path])

    def test_source_inventory_cli_does_not_modify_existing_state_dir(self):
        with tempfile.TemporaryDirectory() as tmp:
            state_dir = Path(tmp) / "state"
            state_dir.mkdir()
            marker = state_dir / "marker.txt"
            marker.write_text("unchanged", encoding="utf-8")
            before = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}

            self.run_inventory_cli("--format", "json", "--lang", "en", state_dir=state_dir)

            after = {path.relative_to(tmp): path.stat().st_mtime_ns for path in Path(tmp).rglob("*")}
            self.assertEqual(after, before)
            self.assertEqual(marker.read_text(encoding="utf-8"), "unchanged")


if __name__ == "__main__":
    unittest.main()
