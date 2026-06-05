# Manual Tag and Branch Command Sheet

Chinese version: [MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md)

Status: `P158`, `manual-command-sheet`, `planning-only`, `no-tag-created`,
`no-branch-created`, `no-push-tags`, `no-rebuild-started`.

P158 provides command drafts for a future human/manual operation. It does not
run any command in this sheet. It does not create git tags, create git branches,
push tags, start local 01 rebuild, connect old 01, connect adapters, or modify
Core state.

## Do-Not-Execute Boundary

This sheet is not an execution phase.

- `git_tag_created: false`
- `git_branch_created: false`
- `rebuild_started: false`
- no command below has been run by P158
- all commands require founder confirmation before use

## Execute-Only-After Checks

Run these checks manually before any future tag or branch creation:

```bash
git status --short
git branch --show-current
git log -1 --oneline
git diff --check
python3 -m unittest
python3 -m one_core.cli pre-rebuild-verification --format json --lang en
```

Expected precondition:

- branch is `main`;
- worktree is clean;
- tests pass;
- forbidden search passes;
- GitHub `main` has already been pushed after P159/P160;
- founder has confirmed the exact tag and branch choices.

## Founder Confirmation Required

Do not run these until the founder explicitly confirms:

- whether `core-v0-baseline` uses `83bede1` or `5e5fe21`;
- whether `core-v1-pre-rebuild-ready` uses `eb871fc`, `6e7639a`, or a later
  final-readiness commit;
- whether to create all proposed tags now or only a smaller baseline set;
- whether to create any `instance/*`, `research/*`, or `quarantine/*` branch
  now;
- whether a local-only rebuild trial branch may be created.

## Recommended Tag Commands

| Tag | Purpose | Command Draft | Founder Confirmation |
|---|---|---|---|
| `core-v0-baseline` | Earliest local Core baseline after founder chooses the exact anchor. | `git tag core-v0-baseline <confirmed-core-v0-commit>` | required |
| `core-v0-foundation-baseline` | Foundation consolidation baseline. | `git tag core-v0-foundation-baseline 2aa4cf3` | recommended before execution |
| `core-v0-observable-baseline` | Observatory/harness visibility baseline. | `git tag core-v0-observable-baseline 04a15ff` | recommended before execution |
| `core-v1-pre-rebuild-ready` | Accepted pre-rebuild state after final readiness. | `git tag core-v1-pre-rebuild-ready <confirmed-pre-rebuild-commit>` | required |
| `milestone-p100-harness-dry-run` | First no-write harness dry-run milestone. | `git tag milestone-p100-harness-dry-run bedc0a4` | recommended before execution |
| `milestone-p110-scenario-routing` | Scenario routing cycle closure. | `git tag milestone-p110-scenario-routing 04a15ff` | recommended before execution |
| `milestone-p154-pre-rebuild-ready` | Push-readiness audit milestone before lineage governance. | `git tag milestone-p154-pre-rebuild-ready 46e0003` | recommended before execution |
| `milestone-p155-lineage-governance` | Lineage governance milestone. | `git tag milestone-p155-lineage-governance eb871fc` | recommended before execution |
| `milestone-p156-baseline-tagging-plan` | Baseline tagging plan milestone. | `git tag milestone-p156-baseline-tagging-plan 6e7639a` | recommended before execution |
| `milestone-p157-founder-review` | Founder review milestone. | `git tag milestone-p157-founder-review f46cab2` | optional; wait until founder confirms whether review milestones should be tagged |

## Recommended Branch Commands

| Branch | Purpose | Command Draft | Founder Confirmation | Direct Merge To `main` |
|---|---|---|---|---|
| `core/baseline` | Read-only baseline reference. | `git checkout -b core/baseline core-v0-baseline` | required | `false` |
| `core/pre-rebuild-ready` | Protected pre-rebuild reference. | `git checkout -b core/pre-rebuild-ready core-v1-pre-rebuild-ready` | required | `false` |
| `instance/01-local-rebuild-trial` | Local-only rebuild trial sandbox. | `git checkout -b instance/01-local-rebuild-trial core-v1-pre-rebuild-ready` | required | `false` |
| `instance/01-astrbot-shadow` | Future AstrBot shadow observation sandbox. | `git checkout -b instance/01-astrbot-shadow core-v1-pre-rebuild-ready` | required | `false` |
| `instance/01-synthetic-history-v1` | Synthetic-history instance sandbox. | `git checkout -b instance/01-synthetic-history-v1 core-v1-pre-rebuild-ready` | required | `false` |
| `research/synthetic-history-accelerator` | Synthetic-history research branch. | `git checkout -b research/synthetic-history-accelerator core-v1-pre-rebuild-ready` | required | `false` |
| `research/ctm-temporal-dynamics` | CTM-inspired temporal research branch. | `git checkout -b research/ctm-temporal-dynamics core-v1-pre-rebuild-ready` | required | `false` |
| `research/tool-first-evolution` | Tool-first evolution research branch. | `git checkout -b research/tool-first-evolution core-v1-pre-rebuild-ready` | required | `false` |
| `quarantine/imported-astrbot-memory` | Quarantine branch for imported AstrBot/Angel material. | `git checkout -b quarantine/imported-astrbot-memory core-v1-pre-rebuild-ready` | required when material exists | `false` |
| `quarantine/llm-self-claims` | Quarantine branch for model self-claims. | `git checkout -b quarantine/llm-self-claims core-v1-pre-rebuild-ready` | required when material exists | `false` |

## Post-Execution Verification Drafts

If a future human operation creates tags:

```bash
git tag --list "core-*"
git tag --list "milestone-*"
git show --no-patch --oneline core-v1-pre-rebuild-ready
```

If a future human operation creates branches:

```bash
git branch --list "core/*"
git branch --list "instance/*"
git branch --list "research/*"
git branch --list "quarantine/*"
git log -1 --oneline core/pre-rebuild-ready
```

After any future operation:

```bash
git status --short
git branch --show-current
python3 -m unittest
```

## Rollback / Deletion Drafts

Use only if a future manual operation creates the wrong local tag or branch.
These commands are also drafts and are not executed by P158.

Local tag deletion drafts:

```bash
git tag -d <wrong-tag>
```

Local branch deletion drafts:

```bash
git branch -D <wrong-branch>
```

Remote tag deletion is explicitly out of scope for the current plan because P158
does not push tags.

## Return Rules

- `core/*` branches are reference branches, not merge sources.
- `instance/*` branches never direct-merge into `main`.
- `research/*` branches return only RFCs, tests, reports, safe schemas, or
  reviewed boundary improvements.
- `quarantine/*` branches never merge into `main`; they may only support
  source-attributed manual selected return.

## Non-Execution Statement

P158 does not:

- create git tags;
- create git branches;
- push tags;
- push main;
- start local rebuild;
- read old 01;
- connect AstrBot, adapters, Web, or Companion;
- write formal state, event, memory, or recall records;
- mutate Identity Core;
- execute growth, tool, temporal, CTM, or policy runtime.
