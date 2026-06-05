# Manual Tag and Branch Command Sheet / 手动 Tag 与分支命令清单

English version: [MANUAL_TAG_BRANCH_COMMAND_SHEET.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET.md)

状态：`P158`、`manual-command-sheet`、`planning-only`、`no-tag-created`、
`no-branch-created`、`no-push-tags`、`no-rebuild-started`。

P158 为未来 human/manual operation 提供命令草案。它不运行本清单里的任何命令，不创建 git tags，
不创建 git branches，不 push tags，不启动 local 01 rebuild，不接 old 01，不连接 adapters，也不修改
Core state。

## Do-Not-Execute Boundary / 不执行边界

本清单不是执行阶段。

- `git_tag_created: false`
- `git_branch_created: false`
- `rebuild_started: false`
- P158 没有运行下面任何命令
- 所有命令使用前都需要 founder confirmation

## Execute-Only-After Checks / 执行前检查

未来任何 tag 或 branch creation 前，人工运行：

```bash
git status --short
git branch --show-current
git log -1 --oneline
git diff --check
python3 -m unittest
python3 -m one_core.cli pre-rebuild-verification --format json --lang en
```

预期前置条件：

- branch 是 `main`；
- worktree clean；
- tests pass；
- forbidden search pass；
- P159/P160 后 GitHub `main` 已经 push；
- founder 已确认准确 tag 和 branch choices。

## Founder Confirmation Required / 必须等待 Founder 确认

以下事项未确认前不要运行：

- `core-v0-baseline` 使用 `83bede1` 还是 `5e5fe21`；
- `core-v1-pre-rebuild-ready` 使用 `eb871fc`、`6e7639a`，还是后续 final-readiness commit；
- 现在创建所有 proposed tags，还是只创建更小的 baseline set；
- 现在是否创建任何 `instance/*`、`research/*` 或 `quarantine/*` branch；
- 是否允许创建 local-only rebuild trial branch。

## Recommended Tag Commands / 推荐 Tag 命令

| Tag | Purpose | Command Draft | Founder Confirmation |
|---|---|---|---|
| `core-v0-baseline` | founder 选择准确 anchor 后的 earliest local Core baseline。 | `git tag core-v0-baseline <confirmed-core-v0-commit>` | required |
| `core-v0-foundation-baseline` | foundation consolidation baseline。 | `git tag core-v0-foundation-baseline 2aa4cf3` | recommended before execution |
| `core-v0-observable-baseline` | observatory/harness visibility baseline。 | `git tag core-v0-observable-baseline 04a15ff` | recommended before execution |
| `core-v1-pre-rebuild-ready` | final readiness 后 accepted pre-rebuild state。 | `git tag core-v1-pre-rebuild-ready <confirmed-pre-rebuild-commit>` | required |
| `milestone-p100-harness-dry-run` | first no-write harness dry-run milestone。 | `git tag milestone-p100-harness-dry-run bedc0a4` | recommended before execution |
| `milestone-p110-scenario-routing` | scenario routing cycle closure。 | `git tag milestone-p110-scenario-routing 04a15ff` | recommended before execution |
| `milestone-p154-pre-rebuild-ready` | lineage governance 前的 push-readiness audit milestone。 | `git tag milestone-p154-pre-rebuild-ready 46e0003` | recommended before execution |
| `milestone-p155-lineage-governance` | lineage governance milestone。 | `git tag milestone-p155-lineage-governance eb871fc` | recommended before execution |
| `milestone-p156-baseline-tagging-plan` | baseline tagging plan milestone。 | `git tag milestone-p156-baseline-tagging-plan 6e7639a` | recommended before execution |
| `milestone-p157-founder-review` | founder review milestone。 | `git tag milestone-p157-founder-review f46cab2` | optional；等待 founder 确认是否需要 review milestones tag |

## Recommended Branch Commands / 推荐分支命令

| Branch | Purpose | Command Draft | Founder Confirmation | Direct Merge To `main` |
|---|---|---|---|---|
| `core/baseline` | read-only baseline reference。 | `git checkout -b core/baseline core-v0-baseline` | required | `false` |
| `core/pre-rebuild-ready` | protected pre-rebuild reference。 | `git checkout -b core/pre-rebuild-ready core-v1-pre-rebuild-ready` | required | `false` |
| `instance/01-local-rebuild-trial` | local-only rebuild trial sandbox。 | `git checkout -b instance/01-local-rebuild-trial core-v1-pre-rebuild-ready` | required | `false` |
| `instance/01-astrbot-shadow` | future AstrBot shadow observation sandbox。 | `git checkout -b instance/01-astrbot-shadow core-v1-pre-rebuild-ready` | required | `false` |
| `instance/01-synthetic-history-v1` | synthetic-history instance sandbox。 | `git checkout -b instance/01-synthetic-history-v1 core-v1-pre-rebuild-ready` | required | `false` |
| `research/synthetic-history-accelerator` | synthetic-history research branch。 | `git checkout -b research/synthetic-history-accelerator core-v1-pre-rebuild-ready` | required | `false` |
| `research/ctm-temporal-dynamics` | CTM-inspired temporal research branch。 | `git checkout -b research/ctm-temporal-dynamics core-v1-pre-rebuild-ready` | required | `false` |
| `research/tool-first-evolution` | tool-first evolution research branch。 | `git checkout -b research/tool-first-evolution core-v1-pre-rebuild-ready` | required | `false` |
| `quarantine/imported-astrbot-memory` | imported AstrBot/Angel material 的 quarantine branch。 | `git checkout -b quarantine/imported-astrbot-memory core-v1-pre-rebuild-ready` | required when material exists | `false` |
| `quarantine/llm-self-claims` | model self-claims 的 quarantine branch。 | `git checkout -b quarantine/llm-self-claims core-v1-pre-rebuild-ready` | required when material exists | `false` |

## Post-Execution Verification Drafts / 执行后验证草案

如果未来 human operation 创建 tags：

```bash
git tag --list "core-*"
git tag --list "milestone-*"
git show --no-patch --oneline core-v1-pre-rebuild-ready
```

如果未来 human operation 创建 branches：

```bash
git branch --list "core/*"
git branch --list "instance/*"
git branch --list "research/*"
git branch --list "quarantine/*"
git log -1 --oneline core/pre-rebuild-ready
```

任何 future operation 后：

```bash
git status --short
git branch --show-current
python3 -m unittest
```

## Rollback / Deletion Drafts / 回滚与删除草案

只在 future manual operation 创建了错误 local tag 或 branch 时使用。这些命令也是草案，P158 不执行。

Local tag deletion drafts：

```bash
git tag -d <wrong-tag>
```

Local branch deletion drafts：

```bash
git branch -D <wrong-branch>
```

Remote tag deletion 明确不在当前计划内，因为 P158 不 push tags。

## Return Rules / 回流规则

- `core/*` branches 是 reference branches，不是 merge sources。
- `instance/*` branches 不得 direct-merge 到 `main`。
- `research/*` branches 只回流 RFCs、tests、reports、safe schemas 或 reviewed boundary improvements。
- `quarantine/*` branches 不得 merge 到 `main`；它们只能支持 source-attributed manual selected return。

## Non-Execution Statement / 非执行声明

P158 不会：

- 创建 git tags；
- 创建 git branches；
- push tags；
- push main；
- 启动 local rebuild；
- 读取 old 01；
- 连接 AstrBot、adapters、Web 或 Companion；
- 写 formal state、event、memory 或 recall records；
- 修改 Identity Core；
- 执行 growth、tool、temporal、CTM 或 policy runtime。
