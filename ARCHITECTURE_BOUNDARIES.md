# Architecture Boundaries

Chinese version: [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md)

Status: `document-only`, `boundary-refresh`, `non-runtime`.

P73 refreshes the P53 architecture boundaries with P58-P72 foundation
artifacts. It does not add runtime behavior, schemas, CLI commands, policy
executors, reducers, payload capture, identity mutation, memory rewrite,
adapters, UI, or product behavior.

## Boundary Rule

```text
ownership prevents concept collapse.
review surfaces are not execution paths.
future vocabulary is not runtime permission.
```

This document should be read with [CONCEPT_MAP.md](./CONCEPT_MAP.md),
[OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md), [RFC_INDEX.md](./RFC_INDEX.md), and
[RISK_REGISTER.md](./RISK_REGISTER.md).

## Boundary Matrix

| Boundary | Owner | Allowed | Forbidden |
|---|---|---|---|
| Identity Core | Identity Gate | high-gate review, evidence-backed identity memory append, audit metadata | direct rewrite, adapter-owned identity, Dream-driven mutation, growth-candidate-driven mutation |
| Subject Kernel | future Identity Seed boundary | protected minimal subject anchor vocabulary | runtime split, mutable personality layer, full biography |
| World Seed | future orientation boundary | project/world orientation vocabulary | protected identity, relationship persona, product positioning |
| Memory Layer | memory storage and lifecycle | records, provenance, sensitivity, retrieval eligibility, archive/quarantine | meaning-shift engine, new store for every semantic concept |
| Stateful Memory | interpretation model | encoding/recall/meaning-shift review vocabulary | memory store, memory rewrite, automatic salience mutation |
| Recall Event Write Policy | future write threshold | review-worthy recall vocabulary and negative cases | ordinary retrieval writes, recall event writes now |
| Claim Graph | claim-shaped belief revision | claims, support, contradiction, provenance, reviewed repair | absorbing every meaning shift |
| Task Hub | operational continuity | tasks, queues, procedural memory, warnings, review work items | owning every governance object or becoming a policy executor |
| Dream | offline proposal engine | candidates, conflicts, review material, provenance | direct semantic promotion, Identity Core mutation |
| Event Log | append-only transition audit | event envelope, sequence, transition reference, replay evidence | event rewrite, compaction, state clone, memory store |
| Replay | transition projection proof | projection, readiness report, rollback preview | full object reconstruction, reducer execution |
| Reconstruction Evidence | reconstruction readiness vocabulary | payload/diff gaps, evidence requests, coverage reports | reconstruction execution, state rebuild |
| Reconstruction Reducer Contract | future reducer contract | input envelope, target path identity, operation semantics vocabulary | reducer implementation or execution |
| Payload / Diff Capture Policy | future target-path evidence policy | reference/payload/diff/snapshot policy vocabulary | payload capture, event schema mutation |
| Growth Candidate Review | cross-layer review object | evidence review for possible meaning-bearing transition | growth, memory promotion, identity mutation |
| Growth Candidate Lifecycle | review-object housekeeping | open/deferred/archived/quarantined/rejected vocabulary | subject-state transition, growth lifecycle execution |
| Productive Drift vs Collapse | drift boundary vocabulary | evidence/risk/rejection categories | automatic classifier, automatic growth |
| Governance Surface | cross-layer review ownership | review objects spanning memory, claim, task, event, identity risk | policy executor, growth engine, all-purpose task hub |
| Temporal Awareness | future subjective-time semantics | elapsed-time research vocabulary and review questions | Temporal Awareness runtime, temporal event execution, salience mutation |
| Exploration / Serendipity | future weak signal boundary | record-only or review-only questions, evidence gaps, adjacent signals | companion behavior, product engagement, identity invention |
| RFC Index | document navigation | vocabulary ownership and blocked-action visibility | implementation approval |
| Risk Register | risk visibility | trigger signals and mitigation guidance | risk automation or policy execution |
| Product / Adapter Layer | pushed-back integration layer | future adapter translation and deployment notes | AstrBot specialization, UI, companion, product ownership of identity |

## Identity And Subject Boundaries

Identity Core remains the protected continuity anchor. Subject Kernel and World
Seed may help future review distinguish subject identity from world orientation,
but they do not create runtime mutation paths.

Forbidden:

- Identity Core rewrite;
- automatic identity mutation;
- Subject Kernel runtime split;
- World Seed becoming identity;
- adapter or platform identity ownership;
- product persona or relationship context becoming identity.

## Memory, Recall, And Meaning Boundaries

Memory Layer stores records. Stateful Memory interprets memory through:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

Recall Event Write Policy remains future-only. Ordinary retrieval is not an
event. Missing encoding context produces insufficient context, not repair by
rewrite.

Forbidden:

- memory rewrite;
- new memory store for each semantic concept;
- ordinary recall writes;
- salience mutation from elapsed time alone;
- imported memory becoming identity memory without review.

## Growth And Drift Boundaries

Growth Candidate Review is a review object. Growth Candidate Lifecycle is
review-object housekeeping. Productive Drift is evidence to review. None of
these execute growth.

Forbidden:

- automatic growth;
- growth lifecycle execution;
- memory promotion from drift;
- identity mutation from growth candidates;
- treating collapse as growth.

## Reconstruction And Event Boundaries

Event Log remains append-only audit evidence. Reconstruction Evidence, Reducer
Contract, and Payload / Diff Capture Policy are ordered review surfaces:

```text
Reconstruction Evidence -> Reducer Contract -> Capture Policy -> future implementation only if approved
```

None of these executes reconstruction or captures payloads.

Forbidden:

- event rewrite or compaction;
- reconstruction reducer execution;
- object-level or full-state rebuild;
- payload capture;
- event schema mutation;
- rollback execution.

## Governance Boundaries

Governance Surface owns cross-layer review objects that do not fit cleanly
inside Memory Layer, Claim Graph, Task Hub, Event Log, or Identity Gate. It must
not become an all-purpose executor.

Allowed:

- review object routing;
- evidence requests;
- status visibility;
- manual review checklists.

Forbidden:

- policy executor;
- automatic growth engine;
- automatic task closure;
- automatic claim revision;
- runtime risk automation.

## Temporal And Exploration Boundaries

Temporal Awareness and Exploration / Serendipity remain future directions.
Elapsed time and weak signals may later provide review evidence only after
explicit contracts exist.

Forbidden:

- Temporal Awareness runtime;
- temporal event execution;
- temporal salience mutation;
- exploration engine;
- companion or relationship behavior;
- roleplay residue becoming life history.

## Product, Adapter, And Deployment Boundaries

Adapters translate platforms. 01 Core owns state. Product and deployment work
remain pushed back during the foundation loop.

Forbidden in P68-P80 consolidation:

- AstrBot specialization;
- UI or product surface;
- companion/social layer;
- cloud rollout justified by foundation docs;
- adapter-required identity update.

## P73 Non-Execution Statement

P73 refreshes boundary documentation only. It does not implement:

- identity mutation;
- memory rewrite;
- recall event write;
- growth lifecycle;
- Temporal Awareness runtime;
- reconstruction reducer execution;
- payload capture;
- event schema mutation;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, or product layer.
