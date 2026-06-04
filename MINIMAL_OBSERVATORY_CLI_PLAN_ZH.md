# 最小观察台 CLI 计划

English version: [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md)

状态：`P95`、`planning`、`RFC-only`、`document-only`、`non-runtime`。

P95 规划未来可能存在的最小只读 Foundation Observatory CLI report。它不实现 CLI、parser、
command、generator、dashboard、Web UI、status API、product surface、runtime monitor 或 executor。

## 问题说明 / Problem Statement

P94 创建了 [FOUNDATION_OBSERVATORY_REPORT_ZH.md](./FOUNDATION_OBSERVATORY_REPORT_ZH.md)，
一份手工维护的 Markdown 地基观察台报告，用于 founder-facing visibility。它有价值，因为它让
创始人或 CTO 不必读完每一份 RFC，也能看见当前 01 Core foundation 状态。

下一步可能需要自动生成：未来某个命令可以读取 foundation documents，并稳定地产生同类 sections。

但这不应该变成 Web UI、dashboard runtime、product UI 或 observability executor。最小 CLI
只服务于 founder / CTO 的可见性，范围限于 documents、readiness、boundaries、risks 和 next-step
recommendations。

## 候选 CLI / Proposed CLI

候选命令：

```text
foundation-observatory-report
```

可选子视图：

| Subview | Purpose | Boundary |
|---|---|---|
| `phase-map-view` | 展示 phase index 和 main-line grouping。 | 只读取 phase docs；不创建 phases。 |
| `readiness-matrix-view` | 展示 module readiness categories 和 next actions。 | 报告 readiness；不授权 implementation。 |
| `boundary-status-view` | 展示 disabled、forbidden、RFC-only 和 future boundaries。 | 报告 boundaries；不执行 policy。 |
| `risk-heatmap-view` | 展示 foundation risks 集中区域。 | 报告 risk；不执行 mitigation。 |
| `next-step-recommendation-view` | 展示排序后的 future directions。 | 建议 review choices；不启动 P96 或任何 phase。 |

未来默认输出应是一份完整 Markdown report，而不是 interactive dashboard。

## 输入 / Inputs

未来 CLI input 应限制为已有 documents 和静态 state references。它不得调用 adapters、remote
services、model APIs、live chat surfaces 或 mutable runtime commands。

| Input | Use | Boundary |
|---|---|---|
| [PHASE_INDEX.md](./PHASE_INDEX.md) / [ZH](./PHASE_INDEX_ZH.md) | Phase map 和 current phase coverage。 | Read-only。 |
| [CONCEPT_MAP.md](./CONCEPT_MAP.md) / [ZH](./CONCEPT_MAP_ZH.md) | Concept relationships 和 ownership。 | Read-only。 |
| [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) / [ZH](./FOUNDATION_STATUS_ZH.md) | Stable、exploratory、missing 和 pushed-back foundation state。 | Read-only。 |
| [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) / [ZH](./OPEN_QUESTIONS_ZH.md) | Open questions、blocked work 和 future contracts。 | Read-only。 |
| [RISK_REGISTER.md](./RISK_REGISTER.md) / [ZH](./RISK_REGISTER_ZH.md) | Risk categories 和 mitigations。 | Read-only。 |
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) / [ZH](./ARCHITECTURE_BOUNDARIES_ZH.md) | Forbidden boundaries 和 layer ownership。 | Read-only。 |
| [RFC_INDEX.md](./RFC_INDEX.md) / [ZH](./RFC_INDEX_ZH.md) | Indexed RFC、policy、report 和 review artifacts。 | Read-only。 |
| [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) / [ZH](./VISUAL_NAMING_GUIDE_ZH.md) | 中文显示名和 English `internal_key` 映射。 | Read-only。 |
| [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) / [ZH](./FOUNDATION_OBSERVATORY_REPORT_ZH.md) | 当前手工 report template 和 baseline。 | Read-only。 |

任何未来实现若要读取 static local state summaries，必须先说明读取哪些文件，并证明不发生写入。

## 输出 / Outputs

未来 CLI output 应是 deterministic Markdown 或 JSON-like structured report data，包含：

| Output Section | Meaning | Boundary |
|---|---|---|
| `founder_snapshot` | 当前 01 Core state 的 founder / CTO 简短摘要。 | Summary，不是 release claim。 |
| `main_axes_map` | continuity、growth、temporal、capability、interaction 和 observability axes。 | Report grouping，不是 runtime architecture。 |
| `readiness_matrix` | Module readiness 和 next action table。 | Readiness 不是 authorization。 |
| `boundary_status` | Disabled、forbidden、RFC-only 和 future boundaries。 | Boundary report 不是 enforcement。 |
| `risk_heatmap` | 高风险区域和缓解措施。 | Risk report 不是 mitigation execution。 |
| `next_step_recommendations` | 排序后的 future options。 | Recommendation 不是 automatic phase creation。 |
| `what_not_to_build_yet` | 明确 blocked work list。 | Block list 不是 runtime guard。 |

## 就绪度类别 / Readiness Categories

未来 CLI 必须沿用这些类别：

| Category | Meaning |
|---|---|
| `implemented` | 当前已有 prototype 或 document-backed mechanism。 |
| `report_only` | 只在 reports 或 reviews 中可见，不是 implemented mechanism。 |
| `rfc_only` | 只作为 RFC、policy 或 planning vocabulary 存在。 |
| `evaluation_only` | 只作为 evaluation scenarios 或 signals 设计，不是 runtime truth。 |
| `future_direction` | 有价值的未来方向，但缺 contracts。 |
| `blocked` | 在 future approval 和 gates 存在前明确 forbidden。 |
| `dangerous_if_early` | 如果过早建设，很容易造成 boundary drift。 |

不确定时，未来 CLI 应选择更低成熟度的类别。

## 边界状态 / Boundary Status

未来 CLI 至少必须报告：

| Boundary | Future CLI Status Vocabulary | Required Interpretation |
|---|---|---|
| identity mutation | `blocked` / `forbidden` | 不自动改变 Identity Core。 |
| memory rewrite | `blocked` / `forbidden` | 不 rewrite memories 来模拟 growth 或 cleanup。 |
| recall event write | `rfc_only` / `disabled` | ordinary recall 不是 event write。 |
| growth engine | `blocked` / `forbidden` | growth candidates 不能自动 promote。 |
| temporal runtime | `future_direction` / `disabled` | time 仍是 review evidence，不是 active runtime。 |
| CTM runtime | `blocked` / `forbidden` | CTM 是 inspiration，不是 implementation。 |
| tool execution | `blocked` / `forbidden` | tool candidates 不是 executable tools。 |
| tool promotion | `blocked` / `forbidden` | verification 不等于 promotion。 |
| policy executor | `blocked` / `forbidden` | policy language 不能执行 decisions。 |
| companion layer | `future_direction` / `blocked` | companion behavior 仍留在 foundation work 外。 |
| UI / AstrBot / adapter | `future_direction` / `blocked` | platform surfaces 不能拥有 identity。 |
| reconstruction reducer | `rfc_only` / `disabled` | reducer contract 不是 reducer execution。 |
| event compaction | `blocked` / `forbidden` | event history 必须保持 auditable。 |

## 非目标 / Non-Goals

P95 和任何 minimal observatory CLI plan 都不包括：

- Web UI；
- dashboard runtime；
- product UI；
- companion layer；
- automatic roadmap execution；
- automatic next phase creation；
- automatic status mutation；
- identity mutation；
- memory rewrite；
- recall event write；
- growth promotion 或 growth engine；
- Temporal Awareness runtime；
- CTM runtime；
- tool execution；
- tool promotion；
- policy executor；
- adapter integration；
- reconstruction reducer execution；
- event compaction。

## 实现边界 / Implementation Boundary

P95 不实现 CLI。

P96 只有在 founder explicit approval 后，才可以考虑 Minimal Observatory CLI Implementation。
最小可接受 implementation 必须是 read-only：

- 读取 Markdown 和已批准的 static local state summaries；
- 输出 Markdown 或 JSON-like report；
- 避免 remote calls、adapters、model APIs、network access 和 live runtime mutation；
- 证明不会写入 identity、memory、recall events、growth candidates、tools、policy state、
  reducers 或 compacted event history。

如果任何未来 implementation 需要 writes、network、adapters、model calls 或 runtime state
mutation，它就不再是 minimal observatory CLI。

## 风险 / Risks

| Risk | Level | Why It Matters | Mitigation |
|---|---|---|---|
| observability becoming product UI | High | founder report 容易滑向 dashboard/product work。 | P95 保持 RFC-only；任何 P96 candidate 都必须 read-only。 |
| report becoming decision executor | High | 排序建议可能被误当作 commands。 | Recommendation output 不得创建 phases 或 tasks。 |
| stale document inputs | Medium | generated reports 可能重复过期 source documents。 | future design 应显示 source file timestamps 或 phase coverage。 |
| false readiness signal | High | 干净表格会让 RFC-only concepts 看起来很安全。 | 使用保守 readiness categories 和 blocked labels。 |
| overconfidence from dashboard | High | visual summaries 会隐藏 uncertainty。 | 每个 view 都保留 risk 和 missing-contract fields。 |
| hiding complexity behind simplified labels | Medium | founder-facing names 可能压平技术细节。 | 保留 English `internal_key` 和 source links。 |

## P96 候选 / P96 Candidate

P95 不执行的可能 P96 方向：

1. Minimal Observatory CLI Implementation。
2. Readiness Matrix Static Generator。
3. Boundary Status Static Generator。
4. Founder Snapshot Generator。

推荐顺序：只有在 founder 明确批准从 plan 转入 implementation 时，才考虑 read-only Minimal
Observatory CLI Implementation。否则先暂停，做 founder / CTO review。

## 非执行声明 / Non-Execution Statement

本计划是 RFC-only planning artifact。它不新增 commands、modules、schemas、tests、parsers、
generated files、dashboards、Web UI、adapters、runtime behavior、policy execution、identity
mutation、memory rewrite、recall writes、growth execution、tool execution、reconstruction
reducers、event compaction 或 P96 implementation。
