# Final Pre-Rebuild Ready Review

Chinese version: [FINAL_PRE_REBUILD_READY_REVIEW_ZH.md](./FINAL_PRE_REBUILD_READY_REVIEW_ZH.md)

Status: `P160`, `final-review`, `post-push`, `manual-next-step-only`.

This review answers whether the project can move from final push readiness into
manual baseline tag / branch creation, and whether a local-only 01 rebuild trial
can be prepared. It does not execute either step.

## 1. Is GitHub `main` Synced?

Yes for the first P160 push: GitHub `main` was updated from `b7abfa1` to
`34ce833`.

Because this report and [PUSH_TO_GITHUB_REPORT.md](./PUSH_TO_GITHUB_REPORT.md)
are post-push artifacts, they require one final `main`-only sync after their
commit. That sync must still avoid tags and branch creation.

## 2. Can The Founder Enter Manual Baseline Tags / Branches?

Yes, after final GitHub `main` sync is confirmed.

Allowed next manual operation:

- review [BASELINE_TAGGING_PLAN.md](./BASELINE_TAGGING_PLAN.md);
- review [BASELINE_TAGGING_FOUNDER_REVIEW.md](./BASELINE_TAGGING_FOUNDER_REVIEW.md);
- review [MANUAL_TAG_BRANCH_COMMAND_SHEET.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET.md);
- choose exact baseline commits;
- create tags and branches manually.

This must be a separate founder-confirmed operation. It must not happen inside
P160 automation.

## 3. Can The Project Prepare Local-Only 01 Rebuild Trial?

Yes, but only as preparation after manual tags/branches are created.

The recommended sequence is:

1. Confirm GitHub `main` sync.
2. Founder confirms exact baseline tags and branch set.
3. Manually create baseline tags.
4. Manually create `core/pre-rebuild-ready`.
5. Manually create `instance/01-local-rebuild-trial`.
6. Verify clean worktree and run tests.
7. Only then consider local-only rebuild trial.

P160 does not start rebuild.

## 4. What Still Needs Founder Confirmation?

- exact commit for `core-v0-baseline`;
- exact commit for `core-v1-pre-rebuild-ready`;
- whether to tag every milestone or only the smallest baseline set;
- whether to create research/quarantine branches now or defer them;
- whether `instance/01-local-rebuild-trial` should be created immediately;
- whether to add a GitHub remote alias or keep using explicit GitHub URL;
- whether local-only rebuild trial may begin after manual branch creation.

## 5. Recommended Next Commands

After final GitHub sync and founder confirmation, manual command drafts are in
[MANUAL_TAG_BRANCH_COMMAND_SHEET.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET.md).

Minimum likely sequence:

```bash
git status --short
git branch --show-current
python3 -m unittest
python3 -m one_core.cli pre-rebuild-verification --format json --lang en
git tag core-v1-pre-rebuild-ready <confirmed-pre-rebuild-commit>
git checkout -b core/pre-rebuild-ready core-v1-pre-rebuild-ready
git checkout -b instance/01-local-rebuild-trial core-v1-pre-rebuild-ready
```

Do not run these commands until the founder explicitly confirms the exact
commit and branch set.

## 6. Does Automatic Rebuild Remain Forbidden?

Yes.

Still forbidden:

- automatic rebuild;
- old 01 read;
- AstrBot / adapter integration;
- model call;
- state migration;
- identity mutation;
- memory rewrite;
- recall event write;
- growth lifecycle execution;
- tool execution;
- temporal runtime;
- reconstruction reducer execution;
- event compaction.

## Final Decision

The repository is ready for final GitHub `main` sync and then manual baseline
tag / branch creation review.

It is not yet in local rebuild execution. The next move is founder-confirmed
manual lineage operation, not automatic rebuild.

