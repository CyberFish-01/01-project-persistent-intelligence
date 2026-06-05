# Baseline Tagging Founder Review / 基线 Tag 创始人审查

English version: [BASELINE_TAGGING_FOUNDER_REVIEW.md](./BASELINE_TAGGING_FOUNDER_REVIEW.md)

状态：`P157`、`founder-review`、`planning-only`、`no-tag-created`、
`no-branch-created`、`no-push`、`no-rebuild-started`。

P157 审查 P156 baseline tag 和 branch creation plan，供 founder 做决定。它不创建 tags，不创建
branches，不 push tags，不 push main，不启动 local rebuild，不读取 old 01，不连接 adapters，不写
formal state 或 memory，也不修改 Identity Core。

## Current Review State / 当前审查状态

| Field | Value |
|---|---|
| current_branch_at_review_start | `main` |
| current_HEAD_at_review_start | `6e7639a Add baseline tagging plan` |
| worktree_clean_at_review_start | `true` |
| git_tag_created | `false` |
| git_branch_created | `false` |
| rebuild_started | `false` |

## Tag Review / Tag 审查

| Tag | Candidate Commit | Reason | Confidence | needs_founder_confirmation | Risk | Recommendation |
|---|---|---|---|---|---|---|
| `core-v0-baseline` | `5e5fe21 Add adapter event deduplication` | `2e2ae68 Define project foundation invariants` 前最后一个 early runtime/adapter-hardening commit；如果 founder 希望用 handoff-era protocol 作为锚点，替代候选是 `83bede1 Iterate adapter protocol v0.2`。 | medium | `true` | 选错 early baseline 会误导后续 comparison。 | founder 应先在 `83bede1` 和 `5e5fe21` 之间明确选择。 |
| `core-v0-foundation-baseline` | `2aa4cf3 Add foundation consolidation artifacts` | 明确的 P53 consolidation point，P0-P51 foundation artifacts 在此变得可维护。 | high | `false` | 低；主要风险是把 foundation baseline 误认为 runtime maturity。 | 建议接受为 foundation baseline candidate。 |
| `core-v0-observable-baseline` | `04a15ff Add overnight harness work summary` | 在 observatory、no-write harness、scenario routing、preview specialization、boundary monitor、usability review 和 roadmap 后关闭 P102-P110。 | high | `false` | 中；observability 可能被误认为 product readiness。 | 建议接受为 observability baseline，但不含产品/运行时含义。 |
| `core-v1-pre-rebuild-ready` | `6e7639a Add baseline tagging plan` | 包含 P154 push readiness、P155 lineage governance 和 P156 baseline/branch plan，是当前最佳 pre-rebuild review point。 | high | `true` | tag 名称很权威，可能被误解为 rebuild approval。 | 若 founder 确认 P156 应纳入，则用 `6e7639a`；否则用 `eb871fc`。 |
| `milestone-p100-harness-dry-run` | `bedc0a4 Add minimal CLI harness dry run` | 引入第一个 no-write `harness-dry-run` command。 | high | `false` | 低；milestone 可能被误解为 harness runtime maturity。 | 建议接受为 implementation milestone。 |
| `milestone-p110-scenario-routing` | `04a15ff Add overnight harness work summary` | 关闭 P102-P110 routing 和 review cycle。 | high | `false` | 低；应保持为 cycle closure marker。 | 建议接受为 scenario-routing milestone。 |
| `milestone-p154-pre-rebuild-ready` | `46e0003 Update push readiness audit` | 记录 P155/P156 governance 前的 final push-readiness audit。 | high | `false` | 中；"ready" 可能被误解为 rebuild approval。 | 建议仅作为 pre-lineage push-readiness milestone。 |
| `milestone-p155-lineage-governance` | `eb871fc Add lineage branch governance RFC` | 添加 lineage、branch、tag、checkpoint、sandbox、quarantine、recovery 和 selected-return governance RFC。 | high | `false` | 低；governance RFC 可能被误解为 Git execution approval。 | 建议接受为 lineage-governance milestone。 |
| `milestone-p156-baseline-tagging-plan` | `6e7639a Add baseline tagging plan` | 添加 candidate tag/branch plan 和 manual command drafts，但不执行。 | high | `false` | 低；command drafts 可能被误认为已经运行。 | 建议接受为 planning milestone。 |

## Branch Review / 分支审查

| Branch | Candidate Fork Point | Reason | Confidence | needs_founder_confirmation | Risk | Recommendation |
|---|---|---|---|---|---|---|
| `core/baseline` | founder 选择 `83bede1` 或 `5e5fe21` 后的 `core-v0-baseline` | earliest local Core lineage 的稳定 reference。 | medium | `true` | fork point 错误会削弱 original Core reference。 | 等 founder baseline decision；保持只读 reference。 |
| `core/pre-rebuild-ready` | founder 确认 P155 vs P156 后的 `core-v1-pre-rebuild-ready` | accepted pre-rebuild state 的 protected reference。 | high | `true` | branch 名称可能像 rebuild approval。 | final main push 和 founder confirmation 后再创建。 |
| `instance/01-local-rebuild-trial` | confirmed `core-v1-pre-rebuild-ready` | future local rebuild trial 的 sandbox。 | high | `true` | 可能意外启动 rebuild 或 merge sandbox output。 | 只在 tags、final push、clean tests 和 explicit rebuild-trial approval 后创建。 |
| `instance/01-astrbot-shadow` | confirmed `core-v1-pre-rebuild-ready` | future AstrBot-shaped input observation 的 shadow line。 | medium | `true` | adapter context 可能污染 identity。 | 推迟到 adapter-shadow work 被明确批准。 |
| `instance/01-synthetic-history-v1` | confirmed `core-v1-pre-rebuild-ready` | synthetic-history experiments 的 sandbox。 | medium | `true` | synthetic autobiography 可能被误认为 Core history。 | 除非 synthetic-history work 被明确批准，否则推迟。 |
| `research/synthetic-history-accelerator` | confirmed `core-v1-pre-rebuild-ready` 或 `milestone-p155-lineage-governance` | synthetic-history acceleration theory 的 research line。 | medium | `true` | research branch 可能滑向 instance autobiography。 | 推迟；只允许 RFCs、tests、reports 或 boundary improvements 回流。 |
| `research/ctm-temporal-dynamics` | confirmed `core-v1-pre-rebuild-ready` 或 `milestone-p155-lineage-governance` | symbolic CTM-inspired temporal dynamics 的 research line。 | medium | `true` | CTM vocabulary 可能被误认为 CTM runtime。 | 等具体 CTM research task 被批准后再创建。 |
| `research/tool-first-evolution` | confirmed `core-v1-pre-rebuild-ready` 或 `milestone-p155-lineage-governance` | capability-evidence 和 tool-first evolution policy 的 research line。 | medium | `true` | capability work 可能滑向 tool execution 或 tool trust。 | 推迟；只允许 reviewed evidence schemas、policies、reports 或 tests 回流。 |
| `quarantine/imported-astrbot-memory` | confirmed `core-v1-pre-rebuild-ready` | future imported AstrBot 或 Angel Memory material 的 containment line。 | high | `true` | imported memory 可能看起来像 native Core history。 | 只在 import review 开始时创建；不得 direct-merge。 |
| `quarantine/llm-self-claims` | confirmed `core-v1-pre-rebuild-ready` | model self-claims 或 contaminated autobiographical output 的 containment line。 | high | `true` | model self-claims 可能污染 identity。 | 只在相关材料存在时创建；不得 direct-merge。 |

## Founder Decision Summary / Founder 决策摘要

仍需要 founder confirmation：

- 选择 `core-v0-baseline`：`83bede1` 还是 `5e5fe21`；
- 选择 `core-v1-pre-rebuild-ready`：`eb871fc` 还是 `6e7639a`；
- 决定现在创建所有 proposed tags，还是只创建四个最安全的 milestone tags；
- 决定现在只创建 `core/*` branches，还是把 `instance/*`、`research/*`、`quarantine/*` 延后到实际工作开始时；
- 允许任何 future local rebuild trial branch 存在。

推荐的最安全顺序：

1. 完成 P158 manual command sheet；
2. 完成 P159 final push-readiness audit；
3. 如果检查通过，在 P160 push 当前 `main` 到 GitHub；
4. founder 手动确认 tag decisions；
5. 之后才在单独 manual operation 中创建 tags/branches。

## Non-Execution Statement / 非执行声明

P157 不会：

- 创建 git tags；
- 创建 git branches；
- push；
- push tags；
- 启动 rebuild；
- 读取 old 01；
- 连接 AstrBot、adapters、Web 或 Companion；
- 写 formal state、event、memory 或 recall records；
- 修改 Identity Core；
- 执行 growth、tool、temporal、CTM 或 policy runtime。
