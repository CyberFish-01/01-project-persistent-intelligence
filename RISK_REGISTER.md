# Risk Register

Chinese version: [RISK_REGISTER_ZH.md](./RISK_REGISTER_ZH.md)

Status: `document-only`, `risk-register`, `non-runtime`.

P72 records foundation risks after P71. It does not add runtime behavior,
schemas, CLI commands, validation rules, policy executors, reducers, payload
capture, identity mutation, memory rewrite, adapters, UI, or product behavior.

## Register Rule

```text
risk visibility is not risk automation.
mitigation guidance is not policy execution.
blocked runtime work remains blocked.
```

This register exists to keep the foundation layer honest while P68-P80 continue
low-risk consolidation.

## Risk Levels

- `high`: can undermine the foundation thesis or create unsafe implementation
  pressure.
- `medium`: can confuse ownership, documentation, or future sequencing.
- `low`: should be watched, but does not currently threaten the foundation.

## Active Foundation Risks

| ID | Risk | Level | Trigger Signal | Mitigation | Blocked Action |
|---|---|---|---|---|---|
| R1 | Concept inflation | high | new named concepts are added faster than ownership boundaries | prefer updates to [CONCEPT_MAP.md](./CONCEPT_MAP.md), [RFC_INDEX.md](./RFC_INDEX.md), or this register before creating a new surface | adding new runtime capability to justify a concept |
| R2 | Review layer over review layer | high | a review object needs another review object before it can be understood | consolidate into [GOVERNANCE Surface](./CONCEPT_MAP.md) language or defer | policy executor, growth engine |
| R3 | Reports outnumber mechanisms | medium | documentation expands but future implementation contracts remain vague | keep reports tied to open questions, contracts, and blocked runtime lists | claiming readiness from reports alone |
| R4 | Growth misunderstood as automatic growth | high | productive drift, meaning shift, or lifecycle labels are treated as promotion | repeat Growth Candidate Review boundary and Identity Gate escalation | growth lifecycle execution, memory promotion |
| R5 | Temporal Awareness implemented too early | high | elapsed-time vocabulary is treated as event schema or salience mutation | keep [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) future-only until write policy and validation exist | temporal runtime, temporal event execution |
| R6 | Recall retrieval becomes write path | high | ordinary retrieval, similarity search, or context fill writes durable events | enforce [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) rule: ordinary recall is not a write | recall event writes |
| R7 | Memory rewrite pressure | high | missing encoding context is "fixed" by editing memory | use [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md): insufficient context is the safe output | memory rewrite |
| R8 | Reconstruction readiness mistaken for reconstruction | high | evidence reports or reducer contracts are treated as rebuild execution | keep reducer contract, capture policy, and execution separate | reducer execution, state rebuild |
| R9 | Payload capture slips into schema mutation | high | capture policy recommendations are implemented as event fields without review | require privacy, schema, compatibility, and validation review first | payload capture, event schema mutation |
| R10 | Identity boundary dilution | high | Subject Kernel, World Seed, memory, or product context start acting as identity | keep Identity Core high-gated and Subject Kernel / World Seed conceptual | Identity Core rewrite |
| R11 | Companion/social layer arrives early | high | exploration, relationship silence, or product language becomes companion behavior | keep exploration record-only or review-only; push relationship memory back | companion, relationship memory, UI/product behavior |
| R12 | Adapter or platform owns identity | high | AstrBot, adapter metadata, or platform sessions imply identity updates | preserve "01 Core owns state; adapters translate" | adapter integration required, platform-owned identity |
| R13 | Event audit trail weakened | high | retention review, capture policy, or reconstruction suggests compaction/rewrite | keep Event Log append-only; use reports and references instead | event compaction, event rewrite |
| R14 | Governance Surface becomes too broad | medium | every task, claim, or memory review is routed to governance | use ownership boundaries: Task Hub owns work, Claim Graph owns claims, Memory Layer owns records | centralizing all review semantics |
| R15 | Bilingual drift | medium | Chinese and English docs diverge on status or blocked actions | use [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md), run consistency passes, and prefer paired edits | treating one language as authoritative when contradictory |
| R16 | README entrance overload | medium | new readers cannot find stable foundation vs future-only work | optimize README entrance and index docs without adding features | productizing the README |
| R17 | P80 pressure | medium | phases are opened just to advance numbering | use [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md) as the stop condition; skip, merge, or stop if a phase does not add clarity | opening empty phases |
| R18 | Cloud/AstrBot deployment pressure | medium | local foundation docs are treated as a reason to update cloud or AstrBot now | keep cloud and AstrBot pushed back until foundation loop ends | cloud runtime rollout, AstrBot specialization |

## Risk Clusters

### Foundation Semantics

Risks: R1, R2, R3, R14, R17.

Primary control: keep [PHASE_INDEX.md](./PHASE_INDEX.md),
[CONCEPT_MAP.md](./CONCEPT_MAP.md), [RFC_INDEX.md](./RFC_INDEX.md), and
[OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) aligned. Do not create a new concept
unless it reduces ambiguity.

### Memory And Growth

Risks: R4, R6, R7.

Primary control: keep Stateful Memory, Meaning Shift, Productive Drift, Growth
Candidate Review, and Growth Candidate Lifecycle separate. Review objects do
not execute subject-state transition.

### Time And Exploration

Risks: R5, R11.

Primary control: Temporal Awareness and Exploration / Serendipity remain
future-only, review-only, and non-product until later explicit implementation
contracts exist.

### Reconstruction And Events

Risks: R8, R9, R13.

Primary control: Reconstruction Evidence is not reconstruction. Reducer
Contract is not reducer execution. Capture Policy is not payload capture. Event
Log remains append-only.

### Identity And Platform Boundary

Risks: R10, R12, R18.

Primary control: Identity Core stays high-gated. Subject Kernel / World Seed
remain conceptual. Platforms and adapters translate; they do not own identity.

### Documentation Operations

Risks: R15, R16.

Primary control: keep bilingual docs synchronized, reduce README overload, and
make stable/future/blocked status visible through indexes.

## Immediate Watch Items For P73-P80

- P73 Architecture Boundary Refresh should update older P53 boundary language
  with P58-P72 artifacts.
- P74 Glossary Deduplication should reduce term drift around growth, drift,
  lifecycle, recall, temporal awareness, reducer, and capture.
- P75 README Entrance Optimization should make foundation, RFCs, and blocked
  runtime work easier to scan.
- P76 Foundation Review Checklist should convert this register into a manual
  review checklist, not an automated executor.

## Non-Execution Statement

P72 does not implement:

- risk automation;
- policy execution;
- Temporal Awareness runtime;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, or product layer.
