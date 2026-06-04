# Stateful Memory Encoding Policy v0.1 / 状态化记忆编码策略 v0.1

English version: [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md)

状态：`document-only`、`policy`、`non-runtime`。

P60 定义在 review stateful memory 或 meaning shift claim 之前，最少需要哪些安全的
encoding references。它不创建新 memory store，不修改 schemas，不写 recall events，
不 rewrite memory，不 mutate identity，不 promote growth，不执行 reducers，也不实现
Temporal Awareness。

## Purpose / 目的

P50 引入：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

P59 已澄清 recall event writes 仍然 forbidden。P60 回答下一个基础层问题：在安全
review later recall state 或 meaning shift 之前，关于 original encoding context 至少要知道什么？

如果没有 minimum encoding policy，系统可能过度解释弱 memory records，把 missing
context 误认为 growth，或者把 retrieval artifacts 误认为 continuity evidence。

## Core Rule / 核心规则

```text
missing encoding context weakens interpretation.
missing encoding context does not authorize repair by rewrite.
insufficient encoding context must produce insufficient-context review.
```

Stateful Memory 是 interpretation model。它不是新的 storage layer，也不取代 Memory
Layer provenance。

## Required Minimum Encoding References / 必需最小编码引用

Stateful memory review 应尽可能要求以下 references：

| Field | Purpose | If Missing |
|---|---|---|
| `source_memory_ref` | 标识被解释的 memory record | 不能作为 stateful memory review |
| `source_event_ref` | 把 memory 锚定到产生或导入它的 event | 标记 weak provenance |
| `encoded_at` | 建立 original time of encoding | 标记 temporal gap unknown |
| `encoding_operation` | 说明 memory 是 imported、episodic、semantic、identity、procedural 还是 archived | 标记 origin ambiguous |
| `state_version_ref` | 连接 encoding 和 state version 或 snapshot boundary | 标记 reconstruction weak |
| `provenance_ref` | 记录 source system、adapter、import 或 user/session origin | 标记 source weak |

这些 references 是 review quality 的 policy requirements。P60 不把它们新增为 active
schema fields。

## Conditional Encoding Context / 条件编码上下文

当 memory 相关时，还需要这些 references：

| Context | Needed When | Review Value |
|---|---|---|
| `active_task_refs` | memory 在 ongoing work 中被 encoded | 避免脱离 task 的 reinterpretation |
| `active_claim_refs` | memory 触及 beliefs、decisions 或 contradictions | 区分 meaning shift 和 claim revision |
| `identity_anchor_refs` | memory 与 identity-adjacent context 相关 | 触发 Identity Gate review |
| `privacy_scope` | memory 可能敏感或来自 external logs | 避免不安全 review 或 exposure |
| `salience_at_encoding` | encoding 时已有 salience | 区分 later salience change |
| `confidence_at_encoding` | encoding 时已有 confidence | 区分 later confidence change |
| `dream_artifact_ref` | memory 来自 Dream proposal 或 consolidation | 保留 Dream-proposes boundary |
| `review_decision_ref` | memory 来自 reviewed candidate | 区分 reviewed state 和 raw proposal |

如果 conditional context 相关但缺失，review 应降级为 weak evidence 或 insufficient context。

## Recall-State Dependency / Recall State 依赖

Recall state 不能被孤立判断。后续 recall review 应比较：

- encoding time 当时知道什么；
- memory 现在为什么被 recall；
- 当前 active task、claim、identity 或 governance context 是什么；
- 哪些 evidence 支持 alleged meaning shift；
- 因 encoding context 缺失而仍未知什么。

如果 encoding context 太弱，安全输出是 `insufficient_context`，不是 growth、identity
change、claim revision 或 memory promotion。

## Meaning Shift Eligibility / Meaning Shift 资格

Meaning shift 只有在以下条件满足时才能被 review：

1. source memory 已识别；
2. encoding context 被充分锚定；
3. recall reason 明确；
4. evidence references 解释 shift；
5. missing context 被声明；
6. risk level 和 review gate 已分配。

如果这些条件不满足，shift 应被 rejected、deferred 或标记为 insufficient context。

## Future-Only Fields / 未来字段

下面这些仍然是 future-only，P60 不实现：

- `elapsed_time_since_encoding`；
- `elapsed_time_since_last_recall`；
- `last_recall_ref`；
- `temporal_gap_type`；
- `staleness_hint`；
- `silence_interval`；
- recall event payload；
- growth lifecycle decision。

这些 fields 依赖未来 policy 和 runtime work。P60 只说明它们和 encoding quality 的关系。

## Negative Cases / 反例

系统不得：

- 只靠 similar text 推断 encoding context；
- 通过 rewrite memory 来 backfill missing encoding fields；
- 未经 review 就把 imported logs 当作 identity memory；
- 把 Dream proposals 当作 accepted semantic memory；
- 把 recall state 视为比 encoding state 更权威；
- 把每次 retrieved memory 都变成 stateful memory review；
- 把 weak provenance 当作 productive drift 的证据；
- 因 encoding context 不完整而 promote memory；
- 因旧 memory 现在感觉重要而 mutate Identity Core。

## Relationship To Existing Layers / 与现有层的关系

Memory Layer 负责 storage、provenance、lifecycle、sensitivity 和 retrieval eligibility。

Stateful Memory 负责 encoding、recall 和 meaning shift 的 interpretation vocabulary。

Claim Graph 只接收有 evidence 的 claim-shaped shifts。

Task Hub 只接收 operationally relevant task context 和 stale-work signals。

Identity Gate 接收 identity-adjacent pressure，但 P60 不允许 automatic identity
mutation。

Governance Surface 可以承载未来跨 memory、claim、task、identity 和 event evidence 的
review objects。

## Review Output Guidance / Review 输出指导

未来 review report 应优先输出这些 non-executing outcomes：

- sufficient encoding context for review；
- weak provenance；
- missing temporal anchor；
- missing task/claim/identity context；
- insufficient context；
- identity-gate-required；
- defer pending evidence。

这些 outcomes 本身都不改变 state。

## P61 Handoff / P61 交接

P61 可以定义 Growth Candidate Lifecycle RFC。它必须保留这个规则：lifecycle decision
不是 promotion，不是 memory rewrite，也不是 identity mutation。

在此之前，stateful memory encoding policy 仍是 document-level review policy。
