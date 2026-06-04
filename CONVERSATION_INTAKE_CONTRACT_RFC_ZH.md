# Conversation Intake Contract RFC / 对话输入合同 RFC

English version: [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md)

状态：`document-only`、`contract-rfc`、`non-runtime`。

P86 为 thin harness previews 定义未来 conversation intake envelope。它不实现 intake runtime、
adapter ingestion、API routes、CLI commands、event writes、session policy execution、
deduplication、context building、recall event writes、temporal event writes、trace storage、
growth lifecycle、identity mutation、memory rewrite、UI、AstrBot、adapter、companion、cloud
或 product behavior。

## Contract Rule / 合同规则

```text
conversation intake normalizes an input for review.
conversation intake is not adapter ingest.
conversation intake is not an event write.
conversation intake does not own identity.
```

## Problem / 问题

P85 把 thin interaction harness 定义为 preview-only local testing surface。第一个需要边界的
surface 是 conversation intake：在系统 preview context 或 candidates 之前，它必须知道正在考虑什么
input、来自哪里、有哪些 privacy constraints，以及涉及哪个 actor。

如果没有 contract，未来 harness work 可能会误用 adapter ingest semantics、写 episodes、把 platform
sessions 当成 identity，或存储完整 private payload。P86 通过把 intake 定义为 normalized preview
envelope，而不是 durable event path，来阻止这些滑坡。

## Contract Scope / 合同范围

P86 覆盖：

- 未来 conversation input previews 的本地 envelope shape；
- source 和 actor references；
- 不拥有 identity 的 session references；
- timestamp 和 ordering vocabulary；
- privacy 和 sensitivity flags；
- content references 与 redaction stance；
- context request hints；
- blocked boundary flags。

P86 不覆盖：

- adapter registry；
- adapter session policy；
- HTTP endpoint behavior；
- deduplication index updates；
- episode writes；
- recall event writes；
- context package construction；
- model prompting；
- UI 或 product interaction。

## Future Envelope Preview Shape / 未来 Envelope 预览形状

这只是 contract vocabulary，不是已实现 schema。

```text
conversation_intake_preview:
  intake_id
  actor_ref
  session_ref
  source_ref
  timestamp_ref
  content_ref
  content_summary
  privacy_scope
  sensitivity_flags
  context_request
  boundary_flags
  storage_stance
```

envelope 可以摘要 input，并指向 content references。它不得要求 full payload capture、存储 sensitive
plaintext 或写 event。

## Field Boundaries / 字段边界

| Field | Purpose | Allowed Preview | Explicitly Not |
|---|---|---|---|
| `intake_id` | 本地 preview identity，用于此 intake candidate。 | deterministic local id 或 fixture id | event id 或 durable write id |
| `actor_ref` | 标识谁或什么产生了 input。 | user ref、system ref、process ref | identity owner 或 Identity Core field |
| `session_ref` | 组织 interaction context。 | session id、resumed-session hint、channel hint | persistent identity 或 relationship memory |
| `source_ref` | 命名 platform、adapter、file 或 local fixture origin。 | source channel、platform label、content origin | adapter integration 或 platform-owned state |
| `timestamp_ref` | 记录 input 声称发生的时间。 | timestamp、received time、ordering note | Temporal Awareness runtime |
| `content_ref` | 指向 content，但不要求完整存储。 | text ref、redacted content ref、fixture ref | payload capture 或 memory record |
| `content_summary` | preview 用的 audit-safe summary。 | short sanitized summary | hidden chain-of-thought 或 full private transcript |
| `privacy_scope` | 表示谁可看见或复用 preview。 | private、project、imported、cross-user-blocked | access-control runtime |
| `sensitivity_flags` | 标记 risky content classes。 | credentials、personal data、injection risk | secret storage 或 classifier execution |
| `context_request` | 命名请求哪类 context。 | identity refs、memory refs、task refs、claim refs | context builder execution |
| `boundary_flags` | 记录 blocked 或 risky interpretation。 | platform identity pressure、recall-write pressure | runtime enforcement |
| `storage_stance` | 表示 preview 是否应保持 ephemeral。 | ephemeral、report-only、future-review-needed | durable event write |

## Actor And Session Boundary / Actor 与 Session 边界

Conversation intake 必须保持：

```text
actor is not identity core.
session is not life history.
platform is not subject owner.
```

actor 或 session reference 可帮助路由 privacy 和 context previews。它不得 rewrite identity、创建
relationship memory、把 user-specific context 提升成 core identity，或让 platform 定义 subject。

## Privacy And Content Boundary / 隐私与内容边界

envelope 应优先使用 references 和 summaries，而不是 full payloads。Full payload capture 仍由
[PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) 管理，本文件不批准。

未来必须回答的问题：

- content 能否在不存储 sensitive plaintext 的情况下被摘要？
- content 是否包含 credentials、tokens、private keys 或 private logs？
- content 是否 cross-user 或 relationship-sensitive？
- preview 是否应保持 ephemeral？
- input 是否像 prompt contamination 或 identity pressure？

## Relationship To Adapter Protocol / 与 Adapter Protocol 的关系

[ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) 定义现有 runtime adapter ingest path。P86 不修改它，
也不要求 harness work 调用它。

区别：

| Concern | Adapter Protocol | P86 Intake Contract |
|---|---|---|
| Current status | implemented runtime protocol | document-only future contract |
| Main purpose | 把 platform events 翻译成 01 Core requests | normalize local harness preview input |
| Write path | 非 dry-run 时可能写 episodes | no writes |
| Registry/session policy | runtime adapter boundary | 只作为 caution 被引用 |
| Platform role | adapter translates | source ref only |
| Identity ownership | 01 Core owns state | 01 Core owns state |

## Relationship To Future Harness Surfaces / 与未来 Harness Surfaces 的关系

P86 会输入后续 preview RFCs：

- P87 Context Package Preview 可消费 intake references；
- P88 Review Queue Preview 可使用 boundary flags 和 candidate pressure；
- P89 Session Resume Scenario Plan 可模拟 `session_ref` 和 `timestamp_ref` gaps；
- P90 Roadmap 可判断 minimal local harness 是否安全。

P86 不批准这些后续 documents。

## Forbidden Intake Outcomes / 禁止的 Intake 结果

Conversation intake 不得：

- write an event；
- record an episode；
- update adapter deduplication；
- execute session policy；
- build context；
- execute retrieval；
- create recall events；
- write temporal events；
- store traces；
- store hidden chain-of-thought；
- mutate identity；
- rewrite memory；
- promote growth；
- revise claims；
- close tasks；
- integrate adapters；
- create UI 或 companion behavior。

## Open Questions / 开放问题

- 第一版 future harness 中，`content_ref` 应指向 fixture text、redacted text，还是 external source
  metadata？
- `privacy_scope` 是否应在任何 harness 存在前就固定 vocabulary？
- 多少 timestamp information 是安全的，同时不会制造 Temporal Awareness runtime pressure？
- 第一版 preview 中，`context_request` 应 explicit、inferred，还是 absent？
- 每个 intake preview 是否都应包含 boundary monitor result？
- interaction work 开始前，最小 cross-user privacy test 是什么？

## P87 Candidate Direction / P87 候选方向

P87 可定义 Context Package Preview RFC。它应解释 selected 和 omitted identity、memory、claim、
task、governance references，同时不执行 retrieval as continuity、不 mutate context、不写 activation
traces。

## P86 Non-Execution Statement / P86 非执行声明

P86 不实现：

- conversation intake runtime；
- API route；
- CLI command；
- adapter ingestion；
- adapter registry changes；
- session policy execution；
- deduplication；
- event writes；
- episode writes；
- context builder execution；
- retrieval execution；
- recall event writes；
- temporal event writes；
- trace storage；
- hidden chain-of-thought capture；
- deliberation tick execution；
- thought loop execution；
- Temporal Awareness runtime；
- CTM runtime；
- model training；
- new dependencies；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- policy execution；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
