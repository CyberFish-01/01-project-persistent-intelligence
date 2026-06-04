# RFC Index

Chinese version: [RFC_INDEX_ZH.md](./RFC_INDEX_ZH.md)

Status: `document-only`, `index`, `non-runtime`.

P68 started the index for foundation RFC, policy, review, audit, and matrix
documents created during P54-P67. Later maintenance phases add review artifacts
without changing the index rule. This file does not add runtime behavior,
schemas, CLI commands, validation rules, adapters, product surfaces, event
writes, reducers, payload capture, identity mutation, memory rewrite, or growth
execution.

## Index Rule

```text
an RFC defines a review surface.
an RFC does not approve execution.
an index improves navigation.
an index does not change architecture.
```

P68 exists because the foundation layer now has many review artifacts. Without a
single index, later work can easily treat scattered RFC language as
implementation approval.

## Foundation Integrity And Governance

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P54 | [FOUNDATION_INTEGRITY_AUDIT.md](./FOUNDATION_INTEGRITY_AUDIT.md) / [ZH](./FOUNDATION_INTEGRITY_AUDIT_ZH.md) | audit | stable review | Checks whether foundation principles, boundaries, and risks still agree. | runtime enforcement |
| P55 | [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md) / [ZH](./CONCEPT_OVERLAP_REVIEW_ZH.md) | review | stable boundary review | Assigns primary ownership where concepts overlap. | concept deletion or schema change |
| P56 | [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) / [ZH](./BOUNDARY_TEST_MATRIX_ZH.md) | matrix | stable doc gate | Lists allowed and forbidden foundation outputs. | runtime test expansion |
| P57 | [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) / [ZH](./OPEN_QUESTIONS_TRIAGE_ZH.md) | triage | active routing | Sorts open questions into safe RFCs, watch items, and blocked runtime work. | closing the questions |
| P67 | [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) / [ZH](./FOUNDATION_ROADMAP_ZH.md) | roadmap | active guidance | Synthesizes stable foundation, blocked runtime work, future dependencies, and low-risk backlog. | runtime authorization |
| P76 | [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) / [ZH](./FOUNDATION_REVIEW_CHECKLIST_ZH.md) | manual checklist | phase review gate | Converts boundary, risk, RFC, bilingual, verification, and commit checks into a human review gate. | automated executor |
| P79 | [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md) / [ZH](./BILINGUAL_CONSISTENCY_REVIEW_ZH.md) | review | manual consistency record | Records paired-document, status, link, summary, and blocked-boundary alignment. | automated translation checker |
| P80 | [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md) / [ZH](./FOUNDATION_MAINTENANCE_REVIEW_ZH.md) | review | cycle closure | Records maintained artifacts, residual gaps, residual risks, and stop condition for P54-P80. | implementation approval |

## Stateful Memory And Growth Semantics

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P58 | [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) / [ZH](./TEMPORAL_AWARENESS_RFC_ZH.md) | future RFC | future direction | Frames elapsed time as possible subject-state evidence. | Temporal Awareness runtime |
| P59 | [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) / [ZH](./RECALL_EVENT_WRITE_POLICY_RFC_ZH.md) | policy RFC | blocked write policy | Defines future recall event write thresholds. | recall event writes |
| P60 | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) / [ZH](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md) | policy | review policy | Defines minimum encoding references for meaning-shift review. | new memory store |
| P61 | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) / [ZH](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md) | lifecycle RFC | future review-object policy | Defines future review-object states such as deferred, archived, or quarantined. | growth lifecycle execution |
| P62 | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) / [ZH](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md) | boundary RFC | review vocabulary | Separates productive drift, random drift, identity-threatening drift, and collapse. | automatic drift classifier |
| P81 | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) / [ZH](./CTM_TEMPORAL_DYNAMICS_RFC_ZH.md) | future RFC | RFC-only mapping | Translates CTM-inspired temporal dynamics into symbolic foundation vocabulary. | CTM runtime or temporal event execution |
| P82 | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) / [ZH](./TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md) | evaluation plan | RFC-only evaluation design | Defines deterministic scenarios and future signals for temporal coherence vocabulary. | temporal runtime or thought loop execution |
| P83 | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) / [ZH](./DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md) | future RFC | review-depth policy vocabulary | Defines deliberation tick, review depth, and risk-level planning boundaries. | tick runtime or thought loop execution |
| P84 | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) / [ZH](./THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md) | policy RFC | storage-boundary policy | Defines what a future trace may summarize and what must never be stored. | hidden chain-of-thought capture or trace storage |
| P85 | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) / [ZH](./THIN_INTERACTION_HARNESS_RFC_ZH.md) | future RFC | harness boundary | Defines preview-only interaction surfaces before any harness implementation. | product, adapter, UI, or mutation path |
| P86 | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) / [ZH](./CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md) | contract RFC | intake envelope boundary | Defines future conversation intake preview fields without adapter ingest or writes. | conversation runtime, adapter ingest, or event write |
| P87 | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) / [ZH](./CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md) | future RFC | context preview boundary | Defines selected and omitted context reference explanations for future harness previews. | retrieval as continuity or activation trace writes |
| P88 | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) / [ZH](./REVIEW_QUEUE_PREVIEW_RFC_ZH.md) | future RFC | review queue preview | Defines candidate preview types, ordering signals, review depth, and blocked items. | lifecycle execution, approval, or mutation |
| P89 | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) / [ZH](./SESSION_RESUME_SCENARIO_PLAN_ZH.md) | scenario plan | resume simulation plan | Defines deterministic session resume scenarios using simulated elapsed time. | Temporal Awareness runtime or temporal event writes |
| P90 | [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) / [ZH](./CORE_INTERACTION_HARNESS_ROADMAP_ZH.md) | roadmap | harness readiness roadmap | Assesses future minimal CLI harness readiness and gates. | harness implementation or approval |
| P82-P90 | [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md) / [ZH](./HARNESS_TRANSITION_SUMMARY_ZH.md) | summary | transition closure | Summarizes the planning bridge from temporal concept safety to future harness readiness. | P91 implementation approval |

## Capability Evolution And Tool Boundary

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P91 | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) / [ZH](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md) | future RFC | capability evolution boundary | Translates Yunjue / zero-start tool-first self-evolution into review-only capability evolution vocabulary. | tool execution, auto tool generation, auto promotion, policy executor, or identity growth |
| P92 | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) / [ZH](./CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md) | boundary RFC | capability boundary | Defines allowed and forbidden scopes for capability evolution before any tool runtime or promotion policy. | automatic tool execution, automatic tool promotion, policy executor, identity mutation, memory rewrite |

## Founder-Facing Vocabulary And Visual Naming

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P93 | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) / [ZH](./VISUAL_NAMING_GUIDE_ZH.md) | naming guide | founder-facing vocabulary | Maps English internal keys to Chinese display names for future visual foundation surfaces. | Web UI, dashboard runtime, observability CLI, product layer, or Foundation Observatory implementation |

## Exploration And Subject Boundary

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P63 | [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) / [ZH](./EXPLORATION_SERENDIPITY_RFC_ZH.md) | future RFC | future direction | Defines exploration and serendipity as record-only or review-only signals. | exploration engine or companion feature |
| P64 | [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) / [ZH](./SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md) | boundary RFC | future boundary | Distinguishes protected subject anchor from evolvable world orientation. | Identity Core rewrite |

## Reconstruction Readiness

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P65 | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) / [ZH](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md) | contract RFC | future contract | Defines what a future reconstruction reducer contract must specify. | reducer execution |
| P66 | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) / [ZH](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md) | policy RFC | future policy | Defines target-path vocabulary for payload, diff, snapshot, and reference-only treatment. | payload capture or event schema mutation |

## Dependency Order

The current dependency order is:

1. [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) identifies safe
   document-only questions and blocked runtime work.
2. [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) remains future-only
   until recall write policy, payload/diff rules, and review placement exist.
3. [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md)
   blocks ordinary retrieval from becoming durable events.
4. [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md)
   defines what must be known before meaning-shift review can be trusted.
5. [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md)
   keeps lifecycle vocabulary separate from growth execution.
6. [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md)
   separates bounded change from random drift and collapse.
7. [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) and
   [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) keep
   future exploration and subject/world boundaries outside product behavior.
8. [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md)
   must exist before reducer execution can even be discussed.
9. [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md)
   defines capture policy vocabulary but does not capture payloads.
10. [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) keeps future work in
    low-risk consolidation until implementation is explicitly approved.
11. [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) provides
    a manual gate for later document-only phases without approving execution.
12. [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)
    records the latest manual bilingual consistency baseline without automating
    review.
13. [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md)
    closes the P54-P80 maintenance cycle without approving runtime work.
14. [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) maps
    CTM-inspired temporal concepts into foundation vocabulary without approving
    CTM runtime, temporal event writes, or model training.
15. [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md)
    turns P81 vocabulary into evaluation scenarios without implementing tests,
    temporal runtime, thought loops, or event writes.
16. [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md)
    defines tick and review-depth preview vocabulary without executing ticks,
    thought loops, policy, or mutations.
17. [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md)
    defines future trace storage boundaries without storing hidden
    chain-of-thought, private model reasoning, model internals, or runtime
    traces.
18. [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md)
    defines the future harness as a preview-only local testing surface, not a
    product, adapter, UI, runtime executor, or mutation path.
19. [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md)
    defines the future intake envelope for harness previews without adapter
    ingestion, conversation runtime, context building, or event writes.
20. [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md)
    defines future selected/omitted context reference explanations without
    retrieval execution, context mutation, or activation trace writes.
21. [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md)
    defines future candidate queue preview vocabulary without lifecycle
    execution, automatic approval, policy execution, or mutation.
22. [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md)
    defines deterministic resume scenario inputs and expected previews without
    temporal runtime, temporal event writes, memory decay, or salience mutation.
23. [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md)
    assesses future minimal CLI harness readiness without approving harness
    implementation, commands, schemas, tests, adapters, UI, or runtime work.
24. [HARNESS_TRANSITION_SUMMARY.md](./HARNESS_TRANSITION_SUMMARY.md)
    closes the P82-P90 planning bridge and keeps P91 implementation blocked
    until explicit future approval.
25. [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md)
    translates zero-start, tool-first self-evolution into capability review
    vocabulary without approving tool execution, tool generation, tool
    promotion, policy execution, or Identity Core mutation.
26. [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md)
    defines the allowed proposal/evidence/review scope and the forbidden
    execution/promotion/policy/identity boundaries for capability evolution.
27. [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) maps founder-facing
    Chinese display names to English internal keys without approving Web UI,
    dashboard runtime, observability CLI, product layer, or Foundation
    Observatory implementation.

## Runtime-Blocked Topics

The indexed documents do not approve:

- Temporal Awareness runtime;
- CTM runtime or model training;
- thought loop execution;
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
- tool authorization without human review;
- self-modifying runtime;
- unreviewed dependency installation;
- uncontrolled filesystem or network access;
- Web UI;
- dashboard runtime;
- Foundation Observatory runtime;
- observability CLI;
- harness implementation;
- fixture schema;
- output schema;
- recall event writes;
- growth lifecycle execution;
- automatic growth classification;
- automatic drift classification;
- identity mutation;
- memory rewrite;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- event compaction;
- policy executor;
- companion, relationship memory, UI, AstrBot, adapter, or product layer.

## Stable Interpretation

Use this index to answer three questions:

1. Which document owns the current vocabulary?
2. Which future contract is missing before implementation?
3. Which forbidden action must remain blocked?

Do not use this index as approval to implement any future capability.
