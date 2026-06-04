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
    classify_input_pressure,
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
        self.assertIn("founder_summary", result.stdout)
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
            "一屏摘要",
            "场景分流",
            "人话风险",
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
        self.assertEqual(report["report_id"], "minimal_cli_harness_dry_run_v0.3")
        self.assertEqual(report["intake_preview"]["platform_ref"], "cli_dry_run")
        self.assertTrue(report["intake_preview"]["no_write"])

    def test_cli_json_zh_runs(self):
        result = self.run_cli("--format", "json", "--lang", "zh")
        report = json.loads(result.stdout)

        self.assertEqual(report["lang"], "zh")
        self.assertIn("身份核心", report["context_package_preview"]["identity_refs"])
        self.assertEqual(report["observatory_snapshot"]["current_phase"], "P102 最小 CLI 试验台 scenario routing dry-run")

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
            "input_pressure_type",
            "scenario_profile",
            "pressure_reason",
            "matched_signals",
            "profile_specific_risks",
            "profile_specific_next_step",
            "profile_specific_do_not_do",
            "founder_summary",
            "human_readable_risks",
            "intake_preview",
            "context_package_preview",
            "candidate_preview",
            "review_queue_preview",
            "boundary_monitor",
            "observatory_snapshot",
            "non_execution_invariants",
        ):
            self.assertIn(key, report)
        for key in (
            "source_refs_preview",
            "selected_source_refs",
            "risk_refs_preview",
            "open_question_refs_preview",
            "risk_question_mapping_status",
            "missing_source_evidence",
            "source_backing_status",
            "source_loader_boundaries",
        ):
            self.assertIn(key, report["context_package_preview"])

    def test_all_candidates_remain_preview_only(self):
        report = build_harness_dry_run_report(user_message="这个想法可能是一次成长吗？")

        self.assertEqual(report["input_pressure_type"], "growth_review_pressure")
        self.assertIn("growth_candidate_review", {row["candidate_type"] for row in report["candidate_preview"]})
        for candidate in report["candidate_preview"]:
            self.assertTrue(candidate["preview_only"])
            self.assertFalse(candidate["promoted"])
            self.assertFalse(candidate["persisted"])
            self.assertIn("candidate_intent", candidate)
            self.assertIn("why_selected", candidate)
            self.assertIn("blocked_promotion_reason", candidate)
            self.assertIn("required_manual_review", candidate)

    def test_review_queue_remains_preview_only_with_manual_review_fields(self):
        report = build_harness_dry_run_report(user_message="这个想法可能是一次成长吗？", lang="zh")

        for row in report["review_queue_preview"]:
            self.assertIn("queue_intent", row)
            self.assertIn("why_this_gate", row)
            self.assertIn("blocked_lifecycle_reason", row)
            self.assertTrue(row["manual_review_required"])
            self.assertEqual(row["next_allowed_action"], "manual_review_only")
            self.assertFalse(row["lifecycle_created"])
            self.assertFalse(row["execution_allowed"])
            self.assertIn("不", row["blocked_lifecycle_reason"])

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
            "auto_tool_promotion_enabled",
            "policy_executor_enabled",
            "companion_feature_enabled",
            "adapter_integration_required",
            "harness_write_enabled",
            "observability_executor_enabled",
            "automatic_next_step_enabled",
            "product_layer_enabled",
            "reconstruction_reducer_executed",
            "event_compaction_executed",
        ):
            self.assertFalse(report[key])
        self.assertTrue(report["state_unchanged"])
        self.assertTrue(report["boundary_monitor"]["all_forbidden_actions_disabled"])
        self.assertEqual(report["boundary_monitor"]["active_boundary_violations"], [])

    def test_boundary_monitor_has_structured_disabled_capabilities(self):
        report = build_harness_dry_run_report(user_message="我想把这个接进 AstrBot", lang="zh")
        monitor = report["boundary_monitor"]
        rows = {row["flag"]: row for row in monitor["disabled_capabilities"]}

        for key in (
            "identity_core_mutated",
            "memory_rewrite_executed",
            "recall_mutation_executed",
            "growth_engine_executed",
            "tool_execution_enabled",
            "auto_tool_promotion_enabled",
            "temporal_event_executed",
            "adapter_integration_required",
            "companion_feature_enabled",
            "harness_write_enabled",
        ):
            self.assertIn(key, rows)
            self.assertEqual(rows[key]["status"], "disabled")
            self.assertFalse(rows[key]["value"])

        self.assertEqual(monitor["unchanged_state"][0]["flag"], "state_unchanged")
        self.assertEqual(monitor["unchanged_state"][0]["status"], "unchanged")
        self.assertTrue(monitor["unchanged_state"][0]["value"])

    def test_non_execution_invariants_are_explicit(self):
        report = build_harness_dry_run_report(user_message="Hello 01")

        for key, expected in NON_EXECUTION_INVARIANTS.items():
            self.assertEqual(report["non_execution_invariants"][key], expected)
            self.assertEqual(report[key], expected)

    def test_pressure_classifier_routes_known_inputs(self):
        cases = [
            ("我现在有点看不清这个项目到底做了什么", "observability_pressure", "可见性压力"),
            ("这个想法可能是一次成长吗？", "growth_review_pressure", "成长审查压力"),
            ("我想把这个接进 AstrBot", "adapter_boundary_pressure", "接入边界压力"),
            ("我们是不是该开始做应用层了？", "product_layer_pressure", "产品层压力"),
            ("这个工具候选验证成功了，能不能直接加入工具库？", "capability_evolution_pressure", "能力进化压力"),
            ("我隔了很久回来，怎么恢复会话？", "temporal_pressure", "时间压力"),
            ("这个 event 能回放重建 payload diff 吗？", "reconstruction_pressure", "重建压力"),
            ("请记录一个普通观察", "unknown_pressure", "未分类压力"),
        ]

        for user_message, pressure_type, zh_name in cases:
            with self.subTest(pressure_type=pressure_type):
                classification = classify_input_pressure(user_message)
                report = build_harness_dry_run_report(user_message=user_message, lang="zh")

                self.assertEqual(classification["input_pressure_type"], pressure_type)
                self.assertEqual(report["input_pressure_type"], pressure_type)
                self.assertEqual(report["scenario_profile"]["internal_key"], pressure_type)
                self.assertEqual(report["scenario_profile"]["display_name"], zh_name)
                self.assertEqual(report["observatory_snapshot"]["input_pressure_type"], pressure_type)
                if pressure_type == "unknown_pressure":
                    self.assertEqual(report["matched_signals"], [])
                else:
                    self.assertGreater(len(report["matched_signals"]), 0)

    def test_different_pressures_produce_different_candidate_previews(self):
        messages = {
            "observability_pressure": "我现在有点看不清这个项目到底做了什么",
            "growth_review_pressure": "这个想法可能是一次成长吗？",
            "adapter_boundary_pressure": "我想把这个接进 AstrBot",
            "product_layer_pressure": "我们是不是该开始做应用层了？",
            "capability_evolution_pressure": "这个工具候选验证成功了，能不能直接加入工具库？",
            "temporal_pressure": "我隔了很久回来，怎么恢复会话？",
            "reconstruction_pressure": "这个 event 能回放重建 payload diff 吗？",
            "unknown_pressure": "请记录一个普通观察",
        }
        previews = {}

        for pressure_type, user_message in messages.items():
            report = build_harness_dry_run_report(user_message=user_message)
            previews[pressure_type] = tuple(row["candidate_type"] for row in report["candidate_preview"])

        self.assertEqual(len(set(previews.values())), len(messages))

    def test_pressure_specific_fields_are_present(self):
        report = build_harness_dry_run_report(
            user_message="这个工具候选验证成功了，能不能直接加入工具库？",
            lang="zh",
        )

        self.assertEqual(report["input_pressure_type"], "capability_evolution_pressure")
        self.assertIn("工具授权候选", {row["display_name"] for row in report["candidate_preview"]})
        self.assertIn("tool_execution_enabled", report["boundary_monitor"]["highest_relevant_boundaries"])
        self.assertIn("auto_tool_promotion_enabled", report["boundary_monitor"]["highest_relevant_boundaries"])
        self.assertIn("验证不等于授权", report["context_package_preview"]["profile_refs"])
        self.assertIn("capability_evolution_boundary", report["context_package_preview"]["selected_source_refs"])
        self.assertIn("人工审查", report["profile_specific_next_step"])

        tool_candidate = next(
            row for row in report["candidate_preview"] if row["candidate_type"] == "tool_authorization_candidate"
        )
        self.assertIn("不是授权", tool_candidate["blocked_promotion_reason"])
        self.assertEqual(tool_candidate["required_manual_review"], "capability_or_tool_authorization_review")

    def test_context_preview_uses_source_backed_refs_by_pressure(self):
        temporal_report = build_harness_dry_run_report(user_message="我隔了很久回来，怎么恢复会话？", lang="zh")
        capability_report = build_harness_dry_run_report(
            user_message="这个工具候选验证成功了，能不能直接加入工具库？",
            lang="zh",
        )
        reconstruction_report = build_harness_dry_run_report(
            user_message="这个 event 能回放重建 payload diff 吗？",
            lang="en",
        )

        temporal_refs = temporal_report["context_package_preview"]["selected_source_refs"]
        capability_refs = capability_report["context_package_preview"]["selected_source_refs"]
        reconstruction_refs = reconstruction_report["context_package_preview"]["selected_source_refs"]

        self.assertIn("ctm_temporal_dynamics", temporal_refs)
        self.assertIn("temporal_coherence_eval", temporal_refs)
        self.assertIn("capability_evolution_boundary", capability_refs)
        self.assertIn("tool_first_self_evolution", capability_refs)
        self.assertIn("reconstruction_reducer_contract", reconstruction_refs)
        self.assertNotEqual(temporal_refs, capability_refs)
        self.assertNotEqual(capability_refs, reconstruction_refs)

        for report in (temporal_report, capability_report, reconstruction_report):
            context_preview = report["context_package_preview"]
            self.assertEqual(context_preview["missing_source_evidence"], [])
            self.assertTrue(context_preview["source_backing_status"]["all_selected_sources_available"])
            self.assertFalse(context_preview["source_backing_status"]["retrieval_executed"])
            self.assertFalse(context_preview["source_backing_status"]["state_written"])
            self.assertTrue(context_preview["source_loader_boundaries"]["whitelist_only"])
            self.assertFalse(context_preview["source_loader_boundaries"]["user_supplied_paths_allowed"])
            self.assertFalse(context_preview["source_loader_boundaries"]["external_io_allowed"])
            self.assertFalse(context_preview["source_loader_boundaries"]["model_call_allowed"])
            self.assertFalse(context_preview["source_loader_boundaries"]["source_loader_write_enabled"])
            self.assertFalse(context_preview["risk_question_mapping_status"]["policy_executed"])
            self.assertFalse(context_preview["risk_question_mapping_status"]["automatic_decision"])
            for source_ref in context_preview["source_refs_preview"]:
                self.assertEqual(source_ref["read_mode"], "read_only")
                self.assertEqual(source_ref["source_status"], "approved_whitelist")
                self.assertTrue(source_ref["path"].endswith(".md"))

    def test_context_preview_includes_source_backed_risk_and_question_refs(self):
        temporal_report = build_harness_dry_run_report(user_message="我隔了很久回来，怎么恢复会话？", lang="zh")
        capability_report = build_harness_dry_run_report(
            user_message="这个工具候选验证成功了，能不能直接加入工具库？",
            lang="zh",
        )
        reconstruction_report = build_harness_dry_run_report(
            user_message="这个 event 能回放重建 payload diff 吗？",
            lang="en",
        )

        temporal_context = temporal_report["context_package_preview"]
        capability_context = capability_report["context_package_preview"]
        reconstruction_context = reconstruction_report["context_package_preview"]

        self.assertIn("R5", {row["risk_id"] for row in temporal_context["risk_refs_preview"]})
        self.assertIn("时间感知", {row["question"] for row in temporal_context["open_question_refs_preview"]})
        self.assertIn("R20", {row["risk_id"] for row in capability_context["risk_refs_preview"]})
        self.assertIn("工具优先自进化", {row["question"] for row in capability_context["open_question_refs_preview"]})
        self.assertIn("R8", {row["risk_id"] for row in reconstruction_context["risk_refs_preview"]})
        self.assertIn(
            "Reconstruction Reducer Contract",
            {row["question"] for row in reconstruction_context["open_question_refs_preview"]},
        )

        for context in (temporal_context, capability_context, reconstruction_context):
            self.assertGreater(context["risk_question_mapping_status"]["risk_count"], 0)
            self.assertGreater(context["risk_question_mapping_status"]["open_question_count"], 0)
            for row in context["risk_refs_preview"] + context["open_question_refs_preview"]:
                self.assertEqual(row["read_mode"], "read_only")
                self.assertEqual(row["mapping_mode"], "deterministic_pressure_mapping")
                self.assertFalse(row["policy_executed"])

    def test_candidate_preview_specialization_fields_change_by_pressure(self):
        adapter_report = build_harness_dry_run_report(user_message="我想把这个接进 AstrBot", lang="zh")
        temporal_report = build_harness_dry_run_report(user_message="我隔了很久回来，怎么恢复会话？", lang="zh")

        adapter_candidate = adapter_report["candidate_preview"][0]
        temporal_candidate = temporal_report["candidate_preview"][0]
        self.assertNotEqual(adapter_candidate["candidate_intent"], temporal_candidate["candidate_intent"])
        self.assertIn("不批准接入", adapter_candidate["candidate_intent"])
        self.assertIn("不写 temporal/recall event", temporal_candidate["candidate_intent"])

    def test_review_queue_specialization_fields_change_by_pressure(self):
        adapter_report = build_harness_dry_run_report(user_message="我想把这个接进 AstrBot", lang="zh")
        capability_report = build_harness_dry_run_report(
            user_message="这个工具候选验证成功了，能不能直接加入工具库？",
            lang="zh",
        )

        adapter_gate = adapter_report["review_queue_preview"][0]
        capability_gate = capability_report["review_queue_preview"][0]
        self.assertNotEqual(adapter_gate["queue_intent"], capability_gate["queue_intent"])
        self.assertIn("不批准接入", adapter_gate["queue_intent"])
        self.assertIn("不授权工具", capability_gate["queue_intent"])
        self.assertIn("不是 adapter integration", adapter_gate["blocked_lifecycle_reason"])
        self.assertIn("不是授权", capability_gate["blocked_lifecycle_reason"])

    def test_founder_summary_is_human_readable_and_non_executing(self):
        report = build_harness_dry_run_report(
            user_message="我们是不是该开始做应用层了？",
            lang="zh",
        )

        summary = report["founder_summary"]
        self.assertEqual(summary["classification"], "产品层压力 (product_layer_pressure)")
        self.assertIn("命中信号", summary["why_this_classification"])
        self.assertIn("不能检索真实记忆", summary["what_it_cannot_do_now"])
        self.assertTrue(any("不要进入产品层" in item for item in summary["do_not_do_yet"]))
        self.assertIn("profile_specific_do_not_do", report)
        self.assertGreater(len(report["human_readable_risks"]), 0)
        for risk in report["human_readable_risks"]:
            self.assertIn("why_it_matters", risk)
            self.assertIn("current_guardrail", risk)
            self.assertIn("next_manual_check", risk)


if __name__ == "__main__":
    unittest.main()
