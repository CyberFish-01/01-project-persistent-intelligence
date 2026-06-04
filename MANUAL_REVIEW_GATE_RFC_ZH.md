# 人工审查门 RFC

English version: [MANUAL_REVIEW_GATE_RFC.md](./MANUAL_REVIEW_GATE_RFC.md)

状态：`P146`、`RFC-only`、`document-only`、`non-runtime`。

P146 定义 future candidates 和任何 durable state change 之间必须存在的 manual review gate。它不实现 review lifecycle、approval storage、event writes、memory writes、recall writes、identity mutation、growth execution、tool execution、policy executor、adapter integration、model calls 或 rebuild。

## 核心规则

```text
manual review 是 gate。
gate 不是 approval。
approval 不是 write execution。
write policy 必须早于 write。
```

## Gate 目的

manual review gate 防止 preview candidates 仅仅因为合理、有用、情绪显著或由模型生成，就变成 durable state。

它创建一个位置，让 founder 判断某个东西是否值得以后进入 write-policy path。

## Review Gate Types

| Gate | Owns | Default Decision |
|---|---|---|
| memory review | memory-like candidates | no write |
| claim review | factual/project claims | evidence check |
| task review | task update candidates | manual planning |
| identity high gate | identity-bearing claims | reject or quarantine by default |
| growth review | meaning shift/growth candidates | no promotion |
| recall policy review | recall event candidates | no write |
| temporal review | elapsed-time and coherence cues | symbolic only |
| capability review | tool/procedure/capability candidates | no execution |
| quarantine review | untrusted/external/model output | containment |
| rebuild checkpoint | migration/rebuild pressure | blocked until final verification |

## 必需 Review Questions

每个 gate 都应询问：

- source 是什么？
- trust level 是什么？
- 有什么 evidence 支持？
- 如果接受，会改变什么？
- 可能违反哪个 boundary？
- 是否有 lower-risk outcome？
- 这种类型是否已有 write policy？
- founder approval 是否明确覆盖这个 action？

## 允许 Outcomes

Manual review 可以产生：

- `reject`
- `keep_preview_only`
- `keep_quarantined`
- `defer_pending_evidence`
- `route_to_lower_risk_note`
- `route_to_future_write_policy`

它不能直接产生：

- state write；
- memory write；
- recall event write；
- identity mutation；
- growth promotion；
- tool execution；
- tool authorization；
- adapter integration；
- rebuild start。

## 最低风险未来写入

如果后续批准，第一类 possible future write 应该是：

- founder decision note；
- review note；
- low-risk planning note。

即使如此，也需要后续明确 write policy，P146 不授权它。

## CTM-Inspired Temporal Gate

Temporal review 可以考虑 elapsed time、interruption、unresolved tension、delayed alignment 和 review depth。它不得写 temporal events、recall events、thought traces、salience changes、CTM runtime state 或 identity updates。

## Tool-First Gate

Capability review 可以考虑 tool candidates、procedure candidates、verification evidence 和 cautionary procedural memory candidates。它不得执行工具、晋升工具、授权工具、安装依赖、修改工具库或声称 subject growth。

## 未来测试预期

如果后续实现，tests 应验证：

- every candidate routes to a gate；
- gate output remains non-persistent unless a later write policy exists；
- identity 和 recall gates default to no write；
- temporal 和 capability gates keep forbidden actions false；
- approval alone cannot write state；
- missing gate causes fail-closed output。

## 完成声明

P146 把 manual review 定义为任何 future durable change 前必需的人类 gate。它明确保持 review 与 approval 分离，approval 与 write execution 分离。
