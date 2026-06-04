# Core Interaction Harness Roadmap

Chinese version: [CORE_INTERACTION_HARNESS_ROADMAP_ZH.md](./CORE_INTERACTION_HARNESS_ROADMAP_ZH.md)

Status: `document-only`, `roadmap`, `non-runtime`.

P90 assesses whether the foundation is ready to consider a future minimal local
interaction harness. It does not implement a harness, CLI command, API route,
adapter integration, UI, context builder, review queue, temporal runtime,
recall event write, trace storage, thought loop, growth lifecycle, identity
mutation, memory rewrite, cloud rollout, companion layer, or product behavior.

## Roadmap Rule

```text
roadmap is not implementation approval.
minimal harness means preview-only.
preview-only means no writes, no mutation, no lifecycle, no adapter ownership.
```

## Readiness Assessment

P82-P89 created enough document-level contracts to discuss a minimal harness
later:

- P82: temporal coherence evaluation scenarios;
- P83: review depth and deliberation tick vocabulary;
- P84: thought trace storage boundary;
- P85: thin harness boundary;
- P86: conversation intake envelope;
- P87: context package preview;
- P88: review queue preview;
- P89: session resume scenario plan.

This is enough for a roadmap. It is not enough for implementation. The project
still lacks accepted schemas, validation contracts, storage policy, privacy
rules, and explicit approval for runtime work.

## Future Minimal Scope Candidate

If a later implementation phase is explicitly approved, the smallest safe local
CLI harness should be preview-only and fixture-first.

Candidate future commands:

| Candidate Command | Future Purpose | Allowed Output | Explicitly Not |
|---|---|---|---|
| `harness-intake-preview` | Normalize a fixture or stdin input into an intake preview. | envelope preview, privacy flags, boundary flags | adapter ingest, event write |
| `harness-context-preview` | Explain selected and omitted refs from fixture state. | selected refs, omitted refs, reasons, gaps | retrieval as continuity, activation trace write |
| `harness-review-preview` | Show candidate previews and ordering reasons. | candidate type, risk, review depth, blocked reason | lifecycle execution, approval |
| `harness-resume-scenario` | Run deterministic resume scenarios from fixtures. | expected refs, gaps, queue preview labels | Temporal Awareness runtime, temporal event write |
| `harness-boundary-check` | Report blocked outputs for a fixture. | blocked flags and source artifact refs | runtime enforcement, policy executor |

No command is approved by P90. These names are roadmap placeholders only.

## Required Implementation Gates

Before any future harness implementation, a later phase must define:

- exact fixture format;
- whether preview output is ephemeral or report-only;
- privacy and redaction rules;
- local-only execution boundary;
- no-write validation invariants;
- forbidden-output tests;
- bilingual documentation updates;
- commit-by-phase verification;
- explicit statement that adapter/UI/cloud/product work remains out of scope.

## Proposed Future Harness Flow

This is a roadmap sketch, not execution.

```text
fixture or stdin input
  -> intake preview
  -> context preview
  -> review queue preview
  -> optional resume scenario preview
  -> boundary check
  -> no state write
```

The flow must be able to run without accessing live adapters, cloud services,
UI surfaces, or model-internal traces.

## Non-Negotiable Boundaries

A future harness must not:

- write events;
- write episodes;
- update adapter indexes;
- execute retrieval as continuity;
- persist activation traces;
- mutate context;
- write recall events;
- write temporal events;
- store hidden chain-of-thought;
- store thought traces without a future accepted policy;
- execute deliberation ticks or thought loops;
- execute growth lifecycle;
- approve candidates;
- mutate Identity Core;
- rewrite memory;
- revise claims automatically;
- close tasks automatically;
- execute policy;
- execute reconstruction reducers;
- compact events;
- call AstrBot, adapters, UI, cloud, or product layers.

## Roadmap Phases After P90

Candidate future directions only:

1. `P91 Harness Fixture Contract RFC`
   Define local fixture inputs and redaction rules.
2. `P92 Harness Output Contract RFC`
   Define preview-only output sections and no-write invariants.
3. `P93 Harness Boundary Test Plan`
   Define deterministic forbidden-output tests before code.
4. `P94 Minimal CLI Harness Implementation`
   Only if explicitly approved after P91-P93.
5. `P95 Harness Completion Review`
   Audit runtime changes, no-write guarantees, and blocked boundaries.

P90 does not execute these phases.

## What Is Ready

- The conceptual surfaces are separated.
- Adapter ownership is blocked.
- Context preview is separated from continuity.
- Review queue preview is separated from lifecycle.
- Resume scenarios are separated from Temporal Awareness runtime.
- Thought trace storage boundaries are explicit.
- Forbidden outputs are listed and searchable.

## What Is Not Ready

- No fixture schema exists.
- No output contract exists.
- No harness-specific tests exist.
- No privacy/redaction implementation plan exists.
- No approved storage stance exists.
- No CLI implementation approval exists.
- No runtime boundary enforcement exists.
- No guarantee exists that report output is safe to persist.

## Risk Assessment

| Risk | Level | Mitigation Before Implementation |
|---|---|---|
| Harness becomes product | high | keep fixture-first, local-only, no UI |
| Preview becomes write path | high | no-write validation and forbidden-output tests |
| Context preview becomes retrieval continuity | high | mandatory continuity boundary note |
| Review queue becomes lifecycle | high | no approval or lifecycle commands |
| Resume scenarios become Temporal Awareness runtime | high | simulated elapsed time only |
| Trace preview captures hidden reasoning | high | enforce P84 storage boundary |
| Adapter sneaks in through source refs | high | no live adapter calls |
| Reports outnumber mechanisms | medium | require P91-P93 contracts before code |

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | Defines the harness boundary P90 roadmaps. |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | Defines intake preview vocabulary. |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | Defines context preview vocabulary. |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | Defines review queue preview vocabulary. |
| [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) | Defines resume scenarios. |
| [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | Provides the manual gate for any future phase. |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | Lists risks P90 must keep visible. |

## Recommendation

Do not implement the harness yet. The project is ready for a transition summary
and, later, P91-P93 contracts if the founder explicitly wants to move toward a
minimal CLI harness.

The safest next output is a P82-P90 harness transition summary.

## P90 Non-Execution Statement

P90 does not implement:

- harness runtime;
- CLI command;
- API route;
- fixture schema;
- output schema;
- validation tests;
- context builder execution;
- retrieval execution;
- review queue execution;
- session resume runtime;
- Temporal Awareness runtime;
- temporal event writes;
- recall event writes;
- trace storage;
- hidden chain-of-thought capture;
- deliberation tick execution;
- thought loop execution;
- CTM runtime;
- model training;
- new dependencies;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- claim auto-revision;
- task auto-closure;
- policy execution;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
