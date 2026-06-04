# 术语表

## Growth Candidate / 成长候选

由 growth semantics 识别出的、可能带有意义变化的 state transition。它不是成长本身，也不能自动 promote 自己。

## Growth Candidate Review / 成长候选审查

用于检查 growth candidate 的 review-only governance object。P51 中它由
`growth_candidate_review_v0.1` 表示，引用 source events、related memories、related claims、related tasks、encoding state、recall state、meaning shift、evidence、rejection reasons、risk level 和 review gate。

## Governance Surface / 治理表层

一个审查层，可以引用 Memory Layer、Claim Graph、Task Hub、Identity Gate 和 event evidence，但不直接属于任何单层。P51 推荐把 `growth_candidate_review` 放在这里。

## Meaning Shift / 意义变化

一段 memory 在 encoding state 与 recall state 之间出现的解释变化。P51 要求
`reinforced`、`weakened`、`reinterpreted` 和 `conflicted` 都必须有 evidence。没有 `evidence_refs` 的 meaning shift 只能是 `random_drift` 或 `insufficient_context`，不能算 growth。

## Anti-Growth Filter / 反成长过滤器

用于拒绝不能算 growth 的信号：single-turn style change、unsupported personality change、prompt contamination、adapter-specific behavior、isolated preference flip、model tone drift、tool artifact、roleplay residue、ungrounded identity statement 和 unsupported relationship escalation。

## Temporal Awareness / 时间感知

P52/P53 候选方向，不是 P51 实现内容。原则：time is not only metadata; time is part of subject state transition.
