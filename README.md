# 01 Project

**How Can Intelligence Persist Through Time?**

[中文 README](./README_ZH.md)

01 Project is a research program about persistent intelligence: how an AI system can remain continuous across conversations, tasks, memories, dreams, conflicts, and social interactions.

The project begins from a simple problem:

> Existing AI systems restart too easily.

Even when a model is powerful, its context is long, and its agent loop is complex, it can still lose state, drift in identity, forget long-term intent, or become a different behavioral subject across time.

This repository now has two layers:

- foundation documents that define continuity, identity, event sourcing,
  review, reconstruction readiness, and blocked future work;
- earlier prototype references for the local 01 Core runtime and adapter
  surfaces.

Current work status: P160 main-only GitHub sync is complete.
The P154 audit found the project push-ready; P155 added lineage governance;
P156 proposed candidate tags/branches; P157 reviewed those choices; P158 adds
manual command drafts for a later human operation; P159 confirms final
pre-rebuild push readiness and warns that current `origin` is a local path, not
GitHub; P160 pushed `main` to GitHub without tags or branch creation. Tag
creation, branch creation, and rebuild remain blocked until explicit
founder/operator confirmation.

The runtime and adapter references below are historical/engineering references;
they are not approval to enter P103, build dashboard runtime, Web UI,
observability executor, status API, expand into the application layer, UI,
AstrBot, product, Companion, Temporal Awareness runtime, tool execution,
automatic tool generation, automatic tool promotion, growth execution, memory
rewrite, or reconstruction reducers.

## Document Entrance

Read these first when joining the project or handing it to another agent:

- [FOUNDATION.md](./FOUNDATION.md) / [FOUNDATION_ZH.md](./FOUNDATION_ZH.md): project-level boundaries, invariants, and stage order.
- [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) / [FOUNDATION_STATUS_ZH.md](./FOUNDATION_STATUS_ZH.md): what the foundation has, what is missing, and what remains exploratory or pushed back.
- [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) / [FOUNDATION_ROADMAP_ZH.md](./FOUNDATION_ROADMAP_ZH.md): stable foundation, blocked runtime work, future contracts, and low-risk consolidation.
- [PHASE_INDEX.md](./PHASE_INDEX.md) / [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md): P0-P160 foundation phase index by proposition and main line.
- [CONCEPT_MAP.md](./CONCEPT_MAP.md) / [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md): current foundation concept map and cross-layer relationships.
- [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) / [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md): P73 architecture boundary refresh across identity, memory, growth, temporal, reconstruction, governance, and product layers.
- [GLOSSARY.md](./GLOSSARY.md) / [GLOSSARY_ZH.md](./GLOSSARY_ZH.md): P74 deduplicated shared terms and boundaries for growth, drift, stateful memory, governance, reconstruction, and temporal awareness.
- [RISK_REGISTER.md](./RISK_REGISTER.md) / [RISK_REGISTER_ZH.md](./RISK_REGISTER_ZH.md): P72 foundation risk register for concept inflation, premature runtime pressure, and boundary drift.
- [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) / [FOUNDATION_REVIEW_CHECKLIST_ZH.md](./FOUNDATION_REVIEW_CHECKLIST_ZH.md): P76 manual review checklist for future document-only foundation phases.
- [DECISIONS.md](./DECISIONS.md) / [DECISIONS_ZH.md](./DECISIONS_ZH.md): P77 document-only log of accepted, deferred, blocked, and watch foundation decisions.
- [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md) / [BILINGUAL_CONSISTENCY_REVIEW_ZH.md](./BILINGUAL_CONSISTENCY_REVIEW_ZH.md): P79 manual bilingual consistency pass for paired foundation documents and blocked-boundary alignment.
- [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md) / [FOUNDATION_MAINTENANCE_REVIEW_ZH.md](./FOUNDATION_MAINTENANCE_REVIEW_ZH.md): P80 final foundation maintenance review and stop condition for the P54-P80 cycle.
- [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) / [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md): current open foundation questions and status.
- [RFC_INDEX.md](./RFC_INDEX.md) / [RFC_INDEX_ZH.md](./RFC_INDEX_ZH.md): index for foundation RFC, policy, review, audit, and matrix artifacts.
- [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) / [VISUAL_NAMING_GUIDE_ZH.md](./VISUAL_NAMING_GUIDE_ZH.md): P93 founder-facing vocabulary and Chinese display-name mapping for future visual surfaces.
- [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) / [FOUNDATION_OBSERVATORY_REPORT_ZH.md](./FOUNDATION_OBSERVATORY_REPORT_ZH.md): P94 Markdown founder-facing snapshot, readiness matrix, boundary status, risk heatmap, and next-step recommendation.
- [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md) / [MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md](./MINIMAL_OBSERVATORY_CLI_PLAN_ZH.md): P95 RFC-only plan for a future read-only observatory CLI report boundary.
- [OBSERVATORY_USABILITY_REVIEW.md](./OBSERVATORY_USABILITY_REVIEW.md) / [OBSERVATORY_USABILITY_REVIEW_ZH.md](./OBSERVATORY_USABILITY_REVIEW_ZH.md): P97 founder-facing usability review that led to the P98 readability improvements.
- [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md) / [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md): P99 document-only implementation plan for the P100 no-write `harness-dry-run` pressure-test command.
- [HARNESS_USABILITY_REVIEW.md](./HARNESS_USABILITY_REVIEW.md) / [HARNESS_USABILITY_REVIEW_ZH.md](./HARNESS_USABILITY_REVIEW_ZH.md): P101 review of whether the P100 dry-run helps the founder understand an input path through 01 Core.
- [HARNESS_USABILITY_REVIEW_P108.md](./HARNESS_USABILITY_REVIEW_P108.md) / [HARNESS_USABILITY_REVIEW_P108_ZH.md](./HARNESS_USABILITY_REVIEW_P108_ZH.md): P108 re-review after pressure routing, specialized candidates, review gate specialization, and boundary hardening.
- [HARNESS_ROADMAP.md](./HARNESS_ROADMAP.md) / [HARNESS_ROADMAP_ZH.md](./HARNESS_ROADMAP_ZH.md): P109 roadmap for what `harness-dry-run` can see now, cannot see yet, and may safely plan next as read-only work.
- [OVERNIGHT_HARNESS_WORK_SUMMARY.md](./OVERNIGHT_HARNESS_WORK_SUMMARY.md) / [OVERNIGHT_HARNESS_WORK_SUMMARY_ZH.md](./OVERNIGHT_HARNESS_WORK_SUMMARY_ZH.md): P110 closure summary for P102-P110, including commits, tests, boundaries, usability change, and stop condition.
- [POST_HARNESS_FOUNDER_REVIEW.md](./POST_HARNESS_FOUNDER_REVIEW.md) / [POST_HARNESS_FOUNDER_REVIEW_ZH.md](./POST_HARNESS_FOUNDER_REVIEW_ZH.md): P111 founder review of whether P102-P110 solved P101 and whether a State-Backed Read-Only Harness is an appropriate next boundary.
- [STATE_BACKED_READ_ONLY_HARNESS_RFC.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC.md) / [STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md): P112 boundary RFC for read-only local source backing before any state-backed harness implementation.
- [HARNESS_SOURCE_INVENTORY.md](./HARNESS_SOURCE_INVENTORY.md) / [HARNESS_SOURCE_INVENTORY_ZH.md](./HARNESS_SOURCE_INVENTORY_ZH.md): P113 explicit local Markdown source whitelist and pressure mapping for future read-only source backing.
- [READ_ONLY_SOURCE_LOADER_PLAN.md](./READ_ONLY_SOURCE_LOADER_PLAN.md) / [READ_ONLY_SOURCE_LOADER_PLAN_ZH.md](./READ_ONLY_SOURCE_LOADER_PLAN_ZH.md): P114 implementation plan for a deterministic no-write source loader over the P113 whitelist.
- [SOURCE_LOADER_SAFETY_HARDENING.md](./SOURCE_LOADER_SAFETY_HARDENING.md) / [SOURCE_LOADER_SAFETY_HARDENING_ZH.md](./SOURCE_LOADER_SAFETY_HARDENING_ZH.md): P116 safety validation for the source loader whitelist before CLI or harness integration.
- [SOURCE_BACKED_HARNESS_USABILITY_REVIEW.md](./SOURCE_BACKED_HARNESS_USABILITY_REVIEW.md) / [SOURCE_BACKED_HARNESS_USABILITY_REVIEW_ZH.md](./SOURCE_BACKED_HARNESS_USABILITY_REVIEW_ZH.md): P120 review of whether P112-P119 made the harness source-backed and founder-readable enough to proceed to Core Lockdown / Quarantine planning.
- [CORE_LOCKDOWN_MODE_RFC.md](./CORE_LOCKDOWN_MODE_RFC.md) / [CORE_LOCKDOWN_MODE_RFC_ZH.md](./CORE_LOCKDOWN_MODE_RFC_ZH.md): P121 RFC-only boundary for sandbox/quarantine/candidate handling before future imports, model output, adapters, tools, or rebuild work.
- [IMPORT_QUARANTINE_RFC.md](./IMPORT_QUARANTINE_RFC.md) / [IMPORT_QUARANTINE_RFC_ZH.md](./IMPORT_QUARANTINE_RFC_ZH.md): P122 RFC-only quarantine boundary for future imports from old 01, logs, memory dumps, model output, adapter exports, tool results, or external files.
- [SHADOW_ADAPTER_MODE_RFC.md](./SHADOW_ADAPTER_MODE_RFC.md) / [SHADOW_ADAPTER_MODE_RFC_ZH.md](./SHADOW_ADAPTER_MODE_RFC_ZH.md): P123 RFC-only shadow boundary for observing adapter-shaped input without live integration, ingest, event writes, or platform-owned identity.
- [CONTAMINATION_SCAN_RFC.md](./CONTAMINATION_SCAN_RFC.md) / [CONTAMINATION_SCAN_RFC_ZH.md](./CONTAMINATION_SCAN_RFC_ZH.md): P124 RFC-only scan boundary for future contamination candidate detection without scanner runtime or enforcement.
- [LOCKDOWN_INTEGRATION_READINESS.md](./LOCKDOWN_INTEGRATION_READINESS.md) / [LOCKDOWN_INTEGRATION_READINESS_ZH.md](./LOCKDOWN_INTEGRATION_READINESS_ZH.md): P125 review of whether P121-P124 are coherent enough to continue Core Lockdown / Quarantine planning.
- [LOCKDOWN_FIXTURE_MATRIX.md](./LOCKDOWN_FIXTURE_MATRIX.md) / [LOCKDOWN_FIXTURE_MATRIX_ZH.md](./LOCKDOWN_FIXTURE_MATRIX_ZH.md): P126 synthetic no-write fixture matrix for contamination classes, expected routes, review gates, and forbidden actions.
- [QUARANTINE_REVIEW_GATE_PLAN.md](./QUARANTINE_REVIEW_GATE_PLAN.md) / [QUARANTINE_REVIEW_GATE_PLAN_ZH.md](./QUARANTINE_REVIEW_GATE_PLAN_ZH.md): P127 document-only quarantine gate plan for manual review, evidence rules, and safe outcomes before candidate consideration.
- [SHADOW_ADAPTER_EXAMPLE_SHAPES.md](./SHADOW_ADAPTER_EXAMPLE_SHAPES.md) / [SHADOW_ADAPTER_EXAMPLE_SHAPES_ZH.md](./SHADOW_ADAPTER_EXAMPLE_SHAPES_ZH.md): P128 synthetic adapter-shaped examples for future shadow review without platform connection or ingest.
- [CONTAMINATION_FALSE_POSITIVE_REVIEW.md](./CONTAMINATION_FALSE_POSITIVE_REVIEW.md) / [CONTAMINATION_FALSE_POSITIVE_REVIEW_ZH.md](./CONTAMINATION_FALSE_POSITIVE_REVIEW_ZH.md): P129 review of false-positive risk so future contamination signals do not become truth, punishment, or enforcement.
- [CORE_LOCKDOWN_CYCLE_REVIEW.md](./CORE_LOCKDOWN_CYCLE_REVIEW.md) / [CORE_LOCKDOWN_CYCLE_REVIEW_ZH.md](./CORE_LOCKDOWN_CYCLE_REVIEW_ZH.md): P130 closure review for Core Lockdown / Quarantine readiness, gaps, risks, and next safe planning boundary.
- [FOUNDER_CONSOLE_BOUNDARY_RFC.md](./FOUNDER_CONSOLE_BOUNDARY_RFC.md) / [FOUNDER_CONSOLE_BOUNDARY_RFC_ZH.md](./FOUNDER_CONSOLE_BOUNDARY_RFC_ZH.md): P131 RFC-only boundary for a local, founder-only, no-write visibility surface.
- [FOUNDER_CONSOLE_USER_FLOW.md](./FOUNDER_CONSOLE_USER_FLOW.md) / [FOUNDER_CONSOLE_USER_FLOW_ZH.md](./FOUNDER_CONSOLE_USER_FLOW_ZH.md): P132 document-only founder-console flow from status visibility to preview to manual decision.
- [FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md](./FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md) / [FOUNDER_CONSOLE_NO_WRITE_CONTRACT_ZH.md](./FOUNDER_CONSOLE_NO_WRITE_CONTRACT_ZH.md): P133 no-write contract for future founder-console reads, explicit report outputs, forbidden writes, and verification expectations.
- [FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md](./FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md) / [FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA_ZH.md](./FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA_ZH.md): P134 acceptance criteria for future founder-console visibility, no-write behavior, boundary display, and failure conditions.
- [FOUNDER_CONSOLE_RISK_REVIEW.md](./FOUNDER_CONSOLE_RISK_REVIEW.md) / [FOUNDER_CONSOLE_RISK_REVIEW_ZH.md](./FOUNDER_CONSOLE_RISK_REVIEW_ZH.md): P135 risk review for founder-console product creep, Companion creep, automation, write paths, adapters, model calls, temporal overreach, and capability overreach.
- [FOUNDER_CONSOLE_ROADMAP.md](./FOUNDER_CONSOLE_ROADMAP.md) / [FOUNDER_CONSOLE_ROADMAP_ZH.md](./FOUNDER_CONSOLE_ROADMAP_ZH.md): P136 roadmap closing founder-console planning and deferring implementation until context package contracts exist.
- [CONTEXT_PACKAGE_BUILDER_RFC.md](./CONTEXT_PACKAGE_BUILDER_RFC.md) / [CONTEXT_PACKAGE_BUILDER_RFC_ZH.md](./CONTEXT_PACKAGE_BUILDER_RFC_ZH.md): P137 RFC-only context package contract for future model-as-resource preparation.
- [CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md](./CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md) / [CONTEXT_PACKAGE_PREVIEW_CLI_PLAN_ZH.md](./CONTEXT_PACKAGE_PREVIEW_CLI_PLAN_ZH.md): P138 document-only plan for a future local deterministic read-only context package preview CLI.
- [SOURCE_SELECTION_MATRIX.md](./SOURCE_SELECTION_MATRIX.md) / [SOURCE_SELECTION_MATRIX_ZH.md](./SOURCE_SELECTION_MATRIX_ZH.md): P139 source selection matrix for future context packages, trust levels, omission reasons, and temporal/capability boundaries.
- [BOUNDARY_INJECTION_RFC.md](./BOUNDARY_INJECTION_RFC.md) / [BOUNDARY_INJECTION_RFC_ZH.md](./BOUNDARY_INJECTION_RFC_ZH.md): P140 RFC-only boundary injection contract for future context package boundary and response-strategy packs.
- [CTM_TEMPORAL_CONTEXT_PACK_RFC.md](./CTM_TEMPORAL_CONTEXT_PACK_RFC.md) / [CTM_TEMPORAL_CONTEXT_PACK_RFC_ZH.md](./CTM_TEMPORAL_CONTEXT_PACK_RFC_ZH.md): P141 RFC-only symbolic temporal pack contract for CTM-inspired review cues.
- [CAPABILITY_CONTEXT_PACK_RFC.md](./CAPABILITY_CONTEXT_PACK_RFC.md) / [CAPABILITY_CONTEXT_PACK_RFC_ZH.md](./CAPABILITY_CONTEXT_PACK_RFC_ZH.md): P142 RFC-only capability pack contract for Tool-First candidate/evidence/review context.
- [RESPONSE_ORCHESTRATION_PREVIEW_RFC.md](./RESPONSE_ORCHESTRATION_PREVIEW_RFC.md) / [RESPONSE_ORCHESTRATION_PREVIEW_RFC_ZH.md](./RESPONSE_ORCHESTRATION_PREVIEW_RFC_ZH.md): P143 RFC-only response orchestration preview path with model output treated as untrusted by default.
- [LLM_AS_RESOURCE_BOUNDARY_RFC.md](./LLM_AS_RESOURCE_BOUNDARY_RFC.md) / [LLM_AS_RESOURCE_BOUNDARY_RFC_ZH.md](./LLM_AS_RESOURCE_BOUNDARY_RFC_ZH.md): P144 RFC-only boundary for treating future LLM calls as resource usage rather than subject ownership.
- [POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md](./POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md) / [POST_RESPONSE_CANDIDATE_EXTRACTION_RFC_ZH.md](./POST_RESPONSE_CANDIDATE_EXTRACTION_RFC_ZH.md): P145 RFC-only extraction boundary for future model output as preview-only candidates.
- [MANUAL_REVIEW_GATE_RFC.md](./MANUAL_REVIEW_GATE_RFC.md) / [MANUAL_REVIEW_GATE_RFC_ZH.md](./MANUAL_REVIEW_GATE_RFC_ZH.md): P146 RFC-only manual review gate before any future durable change.
- [REBUILD_MIGRATION_PROTOCOL_RFC.md](./REBUILD_MIGRATION_PROTOCOL_RFC.md) / [REBUILD_MIGRATION_PROTOCOL_RFC_ZH.md](./REBUILD_MIGRATION_PROTOCOL_RFC_ZH.md): P147 RFC-only rebuild migration protocol for future local rebuild entry gates and stop conditions.
- [REBUILD_ENTRY_GATE_CHECKLIST.md](./REBUILD_ENTRY_GATE_CHECKLIST.md) / [REBUILD_ENTRY_GATE_CHECKLIST_ZH.md](./REBUILD_ENTRY_GATE_CHECKLIST_ZH.md): P148 checklist distinguishing ready-for-verification from ready-for-rebuild.
- [PRE_REBUILD_SYSTEM_REVIEW.md](./PRE_REBUILD_SYSTEM_REVIEW.md) / [PRE_REBUILD_SYSTEM_REVIEW_ZH.md](./PRE_REBUILD_SYSTEM_REVIEW_ZH.md): P149 system review concluding the project is ready for final read-only verification, not rebuild.
- [FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md](./FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md) / [FULL_VERIFICATION_PLAN_BEFORE_REBUILD_ZH.md](./FULL_VERIFICATION_PLAN_BEFORE_REBUILD_ZH.md): P150 full read-only verification plan before rebuild.
- [PRE_REBUILD_VERIFICATION_SUITE.md](./PRE_REBUILD_VERIFICATION_SUITE.md) / [PRE_REBUILD_VERIFICATION_SUITE_ZH.md](./PRE_REBUILD_VERIFICATION_SUITE_ZH.md): P151 read-only local verification suite command for checking artifacts, links, forbidden flags, boundaries, and report builders before P152.
- [VERIFICATION_REPORT.md](./VERIFICATION_REPORT.md) / [VERIFICATION_REPORT_ZH.md](./VERIFICATION_REPORT_ZH.md): P152 read-only verification report; passes for founder checkpoint, not rebuild approval.
- [FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md](./FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT.md) / [FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT_ZH.md](./FINAL_PRE_REBUILD_FOUNDER_CHECKPOINT_ZH.md): P153 final founder checkpoint; records that rebuild needs explicit founder approval and has not started.
- [PUSH_READINESS_REPORT.md](./PUSH_READINESS_REPORT.md) / [PUSH_READINESS_REPORT_ZH.md](./PUSH_READINESS_REPORT_ZH.md): P154 audit confirming local `main` is clean, checked, and push-ready after the report commit; it does not execute push or approve rebuild.
- [LINEAGE_BRANCH_GOVERNANCE_RFC.md](./LINEAGE_BRANCH_GOVERNANCE_RFC.md) / [LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md](./LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md): P155 governance-only rules for future lineage, branch, tag, checkpoint, sandbox, quarantine, and selected-return decisions; it does not create a tag, create a branch, push, or start rebuild.
- [BASELINE_TAGGING_PLAN.md](./BASELINE_TAGGING_PLAN.md) / [BASELINE_TAGGING_PLAN_ZH.md](./BASELINE_TAGGING_PLAN_ZH.md): P156 planning-only candidate baseline tag, milestone tag, and branch creation plan for founder review; it does not create tags, create branches, push, modify git history, or start rebuild.
- [BASELINE_TAGGING_FOUNDER_REVIEW.md](./BASELINE_TAGGING_FOUNDER_REVIEW.md) / [BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md](./BASELINE_TAGGING_FOUNDER_REVIEW_ZH.md): P157 founder review of P156 tag and branch candidates, including confidence, risk, confirmation needs, and recommendations; it does not create tags, branches, or rebuild work.
- [MANUAL_TAG_BRANCH_COMMAND_SHEET.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET.md) / [MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md](./MANUAL_TAG_BRANCH_COMMAND_SHEET_ZH.md): P158 manual command draft sheet for future human tag/branch operations; it does not run commands, create tags, create branches, push tags, push main, or start rebuild.
- [FINAL_PRE_REBUILD_PUSH_READINESS.md](./FINAL_PRE_REBUILD_PUSH_READINESS.md) / [FINAL_PRE_REBUILD_PUSH_READINESS_ZH.md](./FINAL_PRE_REBUILD_PUSH_READINESS_ZH.md): P159 final push-readiness audit before any rebuild; it recommends GitHub `main` push only and does not push, create tags, create branches, or start rebuild.
- [PUSH_TO_GITHUB_REPORT.md](./PUSH_TO_GITHUB_REPORT.md) / [PUSH_TO_GITHUB_REPORT_ZH.md](./PUSH_TO_GITHUB_REPORT_ZH.md): P160 report for the main-only GitHub push; it records no tag creation, no branch creation, no tag push, and no rebuild.
- [FINAL_PRE_REBUILD_READY_REVIEW.md](./FINAL_PRE_REBUILD_READY_REVIEW.md) / [FINAL_PRE_REBUILD_READY_REVIEW_ZH.md](./FINAL_PRE_REBUILD_READY_REVIEW_ZH.md): final review of whether manual baseline tags/branches and local-only rebuild trial preparation may proceed after founder confirmation.
- [SCENARIO_PROFILE_TEST_MATRIX.md](./SCENARIO_PROFILE_TEST_MATRIX.md) / [SCENARIO_PROFILE_TEST_MATRIX_ZH.md](./SCENARIO_PROFILE_TEST_MATRIX_ZH.md): P104 expected pressure profiles, candidates, boundaries, and next steps for `harness-dry-run`.
- [AUTONOMOUS_WORK_SUMMARY.md](./AUTONOMOUS_WORK_SUMMARY.md) / [AUTONOMOUS_WORK_SUMMARY_ZH.md](./AUTONOMOUS_WORK_SUMMARY_ZH.md): latest autonomous foundation work summary and next safe direction.

## Foundation Review Artifacts

Use these when checking whether new foundation work is still inside the guardrails:

- [FOUNDATION_INTEGRITY_AUDIT.md](./FOUNDATION_INTEGRITY_AUDIT.md) / [FOUNDATION_INTEGRITY_AUDIT_ZH.md](./FOUNDATION_INTEGRITY_AUDIT_ZH.md): P54 integrity audit for foundation principles, boundaries, and overlap risks.
- [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md) / [CONCEPT_OVERLAP_REVIEW_ZH.md](./CONCEPT_OVERLAP_REVIEW_ZH.md): P55 concept overlap reduction for foundation ownership boundaries.
- [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) / [BOUNDARY_TEST_MATRIX_ZH.md](./BOUNDARY_TEST_MATRIX_ZH.md): P56 document-level matrix for allowed and forbidden foundation outputs.
- [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) / [OPEN_QUESTIONS_TRIAGE_ZH.md](./OPEN_QUESTIONS_TRIAGE_ZH.md): P57 triage of open questions into safe RFC order and blocked runtime work.
- [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) / [FOUNDATION_REVIEW_CHECKLIST_ZH.md](./FOUNDATION_REVIEW_CHECKLIST_ZH.md): P76 human review gate for phase scope, invariants, risks, bilingual consistency, verification, and commit review.
- [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md) / [BILINGUAL_CONSISTENCY_REVIEW_ZH.md](./BILINGUAL_CONSISTENCY_REVIEW_ZH.md): P79 record of pair presence, reciprocal links, status alignment, and bilingual blocked-boundary checks.
- [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md) / [FOUNDATION_MAINTENANCE_REVIEW_ZH.md](./FOUNDATION_MAINTENANCE_REVIEW_ZH.md): P80 closure review for maintained artifacts, residual gaps, residual risks, and future options.

## Future RFC And Policy Artifacts

These documents define review surfaces and future contracts. They do not approve execution:

- [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) / [TEMPORAL_AWARENESS_RFC_ZH.md](./TEMPORAL_AWARENESS_RFC_ZH.md): P58 document-only RFC for elapsed time as future subject-state transition evidence.
- [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) / [RECALL_EVENT_WRITE_POLICY_RFC_ZH.md](./RECALL_EVENT_WRITE_POLICY_RFC_ZH.md): P59 document-only RFC for future recall event write policy boundaries.
- [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) / [STATEFUL_MEMORY_ENCODING_POLICY_ZH.md](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md): P60 policy for minimum safe encoding references before meaning-shift review.
- [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) / [GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md): P61 document-only RFC for growth candidate review-object lifecycle boundaries.
- [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) / [PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md): P62 boundary RFC for productive drift, random drift, identity-threatening drift, and collapse.
- [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) / [EXPLORATION_SERENDIPITY_RFC_ZH.md](./EXPLORATION_SERENDIPITY_RFC_ZH.md): P63 document-only RFC for exploration and serendipity signal boundaries.
- [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) / [SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md](./SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md): P64 boundary RFC for protected subject kernel and evolvable world seed.
- [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) / [RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md): P65 document-only contract RFC for future reconstruction reducers before any reducer execution.
- [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) / [PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md): P66 document-only policy RFC for target-path payload, diff, snapshot, and reference-only treatment.

## Original Research Base

Use these for the project vision, theory, and early architecture:

- [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md): the full research vision for Persistent Intelligence, State Transfer, Dream Engine, Memory Lifecycle, Identity Growth, and Cognitive Ecology.
- [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) / [RESEARCH_NOTES_INDEX_ZH.md](./RESEARCH_NOTES_INDEX_ZH.md): P78 source-note index mapping original idea chains to current foundation documents.
- [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md): the theory of artificial life history, including false assigned history, generated history, and identity seed.
- [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md): Chinese research notes preserving the two original idea chains in detail.
- [NON_CLAIMS.md](./NON_CLAIMS.md) / [NON_CLAIMS_ZH.md](./NON_CLAIMS_ZH.md): what the project does not claim, including consciousness, biological emotion, and personhood.
- [ARCHITECTURE.md](./ARCHITECTURE.md) / [ARCHITECTURE_ZH.md](./ARCHITECTURE_ZH.md): a first technical architecture for identity-first persistent agents.
- [STATE_SCHEMA.md](./STATE_SCHEMA.md) / [STATE_SCHEMA_ZH.md](./STATE_SCHEMA_ZH.md): a concrete state-transfer schema for identity, memory, tasks, affective state, conflicts, and update logs.
- [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md) / [DREAM_ENGINE_SPEC_ZH.md](./DREAM_ENGINE_SPEC_ZH.md): the proposed offline reflection and consolidation process.
- [EVALUATION.md](./EVALUATION.md) / [EVALUATION_ZH.md](./EVALUATION_ZH.md): how to test persistence, drift, memory lifecycle quality, and identity continuity.
- [LITERATURE_MAP.md](./LITERATURE_MAP.md) / [LITERATURE_MAP_ZH.md](./LITERATURE_MAP_ZH.md): related work in LLM agents, cognitive architecture, psychology, neuroscience, and continual learning.
- [THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md) / [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md): synthesis of current gaps, external theory, and the P7-P13 implementation plan.

## Runtime And Adapter References

These describe existing prototype surfaces. They are not current foundation work:

- [IMPLEMENTATION_START.md](./IMPLEMENTATION_START.md) / [IMPLEMENTATION_START_ZH.md](./IMPLEMENTATION_START_ZH.md): the first runnable local 01 Core prototype.
- [MEMORY_IMPORT.md](./MEMORY_IMPORT.md) / [MEMORY_IMPORT_ZH.md](./MEMORY_IMPORT_ZH.md): how to import memories from AstrBot, Angel Memory, or other systems as generic text.
- [API.md](./API.md) / [API_ZH.md](./API_ZH.md): local HTTP API for adapters such as AstrBot.
- [ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) / [ADAPTER_PROTOCOL_ZH.md](./ADAPTER_PROTOCOL_ZH.md): generic adapter protocol. Stabilize the local generic version before AstrBot specialization.
- [adapters/astrbot/astrbot_plugin_01_core](./adapters/astrbot/astrbot_plugin_01_core): first AstrBot adapter. AstrBot is the entrance; 01 Core owns continuity state.
- [CLOUD_DEPLOYMENT.md](./CLOUD_DEPLOYMENT.md) / [CLOUD_DEPLOYMENT_ZH.md](./CLOUD_DEPLOYMENT_ZH.md): deploy 01 Core as a persistent cloud service.

Documentation policy:

> Future documents should be drafted in Chinese first, then mirrored in English. The English versions are preserved because many technical terms in this research program remain most precise in English.

The central claim:

> Continuity is not memory retrieval.
> Continuity is state transfer through time.

01 is not intended to be the strongest model, a super-agent, or a fictional character with a prewritten biography.

01 is an **Identity Seed**: a first experiment in giving intelligence a starting point, a direction, a world, and enough continuity to grow a life history of its own.

## Prototype Reference

This repository includes a minimal local prototype. The observatory CLI remains
read-only after P98 readability improvements. P102 keeps `harness-dry-run` as a
local dry-run preview surface and adds deterministic scenario routing. It is
still not a chat application, product layer, Companion, adapter, model caller,
retrieval engine, event writer, or memory writer. The other commands remain
verification and orientation references only:

```bash
python3 -m one_core.cli init
python3 -m one_core.cli interact "We begin implementing 01 Core."
python3 -m one_core.cli dream
python3 -m one_core.cli status
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
```

It stores state under `work/01_state` by default.

Read-only founder-facing observatory report:

```bash
python3 -m one_core.cli foundation-observatory-report
python3 -m one_core.cli foundation-observatory-report --format json
python3 -m one_core.cli foundation-observatory-report --lang zh
```

This command reads approved foundation documents and emits a static report. It
does not mutate state, execute policy, create roadmap phases, implement a
harness, or become a dashboard runtime.

Read-only harness dry-run:

```bash
python3 -m one_core.cli harness-dry-run --input "Preview this without writing state."
python3 -m one_core.cli harness-dry-run --input "只做预览，不写 state。" --lang zh
python3 -m one_core.cli harness-dry-run --input "Preview this." --format json
```

This command emits intake, context package, candidate, review queue, boundary,
observatory, scenario routing, and non-execution previews. It classifies inputs
into pressure profiles such as observability, growth review, adapter boundary,
product layer, capability evolution, temporal, reconstruction, or unknown. It
now cites pressure-specific whitelisted Markdown source refs inside
`context_package_preview`, including source-backed risk and open-question refs;
it does not write state, call a model, call external APIs, integrate adapters,
run retrieval, execute policy, or execute the next step.

Read-only harness source inventory:

```bash
python3 -m one_core.cli harness-source-inventory
python3 -m one_core.cli harness-source-inventory --format json
python3 -m one_core.cli harness-source-inventory --lang zh
```

This command reports the approved local Markdown source whitelist plus pressure,
risk, and open-question mappings used by future state-backed read-only harness
work. It only cites source IDs and safety metadata; it does not read
user-supplied paths, write state, execute retrieval, call a model, execute
policy, or authorize rebuild work.

Read-only pre-rebuild verification suite:

```bash
python3 -m one_core.cli pre-rebuild-verification
python3 -m one_core.cli pre-rebuild-verification --format json
python3 -m one_core.cli pre-rebuild-verification --lang zh
```

This command checks required P112-P151 artifacts, README/index coverage, local
Markdown links, active forbidden true flags, existing read-only report builders,
CTM boundaries, Tool-First boundaries, and rebuild boundaries. It does not run
rebuild, call a model, connect adapters, write state, or approve P152/P153/P154/P155/P156/P157/P158/P159/P160.

Local API reference:

```bash
python3 -m one_core.cli serve
```

AstrBot adapter reference:

```bash
cp -R adapters/astrbot/astrbot_plugin_01_core /root/data/plugins/
```

Then use:

```text
/01 ping
/01 status
/01 chat <message>
/01 dream
```

Generic adapter protocol reference:

```bash
python3 -m one_core.cli remote health
python3 -m one_core.cli remote adapters
python3 -m one_core.cli remote interact "Continue 01 Core."
python3 -m one_core.cli remote status
```

```text
01 Project

We are not trying to build a smarter model.
We are trying to build an intelligence that can pass through time,
carry a life history,
and remain recognizably itself.
```
