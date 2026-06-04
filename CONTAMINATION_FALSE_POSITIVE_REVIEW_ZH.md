# 污染误报复盘

English version: [CONTAMINATION_FALSE_POSITIVE_REVIEW.md](./CONTAMINATION_FALSE_POSITIVE_REVIEW.md)

状态：`P129`、`review-only`、`document-only`、`non-runtime`。

P129 复盘 Core Lockdown / Quarantine stack 中的 false-positive 风险。它不实现 scanner、classifier、validator、enforcement engine、quarantine storage、import runtime、adapter integration、model call、write path 或 rebuild。

## 为什么需要它

项目需要 contamination detection language，但 detection 很容易变得过度自信。

误报很重要，因为未来 scan 可能把有用、无害或 founder 写的材料错误标成 contamination。这会阻塞合法 review，损害系统可信度，或者让 founder 把 scanner output 当作 verdict。

规则是：

```text
detection 是 suspicion。
suspicion 不是真相。
false positive review 必须早于 enforcement。
enforcement 尚未实现。
```

## False Positive Classes

| False Positive Class | Example | Why It Can Happen | Safe Handling |
|---|---|---|---|
| `founder_note_misread_as_prompt_contamination` | Founder 在 planning note 中写“以后采用这个”。 | 这句话看起来像 imperative。 | 路由到 founder clarification，而不是 contamination verdict。 |
| `historical_summary_misread_as_memory_claim` | 文档总结早期设计决策。 | 它听起来像 remembered history。 | quarantine 前检查 source class 和 citation。 |
| `adapter_example_misread_as_live_adapter` | synthetic adapter shape 提到 platform fields。 | 形状像真实 payload。 | 除非 source 说明 live，否则保持 synthetic fixture。 |
| `tool_plan_misread_as_tool_execution` | RFC 说未来某个 tool 可以被验证。 | Capability language 像 execution。 | 标记为 RFC-only capability candidate。 |
| `temporal_rfc_misread_as_runtime` | 文档讨论 elapsed time 或 review depth。 | Temporal language 听起来像 operational。 | 保持 symbolic review vocabulary。 |
| `rebuild_plan_misread_as_rebuild_started` | checklist 定义 rebuild entry criteria。 | Planning language 听起来像 action。 | 保持 entry-gate planning，直到明确批准 start。 |

## 审查问题

任何 future contamination candidate 都应该问：

- source 是 synthetic、founder-authored、whitelisted 还是 external？
- 这段话是 plan、example、quote、fixture，还是 actual instruction？
- artifact 是否说明自己是 RFC-only、review-only 或 non-runtime？
- 是否有真实 write path 的证据，还是只有 planning language？
- 这是否可能只是有用 warning，而不是 contamination？
- 如果错误 quarantine，会损失什么？
- 在路由前是否需要 founder review 澄清 intent？

## 允许结果

False-positive review 可以产生：

- `confirmed_contamination_candidate`
- `likely_false_positive`
- `needs_founder_clarification`
- `keep_as_fixture`
- `keep_as_rfc_language`
- `defer_without_action`

它不能产生：

- automatic deletion；
- automatic quarantine storage；
- automatic rejection of a whole source；
- memory rewrite；
- identity mutation；
- event compaction；
- tool disablement；
- adapter blocking as runtime enforcement；
- rebuild blocking as execution。

## CTM-Inspired Temporal Dynamics 边界

Temporal vocabulary 有很高误报风险。`tick`、`thought_trace`、`delayed_alignment`、`temporal_coherence` 和 `unresolved_tension` 这类词，在后续批准 runtime 之前都是 planning terms。

False-positive review 不能把 symbolic temporal discussion 当成 CTM runtime、thought-loop execution、temporal event writes、recall event writes 或 identity change 的证据。

## Tool-First Self-Evolution 边界

Capability vocabulary 也有很高误报风险。`verification`、`tool_candidate`、`procedure_candidate`、`skill_memory` 和 `capability_growth_candidate` 这类词，在明确批准 execution 前都是 review vocabulary。

False-positive review 不能把 tool plan 当成 tool execution，也不能把 verification note 当成 tool authorization。

## Founder-Facing 展示

未来 report 应显示三列：

| Signal | Meaning | Founder Interpretation |
|---|---|---|
| contamination signal | 某个模式看起来有风险。 | 审查它；暂时不要信任。 |
| false-positive possibility | 这个模式可能只是无害 context。 | 不要过度反应。 |
| required gate | 一个 human review surface 拥有下一步决定。 | 没有 automatic action。 |

这样 report 能保持有用，但不变得惩罚化。

## 剩余风险

- 未来 scanner 可能过度标记普通 planning text。
- founder-facing reports 可能让 warnings 看起来像 verdicts。
- quarantine language 可能压制有用 examples。
- Capability 或 temporal terms 可能被误读成 runtime。
- false-positive route 可能变成删除或忽略困难案例的借口。

## 完成声明

P129 补上了一条必要谨慎：lockdown 要保护 core，但不能把每个 warning 都变成 verdict。未来 scan outputs 必须保持 review-only，并且在任何 enforcement 被讨论前必须包含 false-positive handling。
