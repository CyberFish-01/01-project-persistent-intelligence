# Baseline Tagging Founder Review

Chinese version: [BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md](./BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md)

Status: `P157`, `founder-review`, `planning-only`, `no-tag-created`,
`no-branch-created`, `no-push`, `no-rebuild-started`.

P157 reviews the P156 baseline tag and branch creation plan for founder
decision. It does not create tags, create branches, push tags, push main, start
local rebuild, read old 01, connect adapters, write formal state, write memory,
or modify Identity Core.

## Current Review State

| Field | Value |
|---|---|
| current_branch_at_review_start | `main` |
| current_HEAD_at_review_start | `6e7639a Add baseline tagging plan` |
| worktree_clean_at_review_start | `true` |
| git_tag_created | `false` |
| git_branch_created | `false` |
| rebuild_started | `false` |

## Tag Review

| Tag | Candidate Commit | Reason | Confidence | needs_founder_confirmation | Risk | Recommendation |
|---|---|---|---|---|---|---|
| `core-v0-baseline` | `5e5fe21 Add adapter event deduplication` | Last early runtime/adapter-hardening commit before `2e2ae68 Define project foundation invariants`; alternative is `83bede1 Iterate adapter protocol v0.2` if founder wants the handoff-era protocol as the anchor. | medium | `true` | Wrong early baseline can make later comparison misleading. | Founder should choose between `83bede1` and `5e5fe21` before any tag creation. |
| `core-v0-foundation-baseline` | `2aa4cf3 Add foundation consolidation artifacts` | Explicit P53 consolidation point where P0-P51 foundation artifacts were made maintainable. | high | `false` | Low; only risk is treating foundation baseline as runtime maturity. | Accept as recommended candidate after final checks. |
| `core-v0-observable-baseline` | `04a15ff Add overnight harness work summary` | Closes P102-P110 after observatory, no-write harness, scenario routing, preview specialization, boundary monitor, usability review, and roadmap. | high | `false` | Medium; observability may be mistaken for product readiness. | Accept as observability baseline, with no product/runtime implication. |
| `core-v1-pre-rebuild-ready` | `6e7639a Add baseline tagging plan` | Includes P154 push readiness, P155 lineage governance, and P156 baseline/branch plan; this is the best current pre-rebuild review point. | high | `true` | This tag sounds authoritative and could be misread as rebuild approval. | Use `6e7639a` only if founder confirms P156 should be included; otherwise use `eb871fc`. |
| `milestone-p100-harness-dry-run` | `bedc0a4 Add minimal CLI harness dry run` | Introduces the first no-write `harness-dry-run` command. | high | `false` | Low; milestone might be mistaken for harness runtime maturity. | Accept as implementation milestone. |
| `milestone-p110-scenario-routing` | `04a15ff Add overnight harness work summary` | Closes the P102-P110 routing and review cycle. | high | `false` | Low; should remain a cycle closure marker. | Accept as scenario-routing milestone. |
| `milestone-p154-pre-rebuild-ready` | `46e0003 Update push readiness audit` | Records final push-readiness audit before P155/P156 governance work. | high | `false` | Medium; "ready" could be mistaken for rebuild approval. | Accept as pre-lineage push-readiness milestone only. |
| `milestone-p155-lineage-governance` | `eb871fc Add lineage branch governance RFC` | Adds the lineage, branch, tag, checkpoint, sandbox, quarantine, recovery, and selected-return governance RFC. | high | `false` | Low; governance RFC might be mistaken for Git execution approval. | Accept as lineage-governance milestone. |
| `milestone-p156-baseline-tagging-plan` | `6e7639a Add baseline tagging plan` | Adds the candidate tag/branch plan and manual command drafts without execution. | high | `false` | Low; command drafts may be mistaken for commands already run. | Accept as planning milestone. |

## Branch Review

| Branch | Candidate Fork Point | Reason | Confidence | needs_founder_confirmation | Risk | Recommendation |
|---|---|---|---|---|---|---|
| `core/baseline` | `core-v0-baseline` after founder chooses `83bede1` or `5e5fe21` | Stable reference for earliest local Core lineage. | medium | `true` | Wrong fork point weakens original Core reference. | Wait for founder baseline decision; keep read-only reference. |
| `core/pre-rebuild-ready` | `core-v1-pre-rebuild-ready` after founder confirms P155 vs P156 | Protected reference for accepted pre-rebuild state. | high | `true` | Branch name can look like rebuild approval. | Create only after final main push and founder confirmation. |
| `instance/01-local-rebuild-trial` | confirmed `core-v1-pre-rebuild-ready` | Local sandbox for future rebuild trial. | high | `true` | Accidentally starting rebuild or merging sandbox output. | Create only after tags, final push, clean tests, and explicit rebuild-trial approval. |
| `instance/01-astrbot-shadow` | confirmed `core-v1-pre-rebuild-ready` | Future shadow line for AstrBot-shaped input observation. | medium | `true` | Adapter context can contaminate identity. | Delay until adapter-shadow work is explicitly approved. |
| `instance/01-synthetic-history-v1` | confirmed `core-v1-pre-rebuild-ready` | Sandbox for synthetic-history experiments. | medium | `true` | Synthetic autobiography may be mistaken for Core history. | Delay unless synthetic-history work is explicitly approved. |
| `research/synthetic-history-accelerator` | confirmed `core-v1-pre-rebuild-ready` or `milestone-p155-lineage-governance` | Research line for synthetic-history acceleration theory. | medium | `true` | Research branch may drift into instance autobiography. | Delay; return only RFCs, tests, reports, or boundary improvements. |
| `research/ctm-temporal-dynamics` | confirmed `core-v1-pre-rebuild-ready` or `milestone-p155-lineage-governance` | Research line for symbolic CTM-inspired temporal dynamics. | medium | `true` | CTM vocabulary may be mistaken for CTM runtime. | Delay until a specific CTM research task is approved. |
| `research/tool-first-evolution` | confirmed `core-v1-pre-rebuild-ready` or `milestone-p155-lineage-governance` | Research line for capability-evidence and tool-first evolution policy. | medium | `true` | Capability work may slide into tool execution or tool trust. | Delay; return only reviewed evidence schemas, policies, reports, or tests. |
| `quarantine/imported-astrbot-memory` | confirmed `core-v1-pre-rebuild-ready` | Containment line for future imported AstrBot or Angel Memory material. | high | `true` | Imported memory can look like native Core history. | Create only when import review begins; never direct-merge. |
| `quarantine/llm-self-claims` | confirmed `core-v1-pre-rebuild-ready` | Containment line for model self-claims or contaminated autobiographical output. | high | `true` | Model self-claims can contaminate identity. | Create only when such material exists; never direct-merge. |

## Founder Decision Summary

Founder confirmation is still required for:

- choosing `core-v0-baseline`: `83bede1` vs `5e5fe21`;
- choosing `core-v1-pre-rebuild-ready`: `eb871fc` vs `6e7639a`;
- deciding whether to create all proposed tags now or only the four safest
  milestone tags;
- deciding whether to create only `core/*` branches now and defer
  `instance/*`, `research/*`, and `quarantine/*` branches until work begins;
- allowing any future local rebuild trial branch to exist.

Recommended safest sequence:

1. finish P158 manual command sheet;
2. finish P159 final push-readiness audit;
3. push current `main` to GitHub in P160 if checks pass;
4. founder manually confirms tag decisions;
5. only then create tags/branches in a separate manual operation.

## Non-Execution Statement

P157 does not:

- create git tags;
- create git branches;
- push;
- push tags;
- start rebuild;
- read old 01;
- connect AstrBot, adapters, Web, or Companion;
- write formal state, event, memory, or recall records;
- mutate Identity Core;
- execute growth, tool, temporal, CTM, or policy runtime.
