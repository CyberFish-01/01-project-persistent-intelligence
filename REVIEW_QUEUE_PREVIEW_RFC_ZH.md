# Review Queue Preview RFC / 审查队列预览 RFC

English version: [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md)

状态：`document-only`、`RFC-only`、`non-runtime`。

P88 为 thin interaction harness 定义未来 review queue preview surface。它不实现 queue、lifecycle
execution、policy execution、candidate promotion、claim revision、task closure、recall event
writes、temporal event writes、trace storage、context building、identity mutation、memory
rewrite、UI、AstrBot、adapter、companion、cloud 或 product behavior。

## RFC Rule / RFC 规则

```text
a review queue preview organizes review pressure.
a review queue preview is not a lifecycle engine.
a review queue preview is not approval.
a review queue preview is not mutation.
```

## Problem / 问题

P85-P87 定义了 future harness boundary、conversation intake envelope 和 context package
preview。一旦这些 surface 在概念上存在，下一步问题就是 harness 可以展示哪些 review objects，以及它们
应如何排序。

风险在于 "queue" 听起来像 executable。P88 把 queue language 保持在 preview-only：它可以解释
candidate type、risk、review depth、evidence 和 blocked boundaries，但不得执行 candidate lifecycle
actions 或改变 subject state。

## Preview Scope / 预览范围

P88 覆盖未来 preview vocabulary：

- candidate type；
- source references；
- evidence references；
- risk level；
- review depth；
- boundary flags；
- blocked reason；
- unresolved questions；
- recommended review route；
- preview ordering reason。

P88 不覆盖：

- lifecycle execution；
- durable queue persistence；
- automatic approval；
- policy execution；
- state mutation；
- event writes；
- prompt 或 model behavior。

## Future Preview Shape / 未来预览形状

这只是 vocabulary，不是 schema，也没有实现。

```text
review_queue_preview:
  queue_preview_id
  intake_ref
  context_preview_ref
  candidate_previews
  ordering_policy_note
  blocked_items
  unresolved_questions
  non_execution_boundary
```

```text
candidate_preview:
  candidate_ref
  candidate_type
  source_refs
  evidence_refs
  risk_level
  review_depth
  boundary_flags
  blocked_reason
  suggested_route
  preview_status
```

## Candidate Types / 候选类型

| Candidate Type | What It Previews | Suggested Route | Explicitly Not |
|---|---|---|---|
| `memory_candidate` | possible memory review、provenance concern、archive/quarantine question | Memory Layer review | memory promotion 或 rewrite |
| `claim_candidate` | support、contradiction、uncertainty、repair need | Claim Graph review | claim auto-revision |
| `growth_candidate` | evidence-backed possible meaning-bearing transition | Growth Candidate Review | growth promotion |
| `meaning_shift_candidate` | reinforced、weakened、reinterpreted 或 conflicted memory meaning | Stateful Memory review | recall write 或 memory rewrite |
| `recall_candidate` | P59 thresholds 下的 review-worthy recall question | Recall Event Write Policy review | recall event write |
| `task_candidate` | active task、blocker、procedural 或 cautionary work item | Task Hub review | task auto-closure 或 workflow execution |
| `governance_candidate` | boundary、policy、RFC、risk 或 review object | Governance Surface | policy executor |
| `identity_candidate` | identity-adjacent pressure 或 anchor question | Identity Gate | Identity Core mutation |
| `temporal_candidate` | delayed alignment、unresolved tension、stale context | future Temporal Awareness review | temporal event write |
| `trace_candidate` | public review summary storage question | Thought Trace Storage Policy review | hidden reasoning storage |

## Ordering Signals / 排序信号

未来 preview ordering 可以考虑：

- identity pressure；
- privacy 或 cross-user risk；
- prompt contamination risk；
- evidence strength；
- unresolved tension；
- review depth；
- blocked boundary severity；
- task urgency；
- stale context；
- missing provenance。

Ordering 不是 execution priority。排名靠前的 item 不会因此被 approved、stored、promoted 或 written。

## Review Depth Boundary / 审查深度边界

P83 把 review depth 定义为 planning vocabulary。P88 可以显示：

- `shallow`；
- `normal`；
- `deep`；
- `blocked`。

它不得执行 deliberation ticks、thought loops、policy、lifecycle 或 approval。`blocked` 表示 do not
execute；它不是实现 guardrail 的请求。

## Blocked Items / 阻塞项

当 item 请求或暗示以下内容时，preview 应将其标为 blocked：

- identity mutation；
- memory rewrite；
- recall event write；
- temporal event write；
- growth lifecycle execution；
- policy executor；
- reconstruction reducer execution；
- event compaction；
- hidden chain-of-thought capture；
- adapter integration；
- UI、companion 或 product behavior。

Blocked items 可以作为 audit 和 planning objects 保持可见。它们不得被 queue 转换为 execution tasks。

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | P88 定义 future harness boundary 内的 review queue surface。 |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | Context gaps 或 selected refs 可以输入 candidate previews。 |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | 提供 review depth vocabulary，但不执行 ticks。 |
| [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | 保持 lifecycle labels 与 queue preview 分离。 |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | 提供 drift 和 collapse rejection reasons。 |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | 保持 recall candidates 与 recall writes 分离。 |
| [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | 保持 trace candidates 与 hidden reasoning storage 分离。 |
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | 定义每类 candidate 应由哪个 owner review。 |

## Open Questions / 开放问题

- queue previews 应按 risk、age、evidence strength，还是 owner boundary 排序？
- blocked candidates 应保持可见，还是分离到 blocked view？
- review queue preview 能否作为 report 存储，同时不变成 lifecycle history？
- future harness 中，context gaps 应自动创建 queue candidates，还是只在明确请求时创建？
- identity-adjacent items 如何路由到 Identity Gate，同时不制造 mutation pressure？
- low-risk items 如何避免 review overload？

## P89 Candidate Direction / P89 候选方向

P89 可定义 Session Resume Scenario Plan。它应模拟 minutes、hours、days、unresolved tasks、stale
claims、stale memories、pending review candidates 和 context gaps，同时不写 temporal events，也不执行
Temporal Awareness runtime。

## P88 Non-Execution Statement / P88 非执行声明

P88 不实现：

- review queue runtime；
- queue storage；
- lifecycle execution；
- growth promotion；
- candidate approval；
- policy execution；
- context builder execution；
- retrieval execution；
- API route；
- CLI command；
- model prompting；
- trace storage；
- hidden chain-of-thought capture；
- deliberation tick execution；
- thought loop execution；
- Temporal Awareness runtime；
- CTM runtime；
- model training；
- new dependencies；
- temporal event writes；
- recall event writes；
- identity mutation；
- memory rewrite；
- claim auto-revision；
- task auto-closure；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
