# 地基观察台可用性审查

English version: [OBSERVATORY_USABILITY_REVIEW.md](./OBSERVATORY_USABILITY_REVIEW.md)

状态：`review-only`、`document-only`、`non-runtime`。

P97 审查 P96 的 `foundation-observatory-report` command 是否真的能让项目创始人看懂
01 Core 当前状态。它不改变 runtime behavior、Identity Core、memory、recall policy、
harness implementation、UI、AstrBot、adapters 或 next-step execution。

## 已审查命令

本次审查运行了：

- `python3 -m one_core.cli foundation-observatory-report`
- `python3 -m one_core.cli foundation-observatory-report --lang zh`
- `python3 -m one_core.cli foundation-observatory-report --format json`
- `python3 -m one_core.cli foundation-observatory-report --format json --lang zh`
- `python3 -m one_core.cli --state-dir /tmp/.../state foundation-observatory-report --output /tmp/.../report.md`

临时 `--output` 检查成功，并且没有创建临时 state 目录。

## 可读性评分

整体 founder-facing 可读性：**7 / 10**。

| 区域 | 分数 | 原因 |
|---|---:|---|
| 创始人快照 | 8 | 能快速说明 01 Core 是连续性地基，不是产品或执行器。 |
| 主轴地图 | 7 | 分组有用，但多条轴仍依赖抽象 English internal keys。 |
| 就绪度矩阵 | 7 | status 可见，但 `rfc_only`、`report_only` 等状态需要中文解释。 |
| 边界状态 | 8 | `enabled: false` 让 forbidden / disabled 边界比较容易扫描。 |
| 风险热力图 | 5 | 能列出风险，但 mitigation 仍偏泛，指导性不够。 |
| 下一步建议 | 7 | 保守且不自动决策，但还应更强地区分“先审查”和“开始建设”。 |

## 好用的部分

- 报告明确说明 P96 是 read-only，不修改 state。
- `implemented`、`rfc_only`、`evaluation_only`、`future_direction`、`blocked`
  对技术读者已经足够可见。
- 边界表是目前最强的部分：identity mutation、memory rewrite、growth engine、
  temporal runtime、tool execution、policy executor、event compaction 等 forbidden work
  很容易扫到。
- 中文报告已经对关键概念使用中文显示名，同时保留 English `internal_key`。
- JSON 输出对未来 static reporting 有结构价值，但它应继续只是 report artifact，不是 execution
  contract。

## 仍然抽象的部分

- 报告仍假设 founder 理解 `rfc_only`、`report_only`、`evaluation_only`、`symbolic`、
  `review evidence`、`reconstruction reducer`、`meaning shift`、`policy executor` 等术语。
- 主轴地图概念上正确，但仍像 research index。它还没有用足够浅显的语言回答：“这周我应该关心什么？”
- 就绪度矩阵说明了每项是什么状态，但没有说明为什么这个状态重要。
- 风险热力图缺少具体症状。例如“概念膨胀”是真的风险，但报告应说明什么现象代表它正在发生。
- 部分中文解释仍混入较多英文抽象词。作为 internal key 可以保留英文，但 founder-facing explanation
  应更浅显。

## 建议改的中文名

| 当前名称 | 建议显示名 | 原因 |
|---|---|---|
| 状态化记忆 | 带状态的记忆 | 更具体，论文感更少。 |
| 成长候选审查 | 成长提案审查 | “提案”更清楚地表示它不是已经完成的成长。 |
| 时间一致性 | 时间线一致性检查 | 听起来像可评估检查，而不是心理属性。 |
| 能力进化 | 能力改进边界 | 减少把能力改进误解成主体成长的风险。 |
| 工具优先自进化 | 先改工具，不改身份 | 更适合 founder-facing，边界更直观。 |
| 轻量交互试验台 | 本地交互预演 | 比 “harness” 更容易理解。 |
| 信念证据图 | 说法证据图 | 对非研究阅读更直观。 |
| Governance Surface | 跨层审查区 | 更贴近实际职责。 |

这些只是 display-name 建议，不重命名 internal keys、schemas、files、RFCs 或 code identifiers。

## 需要更浅显解释的模块

- Identity Core：解释成“01 关于自己是谁的受保护答案”。
- Event Log：解释成“重要状态变化的账本”。
- Replay：解释成“检查历史能不能再走一遍”。
- Reconstruction：解释成“用证据重建过去状态，但现在还不执行”。
- Claim Graph：解释成“哪些说法有证据、互相冲突、仍未解决”。
- Stateful Memory：解释成“记忆加上形成和被回忆时的状态条件”。
- Temporal Coherence：解释成“一个变化是否仍符合时间线”。
- Capability Evolution：解释成“工具和流程改进，但不能改变身份”。
- Thin Interaction Harness：解释成“未来本地预演面，不是聊天产品”。

## 风险展示不够清楚之处

进入任何 harness work 前，risk heatmap 应更可操作：

- 增加 `symptom` 字段：如果这个风险正在发生，founder 会看到什么现象？
- 增加 `current_guardrail` 字段：当前靠什么挡住这个风险？
- 增加 `next_manual_check` 字段：下一步人工应该检查什么？
- 中文报告里的 mitigation 需要翻译。
- 按 identity、memory、temporal、tool、observability、product 分层展示风险。
- 避免只写 “use glossary” 这类泛化 mitigation，除非同时给出具体动作。

## 是否建议进入 minimal CLI harness

**不建议现在进入 minimal CLI harness implementation。**

P96 observatory 作为静态状态报告已经有用，但作为交互工作前的 foundation visibility layer 还不够强。
报告应先让 founder 不依赖 P0-P96 术语背景，也能看懂当前状态、风险和 blocked boundaries。

## 进入 harness 前还需要怎么改 observatory

建议先做 observatory-only 改进：

- 给 readiness status 增加中文显示标签：
  `已实现`、`报告层`、`RFC 层`、`评估层`、`未来方向`、`已阻塞`、`过早危险`。
- 给 readiness matrix 每一行增加一句 “为什么这个状态重要”。
- 给 risk heatmap 增加 `symptom`、`guardrail`、`manual_check` 字段。
- 增加一个非常短的 “current safe next step” 区域，明确先 review。
- 增加一个可以一屏读完的 founder summary。
- 所有改进都继续保持 static 和 read-only。

## 边界声明

P97 建议先提升 observatory 清晰度，再讨论任何 minimal CLI harness。它不授权 harness
implementation、product UI、AstrBot integration、companion behavior、policy execution、
tool execution、identity mutation、memory rewrite、recall event writes、growth execution、
Temporal Awareness runtime、reconstruction reducer execution、event compaction 或 automatic
roadmap execution。
