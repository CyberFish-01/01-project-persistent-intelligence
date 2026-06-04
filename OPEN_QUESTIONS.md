# Open Questions

Chinese version: [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md)

Status: `document-only`, `status-update`, `non-runtime`.

P71 updates the P53 open questions after P58-P70. Several questions now have
RFC, policy, roadmap, or concept-map artifacts. That means they are clarified,
not implemented, and not closed as runtime capabilities.

## Status Legend

- `rfc-drafted`: a document-only RFC exists.
- `policy-drafted`: a document-only policy exists.
- `indexed`: the question is listed in [RFC_INDEX.md](./RFC_INDEX.md).
- `mapped`: the concept appears in [CONCEPT_MAP.md](./CONCEPT_MAP.md).
- `blocked-runtime`: implementation remains forbidden in the foundation loop.
- `future-contract-needed`: more contract, validation, privacy, or review gates
  are required before implementation can be considered.
- `watch`: important, but not ready for implementation.

## Status Table

| Question | Current Status | Main Artifact | Still Open Because | Forbidden Now |
|---|---|---|---|---|
| Temporal Awareness | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | elapsed-time evidence rules, temporal review placement, and write policy are not accepted runtime contracts | Temporal Awareness runtime, temporal event execution |
| CTM-inspired Temporal Dynamics | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | CTM concepts are translated only as symbolic foundation vocabulary; storage policy, evaluation, and runtime contracts are missing | CTM runtime, model training, temporal event writes |
| Temporal Coherence Evaluation | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | deterministic scenarios and future signals are planned, but no tests or runtime metrics exist | temporal runtime, thought loop execution, event writes |
| Recall Event Write Policy | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | event schema, payload/diff rules, validation invariants, and review gates are missing | recall event writes |
| Stateful Memory Minimal Encoding Policy | `policy-drafted`, `indexed`, `mapped` | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | it defines review quality, but does not add schema fields or a memory store | memory rewrite, new memory store |
| Growth Candidate Lifecycle | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | lifecycle vocabulary remains review-object housekeeping only | lifecycle execution, promotion |
| Productive Drift vs Collapse | `rfc-drafted`, `indexed`, `mapped`, `future-contract-needed` | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | evidence thresholds exist as vocabulary, not classifier or evaluation engine | automatic drift or growth classification |
| Exploration / Serendipity Engine | `rfc-drafted`, `indexed`, `mapped`, `watch` | [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) | future signal schema, quarantine rules, and anti-companion evaluation are missing | exploration engine, companion/product behavior |
| Subject Kernel / World Seed Direction | `rfc-drafted`, `indexed`, `mapped`, `watch` | [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) | identity boundary review and reconstruction path distinction remain future work | Identity Core rewrite, runtime split |
| Reconstruction Reducer Contract | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) | accepted reducer contract, deterministic validation, and target-path capture policy are not implemented | reducer execution, state rebuild |
| Payload / Diff Capture Policy | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | privacy/redaction, schema review, compatibility plan, and capture mechanics are missing | payload capture, event schema mutation |
| Productive Drift vs Random Drift Evaluation | `watch`, `future-contract-needed` | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | evaluation cases are not designed yet | growth engine execution |

## Updated Open Items

### Temporal Awareness

Clarified by [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md), but not
implemented. It remains open because elapsed time has not been given accepted
runtime semantics, event representation, review routing, or validation.

Still open:

- whether elapsed time belongs in recall-state review;
- how elapsed time can become evidence without being evidence by itself;
- whether `long_pause`, `interruption`, or `resumed_session` should ever become
  temporal events;
- how task staleness, claim staleness, memory decay, and relationship silence
  can be represented without companion or social-layer behavior;
- whether CTM-inspired temporal dynamics should remain review vocabulary or
  later split into smaller RFCs such as deliberation ticks, thought traces, and
  temporal coherence evaluation.

### CTM-inspired Temporal Dynamics

Clarified by [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md),
but not implemented. It remains open because P81 only translates CTM-inspired
concepts into symbolic foundation vocabulary.

Still open:

- whether deliberation ticks are events, traces, or ephemeral review steps;
- whether any thought trace should be persisted;
- how to test temporal coherence without pseudo-consciousness claims;
- how review depth budget should relate to risk level;
- how unresolved tension or delayed alignment could become review evidence;
- how CTM-inspired dynamics should relate to reconstruction evidence.

### Temporal Coherence Evaluation

Clarified by
[TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md),
but not implemented. It remains open because P82 defines deterministic scenario
ideas and future evaluation signals only.

Still open:

- whether temporal coherence should become a report, validator, or manual review
  checklist later;
- how to score evidence alignment without turning scores into runtime truth;
- how to simulate deliberation ticks without executing a thought loop;
- how to test thought traces without storage policy;
- how to connect coherence evaluation to reconstruction evidence without
  reducer execution.

### Recall Event Write Policy

Clarified by [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md).
Ordinary retrieval is not an event, and ordinary recall is not a write.

Still open:

- accepted event schema for future recall candidates;
- payload and diff requirements;
- validation proving no memory rewrite or identity mutation;
- replay interpretation for future recall events;
- privacy and sensitivity scope.

### Stateful Memory Minimal Encoding Policy

Clarified by [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md).
It defines minimum references for review quality, not active schema.

Still open:

- whether any future schema should carry these references;
- how imported memories should expose weak provenance;
- how missing encoding context should affect review UX or reports;
- how encoding-state references interact with reconstruction evidence.

### Growth Candidate Lifecycle

Clarified by [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md).
Lifecycle labels organize review objects only.

Still open:

- whether lifecycle decisions become durable review records;
- what authority can acknowledge, defer, archive, quarantine, or reject;
- how lifecycle history is audited without executing growth;
- how Identity Gate escalation is represented.

### Productive Drift vs Collapse

Clarified by [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md).
It provides evidence and risk vocabulary, not an automatic classifier.

Still open:

- evaluation cases for productive drift vs random drift;
- thresholds for repeated evidence across time;
- Temporal Awareness contribution to delayed realization or cooled-down
  reinterpretation;
- collapse recovery review boundaries.

### Exploration / Serendipity Engine

Clarified by [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md).
Exploration remains future-only and review-only.

Still open:

- signal schema;
- input scope;
- quarantine rules;
- anti-companion and anti-roleplay evaluation;
- how exploration can request evidence without creating product behavior.

### Subject Kernel / World Seed Direction

Clarified by [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md).
The split remains conceptual.

Still open:

- which Identity Seed fields belong to Subject Kernel;
- which fields belong to World Seed;
- how reconstruction preserves the distinction;
- which world/context changes require Identity Gate.

### Reconstruction Reducer Contract

Clarified by [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md).
Reducer contract remains separate from reducer execution.

Still open:

- accepted input envelope;
- target path identity;
- operation semantics;
- deterministic output validation;
- failure modes for missing or ambiguous evidence.

### Payload / Diff Capture Policy

Clarified by [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md).
Capture policy remains separate from payload capture.

Still open:

- privacy and redaction policy;
- schema compatibility plan;
- hash and snapshot strategy;
- target-path acceptance gates;
- migration plan for future event compatibility.

## Runtime-Blocked Items

The following remain blocked until a future explicit implementation phase:

- Temporal Awareness runtime;
- recall event writes;
- growth lifecycle execution;
- automatic growth or drift classification;
- identity mutation;
- memory rewrite;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- event compaction;
- CTM runtime or model training;
- thought loop execution;
- policy executor;
- companion, relationship memory, UI, AstrBot, adapter, or product layer.

## Current Recommendation

Continue low-risk consolidation only. The next useful work is a risk register
or architecture boundary refresh, not runtime capability.
