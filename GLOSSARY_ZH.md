# 术语表

English version: [GLOSSARY.md](./GLOSSARY.md)

P53 让 glossary 聚焦基础层概念。这些定义不创建 runtime behavior。

## Growth / 成长

经过 evidence 支持、review 通过、并带有意义变化的 state transition，可能影响未来 continuity。Growth 不是自动行为，也不等于 memory promotion、identity mutation 或 tone drift。

## Growth Candidate / 成长候选

由 growth semantics 识别出的、可能带有意义变化的 state transition。它不是成长本身，也不能自动 promote 自己。

## Drift / 漂移

interpretation、behavior、salience、belief 或 identity pressure 随时间发生的变化。Drift 可以是 productive、random、exploratory、conflict-driven 或 identity-threatening。

## Productive Drift / 生产性漂移

有 evidence、有边界、并具备 review value 的 drift。Productive drift 可以成为 growth candidate review object，但它本身仍不是 growth。

## Random Drift / 随机漂移

缺少足够 evidence 或 state context 的 unsupported change。Random drift 应被 reject 或标记为 insufficient context。

## Meaning Shift / 意义变化

encoded memory 和 recalled memory state 之间的 interpretive change。P51 要求
`reinforced`、`weakened`、`reinterpreted` 和 `conflicted` shift 必须有 evidence。

## Recall State / 回忆状态

memory 被 recall 时的状态：task context、claim context、retrieval reason、active identity anchors，以及未来可能加入的 temporal fields。Recall state 会改变 memory 的意义。

## Encoding State / 编码状态

memory 最初被记录时的状态：source event、timestamp、active task、active claims、identity anchors、confidence、salience、privacy scope 和 state version。

## Identity-Threatening Drift / 身份威胁漂移

对 Identity Core continuity 施加压力或尝试 identity overwrite 的 drift signal。它需要 high-gate review，并且不能自动 mutate Identity Core。

## Review-Only / 只审查

不执行的 artifact 或 decision mode。Review-only object 可以记录、总结、排序、路由或请求 evidence，但不 mutate identity、不 rewrite memory、不 execute policy、不 compact events、不 promote growth。

## Growth Candidate Review / 成长候选审查

用于检查 growth candidate 的 review-only governance object。P51 中它由
`growth_candidate_review_v0.1` 表示，引用 source events、related memories、related claims、related tasks、encoding state、recall state、meaning shift、evidence、rejection reasons、risk level 和 review gate。

## Governance Surface / 治理表层

一个跨层 review surface，可以引用 Memory Layer、Claim Graph、Task Hub、Identity Gate 和 event evidence，但不直接属于任何单层。P51 推荐把 `growth_candidate_review` 放在这里。

## Temporal Awareness / 时间感知

未来方向，不是 P53 实现内容。原则：time is not only metadata; time is part of subject state transition.
