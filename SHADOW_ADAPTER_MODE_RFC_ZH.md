# Shadow Adapter Mode RFC / 影子 Adapter 模式 RFC

English version: [SHADOW_ADAPTER_MODE_RFC.md](./SHADOW_ADAPTER_MODE_RFC.md)

状态：`P123`、`RFC-only`、`document-only`、`non-runtime`。

P123 定义任何 live adapter integration 前的 future shadow adapter boundary。它不实现 adapter code、AstrBot integration、network access、message ingestion、event writes、memory writes、identity mutation、model calls 或 rebuild。

## 问题

Adapter 有用，因为它能揭示真实平台如何塑造交互。Adapter 也危险，因为它可能悄悄变成 identity、memory、session truth 或 social behavior 的拥有者。

在连接旧 01、AstrBot、Telegram、QQ、Web 或任何外部 adapter 前，项目需要一种模式：能观察 adapter input，但不让它变成 core state。

## Shadow 命题

```text
shadow adapter observes shape.
shadow adapter does not ingest.
platform context is not identity.
adapter metadata is not memory.
shadow evidence is not integration approval.
```

Shadow Adapter Mode 是一种 future local、no-write、no-network 边界：adapter-shaped input 可以作为 artifact 被 preview，但不能影响正式 state。

## 允许的未来 Shadow Inputs

未来 shadow adapter previews 可以包含：

- `adapter_id`；
- `platform_name`；
- `channel`；
- `session_id`；
- `actor_id`；
- `timestamp`；
- `message_shape`；
- `metadata_shape`；
- `privacy_scope`；
- `redaction_status`；
- `source_confidence`；
- `boundary_flags`。

P123 不创建该 schema 或 parser。

## 禁止 Live Integration

Shadow mode 禁止：

- live network connection；
- platform API calls；
- AstrBot plugin deployment；
- adapter ingest endpoint calls；
- `/v1/adapter/ingest` writes；
- conversation event writes；
- memory writes；
- recall event writes；
- identity mutation；
- Companion behavior；
- UI 或 product layer；
- model calls；
- tool execution；
- rebuild start。

## Shadow Output

未来 shadow report 可以显示：

- platform shape preview；
- adapter ownership warning；
- privacy and redaction warnings；
- candidate routes；
- quarantine route；
- highest relevant boundaries；
- source-backed RFC refs；
- non-execution invariants。

它不能创建真实 review lifecycle、写 state 或授权 integration。

## Candidate Routes

Adapter-shaped input 只能成为：

- `adapter_context_artifact`；
- `prompt_contamination_candidate`；
- `identity_claim_candidate`；
- `memory_claim_candidate`；
- `task_context_candidate`；
- `privacy_review_candidate`；
- `import_quarantine_candidate`。

Candidate 不是 adoption。Shadow 不是 integration。Metadata 不是 memory。

## 与 P121-P122 的关系

P121 冻结 core boundary。P122 隔离 imports。P123 把同样逻辑应用到 adapters。

如果 adapter 导出历史，它走 P122 import quarantine。如果 adapter stream live context，在未来明确 integration gate 存在前，它只能保持 shadow-only。

## CTM-Inspired Temporal Dynamics 边界

Adapters 常带 timestamps、pause/resume signals 和 session gaps。Shadow mode 可以把它们 preview 成 temporal pressure，但不能创建 temporal state。

阻止：

- temporal runtime；
- temporal event writes；
- recall event writes；
- elapsed-time salience mutation；
- thought loop execution；
- thought trace storage。

允许的未来 preview：

- 把 session gap 标为 `temporal_review_candidate`；
- 引用 Temporal Awareness / CTM RFC source refs；
- 路由到 manual review depth planning。

## Tool-First In-Situ Self-Evolution 边界

Adapters 可能报告 tool results、commands 或 automation suggestions。Shadow mode 把它们当作 unverified capability claims。

阻止：

- tool execution；
- automatic tool promotion；
- policy executor；
- tool library mutation；
- dependency installation；
- capability evidence mutating identity。

允许的未来 preview：

- `unverified_capability_claim`；
- `tool_candidate`；
- `procedure_candidate`；
- `cautionary_procedural_memory_candidate`；
- `capability_review_candidate`。

## Integration Gate Requirements

未来任何 live adapter integration 被考虑前，项目需要：

- import quarantine policy accepted；
- contamination scan policy accepted；
- privacy/redaction policy accepted；
- no-write shadow report tested；
- adapter ownership boundaries visible；
- founder approval；
- explicit rollback plan；
- 证明 01 Core owns state and adapters only translate。

P123 不满足这些要求。它只命名这些要求。

## P124 候选方向

推荐 P124：**Contamination Scan RFC**。

它应定义如何把 prompt contamination、model memory claims、adapter artifacts 和 unverified capability claims 检测成 review candidates，同时不执行 scanner runtime。
