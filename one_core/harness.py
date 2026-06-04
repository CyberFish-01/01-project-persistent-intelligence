from __future__ import annotations

import json
from typing import Any

from .observatory import build_observatory_report


PRIVACY_SCOPES = ("local", "private", "public")

BOUNDARY_MONITOR = {
    "identity_core_mutated": False,
    "memory_rewrite_executed": False,
    "recall_mutation_executed": False,
    "growth_engine_executed": False,
    "temporal_event_executed": False,
    "tool_execution_enabled": False,
    "policy_executor_enabled": False,
    "companion_feature_enabled": False,
    "adapter_integration_required": False,
    "harness_write_enabled": False,
    "state_unchanged": True,
}

NON_EXECUTION_INVARIANTS = {
    "dry_run": True,
    "no_write": True,
    "execution_prohibited": True,
    "state_unchanged": True,
    "candidate_is_not_promotion": True,
    "preview_is_not_persistence": True,
}

FORBIDDEN_BOUNDARY_KEYS = (
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
)


def build_harness_dry_run_report(
    *,
    user_message: str,
    session_id: str = "demo-session",
    actor_id: str = "founder",
    lang: str = "en",
    privacy_scope: str = "local",
    no_write: bool = True,
) -> dict[str, Any]:
    if lang not in {"en", "zh"}:
        raise ValueError("lang must be 'en' or 'zh'")
    if privacy_scope not in PRIVACY_SCOPES:
        raise ValueError("privacy_scope must be one of: local, private, public")
    if not user_message.strip():
        raise ValueError("user_message must not be empty")
    if no_write is not True:
        raise ValueError("harness-dry-run requires --no-write=true")

    observatory_report = build_observatory_report(lang=lang)
    report = {
        "report_id": "minimal_cli_harness_dry_run_v0.1",
        "generated_by": "harness-dry-run",
        "lang": lang,
        "harness_scope": "read_only_dry_run_preview",
        "intake_preview": _intake_preview(
            user_message=user_message,
            session_id=session_id,
            actor_id=actor_id,
            privacy_scope=privacy_scope,
        ),
        "context_package_preview": _context_package_preview(lang, privacy_scope),
        "candidate_preview": _candidate_preview(lang, user_message),
        "review_queue_preview": _review_queue_preview(lang),
        "boundary_monitor": dict(BOUNDARY_MONITOR),
        "observatory_snapshot": _observatory_snapshot(lang, observatory_report),
        "non_execution_invariants": dict(NON_EXECUTION_INVARIANTS),
    }
    report.update(BOUNDARY_MONITOR)
    report.update(NON_EXECUTION_INVARIANTS)
    return report


def render_harness_dry_run_report(report: dict[str, Any], output_format: str) -> str:
    if output_format == "json":
        return json.dumps(report, ensure_ascii=False, indent=2)
    if output_format == "markdown":
        return _render_markdown(report)
    raise ValueError("output_format must be 'markdown' or 'json'")


def _intake_preview(
    *,
    user_message: str,
    session_id: str,
    actor_id: str,
    privacy_scope: str,
) -> dict[str, Any]:
    return {
        "user_message": user_message,
        "session_id": session_id,
        "actor_id": actor_id,
        "privacy_scope": privacy_scope,
        "platform_ref": "cli_dry_run",
        "no_write": True,
    }


def _context_package_preview(lang: str, privacy_scope: str) -> dict[str, Any]:
    if lang == "zh":
        selection_reason = "使用静态地基引用展示处理路径，不执行真实检索。"
        source_attribution = "静态来源：FOUNDATION、PHASE_INDEX、OPEN_QUESTIONS、RFC_INDEX、GLOSSARY。"
        privacy_note = "private 输入只显示边界和类别，不扩展内容。" if privacy_scope == "private" else "输入保持本地 dry-run，不写入 state。"
        risk_flags = [
            "preview_only",
            "no_retrieval_execution",
            "no_prompt_construction",
            "no_state_write",
            privacy_note,
        ]
        return {
            "identity_refs": ["身份核心", "Identity Gate", "Continuity = State Transfer"],
            "memory_refs": ["带状态的记忆", "Memory Lifecycle", "Dream proposes, review decides"],
            "claim_refs": ["说法证据图", "Claim review remains review-only"],
            "task_refs": ["任务中心", "当前任务只能 preview，不能自动执行"],
            "governance_refs": ["跨层审查区", "Boundary Test Matrix", "P99 no-write harness plan"],
            "selection_reason": selection_reason,
            "source_attribution": source_attribution,
            "risk_flags": risk_flags,
        }

    privacy_note = "Private input shows boundary and category only." if privacy_scope == "private" else "Input remains local dry-run and is not written to state."
    return {
        "identity_refs": ["Identity Core", "Identity Gate", "Continuity = State Transfer"],
        "memory_refs": ["Stateful Memory", "Memory Lifecycle", "Dream proposes, review decides"],
        "claim_refs": ["Claim Graph", "Claim review remains review-only"],
        "task_refs": ["Task Hub", "Task context can be previewed but not auto-executed"],
        "governance_refs": ["Governance Surface", "Boundary Test Matrix", "P99 no-write harness plan"],
        "selection_reason": "Use static foundation references to show the processing path without executing retrieval.",
        "source_attribution": "Static sources: FOUNDATION, PHASE_INDEX, OPEN_QUESTIONS, RFC_INDEX, GLOSSARY.",
        "risk_flags": [
            "preview_only",
            "no_retrieval_execution",
            "no_prompt_construction",
            "no_state_write",
            privacy_note,
        ],
    }


def _candidate_preview(lang: str, user_message: str) -> list[dict[str, Any]]:
    labels = {
        "memory_candidate": (
            "Memory candidate",
            "记忆候选",
            "The input may be relevant to future memory review.",
            "输入可能与未来记忆审查有关。",
        ),
        "claim_candidate": (
            "Claim candidate",
            "说法候选",
            "The input may support, weaken, or conflict with a claim.",
            "输入可能支持、削弱或冲突于某个说法。",
        ),
        "growth_candidate_review": (
            "Growth candidate review",
            "成长提案审查",
            "The input may be relevant to growth review, not growth promotion.",
            "输入可能与成长审查有关，但不是成长提升。",
        ),
        "meaning_shift_candidate": (
            "Meaning-shift candidate",
            "意义变化候选",
            "The input may change how an existing memory or claim is interpreted.",
            "输入可能影响既有记忆或说法的解释方式。",
        ),
        "recall_event_candidate": (
            "Recall-event candidate",
            "回忆事件候选",
            "The input may raise a future recall-write policy question.",
            "输入可能提出未来 recall-write policy question。",
        ),
        "task_update_candidate": (
            "Task-update candidate",
            "任务更新候选",
            "The input may suggest a future task update for review.",
            "输入可能提示未来任务更新审查。",
        ),
    }
    preview_excerpt = user_message.strip()
    if len(preview_excerpt) > 120:
        preview_excerpt = preview_excerpt[:117] + "..."

    candidates = []
    for candidate_type, (en_name, zh_name, en_reason, zh_reason) in labels.items():
        candidates.append(
            {
                "candidate_type": candidate_type,
                "display_name": zh_name if lang == "zh" else en_name,
                "preview_reason": zh_reason if lang == "zh" else en_reason,
                "input_excerpt": preview_excerpt,
                "preview_only": True,
                "promoted": False,
                "persisted": False,
            }
        )
    return candidates


def _review_queue_preview(lang: str) -> list[dict[str, Any]]:
    gates = [
        ("memory_review", "Memory Review", "记忆审查", "memory_candidate"),
        ("claim_review", "Claim Review", "说法审查", "claim_candidate"),
        ("growth_candidate_review", "Growth Candidate Review", "成长提案审查", "growth_candidate_review"),
        ("identity_high_gate", "Identity High Gate", "身份高门槛", "meaning_shift_candidate"),
        ("task_review", "Task Review", "任务审查", "task_update_candidate"),
    ]
    if lang == "zh":
        return [
            {
                "review_gate": gate,
                "display_name": zh_name,
                "candidate_type": candidate_type,
                "gate_status": "preview_only",
                "lifecycle_created": False,
                "execution_allowed": False,
                "reason": "仅展示未来可能进入的审查门，不创建真实 lifecycle。",
            }
            for gate, _en_name, zh_name, candidate_type in gates
        ]
    return [
        {
            "review_gate": gate,
            "display_name": en_name,
            "candidate_type": candidate_type,
            "gate_status": "preview_only",
            "lifecycle_created": False,
            "execution_allowed": False,
            "reason": "Shows the possible future review gate without creating a lifecycle.",
        }
        for gate, en_name, _zh_name, candidate_type in gates
    ]


def _observatory_snapshot(lang: str, observatory_report: dict[str, Any]) -> dict[str, Any]:
    risks = observatory_report["risk_heatmap"][:3]
    if lang == "zh":
        return {
            "current_phase": "P100 最小 CLI 试验台 dry-run",
            "readiness_summary": "当前只允许本地只读 preview；观察台、边界和候选项可见，但不执行。",
            "highest_risks": [risk["display_name"] for risk in risks],
            "recommended_next_step": "先审查 dry-run 输出是否清楚且无写入，再决定是否进入 P101。",
        }
    return {
        "current_phase": "P100 minimal CLI harness dry-run",
        "readiness_summary": "Only local read-only preview is allowed; observatory, boundaries, and candidates are visible but non-executing.",
        "highest_risks": [risk["display_name"] for risk in risks],
        "recommended_next_step": "Review whether dry-run output is clear and no-write before deciding on P101.",
    }


def _render_markdown(report: dict[str, Any]) -> str:
    zh = report["lang"] == "zh"
    title = "# 最小 CLI 试验台 Dry-Run 报告" if zh else "# Minimal CLI Harness Dry-Run Report"
    lines = [
        title,
        "",
        f"`report_id`: `{report['report_id']}`",
        f"`lang`: `{report['lang']}`",
        f"`harness_scope`: `{report['harness_scope']}`",
        "",
    ]
    lines.extend(_render_object_section("intake_preview", "输入预览", report["intake_preview"], zh))
    lines.extend(_render_object_section("context_package_preview", "上下文包预览", report["context_package_preview"], zh))
    lines.extend(_render_list_section("candidate_preview", "候选项预览", report["candidate_preview"], zh))
    lines.extend(_render_list_section("review_queue_preview", "审查队列预览", report["review_queue_preview"], zh))
    lines.extend(_render_object_section("boundary_monitor", "边界监视器", report["boundary_monitor"], zh))
    lines.extend(_render_object_section("observatory_snapshot", "观察台快照", report["observatory_snapshot"], zh))
    lines.extend(_render_object_section("non_execution_invariants", "非执行边界", report["non_execution_invariants"], zh))
    return "\n".join(lines)


def _render_object_section(
    internal_key: str,
    zh_name: str,
    data: dict[str, Any],
    zh: bool,
) -> list[str]:
    heading = f"## {internal_key} / {zh_name}" if zh else f"## {internal_key}"
    lines = [heading, ""]
    for key, value in data.items():
        lines.append(f"- {key}: {_cell(value)}")
    lines.append("")
    return lines


def _render_list_section(
    internal_key: str,
    zh_name: str,
    rows: list[dict[str, Any]],
    zh: bool,
) -> list[str]:
    heading = f"## {internal_key} / {zh_name}" if zh else f"## {internal_key}"
    if not rows:
        return [heading, "", "_empty_", ""]
    keys = list(rows[0].keys())
    lines = [heading, "", "| " + " | ".join(keys) + " |", "| " + " | ".join(["---"] * len(keys)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(row[key]) for key in keys) + " |")
    lines.append("")
    return lines


def _cell(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, list):
        return ", ".join(_cell(item) for item in value)
    if isinstance(value, dict):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value).replace("|", "\\|")
