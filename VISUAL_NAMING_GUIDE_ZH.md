# 视觉命名指南

English version: [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md)

状态：`P93`、`document-only`、`planning`、`non-runtime`。

P93 为未来的 Foundation Observatory、Founder Dashboard、Readiness Matrix 和
Concept Graph 设计 founder-facing vocabulary。本文件不实现这些视图。它的目标是让未来
视觉层对项目创始人更直观，同时保留论文、RFC、代码和审计所需的英文 internal key。

## 目标

未来 foundation 视图应该像仪表盘，而不是论文目录。Founder-facing 层应该直接回答：

```text
这是什么？
它是干什么的？
它已经实现了吗，还是报告层、RFC 层、未来方向、危险过早？
它有什么风险？
下一步应该做什么？
```

英文术语保留为 `internal_key`。中文显示名是展示给 founder 的第一标题。

## 命名原则

- founder-facing 视图优先显示中文名。
- 英文名保留为稳定的 `internal_key`。
- 显示名必须说明这个概念是干什么的，而不只是显得抽象。
- 避免论文腔、过度抽象和流行词堆叠。
- 优先使用 `状态库`、`任务中心`、`边界状态` 这类清楚的名词。
- 不把 RFC-only 概念显示成已实现能力。
- 不把 candidate 显示成 promoted result。
- 不把 review object 显示成 execution。
- 成熟度不确定时，显示更保守的状态。
- 中英文必须共用一张映射表，避免 dashboard 语言与 RFC、paper、code 语言割裂。

## 映射表

| internal_key | 中文显示名 | 它是干什么的 | 视觉层状态 | 边界 |
|---|---|---|---|---|
| Identity Core | 身份核心 | 保护不应被随意改变的稳定身份锚点。 | 报告层 | 不允许自动身份修改。 |
| Identity Gate | 身份闸门 | 在任何 identity-facing 变化前审查高风险身份压力。 | 报告层 | 是审查闸门，不是身份更新。 |
| State Transfer | 状态传递 | 通过状态穿过时间来保持连续性，而不是只检索记忆。 | 报告层 | 是基础命题，不是独立 runtime feature。 |
| StateStore | 状态库 | 持久保存 state、episodes、dreams 和 imports 等本地状态。 | 已实现 | 存储不拥有身份。 |
| Event Log | 事件日志 | 记录可审计的状态转移，让后续 review 能追踪发生了什么。 | 已实现 | 记录日志不是执行 reconstruction。 |
| Replay | 回放检查 | 检查状态转移是否可以被 replay 或 projection，以支持审计。 | 报告层 | 回放检查不是重建状态。 |
| Reconstruction | 状态重建 | 未来从证据重建或解释主体历史的能力方向。 | RFC 层 | reducer execution 仍然 blocked。 |
| Claim Graph | 信念证据图 | 跟踪 claims、evidence、conflict 和 belief status。 | 报告层 | 不吞掉所有 meaning shift。 |
| Task Hub | 任务中心 | 跟踪 durable tasks、procedures 和 work state。 | 报告层 | 不替代 governance review。 |
| Dream Engine | 离线整理器 | 把 episodes 和 imported memory 整理成 semantic material。 | 已实现 | Dream proposes; review decides。 |
| Memory Lifecycle | 记忆生命周期 | 解释 memory 如何被暂存、保留、整理或遗忘。 | 已实现 | lifecycle status 不是 memory rewrite。 |
| Stateful Memory | 状态化记忆 | 把 memory meaning 理解为 event、encoding state、recall state 和 meaning shift 的组合。 | RFC 层 | 是语义，不是新 memory store。 |
| Meaning Shift | 意义变化 | 描述一个记忆在后续 recall state 下意义如何改变。 | RFC 层 | 不等于 claim revision。 |
| Growth Candidate Review | 成长候选审查 | 在任何 growth claim 前审查可能带来意义变化的状态转移。 | RFC 层 | candidate 不是 promoted growth。 |
| Governance Surface | 跨层审查区 | 承载引用 memory、claims、tasks、identity 和 evidence 的 review objects。 | 报告层 | 是 review surface，不是 policy executor。 |
| Temporal Awareness | 时间感知 | 研究 elapsed time 如何成为 subject-state transition 的一部分。 | RFC 层 | 不实现 temporal runtime 或 temporal event writes。 |
| Temporal Coherence | 时间一致性 | 检查 later interpretation 是否仍能与 earlier state 和 evidence 相容。 | RFC 层 | 是 evaluation signal，不是真理或 identity update。 |
| Deliberation Tick | 思考刻度 | 命名未来可能用于 risk-calibrated deliberation 的 review steps。 | RFC 层 | 不是 thought-loop execution。 |
| Thought Trace | 思考痕迹 | 命名未来可能用于摘要 review-state movement 的 review artifact。 | RFC 层 | 不是 hidden chain-of-thought 或 consciousness proof。 |
| Capability Evolution | 能力进化 | 审查 tools、skills 和 procedures 是否有可验证的持续改进。 | RFC 层 | 能力改进不是 identity growth。 |
| Tool-First Self-Evolution | 工具优先自进化 | 把可验证的工具和流程改进放在主体演化之前。 | RFC 层 | 不批准 tool execution 或 promotion。 |
| Tool Candidate | 工具候选 | 提出一个未来可能有用、但需要 review 的工具。 | RFC 层 | candidate 不是 trusted tool。 |
| Procedure Candidate | 流程候选 | 提出一个可重复 workflow，等待 review。 | RFC 层 | candidate 不是 procedural memory。 |
| Skill Memory | 技能记忆 | 未来经过 review 的可复用能力知识。 | 未来方向 | 不是 policy execution 或 automatic invocation。 |
| Procedural Memory | 程序性记忆 | 关于已审查 procedures 和 workflows 的 durable knowledge。 | 报告层 | 不是 automatic tool runner。 |
| Cautionary Memory | 警示记忆 | 保存 failures 或 unsafe patterns 产生的警示。 | 报告层 | warning 不是 enforcement code。 |
| Thin Interaction Harness | 轻量交互试验台 | 未来本地预览 intake、context、review queue 和 boundary flags 的试验面。 | RFC 层 | 不实现 harness runtime、CLI、UI 或 adapter work。 |
| Context Package Preview | 上下文包预览 | 解释哪些 context references 会被选择或省略。 | RFC 层 | 不是 retrieval execution 或 prompt construction。 |
| Review Queue Preview | 审查队列预览 | 展示 candidate review pressure、ordering signals 和 blocked boundaries。 | RFC 层 | 不是 queue execution 或 approval。 |
| Session Resume Scenario | 会话恢复场景 | 模拟暂停会话如何恢复 references 和 context。 | 报告层 | 不是 resume runtime 或 temporal event write。 |
| Core Boundary Monitor | 核心边界监视器 | 未来解释哪些 action 被 blocked、deferred 或需要 review 的视图。 | 未来方向 | 不是 runtime enforcement。 |
| Foundation Observatory | 地基观察台 | 未来面向 founder 展示 foundation status、risks、concepts 和 gaps 的视图。 | 未来方向 | P93 不实现 dashboard runtime。 |
| Readiness Matrix | 就绪度矩阵 | 展示一个概念是否 ready、blocked，或还缺哪些 gates。 | 报告层 | readiness 不是 authorization。 |
| Risk Heatmap | 风险热力图 | 展示 concept、runtime、identity、memory 或 tool risk 集中在哪里。 | 未来方向 | risk view 不是 governance execution。 |
| Open Questions | 未决问题 | 列出仍未解决的 foundation questions 及其当前 routing。 | 报告层 | open question 不是 approval。 |
| Boundary Status | 边界状态 | 展示一个概念是 allowed、blocked、RFC-only 还是 future-only。 | 报告层 | status label 不是 enforcement。 |

## 展示卡片格式

未来每个视觉层概念卡片至少包含：

| 字段 | 要求 |
|---|---|
| 中文显示名 | 第一个可见标题，面向 founder。 |
| English internal_key | RFC、paper、code 和 audit 使用的稳定术语。 |
| 一句话解释 | 用朴素语言回答“它是干什么的？” |
| 当前状态 | 使用 `已实现`、`报告层`、`RFC 层`、`未来方向`、`危险过早` 之一。 |
| 风险等级 | 低、中、高或 blocked，并附一句原因。 |
| 下一步建议 | 最安全的下一步，通常是 review、document、defer 或 block。 |

示例卡片：

| 字段 | 示例 |
|---|---|
| 中文显示名 | 成长候选审查 |
| English internal_key | Growth Candidate Review |
| 一句话解释 | 在任何 growth claim 前审查可能带来意义变化的状态转移。 |
| 当前状态 | RFC 层 |
| 风险等级 | 如果被误当成自动成长，则为高风险。 |
| 下一步建议 | 在 promotion gates 和 evidence contracts 存在前保持 review-only。 |

## Paper Naming Mode

英文术语可继续用于：

- papers；
- RFCs；
- whitepapers；
- code identifiers；
- schemas；
- audits；
- cross-project comparison。

中文术语应优先用于：

- founder-facing dashboard summaries；
- future Foundation Observatory views；
- README summaries；
- readiness views；
- risk views；
- concept graph labels。

两种模式必须保持映射。中文显示名可以比英文术语更直白，但不能改变概念边界。英文
`internal_key` 可以保持精确，但不能强迫 founder-facing surface 看起来像论文目录。

## 边界规则

P93 不实现：

- Web UI；
- dashboard runtime；
- Foundation Observatory runtime；
- product layer；
- observability CLI；
- runtime changes；
- new features；
- Temporal Awareness runtime；
- CTM runtime；
- thought loop execution；
- tool execution；
- tool promotion；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- recall event writes；
- reconstruction reducer execution；
- companion、relationship、AstrBot、adapter、cloud 或 product integration；
- P94。

## 非执行声明

本指南是 future visual surfaces 的命名合同。它不是 UI specification、implementation plan、
dashboard schema、CLI contract、runtime report、status API，也不是建设 Foundation Observatory
的授权。
