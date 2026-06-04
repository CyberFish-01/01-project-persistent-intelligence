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
    ("OBSERVATORY_USABILITY_REVIEW.md", "OBSERVATORY_USABILITY_REVIEW_ZH.md"),
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
        "report_id": "foundation_observatory_report_v0.3",
        "generated_by": "foundation-observatory-report",
        "lang": lang,
        "observatory_scope": "read_only_static_report",
        "source_documents": [_source_document(en, zh, lang) for en, zh in SOURCE_DOCUMENTS],
        "readiness_categories": READINESS_CATEGORIES,
        "founder_summary": _founder_summary(lang),
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


def _founder_summary(lang: str) -> dict[str, Any]:
    if lang == "zh":
        return {
            "display_name": "一屏摘要",
            "internal_key": "founder_summary",
            "headline": "01 Core 现在是可审查的连续性地基，不是自动行动系统。",
            "current_focus": "先把状态、边界、风险和下一步看清楚，再决定是否进入交互试验。",
            "safe_next_step": "继续打磨观察台，并由创始人 / CTO 审查 P98 输出。",
            "do_not_do_yet": "不要进入 harness implementation、产品 UI、AstrBot 集成、自动成长或工具执行。",
            "readiness_hint": "看到 RFC 层、评估层或未来方向时，只代表已有想法或计划，不代表已经实现。",
        }
    return {
        "display_name": "One-Screen Summary",
        "internal_key": "founder_summary",
        "headline": "01 Core is now an auditable continuity foundation, not an automatic action system.",
        "current_focus": "Make status, boundaries, risks, and next steps clear before interaction work.",
        "safe_next_step": "Continue polishing the observatory and have the founder / CTO review P98 output.",
        "do_not_do_yet": "Do not enter harness implementation, product UI, AstrBot integration, automatic growth, or tool execution.",
        "readiness_hint": "RFC-only, evaluation-only, and future-direction items are plans or review surfaces, not implemented capabilities.",
    }


def _founder_snapshot(lang: str) -> dict[str, Any]:
    if lang == "zh":
        return {
            "display_name": "创始人快照",
            "internal_key": "founder_snapshot",
            "summary": "01 Core 当前是在打地基：让一个 AI Core 的状态、身份、事件、风险和边界能被看见、审查和延续。",
            "current_state": [
                "已有本地 01 Core prototype、事件/状态相关工程参考，以及大量 foundation documents。",
                "当前重点是可见性、边界和只读观察，不是增加行动能力。",
                "P98 observatory 输出只生成报告，不修改 state，也不执行下一步。",
            ],
            "why_observatory_next": "观察台应该让创始人不用读完整论文式文档，也能看清已实现、计划中、禁止做和下一步该审查的内容。",
        }
    return {
        "display_name": "Founder Snapshot",
        "internal_key": "founder_snapshot",
        "summary": "01 Core is currently foundation work: making state, identity, events, risks, and boundaries visible, reviewable, and continuous.",
        "current_state": [
            "A local 01 Core prototype, event/state engineering references, and broad foundation documents exist.",
            "The current focus is visibility, boundaries, and read-only observation, not more action power.",
            "The P98 observatory output generates reports only and does not mutate state or execute next steps.",
        ],
        "why_observatory_next": "The observatory should let the founder understand implemented, planned, forbidden, and review-next work without reading the entire research corpus.",
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
        _readiness_row(
            zh_display="身份核心",
            display="Identity Core",
            internal_key="Identity Core",
            status="report_only",
            status_label_zh="报告层",
            status_label_en="report layer",
            risk="high",
            what_is_it_zh="01 关于“我是谁”的受保护答案。",
            what_is_it_en="The protected answer to who 01 is.",
            can_do_zh="可以被观察、审查和作为边界引用。",
            can_do_en="Can be observed, reviewed, and referenced as a boundary.",
            cannot_do_zh="不能被自动改写，也不能被聊天、工具或报告直接修改。",
            cannot_do_en="Cannot be automatically rewritten or changed by chat, tools, or reports.",
            next_action_zh="继续由 Identity Gate 保护，所有变化都保持 high-gate review。",
            next_action_en="Keep it protected by Identity Gate and require high-gate review for changes.",
        ),
        _readiness_row(
            zh_display="状态传递",
            display="State Transfer",
            internal_key="State Transfer",
            status="report_only",
            status_label_zh="报告层",
            status_label_en="report layer",
            risk="medium",
            what_is_it_zh="把当前状态穿过时间传下去，而不是只检索旧记忆。",
            what_is_it_en="Passing current state through time, not merely retrieving old memories.",
            can_do_zh="可以作为整个项目的判断标准。",
            can_do_en="Can be used as the core project criterion.",
            cannot_do_zh="不能被简化成 summary、retrieval 或长上下文。",
            cannot_do_en="Cannot be reduced to summary, retrieval, or long context.",
            next_action_zh="继续用它校准 observatory 和未来 harness 计划。",
            next_action_en="Use it to calibrate observatory output and future harness plans.",
        ),
        _readiness_row(
            zh_display="事件日志",
            display="Event Log",
            internal_key="Event Log",
            status="implemented",
            status_label_zh="已实现",
            status_label_en="implemented",
            risk="medium",
            what_is_it_zh="重要状态变化的账本。",
            what_is_it_en="A ledger of important state changes.",
            can_do_zh="可以记录和检查已有事件线索。",
            can_do_en="Can record and inspect existing event evidence.",
            cannot_do_zh="不能压缩历史，也不能替代完整重建。",
            cannot_do_en="Cannot compact history or replace full reconstruction.",
            next_action_zh="保持 append-only 和可审计。",
            next_action_en="Keep it append-only and auditable.",
        ),
        _readiness_row(
            zh_display="回放检查",
            display="Replay",
            internal_key="Replay",
            status="report_only",
            status_label_zh="报告层",
            status_label_en="report layer",
            risk="medium",
            what_is_it_zh="检查历史线索能不能再走一遍。",
            what_is_it_en="Checking whether historical evidence can be followed again.",
            can_do_zh="可以报告 replay readiness。",
            can_do_en="Can report replay readiness.",
            cannot_do_zh="不能重建 state，也不能执行 rollback。",
            cannot_do_en="Cannot rebuild state or execute rollback.",
            next_action_zh="继续只报告 readiness，不执行 reducer。",
            next_action_en="Continue reporting readiness without executing reducers.",
        ),
        _readiness_row(
            zh_display="状态重建",
            display="Reconstruction",
            internal_key="Reconstruction",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="high",
            what_is_it_zh="未来用证据重建过去状态的方向。",
            what_is_it_en="The future direction for rebuilding past state from evidence.",
            can_do_zh="可以讨论 contract、payload 和 diff 要求。",
            can_do_en="Can discuss contracts, payload requirements, and diff requirements.",
            cannot_do_zh="现在不能执行 reducer 或重建 state。",
            cannot_do_en="Cannot execute reducers or rebuild state now.",
            next_action_zh="先补清楚 reducer contract 和 evidence gaps。",
            next_action_en="Clarify reducer contracts and evidence gaps first.",
        ),
        _readiness_row(
            zh_display="说法证据图",
            display="Claim Graph",
            internal_key="Claim Graph",
            status="report_only",
            status_label_zh="报告层",
            status_label_en="report layer",
            risk="medium",
            what_is_it_zh="记录哪些说法有证据、冲突或仍未解决。",
            what_is_it_en="Tracks which claims are supported, conflicting, or unresolved.",
            can_do_zh="可以帮助审查 claim 和 evidence。",
            can_do_en="Can support claim and evidence review.",
            cannot_do_zh="不能吞掉所有意义变化，也不能自动改信念。",
            cannot_do_en="Cannot absorb every meaning shift or automatically change beliefs.",
            next_action_zh="继续保持 claim review 和 meaning shift 分工。",
            next_action_en="Keep claim review separate from meaning-shift review.",
        ),
        _readiness_row(
            zh_display="任务中心",
            display="Task Hub",
            internal_key="Task Hub",
            status="report_only",
            status_label_zh="报告层",
            status_label_en="report layer",
            risk="medium",
            what_is_it_zh="保存正在做什么、接下来要看什么的任务视图。",
            what_is_it_en="A task view for what is active and what needs attention next.",
            can_do_zh="可以辅助恢复任务上下文。",
            can_do_en="Can help resume task context.",
            cannot_do_zh="不能替代 governance review 或自动执行 roadmap。",
            cannot_do_en="Cannot replace governance review or execute roadmaps automatically.",
            next_action_zh="继续把任务状态和审查对象分开。",
            next_action_en="Keep task state separate from review objects.",
        ),
        _readiness_row(
            zh_display="带状态的记忆",
            display="Stateful Memory",
            internal_key="Stateful Memory",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="high",
            what_is_it_zh="记忆加上形成和被回忆时的状态条件。",
            what_is_it_en="Memory plus the conditions under which it was encoded and recalled.",
            can_do_zh="可以作为解释 meaning shift 的语义框架。",
            can_do_en="Can frame how meaning shifts should be interpreted.",
            cannot_do_zh="不能改写 memory，也不能自动提升成 growth。",
            cannot_do_en="Cannot rewrite memory or automatically promote growth.",
            next_action_zh="先定义最小 encoding policy 和 review criteria。",
            next_action_en="Clarify minimal encoding policy and review criteria first.",
        ),
        _readiness_row(
            zh_display="成长提案审查",
            display="Growth Candidate Review",
            internal_key="Growth Candidate Review",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="high",
            what_is_it_zh="把可能的成长先作为提案审查，而不是直接当成已经成长。",
            what_is_it_en="Reviews possible growth as a proposal, not completed growth.",
            can_do_zh="可以帮助区分 candidate 和 promoted result。",
            can_do_en="Can separate candidates from promoted results.",
            cannot_do_zh="不能执行 growth lifecycle，也不能修改身份。",
            cannot_do_en="Cannot execute growth lifecycle or mutate identity.",
            next_action_zh="继续保持 review-only，避免自动成长。",
            next_action_en="Keep it review-only and avoid automatic growth.",
        ),
        _readiness_row(
            zh_display="时间感知",
            display="Temporal Awareness",
            internal_key="Temporal Awareness",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="high",
            what_is_it_zh="研究时间流逝如何影响状态理解。",
            what_is_it_en="Studies how elapsed time may affect state interpretation.",
            can_do_zh="可以作为 future direction 和 review question。",
            can_do_en="Can remain a future direction and review question.",
            cannot_do_zh="不能写 temporal event，也不能做 temporal runtime。",
            cannot_do_en="Cannot write temporal events or implement temporal runtime.",
            next_action_zh="继续放在 RFC / evaluation 层。",
            next_action_en="Keep it in RFC and evaluation layers.",
        ),
        _readiness_row(
            zh_display="时间线一致性检查",
            display="Temporal Coherence",
            internal_key="Temporal Coherence",
            status="evaluation_only",
            status_label_zh="评估层",
            status_label_en="evaluation layer",
            risk="high",
            what_is_it_zh="检查一个变化是否仍符合时间线和证据。",
            what_is_it_en="Checks whether a change still fits the timeline and evidence.",
            can_do_zh="可以设计 deterministic scenario。",
            can_do_en="Can design deterministic scenarios.",
            cannot_do_zh="不能当成意识、思维或身份更新依据。",
            cannot_do_en="Cannot be treated as consciousness, thought, or identity-update proof.",
            next_action_zh="继续作为 evaluation signal，不变成 runtime truth。",
            next_action_en="Keep it as an evaluation signal, not runtime truth.",
        ),
        _readiness_row(
            zh_display="能力改进边界",
            display="Capability Evolution",
            internal_key="Capability Evolution",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="high",
            what_is_it_zh="工具和流程可以改进，但不能等同于主体成长。",
            what_is_it_en="Tools and procedures may improve, but that is not subject growth.",
            can_do_zh="可以定义 evidence 和 authorization 边界。",
            can_do_en="Can define evidence and authorization boundaries.",
            cannot_do_zh="不能自动执行工具、提升工具或改变身份。",
            cannot_do_en="Cannot execute tools, promote tools, or change identity automatically.",
            next_action_zh="先做 Tool Verification Evidence Model，而不是 tool runtime。",
            next_action_en="Consider a Tool Verification Evidence Model before any tool runtime.",
        ),
        _readiness_row(
            zh_display="先改工具，不改身份",
            display="Tool-First Self-Evolution",
            internal_key="Tool-First Self-Evolution",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="high",
            what_is_it_zh="先研究可验证的工具改进，不让它滑向身份成长。",
            what_is_it_en="Studies verifiable tool improvement before any subject or identity change.",
            can_do_zh="可以作为 capability RFC 方向。",
            can_do_en="Can guide capability RFC work.",
            cannot_do_zh="不能生成工具、执行工具或自动 promotion。",
            cannot_do_en="Cannot generate tools, execute tools, or promote automatically.",
            next_action_zh="继续保持 verification 不等于 authorization。",
            next_action_en="Keep verification separate from authorization.",
        ),
        _readiness_row(
            zh_display="本地交互预演",
            display="Thin Interaction Harness",
            internal_key="Thin Interaction Harness",
            status="rfc_only",
            status_label_zh="RFC 层",
            status_label_en="RFC layer",
            risk="medium",
            what_is_it_zh="未来可能用于本地预演交互的窄入口，不是聊天产品。",
            what_is_it_en="A possible narrow local interaction preview, not a chat product.",
            can_do_zh="可以继续 planning 或写 implementation plan。",
            can_do_en="Can continue planning or receive an implementation plan.",
            cannot_do_zh="现在不能实现 harness、UI、adapter 或 mutation path。",
            cannot_do_en="Cannot implement harness, UI, adapters, or mutation paths now.",
            next_action_zh="先让 observatory 更清楚，再讨论 implementation plan。",
            next_action_en="Clarify the observatory before discussing implementation plans.",
        ),
        _readiness_row(
            zh_display="地基观察台",
            display="Foundation Observatory",
            internal_key="Foundation Observatory",
            status="implemented",
            status_label_zh="已实现",
            status_label_en="implemented",
            risk="medium",
            what_is_it_zh="用只读报告展示地基状态、风险、边界和下一步候选。",
            what_is_it_en="A read-only report showing foundation status, risks, boundaries, and candidate next steps.",
            can_do_zh="可以生成 Markdown / JSON 报告。",
            can_do_en="Can generate Markdown and JSON reports.",
            cannot_do_zh="不能变成 dashboard runtime、policy executor 或自动路线图执行器。",
            cannot_do_en="Cannot become dashboard runtime, policy executor, or automatic roadmap executor.",
            next_action_zh="继续打磨可读性，不进入产品层。",
            next_action_en="Continue improving readability without entering product work.",
        ),
    ]
    return [_localized_readiness_row(row, lang) for row in rows]


def _readiness_row(
    *,
    zh_display: str,
    display: str,
    internal_key: str,
    status: str,
    status_label_zh: str,
    status_label_en: str,
    risk: str,
    what_is_it_zh: str,
    what_is_it_en: str,
    can_do_zh: str,
    can_do_en: str,
    cannot_do_zh: str,
    cannot_do_en: str,
    next_action_zh: str,
    next_action_en: str,
) -> dict[str, Any]:
    return {
        "zh_display_name": zh_display,
        "display_name": display,
        "internal_key": internal_key,
        "status": status,
        "status_label_zh": status_label_zh,
        "status_label_en": status_label_en,
        "risk": risk,
        "what_is_it_zh": what_is_it_zh,
        "what_is_it_en": what_is_it_en,
        "can_do_zh": can_do_zh,
        "can_do_en": can_do_en,
        "cannot_do_zh": cannot_do_zh,
        "cannot_do_en": cannot_do_en,
        "next_action_zh": next_action_zh,
        "next_action_en": next_action_en,
    }


def _localized_readiness_row(row: dict[str, Any], lang: str) -> dict[str, Any]:
    if lang == "zh":
        return {
            "display_name": row["zh_display_name"],
            "internal_key": row["internal_key"],
            "status_label": row["status_label_zh"],
            "status": row["status"],
            "risk": row["risk"],
            "what_is_it": row["what_is_it_zh"],
            "can_do": row["can_do_zh"],
            "cannot_do": row["cannot_do_zh"],
            "next_action": row["next_action_zh"],
        }
    return {
        "display_name": row["display_name"],
        "internal_key": row["internal_key"],
        "zh_display_name": row["zh_display_name"],
        "status_label": row["status_label_en"],
        "status": row["status"],
        "risk": row["risk"],
        "what_is_it": row["what_is_it_en"],
        "can_do": row["can_do_en"],
        "cannot_do": row["cannot_do_en"],
        "next_action": row["next_action_en"],
    }


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
        _risk_row(
            zh_display="概念太多看不清",
            display="Concept overload",
            internal_key="concept inflation",
            risk_level="high",
            plain_zh="概念越来越多，创始人很难判断哪个是真地基、哪个只是未来想法。",
            plain_en="There are so many concepts that it becomes hard to tell foundation from future ideas.",
            danger_zh="如果不收敛，后续开发会把 RFC、review object 或 candidate 误当成已实现能力。",
            danger_en="If it is not controlled, later work may treat RFCs, review objects, or candidates as implemented capabilities.",
            mitigation_zh="用 phase index、glossary 和 observatory status 明确每个概念的位置。",
            mitigation_en="Use the phase index, glossary, and observatory status to place each concept clearly.",
            next_zh="继续给每个抽象概念加一句浅显解释和 status label。",
            next_en="Continue adding plain explanations and status labels to abstract concepts.",
        ),
        _risk_row(
            zh_display="审查层叠太厚",
            display="Review stacking",
            internal_key="review layer stacking",
            risk_level="medium",
            plain_zh="审查对象越来越多，可能变成只审查审查本身。",
            plain_en="Review objects can pile up until the system mostly reviews its own reviews.",
            danger_zh="这会让真正的状态、风险和下一步被隐藏在流程里。",
            danger_en="This can hide real state, risk, and next steps inside process layers.",
            mitigation_zh="保留少量核心 review surface，并说明每个 review 管什么。",
            mitigation_en="Keep only a small set of core review surfaces and state their ownership.",
            next_zh="把重复 review 概念合并到跨层审查区或 open questions。",
            next_en="Merge overlapping review concepts into governance surface or open questions.",
        ),
        _risk_row(
            zh_display="过早做运行时",
            display="Premature runtime",
            internal_key="premature runtime",
            risk_level="high",
            plain_zh="还没看清边界就开始写能行动的功能。",
            plain_en="Building action-capable runtime before boundaries are clear.",
            danger_zh="一旦 runtime 写进去，review-only 可能被误读成自动执行。",
            danger_en="Once runtime exists, review-only concepts may be mistaken for execution.",
            mitigation_zh="所有 implementation 都必须有创始人明确批准，并通过 forbidden search。",
            mitigation_en="Require explicit founder approval and forbidden-search checks for implementation.",
            next_zh="P98 只改静态报告；不要进入 harness implementation。",
            next_en="Keep P98 to static reporting; do not enter harness implementation.",
        ),
        _risk_row(
            zh_display="陪伴层过早介入",
            display="Companion contamination",
            internal_key="companion contamination",
            risk_level="high",
            plain_zh="把连续性地基误做成陪伴产品或社交人格。",
            plain_en="Mistaking the continuity foundation for a companion product or social persona.",
            danger_zh="这会污染 Identity Core，并把 relationship behavior 误当成主体成长。",
            danger_en="It can contaminate Identity Core and confuse relationship behavior with subject growth.",
            mitigation_zh="继续阻塞 companion、relationship、UI 和 product layer。",
            mitigation_en="Keep companion, relationship, UI, and product layers blocked.",
            next_zh="所有 founder-facing 文案继续强调“地基，不是产品”。",
            next_en="Keep founder-facing text clear: foundation, not product.",
        ),
        _risk_row(
            zh_display="工具能力滑向自动执行",
            display="Tool autonomy creep",
            internal_key="tool autonomy creep",
            risk_level="high",
            plain_zh="工具验证、工具候选和工具执行混在一起。",
            plain_en="Tool verification, tool candidates, and tool execution start blending together.",
            danger_zh="验证成功可能被误当成授权，从而打开不受控执行。",
            danger_en="A successful verification could be mistaken for authorization and enable uncontrolled execution.",
            mitigation_zh="坚持 verification 不等于 authorization，candidate 不等于 promoted tool。",
            mitigation_en="Keep verification separate from authorization and candidates separate from promoted tools.",
            next_zh="如继续能力方向，先写 Tool Verification Evidence Model，不写 tool runtime。",
            next_en="If capability work continues, write Tool Verification Evidence Model before any tool runtime.",
        ),
        _risk_row(
            zh_display="时间概念过度解释",
            display="Temporal overreach",
            internal_key="temporal overreach",
            risk_level="high",
            plain_zh="把时间一致性、CTM 启发或 thought trace 说得像真实思维。",
            plain_en="Treating temporal coherence, CTM inspiration, or traces as if they were real thought.",
            danger_zh="这会越过 anti-pseudocognition boundary，并误导身份更新判断。",
            danger_en="It crosses anti-pseudocognition boundaries and can mislead identity-update decisions.",
            mitigation_zh="时间相关内容保持 symbolic、RFC-only 或 evaluation-only。",
            mitigation_en="Keep temporal concepts symbolic, RFC-only, or evaluation-only.",
            next_zh="不要实现 temporal runtime；只改报告里的解释清晰度。",
            next_en="Do not implement temporal runtime; only clarify report wording.",
        ),
        _risk_row(
            zh_display="身份漂移",
            display="Identity drift",
            internal_key="identity drift",
            risk_level="high",
            plain_zh="系统在没有高门槛审查的情况下改变“我是谁”。",
            plain_en="The system changes who it is without high-gate review.",
            danger_zh="这会破坏 continuity，把持续主体变成一组临时行为。",
            danger_en="It breaks continuity and turns the subject into temporary behavior.",
            mitigation_zh="Identity Core 保持 high-gated，observatory 只显示状态，不修改状态。",
            mitigation_en="Keep Identity Core high-gated; observatory shows state and never changes it.",
            next_zh="继续在 boundary status 中显式显示身份修改 blocked。",
            next_en="Continue showing identity mutation as blocked in boundary status.",
        ),
        _risk_row(
            zh_display="观察台变产品界面",
            display="Observatory becoming product UI",
            internal_key="observability becoming product UI",
            risk_level="medium",
            plain_zh="只读报告被误用成 dashboard runtime、状态 API 或产品入口。",
            plain_en="A read-only report gets mistaken for dashboard runtime, status API, or product entry.",
            danger_zh="观察层如果能执行决策，就会绕过 review-only 边界。",
            danger_en="If the observability layer executes decisions, it bypasses review-only boundaries.",
            mitigation_zh="CLI 只读输出 Markdown/JSON，不监听、不执行、不创建 phase。",
            mitigation_en="The CLI only emits Markdown/JSON and does not monitor, execute, or create phases.",
            next_zh="继续打磨静态输出，不做 Web UI 或 runtime monitor。",
            next_en="Improve static output only; do not build Web UI or runtime monitoring.",
        ),
        _risk_row(
            zh_display="伪认知词汇误导",
            display="Pseudocognition wording",
            internal_key="fake cognition vocabulary",
            risk_level="high",
            plain_zh="术语听起来像意识、真实思考或自动成长。",
            plain_en="Vocabulary sounds like consciousness, real thought, or automatic growth.",
            danger_zh="这会让 review signal 被误读成主体状态事实。",
            danger_en="It can make review signals look like facts about subject state.",
            mitigation_zh="所有 temporal、thought、growth 术语都标注为 review / RFC / evaluation。",
            mitigation_en="Label temporal, thought, and growth terms as review, RFC, or evaluation surfaces.",
            next_zh="继续用浅显中文解释：候选不是结果，审查不是执行。",
            next_en="Keep using plain wording: candidates are not results, review is not execution.",
        ),
    ]
    return [_localized_risk_row(row, lang) for row in risks]


def _risk_row(
    *,
    zh_display: str,
    display: str,
    internal_key: str,
    risk_level: str,
    plain_zh: str,
    plain_en: str,
    danger_zh: str,
    danger_en: str,
    mitigation_zh: str,
    mitigation_en: str,
    next_zh: str,
    next_en: str,
) -> dict[str, str]:
    return {
        "zh_display_name": zh_display,
        "display_name": display,
        "internal_key": internal_key,
        "risk_level": risk_level,
        "plain_explanation_zh": plain_zh,
        "plain_explanation_en": plain_en,
        "why_dangerous_zh": danger_zh,
        "why_dangerous_en": danger_en,
        "current_mitigation_zh": mitigation_zh,
        "current_mitigation_en": mitigation_en,
        "next_step_zh": next_zh,
        "next_step_en": next_en,
    }


def _localized_risk_row(row: dict[str, str], lang: str) -> dict[str, str]:
    if lang == "zh":
        return {
            "display_name": row["zh_display_name"],
            "internal_key": row["internal_key"],
            "plain_explanation": row["plain_explanation_zh"],
            "why_dangerous": row["why_dangerous_zh"],
            "current_mitigation": row["current_mitigation_zh"],
            "next_step": row["next_step_zh"],
            "risk_level": row["risk_level"],
        }
    return {
        "display_name": row["display_name"],
        "internal_key": row["internal_key"],
        "zh_display_name": row["zh_display_name"],
        "plain_explanation": row["plain_explanation_en"],
        "why_dangerous": row["why_dangerous_en"],
        "current_mitigation": row["current_mitigation_en"],
        "next_step": row["next_step_en"],
        "risk_level": row["risk_level"],
    }


def _next_steps(lang: str) -> list[dict[str, Any]]:
    rows = [
        _next_step_row(
            priority=1,
            candidate_zh="继续打磨观察台",
            candidate_en="Continue polishing the observatory",
            why_zh="P97 发现可读性只有 7/10，风险和抽象术语还不够 founder-facing。",
            why_en="P97 found readability at 7/10; risks and abstract terms are still not founder-facing enough.",
            benefit_zh="收益是让创始人不用读完整文档，也能看懂状态、风险和边界。",
            benefit_en="The benefit is making status, risks, and boundaries understandable without reading the full corpus.",
            risk_zh="风险很低，只要保持 static、read-only、不执行下一步。",
            risk_en="Risk is low if it stays static, read-only, and non-executing.",
            not_zh="不要把观察台做成 dashboard runtime、status API 或自动路线图执行器。",
            not_en="Do not turn the observatory into dashboard runtime, status API, or automatic roadmap executor.",
        ),
        _next_step_row(
            priority=2,
            candidate_zh="Founder / CTO Review",
            candidate_en="Founder / CTO Review",
            why_zh="现在最需要人工判断：哪些概念真正该保留，哪些需要后推。",
            why_en="Human judgment is needed to decide which concepts stay and which should be deferred.",
            benefit_zh="收益是避免工程继续堆概念，同时让下一阶段有明确批准。",
            benefit_en="The benefit is avoiding concept buildup and giving the next phase explicit approval.",
            risk_zh="风险很低，但可能会暂停实现节奏。",
            risk_en="Risk is low, though it may slow implementation momentum.",
            not_zh="不要把 review 结论自动转成执行任务。",
            not_en="Do not automatically turn review conclusions into execution tasks.",
        ),
        _next_step_row(
            priority=3,
            candidate_zh="Minimal CLI Harness Implementation Plan",
            candidate_en="Minimal CLI Harness Implementation Plan",
            why_zh="如果创始人确认需要往交互试验推进，应先写 implementation plan，而不是直接实现 harness。",
            why_en="If the founder wants interaction work, write an implementation plan before building the harness.",
            benefit_zh="收益是提前定义输入、输出、fixture、no-write 边界和测试计划。",
            benefit_en="The benefit is defining inputs, outputs, fixtures, no-write boundaries, and tests first.",
            risk_zh="风险是计划语言可能被误读成已批准实现。",
            risk_en="The risk is that planning language may be mistaken for implementation approval.",
            not_zh="不要实现 harness、conversation runtime、adapter ingest 或 memory writes。",
            not_en="Do not implement harness, conversation runtime, adapter ingest, or memory writes.",
        ),
        _next_step_row(
            priority=4,
            candidate_zh="Tool Verification Evidence Model",
            candidate_en="Tool Verification Evidence Model",
            why_zh="能力方向有价值，但必须先证明 verification 不等于 authorization。",
            why_en="Capability work is valuable, but it must first prove verification is not authorization.",
            benefit_zh="收益是为未来工具候选提供 evidence vocabulary，同时阻止 tool execution creep。",
            benefit_en="The benefit is evidence vocabulary for future tool candidates while blocking tool execution creep.",
            risk_zh="风险是 founder 可能误以为要开始自动工具执行。",
            risk_en="The risk is that it may look like the start of automatic tool execution.",
            not_zh="不要执行工具、安装依赖、提升工具或写 policy executor。",
            not_en="Do not execute tools, install dependencies, promote tools, or write a policy executor.",
        ),
    ]
    return [_localized_next_step(row, lang) for row in rows]


def _next_step_row(
    *,
    priority: int,
    candidate_zh: str,
    candidate_en: str,
    why_zh: str,
    why_en: str,
    benefit_zh: str,
    benefit_en: str,
    risk_zh: str,
    risk_en: str,
    not_zh: str,
    not_en: str,
) -> dict[str, Any]:
    return {
        "priority": priority,
        "candidate_zh": candidate_zh,
        "candidate_en": candidate_en,
        "why_recommended_zh": why_zh,
        "why_recommended_en": why_en,
        "benefit_zh": benefit_zh,
        "benefit_en": benefit_en,
        "risk_zh": risk_zh,
        "risk_en": risk_en,
        "not_recommended_zh": not_zh,
        "not_recommended_en": not_en,
    }


def _localized_next_step(row: dict[str, Any], lang: str) -> dict[str, Any]:
    if lang == "zh":
        return {
            "priority": row["priority"],
            "candidate": row["candidate_zh"],
            "why_recommended": row["why_recommended_zh"],
            "benefit": row["benefit_zh"],
            "risk": row["risk_zh"],
            "not_recommended": row["not_recommended_zh"],
        }
    return {
        "priority": row["priority"],
        "candidate": row["candidate_en"],
        "why_recommended": row["why_recommended_en"],
        "benefit": row["benefit_en"],
        "risk": row["risk_en"],
        "not_recommended": row["not_recommended_en"],
    }


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
    lines.extend(_render_founder_summary(report["founder_summary"], zh))
    lines.extend(_render_snapshot(report["founder_snapshot"], zh))
    lines.extend(_render_table_section("main_axes_map", report["main_axes_map"], zh))
    lines.extend(_render_table_section("readiness_matrix", report["readiness_matrix"], zh))
    lines.extend(_render_table_section("boundary_status", report["boundary_status"], zh))
    lines.extend(_render_table_section("risk_heatmap", report["risk_heatmap"], zh))
    lines.extend(_render_next_steps(report["next_step_recommendations"], zh))
    lines.extend(_render_list_section("what_not_to_build_yet", report["what_not_to_build_yet"], zh))
    lines.extend(_render_invariants(report["non_execution_invariants"], zh))
    return "\n".join(lines)


def _render_founder_summary(summary: dict[str, Any], zh: bool) -> list[str]:
    heading = "## founder_summary / 一屏摘要" if zh else "## founder_summary / One-Screen Summary"
    lines = [
        heading,
        "",
        f"**{summary['display_name']}** (`{summary['internal_key']}`)",
        "",
        f"- headline: {summary['headline']}",
        f"- current_focus: {summary['current_focus']}",
        f"- safe_next_step: {summary['safe_next_step']}",
        f"- do_not_do_yet: {summary['do_not_do_yet']}",
        f"- readiness_hint: {summary['readiness_hint']}",
        "",
    ]
    return lines


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
    keys = list(rows[0].keys())
    lines = [heading, "", "| " + " | ".join(keys) + " |", "| " + " | ".join(["---"] * len(keys)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(_cell(row[key]) for key in keys) + " |")
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
