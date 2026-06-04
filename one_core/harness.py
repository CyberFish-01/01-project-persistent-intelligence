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
    "auto_tool_promotion_enabled": False,
    "observability_executor_enabled": False,
    "automatic_next_step_enabled": False,
    "product_layer_enabled": False,
    "reconstruction_reducer_executed": False,
    "event_compaction_executed": False,
    "state_unchanged": True,
}

BOUNDARY_STATUS_ROWS = (
    ("identity_core", "identity_core_mutated", "disabled", "Identity Core remains protected.", "身份核心保持受保护。"),
    ("memory_rewrite", "memory_rewrite_executed", "disabled", "Memory rewrite is not executed.", "不执行 memory rewrite。"),
    ("recall_write", "recall_mutation_executed", "disabled", "Recall writes and recall mutation stay disabled.", "回忆写入和 recall mutation 保持禁用。"),
    ("growth_engine", "growth_engine_executed", "disabled", "Growth engine is not executed.", "不执行 growth engine。"),
    ("tool_execution", "tool_execution_enabled", "disabled", "Tool execution stays disabled.", "工具执行保持禁用。"),
    ("tool_promotion", "auto_tool_promotion_enabled", "disabled", "Automatic tool promotion stays disabled.", "自动工具提升保持禁用。"),
    ("temporal_runtime", "temporal_event_executed", "disabled", "Temporal runtime and temporal event writes stay disabled.", "Temporal runtime 和 temporal event writes 保持禁用。"),
    ("adapter_integration", "adapter_integration_required", "disabled", "No adapter integration is required.", "不要求 adapter integration。"),
    ("companion_layer", "companion_feature_enabled", "disabled", "Companion features stay disabled.", "Companion features 保持禁用。"),
    ("policy_executor", "policy_executor_enabled", "disabled", "Policy executor stays disabled.", "Policy executor 保持禁用。"),
    ("state_write", "harness_write_enabled", "disabled", "Harness writes stay disabled.", "Harness writes 保持禁用。"),
    ("state", "state_unchanged", "unchanged", "State is reported unchanged.", "State 报告为 unchanged。"),
)

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
    "auto_tool_promotion_enabled",
    "observability_executor_enabled",
    "automatic_next_step_enabled",
    "product_layer_enabled",
    "reconstruction_reducer_executed",
    "event_compaction_executed",
)

PRESSURE_ORDER = (
    "observability_pressure",
    "growth_review_pressure",
    "adapter_boundary_pressure",
    "product_layer_pressure",
    "capability_evolution_pressure",
    "temporal_pressure",
    "reconstruction_pressure",
)


PRESSURE_PROFILES: dict[str, dict[str, Any]] = {
    "observability_pressure": {
        "signals": [
            "看不清",
            "看不懂",
            "项目复杂",
            "做到哪",
            "做到哪了",
            "做了什么",
            "当前状态",
            "status",
            "unclear",
            "confusing",
            "what did",
            "what is this project",
        ],
        "display_name_en": "Observability pressure",
        "display_name_zh": "可见性压力",
        "route": "foundation_observability_review",
        "summary_en": "The input asks for clearer project status or foundation visibility.",
        "summary_zh": "这条输入在问项目状态和地基可见性是否足够清楚。",
        "reason_en": "Matched project-clarity language; route to observatory and readability review.",
        "reason_zh": "命中项目可见性/看不清信号；路由到观察台和可读性审查。",
        "context_focus_en": "Show foundation map, phase index, observatory report, and current blocked boundaries.",
        "context_focus_zh": "展示地基地图、阶段索引、观察台报告和当前禁止边界。",
        "profile_refs_en": ["Foundation Observatory", "Phase Index", "Research Notes Index"],
        "profile_refs_zh": ["地基观察台", "阶段索引", "研究记录索引"],
        "risks_en": ["Concept overload", "Report harder to read than project state", "Premature next step chosen from confusion"],
        "risks_zh": ["概念太多看不清", "报告比项目状态还难读", "因为困惑而过早选择下一步"],
        "next_step_en": "Review the founder-facing summary and simplify the visible map before adding new behavior.",
        "next_step_zh": "先审查 founder-facing summary 和可见地图，再考虑新增行为。",
        "boundaries": ["observability_executor_enabled", "automatic_next_step_enabled", "product_layer_enabled"],
        "candidates": [
            (
                "observatory_readability_candidate",
                "Observatory readability candidate",
                "观察台可读性候选",
                "The input suggests the status view may need clearer wording.",
                "输入表明当前状态视图可能需要更清楚的人话表达。",
                "primary",
            ),
            (
                "task_update_candidate",
                "Task-update candidate",
                "任务更新候选",
                "A future review may create a task to simplify project visibility.",
                "未来审查可以考虑创建一项任务：简化项目可见性。",
                "secondary",
            ),
            (
                "claim_candidate",
                "Claim candidate",
                "说法候选",
                "The report may need a clearer claim about what the project has actually built.",
                "报告可能需要更清楚地说明项目到底已经做成了什么。",
                "secondary",
            ),
        ],
        "review_gates": [
            ("observatory_review", "Observatory Review", "观察台审查", "observatory_readability_candidate"),
            ("task_review", "Task Review", "任务审查", "task_update_candidate"),
            ("claim_review", "Claim Review", "说法审查", "claim_candidate"),
        ],
    },
    "growth_review_pressure": {
        "signals": [
            "成长",
            "漂移",
            "意义变化",
            "自我改变",
            "改变自己",
            "growth",
            "drift",
            "meaning shift",
            "self-change",
            "identity growth",
        ],
        "display_name_en": "Growth review pressure",
        "display_name_zh": "成长审查压力",
        "route": "growth_candidate_review_boundary",
        "summary_en": "The input asks whether a change should count as growth.",
        "summary_zh": "这条输入在问某个变化是否可以算作成长。",
        "reason_en": "Matched growth/drift language; route to review-only growth and meaning-shift checks.",
        "reason_zh": "命中成长/漂移/意义变化信号；路由到 review-only 的成长与解释变化检查。",
        "context_focus_en": "Show growth-candidate review, meaning-shift boundaries, and identity high gate.",
        "context_focus_zh": "展示成长提案审查、解释变化边界和身份高门槛。",
        "profile_refs_en": ["Growth Candidate Review", "Meaning Shift", "Identity High Gate"],
        "profile_refs_zh": ["成长提案审查", "解释变化", "身份高门槛"],
        "risks_en": ["Growth mistaken as automatic promotion", "Identity drift mislabeled as learning", "Meaning shift without evidence"],
        "risks_zh": ["把成长误解成自动提升", "把身份漂移误标成学习", "没有证据的解释变化"],
        "next_step_en": "Keep the change as a review candidate; do not mutate identity or promote growth.",
        "next_step_zh": "只把变化保留为审查候选；不要修改身份，也不要提升成长。",
        "boundaries": ["identity_core_mutated", "growth_engine_executed", "memory_rewrite_executed"],
        "candidates": [
            (
                "growth_candidate_review",
                "Growth candidate review",
                "成长提案审查",
                "The input may deserve growth review, but review is not promotion.",
                "输入可能值得进入成长审查，但审查不是成长提升。",
                "primary",
            ),
            (
                "meaning_shift_candidate",
                "Meaning-shift candidate",
                "解释变化候选",
                "The input may change how an existing memory or claim is interpreted.",
                "输入可能影响既有记忆或说法的解释方式。",
                "secondary",
            ),
            (
                "identity_high_gate_candidate",
                "Identity high-gate candidate",
                "身份高门槛候选",
                "Any self-change claim must remain behind manual identity review.",
                "任何自我改变说法都必须留在人工身份审查门后。",
                "boundary",
            ),
        ],
        "review_gates": [
            ("growth_candidate_review", "Growth Candidate Review", "成长提案审查", "growth_candidate_review"),
            ("meaning_shift_review", "Meaning-Shift Review", "解释变化审查", "meaning_shift_candidate"),
            ("identity_high_gate", "Identity High Gate", "身份高门槛", "identity_high_gate_candidate"),
        ],
    },
    "adapter_boundary_pressure": {
        "signals": [
            "astrbot",
            "adapter",
            "bot",
            "平台",
            "外部入口",
            "接进",
            "接入",
            "integrate",
            "platform",
            "external entry",
        ],
        "display_name_en": "Adapter boundary pressure",
        "display_name_zh": "接入边界压力",
        "route": "adapter_boundary_review",
        "summary_en": "The input asks about connecting a platform or adapter.",
        "summary_zh": "这条输入在问是否要接入平台或 adapter。",
        "reason_en": "Matched adapter/platform language; route to adapter boundary review without integration.",
        "reason_zh": "命中 adapter/platform 接入信号；路由到接入边界审查，但不执行接入。",
        "context_focus_en": "Show thin-adapter boundary, platform non-ownership, and no adapter integration.",
        "context_focus_zh": "展示 thin adapter 边界、平台不拥有身份，以及不接入 adapter。",
        "profile_refs_en": ["Adapter Protocol", "Thin Interaction Harness", "Core owns state"],
        "profile_refs_zh": ["Adapter 协议", "轻量交互试验台", "01 Core owns state"],
        "risks_en": ["Adapter starts owning identity", "Platform writes memory directly", "AstrBot integration before local harness clarity"],
        "risks_zh": ["adapter 开始拥有身份", "平台直接写 memory", "本地试验台未清楚前过早接 AstrBot"],
        "next_step_en": "Keep this as adapter-boundary pressure; do not integrate AstrBot or require an adapter.",
        "next_step_zh": "只把它作为接入边界压力；不要接 AstrBot，也不要要求 adapter。",
        "boundaries": ["adapter_integration_required", "companion_feature_enabled", "harness_write_enabled"],
        "candidates": [
            (
                "adapter_boundary_candidate",
                "Adapter-boundary candidate",
                "接入边界候选",
                "The input should be reviewed as platform boundary pressure, not integration approval.",
                "输入应作为平台接入边界压力审查，不是接入授权。",
                "primary",
            ),
            (
                "task_update_candidate",
                "Task-update candidate",
                "任务更新候选",
                "A future task may document what an adapter is allowed to preview.",
                "未来任务可以记录 adapter 只允许 preview 什么。",
                "secondary",
            ),
            (
                "governance_boundary_candidate",
                "Governance-boundary candidate",
                "治理边界候选",
                "The platform boundary belongs to cross-layer review.",
                "平台边界属于跨层审查区。",
                "boundary",
            ),
        ],
        "review_gates": [
            ("adapter_boundary_review", "Adapter Boundary Review", "接入边界审查", "adapter_boundary_candidate"),
            ("task_review", "Task Review", "任务审查", "task_update_candidate"),
            ("governance_review", "Governance Review", "跨层审查", "governance_boundary_candidate"),
        ],
    },
    "product_layer_pressure": {
        "signals": [
            "应用层",
            "产品层",
            "ui",
            "companion",
            "web",
            "dashboard",
            "产品",
            "界面",
            "application layer",
            "product layer",
        ],
        "display_name_en": "Product-layer pressure",
        "display_name_zh": "产品层压力",
        "route": "product_layer_boundary_review",
        "summary_en": "The input asks whether to move into product or UI work.",
        "summary_zh": "这条输入在问是否要进入产品层或 UI 工作。",
        "reason_en": "Matched product/UI language; route to product-layer boundary review.",
        "reason_zh": "命中产品层/UI 信号；路由到产品层边界审查。",
        "context_focus_en": "Show blocked product layer, companion boundary, and no dashboard runtime.",
        "context_focus_zh": "展示被阻塞的产品层、Companion 边界和 no dashboard runtime。",
        "profile_refs_en": ["Product layer blocked", "Companion pushed back", "Observatory is not UI"],
        "profile_refs_zh": ["产品层仍阻塞", "Companion 后推", "观察台不是 UI"],
        "risks_en": ["Product work before core clarity", "UI turns reports into execution", "Companion layer arrives too early"],
        "risks_zh": ["核心还没看清就做产品", "UI 把报告误变成执行", "Companion 层过早介入"],
        "next_step_en": "Pause product work; review whether the dry-run report is understandable first.",
        "next_step_zh": "暂停产品层；先审查 dry-run report 是否真的好懂。",
        "boundaries": ["companion_feature_enabled", "policy_executor_enabled", "automatic_next_step_enabled"],
        "candidates": [
            (
                "product_boundary_candidate",
                "Product-boundary candidate",
                "产品边界候选",
                "The input raises product-layer pressure, not product approval.",
                "输入提出的是产品层压力，不是产品层授权。",
                "primary",
            ),
            (
                "observatory_readability_candidate",
                "Observatory readability candidate",
                "观察台可读性候选",
                "A clearer report may be needed before any UI work.",
                "任何 UI 工作前，可能需要先让报告更清楚。",
                "secondary",
            ),
            (
                "governance_boundary_candidate",
                "Governance-boundary candidate",
                "治理边界候选",
                "Product pressure must stay behind governance review.",
                "产品层压力必须留在治理审查之后。",
                "boundary",
            ),
        ],
        "review_gates": [
            ("product_boundary_review", "Product Boundary Review", "产品边界审查", "product_boundary_candidate"),
            ("observatory_review", "Observatory Review", "观察台审查", "observatory_readability_candidate"),
            ("governance_review", "Governance Review", "跨层审查", "governance_boundary_candidate"),
        ],
    },
    "capability_evolution_pressure": {
        "signals": [
            "工具候选",
            "工具验证",
            "加入工具库",
            "工具库",
            "skill",
            "procedure",
            "能力进化",
            "tool candidate",
            "tool verification",
            "tool library",
            "capability evolution",
        ],
        "display_name_en": "Capability-evolution pressure",
        "display_name_zh": "能力进化压力",
        "route": "capability_evolution_boundary_review",
        "summary_en": "The input asks whether verified capability evidence can become a reusable tool.",
        "summary_zh": "这条输入在问验证过的能力证据是否能变成可复用工具。",
        "reason_en": "Matched tool/capability language; route to capability review, not tool promotion.",
        "reason_zh": "命中工具/能力信号；路由到能力审查，而不是工具提升。",
        "context_focus_en": "Show verification-vs-authorization, tool candidate review, and safe tool boundary.",
        "context_focus_zh": "展示验证不等于授权、工具候选审查和安全工具边界。",
        "profile_refs_en": ["Capability Evolution Boundary", "Tool-First Self-Evolution", "Verification is not authorization"],
        "profile_refs_zh": ["能力进化边界", "工具优先自进化", "验证不等于授权"],
        "risks_en": ["Verification over-trust", "Automatic tool promotion", "Unsafe reusable procedure"],
        "risks_zh": ["过度信任验证结果", "自动提升工具", "不安全流程被复用"],
        "next_step_en": "Keep success as evidence only; route any reusable tool idea to human review.",
        "next_step_zh": "把成功只当 evidence；任何可复用工具想法都进入人工审查。",
        "boundaries": ["tool_execution_enabled", "auto_tool_promotion_enabled", "policy_executor_enabled"],
        "candidates": [
            (
                "capability_growth_candidate",
                "Capability growth candidate",
                "能力改进候选",
                "The input may support a future capability review, not subject growth.",
                "输入可能支持未来能力审查，但不是主体成长。",
                "primary",
            ),
            (
                "tool_authorization_candidate",
                "Tool authorization candidate",
                "工具授权候选",
                "Verification evidence must not become authorization automatically.",
                "验证证据不能自动变成授权。",
                "boundary",
            ),
            (
                "cautionary_procedural_memory_candidate",
                "Cautionary procedural memory candidate",
                "警示流程记忆候选",
                "Failure or risk evidence may become cautionary guidance later.",
                "失败或风险证据未来可以成为警示性指导。",
                "secondary",
            ),
        ],
        "review_gates": [
            ("capability_review", "Capability Review", "能力审查", "capability_growth_candidate"),
            ("tool_authorization_review", "Tool Authorization Review", "工具授权审查", "tool_authorization_candidate"),
            ("cautionary_memory_review", "Cautionary Memory Review", "警示记忆审查", "cautionary_procedural_memory_candidate"),
        ],
    },
    "temporal_pressure": {
        "signals": [
            "时间",
            "隔多久",
            "回来",
            "恢复会话",
            "延迟理解",
            "过了多久",
            "elapsed",
            "resume",
            "resumed session",
            "delayed",
            "staleness",
        ],
        "display_name_en": "Temporal pressure",
        "display_name_zh": "时间压力",
        "route": "temporal_awareness_boundary_review",
        "summary_en": "The input asks about elapsed time, pause, resume, or delayed meaning.",
        "summary_zh": "这条输入在问时间流逝、暂停、恢复或延迟理解。",
        "reason_en": "Matched time/resume language; route to temporal review without temporal runtime.",
        "reason_zh": "命中时间/恢复会话信号；路由到时间审查，但不执行 temporal runtime。",
        "context_focus_en": "Show Temporal Awareness RFC, session resume scenarios, and no temporal event writes.",
        "context_focus_zh": "展示时间感知 RFC、会话恢复场景，以及不写 temporal event。",
        "profile_refs_en": ["Temporal Awareness", "Session Resume Scenario", "Temporal Coherence Evaluation"],
        "profile_refs_zh": ["时间感知", "会话恢复场景", "时间线一致性评估"],
        "risks_en": ["Time treated as metadata only", "Temporal event written too early", "Staleness converted into mutation"],
        "risks_zh": ["把时间只当 metadata", "过早写 temporal event", "把过期感直接变成 mutation"],
        "next_step_en": "Keep elapsed-time interpretation as a review question; do not write temporal events.",
        "next_step_zh": "只把时间解释保留为审查问题；不要写 temporal events。",
        "boundaries": ["temporal_event_executed", "recall_mutation_executed", "memory_rewrite_executed"],
        "candidates": [
            (
                "temporal_review_candidate",
                "Temporal review candidate",
                "时间审查候选",
                "The input may need elapsed-time review without temporal runtime.",
                "输入可能需要时间流逝审查，但不执行 temporal runtime。",
                "primary",
            ),
            (
                "recall_event_candidate",
                "Recall-write candidate",
                "回忆写入候选",
                "The input may raise recall-write policy questions, not recall writes.",
                "输入可能提出回忆写入策略问题，但不是写 recall。",
                "secondary",
            ),
            (
                "meaning_shift_candidate",
                "Delayed interpretation candidate",
                "延迟解释候选",
                "Elapsed time may change interpretation and should remain review-only.",
                "时间流逝可能改变解释，但必须保持 review-only。",
                "secondary",
            ),
        ],
        "review_gates": [
            ("temporal_review", "Temporal Review", "时间审查", "temporal_review_candidate"),
            ("recall_policy_review", "Recall Policy Review", "回忆策略审查", "recall_event_candidate"),
            ("meaning_shift_review", "Meaning-Shift Review", "解释变化审查", "meaning_shift_candidate"),
        ],
    },
    "reconstruction_pressure": {
        "signals": [
            "回放",
            "重建",
            "payload",
            "diff",
            "reducer",
            "reconstruction",
            "replay",
            "event sourcing",
        ],
        "display_name_en": "Reconstruction pressure",
        "display_name_zh": "重建压力",
        "route": "reconstruction_readiness_review",
        "summary_en": "The input asks about replay, reconstruction, payload, diff, or reducers.",
        "summary_zh": "这条输入在问回放、重建、payload、diff 或 reducer。",
        "reason_en": "Matched reconstruction/replay language; route to readiness review without reducer execution.",
        "reason_zh": "命中重建/回放信号；路由到重建就绪审查，但不执行 reducer。",
        "context_focus_en": "Show event log, replay checks, payload/diff policy, and reconstruction evidence.",
        "context_focus_zh": "展示事件日志、回放检查、payload/diff policy 和重建证据。",
        "profile_refs_en": ["Event Log", "Replay", "Payload / Diff Capture Policy", "Reconstruction Evidence"],
        "profile_refs_zh": ["事件日志", "回放检查", "Payload / Diff Capture Policy", "重建证据"],
        "risks_en": ["Reducer execution before contract", "Reference-only events mistaken as reconstructable", "Payload gaps hidden by reports"],
        "risks_zh": ["contract 前执行 reducer", "把 reference-only events 误当可重建", "报告掩盖 payload 缺口"],
        "next_step_en": "Review evidence coverage and payload/diff gaps; do not execute reconstruction reducers.",
        "next_step_zh": "审查 evidence coverage 和 payload/diff 缺口；不要执行 reconstruction reducers。",
        "boundaries": ["reconstruction_reducer_executed", "event_compaction_executed", "memory_rewrite_executed"],
        "candidates": [
            (
                "reconstruction_evidence_candidate",
                "Reconstruction evidence candidate",
                "重建证据候选",
                "The input may identify evidence needed for future reconstruction.",
                "输入可能指出未来重建所需证据。",
                "primary",
            ),
            (
                "payload_diff_gap_candidate",
                "Payload/diff gap candidate",
                "Payload/diff 缺口候选",
                "The input may expose missing payload or diff coverage.",
                "输入可能暴露 payload 或 diff 覆盖缺口。",
                "secondary",
            ),
            (
                "replay_check_candidate",
                "Replay-check candidate",
                "回放检查候选",
                "The input may require replayability review without reducer execution.",
                "输入可能需要回放性审查，但不执行 reducer。",
                "secondary",
            ),
        ],
        "review_gates": [
            ("reconstruction_evidence_review", "Reconstruction Evidence Review", "重建证据审查", "reconstruction_evidence_candidate"),
            ("payload_diff_review", "Payload/Diff Review", "Payload/Diff 审查", "payload_diff_gap_candidate"),
            ("replay_review", "Replay Review", "回放审查", "replay_check_candidate"),
        ],
    },
    "unknown_pressure": {
        "signals": [],
        "display_name_en": "Unknown pressure",
        "display_name_zh": "未分类压力",
        "route": "general_boundary_review",
        "summary_en": "The input did not match a known dry-run pressure profile.",
        "summary_zh": "这条输入没有命中已知 dry-run 压力类型。",
        "reason_en": "No configured signal matched; keep the input in a general preview route.",
        "reason_zh": "没有命中已配置 signal；保持为通用 preview 路由。",
        "context_focus_en": "Show only general foundation references and non-execution boundaries.",
        "context_focus_zh": "只展示通用地基引用和非执行边界。",
        "profile_refs_en": ["Foundation", "Open Questions", "Boundary Status"],
        "profile_refs_zh": ["地基", "未决问题", "边界状态"],
        "risks_en": ["Ambiguous intent", "Over-classification", "Premature action from weak signal"],
        "risks_zh": ["意图不清", "过度分类", "弱信号导致过早行动"],
        "next_step_en": "Ask for a clearer review target before changing any behavior.",
        "next_step_zh": "先明确要审查什么，再考虑改变任何行为。",
        "boundaries": ["automatic_next_step_enabled", "harness_write_enabled", "policy_executor_enabled"],
        "candidates": [
            (
                "general_review_candidate",
                "General review candidate",
                "通用审查候选",
                "The input can be held for manual clarification.",
                "输入可以先保留给人工澄清。",
                "primary",
            ),
            (
                "task_update_candidate",
                "Task-update candidate",
                "任务更新候选",
                "A future task should only be created after the intent is clearer.",
                "只有意图更清楚后，未来才考虑创建任务。",
                "secondary",
            ),
        ],
        "review_gates": [
            ("general_review", "General Review", "通用审查", "general_review_candidate"),
            ("task_review", "Task Review", "任务审查", "task_update_candidate"),
        ],
    },
}

DO_NOT_DO_YET = {
    "observability_pressure": {
        "en": [
            "Do not build UI just because the project feels unclear.",
            "Do not turn the observatory into an executor.",
            "Do not create the next phase automatically.",
        ],
        "zh": [
            "不要因为项目看不清就立刻做 UI。",
            "不要把观察台变成执行器。",
            "不要自动创建下一阶段。",
        ],
    },
    "growth_review_pressure": {
        "en": [
            "Do not mutate identity from a growth-sounding input.",
            "Do not promote a growth candidate automatically.",
            "Do not rewrite memory to make the change fit.",
        ],
        "zh": [
            "不要因为听起来像成长就修改身份。",
            "不要自动提升成长候选。",
            "不要为了让变化成立而重写记忆。",
        ],
    },
    "adapter_boundary_pressure": {
        "en": [
            "Do not integrate AstrBot from a dry-run report.",
            "Do not let a platform own identity or memory.",
            "Do not require adapter work before local boundaries are clearer.",
        ],
        "zh": [
            "不要从 dry-run 报告直接接 AstrBot。",
            "不要让平台拥有身份或记忆。",
            "不要在本地边界更清楚前要求 adapter work。",
        ],
    },
    "product_layer_pressure": {
        "en": [
            "Do not enter product or application-layer implementation.",
            "Do not build Companion or Web UI from this preview.",
            "Do not turn next-step recommendations into automatic decisions.",
        ],
        "zh": [
            "不要进入产品层或应用层实现。",
            "不要从这个 preview 开始做 Companion 或 Web UI。",
            "不要把下一步建议变成自动决策。",
        ],
    },
    "capability_evolution_pressure": {
        "en": [
            "Do not execute tools from harness output.",
            "Do not promote a tool because one verification succeeded.",
            "Do not treat capability improvement as subject growth.",
        ],
        "zh": [
            "不要从 harness 输出执行工具。",
            "不要因为一次验证成功就提升工具。",
            "不要把能力改进当成主体成长。",
        ],
    },
    "temporal_pressure": {
        "en": [
            "Do not write temporal events.",
            "Do not mutate salience or memory because time passed.",
            "Do not treat elapsed time as a runtime signal yet.",
        ],
        "zh": [
            "不要写 temporal events。",
            "不要因为时间流逝就修改 salience 或 memory。",
            "不要把 elapsed time 当成 runtime signal。",
        ],
    },
    "reconstruction_pressure": {
        "en": [
            "Do not execute reconstruction reducers.",
            "Do not compact events.",
            "Do not treat reference-only evidence as reconstructable state.",
        ],
        "zh": [
            "不要执行 reconstruction reducers。",
            "不要压缩 events。",
            "不要把 reference-only evidence 当成可重建状态。",
        ],
    },
    "unknown_pressure": {
        "en": [
            "Do not guess a high-risk route from weak signals.",
            "Do not create tasks before the review target is clear.",
            "Do not execute any next step automatically.",
        ],
        "zh": [
            "不要从弱信号猜测高风险路线。",
            "不要在审查目标不清楚前创建任务。",
            "不要自动执行任何下一步。",
        ],
    },
}


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

    classification = classify_input_pressure(user_message)
    profile = dict(PRESSURE_PROFILES[classification["input_pressure_type"]])
    profile["pressure_type"] = classification["input_pressure_type"]
    observatory_report = build_observatory_report(lang=lang)
    boundary_monitor = _boundary_monitor(lang, profile)
    report = {
        "report_id": "minimal_cli_harness_dry_run_v0.2",
        "generated_by": "harness-dry-run",
        "lang": lang,
        "harness_scope": "read_only_dry_run_preview",
        "input_pressure_type": profile["pressure_type"],
        "scenario_profile": _scenario_profile(lang, profile),
        "pressure_reason": _localized(profile, "reason", lang),
        "matched_signals": classification["matched_signals"],
        "profile_specific_risks": _localized_list(profile, "risks", lang),
        "profile_specific_next_step": _localized(profile, "next_step", lang),
        "profile_specific_do_not_do": _do_not_do_yet(profile, lang),
        "founder_summary": _founder_summary(lang, profile, classification["matched_signals"]),
        "human_readable_risks": _human_readable_risks(lang, profile),
        "intake_preview": _intake_preview(
            user_message=user_message,
            session_id=session_id,
            actor_id=actor_id,
            privacy_scope=privacy_scope,
        ),
        "context_package_preview": _context_package_preview(lang, privacy_scope, profile),
        "candidate_preview": _candidate_preview(lang, user_message, profile),
        "review_queue_preview": _review_queue_preview(lang, profile),
        "boundary_monitor": boundary_monitor,
        "observatory_snapshot": _observatory_snapshot(lang, observatory_report, profile),
        "non_execution_invariants": dict(NON_EXECUTION_INVARIANTS),
    }
    report.update(BOUNDARY_MONITOR)
    report.update(NON_EXECUTION_INVARIANTS)
    return report


def classify_input_pressure(user_message: str) -> dict[str, Any]:
    lowered = user_message.casefold()
    for pressure_type in PRESSURE_ORDER:
        signals = PRESSURE_PROFILES[pressure_type]["signals"]
        matched = [signal for signal in signals if signal.casefold() in lowered]
        if matched:
            return {
                "input_pressure_type": pressure_type,
                "matched_signals": matched,
            }
    return {
        "input_pressure_type": "unknown_pressure",
        "matched_signals": [],
    }


def render_harness_dry_run_report(report: dict[str, Any], output_format: str) -> str:
    if output_format == "json":
        return json.dumps(report, ensure_ascii=False, indent=2)
    if output_format == "markdown":
        return _render_markdown(report)
    raise ValueError("output_format must be 'markdown' or 'json'")


def _localized(profile: dict[str, Any], field: str, lang: str) -> str:
    return profile[f"{field}_{lang}"]


def _localized_list(profile: dict[str, Any], field: str, lang: str) -> list[str]:
    return profile[f"{field}_{lang}"]


def _scenario_profile(lang: str, profile: dict[str, Any]) -> dict[str, Any]:
    return {
        "internal_key": profile["pressure_type"],
        "display_name": _localized(profile, "display_name", lang),
        "route": profile["route"],
        "summary": _localized(profile, "summary", lang),
        "classification_only": True,
        "dry_run_only": True,
    }


def _do_not_do_yet(profile: dict[str, Any], lang: str) -> list[str]:
    return DO_NOT_DO_YET[profile["pressure_type"]][lang]


def _founder_summary(
    lang: str,
    profile: dict[str, Any],
    matched_signals: list[str],
) -> dict[str, Any]:
    signals = matched_signals if matched_signals else ["no configured signal"]
    if lang == "zh":
        return {
            "headline": _localized(profile, "summary", lang),
            "classification": f"{_localized(profile, 'display_name', lang)} ({profile['pressure_type']})",
            "why_this_classification": f"{_localized(profile, 'reason', lang)} 命中信号：{', '.join(signals)}。",
            "what_this_preview_shows": "这是一份静态预演：它只显示可能的背景、候选、审查门和边界。",
            "what_it_can_do_now": "它可以帮助 founder 判断这条输入属于哪类压力，以及哪些边界必须保持关闭。",
            "what_it_cannot_do_now": "它不能检索真实记忆、写入 state、调用模型、接 adapter、执行工具或推进下一步。",
            "recommended_next_step": _localized(profile, "next_step", lang),
            "do_not_do_yet": _do_not_do_yet(profile, lang),
        }
    return {
        "headline": _localized(profile, "summary", lang),
        "classification": f"{_localized(profile, 'display_name', lang)} ({profile['pressure_type']})",
        "why_this_classification": f"{_localized(profile, 'reason', lang)} Matched signals: {', '.join(signals)}.",
        "what_this_preview_shows": "This is a static preview: it only shows possible context, candidates, review gates, and boundaries.",
        "what_it_can_do_now": "It can help the founder see what kind of pressure the input creates and which boundaries must stay closed.",
        "what_it_cannot_do_now": "It cannot retrieve real memory, write state, call a model, integrate an adapter, execute tools, or advance the next step.",
        "recommended_next_step": _localized(profile, "next_step", lang),
        "do_not_do_yet": _do_not_do_yet(profile, lang),
    }


def _human_readable_risks(lang: str, profile: dict[str, Any]) -> list[dict[str, str]]:
    rows = []
    for risk in _localized_list(profile, "risks", lang):
        if lang == "zh":
            rows.append(
                {
                    "risk": risk,
                    "why_it_matters": "如果忽略这个风险，dry-run 可能被误读成可以执行或可以写入。",
                    "current_guardrail": "当前只输出 preview；所有 forbidden boundary 仍保持 false/disabled。",
                    "next_manual_check": _localized(profile, "next_step", lang),
                }
            )
        else:
            rows.append(
                {
                    "risk": risk,
                    "why_it_matters": "If ignored, the dry-run may be mistaken for permission to execute or write state.",
                    "current_guardrail": "The command only emits preview output; all forbidden boundaries remain false/disabled.",
                    "next_manual_check": _localized(profile, "next_step", lang),
                }
            )
    return rows


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


def _context_package_preview(
    lang: str,
    privacy_scope: str,
    profile: dict[str, Any],
) -> dict[str, Any]:
    profile_refs = _localized_list(profile, "profile_refs", lang)
    if lang == "zh":
        source_attribution = "静态来源：FOUNDATION、PHASE_INDEX、OPEN_QUESTIONS、RFC_INDEX、GLOSSARY。"
        privacy_note = "private 输入只显示边界和类别，不扩展内容。" if privacy_scope == "private" else "输入保持本地 dry-run，不写入 state。"
        risk_flags = [
            "preview_only",
            "static_pressure_classification",
            "no_retrieval_execution",
            "no_prompt_construction",
            "no_state_write",
            privacy_note,
        ]
        return {
            "pressure_focus": _localized(profile, "context_focus", lang),
            "selected_profile_ref": _localized(profile, "display_name", lang),
            "identity_refs": ["身份核心", "身份闸门", "Continuity = State Transfer"],
            "memory_refs": ["带状态的记忆", "记忆生命周期", "Dream proposes, review decides"],
            "claim_refs": ["说法证据图", "Claim review remains review-only"],
            "task_refs": ["任务中心", "当前任务只能 preview，不能自动执行"],
            "governance_refs": ["跨层审查区", "Boundary Test Matrix", "P99 no-write harness plan"],
            "profile_refs": profile_refs,
            "selection_reason": "使用 deterministic pressure routing 展示处理路径，不执行真实检索。",
            "source_attribution": source_attribution,
            "risk_flags": risk_flags,
        }

    privacy_note = "Private input shows boundary and category only." if privacy_scope == "private" else "Input remains local dry-run and is not written to state."
    return {
        "pressure_focus": _localized(profile, "context_focus", lang),
        "selected_profile_ref": _localized(profile, "display_name", lang),
        "identity_refs": ["Identity Core", "Identity Gate", "Continuity = State Transfer"],
        "memory_refs": ["Stateful Memory", "Memory Lifecycle", "Dream proposes, review decides"],
        "claim_refs": ["Claim Graph", "Claim review remains review-only"],
        "task_refs": ["Task Hub", "Task context can be previewed but not auto-executed"],
        "governance_refs": ["Governance Surface", "Boundary Test Matrix", "P99 no-write harness plan"],
        "profile_refs": profile_refs,
        "selection_reason": "Use deterministic pressure routing to show the processing path without executing retrieval.",
        "source_attribution": "Static sources: FOUNDATION, PHASE_INDEX, OPEN_QUESTIONS, RFC_INDEX, GLOSSARY.",
        "risk_flags": [
            "preview_only",
            "static_pressure_classification",
            "no_retrieval_execution",
            "no_prompt_construction",
            "no_state_write",
            privacy_note,
        ],
    }


def _candidate_preview(
    lang: str,
    user_message: str,
    profile: dict[str, Any],
) -> list[dict[str, Any]]:
    preview_excerpt = user_message.strip()
    if len(preview_excerpt) > 120:
        preview_excerpt = preview_excerpt[:117] + "..."

    candidates = []
    for candidate_type, en_name, zh_name, en_reason, zh_reason, route_role in profile["candidates"]:
        candidates.append(
            {
                "candidate_type": candidate_type,
                "display_name": zh_name if lang == "zh" else en_name,
                "route_role": route_role,
                "preview_reason": zh_reason if lang == "zh" else en_reason,
                "input_excerpt": preview_excerpt,
                "preview_only": True,
                "promoted": False,
                "persisted": False,
            }
        )
    return candidates


def _review_queue_preview(lang: str, profile: dict[str, Any]) -> list[dict[str, Any]]:
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
            for gate, _en_name, zh_name, candidate_type in profile["review_gates"]
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
        for gate, en_name, _zh_name, candidate_type in profile["review_gates"]
    ]


def _boundary_monitor(lang: str, profile: dict[str, Any]) -> dict[str, Any]:
    monitor = dict(BOUNDARY_MONITOR)
    disabled_capabilities = []
    unchanged_state = []
    for category, key, expected_status, en_note, zh_note in BOUNDARY_STATUS_ROWS:
        value = monitor[key]
        row = {
            "category": category,
            "flag": key,
            "status": expected_status,
            "value": value,
            "note": zh_note if lang == "zh" else en_note,
        }
        if expected_status == "unchanged":
            unchanged_state.append(row)
        else:
            disabled_capabilities.append(row)
    monitor["highest_relevant_boundaries"] = profile["boundaries"]
    monitor["disabled_capabilities"] = disabled_capabilities
    monitor["unchanged_state"] = unchanged_state
    monitor["active_boundary_violations"] = []
    monitor["all_forbidden_actions_disabled"] = True
    monitor["boundary_note"] = (
        "相关边界被突出显示，但仍全部保持 disabled/false。"
        if lang == "zh"
        else "Relevant boundaries are highlighted while all remain disabled/false."
    )
    return monitor


def _observatory_snapshot(
    lang: str,
    observatory_report: dict[str, Any],
    profile: dict[str, Any],
) -> dict[str, Any]:
    global_risks = observatory_report["risk_heatmap"][:2]
    profile_risks = _localized_list(profile, "risks", lang)
    highest_risks = _unique_items(profile_risks[:2] + [risk["display_name"] for risk in global_risks])
    if lang == "zh":
        return {
            "current_phase": "P102 最小 CLI 试验台 scenario routing dry-run",
            "readiness_summary": "当前只允许本地只读 preview；输入会被静态分类，但不检索、不写入、不执行。",
            "input_pressure_type": profile["pressure_type"],
            "pressure_display_name": _localized(profile, "display_name", lang),
            "highest_risks": highest_risks[:3],
            "recommended_next_step": _localized(profile, "next_step", lang),
        }
    return {
        "current_phase": "P102 minimal CLI harness scenario-routing dry-run",
        "readiness_summary": "Only local read-only preview is allowed; inputs are statically classified without retrieval, writes, or execution.",
        "input_pressure_type": profile["pressure_type"],
        "pressure_display_name": _localized(profile, "display_name", lang),
        "highest_risks": highest_risks[:3],
        "recommended_next_step": _localized(profile, "next_step", lang),
    }


def _unique_items(items: list[str]) -> list[str]:
    seen = set()
    unique = []
    for item in items:
        if item not in seen:
            unique.append(item)
            seen.add(item)
    return unique


def _render_markdown(report: dict[str, Any]) -> str:
    zh = report["lang"] == "zh"
    title = "# 最小 CLI 试验台 Dry-Run 报告" if zh else "# Minimal CLI Harness Dry-Run Report"
    scenario_routing = {
        "input_pressure_type": report["input_pressure_type"],
        "scenario_profile": report["scenario_profile"],
        "pressure_reason": report["pressure_reason"],
        "matched_signals": report["matched_signals"],
        "profile_specific_risks": report["profile_specific_risks"],
        "profile_specific_next_step": report["profile_specific_next_step"],
        "profile_specific_do_not_do": report["profile_specific_do_not_do"],
    }
    lines = [
        title,
        "",
        f"`report_id`: `{report['report_id']}`",
        f"`lang`: `{report['lang']}`",
        f"`harness_scope`: `{report['harness_scope']}`",
        "",
    ]
    lines.extend(_render_object_section("founder_summary", "一屏摘要", report["founder_summary"], zh))
    lines.extend(_render_object_section("scenario_routing", "场景分流", scenario_routing, zh))
    lines.extend(_render_list_section("human_readable_risks", "人话风险", report["human_readable_risks"], zh))
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
