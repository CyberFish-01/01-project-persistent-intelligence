from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from .harness import build_harness_dry_run_report
from .observatory import build_observatory_report
from .source_loader import build_source_inventory_report


REPO_ROOT = Path(__file__).resolve().parents[1]

LANGUAGES = ("en", "zh")
OUTPUT_FORMATS = ("markdown", "json")
CURRENT_PHASE = "P151"

FORBIDDEN_TRUE_FLAGS = (
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
    "ctm_runtime_enabled",
    "external_io_enabled",
    "model_call_enabled",
    "source_loader_write_enabled",
    "app_write_enabled",
    "rebuild_started",
)

NON_EXECUTION_INVARIANTS = {
    "pre_rebuild_verification_report_only": True,
    "execution_prohibited": True,
    "state_unchanged": True,
    "identity_core_mutated": False,
    "memory_rewrite_executed": False,
    "recall_mutation_executed": False,
    "growth_engine_executed": False,
    "temporal_event_executed": False,
    "tool_execution_enabled": False,
    "auto_tool_promotion_enabled": False,
    "policy_executor_enabled": False,
    "companion_feature_enabled": False,
    "adapter_integration_required": False,
    "harness_write_enabled": False,
    "ctm_runtime_enabled": False,
    "external_io_enabled": False,
    "model_call_enabled": False,
    "source_loader_write_enabled": False,
    "app_write_enabled": False,
    "rebuild_started": False,
}

CURRENT_REQUIRED_ARTIFACTS = (
    ("P112", "STATE_BACKED_READ_ONLY_HARNESS_RFC.md", "STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md"),
    ("P113", "HARNESS_SOURCE_INVENTORY.md", "HARNESS_SOURCE_INVENTORY_ZH.md"),
    ("P114", "READ_ONLY_SOURCE_LOADER_PLAN.md", "READ_ONLY_SOURCE_LOADER_PLAN_ZH.md"),
    ("P116", "SOURCE_LOADER_SAFETY_HARDENING.md", "SOURCE_LOADER_SAFETY_HARDENING_ZH.md"),
    ("P120", "SOURCE_BACKED_HARNESS_USABILITY_REVIEW.md", "SOURCE_BACKED_HARNESS_USABILITY_REVIEW_ZH.md"),
    ("P121", "CORE_LOCKDOWN_MODE_RFC.md", "CORE_LOCKDOWN_MODE_RFC_ZH.md"),
    ("P122", "IMPORT_QUARANTINE_RFC.md", "IMPORT_QUARANTINE_RFC_ZH.md"),
    ("P123", "SHADOW_ADAPTER_MODE_RFC.md", "SHADOW_ADAPTER_MODE_RFC_ZH.md"),
    ("P124", "CONTAMINATION_SCAN_RFC.md", "CONTAMINATION_SCAN_RFC_ZH.md"),
    ("P125", "LOCKDOWN_INTEGRATION_READINESS.md", "LOCKDOWN_INTEGRATION_READINESS_ZH.md"),
    ("P126", "LOCKDOWN_FIXTURE_MATRIX.md", "LOCKDOWN_FIXTURE_MATRIX_ZH.md"),
    ("P127", "QUARANTINE_REVIEW_GATE_PLAN.md", "QUARANTINE_REVIEW_GATE_PLAN_ZH.md"),
    ("P128", "SHADOW_ADAPTER_EXAMPLE_SHAPES.md", "SHADOW_ADAPTER_EXAMPLE_SHAPES_ZH.md"),
    ("P129", "CONTAMINATION_FALSE_POSITIVE_REVIEW.md", "CONTAMINATION_FALSE_POSITIVE_REVIEW_ZH.md"),
    ("P130", "CORE_LOCKDOWN_CYCLE_REVIEW.md", "CORE_LOCKDOWN_CYCLE_REVIEW_ZH.md"),
    ("P131", "FOUNDER_CONSOLE_BOUNDARY_RFC.md", "FOUNDER_CONSOLE_BOUNDARY_RFC_ZH.md"),
    ("P132", "FOUNDER_CONSOLE_USER_FLOW.md", "FOUNDER_CONSOLE_USER_FLOW_ZH.md"),
    ("P133", "FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md", "FOUNDER_CONSOLE_NO_WRITE_CONTRACT_ZH.md"),
    ("P134", "FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md", "FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA_ZH.md"),
    ("P135", "FOUNDER_CONSOLE_RISK_REVIEW.md", "FOUNDER_CONSOLE_RISK_REVIEW_ZH.md"),
    ("P136", "FOUNDER_CONSOLE_ROADMAP.md", "FOUNDER_CONSOLE_ROADMAP_ZH.md"),
    ("P137", "CONTEXT_PACKAGE_BUILDER_RFC.md", "CONTEXT_PACKAGE_BUILDER_RFC_ZH.md"),
    ("P138", "CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md", "CONTEXT_PACKAGE_PREVIEW_CLI_PLAN_ZH.md"),
    ("P139", "SOURCE_SELECTION_MATRIX.md", "SOURCE_SELECTION_MATRIX_ZH.md"),
    ("P140", "BOUNDARY_INJECTION_RFC.md", "BOUNDARY_INJECTION_RFC_ZH.md"),
    ("P141", "CTM_TEMPORAL_CONTEXT_PACK_RFC.md", "CTM_TEMPORAL_CONTEXT_PACK_RFC_ZH.md"),
    ("P142", "CAPABILITY_CONTEXT_PACK_RFC.md", "CAPABILITY_CONTEXT_PACK_RFC_ZH.md"),
    ("P143", "RESPONSE_ORCHESTRATION_PREVIEW_RFC.md", "RESPONSE_ORCHESTRATION_PREVIEW_RFC_ZH.md"),
    ("P144", "LLM_AS_RESOURCE_BOUNDARY_RFC.md", "LLM_AS_RESOURCE_BOUNDARY_RFC_ZH.md"),
    ("P145", "POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md", "POST_RESPONSE_CANDIDATE_EXTRACTION_RFC_ZH.md"),
    ("P146", "MANUAL_REVIEW_GATE_RFC.md", "MANUAL_REVIEW_GATE_RFC_ZH.md"),
    ("P147", "REBUILD_MIGRATION_PROTOCOL_RFC.md", "REBUILD_MIGRATION_PROTOCOL_RFC_ZH.md"),
    ("P148", "REBUILD_ENTRY_GATE_CHECKLIST.md", "REBUILD_ENTRY_GATE_CHECKLIST_ZH.md"),
    ("P149", "PRE_REBUILD_SYSTEM_REVIEW.md", "PRE_REBUILD_SYSTEM_REVIEW_ZH.md"),
    ("P150", "FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md", "FULL_VERIFICATION_PLAN_BEFORE_REBUILD_ZH.md"),
    ("P151", "PRE_REBUILD_VERIFICATION_SUITE.md", "PRE_REBUILD_VERIFICATION_SUITE_ZH.md"),
)

FUTURE_ARTIFACTS = (
    ("P152", "VERIFICATION_REPORT.md", "VERIFICATION_REPORT_ZH.md"),
    ("P153", "FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md", "FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT_ZH.md"),
    ("P154", "PUSH_READINESS_REPORT.md", "PUSH_READINESS_REPORT_ZH.md"),
)


def build_pre_rebuild_verification_report(lang: str = "en") -> dict[str, Any]:
    _validate_lang(lang)
    current_artifacts = _artifact_status(CURRENT_REQUIRED_ARTIFACTS, required=True)
    future_artifacts = _artifact_status(FUTURE_ARTIFACTS, required=False)
    markdown_link_status = _markdown_link_status()
    forbidden_pattern_status = _forbidden_pattern_status()
    phase_index_status = _phase_index_status()
    index_status = _index_status()
    readme_status = _readme_status()
    read_only_cli_status = _read_only_cli_status(lang)
    boundary_status = _boundary_status(read_only_cli_status)
    ctm_temporal_status = _topic_boundary_status(
        "ctm_temporal_status",
        (
            "CTM_TEMPORAL_DYNAMICS_RFC.md",
            "CTM_TEMPORAL_CONTEXT_PACK_RFC.md",
            "TEMPORAL_COHERENCE_EVALUATION_PLAN.md",
            "THOUGHT_TRACE_STORAGE_POLICY_RFC.md",
        ),
        ("ctm_runtime_enabled", "temporal_event_executed"),
    )
    tool_first_status = _topic_boundary_status(
        "tool_first_status",
        (
            "TOOL_FIRST_SELF_EVOLUTION_RFC.md",
            "CAPABILITY_EVOLUTION_BOUNDARY_RFC.md",
            "CAPABILITY_CONTEXT_PACK_RFC.md",
        ),
        ("tool_execution_enabled", "auto_tool_promotion_enabled", "policy_executor_enabled"),
    )

    gate_results = [
        _gate("required_artifacts", _all_present(current_artifacts), _count_missing(current_artifacts), "P112-P151 artifacts exist."),
        _gate("phase_index_status", phase_index_status["status"] == "pass", len(phase_index_status["issues"]), "PHASE_INDEX / ZH reaches P151."),
        _gate("index_status", index_status["status"] == "pass", len(index_status["issues"]), "RFC_INDEX / ZH includes P151 artifacts."),
        _gate("readme_status", readme_status["status"] == "pass", len(readme_status["issues"]), "README / ZH reflects P151."),
        _gate("markdown_link_status", markdown_link_status["status"] == "pass", len(markdown_link_status["issues"]), "Local Markdown links resolve."),
        _gate("forbidden_pattern_status", forbidden_pattern_status["status"] == "pass", len(forbidden_pattern_status["matches"]), "Active forbidden true flags are absent."),
        _gate("read_only_cli_status", read_only_cli_status["status"] == "pass", len(read_only_cli_status["issues"]), "Read-only report builders still produce safe reports."),
        _gate("boundary_status", boundary_status["status"] == "pass", len(boundary_status["issues"]), "Forbidden boundaries remain disabled."),
        _gate("ctm_temporal_status", ctm_temporal_status["status"] == "pass", len(ctm_temporal_status["issues"]), "CTM work remains symbolic and review-only."),
        _gate("tool_first_status", tool_first_status["status"] == "pass", len(tool_first_status["issues"]), "Tool-First work remains candidate/evidence/review-only."),
    ]
    blocking_gate_failures = [gate for gate in gate_results if gate["status"] != "pass"]

    report = {
        "report_id": "pre_rebuild_verification_suite_v0.1",
        "generated_by": "pre-rebuild-verification",
        "lang": lang,
        "current_phase": CURRENT_PHASE,
        "scope": "read_only_local_pre_rebuild_verification",
        "verification_summary": _verification_summary(lang, blocking_gate_failures),
        "gate_results": gate_results,
        "required_artifacts": current_artifacts,
        "future_artifacts": future_artifacts,
        "phase_index_status": phase_index_status,
        "index_status": index_status,
        "readme_status": readme_status,
        "forbidden_pattern_status": forbidden_pattern_status,
        "markdown_link_status": markdown_link_status,
        "read_only_cli_status": read_only_cli_status,
        "boundary_status": boundary_status,
        "ctm_temporal_status": ctm_temporal_status,
        "tool_first_status": tool_first_status,
        "verification_commands_for_p152": _verification_commands(),
        "non_execution_invariants": dict(NON_EXECUTION_INVARIANTS),
    }
    report.update(NON_EXECUTION_INVARIANTS)
    return report


def render_pre_rebuild_verification_report(report: dict[str, Any], output_format: str) -> str:
    if output_format not in OUTPUT_FORMATS:
        raise ValueError("output_format must be 'markdown' or 'json'")
    if output_format == "json":
        return json.dumps(report, ensure_ascii=False, indent=2)
    return _render_markdown(report)


def _verification_summary(lang: str, blocking_gate_failures: list[dict[str, Any]]) -> dict[str, Any]:
    if lang == "zh":
        return {
            "display_name": "重构前验证摘要",
            "status": "pass" if not blocking_gate_failures else "blocked",
            "ready_for_final_verification_report": not blocking_gate_failures,
            "ready_for_rebuild": False,
            "summary": "P151 只实现本地只读验证套件；它可以支持 P152 出具验证报告，但不启动重构。",
            "next_step": "如果本报告保持 pass，下一步是 P152 Verification Report，而不是 rebuild。",
            "blocked_reason": "" if not blocking_gate_failures else "一个或多个阻塞 gate 未通过。",
        }
    return {
        "display_name": "Pre-Rebuild Verification Summary",
        "status": "pass" if not blocking_gate_failures else "blocked",
        "ready_for_final_verification_report": not blocking_gate_failures,
        "ready_for_rebuild": False,
        "summary": "P151 implements the local read-only verification suite; it can support P152 reporting, but it does not start rebuild.",
        "next_step": "If this report remains pass, the next step is P152 Verification Report, not rebuild.",
        "blocked_reason": "" if not blocking_gate_failures else "One or more blocking gates did not pass.",
    }


def _artifact_status(artifacts: tuple[tuple[str, str, str], ...], required: bool) -> list[dict[str, Any]]:
    rows = []
    for phase, en_path, zh_path in artifacts:
        en_exists = (REPO_ROOT / en_path).exists()
        zh_exists = (REPO_ROOT / zh_path).exists()
        rows.append(
            {
                "phase": phase,
                "en_path": en_path,
                "zh_path": zh_path,
                "en_exists": en_exists,
                "zh_exists": zh_exists,
                "required_now": required,
                "status": "present" if en_exists and zh_exists else ("missing" if required else "pending_future_phase"),
            }
        )
    return rows


def _phase_index_status() -> dict[str, Any]:
    paths = ("PHASE_INDEX.md", "PHASE_INDEX_ZH.md")
    issues = []
    for path in paths:
        text = _read_repo_text(path)
        if "| P151 |" not in text:
            issues.append({"path": path, "issue": "missing_P151_row"})
        if "Pre-Rebuild Verification" not in text and "重构前验证" not in text:
            issues.append({"path": path, "issue": "missing_pre_rebuild_verification_label"})
    return {"status": "pass" if not issues else "fail", "issues": issues, "paths": list(paths)}


def _index_status() -> dict[str, Any]:
    paths = ("RFC_INDEX.md", "RFC_INDEX_ZH.md")
    required_tokens = ("PRE_REBUILD_VERIFICATION_SUITE.md", "PRE_REBUILD_VERIFICATION_SUITE_ZH.md")
    issues = []
    for path in paths:
        text = _read_repo_text(path)
        for token in required_tokens:
            if token not in text:
                issues.append({"path": path, "issue": "missing_token", "token": token})
    return {"status": "pass" if not issues else "fail", "issues": issues, "paths": list(paths)}


def _readme_status() -> dict[str, Any]:
    paths = ("README.md", "README_ZH.md")
    issues = []
    for path in paths:
        text = _read_repo_text(path)
        if "P151" not in text:
            issues.append({"path": path, "issue": "missing_P151_status"})
        if "pre-rebuild-verification" not in text:
            issues.append({"path": path, "issue": "missing_pre_rebuild_verification_command"})
    return {"status": "pass" if not issues else "fail", "issues": issues, "paths": list(paths)}


def _markdown_link_status() -> dict[str, Any]:
    issues = []
    checked_files = 0
    checked_links = 0
    for path in _iter_text_files(".md"):
        checked_files += 1
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
            target = match.group(1).strip()
            if _skip_markdown_link(target):
                continue
            checked_links += 1
            target_path = target.split("#", 1)[0]
            target_path = target_path.strip("<>")
            if not target_path:
                continue
            resolved = (path.parent / target_path).resolve()
            try:
                resolved.relative_to(REPO_ROOT)
            except ValueError:
                issues.append({"path": _rel(path), "target": target, "issue": "link_escapes_repo"})
                continue
            if not resolved.exists():
                issues.append({"path": _rel(path), "target": target, "issue": "missing_local_link_target"})
    return {
        "status": "pass" if not issues else "fail",
        "checked_files": checked_files,
        "checked_links": checked_links,
        "issues": issues,
    }


def _forbidden_pattern_status() -> dict[str, Any]:
    matches = []
    patterns = [(flag, re.compile(rf"{re.escape(flag)}\s*:\s*true", re.IGNORECASE)) for flag in FORBIDDEN_TRUE_FLAGS]
    for path in _iter_text_files():
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_number, line in enumerate(text.splitlines(), start=1):
            for flag, pattern in patterns:
                if pattern.search(line):
                    matches.append({"path": _rel(path), "line": line_number, "flag": flag})
    return {
        "status": "pass" if not matches else "fail",
        "checked_flags": list(FORBIDDEN_TRUE_FLAGS),
        "matches": matches,
    }


def _read_only_cli_status(lang: str) -> dict[str, Any]:
    issues = []
    observatory = build_observatory_report(lang=lang)
    source_inventory = build_source_inventory_report(lang=lang)
    harness_en = build_harness_dry_run_report(
        user_message="event replay payload diff reconstruction verification",
        lang="en",
    )
    harness_zh = build_harness_dry_run_report(
        user_message="重构前验证：回放和重建检查",
        lang="zh",
    )

    if observatory.get("report_id") != "foundation_observatory_report_v0.3":
        issues.append({"report": "foundation_observatory_report", "issue": "unexpected_report_id"})
    if source_inventory.get("safety_status") != "pass":
        issues.append({"report": "harness_source_inventory", "issue": "source_inventory_safety_not_pass"})
    if harness_en.get("input_pressure_type") != "reconstruction_pressure":
        issues.append({"report": "harness_dry_run_en", "issue": "unexpected_pressure_type"})
    if harness_zh.get("input_pressure_type") != "reconstruction_pressure":
        issues.append({"report": "harness_dry_run_zh", "issue": "unexpected_pressure_type"})
    for name, report in (
        ("observatory", observatory),
        ("source_inventory", source_inventory),
        ("harness_en", harness_en),
        ("harness_zh", harness_zh),
    ):
        _check_false_boundaries(name, report, issues)

    return {
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "checked_reports": [
            "foundation_observatory_report",
            "harness_source_inventory",
            "harness_dry_run_en",
            "harness_dry_run_zh",
        ],
        "read_only_builder_mode": True,
        "subprocess_executed": False,
        "external_io_performed": False,
    }


def _boundary_status(read_only_cli_status: dict[str, Any]) -> dict[str, Any]:
    issues = list(read_only_cli_status["issues"])
    for flag, expected in NON_EXECUTION_INVARIANTS.items():
        if expected is False and flag.endswith(("enabled", "mutated", "executed", "required", "started")):
            continue
    return {
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "disabled_flags": [flag for flag, value in NON_EXECUTION_INVARIANTS.items() if value is False],
        "true_invariants": [flag for flag, value in NON_EXECUTION_INVARIANTS.items() if value is True],
    }


def _topic_boundary_status(
    status_id: str,
    paths: tuple[str, ...],
    disabled_flags: tuple[str, ...],
) -> dict[str, Any]:
    issues = []
    for path in paths:
        if not (REPO_ROOT / path).exists():
            issues.append({"path": path, "issue": "missing_topic_artifact"})
    for flag in disabled_flags:
        if NON_EXECUTION_INVARIANTS.get(flag) is not False:
            issues.append({"flag": flag, "issue": "flag_not_disabled"})
    return {
        "status_id": status_id,
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "checked_paths": list(paths),
        "disabled_flags": list(disabled_flags),
    }


def _check_false_boundaries(name: str, report: dict[str, Any], issues: list[dict[str, Any]]) -> None:
    for flag in FORBIDDEN_TRUE_FLAGS:
        if report.get(flag) is True:
            issues.append({"report": name, "flag": flag, "issue": "forbidden_flag_enabled"})
        invariants = report.get("non_execution_invariants", {})
        if isinstance(invariants, dict) and invariants.get(flag) is True:
            issues.append({"report": name, "flag": flag, "issue": "forbidden_invariant_enabled"})


def _verification_commands() -> list[str]:
    return [
        "git status --short",
        "git branch --show-current",
        "git diff --check",
        "python3 -m unittest",
        "python3 -m one_core.cli pre-rebuild-verification --format json --lang en",
        "python3 -m one_core.cli pre-rebuild-verification --format json --lang zh",
        "python3 -m one_core.cli foundation-observatory-report --format json --lang en",
        "python3 -m one_core.cli foundation-observatory-report --format json --lang zh",
        "python3 -m one_core.cli harness-source-inventory --format json --lang en",
        "python3 -m one_core.cli harness-source-inventory --format json --lang zh",
        'python3 -m one_core.cli harness-dry-run --input "event replay payload diff reconstruction verification" --format json --lang en',
        'python3 -m one_core.cli harness-dry-run --input "重构前验证：回放和重建检查" --format json --lang zh',
    ]


def _gate(name: str, passed: bool, issue_count: int, summary: str) -> dict[str, Any]:
    return {
        "gate": name,
        "status": "pass" if passed else "fail",
        "issue_count": issue_count,
        "summary": summary,
    }


def _all_present(rows: list[dict[str, Any]]) -> bool:
    return all(row["status"] == "present" for row in rows)


def _count_missing(rows: list[dict[str, Any]]) -> int:
    return sum(1 for row in rows if row["status"] != "present")


def _read_repo_text(path: str) -> str:
    full_path = REPO_ROOT / path
    return full_path.read_text(encoding="utf-8") if full_path.exists() else ""


def _iter_text_files(suffix: str | None = None):
    excluded_dirs = {
        ".git",
        ".agents",
        ".codex",
        "__pycache__",
        ".pytest_cache",
        "work",
        "outputs",
        ".mypy_cache",
        ".ruff_cache",
    }
    for path in REPO_ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in excluded_dirs for part in path.relative_to(REPO_ROOT).parts):
            continue
        if suffix and path.suffix != suffix:
            continue
        if suffix is None and path.suffix not in {".md", ".py", ".json", ".yaml", ".yml", ".service"}:
            continue
        yield path


def _skip_markdown_link(target: str) -> bool:
    lower = target.lower()
    return (
        not target
        or target.startswith("#")
        or lower.startswith("http://")
        or lower.startswith("https://")
        or lower.startswith("mailto:")
        or lower.startswith("file:")
    )


def _rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


def _render_markdown(report: dict[str, Any]) -> str:
    zh = report.get("lang") == "zh"
    title = "重构前验证套件报告" if zh else "Pre-Rebuild Verification Suite Report"
    lines = [
        f"# {title}",
        "",
        f"`report_id`: `{report['report_id']}`",
        f"`current_phase`: `{report['current_phase']}`",
        f"`scope`: `{report['scope']}`",
        "",
        "## Verification Summary" if not zh else "## Verification Summary / 验证摘要",
        "",
    ]
    summary = report["verification_summary"]
    for key in ("display_name", "status", "ready_for_final_verification_report", "ready_for_rebuild", "summary", "next_step", "blocked_reason"):
        lines.append(f"- {key}: {summary[key]}")

    lines.extend([
        "",
        "## Gate Results" if not zh else "## Gate Results / Gate 结果",
        "",
        "| gate | status | issue_count | summary |",
        "| --- | --- | --- | --- |",
    ])
    for row in report["gate_results"]:
        lines.append(f"| `{row['gate']}` | {row['status']} | {row['issue_count']} | {_escape(row['summary'])} |")

    lines.extend([
        "",
        "## Required Artifacts" if not zh else "## Required Artifacts / 必需文档",
        "",
        "| phase | en_path | zh_path | status |",
        "| --- | --- | --- | --- |",
    ])
    for row in report["required_artifacts"]:
        lines.append(f"| {row['phase']} | {row['en_path']} | {row['zh_path']} | {row['status']} |")

    lines.extend([
        "",
        "## Future Artifacts" if not zh else "## Future Artifacts / 后续文档",
        "",
        "| phase | en_path | zh_path | status |",
        "| --- | --- | --- | --- |",
    ])
    for row in report["future_artifacts"]:
        lines.append(f"| {row['phase']} | {row['en_path']} | {row['zh_path']} | {row['status']} |")

    lines.extend([
        "",
        "## Check Status" if not zh else "## Check Status / 检查状态",
        "",
        f"- markdown_link_status: {report['markdown_link_status']['status']} ({len(report['markdown_link_status']['issues'])} issues)",
        f"- forbidden_pattern_status: {report['forbidden_pattern_status']['status']} ({len(report['forbidden_pattern_status']['matches'])} matches)",
        f"- phase_index_status: {report['phase_index_status']['status']} ({len(report['phase_index_status']['issues'])} issues)",
        f"- index_status: {report['index_status']['status']} ({len(report['index_status']['issues'])} issues)",
        f"- readme_status: {report['readme_status']['status']} ({len(report['readme_status']['issues'])} issues)",
        f"- read_only_cli_status: {report['read_only_cli_status']['status']} ({len(report['read_only_cli_status']['issues'])} issues)",
        f"- boundary_status: {report['boundary_status']['status']} ({len(report['boundary_status']['issues'])} issues)",
        f"- ctm_temporal_status: {report['ctm_temporal_status']['status']} ({len(report['ctm_temporal_status']['issues'])} issues)",
        f"- tool_first_status: {report['tool_first_status']['status']} ({len(report['tool_first_status']['issues'])} issues)",
        "",
        "## Verification Commands For P152" if not zh else "## Verification Commands For P152 / P152 验证命令",
        "",
    ])
    for command in report["verification_commands_for_p152"]:
        lines.append(f"- `{command}`")

    lines.extend([
        "",
        "## Non-Execution Invariants" if not zh else "## Non-Execution Invariants / 非执行边界",
        "",
    ])
    for key, value in report["non_execution_invariants"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    return "\n".join(lines)


def _escape(value: str) -> str:
    return value.replace("|", "\\|")


def _validate_lang(lang: str) -> None:
    if lang not in LANGUAGES:
        raise ValueError("lang must be 'en' or 'zh'")
