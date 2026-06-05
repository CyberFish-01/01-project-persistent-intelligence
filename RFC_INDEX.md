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
| P99 | [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md) / [ZH](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md) | implementation plan | RFC-only plan | Defines the no-write `harness-dry-run` pressure-test boundary, flow, inputs, outputs, candidates, boundaries, and tests plan later implemented narrowly in P100. | model calls, external APIs, state writes, adapter integration, product layer, or P101 execution |
| P100 | `python3 -m one_core.cli harness-dry-run` | read-only CLI | implemented dry-run preview | Generates local Markdown or JSON previews for intake, context package, candidates, review queue, boundary monitor, observatory snapshot, and non-execution invariants. | model calls, external APIs, state writes, memory writes, recall writes, identity mutation, adapter integration, Companion, product layer, or automatic next-step execution |

## Capability Evolution And Tool Boundary

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P91 | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) / [ZH](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md) | future RFC | capability evolution boundary | Translates Yunjue / zero-start tool-first self-evolution into review-only capability evolution vocabulary. | tool execution, auto tool generation, auto promotion, policy executor, or identity growth |
| P92 | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) / [ZH](./CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md) | boundary RFC | capability boundary | Defines allowed and forbidden scopes for capability evolution before any tool runtime or promotion policy. | automatic tool execution, automatic tool promotion, policy executor, identity mutation, memory rewrite |

## Core Lockdown And Quarantine

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P121 | [CORE_LOCKDOWN_MODE_RFC.md](./CORE_LOCKDOWN_MODE_RFC.md) / [ZH](./CORE_LOCKDOWN_MODE_RFC_ZH.md) | boundary RFC | RFC-only lockdown boundary | Defines sandbox/quarantine/candidate handling before future old 01 imports, model output, adapter context, tool evidence, external IO, or rebuild pressure can touch trusted state. | lockdown runtime, validator, import pipeline, adapter hook, model call, write path, or rebuild |
| P122 | [IMPORT_QUARANTINE_RFC.md](./IMPORT_QUARANTINE_RFC.md) / [ZH](./IMPORT_QUARANTINE_RFC_ZH.md) | quarantine RFC | RFC-only import boundary | Defines source classes, quarantine routes, and review gates for future imports from old 01, logs, memory dumps, model output, adapter exports, tool results, or external files. | import runtime, file loading, quarantine storage, memory write, identity mutation, adapter integration, model call, or rebuild |
| P123 | [SHADOW_ADAPTER_MODE_RFC.md](./SHADOW_ADAPTER_MODE_RFC.md) / [ZH](./SHADOW_ADAPTER_MODE_RFC_ZH.md) | shadow boundary RFC | RFC-only adapter boundary | Defines how future adapter-shaped input can be observed as shadow evidence without live integration, ingest, event writes, memory writes, or platform-owned identity. | adapter code, AstrBot integration, network access, adapter ingest, event write, memory write, model call, or rebuild |
| P124 | [CONTAMINATION_SCAN_RFC.md](./CONTAMINATION_SCAN_RFC.md) / [ZH](./CONTAMINATION_SCAN_RFC_ZH.md) | scan RFC | RFC-only contamination boundary | Defines future contamination candidate types, scan inputs, output preview, routing rules, and false-positive policy. | scanner runtime, validation enforcement, import processing, model call, adapter integration, write path, or rebuild |
| P125 | [LOCKDOWN_INTEGRATION_READINESS.md](./LOCKDOWN_INTEGRATION_READINESS.md) / [ZH](./LOCKDOWN_INTEGRATION_READINESS_ZH.md) | review | readiness review | Reviews whether P121-P124 form a coherent lockdown stack before fixture or validator planning continues. | validator implementation, runtime enforcement, adapter integration, import processing, model call, write path, or rebuild |
| P126 | [LOCKDOWN_FIXTURE_MATRIX.md](./LOCKDOWN_FIXTURE_MATRIX.md) / [ZH](./LOCKDOWN_FIXTURE_MATRIX_ZH.md) | fixture matrix | document-only examples | Defines synthetic no-write fixtures for contamination classes and boundary routes before any future validator or scanner. | real imports, validator implementation, scanner runtime, adapter integration, model call, write path, or rebuild |
| P127 | [QUARANTINE_REVIEW_GATE_PLAN.md](./QUARANTINE_REVIEW_GATE_PLAN.md) / [ZH](./QUARANTINE_REVIEW_GATE_PLAN_ZH.md) | review gate plan | document-only gate plan | Defines manual quarantine gate stages, review gates, evidence rules, and safe outcomes before candidate consideration. | quarantine storage, import processing, lifecycle execution, model call, adapter integration, write path, or rebuild |
| P128 | [SHADOW_ADAPTER_EXAMPLE_SHAPES.md](./SHADOW_ADAPTER_EXAMPLE_SHAPES.md) / [ZH](./SHADOW_ADAPTER_EXAMPLE_SHAPES_ZH.md) | example shapes | document-only examples | Defines synthetic adapter-shaped examples for future shadow review without connecting any platform. | adapter code, AstrBot integration, network access, adapter ingest, event write, memory write, model call, or rebuild |
| P129 | [CONTAMINATION_FALSE_POSITIVE_REVIEW.md](./CONTAMINATION_FALSE_POSITIVE_REVIEW.md) / [ZH](./CONTAMINATION_FALSE_POSITIVE_REVIEW_ZH.md) | review | false-positive review | Reviews how future contamination signals can be useful without becoming truth, punishment, or enforcement. | scanner runtime, classifier implementation, enforcement engine, quarantine storage, write path, model call, adapter integration, or rebuild |
| P130 | [CORE_LOCKDOWN_CYCLE_REVIEW.md](./CORE_LOCKDOWN_CYCLE_REVIEW.md) / [ZH](./CORE_LOCKDOWN_CYCLE_REVIEW_ZH.md) | cycle review | block closure | Closes P121-P130 with readiness, missing prerequisites, boundary audit, risks, and next safe planning boundary. | validator implementation, scanner runtime, import pipeline, adapter integration, write path, model call, or rebuild |

## Thin Founder Console

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P131 | [FOUNDER_CONSOLE_BOUNDARY_RFC.md](./FOUNDER_CONSOLE_BOUNDARY_RFC.md) / [ZH](./FOUNDER_CONSOLE_BOUNDARY_RFC_ZH.md) | boundary RFC | RFC-only console boundary | Defines the future Thin Founder Console as local, founder-only, no-write visibility rather than product behavior. | console implementation, Web UI, Companion, adapter integration, model call, tool execution, write path, policy executor, or rebuild |
| P132 | [FOUNDER_CONSOLE_USER_FLOW.md](./FOUNDER_CONSOLE_USER_FLOW.md) / [ZH](./FOUNDER_CONSOLE_USER_FLOW_ZH.md) | user flow | document-only flow | Defines the future founder-console path from status visibility to dry-run preview to manual next-step decision. | console implementation, automatic roadmap, Web UI, Companion, adapter integration, model call, write path, or rebuild |
| P133 | [FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md](./FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md) / [ZH](./FOUNDER_CONSOLE_NO_WRITE_CONTRACT_ZH.md) | contract | no-write contract | Defines allowed reads, explicit report-output writes, forbidden formal writes, invariants, and future verification expectations. | console implementation, state write, memory write, recall write, identity mutation, adapter integration, model call, tool execution, or rebuild |
| P134 | [FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md](./FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md) / [ZH](./FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA_ZH.md) | acceptance criteria | document-only gate | Defines what a future founder console must pass or fail before implementation can be considered acceptable. | console implementation, Web UI, Companion, adapter integration, model call, tool execution, write path, policy executor, or rebuild |
| P135 | [FOUNDER_CONSOLE_RISK_REVIEW.md](./FOUNDER_CONSOLE_RISK_REVIEW.md) / [ZH](./FOUNDER_CONSOLE_RISK_REVIEW_ZH.md) | risk review | document-only risk review | Reviews founder-console risks such as product creep, Companion creep, roadmap automation, write paths, adapters, model calls, temporal overreach, and capability overreach. | console implementation, Web UI, Companion, adapter integration, model call, tool execution, write path, policy executor, or rebuild |
| P136 | [FOUNDER_CONSOLE_ROADMAP.md](./FOUNDER_CONSOLE_ROADMAP.md) / [ZH](./FOUNDER_CONSOLE_ROADMAP_ZH.md) | roadmap | block closure | Closes founder-console planning and routes the next safe work to context package contracts before implementation. | console implementation, Web UI, Companion, adapter integration, model call, tool execution, write path, policy executor, or rebuild |

## Context Package And Response Preparation

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P137 | [CONTEXT_PACKAGE_BUILDER_RFC.md](./CONTEXT_PACKAGE_BUILDER_RFC.md) / [ZH](./CONTEXT_PACKAGE_BUILDER_RFC_ZH.md) | builder RFC | RFC-only package contract | Defines required context packs, trust levels, source references, temporal pack boundary, capability pack boundary, and response strategy pack. | builder implementation, retrieval engine, model call, prompt execution, state write, memory write, identity mutation, adapter integration, tool execution, or rebuild |
| P138 | [CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md](./CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md) / [ZH](./CONTEXT_PACKAGE_PREVIEW_CLI_PLAN_ZH.md) | CLI plan | document-only plan | Plans a future local deterministic read-only context package preview CLI without adding the command. | command implementation, parser, builder, retrieval engine, model call, prompt execution, state write, memory write, adapter integration, tool execution, or rebuild |
| P139 | [SOURCE_SELECTION_MATRIX.md](./SOURCE_SELECTION_MATRIX.md) / [ZH](./SOURCE_SELECTION_MATRIX_ZH.md) | matrix | document-only selection matrix | Defines pack-level source preferences, trust levels, omission reasons, and temporal/capability selection boundaries. | retrieval implementation, ranking engine, builder, model call, prompt execution, state write, memory write, adapter integration, tool execution, or rebuild |
| P140 | [BOUNDARY_INJECTION_RFC.md](./BOUNDARY_INJECTION_RFC.md) / [ZH](./BOUNDARY_INJECTION_RFC_ZH.md) | boundary RFC | RFC-only injection contract | Defines how future context packages should carry boundary reminders in boundary and response-strategy packs. | builder implementation, prompt builder, runtime guard, model call, policy executor, state write, memory write, adapter integration, tool execution, or rebuild |
| P141 | [CTM_TEMPORAL_CONTEXT_PACK_RFC.md](./CTM_TEMPORAL_CONTEXT_PACK_RFC.md) / [ZH](./CTM_TEMPORAL_CONTEXT_PACK_RFC_ZH.md) | temporal pack RFC | RFC-only pack contract | Defines the future `temporal_pack` as symbolic CTM-inspired review context with explicit forbidden temporal actions. | temporal runtime, CTM runtime, thought loop, thought-trace storage, temporal event write, recall event write, model call, state mutation, or rebuild |
| P142 | [CAPABILITY_CONTEXT_PACK_RFC.md](./CAPABILITY_CONTEXT_PACK_RFC.md) / [ZH](./CAPABILITY_CONTEXT_PACK_RFC_ZH.md) | capability pack RFC | RFC-only pack contract | Defines the future `capability_pack` as Tool-First candidate/evidence/review context with explicit forbidden tool actions. | tool execution, tool verification runtime, tool promotion, tool library mutation, dependency installation, policy executor, model call, state mutation, or rebuild |

## Response And Model Boundary

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P143 | [RESPONSE_ORCHESTRATION_PREVIEW_RFC.md](./RESPONSE_ORCHESTRATION_PREVIEW_RFC.md) / [ZH](./RESPONSE_ORCHESTRATION_PREVIEW_RFC_ZH.md) | response RFC | RFC-only preview path | Defines a future response orchestration preview path from intake to context package to model-as-resource strategy to post-response candidate extraction. | orchestration implementation, prompt builder, model call, response generation, extraction runtime, state write, memory write, adapter integration, tool execution, or rebuild |
| P144 | [LLM_AS_RESOURCE_BOUNDARY_RFC.md](./LLM_AS_RESOURCE_BOUNDARY_RFC.md) / [ZH](./LLM_AS_RESOURCE_BOUNDARY_RFC_ZH.md) | boundary RFC | RFC-only model boundary | Defines future LLM calls as resource usage, with output untrusted by default and outside subject ownership. | model call, prompt engine, adapter integration, state write, memory write, recall write, identity mutation, tool execution, policy executor, or rebuild |
| P145 | [POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md](./POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md) / [ZH](./POST_RESPONSE_CANDIDATE_EXTRACTION_RFC_ZH.md) | extraction RFC | RFC-only extraction boundary | Defines how future model output may be inspected into preview-only candidates with review gates and blocked promotions. | extraction runtime, model call, response generation, candidate storage, review lifecycle, event write, memory write, identity mutation, tool execution, or rebuild |
| P146 | [MANUAL_REVIEW_GATE_RFC.md](./MANUAL_REVIEW_GATE_RFC.md) / [ZH](./MANUAL_REVIEW_GATE_RFC_ZH.md) | review gate RFC | RFC-only manual gate | Defines required manual gates, review questions, allowed outcomes, and blocked direct-write outcomes before any durable change. | review lifecycle implementation, approval storage, event write, memory write, recall write, identity mutation, growth execution, tool execution, adapter integration, model call, or rebuild |
| P147 | [REBUILD_MIGRATION_PROTOCOL_RFC.md](./REBUILD_MIGRATION_PROTOCOL_RFC.md) / [ZH](./REBUILD_MIGRATION_PROTOCOL_RFC_ZH.md) | migration RFC | RFC-only rebuild gate | Defines future local rebuild entry gates, migration source classes, non-goals, stop conditions, and first low-risk write direction. | rebuild start, old 01 read, state migration, import runtime, reducer execution, event compaction, state write, memory write, adapter integration, model call, tool execution, or policy executor |

## Pre-Rebuild Verification

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P148 | [REBUILD_ENTRY_GATE_CHECKLIST.md](./REBUILD_ENTRY_GATE_CHECKLIST.md) / [ZH](./REBUILD_ENTRY_GATE_CHECKLIST_ZH.md) | checklist | document-only gate checklist | Defines required gates and evidence before local 01 rebuild can be considered. | verification execution, rebuild start, old 01 read, state migration, memory write, adapter integration, model call, tool execution, reducer execution, or event compaction |
| P149 | [PRE_REBUILD_SYSTEM_REVIEW.md](./PRE_REBUILD_SYSTEM_REVIEW.md) / [ZH](./PRE_REBUILD_SYSTEM_REVIEW_ZH.md) | system review | document-only review | Reviews whether P112-P148 prepared the system for final read-only pre-rebuild verification. | verification execution, rebuild start, old 01 read, state migration, memory write, adapter integration, model call, tool execution, reducer execution, or event compaction |
| P150 | [FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md](./FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md) / [ZH](./FULL_VERIFICATION_PLAN_BEFORE_REBUILD_ZH.md) | verification plan | document-only plan | Defines final read-only verification areas, commands, forbidden patterns, pass criteria, and failure handling before rebuild. | verification execution, rebuild start, old 01 read, state migration, memory write, adapter integration, model call, tool execution, reducer execution, or event compaction |
| P151 | [PRE_REBUILD_VERIFICATION_SUITE.md](./PRE_REBUILD_VERIFICATION_SUITE.md) / [ZH](./PRE_REBUILD_VERIFICATION_SUITE_ZH.md) | read-only verification CLI | implemented report-only suite | Checks required artifacts, links, forbidden flags, read-only builders, CTM boundaries, Tool-First boundaries, and rebuild boundaries. | rebuild execution, rebuild approval, old 01 read, state migration, adapter integration, model call, tool execution, or write authority |
| P152 | [VERIFICATION_REPORT.md](./VERIFICATION_REPORT.md) / [ZH](./VERIFICATION_REPORT_ZH.md) | verification report | read-only evidence report | Records final verification evidence and pass status for founder checkpoint. | rebuild approval, rebuild start, migration, import, write path, model call, adapter integration, or automatic next phase |
| P153 | [FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md](./FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md) / [ZH](./FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT_ZH.md) | founder checkpoint | review-only checkpoint | Records that verification passed enough to ask the founder, while rebuild remains blocked without explicit approval. | founder approval fabrication, rebuild start, old 01 read, migration, model call, adapter integration, or automatic roadmap execution |
| P154 | [PUSH_READINESS_REPORT.md](./PUSH_READINESS_REPORT.md) / [ZH](./PUSH_READINESS_REPORT_ZH.md) | push audit | audit-only report | Audits local `main` for clean status, ahead commits, file types, sensitive information, forbidden boundaries, links, tests, and push recommendation. | push execution, rebuild approval, cloud/server update, AstrBot upload, old 01 read, model call, adapter integration, or automatic next phase |
| P155 | [LINEAGE_BRANCH_GOVERNANCE_RFC.md](./LINEAGE_BRANCH_GOVERNANCE_RFC.md) / [ZH](./LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md) | lineage governance RFC | governance-only planning | Defines future lineage, branch, tag, checkpoint, sandbox, quarantine, and manual selected-return rules before any local rebuild. | git tag creation, git branch creation, push execution, rebuild start, direct instance merge, quarantine merge, old 01 read, model call, adapter integration, or automatic selected return |
| P156 | [BASELINE_TAGGING_PLAN.md](./BASELINE_TAGGING_PLAN.md) / [ZH](./BASELINE_TAGGING_PLAN_ZH.md) | baseline tagging plan | planning-only report | Proposes candidate baseline tags, milestone tags, branch fork points, manual commands, and rebuild safety gates for founder review. | git tag creation, git branch creation, push execution, git history modification, rebuild start, branch merge, old 01 read, model call, adapter integration, or automatic selected return |
| P157 | [BASELINE_TAGGING_FOUNDER_REVIEW.md](./BASELINE_TAGGING_FOUNDER_REVIEW.md) / [ZH](./BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md) | founder review | review-only report | Reviews P156 tag and branch candidates with confidence, risks, founder-confirmation needs, and recommendations. | git tag creation, git branch creation, push execution, git history modification, rebuild start, branch merge, old 01 read, model call, adapter integration, or automatic selected return |
| P158 | [MANUAL_TAG_BRANCH_COMMAND_SHEET.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET.md) / [ZH](./MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md) | command sheet | manual-command draft | Provides future manual tag/branch command drafts, pre-checks, post-checks, rollback drafts, and confirmation requirements. | command execution, git tag creation, git branch creation, push tags, push main, git history modification, rebuild start, branch merge, old 01 read, model call, or adapter integration |

## Founder-Facing Vocabulary And Visual Naming

| Phase | Artifact | Type | Status | Purpose | Explicitly Not |
|---|---|---|---|---|---|
| P93 | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) / [ZH](./VISUAL_NAMING_GUIDE_ZH.md) | naming guide | founder-facing vocabulary | Maps English internal keys to Chinese display names for future visual foundation surfaces. | Web UI, dashboard runtime, observability CLI, product layer, or Foundation Observatory implementation |
| P94 | [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) / [ZH](./FOUNDATION_OBSERVATORY_REPORT_ZH.md) | observatory report | founder-facing report | Provides a Markdown snapshot, axes map, readiness matrix, boundary status, and risk heatmap for the foundation. | dashboard runtime, Web UI, observability CLI, product layer, status API, or runtime report generator |
| P95 | [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md) / [ZH](./MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md) | CLI plan | RFC-only plan | Defines the possible scope, inputs, outputs, categories, boundaries, and risks for a future read-only observatory CLI report. | CLI implementation, commands, parser, generator, dashboard runtime, Web UI, product UI, or executor |
| P96 | `python3 -m one_core.cli foundation-observatory-report` | read-only CLI | implemented static report | Generates founder-facing Markdown or JSON from static foundation artifacts. | dashboard runtime, Web UI, product UI, status API, observability executor, policy execution, state mutation, or phase creation |

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
28. [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md)
    applies P93 naming to a Markdown founder-facing status report without
    approving dashboard runtime, Web UI, observability CLI, product layer,
    status API, or runtime report generation.
29. [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md)
    plans a future read-only observatory CLI report without implementing CLI
    commands, parsers, generators, dashboard runtime, Web UI, product UI,
    status API, or observability executor.
30. [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md)
    plans the no-write `harness-dry-run` command later implemented narrowly in
    P100 without model calls, external APIs, state writes, adapter integration,
    product behavior, or P101.
31. `python3 -m one_core.cli harness-dry-run` implements the P100 local dry-run
    preview command without state writes, model calls, external APIs, adapter
    integration, product behavior, or automatic next-step execution.
32. [PRE_REBUILD_VERIFICATION_SUITE.md](./PRE_REBUILD_VERIFICATION_SUITE.md)
    documents and implements the P151 read-only `pre-rebuild-verification`
    report command for artifact, link, forbidden-pattern, boundary, and
    read-only builder checks before P152. It does not run rebuild or approve
    rebuild.
33. [PRE_REBUILD_VERIFICATION_SUITE_ZH.md](./PRE_REBUILD_VERIFICATION_SUITE_ZH.md)
    mirrors the P151 read-only verification suite boundary in Chinese.
34. [VERIFICATION_REPORT.md](./VERIFICATION_REPORT.md) and
    [VERIFICATION_REPORT_ZH.md](./VERIFICATION_REPORT_ZH.md) record the P152
    read-only verification evidence and pass status for founder checkpoint,
    not rebuild approval.
35. [FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md](./FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md)
    and [FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT_ZH.md](./FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT_ZH.md)
    record the P153 founder checkpoint: verification evidence is sufficient to
    ask the founder, but rebuild remains blocked until explicit approval.
36. [PUSH_READINESS_REPORT.md](./PUSH_READINESS_REPORT.md) and
    [PUSH_READINESS_REPORT_ZH.md](./PUSH_READINESS_REPORT_ZH.md) record the P154
    push readiness audit: local `main` is checked and push-ready after the
    report commit, but push still requires human confirmation and rebuild
    remains blocked.
37. [LINEAGE_BRANCH_GOVERNANCE_RFC.md](./LINEAGE_BRANCH_GOVERNANCE_RFC.md) and
    [LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md](./LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md)
    record the P155 governance-only lineage boundary: future Core, instance,
    research, quarantine, tag, and checkpoint decisions need explicit review;
    P155 does not create tags, create branches, push, or start rebuild.
38. [BASELINE_TAGGING_PLAN.md](./BASELINE_TAGGING_PLAN.md) and
    [BASELINE_TAGGING_PLAN_ZH.md](./BASELINE_TAGGING_PLAN_ZH.md) record the P156
    planning-only tag and branch proposal: candidate commits and branch fork
    points are visible for founder review, but no Git object is created and
    rebuild remains blocked.
39. [BASELINE_TAGGING_FOUNDER_REVIEW.md](./BASELINE_TAGGING_FOUNDER_REVIEW.md)
    and [BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md](./BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md)
    record the P157 founder review: recommendations are clearer, but tag and
    branch execution still waits for manual founder confirmation.
40. [MANUAL_TAG_BRANCH_COMMAND_SHEET.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET.md)
    and [MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md)
    record P158 manual command drafts for future humans; the commands are not
    executed, and tags/branches remain uncreated.

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
- observability CLI with runtime monitoring, enforcement, or execution;
- status API;
- runtime report generator beyond the read-only static P96 command;
- observability executor;
- automatic roadmap execution;
- automatic next phase creation;
- git tag creation;
- git branch creation;
- git history modification;
- automatic merge;
- automatic selected return;
- lineage executor;
- pre-rebuild verification as rebuild approval;
- harness implementation beyond the P100 read-only dry-run command;
- harness runtime beyond the P100 read-only dry-run command;
- fixture schema;
- output schema;
- model calls from harness work;
- external API calls from harness work;
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
