# Open Questions / 开放问题

English version: [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md)

P53 记录 P51 之后仍未关闭的基础层问题。这些是 future directions，不是当前实现指令。

## Temporal Awareness / 时间感知

问题：elapsed time 如何成为 subject state transition 的一部分？

子问题：

- `elapsed_time_since_encoding` 如何影响 meaning shift？
- `elapsed_time_since_last_recall` 如何影响 salience？
- `long_pause`、`interruption`、`resumed_session` 是否应该成为 temporal events？
- task staleness、claim staleness、memory decay、relationship silence 是否应该进入 temporal state？

P53 不实现。

## Growth Candidate Lifecycle / 成长候选生命周期

问题：`growth_candidate_review` 未来是否需要 acknowledge、archive、quarantine 或 defer decision？

风险：lifecycle 容易被误解为 promotion。除非未来 phase 明确定义 promotion boundary，否则它必须保持 review-only。

## Recall Event Write Policy / 回忆事件写入策略

问题：什么样的 recall 足够重要，可以成为 event candidate？

边界：普通 retrieval 不应写 event。只有 meaning-shifting recall 未来才可能成为 candidate。

## Stateful Memory Minimal Encoding Policy / 状态化记忆最小编码策略

问题：stateful memory 所需的最小安全 `encoding_state` 是什么？

候选字段：

- source event id；
- timestamp；
- active task ids；
- active claim ids；
- identity anchor refs；
- privacy scope；
- salience/confidence。

## Reconstruction Reducer Contract / 重建 reducer 契约

问题：什么 contract 可以让 event records 重建 object-level state？

需要：

- reducer input schema；
- target path identity；
- payload/diff requirements；
- validation metadata；
- rollback 和 seed/pre-event references。

contract 被 review 之前，不执行 reducer。

## Payload / Diff Capture Policy / Payload 与 Diff 捕获策略

问题：哪些 state paths 需要 full payload、object diff、snapshot link 或 reference-only treatment？

风险：capture policy 容易滑向 accidental event schema mutation。除非明确进入实现 phase，否则保持 review-only。

## Subject Kernel / World Seed Direction / 主体内核与世界种子方向

问题：Identity Seed 是否应该拆成更小的 subject kernel 和 world seed？

目的：让 Identity Core 保持小而稳定，同时允许 world/context orientation 演化，而不是改写 identity。

## Exploration / Serendipity Engine / 探索与偶然性引擎

问题：系统如何支持 exploration，同时避免 collapse、roleplay residue 或 ungrounded identity changes？

边界：exploration 应生成 record-only 或 review-only signals，而不是 automatic growth。

## Productive Drift vs Collapse / 生产性漂移与崩塌

问题：系统如何区分 evidence-backed productive drift、random drift、identity-threatening drift 和 collapse？

需要：

- evidence threshold；
- risk level；
- review gate；
- anti-growth rejection reasons；
- temporal aging policy。
