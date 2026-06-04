# Context Package Preview RFC / 上下文包预览 RFC

English version: [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md)

状态：`document-only`、`RFC-only`、`non-runtime`。

P87 为 thin interaction harness 定义未来 context package preview surface。它不实现 context
building、retrieval、activation traces、context package persistence、API routes、CLI commands、
model prompting、adapter integration、recall event writes、temporal event writes、trace
storage、growth lifecycle、identity mutation、memory rewrite、UI、AstrBot、companion、cloud
或 product behavior。

## RFC Rule / RFC 规则

```text
a context package preview explains selection.
a context package preview is not retrieval as continuity.
a context package preview is not context mutation.
a context package preview is not an activation trace write.
```

## Problem / 问题

P86 定义了未来 conversation intake envelope。下一个 harness surface 是 context preview：给定一个
intake preview，系统需要能解释哪些 references 会被选择、哪些会被省略，以及为什么。

风险在于 context preview 很容易被误认为 continuity 本身。本项目里的 continuity 来自 state transfer、
event-sourced history、identity boundaries 和 reviewable state。Retrieval 可以支持 response，但
retrieval alone is not continuity。P87 保持这个边界清晰。

## Preview Scope / 预览范围

P87 覆盖未来 preview vocabulary：

- selected identity references；
- selected memory references；
- selected claim references；
- selected task references；
- selected governance references；
- source 和 evidence reasons；
- token budget notes；
- omitted references 和 omission reasons；
- privacy 和 sensitivity suppression；
- risk 和 boundary flags；
- context gap notes。

P87 不覆盖：

- retrieval execution；
- Context Builder changes；
- activation trace persistence；
- model prompt construction；
- endpoint behavior；
- adapter dry-run behavior；
- recall writes；
- memory salience mutation。

## Future Preview Shape / 未来预览形状

这只是 vocabulary，不是 schema，也没有实现。

```text
context_package_preview:
  intake_ref
  package_preview_id
  selection_policy_ref
  selected_refs
  omitted_refs
  source_attribution_summary
  token_budget_note
  privacy_suppression
  risk_flags
  context_gaps
  continuity_boundary_note
```

## Selected Reference Classes / 被选引用类别

| Reference Class | What It May Preview | Selection Reason | Explicitly Not |
|---|---|---|---|
| identity refs | stable identity anchors 或 identity memory refs | continuity anchor relevance | Identity Core mutation |
| memory refs | episodic、semantic、imported、archived 或 suppressed refs | task relevance、source evidence、privacy-safe availability | memory rewrite 或 salience mutation |
| claim refs | active claims、conflicts、support/contradiction refs | belief-shaped relevance 或 unresolved conflict | claim auto-revision |
| task refs | active tasks、next actions、blockers、procedural/cautionary refs | operational continuity | task auto-closure |
| governance refs | review objects、boundary decisions、risk registers、RFC refs | review pressure 或 blocked boundary | policy execution |
| temporal refs | 来自 intake 或 scenario 的 elapsed-time notes | future evaluation pressure | Temporal Awareness runtime |
| trace refs | 如果未来 policy 允许，可引用 public review summary refs | audit explanation | hidden reasoning storage |

## Omitted Reference Reasons / 省略引用原因

未来 previews 应尽量解释 omissions：

- privacy suppressed；
- cross-user boundary；
- archived or quarantined；
- insufficient provenance；
- token budget；
- weak evidence；
- stale or unresolved；
- identity pressure requires gate；
- forbidden boundary；
- not relevant to intake。

Omission 不是 deletion。Suppression 不是 memory rewrite。Budget pressure 不是 event compaction。

## Token Budget Boundary / Token 预算边界

Token budget notes 可以解释 reference 为什么被 selected 或 omitted。它们不得变成：

- automatic forgetting；
- memory deletion；
- event compaction；
- salience mutation；
- identity trimming；
- 证明某个 omitted reference 永久无关。

## Privacy Boundary / 隐私边界

Context preview 必须先保护 privacy，再追求 usefulness。preview 应能说明某个 reference 存在但被
suppressed，或者由于 cross-user / sensitive-source boundaries，甚至不能暴露 reference 本身。

Privacy suppression 不得通过 memory rewrite、payload capture 或 claim revision 来“修复”。

## Continuity Boundary / 连续性边界

preview 应包含 boundary note：

```text
selected context supports response generation.
selected context does not equal continuity.
continuity depends on state transfer and reviewable history.
```

这可以防止未来 harness 把项目降级成 retrieval-augmented chat。

## Relationship To Existing Context Builder / 与现有 Context Builder 的关系

当前项目已经有 Context Builder behavior 和 `/v1/context` documentation。P87 不修改这些系统。

P87 只定义未来 harness 如何在 response 或 candidate review 前 preview 和 explain context selection。

| Existing Capability | P87 Stance |
|---|---|
| State Transfer Package | 可作为现有 context output 被引用，但不改变 |
| activation traces | P87 不写入 |
| source attribution | 可启发 preview vocabulary，但不新增 persistence |
| dry-run adapter previews | 保持独立 adapter behavior |
| context package version | 不改变 |

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | Intake references 为 context preview 提供输入。 |
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | P87 定义 future harness boundary 内的一个 surface。 |
| [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | 帮助判断 memory refs 是否有足够 provenance 可被 preview。 |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | 保持 ordinary retrieval、context preview 与 recall writes 分离。 |
| [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | 保持 preview references 与 full payload capture 分离。 |
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | 定义 identity、memory、claims、tasks 和 governance 的 owner boundaries。 |

## Open Questions / 开放问题

- preview output 应包含 exact selected text，还是只包含 references 和 summaries？
- token budget 应如何表示，同时不变成 salience mutation？
- privacy suppression 生效时，omitted references 是否可见？
- context preview 如何引用 governance refs，同时不变成 policy execution？
- temporal notes 如何出现，同时不形成 Temporal Awareness runtime？
- context gaps 应创建 review candidates，还是保持 preview-only？

## P88 Candidate Direction / P88 候选方向

P88 可定义 Review Queue Preview RFC。它应解释 candidate types、ordering、review depth、boundary
flags 和 blocked items，同时不执行 growth lifecycle、claim revision、memory rewrite、recall writes、
task closure 或 policy automation。

## P87 Non-Execution Statement / P87 非执行声明

P87 不实现：

- context builder execution；
- retrieval execution；
- context package persistence；
- activation trace writes；
- source attribution persistence；
- API route；
- CLI command；
- model prompt construction；
- adapter dry-run changes；
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
- claim auto-revision；
- task auto-closure；
- policy execution；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
