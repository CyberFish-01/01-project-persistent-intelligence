# 隔离审查门计划

English version: [QUARANTINE_REVIEW_GATE_PLAN.md](./QUARANTINE_REVIEW_GATE_PLAN.md)

状态：`P127`、`document-only`、`review-gate-plan`、`non-runtime`。

P127 定义未来 quarantined inputs 在甚至被考虑为 candidate 之前，应如何被人工审查。它不实现
quarantine storage、import processing、scanner runtime、validator runtime、event writes、memory
writes、identity mutation、model calls、adapter integration、tool execution 或 rebuild。

## 核心规则

```text
quarantine 是 containment。
review 不是 adoption。
candidate status 不是 promotion。
rejection 是有效结果。
```

这个 review gate 的作用，是防止 untrusted content 仅仅因为有趣、情绪上显著、看起来合理或很方便，就穿过边界进入 trusted 01 Core state。

## Gate 阶段

| Stage | Purpose | Allowed Output | Forbidden Output |
|---|---|---|---|
| intake containment | 在解释前把未来输入标记为 untrusted。 | quarantine preview | formal event、memory、claim、recall、identity 或 tool record |
| source classification | 识别来源是 model output、old 01 material、adapter context、tool evidence、prompt text 或 external file。 | source class label | source trust |
| contamination classification | 映射到 P121-P126 的 contamination class。 | contamination class preview | truth decision |
| evidence sufficiency review | 检查 provenance 是否足够后续审查。 | evidence gap note | automatic acceptance |
| boundary route selection | 判断后续哪个 manual gate 拥有 review。 | review gate route | lifecycle execution |
| founder decision point | 询问这类输入是否可以进入后续 no-write candidate plan。 | keep quarantined、reject 或 defer | state write 或 promotion |

## 审查门

| Gate | Handles | Minimum Questions | Safe Decision |
|---|---|---|---|
| memory review | untrusted memory-like claims | 谁断言的、什么时候、来自什么来源？ | 除非 provenance 明确，否则保持 quarantined |
| claim review | factual 或 project claims | 是否有超出 model assertion 的 source evidence？ | founder review 后才可路由到 claim candidate |
| identity high gate | identity-bearing statements | 是否改变 Identity Core、seed 或 life-history claims？ | 默认 reject 或 keep quarantined |
| adapter boundary review | platform-shaped context | 这是否只是外部平台 metadata？ | 只保持 shadow observation |
| capability review | tool/procedure claims | success 是否可复现并被授权？ | 只能是 evidence candidate，绝不变成 tool trust |
| temporal review | elapsed-time interpretations | 时间是否被当作 evidence，而不是真相？ | review-only temporal cue |
| rebuild entry gate | migration/rebuild pressure | 所有 pre-rebuild checks 是否通过？ | 阻塞到 final founder checkpoint |

## Quarantine Outcomes

未来 review 可以选择：

- `keep_quarantined`
- `reject_as_contamination`
- `defer_pending_provenance`
- `route_to_candidate_preview`
- `route_to_false_positive_review`

它不能选择：

- `promote_to_memory`
- `mutate_identity`
- `write_event`
- `write_recall`
- `enable_tool`
- `start_rebuild`

## Evidence 规则

可供后续 review 使用的 evidence 包括：

- source type；
- timestamp if available；
- provenance note；
- originating channel or file class；
- manual founder note；
- tool/procedure claims 的 reproducibility note；
- redaction/privacy note。

不足够的 evidence 包括：

- model confidence；
- emotional salience；
- repeated wording；
- adapter label alone；
- elapsed time alone；
- one-off tool success；
- 缺少 provenance 的“旧 01 是这么说的”。

## CTM-Inspired Temporal Dynamics 边界

Temporal review 可以询问 elapsed time、interruption、delayed alignment 或 unresolved tension 是否改变 review priority。它不能创建 temporal events、recall events、thought traces、identity updates、memory rewrites 或 CTM runtime。

## Tool-First Self-Evolution 边界

Capability review 可以把 tool 或 procedure claim 路由到 evidence review。它不能执行工具、晋升工具、安装依赖、创建 policy executor，或把 capability improvement 当成 subject growth。

## 未来 Validator Contract

未来 no-write validator 可以检查 fixture 是否遵守 gate plan，但 P127 不实现它。

任何 future validator 必须证明：

- input 是 synthetic 或 explicitly allowed；
- state directory 没有变化；
- formal event 或 memory file 没有变化；
- 所有 promotion-like outcomes 都不存在；
- 所有 forbidden capabilities 保持 disabled；
- 任何 candidate 前进前都需要 founder review。

## 完成声明

P127 给 quarantine 一份 founder-readable review gate plan。它让 quarantine 保持 containment，防止 review language 变成 adoption、execution 或 state mutation。
