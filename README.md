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

Current work status: P103 Harness Output Readability Improvement is complete.
The local read-only `harness-dry-run` command now starts with a founder-facing
summary, human-readable risks, classification reason, next-step guidance, and
"do not do yet" guardrails while staying dry-run only.

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
- [PHASE_INDEX.md](./PHASE_INDEX.md) / [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md): P0-P103 foundation phase index by proposition and main line.
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
does not write state, call a model, call external APIs, integrate adapters, run
retrieval, or execute the next step.

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
