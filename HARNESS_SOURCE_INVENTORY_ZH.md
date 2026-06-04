# Harness Source Inventory / 试验台来源清单

English version: [HARNESS_SOURCE_INVENTORY.md](./HARNESS_SOURCE_INVENTORY.md)

状态：`P113`、`inventory`、`document-only`、`non-runtime`。

P113 定义 future state-backed read-only harness 的第一版 source whitelist。它不实现 source loading、
CLI commands、retrieval、state reads、state writes、model calls、adapters、memory writes、recall
writes、identity mutation、tool execution 或 rebuild。

## 清单规则

```text
只有显式列出的本地 Markdown sources 可以支撑 harness。
source refs 用来解释 previews。
source refs 不是 retrieval、memory activation、prompt construction 或 truth。
```

## Source Classes

| Class | 在 Harness 中的用途 | 边界 |
|---|---|---|
| `foundation_status` | 解释项目是什么、哪些地基稳定。 | 不是 implementation approval。 |
| `governance_boundary` | 解释禁止事项、风险和 open questions。 | 不是 policy execution。 |
| `harness_boundary` | 解释 dry-run intake、context、candidates 和 review gates。 | 不扩展 harness runtime。 |
| `temporal_ctm_boundary` | 符号化解释 CTM-inspired temporal concepts。 | 不是 CTM runtime、thought loop 或 temporal event write。 |
| `capability_boundary` | 解释 tool-first self-evolution 和 capability review。 | 不是 tool execution、authorization 或 promotion。 |
| `reconstruction_boundary` | 解释 replay、payload/diff 和 reducer boundaries。 | 不是 reducer execution 或 event compaction。 |
| `founder_readability` | 解释 founder-facing names、observatory 和 usability findings。 | 不是 UI、dashboard runtime 或 product layer。 |

## Approved Source Whitelist

| Source ID | English Path | Chinese Path | Class | Pressure Types | Research Line | Why It Is Allowed |
|---|---|---|---|---|---|---|
| `phase_index` | [PHASE_INDEX.md](./PHASE_INDEX.md) | [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md) | `foundation_status` | all | both | current status 和 phase provenance。 |
| `foundation` | [FOUNDATION.md](./FOUNDATION.md) | [FOUNDATION_ZH.md](./FOUNDATION_ZH.md) | `foundation_status` | all | both | 稳定 project invariants 和 stage order。 |
| `foundation_status` | [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) | [FOUNDATION_STATUS_ZH.md](./FOUNDATION_STATUS_ZH.md) | `foundation_status` | observability, product | both | 已有什么、缺什么、什么被后推。 |
| `concept_map` | [CONCEPT_MAP.md](./CONCEPT_MAP.md) | [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md) | `foundation_status` | all | both | 跨层概念关系。 |
| `architecture_boundaries` | [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md) | `governance_boundary` | growth, temporal, reconstruction, product | both | identity、memory、growth、temporal、reconstruction、governance、product 边界。 |
| `glossary` | [GLOSSARY.md](./GLOSSARY.md) | [GLOSSARY_ZH.md](./GLOSSARY_ZH.md) | `foundation_status` | all | both | 共享词汇和 anti-misreading boundaries。 |
| `open_questions` | [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md) | `governance_boundary` | all | both | active unresolved questions 和 deferred risks。 |
| `risk_register` | [RISK_REGISTER.md](./RISK_REGISTER.md) | [RISK_REGISTER_ZH.md](./RISK_REGISTER_ZH.md) | `governance_boundary` | all | both | 当前 risk signals 和 mitigations。 |
| `rfc_index` | [RFC_INDEX.md](./RFC_INDEX.md) | [RFC_INDEX_ZH.md](./RFC_INDEX_ZH.md) | `governance_boundary` | all | both | RFC-only artifacts 和 non-execution status 导航。 |
| `boundary_test_matrix` | [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | [BOUNDARY_TEST_MATRIX_ZH.md](./BOUNDARY_TEST_MATRIX_ZH.md) | `governance_boundary` | all | both | allowed / forbidden outputs expectations。 |
| `visual_naming` | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) | [VISUAL_NAMING_GUIDE_ZH.md](./VISUAL_NAMING_GUIDE_ZH.md) | `founder_readability` | observability, product | both | founder-facing display names，不实现 UI。 |
| `observatory_report` | [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) | [FOUNDATION_OBSERVATORY_REPORT_ZH.md](./FOUNDATION_OBSERVATORY_REPORT_ZH.md) | `founder_readability` | observability | both | static founder-facing status snapshot。 |
| `minimal_cli_harness_plan` | [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md) | [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md) | `harness_boundary` | all | both | 原始 no-write dry-run scope。 |
| `thin_interaction_harness` | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | [THIN_INTERACTION_HARNESS_RFC_ZH.md](./THIN_INTERACTION_HARNESS_RFC_ZH.md) | `harness_boundary` | all | both | implementation 前的 preview-only harness boundary。 |
| `conversation_intake` | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | [CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md](./CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md) | `harness_boundary` | all | both | intake envelope vocabulary，不做 adapter ingest 或 event writes。 |
| `context_preview` | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | [CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md](./CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md) | `harness_boundary` | all | both | context preview vocabulary，不执行 retrieval。 |
| `review_queue_preview` | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | [REVIEW_QUEUE_PREVIEW_RFC_ZH.md](./REVIEW_QUEUE_PREVIEW_RFC_ZH.md) | `harness_boundary` | all | both | review queue preview vocabulary，不执行 lifecycle。 |
| `scenario_profile_matrix` | [SCENARIO_PROFILE_TEST_MATRIX.md](./SCENARIO_PROFILE_TEST_MATRIX.md) | [SCENARIO_PROFILE_TEST_MATRIX_ZH.md](./SCENARIO_PROFILE_TEST_MATRIX_ZH.md) | `harness_boundary` | all | both | expected pressure profiles、candidates、boundaries 和 next steps。 |
| `harness_usability_p101` | [HARNESS_USABILITY_REVIEW.md](./HARNESS_USABILITY_REVIEW.md) | [HARNESS_USABILITY_REVIEW_ZH.md](./HARNESS_USABILITY_REVIEW_ZH.md) | `founder_readability` | all | both | 6.5/10 baseline usability problems。 |
| `harness_usability_p108` | [HARNESS_USABILITY_REVIEW_P108.md](./HARNESS_USABILITY_REVIEW_P108.md) | [HARNESS_USABILITY_REVIEW_P108_ZH.md](./HARNESS_USABILITY_REVIEW_P108_ZH.md) | `founder_readability` | all | both | 8.0/10 re-review 和 remaining static source gap。 |
| `harness_roadmap` | [HARNESS_ROADMAP.md](./HARNESS_ROADMAP.md) | [HARNESS_ROADMAP_ZH.md](./HARNESS_ROADMAP_ZH.md) | `harness_boundary` | all | both | P109 后 harness 能看见和不能看见什么。 |
| `post_harness_founder_review` | [POST_HARNESS_FOUNDER_REVIEW.md](./POST_HARNESS_FOUNDER_REVIEW.md) | [POST_HARNESS_FOUNDER_REVIEW_ZH.md](./POST_HARNESS_FOUNDER_REVIEW_ZH.md) | `founder_readability` | all | both | P111 判断 narrow state-backed read-only 合适。 |
| `state_backed_read_only_harness` | [STATE_BACKED_READ_ONLY_HARNESS_RFC.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC.md) | [STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md) | `harness_boundary` | all | both | P112 whitelisted local source citation boundary。 |
| `temporal_awareness` | [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | [TEMPORAL_AWARENESS_RFC_ZH.md](./TEMPORAL_AWARENESS_RFC_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | elapsed time future review vocabulary，不是 runtime。 |
| `ctm_temporal_dynamics` | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | [CTM_TEMPORAL_DYNAMICS_RFC_ZH.md](./CTM_TEMPORAL_DYNAMICS_RFC_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | symbolic CTM-inspired mapping，不是 neural CTM 或 training。 |
| `temporal_coherence_eval` | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | [TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | deterministic evaluation plan，不是 temporal runtime。 |
| `deliberation_tick` | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | [DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md) | `temporal_ctm_boundary` | temporal, growth, capability | CTM-inspired Temporal Dynamics | review depth 和 tick vocabulary，不执行 thought loop。 |
| `thought_trace_storage` | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | [THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | trace storage boundary，不捕获 hidden chain-of-thought。 |
| `session_resume` | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) | [SESSION_RESUME_SCENARIO_PLAN_ZH.md](./SESSION_RESUME_SCENARIO_PLAN_ZH.md) | `temporal_ctm_boundary` | temporal | CTM-inspired Temporal Dynamics | resume scenarios，不写 temporal events。 |
| `tool_first_self_evolution` | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) | [TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md) | `capability_boundary` | capability | Tool-First In-Situ Self-Evolution | tool-first capability vocabulary，不执行工具。 |
| `capability_evolution_boundary` | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) | [CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md) | `capability_boundary` | capability | Tool-First In-Situ Self-Evolution | verification 不是 authorization；tool candidate 不是 promotion。 |
| `stateful_memory_policy` | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | [STATEFUL_MEMORY_ENCODING_POLICY_ZH.md](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md) | `governance_boundary` | growth, temporal | both | meaning-shift review 前的最小 encoding policy。 |
| `growth_candidate_lifecycle` | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | [GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md) | `governance_boundary` | growth | both | review-object lifecycle vocabulary，不执行 growth。 |
| `productive_drift` | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | [PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md) | `governance_boundary` | growth | both | drift vocabulary，不做 automatic drift classification。 |
| `reconstruction_reducer_contract` | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) | [RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md) | `reconstruction_boundary` | reconstruction | both | future reducer contract，不执行 reducer。 |
| `payload_diff_policy` | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md) | `reconstruction_boundary` | reconstruction | both | payload/diff vocabulary，不 capture 或 compact。 |

## Explicitly Disallowed Sources / 明确禁止来源

source loader 不得读取：

- 用户提供的任意路径；
- hidden files 或 directories；
- `.env`、credential、cookie、token 或 key files；
- `work/01_state` JSON/JSONL state logs；
- imported memory dumps；
- `adapters/` content；
- cloud deployment secrets 或 server state；
- network URLs；
- AstrBot、Telegram、QQ、Web 或其他 platform exports；
- binary files；
- generated cache files；
- repository root 之外的文件。

## Pressure Type 映射

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

## P114 输入

P114 应把这份 inventory 转成 read-only loader plan：

- explicit whitelist constants；
- paired English/Chinese path support；
- 只做 heading 和 excerpt extraction；
- 不接受 user path input；
- 不写入；
- no external IO；
- 不声称 source-derived authority；
- deterministic output order；
- 测试证明 state 和 source files 都 unchanged。

## 非授权声明

P113 不实现 loading。它不授权 broad file access、真实 retrieval、state reads、state writes、prompt
construction、model calls、adapter integration、tool execution、CTM runtime、temporal runtime、recall
writes、identity mutation、memory rewrite、product work 或 rebuild。
