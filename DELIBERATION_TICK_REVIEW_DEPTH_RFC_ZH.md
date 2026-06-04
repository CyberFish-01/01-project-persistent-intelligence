# Deliberation Tick / Review Depth RFC / 审议 Tick 与审查深度 RFC

English version: [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md)

状态：`document-only`、`RFC-only`、`non-runtime`。

P83 定义 `deliberation_tick`、`review_depth` 和 `risk_level` vocabulary，用于未来 review
planning。它不实现 tick runtime、thought loops、Temporal Awareness runtime、CTM runtime、
recall event writes、growth lifecycle、identity mutation、memory rewrite、companion、UI、
AstrBot 或 adapter behavior。

## RFC Rule / RFC 规则

```text
a deliberation tick is a review planning unit.
a review depth is a risk-calibrated review requirement.
neither is a thought loop or runtime execution.
```

## Problem / 问题

P81 和 P82 引入了 temporal dynamics 与 temporal coherence vocabulary。下一个边界问题是
review effort：低风险 candidate 不应被重治理拖慢，而 identity-threatening 或 ambiguous
candidate 也不能只经过 shallow review。

如果没有 review depth vocabulary，未来 harness work 可能会对所有 candidates 都过度治理，
或者对高风险变化 review 不足。

## Core Concepts / 核心概念

| Concept | Definition | Input References | Output | Explicitly Not |
|---|---|---|---|---|
| `deliberation_tick` | 未来可能用于表示一个 bounded review consideration step 的 symbolic unit。 | candidate id、evidence refs、risk level、unresolved questions | preview 中的 tick count 或 tick plan | thought loop、model trace、runtime step |
| `review_depth` | candidate 所需的 review effort。 | risk level、evidence ambiguity、identity pressure、boundary flags | `shallow`、`normal`、`deep` 或 `blocked` | approval、execution、mutation |
| `risk_level` | review 前对 candidate risk 的分类。 | identity pressure、memory rewrite risk、recall write pressure、product pressure | low、medium、high、identity-threatening、blocked | automatic decision |
| `review_depth_budget` | 未来可能用于限制或规划 review steps 数量的 cap / target。 | candidate type、risk level、available evidence | maximum planned ticks 或 "needs human review" | adaptive compute runtime |

## Risk-Level To Review-Depth Mapping / 风险等级到审查深度映射

| Risk Level | Example Candidate | Required Review Depth | Boundary |
|---|---|---|---|
| `low` | typo-level context clarification 或 harmless candidate preview | `shallow` | no mutation, no durable write |
| `medium` | 有清晰 event 和 memory refs 的 meaning-shift candidate | `normal` | no promotion or lifecycle execution |
| `high` | claim conflict、stale task pressure 或 ambiguous memory provenance | `deep` | no claim auto-revision or memory rewrite |
| `identity_threatening` | candidate 压迫 Identity Core anchors | `deep` plus Identity Gate routing | no identity mutation |
| `blocked` | 请求 companion behavior、temporal runtime、recall write 或 adapter integration | `blocked` | reject or defer; do not execute |

## Deliberation Tick Preview Shape / 审议 Tick 预览形状

这只是 preview vocabulary，不是 schema。

```text
deliberation_tick_preview:
  tick_index
  review_question
  evidence_refs
  unresolved_questions
  boundary_flags
  next_review_need
```

preview 可帮助未来 harness 解释为什么某个 candidate 需要 deeper review。它不能存储 private
model reasoning、hidden chain-of-thought 或 neural internal state。

## Review Depth Inputs / 审查深度输入

未来 review depth planning 可检查：

- source event references；
- encoding_state 和 recall_state references；
- meaning_shift candidate type；
- claim/task/memory alignment；
- unresolved_tension level；
- temporal_coherence_score as future evaluation signal；
- identity pressure；
- privacy 和 provenance gaps；
- forbidden boundary flags。

## Review Depth Outputs / 审查深度输出

允许的未来 outputs：

- recommended review depth；
- reason for review depth；
- candidate should remain preview-only；
- candidate should be deferred；
- candidate requires Identity Gate；
- candidate is blocked by boundary。

禁止的 outputs：

- identity update；
- memory rewrite；
- recall event write；
- growth promotion；
- claim auto-revision；
- temporal event write；
- adapter 或 product action。

## Relationship To Thin Harness / 与 Thin Harness 的关系

P83 可启发未来 thin interaction harness previews：

- context preview 可显示 candidate 为什么需要 shallow 或 deep review；
- candidate preview 可展示 risk 和 review-depth reasons；
- review queue preview 可按 review depth 排序，但不执行 lifecycle；
- boundary monitor 可在 runtime work 前标记 blocked candidates。

P83 不实现 harness。

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | 作为 CTM-inspired concepts 引入 deliberation tick 和 review depth vocabulary。 |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | 定义 future scenarios，其中 review depth 应随 risk 变化。 |
| [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | Lifecycle status 仍 blocked；review depth 只能 preview review effort。 |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | review depth 帮助区分 weak drift 和 evidence-backed evolution。 |
| [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | boundary flags 定义 review depth 何时变成 blocked。 |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | risk clusters 提供 review-depth pressure signals。 |

## Open Questions / 开放问题

- `review_depth` 应手动指定，还是由 future evaluation 计算？
- preview ticks 多少才有用，超过多少会让 review 过重？
- high-risk candidates 是否总是需要 human review？
- `blocked` 是 review depth，还是 separate boundary outcome？
- 能否在不执行 thought-loop 的情况下测试 review depth？
- review depth 应如何与 future thought trace storage policy 互动？

## P84 Candidate Direction / P84 候选方向

P84 可定义 Thought Trace Storage Policy。它应保持 deliberation tick previews 与 hidden
chain-of-thought、private model reasoning 和 model internal traces 分离。

## P83 Non-Execution Statement / P83 非执行声明

P83 不实现：

- deliberation tick runtime；
- thought loop execution；
- thought trace storage；
- Temporal Awareness runtime；
- CTM runtime；
- model training；
- new dependencies；
- temporal event writes；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- policy execution；
- reconstruction reducer execution；
- companion、UI、AstrBot、adapter、cloud rollout 或 product layer。
