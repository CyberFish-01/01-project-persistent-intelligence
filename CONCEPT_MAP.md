# Concept Map

Chinese version: [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md)

P53 consolidates the foundation concepts that emerged from P0-P51. The map is
descriptive: it does not define new runtime behavior.

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
resumed sessions, and meaning shift. P53 does not implement it.
