# 试验台可用性审查

English version: [HARNESS_USABILITY_REVIEW.md](./HARNESS_USABILITY_REVIEW.md)

状态：`review-only`、`document-only`、`non-runtime`。

P101 审查 P100 的 `harness-dry-run` command 是否真的能让 founder 看清：一条输入会如何经过
01 Core 的处理路径。它不改变 Identity Core、memory、recall policy、retrieval、AstrBot、UI、
model calls、tool execution 或 next-step execution。

## 已审查命令

对下面每条输入，本次审查都运行了：

- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format markdown --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format json --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang en --format markdown --output /private/tmp/...`

输入：

- “我现在有点看不清这个项目到底做了什么”
- “这个想法可能是一次成长吗？”
- “我想把这个接进 AstrBot”
- “我们是不是该开始做应用层了？”
- “这个工具候选验证成功了，能不能直接加入工具库？”

所有临时 `--output` 文件都写在仓库外。

## 可读性评分

整体 founder-facing 可读性：**6.5 / 10**。

| 区域 | 分数 | 原因 |
|---|---:|---|
| 输入预览 | 8 | input、session、actor、privacy scope、CLI source 和 no-write 状态很容易看到。 |
| 上下文包预览 | 5 | 能看到 foundation references，但非常不同的输入都会得到同一套静态背景。 |
| 候选项预览 | 5 | 能说明 candidate 不是 promotion，但每条输入都会得到同一张候选表。 |
| 审查队列预览 | 7 | `lifecycle_created: false` 和 `execution_allowed: false` 清楚表达 review-only。 |
| 边界监视器 | 8.5 | 这是最强的区域。禁止事项都明确显示为 disabled。 |
| 观察台快照 | 6 | 能列出真实最高风险，但不够针对当前输入。 |
| 中文文案 | 6.5 | 分区标题清楚，但一些行仍像 RFC 术语翻译。 |
| 帮 founder 判断下一步 | 5.5 | 能阻止过早执行，但还不能帮助选择下一步该审什么。 |

## 每组输入观察

| 输入 | 好用之处 | 不足之处 |
|---|---|---|
| “我现在有点看不清这个项目到底做了什么” | 观察台快照正确把“概念太多看不清”列为最高风险。 | 报告仍没有用朴素项目摘要直接回答 founder 的困惑。 |
| “这个想法可能是一次成长吗？” | 出现 `growth_candidate_review`，并且保持 `promoted: false`。 | growth 问题没有被突出；memory、claim、recall、task 看起来同样相关。 |
| “我想把这个接进 AstrBot” | 边界监视器里能看到 `adapter_integration_required: false`。 | 报告没有直接说“这里不允许接 AstrBot”；信号存在，但不够显眼。 |
| “我们是不是该开始做应用层了？” | 快照里列出“过早做运行时”高风险。 | 输出没有直接把产品层/应用层压力标成当前主问题。 |
| “这个工具候选验证成功了，能不能直接加入工具库？” | tool execution 保持 disabled，也没有 promotion。 | harness 没有 capability/tool-candidate 路由，因此错过了 P92 的关键边界：verification is not authorization。 |

## 好用的部分

- command 证明了 P100 边界：local preview、no model call、no adapter call、no state write、
  no memory write、no recall write、no identity mutation。
- 报告结构是有用的：intake、context preview、candidate preview、review queue、boundary
  monitor、observatory snapshot 和 non-execution invariants。
- 边界监视器足够 founder-readable，可以检查 forbidden actions。
- candidate rows 明确显示 `preview_only: true`、`promoted: false`、`persisted: false`。
- JSON 输出对未来 static review 有结构价值，但它仍只是 report artifact，不是 execution contract。

## 仍然抽象的部分

- `context_package_preview` 基本还是静态 foundation reference list。它还没有解释为什么这条输入选了这些背景。
- `candidate_preview` 有机械感，因为每条输入都会生成同样六种 candidate。
- `observatory_snapshot` 太全局化。它不会随 AstrBot pressure、application-layer pressure、
  tool-promotion pressure 或 growth-review pressure 调整。
- 报告仍使用 `recall_event_candidate`、`meaning_shift_candidate`、`lifecycle`、`preview_only`、
  `policy` 等词，但没有足够的人话解释。
- English internal keys 对审计有用，但在中文报告里仍然有点挤占 founder-facing 阅读空间。

## 候选项预览的问题

当前 candidate preview 是安全的，但太静态。

- growth 问题应该突出 growth review 是 primary candidate，并明确“成长审查不是成长”。
- AstrBot 请求应该突出 adapter / product boundary pressure。
- 应用层请求应该突出 product-layer 和 runtime boundary pressure。
- 工具库请求应该突出 capability-evolution review，并说明“验证成功不等于授权加入工具库”。
- 项目看不清这类输入应该突出 observatory/readability review，而不是把所有 candidate types 显示得同样相关。

这些改进在未来阶段仍应保持 deterministic 和 static。它不需要真实 retrieval、model calls、event writes 或 state reads。

## 建议改的中文名

| 当前显示 | 建议 founder-facing 显示 | 原因 |
|---|---|---|
| 上下文包预览 | 会带哪些背景 | 更像 founder 扫一眼 dry-run 时会理解的说法。 |
| 候选项预览 | 可能进入审查的事项 | 更清楚表达还没有被接受。 |
| 审查队列预览 | 等待人工判断的门 | 比 “queue” 更少抽象感。 |
| 边界监视器 | 禁止事项检查 | 更直接，更安全导向。 |
| 回忆事件候选 | 回忆写入候选 | 更容易看出它连接的是 blocked write policy。 |
| 意义变化候选 | 解释变化候选 | 比 “meaning shift” 更好懂。 |
| Identity Gate | 身份闸门 | 避免中文输出里出现未解释英文。 |
| Memory Lifecycle | 记忆生命周期 | 静态引用标签也应尽量翻译。 |

这些只是 display-name 建议，不重命名 internal keys、schemas、files、RFCs 或 code identifiers。

## 是否建议进入下一步 implementation

**不建议**进入产品层、AstrBot、UI、model-call、真实检索、memory write、recall write、tool execution
或 growth lifecycle implementation。

也不要把 P100 当成真正的 harness runtime。它是一个有用的本地预演面，但仍太静态，还不足以支撑高风险下一步决策。

## P102 推荐方向

推荐 P102：**Harness Readability Improvement / 试验台可读性改进**，仍保持 static 和 read-only。

建议 P102 范围：

- 在 dry-run report 顶部增加一屏能读完的 founder summary；
- 增加 deterministic intent labels，例如 `project_clarity_pressure`、`growth_review_pressure`、
  `adapter_pressure`、`product_layer_pressure`、`tool_promotion_pressure`；
- 增加 `primary_candidate`、`secondary_candidates`、`not_selected_reason`，但不执行 retrieval 或写 state；
- 当输入提到 AstrBot、应用层、工具 promotion、identity growth 或 memory writes 时，让 boundary warning 更显眼；
- 翻译更多中文显示标签，同时保留 English internal keys。

P102 仍应禁止 model calls、真实 retrieval、state reads or writes、memory writes、recall writes、
identity mutation、adapters、UI、product behavior、tool execution 和 automatic next-step execution。

## 边界声明

P101 只是 usability review。它不授权 P102、runtime work、application work、adapter integration、
Companion behavior、model calls、retrieval execution、event writes、memory writes、recall writes、
identity mutation、growth execution、temporal runtime、tool execution、policy execution、
reconstruction reducer execution、event compaction 或 automatic roadmap execution。
