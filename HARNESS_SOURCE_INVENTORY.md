# Harness Source Inventory

Chinese version: [HARNESS_SOURCE_INVENTORY_ZH.md](./HARNESS_SOURCE_INVENTORY_ZH.md)

Status: `P113`, `inventory`, `document-only`, `non-runtime`.

P113 defines the first source whitelist for the future state-backed read-only
harness. It does not implement source loading, CLI commands, retrieval, state
reads, state writes, model calls, adapters, memory writes, recall writes,
identity mutation, tool execution, or rebuild.

## Inventory Rule

```text
only explicit local Markdown sources can back the harness.
source refs explain previews.
source refs are not retrieval, memory activation, prompt construction, or truth.
```

## Source Classes

| Class | Use In Harness | Boundary |
|---|---|---|
| `foundation_status` | Explain what the project is and what is stable. | Not implementation approval. |
| `governance_boundary` | Explain forbidden actions, risks, and open questions. | Not policy execution. |
| `harness_boundary` | Explain dry-run intake, context, candidates, and review gates. | Not harness runtime expansion. |
| `temporal_ctm_boundary` | Explain CTM-inspired temporal concepts symbolically. | Not CTM runtime, thought loop, or temporal event write. |
| `capability_boundary` | Explain tool-first self-evolution and capability review. | Not tool execution, authorization, or promotion. |
| `reconstruction_boundary` | Explain replay, payload/diff, and reducer boundaries. | Not reducer execution or event compaction. |
| `founder_readability` | Explain founder-facing names, observatory, and usability findings. | Not UI, dashboard runtime, or product layer. |

## Approved Source Whitelist

| Source ID | English Path | Chinese Path | Class | Pressure Types | Research Line | Why It Is Allowed |
|---|---|---|---|---|---|---|
| `phase_index` | [PHASE_INDEX.md](./PHASE_INDEX.md) | [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md) | `foundation_status` | all | both | Phase map for current status and provenance. |
| `foundation` | [FOUNDATION.md](./FOUNDATION.md) | [FOUNDATION_ZH.md](./FOUNDATION_ZH.md) | `foundation_status` | all | both | Stable project invariants and stage order. |
| `foundation_status` | [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) | [FOUNDATION_STATUS_ZH.md](./FOUNDATION_STATUS_ZH.md) | `foundation_status` | observability, product | both | What exists, what is missing, and what is pushed back. |
| `concept_map` | [CONCEPT_MAP.md](./CONCEPT_MAP.md) | [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md) | `foundation_status` | all | both | Cross-layer concept relationships. |
| `architecture_boundaries` | [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md) | `governance_boundary` | growth, temporal, reconstruction, product | both | Boundary ownership across identity, memory, growth, temporal, reconstruction, governance, and product layers. |
| `glossary` | [GLOSSARY.md](./GLOSSARY.md) | [GLOSSARY_ZH.md](./GLOSSARY_ZH.md) | `foundation_status` | all | both | Shared vocabulary and anti-misreading boundaries. |
| `open_questions` | [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md) | `governance_boundary` | all | both | Active unresolved questions and deferred risks. |
| `risk_register` | [RISK_REGISTER.md](./RISK_REGISTER.md) | [RISK_REGISTER_ZH.md](./RISK_REGISTER_ZH.md) | `governance_boundary` | all | both | Current risk signals and mitigations. |
| `rfc_index` | [RFC_INDEX.md](./RFC_INDEX.md) | [RFC_INDEX_ZH.md](./RFC_INDEX_ZH.md) | `governance_boundary` | all | both | Navigation for RFC-only artifacts and their non-execution status. |
| `boundary_test_matrix` | [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | [BOUNDARY_TEST_MATRIX_ZH.md](./BOUNDARY_TEST_MATRIX_ZH.md) | `governance_boundary` | all | both | Boundary expectations for allowed and forbidden outputs. |
| `visual_naming` | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) | [VISUAL_NAMING_GUIDE_ZH.md](./VISUAL_NAMING_GUIDE_ZH.md) | `founder_readability` | observability, product | both | Founder-facing display names without UI implementation. |
| `observatory_report` | [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) | [FOUNDATION_OBSERVATORY_REPORT_ZH.md](./FOUNDATION_OBSERVATORY_REPORT_ZH.md) | `founder_readability` | observability | both | Static founder-facing status snapshot. |
| `minimal_cli_harness_plan` | [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md) | [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md) | `harness_boundary` | all | both | Defines the original no-write dry-run scope. |
| `thin_interaction_harness` | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | [THIN_INTERACTION_HARNESS_RFC_ZH.md](./THIN_INTERACTION_HARNESS_RFC_ZH.md) | `harness_boundary` | all | both | Harness preview-only boundary before implementation. |
| `conversation_intake` | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | [CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md](./CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md) | `harness_boundary` | all | both | Intake envelope vocabulary without adapter ingest or event writes. |
| `context_preview` | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | [CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md](./CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md) | `harness_boundary` | all | both | Context preview vocabulary without retrieval execution. |
| `review_queue_preview` | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | [REVIEW_QUEUE_PREVIEW_RFC_ZH.md](./REVIEW_QUEUE_PREVIEW_RFC_ZH.md) | `harness_boundary` | all | both | Review queue preview vocabulary without lifecycle execution. |
| `scenario_profile_matrix` | [SCENARIO_PROFILE_TEST_MATRIX.md](./SCENARIO_PROFILE_TEST_MATRIX.md) | [SCENARIO_PROFILE_TEST_MATRIX_ZH.md](./SCENARIO_PROFILE_TEST_MATRIX_ZH.md) | `harness_boundary` | all | both | Expected pressure profiles, candidates, boundaries, and next steps. |
| `harness_usability_p101` | [HARNESS_USABILITY_REVIEW.md](./HARNESS_USABILITY_REVIEW.md) | [HARNESS_USABILITY_REVIEW_ZH.md](./HARNESS_USABILITY_REVIEW_ZH.md) | `founder_readability` | all | both | Baseline 6.5/10 usability problems. |
| `harness_usability_p108` | [HARNESS_USABILITY_REVIEW_P108.md](./HARNESS_USABILITY_REVIEW_P108.md) | [HARNESS_USABILITY_REVIEW_P108_ZH.md](./HARNESS_USABILITY_REVIEW_P108_ZH.md) | `founder_readability` | all | both | Re-review showing 8.0/10 and remaining static source gap. |
| `harness_roadmap` | [HARNESS_ROADMAP.md](./HARNESS_ROADMAP.md) | [HARNESS_ROADMAP_ZH.md](./HARNESS_ROADMAP_ZH.md) | `harness_boundary` | all | both | What harness can see and cannot see after P109. |
| `post_harness_founder_review` | [POST_HARNESS_FOUNDER_REVIEW.md](./POST_HARNESS_FOUNDER_REVIEW.md) | [POST_HARNESS_FOUNDER_REVIEW_ZH.md](./POST_HARNESS_FOUNDER_REVIEW_ZH.md) | `founder_readability` | all | both | P111 decision that state-backed read-only is appropriate if narrow. |
| `state_backed_read_only_harness` | [STATE_BACKED_READ_ONLY_HARNESS_RFC.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC.md) | [STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md) | `harness_boundary` | all | both | P112 boundary for whitelisted local source citation. |
| `temporal_awareness` | [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | [TEMPORAL_AWARENESS_RFC_ZH.md](./TEMPORAL_AWARENESS_RFC_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | Elapsed time as future review vocabulary, not runtime. |
| `ctm_temporal_dynamics` | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | [CTM_TEMPORAL_DYNAMICS_RFC_ZH.md](./CTM_TEMPORAL_DYNAMICS_RFC_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | Symbolic CTM-inspired mapping without neural CTM or training. |
| `temporal_coherence_eval` | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | [TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | Deterministic evaluation plan without temporal runtime. |
| `deliberation_tick` | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | [DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md) | `temporal_ctm_boundary` | temporal, growth, capability | CTM-inspired Temporal Dynamics | Review depth and tick vocabulary without thought loops. |
| `thought_trace_storage` | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | [THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | Trace storage boundary without hidden chain-of-thought capture. |
| `session_resume` | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) | [SESSION_RESUME_SCENARIO_PLAN_ZH.md](./SESSION_RESUME_SCENARIO_PLAN_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | Resume scenarios without temporal event writes. |
| `tool_first_self_evolution` | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) | [TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md) | `capability_boundary` | capability | Tool-First In-Situ Self-Evolution | Tool-first capability vocabulary without tool execution. |
| `capability_evolution_boundary` | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) | [CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md) | `capability_boundary` | capability | Tool-First In-Situ Self-Evolution | Verification is not authorization; tool candidate is not promotion. |
| `stateful_memory_policy` | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | [STATEFUL_MEMORY_ENCODING_POLICY_ZH.md](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md) | `governance_boundary` | growth, temporal | both | Minimal encoding policy before meaning-shift review. |
| `growth_candidate_lifecycle` | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | [GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md) | `governance_boundary` | growth | both | Review-object lifecycle vocabulary without growth execution. |
| `productive_drift` | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | [PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md) | `governance_boundary` | growth | both | Drift vocabulary without automatic drift classification. |
| `reconstruction_reducer_contract` | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) | [RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md) | `reconstruction_boundary` | reconstruction | both | Future reducer contract without reducer execution. |
| `payload_diff_policy` | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md) | `reconstruction_boundary` | reconstruction | both | Payload/diff vocabulary without capture or compaction. |

## Explicitly Disallowed Sources

The source loader must not read:

- user-supplied arbitrary paths;
- hidden files or directories;
- `.env`, credential, cookie, token, or key files;
- `work/01_state` JSON/JSONL state logs;
- imported memory dumps;
- `adapters/` content;
- cloud deployment secrets or server state;
- network URLs;
- AstrBot, Telegram, QQ, Web, or other platform exports;
- binary files;
- generated cache files;
- files outside the repository root.

## Mapping To Pressure Types

| Pressure Type | Primary Source IDs |
|---|---|
| `observability_pressure` | `foundation_status`, `phase_index`, `observatory_report`, `visual_naming`, `harness_usability_p108` |
| `growth_review_pressure` | `growth_candidate_lifecycle`, `productive_drift`, `stateful_memory_policy`, `architecture_boundaries` |
| `adapter_boundary_pressure` | `architecture_boundaries`, `thin_interaction_harness`, `conversation_intake`, `state_backed_read_only_harness` |
| `product_layer_pressure` | `foundation_status`, `visual_naming`, `architecture_boundaries`, `risk_register` |
| `capability_evolution_pressure` | `tool_first_self_evolution`, `capability_evolution_boundary`, `deliberation_tick`, `risk_register` |
| `temporal_pressure` | `temporal_awareness`, `ctm_temporal_dynamics`, `temporal_coherence_eval`, `deliberation_tick`, `thought_trace_storage`, `session_resume` |
| `reconstruction_pressure` | `reconstruction_reducer_contract`, `payload_diff_policy`, `boundary_test_matrix`, `architecture_boundaries` |
| `unknown_pressure` | `foundation`, `open_questions`, `risk_register`, `boundary_test_matrix` |

## P114 Input

P114 should turn this inventory into a read-only loader plan:

- explicit whitelist constants;
- paired English/Chinese path support;
- heading and excerpt extraction only;
- no user path input;
- no writes;
- no external IO;
- no source-derived authority claims;
- deterministic output order;
- tests proving state and source files are unchanged.

## Non-Authorization

P113 does not implement loading. It does not authorize broad file access, real
retrieval, state reads, state writes, prompt construction, model calls, adapter
integration, tool execution, CTM runtime, temporal runtime, recall writes,
identity mutation, memory rewrite, product work, or rebuild.
