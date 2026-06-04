# Thin Interaction Harness RFC

Chinese version: [THIN_INTERACTION_HARNESS_RFC_ZH.md](./THIN_INTERACTION_HARNESS_RFC_ZH.md)

Status: `document-only`, `RFC-only`, `non-runtime`.

P85 defines the boundary for a possible future thin interaction harness. It does
not implement a harness, CLI command, server, UI, adapter, AstrBot integration,
conversation runtime, context builder, review queue, boundary monitor, recall
event write, temporal event write, thought loop, trace storage, growth
lifecycle, identity mutation, memory rewrite, or product behavior.

## RFC Rule

```text
a thin harness previews interaction surfaces.
a thin harness is not a product.
a thin harness is not an adapter.
a thin harness is not a mutation path.
```

## Problem

P0-P84 built a large foundation: identity boundaries, event sourcing,
reconstruction readiness, stateful memory, growth review, temporal coherence,
review depth, and trace storage boundaries. The next useful step is not a full
runtime or product surface. The next useful step is a small way to reason about
how interaction would touch those foundations.

Without a thin harness boundary, future work may jump straight into companion,
UI, AstrBot, adapter, cloud, or automatic growth behavior. P85 blocks that jump
by defining the harness as a review-only preview surface.

## Harness Definition

A thin interaction harness is a future local testing surface that may preview:

- how a conversation input would be enveloped;
- which identity, memory, claim, task, and governance references would be
  selected for context;
- which review candidates might be shown;
- which review queue entries might need attention;
- how a session resume scenario might be simulated;
- which forbidden boundaries would block execution.

It does not own identity, store memory, write events, mutate state, execute
policy, or integrate a platform.

## Proposed Future Surfaces

These surfaces are RFC targets only. They are not implemented in P85.

| Surface | Future Purpose | Preview Output | Explicitly Not |
|---|---|---|---|
| `conversation_intake` | Define the input envelope for a user/session message. | normalized envelope preview, source refs, privacy flags | adapter ingestion, platform identity, durable event write |
| `context_package_preview` | Explain which state references would be offered to a model. | selected refs, reasons, omitted refs, token budget | memory retrieval as continuity, context mutation |
| `candidate_preview` | Show possible review objects raised by interaction. | memory/claim/growth/meaning-shift/task candidate previews | growth lifecycle, claim revision, memory rewrite |
| `review_queue_preview` | Show review ordering and blocked items. | queue preview, review depth, boundary flags | lifecycle execution or policy executor |
| `session_resume_scenario` | Simulate resuming after minutes, hours, or days. | stale refs, context gaps, unresolved questions | Temporal Awareness runtime or temporal event write |
| `boundary_monitor_preview` | Explain why an action is blocked or deferred. | boundary reason, related artifact, safe next document | runtime enforcement or product guardrail |

## Allowed Future Harness Output

A future harness may be allowed to output:

- preview envelopes;
- selected reference lists;
- omission reasons;
- review-depth recommendations;
- candidate previews;
- boundary flags;
- unresolved questions;
- deterministic scenario reports;
- "blocked", "defer", or "needs review" labels.

## Forbidden Harness Output

A future harness must not output as execution:

- identity update;
- memory rewrite;
- recall event write;
- temporal event write;
- growth promotion;
- claim auto-revision;
- task auto-closure;
- thought loop execution;
- hidden chain-of-thought capture;
- trace storage;
- reconstruction reducer execution;
- event compaction;
- adapter action;
- UI or companion behavior.

## Minimal Future Flow

This is a conceptual flow, not implementation.

```text
conversation input
  -> conversation_intake preview
  -> context_package_preview
  -> candidate_preview
  -> review_queue_preview
  -> boundary_monitor_preview
  -> no mutation unless a future approved phase creates explicit contracts
```

The flow is intentionally preview-only. It is useful only if every step can
explain what it would do without doing it.

## Boundary Ownership

| Boundary | Owner | Harness Behavior |
|---|---|---|
| Identity | Identity Core / Identity Gate | may reference anchors; must not mutate them |
| Memory | Memory Layer / Stateful Memory | may preview refs and meaning-shift candidates; must not rewrite records |
| Claims | Claim Graph | may preview conflicts; must not auto-revise claims |
| Tasks | Task Hub | may preview operational context; must not close tasks |
| Growth | Growth Candidate Review | may preview candidates; must not execute lifecycle or promotion |
| Time | Temporal Awareness RFC | may simulate elapsed-time scenarios; must not write temporal events |
| Traces | Thought Trace Storage Policy | may explain review summaries; must not store hidden reasoning |
| Platforms | Adapter Protocol | may include source refs; must not integrate adapters or own identity |

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | Defines the owner boundaries the harness must preserve. |
| [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | Provides forbidden outputs the harness must surface as blocked. |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | Review depth can appear as preview vocabulary only. |
| [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | Prevents harness previews from becoming hidden reasoning storage. |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | Supplies deterministic evaluation scenarios that a later harness may report. |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | Keeps ordinary recall and context preview separate from durable recall writes. |
| [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | Keeps candidate preview separate from lifecycle execution. |

## Open Questions

- Should a first harness be CLI-only, report-only, or fixture-only?
- What is the smallest envelope that proves platform does not own identity?
- Which preview outputs are safe to store, and which must remain ephemeral?
- Should boundary monitor be a report, a checklist, or future validation?
- How can the harness preview context without implying retrieval equals
  continuity?
- How can review queues be previewed without lifecycle execution?

## P86 Candidate Direction

P86 may define the Conversation Intake Contract RFC. It should describe the
input envelope for future harness previews without implementing runtime intake,
adapter ingestion, event writes, or identity ownership by platform.

## P85 Non-Execution Statement

P85 does not implement:

- thin harness runtime;
- CLI commands;
- server routes;
- UI;
- adapter or AstrBot integration;
- conversation ingestion;
- context builder execution;
- review queue execution;
- boundary monitor execution;
- trace storage;
- hidden chain-of-thought capture;
- deliberation tick execution;
- thought loop execution;
- Temporal Awareness runtime;
- CTM runtime;
- model training;
- new dependencies;
- temporal event writes;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- policy execution;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, cloud rollout, or product layer.
