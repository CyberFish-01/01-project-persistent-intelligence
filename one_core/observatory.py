from __future__ import annotations

import json
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]

SOURCE_DOCUMENTS = [
    ("PHASE_INDEX.md", "PHASE_INDEX_ZH.md"),
    ("CONCEPT_MAP.md", "CONCEPT_MAP_ZH.md"),
    ("FOUNDATION_STATUS.md", "FOUNDATION_STATUS_ZH.md"),
    ("OPEN_QUESTIONS.md", "OPEN_QUESTIONS_ZH.md"),
    ("RISK_REGISTER.md", "RISK_REGISTER_ZH.md"),
    ("ARCHITECTURE_BOUNDARIES.md", "ARCHITECTURE_BOUNDARIES_ZH.md"),
    ("RFC_INDEX.md", "RFC_INDEX_ZH.md"),
    ("VISUAL_NAMING_GUIDE.md", "VISUAL_NAMING_GUIDE_ZH.md"),
    ("FOUNDATION_OBSERVATORY_REPORT.md", "FOUNDATION_OBSERVATORY_REPORT_ZH.md"),
    ("MINIMAL_OBSERVATORY_CLI_PLAN.md", "MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md"),
]

READINESS_CATEGORIES = [
    "implemented",
    "report_only",
    "rfc_only",
    "evaluation_only",
    "future_direction",
    "blocked",
    "dangerous_if_early",
]

NON_EXECUTION_INVARIANTS = {
    "observatory_report_only": True,
    "execution_prohibited": True,
    "state_unchanged": True,
    "identity_core_mutated": False,
    "memory_rewrite_executed": False,
    "recall_mutation_executed": False,
    "growth_engine_executed": False,
    "temporal_event_executed": False,
    "tool_execution_enabled": False,
    "policy_executor_enabled": False,
    "companion_feature_enabled": False,
    "adapter_integration_required": False,
    "observability_executor_enabled": False,
}


def build_observatory_report(lang: str = "en") -> dict[str, Any]:
    if lang not in {"en", "zh"}:
        raise ValueError("lang must be 'en' or 'zh'")

    report = {
        "report_id": "foundation_observatory_report_v0.2",
        "generated_by": "foundation-observatory-report",
        "lang": lang,
        "observatory_scope": "read_only_static_report",
        "source_documents": [_source_document(en, zh, lang) for en, zh in SOURCE_DOCUMENTS],
        "readiness_categories": READINESS_CATEGORIES,
        "founder_snapshot": _founder_snapshot(lang),
        "main_axes_map": _main_axes_map(lang),
        "readiness_matrix": _readiness_matrix(lang),
        "boundary_status": _boundary_status(lang),
        "risk_heatmap": _risk_heatmap(lang),
        "next_step_recommendations": _next_steps(lang),
        "what_not_to_build_yet": _what_not_to_build_yet(lang),
        "non_execution_invariants": dict(NON_EXECUTION_INVARIANTS),
    }
    report.update(NON_EXECUTION_INVARIANTS)
    return report


def render_observatory_report(report: dict[str, Any], output_format: str) -> str:
    if output_format == "json":
        return json.dumps(report, ensure_ascii=False, indent=2)
    if output_format == "markdown":
        return _render_markdown(report)
    raise ValueError("output_format must be 'markdown' or 'json'")


def _source_document(en_path: str, zh_path: str, lang: str) -> dict[str, Any]:
    path = zh_path if lang == "zh" else en_path
    full_path = REPO_ROOT / path
    text = full_path.read_text(encoding="utf-8") if full_path.exists() else ""
    heading = ""
    for line in text.splitlines():
        if line.startswith("# "):
            heading = line[2:].strip()
            break
    return {
        "path": path,
        "paired_path": en_path if lang == "zh" else zh_path,
        "exists": full_path.exists(),
        "heading": heading,
        "read_mode": "read_only",
    }


def _founder_snapshot(lang: str) -> dict[str, Any]:
    if lang == "zh":
        return {
            "display_name": "创始人快照",
            "internal_key": "founder_snapshot",
            "summary": "01 Core 当前是 Persistent Intelligence 的连续性地基，不是产品层或自动执行系统。",
            "current_state": [
                "已有本地 01 Core prototype 和大量 foundation documents。",
                "当前重点是可见性、边界和只读观察，不是增加能力。",
                "P96 CLI 只生成报告，不修改 state。",
            ],
            "why_observatory_next": "观察台让创始人一眼看清已实现、报告层、RFC 层、未来方向和 blocked 工作。",
        }
    return {
        "display_name": "Founder Snapshot",
        "internal_key": "founder_snapshot",
        "summary": "01 Core is currently a continuity foundation for Persistent Intelligence, not a product layer or automatic executor.",
        "current_state": [
            "A local 01 Core prototype and a broad foundation document set exist.",
            "The current focus is visibility, boundaries, and read-only observation, not more power.",
            "The P96 CLI generates reports only and does not mutate state.",
        ],
        "why_observatory_next": "The observatory lets the founder see what is implemented, report-only, RFC-only, future direction, and blocked.",
    }


def _main_axes_map(lang: str) -> list[dict[str, Any]]:
    if lang == "zh":
        return [
            _axis("连续性轴", "Identity / State / Event / Reconstruction", "用身份、状态、事件和重建证据保护连续性。", "report_only", "medium", "继续保持 audit/replay 可见，不执行 reducer。"),
            _axis("成长轴", "Stateful Memory / Meaning Shift / Growth Candidate Review", "解释记忆意义变化，并把成长保持为候选审查。", "rfc_only", "high", "不要把 candidate 显示成 promoted growth。"),
            _axis("时间轴", "Temporal Awareness / CTM-inspired Temporal Dynamics", "研究 elapsed time 和 temporal coherence 的未来 review 价值。", "rfc_only", "high", "保持 symbolic/evaluation-only，不进入 temporal runtime。"),
            _axis("能力轴", "Tool-First Self-Evolution / Capability Evolution", "区分能力改进、工具验证和主体成长。", "rfc_only", "high", "先定义 evidence 和 authorization 边界，不执行工具。"),
            _axis("交互试验轴", "Thin Interaction Harness", "规划未来 preview-only 的本地交互试验面。", "rfc_only", "medium", "保持 fixture-first 和 no-write。"),
            _axis("观察层", "Foundation Observatory", "用 founder-facing 报告展示状态、风险和边界。", "implemented", "medium", "保持 read-only CLI，不变成 dashboard runtime。"),
        ]
    return [
        _axis("Continuity Axis", "Identity / State / Event / Reconstruction", "Protects continuity through identity, state, event evidence, and reconstruction readiness.", "report_only", "medium", "Keep audit/replay visible; do not execute reducers."),
        _axis("Growth Axis", "Stateful Memory / Meaning Shift / Growth Candidate Review", "Explains memory meaning shifts and keeps growth as candidate review.", "rfc_only", "high", "Do not show candidates as promoted growth."),
        _axis("Temporal Axis", "Temporal Awareness / CTM-inspired Temporal Dynamics", "Studies elapsed time and temporal coherence as future review evidence.", "rfc_only", "high", "Keep symbolic/evaluation-only; do not enter temporal runtime."),
        _axis("Capability Axis", "Tool-First Self-Evolution / Capability Evolution", "Separates capability improvement, tool verification, and subject growth.", "rfc_only", "high", "Define evidence and authorization boundaries before tool execution."),
        _axis("Interaction Trial Axis", "Thin Interaction Harness", "Plans a future preview-only local interaction surface.", "rfc_only", "medium", "Keep fixture-first and no-write."),
        _axis("Observatory Layer", "Foundation Observatory", "Shows status, risks, and boundaries through founder-facing reports.", "implemented", "medium", "Keep the CLI read-only and out of dashboard runtime."),
    ]


def _axis(
    display_name: str,
    internal_key: str,
    explanation: str,
    status: str,
    risk: str,
    next_action: str,
) -> dict[str, str]:
    return {
        "display_name": display_name,
        "internal_key": internal_key,
        "explanation": explanation,
        "status": status,
        "risk": risk,
        "next_action": next_action,
    }


def _readiness_matrix(lang: str) -> list[dict[str, Any]]:
    rows = [
        ("身份核心", "Identity Core", "report_only", "high", "Keep protected behind Identity Gate.", "继续由 Identity Gate 保护。"),
        ("状态传递", "State Transfer", "report_only", "medium", "Keep as continuity proposition, not retrieval.", "继续作为 continuity 命题，不降级为 retrieval。"),
        ("事件日志", "Event Log", "implemented", "medium", "Keep auditable and append-only.", "继续保持可审计和 append-only。"),
        ("回放检查", "Replay", "report_only", "medium", "Report readiness without rebuilding state.", "只报告 readiness，不重建 state。"),
        ("状态重建", "Reconstruction", "rfc_only", "high", "Finish contracts before reducers.", "先完成 contracts，再讨论 reducers。"),
        ("信念证据图", "Claim Graph", "report_only", "medium", "Do not absorb every meaning shift.", "不要吞掉所有 meaning shift。"),
        ("任务中心", "Task Hub", "report_only", "medium", "Do not replace governance review.", "不要替代 governance review。"),
        ("状态化记忆", "Stateful Memory", "rfc_only", "high", "Keep semantics separate from memory rewrite.", "保持 semantics 与 memory rewrite 分离。"),
        ("成长候选审查", "Growth Candidate Review", "rfc_only", "high", "Candidate is not promoted growth.", "candidate 不是 promoted growth。"),
        ("时间感知", "Temporal Awareness", "rfc_only", "high", "No temporal runtime or event writes.", "不做 temporal runtime 或 event writes。"),
        ("时间一致性", "Temporal Coherence", "evaluation_only", "high", "Signal is not truth or identity proof.", "signal 不是 truth 或 identity proof。"),
        ("能力进化", "Capability Evolution", "rfc_only", "high", "Capability growth is not subject growth.", "capability growth 不是 subject growth。"),
        ("工具优先自进化", "Tool-First Self-Evolution", "rfc_only", "high", "Verification is not authorization.", "verification 不是 authorization。"),
        ("轻量交互试验台", "Thin Interaction Harness", "rfc_only", "medium", "Keep preview-only until approved.", "未批准前保持 preview-only。"),
        ("地基观察台", "Foundation Observatory", "implemented", "medium", "Use read-only CLI report only.", "只使用 read-only CLI report。"),
    ]
    if lang == "zh":
        return [
            {
                "display_name": display,
                "internal_key": key,
                "status": status,
                "risk": risk,
                "next_action": zh_action,
            }
            for display, key, status, risk, _en_action, zh_action in rows
        ]
    return [
        {
            "display_name": key,
            "internal_key": key,
            "zh_display_name": display,
            "status": status,
            "risk": risk,
            "next_action": en_action,
        }
        for display, key, status, risk, en_action, _zh_action in rows
    ]


def _boundary_status(lang: str) -> list[dict[str, Any]]:
    labels = {
        "identity mutation": ("blocked", "forbidden", "No automatic Identity Core change."),
        "memory rewrite": ("blocked", "forbidden", "No memory rewrite to simulate growth."),
        "recall event write": ("rfc_only", "disabled", "Ordinary recall is not a write."),
        "growth engine": ("blocked", "forbidden", "Growth candidates do not promote themselves."),
        "temporal runtime": ("future_direction", "disabled", "Elapsed time is review evidence, not runtime."),
        "CTM runtime": ("blocked", "forbidden", "CTM is inspiration, not implementation."),
        "tool execution": ("blocked", "forbidden", "Tool candidates are not executable tools."),
        "tool promotion": ("blocked", "forbidden", "Verification does not imply promotion."),
        "policy executor": ("blocked", "forbidden", "Policy language does not execute decisions."),
        "companion layer": ("future_direction", "blocked", "Companion behavior is outside foundation work."),
        "UI / AstrBot / adapter": ("future_direction", "blocked", "Platform surfaces must not own identity."),
        "reconstruction reducer": ("rfc_only", "disabled", "Reducer contract is not reducer execution."),
        "event compaction": ("blocked", "forbidden", "Event history remains auditable."),
    }
    zh_display_names = {
        "identity mutation": "身份修改",
        "memory rewrite": "记忆改写",
        "recall event write": "回忆事件写入",
        "growth engine": "成长引擎",
        "temporal runtime": "时间运行时",
        "CTM runtime": "CTM 运行时",
        "tool execution": "工具执行",
        "tool promotion": "工具提升",
        "policy executor": "策略执行器",
        "companion layer": "陪伴层",
        "UI / AstrBot / adapter": "UI / AstrBot / adapter",
        "reconstruction reducer": "重建 reducer",
        "event compaction": "事件压缩",
    }
    zh_notes = {
        "identity mutation": "不自动改变 Identity Core。",
        "memory rewrite": "不通过 rewrite 模拟 growth。",
        "recall event write": "ordinary recall 不是 write。",
        "growth engine": "growth candidates 不能自动 promote。",
        "temporal runtime": "elapsed time 是 review evidence，不是 runtime。",
        "CTM runtime": "CTM 是 inspiration，不是 implementation。",
        "tool execution": "tool candidates 不是 executable tools。",
        "tool promotion": "verification 不等于 promotion。",
        "policy executor": "policy language 不执行 decisions。",
        "companion layer": "companion behavior 不属于 foundation work。",
        "UI / AstrBot / adapter": "platform surfaces 不能拥有 identity。",
        "reconstruction reducer": "reducer contract 不是 reducer execution。",
        "event compaction": "event history 必须保持 auditable。",
    }
    rows = []
    for key, (status, state, note) in labels.items():
        rows.append(
            {
                "display_name": zh_display_names[key] if lang == "zh" else key,
                "internal_key": key,
                "status": status,
                "state": state,
                "enabled": False,
                "meaning": zh_notes[key] if lang == "zh" else note,
            }
        )
    return rows


def _risk_heatmap(lang: str) -> list[dict[str, str]]:
    risks = [
        ("概念膨胀", "concept inflation", "high", "Use phase index, glossary, and concept ownership."),
        ("review 层套 review 层", "review layer stacking", "medium", "Keep review objects few and owned."),
        ("过早 runtime", "premature runtime", "high", "Require founder approval for implementation."),
        ("companion 污染", "companion contamination", "high", "Keep social/product behavior blocked."),
        ("tool autonomy creep", "tool autonomy creep", "high", "Keep verification separate from authorization."),
        ("temporal overreach", "temporal overreach", "high", "Keep temporal concepts symbolic/evaluation-only."),
        ("identity drift", "identity drift", "high", "Keep identity changes high-gated."),
        ("observability becoming product UI", "observability becoming product UI", "medium", "Keep CLI read-only and non-dashboard."),
        ("fake cognition vocabulary", "fake cognition vocabulary", "high", "Keep anti-pseudocognition boundaries visible."),
    ]
    if lang == "zh":
        return [
            {
                "display_name": display,
                "internal_key": key,
                "risk": risk,
                "mitigation": mitigation,
            }
            for display, key, risk, mitigation in risks
        ]
    return [
        {
            "display_name": key,
            "internal_key": key,
            "zh_display_name": display,
            "risk": risk,
            "mitigation": mitigation,
        }
        for display, key, risk, mitigation in risks
    ]


def _next_steps(lang: str) -> list[dict[str, Any]]:
    if lang == "zh":
        return [
            {"priority": 1, "candidate": "创始人 / CTO 审查", "recommendation": "先审查 P96 输出，再决定是否继续。"},
            {"priority": 2, "candidate": "就绪度矩阵静态生成器", "recommendation": "如果继续，只生成静态矩阵，不执行决策。"},
            {"priority": 3, "candidate": "边界状态静态生成器", "recommendation": "只读生成边界状态，避免 policy executor。"},
            {"priority": 4, "candidate": "创始人快照生成器", "recommendation": "可后续拆出单独 snapshot 生成器。"},
        ]
    return [
        {"priority": 1, "candidate": "Pause for founder / CTO review", "recommendation": "Review P96 output before continuing."},
        {"priority": 2, "candidate": "Readiness Matrix Static Generator", "recommendation": "Generate static matrix only, without decisions."},
        {"priority": 3, "candidate": "Boundary Status Static Generator", "recommendation": "Generate boundary status without policy execution."},
        {"priority": 4, "candidate": "Founder Snapshot Generator", "recommendation": "Split snapshot generation later if useful."},
    ]


def _what_not_to_build_yet(lang: str) -> list[str]:
    if lang == "zh":
        return [
            "Web UI / 网页界面",
            "dashboard runtime / 仪表盘运行时",
            "companion product / 陪伴产品",
            "AstrBot integration / AstrBot 集成",
            "automatic growth / 自动成长",
            "Temporal Awareness runtime / 时间感知运行时",
            "CTM runtime / CTM 运行时",
            "tool execution runtime / 工具执行运行时",
            "policy executor / 策略执行器",
            "reconstruction reducer execution / 重建 reducer 执行",
            "event compaction / 事件压缩",
            "automatic roadmap execution / 自动路线图执行",
            "automatic next phase creation / 自动创建下一阶段",
        ]
    return [
        "Web UI",
        "dashboard runtime",
        "companion product",
        "AstrBot integration",
        "automatic growth",
        "Temporal Awareness runtime",
        "CTM runtime",
        "tool execution runtime",
        "policy executor",
        "reconstruction reducer execution",
        "event compaction",
        "automatic roadmap execution",
        "automatic next phase creation",
    ]


def _render_markdown(report: dict[str, Any]) -> str:
    zh = report["lang"] == "zh"
    title = "地基观察台报告（CLI 生成）" if zh else "Foundation Observatory Report (CLI Generated)"
    lines = [
        f"# {title}",
        "",
        f"`report_id`: `{report['report_id']}`",
        f"`lang`: `{report['lang']}`",
        f"`observatory_scope`: `{report['observatory_scope']}`",
        "",
    ]
    lines.extend(_render_snapshot(report["founder_snapshot"], zh))
    lines.extend(_render_table_section("main_axes_map", report["main_axes_map"], zh))
    lines.extend(_render_table_section("readiness_matrix", report["readiness_matrix"], zh))
    lines.extend(_render_table_section("boundary_status", report["boundary_status"], zh))
    lines.extend(_render_table_section("risk_heatmap", report["risk_heatmap"], zh))
    lines.extend(_render_next_steps(report["next_step_recommendations"], zh))
    lines.extend(_render_list_section("what_not_to_build_yet", report["what_not_to_build_yet"], zh))
    lines.extend(_render_invariants(report["non_execution_invariants"], zh))
    return "\n".join(lines)


def _render_snapshot(snapshot: dict[str, Any], zh: bool) -> list[str]:
    heading = "## founder_snapshot / 创始人快照" if zh else "## founder_snapshot / Founder Snapshot"
    lines = [heading, "", f"**{snapshot['display_name']}** (`{snapshot['internal_key']}`)", "", snapshot["summary"], ""]
    for item in snapshot["current_state"]:
        lines.append(f"- {item}")
    lines.extend(["", f"Next: {snapshot['why_observatory_next']}", ""])
    return lines


def _render_table_section(name: str, rows: list[dict[str, Any]], zh: bool) -> list[str]:
    heading_label = {
        "main_axes_map": "主轴地图" if zh else "Main Axes Map",
        "readiness_matrix": "就绪度矩阵" if zh else "Readiness Matrix",
        "boundary_status": "边界状态" if zh else "Boundary Status",
        "risk_heatmap": "风险热力图" if zh else "Risk Heatmap",
    }[name]
    keys = list(rows[0].keys())
    lines = [f"## {name} / {heading_label}", "", "| " + " | ".join(keys) + " |", "| " + " | ".join(["---"] * len(keys)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(row[key]) for key in keys) + " |")
    lines.append("")
    return lines


def _render_next_steps(rows: list[dict[str, Any]], zh: bool) -> list[str]:
    heading = "## next_step_recommendations / 下一步建议" if zh else "## next_step_recommendations / Next-Step Recommendations"
    lines = [heading, "", "| priority | candidate | recommendation |", "| --- | --- | --- |"]
    for row in rows:
        lines.append(f"| {row['priority']} | {row['candidate']} | {row['recommendation']} |")
    lines.append("")
    return lines


def _render_list_section(name: str, values: list[str], zh: bool) -> list[str]:
    label = "现在不要建设什么" if zh else "What Not To Build Yet"
    lines = [f"## {name} / {label}", ""]
    for value in values:
        lines.append(f"- {value}")
    lines.append("")
    return lines


def _render_invariants(invariants: dict[str, Any], zh: bool) -> list[str]:
    label = "非执行不变量" if zh else "Non-Execution Invariants"
    lines = [f"## non_execution_invariants / {label}", ""]
    for key, value in invariants.items():
        rendered = str(value).lower() if isinstance(value, bool) else str(value)
        lines.append(f"- {key}: {rendered}")
    lines.append("")
    return lines


def _cell(value: Any) -> str:
    if isinstance(value, bool):
        return str(value).lower()
    return str(value).replace("\n", " ")
