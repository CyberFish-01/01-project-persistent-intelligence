# Architecture Boundaries

Chinese version: [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md)

P53 records architecture boundaries after P51. These boundaries protect the
foundation from concept collapse and premature product expansion.

## Identity Core Boundary

Identity Core should not be automatically mutated.

Allowed:

- high-gate review;
- evidence-backed identity memory append;
- explicit audit and rollback metadata.

Forbidden unless a future phase explicitly changes it:

- direct Identity Core rewrite;
- adapter-driven identity change;
- Dream-driven identity mutation;
- growth-candidate-driven identity mutation.

## Memory Layer Boundary

Memory Layer should not absorb Stateful Memory semantics.

Memory Layer owns records, provenance, lifecycle, sensitivity, and retrieval
eligibility. Stateful Memory is a semantic interpretation model:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

Do not turn every semantic concept into a memory store.

## Claim Graph Boundary

Claim Graph should not absorb all meaning shift.

Claim Graph owns claim-shaped evidence, contradiction, support, and revision.
Meaning shifts belong in Claim Graph only when they produce or revise explicit
claims.

## Task Hub Boundary

Task Hub should not absorb all governance review.

Task Hub owns operational continuity: tasks, procedural memory, reflections,
warnings, queues, and reviewed work records. Cross-layer review objects should
live in Governance Surface when they reference multiple layers.

## Governance Surface Boundary

Governance Surface owns cross-layer review objects.

Examples:

- growth candidate review;
- reconstruction schema review material;
- evidence request governance;
- review-only policy proposal objects.

Governance Surface should not become a policy executor or growth engine.

## Temporal Awareness Boundary

Temporal Awareness remains a future direction.

Principle:

```text
time is not only metadata.
time is part of subject state transition.
```

P53 does not implement elapsed-time runtime, temporal events, temporal salience,
or temporal growth candidates.

## Product Boundary

Companion, relationship memory, social layer, UI, AstrBot specialization, and
adapter expansion remain pushed back.

The current project center is foundation continuity:

- identity protection;
- state transfer;
- audit/replay;
- reconstruction readiness;
- review-only growth semantics.
