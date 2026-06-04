# Thin Interaction Harness RFC / 薄交互试验台 RFC

English version: [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md)

状态：`document-only`、`RFC-only`、`non-runtime`。

P85 定义未来可能出现的 thin interaction harness 的边界。它不实现 harness、CLI command、
server、UI、adapter、AstrBot integration、conversation runtime、context builder、review
queue、boundary monitor、recall event write、temporal event write、thought loop、trace
storage、growth lifecycle、identity mutation、memory rewrite 或 product behavior。

## RFC Rule / RFC 规则

```text
a thin harness previews interaction surfaces.
a thin harness is not a product.
a thin harness is not an adapter.
a thin harness is not a mutation path.
```

## Problem / 问题

P0-P84 已经形成了大量 foundation：identity boundaries、event sourcing、reconstruction
readiness、stateful memory、growth review、temporal coherence、review depth 和 trace
storage boundaries。下一步有价值的不是完整 runtime 或 product surface，而是一个很小的方式，
用来推演 interaction 会如何触碰这些地基。

如果没有 thin harness boundary，未来工作很容易直接跳进 companion、UI、AstrBot、adapter、cloud
或 automatic growth behavior。P85 通过把 harness 定义成 review-only preview surface 来阻止这个跳跃。

## Harness Definition / Harness 定义

Thin interaction harness 是未来可能存在的本地 testing surface，可用于 preview：

- conversation input 会如何被 enveloped；
- 哪些 identity、memory、claim、task 和 governance references 会被选入 context；
- interaction 可能展示哪些 review candidates；
- 哪些 review queue entries 可能需要关注；
- session resume scenario 如何被模拟；
- 哪些 forbidden boundaries 会阻止 execution。

它不拥有 identity、不存储 memory、不写 events、不 mutate state、不执行 policy，也不集成平台。

## Proposed Future Surfaces / 候选未来表面

这些 surfaces 只是 RFC targets。P85 不实现它们。

| Surface | Future Purpose | Preview Output | Explicitly Not |
|---|---|---|---|
| `conversation_intake` | 定义 user/session message 的 input envelope。 | normalized envelope preview、source refs、privacy flags | adapter ingestion、platform identity、durable event write |
| `context_package_preview` | 解释哪些 state references 会被提供给 model。 | selected refs、reasons、omitted refs、token budget | memory retrieval as continuity、context mutation |
| `candidate_preview` | 展示 interaction 可能引发的 review objects。 | memory/claim/growth/meaning-shift/task candidate previews | growth lifecycle、claim revision、memory rewrite |
| `review_queue_preview` | 展示 review ordering 和 blocked items。 | queue preview、review depth、boundary flags | lifecycle execution 或 policy executor |
| `session_resume_scenario` | 模拟 minutes、hours 或 days 后的恢复。 | stale refs、context gaps、unresolved questions | Temporal Awareness runtime 或 temporal event write |
| `boundary_monitor_preview` | 解释一个 action 为什么被 blocked 或 deferred。 | boundary reason、related artifact、safe next document | runtime enforcement 或 product guardrail |

## Allowed Future Harness Output / 允许的未来 Harness 输出

未来 harness 可能允许输出：

- preview envelopes；
- selected reference lists；
- omission reasons；
- review-depth recommendations；
- candidate previews；
- boundary flags；
- unresolved questions；
- deterministic scenario reports；
- "blocked"、"defer" 或 "needs review" labels。

## Forbidden Harness Output / 禁止的 Harness 输出

未来 harness 不得把以下内容作为 execution 输出：

- identity update；
- memory rewrite；
- recall event write；
- temporal event write；
- growth promotion；
- claim auto-revision；
- task auto-closure；
- thought loop execution；
- hidden chain-of-thought capture；
- trace storage；
- reconstruction reducer execution；
- event compaction；
- adapter action；
- UI 或 companion behavior。

## Minimal Future Flow / 最小未来流程

这是 conceptual flow，不是 implementation。

```text
conversation input
  -> conversation_intake preview
  -> context_package_preview
  -> candidate_preview
  -> review_queue_preview
  -> boundary_monitor_preview
  -> no mutation unless a future approved phase creates explicit contracts
```

这个 flow 故意保持 preview-only。只有每一步都能解释自己会做什么、同时不真的执行，它才有价值。

## Boundary Ownership / 边界归属

| Boundary | Owner | Harness Behavior |
|---|---|---|
| Identity | Identity Core / Identity Gate | 可引用 anchors；不得 mutate |
| Memory | Memory Layer / Stateful Memory | 可 preview refs 和 meaning-shift candidates；不得 rewrite records |
| Claims | Claim Graph | 可 preview conflicts；不得 auto-revise claims |
| Tasks | Task Hub | 可 preview operational context；不得 close tasks |
| Growth | Growth Candidate Review | 可 preview candidates；不得执行 lifecycle 或 promotion |
| Time | Temporal Awareness RFC | 可模拟 elapsed-time scenarios；不得写 temporal events |
| Traces | Thought Trace Storage Policy | 可解释 review summaries；不得存储 hidden reasoning |
| Platforms | Adapter Protocol | 可包含 source refs；不得集成 adapters 或拥有 identity |

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | 定义 harness 必须保留的 owner boundaries。 |
| [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | 提供 harness 必须显示为 blocked 的 forbidden outputs。 |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | review depth 只能作为 preview vocabulary 出现。 |
| [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | 防止 harness previews 变成 hidden reasoning storage。 |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | 提供 later harness 可能 report 的 deterministic evaluation scenarios。 |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | 保持 ordinary recall、context preview 与 durable recall writes 分离。 |
| [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | 保持 candidate preview 与 lifecycle execution 分离。 |

## Open Questions / 开放问题

- 第一个 harness 应该是 CLI-only、report-only，还是 fixture-only？
- 什么是最小 envelope，能够证明 platform does not own identity？
- 哪些 preview outputs 可以安全存储，哪些必须保持 ephemeral？
- boundary monitor 应该是 report、checklist，还是 future validation？
- harness 如何 preview context，同时不暗示 retrieval equals continuity？
- review queues 如何被 preview，同时不执行 lifecycle？

## P86 Candidate Direction / P86 候选方向

P86 可定义 Conversation Intake Contract RFC。它应描述未来 harness previews 的 input envelope，
同时不实现 runtime intake、adapter ingestion、event writes 或 platform-owned identity。

## P85 Non-Execution Statement / P85 非执行声明

P85 不实现：

- thin harness runtime；
- CLI commands；
- server routes；
- UI；
- adapter 或 AstrBot integration；
- conversation ingestion；
- context builder execution；
- review queue execution；
- boundary monitor execution；
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
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- policy execution；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、cloud rollout 或 product layer。
