# Harness 后创始人复盘

English version: [POST_HARNESS_FOUNDER_REVIEW.md](./POST_HARNESS_FOUNDER_REVIEW.md)

状态：`P111`、`review-only`、`planning`、`document-only`、`non-runtime`。

P111 复盘 P102-P110 是否真的解决了 P101 的可用性问题，并判断是否适合考虑 State-Backed
Read-Only Harness。它不修改 harness runtime、不改 CLI、不写 state、不写 memory、不写 recall
event、不改 identity、不执行工具、不接 adapter、不进入 UI 或产品层。

## 1. P101 的问题是什么？

P101 发现第一版 `harness-dry-run` 安全，但太静态。

它已经证明了最重要的边界：no state write、no memory write、no recall write、no identity
mutation、no model call、no adapter、no tool execution。但它还不能帮助 founder 看懂“一条具体输入”
给系统带来的压力是什么。

P101 的主要问题：

- 很不同的输入几乎得到同一张 candidate table；
- `context_package_preview` 基本是通用 foundation references；
- growth、AstrBot、product-layer、tool-library 问题没有明显分流；
- boundary flags 可见，但对当前输入不够响亮；
- founder-facing 可读性评分只有 **6.5 / 10**；
- harness 能阻止坏动作，但还不能帮助判断下一步该审什么。

## 2. P102-P110 分别解决了什么？

| Phase | 解决了什么 | 仍保持的边界 |
|---|---|---|
| P102 | 加入 deterministic pressure routing，覆盖 observability、growth、adapter、product、capability、temporal、reconstruction、unknown。 | classification 只是规则匹配，不是理解。 |
| P103 | 加入 founder summary、人话风险、next step 和 do-not-do list。 | summary 是 report text，不是 decision execution。 |
| P104 | 加入 Scenario Profile Test Matrix，让 pressure profiles 有 expected outputs。 | matrix 是文档，不是 runtime policy。 |
| P105 | 强化 boundary monitor，加入 structured disabled capabilities 和 active violations。 | monitor 是 audit output，不是 enforcement。 |
| P106 | 专门化 candidate previews，加入 intent、selection reason、blocked promotion 和 manual review target。 | candidate 仍是 preview-only。 |
| P107 | 专门化 review queue previews，加入 queue intent、gate reason、blocked lifecycle 和 manual-review-only action。 | review routing 不是 lifecycle。 |
| P108 | 对八类输入重新做 usability review，并记录提升。 | review 是 evidence，不是 authorization。 |
| P109 | 加入 roadmap，说明 harness 能看见什么、看不见什么。 | roadmap 不是 implementation approval。 |
| P110 | 用 commits、tests、boundary audit 和 stop condition 收口夜间 cycle。 | summary 不是 P111/P112 execution。 |

## 3. P108 founder-facing 可读性评分是否提升？

是。

P101 founder-facing readability：**6.5 / 10**。

P108 founder-facing readability：**8.0 / 10**。

这个提升可信，因为它直接对应 P101 的原始痛点：

- 输入不再共用一张通用候选表；
- 顶部能看到 pressure type 和 matched signals；
- candidates 会解释为什么被选中，以及为什么不能 promotion；
- review gates 会解释为什么不创建 lifecycle；
- boundary monitor 会突出当前最相关的 blocked capabilities；
- 每个 profile 都有具体人工下一步和 do-not-do list。

分数没有更高，是因为 harness 仍不读取真实 state。

## 4. 哪些 pressure type 最有效？

最有效的 pressure types：

- `adapter_boundary_pressure`：AstrBot / platform 压力很容易被误推进，它现在会清楚进入 adapter
  boundary review，并阻止 integration。
- `capability_evolution_pressure`：很好地表达 P92 原则：verification is not authorization。
- `growth_review_pressure`：把 growth review 放在 primary，同时继续阻止 identity mutation 和 growth execution。
- `product_layer_pressure`：能阻止“项目看不清，所以先做 UI”的跳跃。
- `reconstruction_pressure`：payload/diff、replay、reducers、compaction 容易混淆，现在能分开。

## 5. 哪些 pressure type 仍然像模板？

仍有模板感的 pressure types：

- `observability_pressure`：能正确路由到 observatory readability，但还不能用一段朴素摘要回答“项目到底做了什么”。
- `temporal_pressure`：边界正确，但仍依赖 elapsed time、recall write、temporal event、delayed interpretation 等 RFC 词。
- `unknown_pressure`：安全保守，但普通 note-like 输入会显得无用，因为写入仍被禁止。

这些对 dry-run harness 是可接受的，但说明 read-only state-backed view 下一步会有价值。

## 6. `candidate_preview` 是否更具体？

是。

P101 的 candidate preview 安全但通用。P106 之后 candidates 会按 pressure 变化：

- adapter 输入显示 adapter boundary、task update、governance boundary；
- growth 输入显示 growth review、meaning shift、identity high gate；
- tool-library 输入显示 capability growth、tool authorization、cautionary procedural memory；
- temporal 输入显示 temporal review、recall-write、delayed interpretation；
- reconstruction 输入显示 reconstruction evidence、payload/diff gap、replay check。

每行现在都会说明：

- candidate intent；
- 为什么被选中；
- 为什么不能 promotion；
- 未来需要哪个 manual review gate；
- `preview_only`、`promoted: false`、`persisted: false`。

这已经解决了“同一张静态候选表”的问题。

## 7. `review_queue_preview` 是否更清楚？

是。

P107 让 review gates 解释：

- queue intent；
- candidate 为什么路由到这个 gate；
- 为什么 lifecycle creation 被阻止；
- manual review is required；
- next allowed action 是 `manual_review_only`；
- lifecycle creation 和 execution 继续为 false。

这解决了 P101 中“review queue 安全但太薄”的问题。它现在更像在说“未来人类会从这里看”，而不是暗示一个 live workflow。

## 8. `boundary_monitor` 是否足够显眼？

基本足够。

P105 让 boundary monitor 成为 harness 最强的部分：

- forbidden capabilities 被结构化为 disabled rows；
- unchanged state 明确显示；
- active boundary violations 为空；
- all forbidden actions disabled；
- 每种 pressure 会突出当前输入最相关的 boundaries。

剩余问题：Markdown 中 boundary monitor 仍然较长、视觉密度高。未来可以在完整表格前加一个 compact
“top blocked actions” 区域，但这只能是 display-only。

## 9. `observatory_snapshot` 是否帮助 founder 决策？

部分有帮助。

它现在会跟随 selected pressure type 和 top risks，这足以阻止“现在接 AstrBot”或“现在做 UI”这类过早移动。

但它还不能回答更深的 founder 问题，因为它不读取真实 state、events、memory summaries、task status 或
artifact coverage。它是 pressure-aligned status hint，不是 state-backed project diagnosis。

## 10. 当前是否适合进入 State-Backed Read-Only Harness？

适合，但定义必须很窄。

项目适合进入 **State-Backed Read-Only Harness planning 或最小只读阶段**，但不适合进入 runtime、product、
adapter 或 memory-writing phase。

原因很简单：P102-P110 已经解决了静态 routing 问题。现在的弱点不再是“harness 分不清输入”，而是
“harness 不能显示现有 state evidence 是否真的支持这个 preview”。

只要 state-backed 的含义是 read-only inspection 和 report output only，这就是下一条安全边界。

## 11. 如果适合，P112 应该做什么？

推荐 P112：**State-Backed Read-Only Harness Plan**，或在 founder 明确批准时做非常小的只读实现。

最安全的 P112 范围：

- 定义哪些现有 local state/report files 可以被读取；
- 定义 read-only state snapshot envelope；
- 加入 `state_refs_preview`，不是 real retrieval；
- 展示 selected refs、omitted refs 和 missing evidence；
- 测试 command 前后 state directory files 不变化；
- 所有 candidates 继续 preview-only；
- 所有 review gates 继续 manual-review-only；
- 所有 forbidden boundary flags 继续 disabled/false；
- 不调用 model、tools、adapter、network、AstrBot、UI 或 product code。

P112 不应实现 memory search as continuity、claim mutation、task writes、recall writes、temporal runtime、
reducer execution 或 policy execution。

## 12. 如果不适合，还应该继续改哪里？

如果 founder 判断 P112 仍然太早，继续做 review-only 改进也有价值：

- 减少中文显示里 English internal keys 的拥挤感；
- 加一个更短的 top-level “这条输入意味着什么”摘要；
- 改进 temporal 和 unknown pressure 文案；
- 让 risk explanations 更贴近具体输入，少一些模板感；
- 在写任何代码前定义 state-backed read-only contract；
- 审查现有 state files 是否适合被 dry-run report 读取。

这些是 refinement，不是 blocker。P101 的主要问题已经解决到足以考虑下一条只读边界。

## 创始人判断

P102-P110 没有让 harness 变“聪明”。它让 harness 变“可读”。

这正是当前阶段应该取得的进展。项目现在不该继续堆抽象层，而应决定是否允许 harness 读取一个小的、明确的、本地的、只读的 existing state snapshot。

## 边界声明

P111 只是 review-only。它不授权 runtime work、product work、adapter integration、Companion behavior、
model calls、真实 retrieval、event writes、memory writes、recall writes、identity mutation、growth
execution、temporal runtime、tool execution、policy execution、reconstruction reducer execution、event
compaction、automatic tool promotion 或 automatic roadmap execution。
