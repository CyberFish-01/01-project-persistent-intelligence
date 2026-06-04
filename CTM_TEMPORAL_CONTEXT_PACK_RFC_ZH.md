# CTM 时间上下文包 RFC

English version: [CTM_TEMPORAL_CONTEXT_PACK_RFC.md](./CTM_TEMPORAL_CONTEXT_PACK_RFC.md)

状态：`P141`、`RFC-only`、`document-only`、`non-runtime`。

P141 使用 CTM-inspired symbolic vocabulary 定义 future context packages 的 `temporal_pack`。它不实现 temporal runtime、CTM runtime、thought loops、thought-trace storage、recall event writes、temporal event writes、state mutation、memory mutation、identity mutation、model calls、adapter integration、tool execution、policy executor 或 rebuild。

## 核心规则

```text
temporal_pack 是 symbolic review context。
symbolic temporal context 不是 thought execution。
elapsed time 是 evidence cue，不是 identity update。
```

## Pack 目的

future `temporal_pack` 帮助 model-as-resource 或 founder-facing preview 看见 time-related review pressure，同时不假装系统拥有 biological time awareness 或 neural CTM dynamics。

## 允许字段

pack 可以包含：

- `elapsed_time_since_encoding_hint`
- `elapsed_time_since_last_review_hint`
- `session_gap_hint`
- `interruption_hint`
- `unresolved_tension_note`
- `delayed_alignment_candidate`
- `review_depth_suggestion`
- `temporal_coherence_question`
- `thought_trace_policy_reminder`
- `temporal_boundary_reminder`

## 禁止字段

pack 不得包含：

- hidden chain-of-thought；
- private model reasoning；
- neural synchronization claim；
- CTM runtime state；
- thought loop state；
- temporal event record；
- recall event record；
- salience mutation；
- identity mutation；
- memory rewrite。

## Temporal Cue Matrix

| Cue | Meaning | Allowed Use | Forbidden Interpretation |
|---|---|---|---|
| elapsed time | 时间可能影响 review framing。 | 询问 meaning 是否需要重新 review。 | 时间自动改变 memory。 |
| session gap | 暂停可能影响 context confidence。 | 标记 context freshness risk。 | pause 创建 temporal event。 |
| unresolved tension | 一个 conflict 仍 open。 | 建议更深 manual review。 | conflict aging 成 identity change。 |
| delayed alignment | 后来 evidence 可能澄清 earlier meaning。 | 只创建 review candidate。 | 自动 promote growth。 |
| review depth | 风险可能需要更谨慎 review。 | 建议 shallow/medium/deep review。 | 执行 deliberation ticks。 |
| thought-trace policy | trace storage 很敏感。 | 提醒什么不能被存储。 | 捕获 hidden thoughts。 |

## CTM-Inspired Mapping

P141 只把 CTM 用作 symbolic review vocabulary 的启发：

- temporal dynamics -> state-over-time review cues；
- synchronization -> symbolic coherence question；
- ticks -> review-depth planning language；
- trace -> storage-policy reminder；
- coherence break -> review risk signal。

它不声称：

- consciousness；
- biological equivalence；
- neural synchronization；
- actual internal thought cycles；
- model training 或 CTM implementation。

## Boundary Injection

每个 `temporal_pack` 必须包含：

- `symbolic_only: true`
- `ctm_runtime_allowed: false`
- `thought_loop_allowed: false`
- `thought_trace_storage_allowed: false`
- `temporal_event_write_allowed: false`
- `recall_event_write_allowed: false`
- `identity_update_allowed: false`

这些是 planned contract fields，不是 P141 已实现 runtime flags。

## 与其他 Packs 的关系

`temporal_pack` 不应替代：

- `memory_pack`：memory references 仍需要 source backing；
- `claim_pack`：claims 仍需要 evidence；
- `boundary_pack`：forbidden actions 仍是 global；
- `response_strategy_pack`：future model instructions 仍需要 explicit wording。

## 未来测试预期

如果后续实现，tests 应验证：

- temporal pack 只在 relevant 时出现；
- every cue has a review-only label；
- forbidden temporal actions remain false；
- no thought trace is stored；
- no recall or temporal event is written；
- temporal cues do not mutate identity or memory。

## 完成声明

P141 给 CTM-inspired temporal dynamics 一个安全位置：在 future context packages 中保持 symbolic、visible、bounded 和 review-only。
