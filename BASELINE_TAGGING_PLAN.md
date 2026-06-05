# Baseline Tagging and Branch Creation Plan

Chinese version: [BASELINE_TAGGING_PLAN_ZH.md](./BASELINE_TAGGING_PLAN_ZH.md)

Status: `P156`, `planning-only`, `governance-only`, `non-runtime`,
`no-tag-created`, `no-branch-created`, `no-push`, `no-rebuild-started`.

P156 turns the P155 lineage governance rules into a concrete candidate plan for
future baseline tags, milestone tags, and sandbox branches. It does not create a
git tag, create a git branch, push, modify git history, start local 01 rebuild,
read old 01, import external material, write state, write events, write memory,
mutate Identity Core, execute tools, call a model, or connect adapters.

## 1. Current State

Observed at P156 planning time, before this document is committed:

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

Note: after this P156 document is committed, `HEAD` will move to the P156 commit.
This plan intentionally uses observed pre-P156 candidate commits unless a row
explicitly says that founder review may choose a later P156 commit.

## 2. Proposed Baseline Tags

These tags are recommended only. P156 does not create them.

| Proposed Tag | Purpose | Selection Standard | Candidate Commit | Why This Candidate | needs_founder_confirmation |
|---|---|---|---|---|---|
| `core-v0-baseline` | Preserve the earliest stable local 01 Core baseline before the long foundation/governance expansion. | Choose the last commit that still represents the early local Core and generic adapter work before the foundation-governance run begins. | `5e5fe21 Add adapter event deduplication` | It is the last early runtime/adapter-hardening commit before `2e2ae68 Define project foundation invariants`. Alternative: `83bede1 Iterate adapter protocol v0.2` if the founder wants the handoff-era protocol v0.2 as the baseline. | `true` |
| `core-v0-foundation-baseline` | Preserve the first consolidated foundation map after P0-P51 were compressed into maintainable artifacts. | Choose the commit that adds P53 foundation consolidation artifacts and passes tests. | `2aa4cf3 Add foundation consolidation artifacts` | It is the explicit P53 consolidation commit and is also the known `origin/main` anchor before later autonomous foundation expansion. | `false` |
| `core-v0-observable-baseline` | Preserve the baseline where read-only observatory and dry-run harness visibility are available. | Choose a commit after observatory reporting, no-write harness dry-run, scenario routing, specialization, review, and closure are present. | `04a15ff Add overnight harness work summary` | It closes P102-P110 after observatory work, P100 dry-run, scenario routing, specialized previews, boundary hardening, usability review, and roadmap. | `false` |
| `core-v1-pre-rebuild-ready` | Preserve the current pre-rebuild-ready Core after verification, founder checkpoint, push audit, and lineage governance. | Choose P155 if lineage governance is the final required safety gate, or choose the later P156 commit if the founder wants the tag/branch plan included. | `eb871fc Add lineage branch governance RFC` | It records P155 lineage governance after P154 push readiness. However, founder may decide that the P156 plan commit should be included before naming v1 pre-rebuild-ready. | `true` |
| `milestone-p100-harness-dry-run` | Mark the first minimal no-write local harness dry-run. | Choose the commit that introduced `python3 -m one_core.cli harness-dry-run`. | `bedc0a4 Add minimal CLI harness dry run` | It is the P100 implementation commit for the dry-run harness. | `false` |
| `milestone-p110-scenario-routing` | Mark closure of the P102-P110 harness routing and review cycle. | Choose the commit that closes routing, preview specialization, boundary hardening, review, roadmap, and overnight summary. | `04a15ff Add overnight harness work summary` | It is the P110 closure commit for the scenario-routing cycle. | `false` |
| `milestone-p154-pre-rebuild-ready` | Mark the local push-readiness audit before lineage governance. | Choose the P154 audit commit after verification, founder checkpoint, and clean push-readiness report. | `46e0003 Update push readiness audit` | It is the P154 push-readiness commit immediately before P155. | `false` |
| `milestone-p155-lineage-governance` | Mark the lineage and branch governance safety gate. | Choose the P155 governance commit. | `eb871fc Add lineage branch governance RFC` | It adds lineage, branch, tag, checkpoint, sandbox, quarantine, recovery, and selected-return governance. | `false` |

### Baseline Selection Notes

- If a candidate is marked `needs_founder_confirmation: true`, do not create the
  tag until the founder explicitly accepts that commit.
- `core-v0-baseline` is deliberately conservative because "initial Core" may
  mean either the handoff-era protocol v0.2 commit or the last early runtime
  hardening commit before foundation governance.
- `core-v1-pre-rebuild-ready` may reasonably point at P155 or at the future P156
  commit after this plan is reviewed. That choice should be explicit.

## 3. Proposed Branches

These branches are recommended only. P156 does not create them.

| Proposed Branch | Suggested Fork Point | Purpose | Direct Merge To `main` Allowed | Return Rule |
|---|---|---|---|---|
| `core/baseline` | `core-v0-baseline` after founder confirmation | Stable reference branch for earliest local Core baseline. | `false` | Read-only reference. Do not merge. Use for comparison and recovery only. |
| `core/pre-rebuild-ready` | `core-v1-pre-rebuild-ready` after founder confirmation | Protected reference branch for the accepted pre-rebuild state. | `false` | Manual review only. It can inform recovery or comparison, not act as a merge source. |
| `instance/01-local-rebuild-trial` | `core-v1-pre-rebuild-ready` after confirmed tags | Local rebuild sandbox for a future 01 trial. | `false` | `candidate -> quarantine -> review -> manual selected return`. No direct merge. |
| `instance/01-astrbot-shadow` | `core-v1-pre-rebuild-ready` after confirmed tags | Shadow instance for future AstrBot-shaped input observation. | `false` | Adapter-shaped output remains shadow evidence or quarantine material. No platform-owned identity return. |
| `instance/01-synthetic-history-v1` | `core-v1-pre-rebuild-ready` after confirmed tags | Sandbox for synthetic-history experiments. | `false` | Synthetic autobiography cannot return as Core memory. Only reviewed theory, tests, or boundary improvements may return. |
| `research/synthetic-history-accelerator` | `core-v1-pre-rebuild-ready` or `milestone-p155-lineage-governance` | Research branch for future synthetic-history acceleration ideas. | `false` | Return only RFCs, tests, reports, safe schemas, or reviewed boundary improvements. |
| `research/ctm-temporal-dynamics` | `core-v1-pre-rebuild-ready` or `milestone-p155-lineage-governance` | Research branch for symbolic CTM-inspired temporal dynamics. | `false` | Return symbolic review vocabulary, evaluation plans, or tests only. No CTM runtime return. |
| `research/tool-first-evolution` | `core-v1-pre-rebuild-ready` or `milestone-p155-lineage-governance` | Research branch for capability-evolution and Tool-First evidence models. | `false` | Return reviewed tool evidence schemas, policies, reports, or tests only. No automatic tool trust return. |
| `quarantine/imported-astrbot-memory` | `core-v1-pre-rebuild-ready` after confirmed tags | Quarantine branch for future imported AstrBot or Angel Memory material. | `false` | Quarantine does not merge. Small source-attributed insights may return only through manual selected return. |
| `quarantine/llm-self-claims` | `core-v1-pre-rebuild-ready` after confirmed tags | Quarantine branch for future model self-claims, self-descriptions, or contaminated autobiographical output. | `false` | Model self-claims do not become Core history. Only reviewed risk notes or boundary improvements may return. |

## 4. Do-Not-Execute Rule

P156 is a plan only.

This phase does not:

- create any git tag;
- create any git branch;
- push to a remote;
- modify git history;
- start local 01 rebuild;
- read old 01;
- import memory;
- merge branches;
- approve selected return;
- authorize any future command execution.

All tag and branch suggestions wait for explicit founder confirmation.

## 5. Rebuild Safety Gate

Before any real local rebuild starts, the following must happen in a separate,
explicitly approved operation:

1. push current `main`;
2. create confirmed baseline and milestone tags;
3. create the local rebuild trial branch from the confirmed pre-rebuild tag;
4. verify the worktree is clean;
5. run full tests;
6. run forbidden-pattern checks;
7. confirm no-write, lockdown, quarantine, manual review, and lineage boundaries;
8. record the founder approval that allows the rebuild trial to begin.

Passing this list is still not automatic merge authority.

## 6. Recommended Manual Commands

These commands are drafts for a future manual operation. Do not execute them
until the founder confirms the tag names and commit choices.

Tag drafts:

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

Branch drafts:

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

Verification drafts:

```bash
git status --short
git branch --show-current
git log -1 --oneline
git diff --check
python3 -m unittest
python3 -m one_core.cli pre-rebuild-verification --format json --lang en
```

## 7. Risks

| Risk | Why It Matters | Mitigation |
|---|---|---|
| wrong baseline selection | A bad baseline can make later recovery or comparison misleading. | Mark uncertain candidates with `needs_founder_confirmation`; inspect phase index, verification records, and git log before tagging. |
| tagging polluted commit | A tag can give contaminated or unstable history a false sense of authority. | Run tests, forbidden search, link checks, and founder review before creating tags. |
| instance branch created from unstable state | A sandbox forked from the wrong point can confuse instance behavior with Core history. | Create instance branches only from confirmed baseline/pre-rebuild tags. |
| accidentally merging instance branch into main | Instance output may contain synthetic history, adapter artifacts, model claims, or unreviewed tool trust. | Keep direct merge to `main` normally false; require candidate -> quarantine -> review -> manual selected return. |
| losing original Core reference | Without accepted baseline tags, future rebuild work can obscure the original Core lineage. | Create confirmed baseline tags before rebuild, then keep Core trunk and instance sandbox separate. |

## Non-Execution Statement

P156 does not:

- create git tags;
- create git branches;
- push;
- start rebuild;
- read old 01;
- import AstrBot memory;
- connect adapters;
- call a model;
- write formal state;
- write events;
- write memory;
- write recall events;
- mutate Identity Core;
- rewrite memory;
- execute growth;
- execute tools;
- enable temporal runtime;
- execute policy;
- modify git history.
