# Baseline Tagging and Branch Creation Plan / 基线 Tag 与分支创建计划

English version: [BASELINE_TAGGING_PLAN.md](./BASELINE_TAGGING_PLAN.md)

状态：`P156`、`planning-only`、`governance-only`、`non-runtime`、
`no-tag-created`、`no-branch-created`、`no-push`、`no-rebuild-started`。

P156 把 P155 lineage governance 规则转成 future baseline tags、milestone tags 和 sandbox
branches 的具体候选计划。它不创建 git tag，不创建 git branch，不 push，不修改 git history，
不启动 local 01 rebuild，不读取 old 01，不导入外部材料，不写 state、events 或 memory，不修改
Identity Core，不执行 tools，不调用模型，也不连接 adapters。

## 1. Current State / 当前状态

P156 planning time 观察到的状态，早于本文件 commit：

| Field | Value |
|---|---|
| current_branch | `main` |
| current_HEAD | `eb871fc` |
| latest_commit | `eb871fc Add lineage branch governance RFC` |
| worktree_clean_before_p156_edits | `true` |
| git_tag_created | `false` |
| git_branch_created | `false` |
| push_executed | `false` |
| rebuild_started | `false` |

注意：本 P156 文档 commit 后，`HEAD` 会移动到 P156 commit。除非某行明确说明 founder review 可以选择
后续 P156 commit，否则本计划使用的是 P156 之前观察到的候选 commit。

## 2. Proposed Baseline Tags / 建议的基线 Tag

以下 tag 只是建议。P156 不创建它们。

| Proposed Tag | Purpose | Selection Standard | Candidate Commit | Why This Candidate | needs_founder_confirmation |
|---|---|---|---|---|---|
| `core-v0-baseline` | 保存长期 foundation/governance 扩展前最早稳定的本地 01 Core baseline。 | 选择 foundation-governance run 开始前，仍代表 early local Core 和 generic adapter work 的最后 commit。 | `5e5fe21 Add adapter event deduplication` | 它是 `2e2ae68 Define project foundation invariants` 前最后一个 early runtime/adapter-hardening commit。替代候选：如果 founder 想把 handoff-era protocol v0.2 作为 baseline，则选择 `83bede1 Iterate adapter protocol v0.2`。 | `true` |
| `core-v0-foundation-baseline` | 保存 P0-P51 被压缩成可维护 foundation artifacts 后的第一份 foundation map。 | 选择添加 P53 foundation consolidation artifacts 且 tests pass 的 commit。 | `2aa4cf3 Add foundation consolidation artifacts` | 它是明确的 P53 consolidation commit，也是后续 autonomous foundation expansion 前已知的 `origin/main` 锚点。 | `false` |
| `core-v0-observable-baseline` | 保存 read-only observatory 和 dry-run harness visibility 已具备的 baseline。 | 选择 observatory reporting、no-write harness dry-run、scenario routing、specialization、review 和 closure 都存在后的 commit。 | `04a15ff Add overnight harness work summary` | 它在 observatory、P100 dry-run、scenario routing、specialized previews、boundary hardening、usability review 和 roadmap 后关闭 P102-P110。 | `false` |
| `core-v1-pre-rebuild-ready` | 保存 verification、founder checkpoint、push audit 和 lineage governance 之后的当前 pre-rebuild-ready Core。 | 如果 lineage governance 是最后必要安全门，则选择 P155；如果 founder 希望包含 P156 tag/branch plan，则选择后续 P156 commit。 | `eb871fc Add lineage branch governance RFC` | 它在 P154 push readiness 后记录 P155 lineage governance。但 founder 可能决定把 P156 plan commit 也纳入 v1 pre-rebuild-ready。 | `true` |
| `milestone-p100-harness-dry-run` | 标记第一个 minimal no-write local harness dry-run。 | 选择引入 `python3 -m one_core.cli harness-dry-run` 的 commit。 | `bedc0a4 Add minimal CLI harness dry run` | 它是 P100 dry-run harness implementation commit。 | `false` |
| `milestone-p110-scenario-routing` | 标记 P102-P110 harness routing 和 review cycle 收口。 | 选择关闭 routing、preview specialization、boundary hardening、review、roadmap 和 overnight summary 的 commit。 | `04a15ff Add overnight harness work summary` | 它是 scenario-routing cycle 的 P110 closure commit。 | `false` |
| `milestone-p154-pre-rebuild-ready` | 标记 lineage governance 前的 local push-readiness audit。 | 选择 verification、founder checkpoint 和 clean push-readiness report 后的 P154 audit commit。 | `46e0003 Update push readiness audit` | 它是 P155 前的 P154 push-readiness commit。 | `false` |
| `milestone-p155-lineage-governance` | 标记 lineage 与 branch governance 安全门。 | 选择 P155 governance commit。 | `eb871fc Add lineage branch governance RFC` | 它添加 lineage、branch、tag、checkpoint、sandbox、quarantine、recovery 和 selected-return governance。 | `false` |

### Baseline Selection Notes / 基线选择说明

- 如果某个候选标记为 `needs_founder_confirmation: true`，在 founder 明确接受该 commit 前，不要创建 tag。
- `core-v0-baseline` 故意保持保守，因为“initial Core”可能指 handoff-era protocol v0.2 commit，也可能指 foundation governance 前最后的 early runtime hardening commit。
- `core-v1-pre-rebuild-ready` 可以合理指向 P155，也可以在本计划 review 后指向 future P156 commit。这个选择必须显式确认。

## 3. Proposed Branches / 建议的分支

以下 branch 只是建议。P156 不创建它们。

| Proposed Branch | Suggested Fork Point | Purpose | Direct Merge To `main` Allowed | Return Rule |
|---|---|---|---|---|
| `core/baseline` | founder 确认后的 `core-v0-baseline` | 最早本地 Core baseline 的稳定 reference branch。 | `false` | 只读 reference。不 merge。只用于 comparison 和 recovery。 |
| `core/pre-rebuild-ready` | founder 确认后的 `core-v1-pre-rebuild-ready` | accepted pre-rebuild state 的 protected reference branch。 | `false` | 只允许 manual review。它可用于 recovery 或 comparison，不作为 merge source。 |
| `instance/01-local-rebuild-trial` | confirmed tags 之后的 `core-v1-pre-rebuild-ready` | future 01 local rebuild trial 的 sandbox。 | `false` | `candidate -> quarantine -> review -> manual selected return`。不得 direct merge。 |
| `instance/01-astrbot-shadow` | confirmed tags 之后的 `core-v1-pre-rebuild-ready` | future AstrBot-shaped input observation 的 shadow instance。 | `false` | adapter-shaped output 保持 shadow evidence 或 quarantine material。不得回流 platform-owned identity。 |
| `instance/01-synthetic-history-v1` | confirmed tags 之后的 `core-v1-pre-rebuild-ready` | synthetic-history experiments 的 sandbox。 | `false` | synthetic autobiography 不能作为 Core memory 回流。只允许 reviewed theory、tests 或 boundary improvements 回流。 |
| `research/synthetic-history-accelerator` | `core-v1-pre-rebuild-ready` 或 `milestone-p155-lineage-governance` | future synthetic-history acceleration ideas 的 research branch。 | `false` | 只允许 RFCs、tests、reports、safe schemas 或 reviewed boundary improvements 回流。 |
| `research/ctm-temporal-dynamics` | `core-v1-pre-rebuild-ready` 或 `milestone-p155-lineage-governance` | symbolic CTM-inspired temporal dynamics 的 research branch。 | `false` | 只允许 symbolic review vocabulary、evaluation plans 或 tests 回流。不允许 CTM runtime 回流。 |
| `research/tool-first-evolution` | `core-v1-pre-rebuild-ready` 或 `milestone-p155-lineage-governance` | capability-evolution 和 Tool-First evidence models 的 research branch。 | `false` | 只允许 reviewed tool evidence schemas、policies、reports 或 tests 回流。不允许 automatic tool trust 回流。 |
| `quarantine/imported-astrbot-memory` | confirmed tags 之后的 `core-v1-pre-rebuild-ready` | future imported AstrBot 或 Angel Memory material 的 quarantine branch。 | `false` | quarantine 不 merge。小范围 source-attributed insights 只能通过 manual selected return 回流。 |
| `quarantine/llm-self-claims` | confirmed tags 之后的 `core-v1-pre-rebuild-ready` | future model self-claims、self-descriptions 或 contaminated autobiographical output 的 quarantine branch。 | `false` | model self-claims 不成为 Core history。只允许 reviewed risk notes 或 boundary improvements 回流。 |

## 4. Do-Not-Execute Rule / 不执行规则

P156 只是 plan。

本阶段不：

- 创建任何 git tag；
- 创建任何 git branch；
- push 到远端；
- 修改 git history；
- 启动 local 01 rebuild；
- 读取 old 01；
- 导入 memory；
- merge branches；
- 批准 selected return；
- 授权任何 future command execution。

所有 tag 和 branch 建议都等待 founder 明确确认。

## 5. Rebuild Safety Gate / 重构安全门

任何真实 local rebuild 启动前，必须在单独、明确批准的操作中完成：

1. push current `main`；
2. 创建 confirmed baseline 和 milestone tags；
3. 从 confirmed pre-rebuild tag 创建 local rebuild trial branch；
4. 验证 worktree clean；
5. 运行 full tests；
6. 运行 forbidden-pattern checks；
7. 确认 no-write、lockdown、quarantine、manual review 和 lineage boundaries；
8. 记录允许 rebuild trial 开始的 founder approval。

通过这个列表仍不代表拥有 automatic merge authority。

## 6. Recommended Manual Commands / 建议的人工命令草案

这些命令只是 future manual operation 的草案。在 founder 确认 tag names 和 commit choices 之前不要执行。

Tag drafts：

```bash
git tag core-v0-baseline <confirmed-core-v0-commit>
git tag core-v0-foundation-baseline 2aa4cf3
git tag core-v0-observable-baseline 04a15ff
git tag core-v1-pre-rebuild-ready <confirmed-pre-rebuild-commit>
git tag milestone-p100-harness-dry-run bedc0a4
git tag milestone-p110-scenario-routing 04a15ff
git tag milestone-p154-pre-rebuild-ready 46e0003
git tag milestone-p155-lineage-governance eb871fc
```

Branch drafts：

```bash
git checkout -b core/baseline core-v0-baseline
git checkout -b core/pre-rebuild-ready core-v1-pre-rebuild-ready
git checkout -b instance/01-local-rebuild-trial core-v1-pre-rebuild-ready
git checkout -b instance/01-astrbot-shadow core-v1-pre-rebuild-ready
git checkout -b instance/01-synthetic-history-v1 core-v1-pre-rebuild-ready
git checkout -b research/synthetic-history-accelerator core-v1-pre-rebuild-ready
git checkout -b research/ctm-temporal-dynamics core-v1-pre-rebuild-ready
git checkout -b research/tool-first-evolution core-v1-pre-rebuild-ready
git checkout -b quarantine/imported-astrbot-memory core-v1-pre-rebuild-ready
git checkout -b quarantine/llm-self-claims core-v1-pre-rebuild-ready
```

Verification drafts：

```bash
git status --short
git branch --show-current
git log -1 --oneline
git diff --check
python3 -m unittest
python3 -m one_core.cli pre-rebuild-verification --format json --lang en
```

## 7. Risks / 风险

| Risk | Why It Matters | Mitigation |
|---|---|---|
| wrong baseline selection | 错误 baseline 会让后续 recovery 或 comparison 产生误导。 | 对不确定候选标记 `needs_founder_confirmation`；创建 tag 前检查 phase index、verification records 和 git log。 |
| tagging polluted commit | tag 可能让 contaminated 或 unstable history 获得虚假权威。 | 创建 tag 前运行 tests、forbidden search、link checks 和 founder review。 |
| instance branch created from unstable state | 从错误位置 fork sandbox 会混淆 instance behavior 和 Core history。 | instance branches 只能从 confirmed baseline/pre-rebuild tags 创建。 |
| accidentally merging instance branch into main | instance output 可能包含 synthetic history、adapter artifacts、model claims 或 unreviewed tool trust。 | direct merge to `main` normally false；要求 candidate -> quarantine -> review -> manual selected return。 |
| losing original Core reference | 没有 accepted baseline tags，future rebuild work 可能遮蔽 original Core lineage。 | rebuild 前创建 confirmed baseline tags，并保持 Core trunk 与 instance sandbox 分离。 |

## Non-Execution Statement / 非执行声明

P156 不会：

- 创建 git tags；
- 创建 git branches；
- push；
- 启动 rebuild；
- 读取 old 01；
- 导入 AstrBot memory；
- 连接 adapters；
- 调用模型；
- 写 formal state；
- 写 events；
- 写 memory；
- 写 recall events；
- 修改 Identity Core；
- rewrite memory；
- 执行 growth；
- 执行 tools；
- 启用 temporal runtime；
- 执行 policy；
- 修改 git history。
