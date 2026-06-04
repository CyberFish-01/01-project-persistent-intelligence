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
| Deliberation Tick / Review Depth | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | tick and review-depth vocabulary exists, but no tick runtime, thought loop, or review policy executor exists | tick runtime, thought loop execution, policy execution |
| Thought Trace Storage Policy | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | storage boundaries are defined, but no trace schema, storage backend, redaction policy, or approval gate exists | trace storage, hidden chain-of-thought capture, private reasoning persistence |
| Thin Interaction Harness | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | preview surfaces are named, but no CLI, runtime, context builder, review queue, or boundary monitor exists | harness runtime, UI, adapter integration, mutation path |
| Conversation Intake Contract | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | envelope fields are named, but no intake runtime, API, CLI, adapter ingest, privacy validation, or storage policy exists | conversation runtime, adapter ingest, event write |
| Context Package Preview | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | selected/omitted reference vocabulary exists, but no harness preview, retrieval execution, activation trace write, or storage policy exists | retrieval as continuity, context mutation, activation trace writes |
| Review Queue Preview | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | candidate preview and ordering vocabulary exists, but no queue runtime, storage, lifecycle execution, or approval path exists | queue execution, lifecycle execution, candidate approval |
| Session Resume Scenario Plan | `planned`, `indexed`, `future-contract-needed`, `blocked-runtime` | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) | deterministic scenarios exist, but no harness, tests, temporal runtime, temporal events, or salience policy exists | session runtime, temporal event write, memory decay |
| Core Interaction Harness Roadmap | `roadmap-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) | readiness is assessed, but fixture contract, output contract, boundary test plan, and explicit implementation approval are missing | harness implementation, CLI commands, runtime work |
| Tool-First Self-Evolution | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) | capability evolution vocabulary exists, but no tool execution, verification schema, review schema, safe tool library policy, or promotion gate exists | tool execution, auto tool generation, auto tool promotion, policy executor |
| Capability Evolution Boundary | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) | allowed and forbidden scope is defined, but verification evidence model, candidate review schema, safe tool library policy, and implementation gates are missing | automatic tool execution, automatic promotion, policy executor, identity mutation |
| Visual Naming / Founder-Facing Vocabulary | `guide-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) | internal keys now map to Chinese display names, but no visual surface contract, status assignment policy, or dashboard approval exists | Web UI, dashboard runtime, observability CLI, product layer |
| Foundation Observatory Report | `report-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) | a Markdown founder-facing report exists, but no CLI, dashboard runtime, status API, automatic report generator, or product surface exists | dashboard runtime, observability CLI, status API, product UI |
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

### Deliberation Tick / Review Depth

Clarified by
[DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md),
but not implemented. It remains open because P83 defines review-planning
vocabulary only.

Still open:

- whether review depth should be manually assigned or computed by future
  evaluation;
- whether `blocked` is a review depth or a separate boundary outcome;
- how many preview ticks are useful before review becomes too heavy;
- how review depth should interact with future thought trace storage policy;
- how a thin harness can preview review depth without executing a thought loop.

### Thought Trace Storage Policy

Clarified by
[THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md),
but not implemented. It remains open because P84 defines storage boundaries
only and does not create trace storage, schemas, redaction rules, or approval
gates.

Still open:

- whether trace candidates should ever be stored;
- whether future traces are events, reports, governance records, or ephemeral
  preview output;
- what redaction policy is required for sensitive user content;
- how reconstruction can use trace summaries without private reasoning;
- who or what can approve a future trace storage decision.

### Thin Interaction Harness

Clarified by
[THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md), but not
implemented. It remains open because P85 defines preview-only surfaces and does
not create a CLI, runtime, context builder, review queue, boundary monitor, UI,
or adapter integration.

Still open:

- whether the first harness should be CLI-only, report-only, or fixture-only;
- what minimal conversation envelope proves platform does not own identity;
- what preview output can be stored without becoming trace storage or event
  writes;
- how context preview avoids reducing continuity to retrieval;
- how review queue preview avoids lifecycle execution.

### Conversation Intake Contract

Clarified by
[CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md),
but not implemented. It remains open because P86 defines an envelope boundary
only and does not create runtime intake, adapter ingestion, event writes,
privacy validation, or context building.

Still open:

- whether `content_ref` should point to fixture text, redacted text, or source
  metadata;
- whether `privacy_scope` should be fixed before harness work;
- how much timestamp information is safe without Temporal Awareness runtime
  pressure;
- whether `context_request` should be explicit, inferred, or absent;
- what minimal cross-user privacy test should precede interaction work.

### Context Package Preview

Clarified by
[CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md), but not
implemented. It remains open because P87 defines selected/omitted reference
vocabulary only and does not execute retrieval, mutate context, persist
activation traces, or build prompts.

Still open:

- whether preview output should include exact selected text or only references
  and summaries;
- how token budget notes avoid becoming salience mutation;
- whether privacy-suppressed omitted references can be visible;
- how governance refs can appear without policy execution;
- whether context gaps should create review candidates or remain preview-only.

### Review Queue Preview

Clarified by [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md), but
not implemented. It remains open because P88 defines candidate preview and
ordering vocabulary only and does not create queue runtime, storage, lifecycle
execution, or approval paths.

Still open:

- whether queue previews should sort by risk, age, evidence strength, or owner
  boundary;
- whether blocked candidates remain visible or move to a separate blocked view;
- whether queue preview reports can be stored without becoming lifecycle
  history;
- whether context gaps can create review candidates in a future harness;
- how low-risk items avoid review overload.

### Session Resume Scenario Plan

Clarified by [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md),
but not implemented. It remains open because P89 defines deterministic scenario
plans only and does not create tests, harness runtime, temporal events, memory
decay, salience mutation, or resume automation.

Still open:

- which elapsed-time buckets are useful before Temporal Awareness runtime exists;
- whether unknown gaps should differ from known gaps;
- whether context gaps can create queue candidates;
- how stale task pressure differs from stale claim pressure;
- whether resume scenarios should become deterministic tests before harness
  implementation.

### Core Interaction Harness Roadmap

Clarified by
[CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md),
but not implemented. It remains open because P90 is a roadmap only and does not
approve CLI commands, schemas, tests, runtime work, or harness implementation.

Still open:

- fixture input contract;
- preview output contract;
- no-write validation invariants;
- forbidden-output test plan;
- privacy and redaction policy;
- explicit founder approval for any future implementation phase.

### Tool-First Self-Evolution

Clarified by
[TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md), but not
implemented. It remains open because P91 defines a capability evolution layer
only as review vocabulary and does not create tool execution, auto tool
generation, auto tool promotion, tool library mutation, policy execution, or
identity mutation.

Still open:

- what future tool candidate review schema should contain;
- how verification evidence should be represented without becoming
  authorization;
- how failed tool candidates become cautionary procedural memory candidates;
- what gate separates capability growth candidate review from subject growth
  candidate review;
- what safe tool library policy would block pollution, unsafe reuse, dependency
  risk, network risk, and filesystem risk;
- whether capability evidence can enter Event Log only by reference, and under
  which future event policy.

### Capability Evolution Boundary

Clarified by
[CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md),
but not implemented. It remains open because P92 defines allowed and forbidden
scope only. It does not define a verification evidence model, tool candidate
review schema, safe tool library policy, procedural memory alignment contract,
or capability growth evaluation plan.

Still open:

- what exact fields belong in future tool verification evidence;
- how tool candidate review distinguishes proposal, verification, authorization,
  and promotion;
- how reusable procedure candidates align with Procedural Memory without
  becoming trusted tools;
- how safe tool library policy should prevent contamination and unsafe reuse;
- what evaluation cases prove capability candidates do not mutate identity;
- what human / founder review gate is required before any future tool
  authorization.

### Visual Naming / Founder-Facing Vocabulary

Clarified by [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md), but not
implemented. It remains open because P93 defines naming rules and display-card
shape only. It does not create a Foundation Observatory, dashboard, Web UI,
observability CLI, report generator, status API, or product surface.

Still open:

- which concepts deserve future founder-facing visual cards;
- who assigns `已实现`, `报告层`, `RFC 层`, `未来方向`, and `危险过早`;
- how to prevent RFC-only concepts from appearing implemented;
- how to prevent candidate labels from appearing promoted;
- how bilingual display names and English internal keys are reviewed for drift;
- whether any future Observatory should be docs-only, report-only, CLI-only, or
  UI-based after explicit founder approval.

### Foundation Observatory Report

Clarified by
[FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md), but not
implemented as a runtime surface. It remains open because P94 creates a
Markdown report only. It does not create a dashboard runtime, Web UI,
observability CLI, automatic report generator, status API, product surface, or
runtime monitor.

Still open:

- whether future observatory output should stay Markdown-only or gain a CLI
  report boundary;
- whether status assignment needs a separate Visual Status Assignment Policy;
- how a future CLI would avoid becoming a dashboard runtime;
- whether the report should be generated from files, manually maintained, or
  kept as a phase artifact;
- what founder-approved gate is required before any observability tool exists.

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
- tick runtime execution;
- hidden chain-of-thought capture;
- private model reasoning persistence;
- thought trace storage;
- thin harness runtime;
- conversation intake runtime;
- adapter ingestion for harness work;
- context builder execution;
- retrieval execution as continuity;
- activation trace writes for harness previews;
- review queue execution;
- queue storage;
- candidate approval;
- session resume runtime;
- scenario tests for harness work;
- memory decay;
- salience mutation;
- tool execution runtime;
- automatic tool generation;
- automatic tool promotion;
- tool library mutation;
- self-modifying runtime;
- unreviewed dependency installation;
- uncontrolled filesystem or network access;
- Web UI;
- dashboard runtime;
- Foundation Observatory runtime;
- observability CLI;
- status API;
- automatic report generator;
- product-layer visual surface;
- harness implementation;
- fixture schema;
- output schema;
- policy executor;
- companion, relationship memory, UI, AstrBot, adapter, or product layer.

## Current Recommendation

Continue document-only planning unless the founder explicitly approves an
implementation phase. The P94 report recommends founder / CTO review first,
then a possible Minimal Observatory CLI RFC if the founder chooses to continue
the observability path.
