# 地基观察台报告

English version: [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md)

状态：`P94`、`document/report-only`、`founder-facing`、`non-runtime`。

这是第一版 Markdown 地基观察台报告。它遵守
[VISUAL_NAMING_GUIDE_ZH.md](./VISUAL_NAMING_GUIDE_ZH.md)：中文显示名优先，English
`internal_key` 保持可见，不把 RFC-only 概念显示成已实现，不把 review object 显示成
execution，也不把 candidate 显示成 promoted result。

P94 不实现 dashboard、CLI、Web UI、product layer、status API、runtime report generator、
adapter integration 或 observability runtime。

## 创始人快照 / Founder Snapshot

今天的 01 Core 是 Persistent Intelligence 的连续性地基。它不是产品、伴侣应用、聊天皮肤、
自动工具运行器，也不是会自动修改身份的成长引擎。

现在已经存在：

- 一个本地 prototype，包含 `StateStore`、event records、memory import、Dream consolidation、
  HTTP/API references 和 adapter references 等 durable state 参考；
- 一个更大的 foundation layer，覆盖 identity、state transfer、event sourcing、replay、
  reconstruction readiness、stateful memory、growth review、temporal concepts、capability
  boundaries 和 visual naming；
- 明确 blocked 的边界：identity mutation、memory rewrite、recall writes、growth execution、
  temporal runtime、CTM runtime、tool autonomy、companion behavior、product UI、adapters、
  reducers 和 event compaction。

当前最重要的状态：

```text
01 Core 已经有受保护的地基和可见的边界地图。
它还不是应用层。
下一步最有价值的是选择要观察什么、规划什么，而不是直接增加能力。
```

观察层之所以需要，是因为现在 foundation 已经有许多概念和报告。创始人不应该必须读完每份
RFC，才能知道什么已实现、什么只是报告层、什么只是 RFC 层、什么是未来方向、什么必须继续
blocked。

## 主轴地图 / Main Axes Map

| 中文显示名 | internal_key | 一句话解释 | 当前状态 | 风险等级 | 下一步建议 |
|---|---|---|---|---|---|
| 连续性轴 | Identity / State / Event / Reconstruction | 用身份锚点、持久状态、事件证据、回放检查和未来重建来保护连续性。 | 报告层 | 中：reconstruction 语言容易被误读成 rebuild execution。 | 保持 audit 和 replay evidence 可见，不运行 reducers。 |
| 成长轴 | Stateful Memory / Meaning Shift / Growth Candidate Review | 解释 memory meaning 如何变化，以及可能的 growth 为什么必须保持 review-only。 | RFC 层 | 高：candidate 容易被误读成 actual growth。 | 保持 growth review 与 promotion、identity mutation 分离。 |
| 时间轴 | Temporal Awareness / CTM-inspired Temporal Dynamics | 研究 elapsed time 和 temporal coherence 如何成为未来 review evidence。 | RFC 层 | 高：temporal language 容易制造 cognition 或 runtime 过度声明。 | 保持 deterministic evaluation planning，不进入 temporal runtime。 |
| 能力轴 | Tool-First Self-Evolution / Capability Evolution | 区分可验证能力改进、主体成长和身份变化。 | RFC 层 | 高：tool verification 容易被误读成 authorization。 | 在任何 tool execution 前定义 evidence 和 review policy。 |
| 交互试验轴 | Thin Interaction Harness | 定义未来 preview-only 的本地交互表面，用于 intake、context、queue 和 boundary checks。 | RFC 层 | 中：harness planning 容易滑向 product 或 adapter work。 | 在 explicit approval 前保持 fixture-first 和 no-write。 |
| 观察层 | Foundation Observatory | 给创始人一个可读视图，查看状态、就绪度、风险、未决问题和 blocked boundaries。 | 报告层 | 中：observability 容易过早变成 product UI。 | 除非未来阶段批准 CLI 或 UI plan，否则保持 Markdown/report-only。 |

## 就绪度矩阵 / Readiness Matrix

| 中文显示名 | internal_key | status | layer | risk | next action |
|---|---|---|---|---|---|
| 身份核心 | Identity Core | 报告层 | report-only | 高：如果被当成可自动修改的 identity state。 | 保持 protected；任何 future identity-facing change 都需要 Identity Gate。 |
| 状态传递 | State Transfer | 报告层 | report-only | 中：如果被降级成 retrieval。 | 保持为 continuity 的核心命题。 |
| 事件日志 | Event Log | 已实现 | implemented | 中：如果日志被当成完整 reconstruction evidence。 | 保持 event evidence 可审计；不 compact events。 |
| 回放检查 | Replay | 报告层 | report-only | 中：如果 check 被误读为 rebuild。 | 保持 replay/readiness reports 与 reducer execution 分离。 |
| 状态重建 | Reconstruction | RFC 层 | RFC-only | 高：如果 reducer execution 先于 contracts。 | 先完成 reducer contract、payload 和 validation policy。 |
| 信念证据图 | Claim Graph | 报告层 | report-only | 中：如果它吞掉所有 meaning shift。 | 保持 claim revision 与 memory meaning shift 分离。 |
| 任务中心 | Task Hub | 报告层 | report-only | 中：如果它吞掉所有 governance review。 | 保持 task tracking 与 cross-layer review objects 分离。 |
| 状态化记忆 | Stateful Memory | RFC 层 | RFC-only | 高：如果 semantics 变成 memory rewrite。 | 保持 encoding 和 recall policy document-only。 |
| 成长候选审查 | Growth Candidate Review | RFC 层 | RFC-only | 高：如果 candidate 被显示为 promoted growth。 | 在 lifecycle 和 promotion gates 存在前保持 review-only。 |
| 时间感知 | Temporal Awareness | RFC 层 | RFC-only | 高：如果 elapsed time 变成 runtime authority。 | 作为 future review evidence 保留，不执行 temporal events。 |
| 时间一致性 | Temporal Coherence | RFC 层 | RFC-only | 高：如果 score 变成 truth 或 identity proof。 | 保持 deterministic evaluation plans symbolic 和 review-only。 |
| 能力进化 | Capability Evolution | RFC 层 | RFC-only | 高：如果 tool improvement 被当成 subject growth。 | runtime 前先定义 evidence 和 authorization boundaries。 |
| 工具优先自进化 | Tool-First Self-Evolution | RFC 层 | RFC-only | 高：如果 tool verification 被当成 execution approval。 | 区分 candidate、verification、authorization 和 promotion。 |
| 轻量交互试验台 | Thin Interaction Harness | RFC 层 | RFC-only | 中：如果 preview 变成 product 或 adapter integration。 | 任何 CLI plan 前先要求 fixture 和 output contracts。 |
| 地基观察台 | Foundation Observatory | 报告层 | report-only | 中：如果 Markdown observability 变成 dashboard runtime。 | P94 保持 report-only；P95 方向需要明确选择。 |

## 边界状态 / Boundary Status

| Boundary | Current State | Meaning | Allowed Next Action |
|---|---|---|---|
| identity mutation | forbidden / disabled | Identity Core 不能自动改变。 | 只能做创始人批准的 review policy。 |
| memory rewrite | forbidden / disabled | 不能用 rewrite 作为 growth 或 cleanup 的捷径。 | 只做 policy 和 review evidence 文档。 |
| recall event write | RFC-only / disabled | ordinary recall 不是 event write。 | 继续 recall write policy design。 |
| growth engine | forbidden / disabled | growth candidates 不能自动 promote 自己。 | 保持 candidate review 和 lifecycle 为文档层。 |
| temporal runtime | future / disabled | elapsed time 还不是 active runtime state。 | 继续 Temporal Awareness evaluation planning。 |
| CTM runtime | forbidden / disabled | CTM 是外部启发，不是今天的实现路径。 | 保持 symbolic vocabulary 和 anti-pseudocognition boundaries。 |
| tool execution | forbidden / disabled | tool candidates 不是 trusted executable tools。 | 先定义 verification evidence 和 authorization gates。 |
| tool promotion | forbidden / disabled | successful verification 不等于 promote tool。 | 保持 human/founder review 为 promotion gate。 |
| policy executor | forbidden / disabled | policy language 不能执行决策。 | 保持 governance surfaces review-only。 |
| companion layer | future / forbidden now | relationship 和 companion behavior 不属于 foundation loop。 | 等 core continuity 可 review 后再考虑。 |
| UI / AstrBot / adapter | future / forbidden now | platform entrances 不能拥有 identity，也不能把当前 foundation work 推入 product。 | core contracts 被批准前继续后推 integration。 |
| reconstruction reducer | RFC-only / disabled | reducer contract 是 future planning，不是 execution。 | 先完成 contract、payload/diff 和 validation policy。 |
| event compaction | forbidden / disabled | event history 必须保持可审计。 | retention review 与 compaction 继续分离。 |

## 风险热力图 / Risk Heatmap

| 风险区域 | 风险等级 | 当前缓解措施 | 下一步建议 |
|---|---|---|---|
| 概念膨胀 | 高 | Phase index、concept map、glossary、overlap review、visual naming guide。 | 增加新概念前继续合并或路由旧概念。 |
| review 层套 review 层 | 中 | Governance Surface boundary 和 review-only language。 | 优先减少 review objects，并明确 owner。 |
| 过早 runtime | 高 | README、open questions、RFCs 和本报告都有 runtime-blocked lists。 | implementation phase 前必须有 explicit founder approval。 |
| companion 污染 | 高 | companion、relationship memory、social layer 和 product work 继续 blocked。 | foundation work 中继续排除 social/relationship concepts。 |
| tool autonomy creep | 高 | Capability boundary 区分 candidate、verification、authorization 和 promotion。 | 任何 tool runtime 前先定义 evidence models。 |
| temporal overreach | 高 | CTM 和 Temporal Awareness 保持 symbolic、RFC-only、anti-pseudocognition bounded。 | 不存储 thought loops、temporal events 或 runtime ticks。 |
| identity drift | 高 | Identity Core、Identity Gate 和 drift/collapse boundaries 保持可见。 | identity-facing changes 继续 high-gated 和 human-reviewed。 |
| observability becoming product UI | 中 | P94 是 Markdown report-only，没有 dashboard runtime。 | 如果继续推进，先写 CLI/report boundary，再考虑 UI。 |
| fake cognition vocabulary | 高 | Non-claims、CTM boundaries、thought trace policy 和 temporal coherence evaluation limits。 | 继续使用 symbolic language，避免 consciousness claims。 |

## 下一步建议 / Next-Step Recommendation

推荐优先级：

| Priority | Candidate | Recommendation | Why |
|---|---|---|---|
| 1 | E. Pause for founder / CTO review | 最推荐。 | P94 已让 foundation 可读；创始人应决定下一步是观察、规划 CLI，还是回到 capability policy。 |
| 2 | B. P95 Minimal Observatory CLI RFC | 如果继续 document-only，这是最稳的下一步。 | 它可以定义 CLI/report boundary，同时不实现 CLI 或 UI。 |
| 3 | A. P95 Founder Dashboard CLI Plan | 在 RFC boundary 之后有价值。 | 它可以规划 founder-facing command output，但应等待 minimal boundary。 |
| 4 | D. P95 Tool Verification Evidence Model | 如果选择 capability evolution 路线，这是合理下一步。 | 它推进 P91-P92，同时不执行工具、不 promote 工具。 |
| 5 | C. P95 Minimal CLI Harness Implementation Plan | 风险更高，应后推。 | 它更接近 implementation pressure，需要先有 fixture/output/no-write contracts。 |

本报告不执行任何 P95 方向。下一阶段需要创始人明确选择。

## 现在不要建设什么 / What Not To Build Yet

现在不要建设：

- Web UI；
- Companion product；
- AstrBot integration；
- automatic growth；
- Temporal Awareness runtime；
- CTM runtime；
- tool execution runtime；
- automatic tool promotion；
- policy executor；
- reconstruction reducer execution；
- event compaction；
- dashboard runtime；
- observability CLI；
- status API；
- product layer。

## 非执行声明

本报告是 Markdown observation layer。它读取并组织已有 foundation documents 和 phase boundaries
中的状态。它不创建 runtime behavior、CLI commands、Web UI、status endpoints、dashboards、
adapter behavior、identity updates、memory rewrites、recall writes、tool execution、growth
promotion、temporal events、CTM execution、reconstruction reducers 或 event compaction。
