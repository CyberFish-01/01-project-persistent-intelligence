# 最小 CLI 试验台实现计划

English version: [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md)

状态：`P99`、`planning`、`RFC-only`、`document-only`、`non-runtime`。

P99 定义一个未来最小 CLI 试验台的 implementation plan。它不实现 harness、不新增 CLI 命令、
不新增 tests、不写 schema、不调用模型、不调用外部 API、不修改 state、不集成 adapter，也不进入
product layer。

## Plan Rule / 计划规则

```text
implementation plan is not implementation.
dry-run means no writes.
preview is not persistence.
candidate is not promotion.
review queue preview is not lifecycle.
```

## 1. Problem Statement / 问题陈述

P0-P98 已经形成大量 foundation：identity boundaries、state transfer、event sourcing、
reconstruction readiness、stateful memory、growth review、temporal review vocabulary、
capability boundaries，以及只读 Foundation Observatory。

P96 实现了 `foundation-observatory-report` 静态只读报告。P97 审查它是否真的能让 founder
看懂。P98 改进报告，让 founder 更容易看到状态、风险、边界和下一步候选。

下一步压力来自真实交互。foundation 需要一个最小方式测试：一条真实用户消息会如何触碰 intake、
context、candidate、review queue、boundary 和 observatory summary。但这不能直接跳到
Companion、Web UI、AstrBot、adapter integration、cloud runtime 或 product behavior。

因此 minimal CLI harness 是本地试验台。它不是产品、聊天机器人、adapter、memory writer、
identity owner、growth engine 或 automatic executor。

## 2. Minimal Scope / 最小范围

最小未来命令候选：

```bash
python3 -m one_core.cli harness-dry-run
```

P99 不新增这个命令。P99 只规划 future command boundary。

候选未来参数：

| 参数 | 作用 | 边界 |
|---|---|---|
| `--input TEXT` | 要 preview 的用户消息或 fixture text。 | 只是文本输入，不是 adapter ingest。 |
| `--session-id ID` | 本地 preview session reference。 | 不拥有 identity，也不写 session state。 |
| `--actor-id ID` | 用于 attribution 的 actor reference。 | 不创建 actor identity。 |
| `--lang en\|zh` | 输出语言。 | 只是显示选择。 |
| `--format markdown\|json` | 输出格式。 | 只是报告格式，不是 schema persistence。 |
| `--output PATH` | 可选报告输出路径。 | 只有显式指定时写 report，不写 state。 |
| `--no-write` | 必需 no-write mode，默认 `true`。 | 如果未来实现无法证明 no-write，必须 fail closed。 |

最小允许输出是 deterministic Markdown 或 JSON dry-run report。harness 不得调用模型、外部 API、
adapter、network service、cloud service 或 product surface。

## 3. Dry-run Flow / Dry-run 流程

未来 dry-run flow：

```text
user message or fixture input
  -> conversation_intake_preview
  -> context_package_preview
  -> candidate_preview
  -> review_queue_preview
  -> boundary_monitor
  -> observatory_snapshot
  -> non_execution_invariants
```

| Step | Preview 目的 | 明确的非执行边界 |
|---|---|---|
| `conversation_intake_preview` | 把输入规范化成 audit-safe envelope。 | 不做 adapter ingest、event write、identity ownership 或 session state write。 |
| `context_package_preview` | 展示哪些 context references 会被考虑、选中、省略或抑制。 | 不执行 retrieval as continuity、不构造 prompt、不写 activation trace、不修改 context。 |
| `candidate_preview` | 展示 input 可能引出的 review objects。 | 不创建 durable candidate、不 approval、不 promotion、不执行 lifecycle。 |
| `review_queue_preview` | 展示 candidates 未来可能如何被 route for review。 | 不存储 queue、不做 lifecycle transition、不执行 policy、不修改 owner assignment。 |
| `boundary_monitor` | 把 forbidden actions 显示为 disabled 或 blocked。 | 不是 runtime enforcement、policy executor 或 automatic mitigation。 |
| `observatory_snapshot` | 附带 observatory vocabulary 的 compact status summary。 | observatory 只显示状态，不决定下一 phase。 |

必须保证：

- no state mutation；
- no memory promotion；
- no recall event write；
- no growth execution；
- no adapter ownership；
- no identity mutation；
- no tool execution；
- no model call；
- no external API call。

## 4. Inputs / 输入

未来 dry-run input envelope 应保持最小：

| Input Field | Required | 含义 | 边界 |
|---|---:|---|---|
| `user_message` | yes | 被 preview 的消息或 fixture content。 | harness 不把它存成 memory。 |
| `session_id` | yes | 本地 preview session reference。 | 不是 durable session runtime。 |
| `actor_id` | yes | 用于 attribution 的 actor reference。 | 不创建或修改 identity。 |
| `timestamp` | no | 可选 timestamp，用于 display 或 deterministic fixture comparison。 | 不是 Temporal Awareness runtime。 |
| `platform_ref` | no | 可选 source label，例如 `local_cli` 或 fixture name。 | 不是 adapter integration 或 platform ownership。 |
| `privacy_scope` | yes | 声明 privacy boundary，例如 `private`、`local` 或 `shareable_fixture`。 | 不清楚时必须倾向 suppression。 |
| `context_request` | no | 可选用户请求的 context focus。 | 不是 automatic retrieval 或 prompt construction。 |

未来实现应在缺少 required fields、unsafe privacy scope 或 unsupported formats 时拒绝输入，且不写 state。

## 5. Outputs / 输出

未来报告应包含：

| Output Section | 含义 | 边界 |
|---|---|---|
| `intake_preview` | normalized input envelope、privacy scope、source reference 和 safe display text 或 redaction note。 | 只是 preview，不是 event persistence。 |
| `selected_context_preview` | candidate context references、omission reasons 和 context gaps。 | 不是 retrieval execution、memory rewrite 或 prompt construction。 |
| `candidate_preview` | 可能的 memory、claim、growth-review、meaning-shift、recall-event 或 task candidates。 | candidate is not promotion。 |
| `review_queue_preview` | candidate ordering、review depth hint、risk label 和 blocked reason。 | review queue preview is not lifecycle。 |
| `boundary_status` | disabled、blocked、RFC-only 或 future-direction boundary flags。 | boundary status 不是 runtime enforcement。 |
| `observatory_summary` | 使用 Foundation Observatory naming 的 compact status summary。 | observatory summary 不是 decision execution。 |
| `non_execution_invariants` | 对 forbidden actions 显式输出 false / disabled flags。 | invariants 是 report assertions，不是 runtime capabilities。 |

必需 non-execution invariants：

```yaml
harness_dry_run_only: true
execution_prohibited: true
state_unchanged: true
identity_core_mutated: false
memory_rewrite_executed: false
recall_mutation_executed: false
growth_engine_executed: false
temporal_event_executed: false
tool_execution_enabled: false
policy_executor_enabled: false
companion_feature_enabled: false
adapter_integration_required: false
model_call_executed: false
external_api_call_executed: false
```

## 6. Candidate Types / 候选类型

未来 dry-run 只允许 preview：

| Candidate Type | Preview 含义 | 明确不是 |
|---|---|---|
| `memory_candidate` | 输入可能与 future memory review 有关。 | memory write、memory rewrite 或 memory promotion |
| `claim_candidate` | 输入可能 create、support、conflict with 或 weaken 某个 claim。 | claim revision 或 belief update |
| `growth_candidate_review` | 输入可能与 future growth review 有关。 | growth promotion 或 identity update |
| `meaning_shift_candidate` | 输入可能影响既有 memory 或 claim 的解释方式。 | semantic mutation 或 memory rewrite |
| `recall_event_candidate` | 输入可能提出 future recall event policy question。 | recall event write |
| `task_update_candidate` | 输入可能提示 future task update。 | task closure、task mutation 或 automatic roadmap execution |

规则：

- candidate is not promotion；
- preview is not persistence；
- review queue preview is not lifecycle；
- candidate risk 可以显示，但不得 authorize execution；
- candidate output 必须在相关时包含 blocked boundaries。

## 7. Boundary Rules / 边界规则

未来 harness dry-run 必须禁止：

- write state；
- mutate identity；
- rewrite memory；
- write recall event；
- promote growth；
- execute tool；
- call model；
- call external API；
- integrate AstrBot；
- integrate adapters；
- run companion behavior；
- run temporal runtime；
- execute policy；
- execute reconstruction reducer；
- compact events；
- create roadmap phase；
- auto-select the next phase。

如果未来实现无法证明某个 boundary 已 disabled，就应该把 dry-run 标记为 blocked，并返回说明原因的报告。

## 8. Relationship To Observatory / 与观察台的关系

未来 `harness-dry-run` 应以 `observatory_snapshot` 收尾，让 founder 能把 interaction pressure 和
`foundation-observatory-report` 使用的同一套 status vocabulary 对齐。

关系：

| Artifact | Role |
|---|---|
| [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) | 定义 snapshot 应复用的 founder-facing status sections。 |
| [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md) | 定义为什么 observability 必须保持 read-only。 |
| [OBSERVATORY_USABILITY_REVIEW.md](./OBSERVATORY_USABILITY_REVIEW.md) | 解释 founder-facing output 为什么必须浅显且 boundary-first。 |
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | 定义 harness 必须 preview-only。 |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | 提供 intake envelope vocabulary。 |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | 提供 context preview vocabulary。 |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | 提供 candidate 和 review queue preview vocabulary。 |
| [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) | 提供 readiness gates 和 non-negotiable boundaries。 |

Observatory 只显示状态。它不 decide、approve、promote 或 execute。harness 不得自动执行
observatory 的 next-step recommendations。

## 9. Tests Plan / 测试计划

如果 P100 明确批准 implementation，第一批测试必须包括：

| Test | Required Assertion |
|---|---|
| Future CLI would run dry-run | future `python3 -m one_core.cli harness-dry-run` implementation 会对 valid fixture input 返回 report。 |
| No state file changed | dry-run 后 state directory checksums 或 mtimes 不变。 |
| Markdown output sections | Markdown 包含所有必需 dry-run sections。 |
| JSON output keys | JSON 包含所有必需 top-level keys。 |
| Chinese output naming | `--lang zh` 使用 founder-facing Chinese display names。 |
| Candidate preview does not promote | candidate outputs 不包含 promotion、lifecycle 或 mutation results。 |
| Boundary monitor disables forbidden actions | 所有 forbidden actions 在 output 中 disabled 或 blocked。 |
| Invalid input handled safely | missing input、unsafe privacy scope、unsupported format 或 path errors 都 fail without state writes。 |
| No model or external call | tests 证明不需要 model、network、adapter 或 external API call。 |
| Output path safety | `--output` 只写请求的 report，不创建 state artifacts。 |

Test fixtures 应 deterministic、local、small。它们不应包含真实 secrets、live chat logs、adapter
payloads、cloud references 或 private conversation exports。

## 10. P100 Candidate Directions / P100 候选方向

P100 只列候选，不由 P99 执行：

1. Minimal CLI Harness Dry-Run Implementation.
2. Harness Dry-Run Output Schema.
3. Boundary Monitor CLI Extension.
4. Context Package Preview Static Generator.

推荐顺序：如果 founder 批准 implementation，从严格 local、no-write、no-model-call dry-run command
和 tests 开始。如果 founder 不批准 implementation，则暂停做 founder / CTO review。

## Non-Execution Statement / 非执行声明

P99 不实现：

- `harness-dry-run`；
- CLI command registration；
- parser changes；
- output schema files；
- validation code；
- tests；
- 超出现有文档检查的 state reads；
- state writes；
- memory writes；
- recall event writes；
- growth lifecycle；
- identity mutation；
- memory rewrite；
- temporal runtime；
- thought loop；
- tool execution；
- model calls；
- external API calls；
- adapter 或 AstrBot integration；
- companion behavior；
- UI；
- product layer；
- policy executor；
- reconstruction reducer execution；
- event compaction；
- automatic roadmap execution；
- P100。
