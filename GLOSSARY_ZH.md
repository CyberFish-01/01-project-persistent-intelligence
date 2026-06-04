# 术语表

English version: [GLOSSARY.md](./GLOSSARY.md)

P74 让 glossary 聚焦基础层概念和术语边界。这些定义不创建 runtime behavior。

## Deduplication Rule / 去重规则

当两个术语重叠时，优先使用更窄的 owner：

- Memory Layer 用于 stored memory objects 和 retrieval；
- Stateful Memory 用于 meaning-bearing memory semantics；
- Claim Graph 用于 claim status 和 evidence relations；
- Governance Surface 用于跨层 review objects；
- Event Log 和 Reconstruction Evidence 用于 auditability 与 replay readiness；
- RFC terms 表示 future contracts，不表示已经实现的机制。

## Growth / 成长

经过 evidence 支持、review 通过、并带有意义变化的 state transition，可能影响未来 continuity。

边界：Growth 不是自动行为，也不等于 memory promotion、identity mutation、tone drift 或 lifecycle label。

## Growth Candidate / 成长候选

由 growth semantics 标记出来、等待 review 的可能 meaning-bearing state transition。

边界：Growth candidate 不是 growth；它不能自动 promote 自己，也不 rewrite memory 或 identity。

## Growth Candidate Review / 成长候选审查

用于检查 growth candidate 的 review-only governance object。P51 中它由
`growth_candidate_review_v0.1` 表示，引用 source events、related memories、related claims、related tasks、encoding state、recall state、meaning shift、evidence、rejection reasons、risk level 和 review gate。

边界：这个 object 属于 Governance Surface，不单独属于 Memory Layer、Claim Graph、Task Hub 或 Identity Core。

## Growth Candidate Lifecycle / 成长候选生命周期

未来 review-object housekeeping vocabulary，用来描述 open、deferred、archived、quarantined 或 rejected 等状态。

边界：Lifecycle status 不是 subject growth、不是 memory promotion，也不是 execution engine。

## Drift / 漂移

interpretation、behavior、salience、belief 或 identity pressure 随时间发生的变化。Drift 可以是 productive、random、exploratory、conflict-driven 或 identity-threatening。

边界：Drift 是 signal category；它本身不自动等于好、坏或 growth。

## Productive Drift / 生产性漂移

有 evidence、有边界、有 review value，并且可能帮助 continuity improvement 或 meaning clarification 的 drift。

边界：Productive drift 可以成为 growth candidate review object，但它本身仍不是 growth。

## Random Drift / 随机漂移

缺少足够 evidence、event context 或 state context 的 unsupported change。

边界：Random drift 应被 reject、标记为 insufficient context，或路由到 review；它不应该被 normalise 成 growth。

## Identity-Threatening Drift / 身份威胁漂移

对 Identity Core continuity 施加压力或尝试 identity overwrite 的 drift signal。

边界：它需要 high-gate review，并且不能自动 mutate Identity Core。

## Collapse / 坍塌

continuity、coherence 或 reviewability 的丧失；state transfer 已不足以解释当前状态是如何从主体历史中抵达的。

边界：Collapse 不是更强的 growth；它是 failure mode 或 high-risk condition。

## Meaning Shift / 意义变化

encoded memory 和 recalled memory state 之间的 interpretive change。P51 要求
`reinforced`、`weakened`、`reinterpreted` 和 `conflicted` shift 必须有 evidence。

边界：Meaning shift 不等于 claim revision。Claim revision 改变 claim status；meaning shift 解释 memory 在 recall 时意义如何变化。

## Recall State / 回忆状态

memory 被 recall 时的状态：task context、claim context、retrieval reason、active identity anchors，以及未来可能加入的 temporal fields。Recall state 会改变 memory 的意义。

边界：Recall state 不是 recall event write。它可以在 review 中被引用，而不新增 event。

## Encoding State / 编码状态

memory 最初被记录时的状态：source event、timestamp、active task、active claims、identity anchors、confidence、salience、privacy scope 和 state version。

边界：Encoding state 是后续 interpretation 所需的最小 context reference，不是主体的完整 snapshot。

## Recall Event Write Policy / 回忆事件写入策略

未来 policy surface，用来决定一次 recall 什么时候应该成为 auditable event。

边界：RFC 只定义问题和约束；它不授权 recall event writes。

## Stateful Memory / 有状态记忆

把 memory 解释为以下结构的 memory semantics：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

边界：Stateful Memory 不替代 Memory Layer。Memory Layer 负责存储和 retrieval；Stateful Memory 解释 remembered meaning 如何随 state transition 变化。

## Review-Only / 只审查

不执行的 artifact 或 decision mode。Review-only object 可以记录、总结、排序、路由或请求 evidence。

边界：Review-only object 不 mutate identity、不 rewrite memory、不 execute policy、不 compact events、不 run reducers、不 promote growth。

## Governance Surface / 治理表层

一个跨层 review surface，可以引用 Memory Layer、Claim Graph、Task Hub、Identity Gate 和 event evidence，但不直接属于任何单层。P51 推荐把 `growth_candidate_review` 放在这里。

边界：Governance Surface 拥有 review objects；它不是 policy executor、Task Hub 替代品或 growth engine。

## Temporal Awareness / 时间感知

未来方向，把 elapsed time 视为 subject state transition 的一部分，而不只是 metadata。

边界：P58 只是 document-only。Temporal Awareness 不是 runtime behavior、temporal event execution、task staleness automation 或 memory decay。

## Subject Kernel / 主体内核

主体受保护的 continuity nucleus：identity anchors、core invariants，以及不能被随意 overwrite 的最小 interpretive frame。

边界：Subject Kernel 是未来边界概念，不是当前 runtime split 或 identity rewrite。

## World Seed / 世界种子

主体面向世界的可演化起始框架：assumptions、environment、interests、orientation 和 exploratory context。

边界：World Seed 可以在 review 下演化，但不能把变化偷渡进受保护的 Subject Kernel。

## Reconstruction Evidence / 重建证据

用于判断主体历史是否 auditable、replayable、并为未来 reconstruction 做好准备的 evidence vocabulary 和 report layer。

边界：Reconstruction evidence 不是 reconstruction execution 或 state rebuild。

## Reconstruction Reducer Contract / 重建 reducer 合同

未来任何可能从 events rebuild 或 project state 的 reducer 所需遵守的 contract。

边界：该 contract 在 implementation 前命名必要 guarantees 和 gaps；它不运行 reducer。

## Payload / Diff Capture Policy / Payload 与 Diff 捕获策略

未来 capture policy，用来决定 events 什么时候需要 payloads、diffs、snapshots 或 reference-only records。

边界：该 policy 描述未来需求和风险；它不 capture 新 payloads，也不 mutate event schemas。

## Risk Register / 风险登记表

foundation risks 的文档级 watchlist，例如 concept inflation、premature runtime pressure、boundary drift 和 bilingual drift。

边界：Risk register 记录风险；它不是 governance execution。

## CTM-inspired Temporal Dynamics / CTM 启发的时间动力学

一种 RFC-only vocabulary，把 Continuous Thought Machines 的启发翻译成 01 Core 的 symbolic
temporal review concepts。

边界：01 Core 不是 CTM implementation。该 term 不批准 CTM runtime、model training、
temporal event writes 或 neural synchronization claims。

## Deliberation Tick / 审议 tick

未来可能用于表示 conclusion 前 internal review progression 的单位。

边界：deliberation tick 当前不被 persist，不是 event，也不是 runtime step，除非未来 policy 明确定义。

## Thought Trace / 思考轨迹

未来可能用于记录 review state 如何随 deliberation 演化。

边界：thought trace 在 P81 没有 storage policy，不能创建 event payloads、memory rewrites、
identity changes 或 pseudo-consciousness claims。

## Temporal Coherence / 时间一致性

用于 review later state 是否仍能与 earlier state、current evidence 和 continuity anchors 相容的概念。

边界：temporal coherence 不是真理、growth、consciousness，也不是 automatic claim revision。

## Review Depth Budget / 审查深度预算

未来可能用于让 review effort 匹配 risk level 的 policy concept。

边界：review depth budget 不是 adaptive compute runtime、不是 policy execution，也不是 automatic approval。

## Unresolved Tension / 未解决张力

未来可能用于表示 persistent conflict 的 review signal；该 conflict 尚未成为 decision、claim revision 或 growth candidate。

边界：unresolved tension 不能自动创建 growth candidates、rewrite claims 或 mutate identity。

## Delayed Alignment / 延迟对齐

未来可能表示 later evidence 让 earlier state 或 memory 符合 stable pattern 的 review signal。

边界：delayed alignment 可以提示 review evidence；它不是 semantic promotion、identity update 或 memory rewrite。

## Coherence Break / 一致性断裂

未来可能表示 current state 已不能安全地从 prior state 和 evidence 推导出来。

边界：coherence break 是 review concern，不是 automatic collapse classification 或 reconstruction。
