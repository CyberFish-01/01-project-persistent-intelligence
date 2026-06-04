# Review Queue Preview RFC

Chinese version: [REVIEW_QUEUE_PREVIEW_RFC_ZH.md](./REVIEW_QUEUE_PREVIEW_RFC_ZH.md)

Status: `document-only`, `RFC-only`, `non-runtime`.

P88 defines a future review queue preview surface for a thin interaction
harness. It does not implement a queue, lifecycle execution, policy execution,
candidate promotion, claim revision, task closure, recall event writes,
temporal event writes, trace storage, context building, identity mutation,
memory rewrite, UI, AstrBot, adapter, companion, cloud, or product behavior.

## RFC Rule

```text
a review queue preview organizes review pressure.
a review queue preview is not a lifecycle engine.
a review queue preview is not approval.
a review queue preview is not mutation.
```

## Problem

P85-P87 defined a future harness boundary, conversation intake envelope, and
context package preview. Once those surfaces exist conceptually, the next
question is what review objects a harness may show and how they should be
ordered.

The danger is that a "queue" sounds executable. P88 keeps queue language
preview-only: it may explain candidate type, risk, review depth, evidence, and
blocked boundaries, but it must not perform candidate lifecycle actions or
change subject state.

## Preview Scope

P88 covers future preview vocabulary for:

- candidate type;
- source references;
- evidence references;
- risk level;
- review depth;
- boundary flags;
- blocked reason;
- unresolved questions;
- recommended review route;
- preview ordering reason.

P88 does not cover:

- lifecycle execution;
- durable queue persistence;
- automatic approval;
- policy execution;
- state mutation;
- event writes;
- prompt or model behavior.

## Future Preview Shape

This is vocabulary only, not a schema and not implemented.

```text
review_queue_preview:
  queue_preview_id
  intake_ref
  context_preview_ref
  candidate_previews
  ordering_policy_note
  blocked_items
  unresolved_questions
  non_execution_boundary
```

```text
candidate_preview:
  candidate_ref
  candidate_type
  source_refs
  evidence_refs
  risk_level
  review_depth
  boundary_flags
  blocked_reason
  suggested_route
  preview_status
```

## Candidate Types

| Candidate Type | What It Previews | Suggested Route | Explicitly Not |
|---|---|---|---|
| `memory_candidate` | possible memory review, provenance concern, archive/quarantine question | Memory Layer review | memory promotion or rewrite |
| `claim_candidate` | support, contradiction, uncertainty, repair need | Claim Graph review | claim auto-revision |
| `growth_candidate` | evidence-backed possible meaning-bearing transition | Growth Candidate Review | growth promotion |
| `meaning_shift_candidate` | reinforced, weakened, reinterpreted, or conflicted memory meaning | Stateful Memory review | recall write or memory rewrite |
| `recall_candidate` | review-worthy recall question under P59 thresholds | Recall Event Write Policy review | recall event write |
| `task_candidate` | active task, blocker, procedural or cautionary work item | Task Hub review | task auto-closure or workflow execution |
| `governance_candidate` | boundary, policy, RFC, risk, or review object | Governance Surface | policy executor |
| `identity_candidate` | identity-adjacent pressure or anchor question | Identity Gate | Identity Core mutation |
| `temporal_candidate` | delayed alignment, unresolved tension, stale context | future Temporal Awareness review | temporal event write |
| `trace_candidate` | public review summary storage question | Thought Trace Storage Policy review | hidden reasoning storage |

## Ordering Signals

Future preview ordering may consider:

- identity pressure;
- privacy or cross-user risk;
- prompt contamination risk;
- evidence strength;
- unresolved tension;
- review depth;
- blocked boundary severity;
- task urgency;
- stale context;
- missing provenance.

Ordering is not execution priority. A high-ranked item does not become approved,
stored, promoted, or written.

## Review Depth Boundary

P83 defines review depth as planning vocabulary. P88 may display:

- `shallow`;
- `normal`;
- `deep`;
- `blocked`.

It must not execute deliberation ticks, thought loops, policy, lifecycle, or
approval. `blocked` means do not execute; it is not a request to implement a
guardrail.

## Blocked Items

A preview should mark an item as blocked when it requests or implies:

- identity mutation;
- memory rewrite;
- recall event write;
- temporal event write;
- growth lifecycle execution;
- policy executor;
- reconstruction reducer execution;
- event compaction;
- hidden chain-of-thought capture;
- adapter integration;
- UI, companion, or product behavior.

Blocked items may remain visible as audit and planning objects. They must not be
converted into execution tasks by the queue.

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | P88 defines the review queue surface inside the future harness boundary. |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | Context gaps or selected refs may feed candidate previews. |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | Supplies review depth vocabulary without tick execution. |
| [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | Keeps lifecycle labels separate from queue preview. |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | Supplies drift and collapse rejection reasons. |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | Keeps recall candidates separate from recall writes. |
| [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | Keeps trace candidates separate from hidden reasoning storage. |
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | Defines which owner should review each candidate class. |

## Open Questions

- Should queue previews be sorted by risk, age, evidence strength, or owner
  boundary?
- Should blocked candidates remain visible or be separated into a blocked view?
- Can review queue preview be stored as a report without becoming lifecycle
  history?
- Should context gaps create queue candidates automatically in a future harness,
  or only when explicitly requested?
- How should identity-adjacent items route to Identity Gate without mutation
  pressure?
- How should low-risk items avoid review overload?

## P89 Candidate Direction

P89 may define Session Resume Scenario Plan. It should simulate minutes, hours,
days, unresolved tasks, stale claims, stale memories, pending review candidates,
and context gaps without writing temporal events or executing Temporal
Awareness runtime.

## P88 Non-Execution Statement

P88 does not implement:

- review queue runtime;
- queue storage;
- lifecycle execution;
- growth promotion;
- candidate approval;
- policy execution;
- context builder execution;
- retrieval execution;
- API route;
- CLI command;
- model prompting;
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
- identity mutation;
- memory rewrite;
- claim auto-revision;
- task auto-closure;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
