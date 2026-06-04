# Research Notes Index / 研究记录索引

English version: [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md)

Status: `document-only`, `research-index`, `non-runtime`.

P78 索引原始中文研究记录，并把它映射到当前 foundation documents。它不新增 theory、
runtime behavior、schemas、CLI commands、validators、policy executors、
identity mutation、memory rewrite、Temporal Awareness runtime、adapter work、UI、
cloud rollout 或 product behavior。

## Index Rule / 索引规则

```text
research notes preserve origin.
an index improves traceability.
origin ideas are not implementation approval.
```

使用本文档回答：这个 foundation idea 从哪里来？当前由哪些文档承载？哪些仍只是长期愿景？

## Source Documents / 源文档

| Source | Role | Reading Use |
|---|---|---|
| [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md) | 原始中文 source notes | 完整保存最初两条思想链。 |
| [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md) | Vision synthesis | 把第一条思想链整理成项目愿景。 |
| [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md) | Life-history synthesis | 把第二条思想链整理成 Identity Seed 边界。 |
| [THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md) / [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md) | later synthesis and phase planning | 把早期理论接到 implementation-phase planning。 |
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) / [CTM_TEMPORAL_DYNAMICS_RFC_ZH.md](./CTM_TEMPORAL_DYNAMICS_RFC_ZH.md) | External inspiration RFC | 把 Continuous Thought Machines 启发映射为未来 temporal-dynamics vocabulary，不实现 CTM。 |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) / [TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md) | External inspiration evaluation plan | 把 CTM-inspired temporal vocabulary 转成 deterministic evaluation scenarios，不实现 metrics 或 runtime。 |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) / [DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md) | Review-planning RFC | 定义 tick 和 review-depth vocabulary，不执行 thought loop。 |
| [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) / [THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md) | Storage-boundary RFC | 定义未来 trace candidates 可以摘要什么，同时不存储 hidden chain-of-thought 或 private reasoning。 |
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) / [THIN_INTERACTION_HARNESS_RFC_ZH.md](./THIN_INTERACTION_HARNESS_RFC_ZH.md) | Harness-boundary RFC | 在任何 interaction implementation 前，定义 preview-only local harness boundary。 |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) / [CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md](./CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md) | Intake contract RFC | 定义 future preview envelope，不做 adapter ingest、context building 或 event writes。 |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) / [CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md](./CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md) | Context preview RFC | 定义 selected 和 omitted context reference explanations，不执行 retrieval 或 activation trace writes。 |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) / [REVIEW_QUEUE_PREVIEW_RFC_ZH.md](./REVIEW_QUEUE_PREVIEW_RFC_ZH.md) | Queue preview RFC | 定义 candidate queue preview vocabulary，不执行 lifecycle 或 approval。 |
| [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) / [SESSION_RESUME_SCENARIO_PLAN_ZH.md](./SESSION_RESUME_SCENARIO_PLAN_ZH.md) | Resume scenario plan | 定义 deterministic resume scenarios，不写 temporal events，也不做 resume runtime。 |
| [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) / [CORE_INTERACTION_HARNESS_ROADMAP_ZH.md](./CORE_INTERACTION_HARNESS_ROADMAP_ZH.md) | Harness roadmap | 评估 future minimal CLI harness readiness，但不批准 implementation。 |
| [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md) / [HARNESS_TRANSITION_SUMMARY_ZH.md](./HARNESS_TRANSITION_SUMMARY_ZH.md) | Harness transition summary | 收束 P82-P90 planning，并在 explicit approval 前继续阻塞 implementation。 |
| [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) / [TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md) | External inspiration RFC | 把 Yunjue / zero-start in-situ self-evolving agent 思想翻译成 review-only capability evolution vocabulary，不执行工具。 |
| [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) / [CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md) | Boundary RFC | 定义 capability evolution 的 allowed / forbidden scope，不实现 tool runtime 或 promotion。 |
| [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) / [VISUAL_NAMING_GUIDE_ZH.md](./VISUAL_NAMING_GUIDE_ZH.md) | Founder-facing vocabulary guide | 把内部英文术语映射成中文显示名，不实现 dashboard、observability CLI 或 product UI。 |
| [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) / [FOUNDATION_OBSERVATORY_REPORT_ZH.md](./FOUNDATION_OBSERVATORY_REPORT_ZH.md) | Founder-facing observatory report | 用 Markdown 总结 foundation status，不实现 dashboard、CLI、status API 或 product UI。 |
| [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md) / [MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md](./MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md) | CLI planning RFC | 定义 read-only observatory CLI report boundary，之后在 P96 中窄范围实现。 |
| `python3 -m one_core.cli foundation-observatory-report` | Read-only observatory CLI | 实现 P96 static founder-facing report generator，不做 dashboard runtime、policy execution、state mutation 或 phase creation。 |
| [OBSERVATORY_USABILITY_REVIEW.md](./OBSERVATORY_USABILITY_REVIEW.md) / [OBSERVATORY_USABILITY_REVIEW_ZH.md](./OBSERVATORY_USABILITY_REVIEW_ZH.md) | Usability review | 审查 founder-facing readability，并继续阻塞 harness implementation。 |
| [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md) / [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md) | Harness implementation plan | 规划 no-write dry-run CLI pressure test，之后在 P100 中窄范围实现。 |
| `python3 -m one_core.cli harness-dry-run` | Read-only harness dry-run CLI | 实现 P100 local interaction-path preview，不写 state、不调用模型、不调用外部 API、不接 adapter、不进入产品层。 |
| [HARNESS_USABILITY_REVIEW.md](./HARNESS_USABILITY_REVIEW.md) / [HARNESS_USABILITY_REVIEW_ZH.md](./HARNESS_USABILITY_REVIEW_ZH.md) | Harness usability review | 审查 P100 dry-run 是否帮助 founder 看懂 input flow，并继续阻塞 real routing、retrieval、adapters 和 product work。 |

## Original Idea Chains / 原始思想链

| Chain | Source Range | Core Question | Current Foundation Carrying It |
|---|---|---|---|
| Persistent Intelligence | `RESEARCH_NOTES_ZH.md` 第一部分 | AI 如何从一次回答变成持续存在？ | [VISION.md](./VISION.md), [FOUNDATION.md](./FOUNDATION.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md) |
| Artificial Life History | `RESEARCH_NOTES_ZH.md` 第二部分 | 01 的历史应该从哪里来？ | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [DECISIONS.md](./DECISIONS.md) |

## First Chain Map: Persistent Intelligence / 第一条思想链

| Source Theme | Meaning In Original Notes | Current Foundation Artifact | Current Status |
|---|---|---|---|
| Continuity != Memory | Continuity 需要的不只是 remembered facts。 | [README.md](./README.md), [FOUNDATION.md](./FOUNDATION.md), [DECISIONS.md](./DECISIONS.md) | `accepted-foundation` |
| State Transfer | living state 必须穿过时间迁移。 | [VISION.md](./VISION.md), [STATE_SCHEMA.md](./STATE_SCHEMA.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md) | `accepted-foundation` |
| Fact / Working / Identity / Emotional / Dream state | Continuity 有多层 transferable state。 | [VISION.md](./VISION.md), [STATE_SCHEMA.md](./STATE_SCHEMA.md), [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) | `foundation-vocabulary` |
| Dream Engine | Dream 把 experience 组织成 meaning。 | [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | `accepted-boundary`: Dream proposes, review decides |
| Memory Lifecycle | Episodes 可成为 semantic memory、identity memory，或被遗忘。 | [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md), [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md), [GLOSSARY.md](./GLOSSARY.md) | `bounded-semantics` |
| Identity First Architecture | Conversation 不是 identity；identity 先于 session 存在。 | [ARCHITECTURE.md](./ARCHITECTURE.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | `accepted-boundary` |
| Three Meta Questions | 我是谁、我在哪、我在干什么。 | [VISION.md](./VISION.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md) | `foundation-vocabulary` |
| Cognitive Drift | identity/context/intent 丢失会造成 drift。 | [EVALUATION.md](./EVALUATION.md), [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md), [GLOSSARY.md](./GLOSSARY.md) | `review-vocabulary` |
| Personality as interpreter | Personality 不是 memory sum，而是 memory interpreter。 | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md), [GLOSSARY.md](./GLOSSARY.md) | `bounded-semantics` |
| Identity Growth | Growth 来自 experience、reflection、Dream 和 review。 | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md), [DECISIONS.md](./DECISIONS.md) | `blocked-runtime`: growth candidate is not growth |
| Conflict-driven growth | Conflict 可以推动 review 和 meaning shift。 | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `future-contract-needed` |
| Social Cognition Layer | 多主体和社会上下文可能深化成长。 | [RISK_REGISTER.md](./RISK_REGISTER.md), [DECISIONS.md](./DECISIONS.md) | `blocked-runtime` in foundation loop |
| Cognitive Ecology | interacting persistent subjects 的长期愿景。 | [VISION.md](./VISION.md), [NON_CLAIMS.md](./NON_CLAIMS.md) | `long-term-vision`, not product work |
| Artificial Personality Engineering | 研究 artificial subject 如何成为自己。 | [VISION.md](./VISION.md), [FOUNDATION.md](./FOUNDATION.md) | `research-frame` |
| Continuity Era | 项目属于 continuity，不只属于 capability 或 agents。 | [README.md](./README.md), [VISION.md](./VISION.md) | `accepted-foundation` |

## External Inspiration Map / 外部启发地图

| External Theme | Current Use | Current Foundation Artifact | Current Status |
|---|---|---|---|
| CTM-inspired Temporal Dynamics | time-varying internal state 可能启发未来 continuity review。 | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `external-inspiration`, `RFC-only`, not runtime |
| Temporal Coherence Evaluation | CTM-inspired vocabulary 需要 deterministic scenarios，之后才能讨论 runtime。 | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md), [GLOSSARY.md](./GLOSSARY.md) | `evaluation-plan`, `RFC-only`, not runtime |
| Deliberation Tick / Review Depth | harness preview 前，review effort 需要 risk calibration。 | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `review-planning`, `RFC-only`, not runtime |
| Thought Trace Storage Policy | trace language 需要 hard boundary，防止 hidden reasoning capture。 | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md), [GLOSSARY.md](./GLOSSARY.md) | `storage-boundary`, `RFC-only`, not runtime |
| Thin Interaction Harness | foundation 需要一个通向 interaction 的窄桥，但不能进入 product 或 runtime。 | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md), [RFC_INDEX.md](./RFC_INDEX.md) | `harness-boundary`, `RFC-only`, not runtime |
| Conversation Intake Contract | context preview 前，input 需要 source、actor、session、privacy 和 boundary vocabulary。 | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md), [ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) | `contract-rfc`, `preview-only`, not adapter ingest |
| Context Package Preview | thin harness 变得安全前，context selection 需要 explainability。 | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md), [API.md](./API.md) | `preview-rfc`, not retrieval execution |
| Review Queue Preview | 讨论 review queue 前，candidate pressure 需要 ordering vocabulary。 | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md), [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | `preview-rfc`, not lifecycle execution |
| Session Resume Scenario Plan | 任何 harness runtime 前，resume 需要 deterministic elapsed-time scenarios。 | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md), [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | `scenario-plan`, not temporal runtime |
| Core Interaction Harness Roadmap | foundation 现在可以讨论 future fixture-first CLI harness，但 implementation 仍 blocked。 | [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md), [RISK_REGISTER.md](./RISK_REGISTER.md) | `roadmap`, not implementation approval |
| Harness Transition Summary | future P91 contract work 前，P82-P90 需要 compact closeout。 | [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md), [RFC_INDEX.md](./RFC_INDEX.md) | `summary`, not implementation approval |
| Tool-First Self-Evolution | Yunjue-style zero-start tool evolution 提示应先在 feedback 可验证的能力层演化。 | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `external-inspiration`, `RFC-only`, not tool runtime |
| Capability Evolution Boundary | tool-first capability evolution 在任何 verification 或 library policy work 前需要明确 allowed / forbidden scope。 | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md), [RISK_REGISTER.md](./RISK_REGISTER.md) | `boundary-rfc`, not tool execution |
| Visual Naming Guide | founder-facing views 需要朴素中文标签，同时不能丢失精确的内部英文键。 | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md), [GLOSSARY.md](./GLOSSARY.md) | `naming-guide`, not UI or dashboard runtime |
| Foundation Observatory Report | 任何 dashboard 或 CLI plan 前，创始人需要一份可读 Markdown snapshot。 | [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `report-only`, not runtime observability |
| Minimal Observatory CLI | generated observatory report 现在需要保持 read-only 和 founder-facing。 | [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md), [OBSERVATORY_USABILITY_REVIEW.md](./OBSERVATORY_USABILITY_REVIEW.md), [GLOSSARY.md](./GLOSSARY.md) | `implemented-static-report`, `readability-improved`, not dashboard runtime |
| Minimal CLI Harness Dry-Run | interaction pressure 现在有 local no-write preview command，但没有 runtime、adapter、model call 或 product surface。 | [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md), [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `implemented-static-dry-run`, not harness runtime |

## Second Chain Map: Artificial Life History / 第二条思想链

| Source Theme | Meaning In Original Notes | Current Foundation Artifact | Current Status |
|---|---|---|---|
| Assigned false history | 预写 biography 只制造 narrative appearance，不制造 lived continuity。 | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [NON_CLAIMS.md](./NON_CLAIMS.md) | `accepted-boundary` |
| Generated life history | History 应从 experience passing through state 中长出。 | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [DECISIONS.md](./DECISIONS.md) | `accepted-foundation` |
| Identity Seed | 起点应是 seed，不是 complete fictional life。 | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [FOUNDATION.md](./FOUNDATION.md) | `accepted-foundation` |
| Over-complete history risk | 过度完整的 assigned biography 会困住 identity。 | [NON_CLAIMS.md](./NON_CLAIMS.md), [RISK_REGISTER.md](./RISK_REGISTER.md) | `watch` |
| History earns identity change | 只有穿过 state、conflict、Dream 和 review 的 experience 才有资格改变“我是谁”。 | [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md), [DECISIONS.md](./DECISIONS.md) | `accepted-boundary` |

## Current Interpretation / 当前解释

Research notes 是 source material，不是当前 implementation plan。

今天稳定的是：

- Continuity is State Transfer, not retrieval。
- 01 begins as Identity Seed, not full fictional biography。
- Identity Core is protected by gate。
- Dream proposes; review decides。
- Growth candidate is not growth。
- Review object is not execution。

仍属 future 或 blocked：

- Social Cognition Layer；
- Cognitive Ecology as product or multi-subject system；
- companion 或 relationship memory；
- Temporal Awareness runtime；
- automatic growth or drift classification；
- CTM runtime 或 model training；
- thought loop execution；
- tool execution 或 automatic tool generation；
- automatic tool promotion 或 tool library mutation；
- self-modifying runtime 或 unreviewed dependency installation；
- identity mutation、memory rewrite、payload capture、reducer execution。

## Reading Order / 阅读顺序

追溯 origin 时：

1. 阅读 [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md)，了解原始两条思想链。
2. 阅读 [VISION.md](./VISION.md)，了解 Persistent Intelligence synthesis。
3. 阅读 [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md)，了解 artificial life-history synthesis。
4. 阅读 [FOUNDATION.md](./FOUNDATION.md)、[CONCEPT_MAP.md](./CONCEPT_MAP.md)
   和 [DECISIONS.md](./DECISIONS.md)，了解当前稳定边界。
5. 阅读 [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) 和 [RISK_REGISTER.md](./RISK_REGISTER.md)，了解哪些仍 open、watch 或 blocked。
6. 阅读 [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) 时，只把它当作
   temporal dynamics vocabulary 的 external-inspiration RFC，不要当作 CTM implementation
   approval。
7. 阅读 [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md)
   时，只把它当作 future evaluation plan，不要当作 implemented tests 或 runtime metrics。
8. 阅读 [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md)
   时，只把它当作 review-depth vocabulary，不要当作 thought-loop execution。
9. 阅读 [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md)
   时，只把它当作 storage-boundary policy，不要当作 trace storage 或 hidden reasoning capture。
10. 阅读 [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md)
    时，只把它当作 future harness boundary，不要当作 CLI、UI、adapter 或 runtime implementation。
11. 阅读 [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md)
    时，只把它当作 intake envelope contract，不要当作 adapter ingest、API、CLI、context
    building 或 event write behavior。
12. 阅读 [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md)
    时，只把它当作 context-selection explanation vocabulary，不要当作 retrieval、prompt
    construction、activation trace persistence 或 context mutation。
13. 阅读 [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md)
    时，只把它当作 candidate preview 和 ordering vocabulary，不要当作 queue runtime、lifecycle
    execution、approval 或 mutation。
14. 阅读 [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md)
    时，只把它当作 deterministic scenario planning，不要当作 Temporal Awareness runtime、
    temporal event writes、memory decay、salience mutation 或 resume automation。
15. 阅读 [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md)
    时，只把它当作 readiness planning，不要当作 harness implementation approval、CLI commands、
    schemas、tests、adapters、UI 或 runtime work。
16. 阅读 [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md)
    时，把它当作 P82-P90 closeout，不要当作进入 P91 或实现 harness 的许可。
17. 阅读 [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md)
    时，只把它当作 tool-first capability evolution RFC，不要当作 tool execution、tool generation、
    tool promotion、policy execution 或 identity mutation approval。
18. 阅读 [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md)
    时，只把它当作 capability boundary vocabulary，不要当作 tool authorization、verification
    implementation、safe library policy 或 runtime approval。
19. 阅读 [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) 时，只把它当作
    founder-facing naming guide，不要当作 dashboard implementation、Web UI、
    product layer 或 Foundation Observatory runtime。
20. 阅读 [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md)
    时，只把它当作 Markdown founder-facing report，不要当作 dashboard runtime、status API、
    product UI 或 runtime monitor。
21. 阅读 [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md)
    时，把它当作 P96 read-only command 背后的 boundary plan，不要当作 observability executor、
    dashboard runtime、status API 或 phase automation 的许可。
22. 阅读 [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md)
    时，把它当作 P100 read-only `harness-dry-run` command 背后的 boundary plan，不要当作
    harness runtime、model calls、external API calls、adapter integration、product layer 或 P101 approval。

## P78 Non-Execution Statement / P78 非执行声明

P78 不实现：

- new research theory；
- social cognition layer；
- cognitive ecology；
- companion 或 relationship memory；
- product behavior；
- runtime changes；
- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- tool execution；
- automatic tool generation；
- automatic tool promotion；
- policy executor；
- self-modifying runtime；
- unreviewed dependency installation；
- Web UI；
- dashboard runtime；
- Foundation Observatory runtime；
- 带 runtime monitoring、enforcement 或 execution 的 observability CLI；
- status API；
- 超出 P96 read-only static command 的 runtime report generator；
- observability executor；
- automatic roadmap execution；
- automatic next phase creation；
- 超出 P100 read-only dry-run command 的 harness implementation；
- 超出 P100 read-only dry-run command 的 harness runtime；
- model calls from harness work；
- external API calls from harness work；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- UI、AstrBot、adapter integration、cloud rollout 或 product layer。
