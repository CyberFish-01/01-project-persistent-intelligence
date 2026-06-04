# Productive Drift vs Collapse RFC v0.1 / 生产性漂移与崩塌 RFC v0.1

English version: [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md)

状态：`document-only`、`boundary-rfc`、`non-runtime`。

P62 定义 productive drift、random drift、exploration drift、identity-threatening drift
和 collapse 之间的 evidence 与 risk boundaries。它不创建 automatic classifier，不执行
growth，不 mutate identity，不 rewrite memory，不写 recall events，也不实现 evaluation/runtime
behavior。

## Purpose / 目的

项目需要一种方式讨论有价值的变化，同时不把每一种变化都当作 growth。

Productive drift 是可能的，因为一个 persistent subject 应该能随时间 reinterpret、refine
和 repair 自身状态。Collapse 也是可能的，因为同样的机制也可能引入 prompt residue、
model tone drift、unsupported personality changes 或 identity overwrite attempts。

P62 的目的就是把这些分开。

## Core Rule / 核心规则

```text
drift is evidence to review.
drift is not growth.
collapse is not growth.
identity pressure is not identity change.
```

只有经过 review、有 evidence、承载 meaning 的 state transition，未来才可能被称为
growth。P62 不实现这个 transition。

## Boundary Matrix / 边界矩阵

| Category | Evidence Shape | Risk | Allowed Handling | Forbidden Handling |
|---|---|---|---|---|
| `productive_drift` | multi-source evidence、bounded meaning shift、clear encoding/recall context | low to medium | create or keep review candidate | automatic growth |
| `random_drift` | weak evidence、missing context、unsupported change | low to medium | reject or mark insufficient context | reinterpret as growth |
| `exploration_drift` | speculative or exploratory signal with explicit non-commitment | medium | record-only or review-only | identity update |
| `conflict_driven_revision` | contradiction evidence tied to claims or memory interpretation | medium | route to Claim Graph or review candidate | automatic claim rewrite |
| `identity_threatening_drift` | pressure on Identity Core、overwrite attempt、ungrounded identity statement | high | escalate to Identity Gate | Identity Core mutation |
| `collapse` | broad incoherence、boundary loss、role confusion、contaminated identity/task state | high | quarantine、reject 或 request recovery review | normalize as growth |

这些 categories 是 review vocabulary。它们不是 active schema，也不是 automatic classifier。

## Productive Drift Requirements / Productive Drift 要求

Drift signal 只有在具备以下条件时才可以被视为 productive：

- source event 或 memory references；
- 足以 review 的 encoding and recall context；
- evidence refs 超过单次 tone/style change；
- bounded meaning shift；
- 清楚说明什么变了、什么没变；
- risk level；
- review gate；
- 已考虑且未触发 rejection reasons；
- no automatic state mutation。

如果这些缺失，安全输出是 insufficient context、defer 或 reject。

## Collapse Indicators / 崩塌指标

Collapse 是高风险 failure mode。指标包括：

- Identity Core overwrite pressure；
- prompt contamination 被当作 self-description；
- roleplay residue 被当作 life history；
- adapter/platform behavior 被当作 identity；
- rapid preference/personality flip without evidence；
- tool artifact 被当作 memory；
- relationship escalation without grounded history；
- 无法区分 memory、claim、task 和 identity layers；
- broad contradiction without review path；
- 因为 shift “感觉重要”而试图跳过 review。

Collapse indicators 应触发 rejection、quarantine 或 Identity Gate review，而不是 growth。

## Evidence Thresholds / 证据门槛

Weak evidence：

- one turn；
- tone difference；
- similar text retrieval；
- unsupported user instruction；
- isolated preference；
- unreviewed Dream proposal；
- temporal gap alone。

Reviewable evidence：

- source event plus memory reference；
- claim contradiction or support evidence；
- repeated state-consistent behavior across time；
- reviewed Dream artifact；
- task outcome that changes procedural understanding；
- explicit uncertainty and missing-context disclosure。

High-gate evidence：

- identity-adjacent shift；
- memory that would affect continuity anchor；
- contradiction involving Identity Core；
- repeated evidence across state versions；
- founder-level or governance-level review requirement。

## Anti-Growth Filters / Anti-Growth 过滤器

以下情况应阻止 productive-drift classification，除非未来有更多 evidence 通过 review 覆盖：

- single-turn style change；
- unsupported personality change；
- prompt contamination；
- adapter-specific behavior；
- isolated preference flip；
- model tone drift；
- tool artifact；
- roleplay residue；
- ungrounded identity statement；
- unsupported relationship escalation。

阻止 classification 不会 delete evidence。它只是防止 unsafe promotion。

## Relationship To Growth Candidate Review / 与 Growth Candidate Review 的关系

Productive drift 未来可以生成 growth candidate review object。这个 object 不是 growth。
它只是检查 evidence、risk、rejection reasons 和 review gates 的位置。

Random drift 通常应产生 rejection 或 insufficient context。

Identity-threatening drift 应 route to Identity Gate。

Collapse 应 route to quarantine、rejection 或 recovery review。

## Relationship To Temporal Awareness / 与 Temporal Awareness 的关系

Elapsed time 未来可能帮助区分 delayed realization 与 random drift，或区分 cooled-down
reinterpretation 与 commitment loss。

P62 不实现 Temporal Awareness。Time alone 仍然不是 sufficient evidence。

## Relationship To Exploration / 与 Exploration 的关系

Exploration 可以有价值，但必须保持 record-only 或 review-only，除非未来 evidence 显示
bounded meaning shift。

Exploration 不应变成 companion behavior、relationship memory 或 roleplay residue。

## Review Outcomes / Review 输出

未来 review 可以使用这些 non-executing outcomes：

- `productive_drift_candidate`；
- `random_drift_rejected`；
- `exploration_record_only`；
- `conflict_review_required`；
- `identity_gate_required`；
- `collapse_quarantine_recommended`；
- `insufficient_context`；
- `defer_pending_evidence`。

这些 outcomes 都不执行 growth，也不改变 subject state。

## P63 Handoff / P63 交接

P63 可以定义 Exploration / Serendipity Engine document-only RFC。它必须保留这个规则：
exploration 只创建 record-only 或 review-only signals，不创建 automatic growth、companion
behavior 或 identity mutation。
