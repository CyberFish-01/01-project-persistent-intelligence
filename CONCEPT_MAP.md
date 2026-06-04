# Concept Map

Chinese version: [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md)

P70 updates the P53 foundation concept map with P58-P68 consolidation artifacts.
The map is descriptive: it does not define new runtime behavior, schemas,
execution paths, lifecycle engines, reducers, payload capture, adapters, UI, or
product surfaces.

## Core Flow

```text
Identity Core
  protected by Identity Gate
  informed by Claim Graph, Identity Memory, and Growth Candidate Review
  never automatically mutated

State Transfer
  carried by StateStore, Context Builder, and Event Log
  stronger than memory retrieval

Event Log -> Replay -> Reconstruction Evidence
  Event Log records transitions
  Replay validates transition projection
  Reconstruction Evidence records what payload/diff/schema proof is missing

Memory Layer -> Stateful Memory -> Meaning Shift
  Memory Layer stores records and lifecycle status
  Stateful Memory interprets memory as event + encoding_state + recall_state + meaning_shift
  Meaning Shift is reviewable only when evidence-backed

Productive Drift -> Growth Candidate Review -> Governance Surface
  Productive Drift can create a review candidate
  Growth Candidate Review is not growth
  Governance Surface owns cross-layer review objects

Temporal Awareness
  future direction only
  time is not only metadata
  time is part of subject state transition
```

## P58-P68 Consolidation Flow

```text
Open Questions Triage -> RFC Index -> Foundation Roadmap
  triage selects safe document-only work
  RFC Index prevents review artifacts from becoming execution approval
  Foundation Roadmap keeps runtime work blocked until explicit implementation

Temporal Awareness -> Recall Event Write Policy -> Stateful Memory Encoding Policy
  Temporal Awareness asks how elapsed time may become subject-state evidence
  Recall Event Write Policy blocks ordinary retrieval from durable writes
  Encoding Policy defines minimum provenance before meaning-shift review

Productive Drift -> Growth Candidate Lifecycle -> Governance Surface
  Productive Drift is evidence to review
  Growth Candidate Lifecycle manages review-object state only
  Governance Surface keeps cross-layer review separate from execution

Exploration / Serendipity -> Subject Kernel / World Seed -> Identity Gate
  Exploration may create weak questions or signals
  Subject Kernel protects the subject anchor
  World Seed orients the subject without becoming identity

Reconstruction Evidence -> Reducer Contract -> Payload / Diff Capture Policy
  Reconstruction Evidence names missing proof
  Reducer Contract defines future execution requirements without executing
  Capture Policy classifies target paths without capturing payloads
```

## Concept Roles

### Identity Core

The protected identity anchor. It should remain small and high-gated. It can be
informed by reviewed evidence, but it should not be directly rewritten by Dream,
adapter input, recall, growth candidates, or ordinary memory updates.

### State Transfer

The central continuity mechanism. State transfer means the next run receives a
structured state package rather than merely retrieving similar text.

### Claim Graph

The evidence and belief-revision layer. It manages claims, support,
contradiction, provenance, and reviewable repair. It should not absorb every
meaning shift; only claim-shaped shifts belong here.

### Task Hub

The operational continuity layer. It tracks tasks, procedural memory,
reflection, cautionary warnings, and review queues. It should not become the
owner of every governance object.

### Dream

The offline consolidation engine. Dream can propose semantic candidates,
procedural candidates, conflicts, and review material. Dream does not directly
mutate Identity Core.

### Event Log

The append-only audit ledger for state transitions. It is not a second copy of
state; it is the basis for replay and future reconstruction.

### Replay

The local proof that event records can explain state transitions. Current replay
supports transition projection and readiness assessment, not full object-level
state rebuild.

### Reconstruction Evidence

The vocabulary and governance surface for future reconstruction readiness:
payload coverage, object diffs, rollback snapshots, seed/pre-event references,
and evidence requests.

### Stateful Memory

The semantic model introduced by P50:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

It is not a new memory store. It is a way to reason about why the same memory can
mean something different under a different recall state.

### Meaning Shift

The interpretive delta between encoded memory and recalled memory. P51 requires
evidence for reinforced, weakened, reinterpreted, or conflicted shifts. Without
evidence, the shift is random drift or insufficient context.

### Productive Drift

A bounded, evidence-backed drift category that may deserve review. Productive
drift is not automatically good and does not automatically become growth.

### Growth Candidate Review

A review-only governance object for possible meaning-bearing state transition.
It references memory, claim, task, and event evidence. It does not promote
memory, rewrite identity, write recall events, or execute a growth engine.

### Governance Surface

The cross-layer review surface for objects that reference several foundation
layers. It should own review objects that do not belong cleanly inside Memory
Layer, Claim Graph, Task Hub, or Identity Gate.

### Temporal Awareness

A future direction. It asks how elapsed time affects recall, salience, staleness,
resumed sessions, and meaning shift. P58 records this as an RFC-level future
direction. Temporal Awareness remains separate from ordinary event metadata
until a later accepted contract says otherwise.

### Recall Event Write Policy

The future policy boundary for when meaning-shifting recall might become a
durable event candidate. It blocks ordinary retrieval, ordinary recall, temporal
gap alone, adapter requests, and vague salience from becoming writes.

### Stateful Memory Encoding Policy

The minimum provenance policy for reviewing stateful memory. It says missing
encoding context weakens interpretation and produces insufficient context; it
does not authorize repair by memory rewrite.

### Growth Candidate Lifecycle

A future review-object housekeeping vocabulary for `open`, `deferred`,
`archived`, `quarantined`, and similar states. It manages review object state,
not subject state, memory promotion, or growth execution.

### Productive Drift vs Collapse

The boundary vocabulary that separates bounded, evidence-backed drift from
random drift, identity-threatening drift, and collapse. It is not an automatic
classifier.

### Exploration / Serendipity

A future-only source of weak questions, adjacent connections, evidence gaps, or
review prompts. It must remain record-only or review-only and must not become
companion behavior, product engagement, or identity invention.

### Subject Kernel / World Seed

A future boundary inside Identity Seed. Subject Kernel names the protected
minimal subject anchor. World Seed names the initial world and project
orientation. Neither is a runtime mutation path.

### Reconstruction Reducer Contract

A future contract surface for possible reconstruction reducers. It defines what
a reducer would need before execution can be considered, but it does not rebuild
state or execute reducers.

### Payload / Diff Capture Policy

The target-path policy vocabulary for future payload, diff, snapshot, and
reference-only treatment. It classifies what evidence may be needed; it does not
capture payloads, mutate event schemas, or compact events.

### RFC Index

The navigation and boundary artifact for RFC, policy, review, audit, and matrix
documents. It answers where vocabulary lives and which action remains blocked.
It does not change architecture.

## Ownership Boundaries

| Concept | Owns | Must Not Absorb |
|---|---|---|
| Identity Core | protected continuity anchor | automatic mutation, platform identity, relationship persona |
| State Transfer | continuity package across time | similarity retrieval as continuity |
| Event Log | append-only transition audit | event compaction, state clone, memory store |
| Replay | transition projection proof | full object reconstruction |
| Reconstruction Evidence | missing proof vocabulary and gap visibility | reducer execution, payload capture |
| Reducer Contract | future execution requirements | reducer implementation |
| Payload / Diff Capture Policy | target-path evidence policy | schema mutation or payload capture |
| Memory Layer | records, lifecycle, provenance | meaning-shift engine |
| Stateful Memory | encoding/recall/meaning-shift interpretation | new memory store |
| Recall Event Write Policy | future recall-write threshold | ordinary retrieval writes |
| Claim Graph | claim-shaped belief revision | every meaning shift |
| Task Hub | operational work state and queues | every governance object |
| Growth Candidate Review | possible meaning-bearing transition review | growth execution |
| Growth Candidate Lifecycle | review object housekeeping | subject-state transition |
| Governance Surface | cross-layer review objects | executable policy |
| Temporal Awareness | future subjective-time semantics | ordinary timestamp metadata |
| Exploration / Serendipity | weak future signals and questions | companion/product behavior |
| Subject Kernel | protected minimal subject anchor | mutable personality or full biography |
| World Seed | initial project/world orientation | protected identity |
| RFC Index | document navigation and boundary visibility | implementation approval |

## Stable Non-Execution Reading

The concept map should be read as a boundary map:

- review vocabulary is not runtime capability;
- lifecycle vocabulary is not lifecycle execution;
- policy vocabulary is not policy executor;
- reducer contract is not reducer execution;
- capture policy is not payload capture;
- temporal vocabulary is not Temporal Awareness runtime;
- exploration vocabulary is not companion or product behavior;
- subject/world boundary language is not identity mutation.
