# Minimal Observatory CLI Plan

Chinese version: [MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md](./MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md)

Status: `P95`, `planning`, `RFC-only`, `document-only`, `non-runtime`.

P95 plans a possible minimal read-only CLI report for the Foundation
Observatory. It does not implement a CLI, parser, command, generator, dashboard,
Web UI, status API, product surface, runtime monitor, or executor.

## Problem Statement

P94 created [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md),
a hand-maintained Markdown observatory report for founder-facing visibility.
That report is useful because it shows the current 01 Core foundation without
asking the founder or CTO to read every RFC.

The next possible need is automatic generation: a future command could read
foundation documents and produce the same kinds of sections consistently.

This should not become a Web UI, dashboard runtime, product UI, or observability
executor. The minimal CLI exists only to provide founder / CTO visibility over
documents, readiness, boundaries, risks, and next-step recommendations.

## Proposed CLI

Candidate command:

```text
foundation-observatory-report
```

Optional subviews:

| Subview | Purpose | Boundary |
|---|---|---|
| `phase-map-view` | Show phase index and main-line grouping. | Reads phase docs only; does not create phases. |
| `readiness-matrix-view` | Show module readiness categories and next actions. | Reports readiness; does not authorize implementation. |
| `boundary-status-view` | Show disabled, forbidden, RFC-only, and future boundaries. | Reports boundaries; does not enforce policy. |
| `risk-heatmap-view` | Show concentrated foundation risks. | Reports risk; does not execute mitigation. |
| `next-step-recommendation-view` | Show ranked future directions. | Suggests review choices; does not start P96 or any phase. |

The default future output should be one complete Markdown report, not an
interactive dashboard.

## Inputs

Future CLI input should be limited to existing documents and static state
references. It must not call adapters, remote services, model APIs, live chat
surfaces, or mutable runtime commands.

| Input | Use | Boundary |
|---|---|---|
| [PHASE_INDEX.md](./PHASE_INDEX.md) / [ZH](./PHASE_INDEX_ZH.md) | Phase map and current phase coverage. | Read-only. |
| [CONCEPT_MAP.md](./CONCEPT_MAP.md) / [ZH](./CONCEPT_MAP_ZH.md) | Concept relationships and ownership. | Read-only. |
| [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) / [ZH](./FOUNDATION_STATUS_ZH.md) | Stable, exploratory, missing, and pushed-back foundation state. | Read-only. |
| [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) / [ZH](./OPEN_QUESTIONS_ZH.md) | Open questions, blocked work, and future contracts. | Read-only. |
| [RISK_REGISTER.md](./RISK_REGISTER.md) / [ZH](./RISK_REGISTER_ZH.md) | Risk categories and mitigations. | Read-only. |
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) / [ZH](./ARCHITECTURE_BOUNDARIES_ZH.md) | Forbidden boundaries and layer ownership. | Read-only. |
| [RFC_INDEX.md](./RFC_INDEX.md) / [ZH](./RFC_INDEX_ZH.md) | Indexed RFC, policy, report, and review artifacts. | Read-only. |
| [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) / [ZH](./VISUAL_NAMING_GUIDE_ZH.md) | Chinese display names and English `internal_key` mapping. | Read-only. |
| [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) / [ZH](./FOUNDATION_OBSERVATORY_REPORT_ZH.md) | Current hand-maintained report template and baseline. | Read-only. |

Any future implementation may also read static local state summaries only if the
contract states which files are read and proves no writes occur.

## Outputs

Future CLI output should be deterministic Markdown or JSON-like structured
report data with these sections:

| Output Section | Meaning | Boundary |
|---|---|---|
| `founder_snapshot` | Short founder / CTO summary of current 01 Core state. | Summary, not release claim. |
| `main_axes_map` | Founder-facing map of continuity, growth, temporal, capability, interaction, and observability axes. | Report grouping, not runtime architecture. |
| `readiness_matrix` | Module readiness and next action table. | Readiness is not authorization. |
| `boundary_status` | Disabled, forbidden, RFC-only, and future boundaries. | Boundary report is not enforcement. |
| `risk_heatmap` | High-risk areas and mitigations. | Risk report is not mitigation execution. |
| `next_step_recommendations` | Ranked future options. | Recommendation is not automatic phase creation. |
| `what_not_to_build_yet` | Explicit blocked work list. | Block list is not runtime guard. |

## Readiness Categories

The future CLI should use these categories exactly:

| Category | Meaning |
|---|---|
| `implemented` | A prototype or document-backed mechanism exists today. |
| `report_only` | Visible in reports or reviews, but not an implemented mechanism. |
| `rfc_only` | Defined only as RFC, policy, or planning vocabulary. |
| `evaluation_only` | Designed as evaluation scenarios or signals, not runtime truth. |
| `future_direction` | Useful future direction with missing contracts. |
| `blocked` | Explicitly forbidden until future approval and gates exist. |
| `dangerous_if_early` | Likely to cause boundary drift if built before prerequisites. |

When unsure, the future CLI should choose the lower-maturity category.

## Boundary Status

The future CLI must at least report:

| Boundary | Future CLI Status Vocabulary | Required Interpretation |
|---|---|---|
| identity mutation | `blocked` / `forbidden` | No automatic Identity Core change. |
| memory rewrite | `blocked` / `forbidden` | No rewriting memories to simulate growth or cleanup. |
| recall event write | `rfc_only` / `disabled` | Ordinary recall is not an event write. |
| growth engine | `blocked` / `forbidden` | Growth candidates do not promote themselves. |
| temporal runtime | `future_direction` / `disabled` | Time remains review evidence, not active runtime. |
| CTM runtime | `blocked` / `forbidden` | CTM is inspiration, not implementation. |
| tool execution | `blocked` / `forbidden` | Tool candidates are not executable tools. |
| tool promotion | `blocked` / `forbidden` | Verification does not imply promotion. |
| policy executor | `blocked` / `forbidden` | Policy language must not execute decisions. |
| companion layer | `future_direction` / `blocked` | Companion behavior stays out of foundation work. |
| UI / AstrBot / adapter | `future_direction` / `blocked` | Platform surfaces must not own identity. |
| reconstruction reducer | `rfc_only` / `disabled` | Reducer contract is not reducer execution. |
| event compaction | `blocked` / `forbidden` | Event history remains auditable. |

## Non-Goals

P95 and any minimal observatory CLI plan do not include:

- Web UI;
- dashboard runtime;
- product UI;
- companion layer;
- automatic roadmap execution;
- automatic next phase creation;
- automatic status mutation;
- identity mutation;
- memory rewrite;
- recall event write;
- growth promotion or growth engine;
- Temporal Awareness runtime;
- CTM runtime;
- tool execution;
- tool promotion;
- policy executor;
- adapter integration;
- reconstruction reducer execution;
- event compaction.

## Implementation Boundary

P95 does not implement the CLI.

P96 may consider a Minimal Observatory CLI Implementation only after explicit
founder approval. The smallest acceptable implementation would be read-only:

- read Markdown and approved static local state summaries;
- emit a Markdown or JSON-like report;
- avoid remote calls, adapters, model APIs, network access, and live runtime
  mutation;
- prove it does not write identity, memory, recall events, growth candidates,
  tools, policy state, reducers, or compacted event history.

If any future implementation needs writes, network, adapters, model calls, or
runtime state mutation, it is no longer a minimal observatory CLI.

## Risks

| Risk | Level | Why It Matters | Mitigation |
|---|---|---|---|
| observability becoming product UI | High | A founder report can drift into dashboard/product work. | Keep P95 RFC-only and any P96 candidate read-only. |
| report becoming decision executor | High | Ranked recommendations can be mistaken for commands. | Recommendation output must not create phases or tasks. |
| stale document inputs | Medium | Generated reports may repeat outdated source documents. | Show source file timestamps or phase coverage in future design. |
| false readiness signal | High | A clean table can make RFC-only concepts look safe. | Use conservative readiness categories and blocked labels. |
| overconfidence from dashboard | High | Visual summaries can hide uncertainty. | Include risk and missing-contract fields in every view. |
| hiding complexity behind simplified labels | Medium | Founder-facing names may flatten technical nuance. | Preserve English `internal_key` and source links. |

## P96 Candidate

Possible P96 directions, not executed by P95:

1. Minimal Observatory CLI Implementation.
2. Readiness Matrix Static Generator.
3. Boundary Status Static Generator.
4. Founder Snapshot Generator.

Recommended order: start with a read-only Minimal Observatory CLI
Implementation only if the founder explicitly approves moving from plan to
implementation. Otherwise pause for founder / CTO review.

## Non-Execution Statement

This plan is an RFC-only planning artifact. It does not add commands, modules,
schemas, tests, parsers, generated files, dashboards, Web UI, adapters, runtime
behavior, policy execution, identity mutation, memory rewrite, recall writes,
growth execution, tool execution, reconstruction reducers, event compaction, or
P96 implementation.
