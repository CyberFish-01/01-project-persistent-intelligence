# Decisions Log

Chinese version: [DECISIONS_ZH.md](./DECISIONS_ZH.md)

Status: `document-only`, `decisions-log`, `non-runtime`.

P77 records the foundation decisions that are already stable across P0-P76. It
does not add runtime behavior, approval workflow, schemas, CLI commands,
validators, policy executors, reducers, payload capture, identity mutation,
memory rewrite, adapters, UI, cloud rollout, or product behavior.

## Decision Rule

```text
a decision log records project stance.
a decision log is not an approval engine.
blocked decisions remain blocked until an explicit future implementation phase.
```

Use this document to answer: "What has the project already decided, where is
that decision evidenced, and what must not be inferred from it?"

## Status Legend

- `accepted-foundation`: stable foundation stance.
- `accepted-boundary`: stable ownership or non-execution boundary.
- `deferred-contract`: valid future direction, but contract/gate is missing.
- `blocked-runtime`: implementation is explicitly forbidden in the current
  foundation loop.
- `watch`: important risk or open question that should stay visible.

## Stable Foundation Decisions

| ID | Decision | Status | Evidence | Explicitly Not |
|---|---|---|---|---|
| D01 | Continuity is State Transfer through time, not memory retrieval alone. | `accepted-foundation` | [README.md](./README.md), [FOUNDATION.md](./FOUNDATION.md), [VISION.md](./VISION.md) | retrieval-only continuity |
| D02 | 01 Core owns continuity state; models, platforms, and adapters do not own identity. | `accepted-foundation` | [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md), [ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) | platform-owned identity |
| D03 | Identity Core is protected by gate and must not be automatically mutated. | `accepted-boundary` | [FOUNDATION.md](./FOUNDATION.md), [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | direct identity rewrite |
| D04 | Event Log is append-only audit evidence. | `accepted-boundary` | [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | event rewrite or compaction |
| D05 | Dream proposes; review decides. | `accepted-foundation` | [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md), [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | direct semantic promotion |
| D06 | Review object is not execution. | `accepted-boundary` | [RFC_INDEX.md](./RFC_INDEX.md), [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | policy executor or automatic rollout |
| D07 | Growth candidate is not growth. | `accepted-boundary` | [CONCEPT_MAP.md](./CONCEPT_MAP.md), [GLOSSARY.md](./GLOSSARY.md), [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | memory promotion or growth engine |
| D08 | Reconstruction evidence is not reconstruction. | `accepted-boundary` | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md), [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | reducer execution or state rebuild |
| D09 | Capture policy is not payload capture. | `accepted-boundary` | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md), [RFC_INDEX.md](./RFC_INDEX.md) | event schema mutation |
| D10 | Foundation consolidation should reduce ambiguity before adding power. | `accepted-foundation` | [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md), [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | empty phases or runtime expansion |

## Concept Ownership Decisions

| ID | Decision | Status | Evidence | Explicitly Not |
|---|---|---|---|---|
| D11 | Memory Layer owns memory records, provenance, lifecycle, and retrieval eligibility. | `accepted-boundary` | [CONCEPT_MAP.md](./CONCEPT_MAP.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md), [GLOSSARY.md](./GLOSSARY.md) | meaning-shift engine |
| D12 | Stateful Memory owns meaning-bearing memory semantics. | `accepted-boundary` | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md), [GLOSSARY.md](./GLOSSARY.md) | new memory store |
| D13 | Claim Graph owns claim-shaped belief revision. | `accepted-boundary` | [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | absorbing all meaning shift |
| D14 | Task Hub owns operational continuity, not all governance. | `accepted-boundary` | [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | policy executor |
| D15 | Governance Surface owns cross-layer review objects. | `accepted-boundary` | [CONCEPT_MAP.md](./CONCEPT_MAP.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | growth engine |
| D16 | Subject Kernel and World Seed remain future boundary vocabulary. | `deferred-contract` | [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | runtime split or identity rewrite |

## Deferred Future Directions

| ID | Direction | Status | Required Before Implementation | Explicitly Blocked Now |
|---|---|---|---|---|
| D17 | Temporal Awareness as subject-state transition evidence. | `deferred-contract`, `blocked-runtime` | recall write policy, temporal review placement, elapsed-time evidence rules, validation | Temporal Awareness runtime, temporal event execution |
| D18 | Recall event writes for review-worthy recall. | `deferred-contract`, `blocked-runtime` | accepted event schema, payload/diff policy, privacy, replay interpretation, validation | ordinary recall writes |
| D19 | Growth Candidate Lifecycle as durable review-object history. | `deferred-contract`, `blocked-runtime` | authority model, audit history, Identity Gate escalation, no-execution validation | growth lifecycle execution |
| D20 | Productive Drift vs Random Drift evaluation. | `deferred-contract`, `watch` | evaluation cases, evidence thresholds, collapse recovery boundaries | automatic drift classifier |
| D21 | Exploration / Serendipity signal handling. | `deferred-contract`, `watch` | signal schema, quarantine rules, anti-companion evaluation | exploration engine, companion behavior |
| D22 | Reconstruction Reducer implementation. | `deferred-contract`, `blocked-runtime` | accepted reducer contract, deterministic validation, target-path capture policy | reducer execution, state rebuild |
| D23 | Payload / Diff capture. | `deferred-contract`, `blocked-runtime` | privacy/redaction policy, schema compatibility plan, capture gates | payload capture, event schema mutation |
| D24 | Product, UI, AstrBot specialization, and cloud rollout. | `deferred-contract`, `blocked-runtime` | explicit product-layer phase after foundation loop | productization, adapter integration required |

## Rejected Or Blocked In Current Loop

The following are not accepted decisions in P68-P80:

- identity mutation;
- memory rewrite;
- recall event write;
- growth lifecycle execution;
- Temporal Awareness runtime;
- temporal event execution;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- event compaction;
- policy executor;
- companion, relationship memory, UI, AstrBot, adapter integration, cloud
  rollout, or product layer.

## Decision Review Checklist

Before adding or changing a decision:

1. Link the evidence document.
2. Mark the status as accepted, deferred, blocked, or watch.
3. State what must not be inferred from the decision.
4. Check [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md).
5. Keep the Chinese paired document synchronized.

## P77 Non-Execution Statement

P77 does not implement:

- automated decision workflow;
- approval engine;
- policy executor;
- runtime validation changes;
- Temporal Awareness runtime;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
