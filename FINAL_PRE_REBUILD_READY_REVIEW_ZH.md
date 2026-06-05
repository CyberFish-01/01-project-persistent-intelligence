# Final Pre-Rebuild Ready Review / 最终重构前就绪复盘

English version: [FINAL_PRE_REBUILD_READY_REVIEW.md](./FINAL_PRE_REBUILD_READY_REVIEW.md)

状态：`P160`、`final-review`、`post-push`、`manual-next-step-only`。

本复盘回答项目是否可以从 final push readiness 进入 manual baseline tag / branch creation，以及是否
可以准备 local-only 01 rebuild trial。它不执行这两步。

## 1. GitHub `main` 是否已同步？

已同步。第一次 P160 push 已把 GitHub `main` 从 `b7abfa1` 更新到 `34ce833`。随后 final report commit
会通过最后一次 `main`-only push 同步；完成状态需要通过验证 GitHub `refs/heads/main` 等于本地 `HEAD`
来证明。

## 2. 是否可以进入手动 baseline tags / branches？

可以，但必须在 GitHub `main` 已确认等于本地 `HEAD` 之后。

允许的下一步人工操作：

- 审查 [BASELINE_TAGGING_PLAN_ZH.md](./BASELINE_TAGGING_PLAN_ZH.md)；
- 审查 [BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md](./BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md)；
- 审查 [MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md)；
- 选择准确 baseline commits；
- 手动创建 tags 和 branches。

这必须是单独 founder-confirmed operation。它不得在 P160 自动发生。

## 3. 是否可以准备 local-only 01 rebuild trial？

可以，但只能在 manual tags/branches 创建之后作为准备。

推荐顺序：

1. 确认 GitHub `main` 等于本地 `HEAD`。
2. Founder 确认准确 baseline tags 和 branch set。
3. 手动创建 baseline tags。
4. 手动创建 `core/pre-rebuild-ready`。
5. 手动创建 `instance/01-local-rebuild-trial`。
6. 确认 worktree clean，并运行 tests。
7. 之后才考虑 local-only rebuild trial。

P160 不启动 rebuild。

## 4. 哪些仍需 founder 手动确认？

- `core-v0-baseline` 的准确 commit；
- `core-v1-pre-rebuild-ready` 的准确 commit；
- 是 tag 所有 milestone，还是只创建最小 baseline set；
- research/quarantine branches 现在创建，还是后推；
- 是否立即创建 `instance/01-local-rebuild-trial`；
- 是新增 GitHub remote alias，还是继续使用显式 GitHub URL；
- manual branch creation 后，是否允许 local-only rebuild trial 开始。

## 5. 推荐下一步命令是什么？

GitHub `main` 同步且 founder confirmation 记录之后，manual command drafts 在
[MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md)。

可能的最小顺序：

```bash
git status --short
git branch --show-current
python3 -m unittest
python3 -m one_core.cli pre-rebuild-verification --format json --lang en
git tag core-v1-pre-rebuild-ready <confirmed-pre-rebuild-commit>
git checkout -b core/pre-rebuild-ready core-v1-pre-rebuild-ready
git checkout -b instance/01-local-rebuild-trial core-v1-pre-rebuild-ready
```

在 founder 明确确认 exact commit 和 branch set 前，不要运行这些命令。

## 6. 是否仍禁止自动重构？

是。

仍禁止：

- automatic rebuild；
- old 01 read；
- AstrBot / adapter integration；
- model call；
- state migration；
- identity mutation；
- memory rewrite；
- recall event write；
- growth lifecycle execution；
- tool execution；
- temporal runtime；
- reconstruction reducer execution；
- event compaction。

## Final Decision / 最终判断

仓库在 GitHub `main` 验证等于本地 `HEAD` 后，可以进入 manual baseline tag / branch creation review。

它还没有进入 local rebuild execution。下一步是 founder-confirmed manual lineage operation，不是自动重构。
