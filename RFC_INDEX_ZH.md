# RFC Index / RFC 索引

English version: [RFC_INDEX.md](./RFC_INDEX.md)

状态：`document-only`、`index`、`non-runtime`。

P68 启动了对 P54-P67 期间形成的 foundation RFC、policy、review、audit 和 matrix
文档的索引。后续 maintenance phases 会加入 review artifacts，但不改变 index rule。本文件
不新增 runtime behavior、schemas、CLI commands、validation rules、adapters、
product surfaces、event writes、reducers、payload capture、identity mutation、
memory rewrite 或 growth execution。

## Index Rule / 索引规则

```text
an RFC defines a review surface.
an RFC does not approve execution.
an index improves navigation.
an index does not change architecture.
```

P68 存在的原因是：foundation layer 已经有许多 review artifacts。如果没有一个统一索引，
后续工作很容易把分散的 RFC 语言误读成 implementation approval。

## Foundation Integrity And Governance / 基础完整性与治理

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P54 | [FOUNDATION_INTEGRITY_AUDIT.md](./FOUNDATION_INTEGRITY_AUDIT.md) / [ZH](./FOUNDATION_INTEGRITY_AUDIT_ZH.md) | audit | stable review | 检查 foundation principles、boundaries 和 risks 是否仍一致。 | runtime enforcement |
| P55 | [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md) / [ZH](./CONCEPT_OVERLAP_REVIEW_ZH.md) | review | stable boundary review | 为概念重叠处指定 primary ownership。 | concept deletion 或 schema change |
| P56 | [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) / [ZH](./BOUNDARY_TEST_MATRIX_ZH.md) | matrix | stable doc gate | 列出 foundation allowed / forbidden outputs。 | runtime test expansion |
| P57 | [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) / [ZH](./OPEN_QUESTIONS_TRIAGE_ZH.md) | triage | active routing | 把 open questions 分为 safe RFC、watch items 和 blocked runtime work。 | closing the questions |
| P67 | [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) / [ZH](./FOUNDATION_ROADMAP_ZH.md) | roadmap | active guidance | 综合 stable foundation、blocked runtime work、future dependencies 和 low-risk backlog。 | runtime authorization |
| P76 | [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) / [ZH](./FOUNDATION_REVIEW_CHECKLIST_ZH.md) | manual checklist | phase review gate | 把 boundary、risk、RFC、bilingual、verification 和 commit checks 转成 human review gate。 | automated executor |
| P79 | [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md) / [ZH](./BILINGUAL_CONSISTENCY_REVIEW_ZH.md) | review | manual consistency record | 记录 paired-document、status、link、summary 和 blocked-boundary alignment。 | automated translation checker |
| P80 | [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md) / [ZH](./FOUNDATION_MAINTENANCE_REVIEW_ZH.md) | review | cycle closure | 记录 P54-P80 的 maintained artifacts、residual gaps、residual risks 和 stop condition。 | implementation approval |

## Stateful Memory And Growth Semantics / 状态化记忆与成长语义

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P58 | [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) / [ZH](./TEMPORAL_AWARENESS_RFC_ZH.md) | future RFC | future direction | 把 elapsed time 作为可能的 subject-state evidence 来研究。 | Temporal Awareness runtime |
| P59 | [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) / [ZH](./RECALL_EVENT_WRITE_POLICY_RFC_ZH.md) | policy RFC | blocked write policy | 定义未来 recall event write thresholds。 | recall event writes |
| P60 | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) / [ZH](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md) | policy | review policy | 定义 meaning-shift review 所需的 minimum encoding references。 | new memory store |
| P61 | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) / [ZH](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md) | lifecycle RFC | future review-object policy | 定义 future review-object states，例如 deferred、archived、quarantined。 | growth lifecycle execution |
| P62 | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) / [ZH](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md) | boundary RFC | review vocabulary | 区分 productive drift、random drift、identity-threatening drift 和 collapse。 | automatic drift classifier |
| P81 | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) / [ZH](./CTM_TEMPORAL_DYNAMICS_RFC_ZH.md) | future RFC | RFC-only mapping | 把 CTM-inspired temporal dynamics 翻译成 symbolic foundation vocabulary。 | CTM runtime 或 temporal event execution |
| P82 | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) / [ZH](./TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md) | evaluation plan | RFC-only evaluation design | 为 temporal coherence vocabulary 定义 deterministic scenarios 和 future signals。 | temporal runtime 或 thought loop execution |
| P83 | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) / [ZH](./DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md) | future RFC | review-depth policy vocabulary | 定义 deliberation tick、review depth 和 risk-level planning boundaries。 | tick runtime 或 thought loop execution |
| P84 | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) / [ZH](./THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md) | policy RFC | storage-boundary policy | 定义未来 trace 可以摘要什么，以及哪些内容绝不能被存储。 | hidden chain-of-thought capture 或 trace storage |
| P85 | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) / [ZH](./THIN_INTERACTION_HARNESS_RFC_ZH.md) | future RFC | harness boundary | 在任何 harness implementation 前，定义 preview-only interaction surfaces。 | product、adapter、UI 或 mutation path |
| P86 | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) / [ZH](./CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md) | contract RFC | intake envelope boundary | 定义未来 conversation intake preview fields，但不做 adapter ingest 或 writes。 | conversation runtime、adapter ingest 或 event write |
| P87 | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) / [ZH](./CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md) | future RFC | context preview boundary | 为 future harness previews 定义 selected 与 omitted context reference explanations。 | retrieval as continuity 或 activation trace writes |
| P88 | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) / [ZH](./REVIEW_QUEUE_PREVIEW_RFC_ZH.md) | future RFC | review queue preview | 定义 candidate preview types、ordering signals、review depth 和 blocked items。 | lifecycle execution、approval 或 mutation |
| P89 | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) / [ZH](./SESSION_RESUME_SCENARIO_PLAN_ZH.md) | scenario plan | resume simulation plan | 使用 simulated elapsed time 定义 deterministic session resume scenarios。 | Temporal Awareness runtime 或 temporal event writes |
| P90 | [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) / [ZH](./CORE_INTERACTION_HARNESS_ROADMAP_ZH.md) | roadmap | harness readiness roadmap | 评估未来 minimal CLI harness readiness 和 gates。 | harness implementation 或 approval |
| P82-P90 | [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md) / [ZH](./HARNESS_TRANSITION_SUMMARY_ZH.md) | summary | transition closure | 总结从 temporal concept safety 到 future harness readiness 的 planning bridge。 | P91 implementation approval |

## Capability Evolution And Tool Boundary / 能力演化与工具边界

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P91 | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) / [ZH](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md) | future RFC | capability evolution boundary | 把 Yunjue / zero-start tool-first self-evolution 翻译成 review-only capability evolution vocabulary。 | tool execution、auto tool generation、auto promotion、policy executor 或 identity growth |

## Exploration And Subject Boundary / 探索与主体边界

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P63 | [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) / [ZH](./EXPLORATION_SERENDIPITY_RFC_ZH.md) | future RFC | future direction | 把 exploration 和 serendipity 定义为 record-only 或 review-only signals。 | exploration engine 或 companion feature |
| P64 | [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) / [ZH](./SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md) | boundary RFC | future boundary | 区分 protected subject anchor 和 evolvable world orientation。 | Identity Core rewrite |

## Reconstruction Readiness / 可重建准备度

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P65 | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) / [ZH](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md) | contract RFC | future contract | 定义未来 reconstruction reducer contract 必须说明什么。 | reducer execution |
| P66 | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) / [ZH](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md) | policy RFC | future policy | 定义 payload、diff、snapshot 和 reference-only treatment 的 target-path vocabulary。 | payload capture 或 event schema mutation |

## Dependency Order / 依赖顺序

当前依赖顺序是：

1. [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) 识别安全的
   document-only questions 和 blocked runtime work。
2. [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) 在 recall write
   policy、payload/diff rules 和 review placement 存在前保持 future-only。
3. [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md)
   阻止 ordinary retrieval 变成 durable events。
4. [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md)
   定义 meaning-shift review 可信前必须知道什么。
5. [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md)
   保持 lifecycle vocabulary 与 growth execution 分离。
6. [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md)
   区分 bounded change、random drift 和 collapse。
7. [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) 和
   [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) 让
   future exploration 与 subject/world boundaries 留在 product behavior 之外。
8. [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md)
   必须先存在，才能讨论 reducer execution。
9. [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md)
   定义 capture policy vocabulary，但不捕获 payloads。
10. [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) 让未来工作保持在
    low-risk consolidation，直到 implementation 被明确批准。
11. [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) 为后续
    document-only phases 提供 manual gate，但不批准执行。
12. [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)
    记录最新 manual bilingual consistency baseline，但不自动执行 review。
13. [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md)
    关闭 P54-P80 maintenance cycle，但不批准 runtime work。
14. [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md)
    把 CTM-inspired temporal concepts 映射到 foundation vocabulary，但不批准 CTM
    runtime、temporal event writes 或 model training。
15. [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md)
    把 P81 vocabulary 转为 evaluation scenarios，但不实现 tests、temporal runtime、thought
    loops 或 event writes。
16. [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md)
    定义 tick 和 review-depth preview vocabulary，但不执行 ticks、thought loops、policy 或
    mutations。
17. [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md)
    定义 future trace storage boundaries，但不存储 hidden chain-of-thought、private model
    reasoning、model internals 或 runtime traces。
18. [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md)
    把 future harness 定义为 preview-only local testing surface，而不是 product、adapter、UI、
    runtime executor 或 mutation path。
19. [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md)
    为 harness previews 定义 future intake envelope，但不做 adapter ingestion、conversation
    runtime、context building 或 event writes。
20. [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md)
    定义 future selected/omitted context reference explanations，但不执行 retrieval、context
    mutation 或 activation trace writes。
21. [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md)
    定义 future candidate queue preview vocabulary，但不执行 lifecycle、automatic approval、
    policy execution 或 mutation。
22. [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md)
    定义 deterministic resume scenario inputs 和 expected previews，但不做 temporal runtime、
    temporal event writes、memory decay 或 salience mutation。
23. [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md)
    评估 future minimal CLI harness readiness，但不批准 harness implementation、commands、
    schemas、tests、adapters、UI 或 runtime work。
24. [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md)
    收束 P82-P90 planning bridge，并在 explicit future approval 前继续阻塞 P91 implementation。
25. [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md)
    把 zero-start、tool-first self-evolution 翻译成 capability review vocabulary，但不批准 tool
    execution、tool generation、tool promotion、policy execution 或 Identity Core mutation。

## Runtime-Blocked Topics / Runtime 阻塞项

这些被索引文档不批准：

- Temporal Awareness runtime；
- CTM runtime 或 model training；
- thought loop execution；
- hidden chain-of-thought capture；
- private model reasoning persistence；
- thought trace storage；
- thin harness runtime；
- conversation intake runtime；
- adapter ingestion for harness work；
- context builder execution；
- retrieval execution as continuity；
- activation trace writes for harness previews；
- review queue execution；
- queue storage；
- candidate approval；
- session resume runtime；
- scenario tests for harness work；
- memory decay；
- salience mutation；
- tool execution runtime；
- automatic tool generation；
- automatic tool promotion；
- tool library mutation；
- harness implementation；
- fixture schema；
- output schema；
- recall event writes；
- growth lifecycle execution；
- automatic growth classification；
- automatic drift classification；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- policy executor；
- companion、relationship memory、UI、AstrBot、adapter 或 product layer。

## Stable Interpretation / 稳定解释

使用本索引回答三个问题：

1. 哪份文档拥有当前 vocabulary？
2. implementation 前缺少哪份 future contract？
3. 哪个 forbidden action 必须继续 blocked？

不要把本索引当作任何 future capability 的 implementation approval。
