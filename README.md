# 01 Project

**How Can Intelligence Persist Through Time?**

[中文 README](./README_ZH.md)

01 Project is a research program about persistent intelligence: how an AI system can remain continuous across conversations, tasks, memories, dreams, conflicts, and social interactions.

The project begins from a simple problem:

> Existing AI systems restart too easily.

Even when a model is powerful, its context is long, and its agent loop is complex, it can still lose state, drift in identity, forget long-term intent, or become a different behavioral subject across time.

This repository records the foundational documents and the first engineering frame:

- [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md): the full research vision for Persistent Intelligence, State Transfer, Dream Engine, Memory Lifecycle, Identity Growth, and Cognitive Ecology.
- [FOUNDATION.md](./FOUNDATION.md) / [FOUNDATION_ZH.md](./FOUNDATION_ZH.md): the project-level engineering foundation: boundaries, invariants, and stage order that future implementation must obey.
- [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md): the theory of artificial life history, including false assigned history, generated history, and identity seed.
- [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md): Chinese research notes preserving the two original idea chains in detail.
- [NON_CLAIMS.md](./NON_CLAIMS.md) / [NON_CLAIMS_ZH.md](./NON_CLAIMS_ZH.md): what the project does not claim, including consciousness, biological emotion, and personhood.
- [ARCHITECTURE.md](./ARCHITECTURE.md) / [ARCHITECTURE_ZH.md](./ARCHITECTURE_ZH.md): a first technical architecture for identity-first persistent agents.
- [STATE_SCHEMA.md](./STATE_SCHEMA.md) / [STATE_SCHEMA_ZH.md](./STATE_SCHEMA_ZH.md): a concrete state-transfer schema for identity, memory, tasks, affective state, conflicts, and update logs.
- [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md) / [DREAM_ENGINE_SPEC_ZH.md](./DREAM_ENGINE_SPEC_ZH.md): the proposed offline reflection and consolidation process.
- [EVALUATION.md](./EVALUATION.md) / [EVALUATION_ZH.md](./EVALUATION_ZH.md): how to test persistence, drift, memory lifecycle quality, and identity continuity.
- [LITERATURE_MAP.md](./LITERATURE_MAP.md) / [LITERATURE_MAP_ZH.md](./LITERATURE_MAP_ZH.md): related work in LLM agents, cognitive architecture, psychology, neuroscience, and continual learning.
- [THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md) / [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md): synthesis of current gaps, external theory, and the P7-P13 implementation plan.
- [PHASE_INDEX.md](./PHASE_INDEX.md) / [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md): P0-P51 foundation phase index by proposition and main line.
- [CONCEPT_MAP.md](./CONCEPT_MAP.md) / [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md): current foundation concept map and cross-layer relationships.
- [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) / [FOUNDATION_STATUS_ZH.md](./FOUNDATION_STATUS_ZH.md): what the foundation has, what is missing, and what remains exploratory or pushed back.
- [FOUNDATION_INTEGRITY_AUDIT.md](./FOUNDATION_INTEGRITY_AUDIT.md) / [FOUNDATION_INTEGRITY_AUDIT_ZH.md](./FOUNDATION_INTEGRITY_AUDIT_ZH.md): P54 integrity audit for foundation principles, boundaries, and overlap risks.
- [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md) / [CONCEPT_OVERLAP_REVIEW_ZH.md](./CONCEPT_OVERLAP_REVIEW_ZH.md): P55 concept overlap reduction for foundation ownership boundaries.
- [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) / [BOUNDARY_TEST_MATRIX_ZH.md](./BOUNDARY_TEST_MATRIX_ZH.md): P56 document-level matrix for allowed and forbidden foundation outputs.
- [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) / [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md): open foundation questions after P51.
- [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) / [OPEN_QUESTIONS_TRIAGE_ZH.md](./OPEN_QUESTIONS_TRIAGE_ZH.md): P57 triage of open questions into safe RFC order and blocked runtime work.
- [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) / [TEMPORAL_AWARENESS_RFC_ZH.md](./TEMPORAL_AWARENESS_RFC_ZH.md): P58 document-only RFC for elapsed time as future subject-state transition evidence.
- [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) / [RECALL_EVENT_WRITE_POLICY_RFC_ZH.md](./RECALL_EVENT_WRITE_POLICY_RFC_ZH.md): P59 document-only RFC for future recall event write policy boundaries.
- [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) / [STATEFUL_MEMORY_ENCODING_POLICY_ZH.md](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md): P60 policy for minimum safe encoding references before meaning-shift review.
- [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) / [GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md): P61 document-only RFC for growth candidate review-object lifecycle boundaries.
- [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) / [PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md): P62 boundary RFC for productive drift, random drift, identity-threatening drift, and collapse.
- [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) / [EXPLORATION_SERENDIPITY_RFC_ZH.md](./EXPLORATION_SERENDIPITY_RFC_ZH.md): P63 document-only RFC for exploration and serendipity signal boundaries.
- [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) / [SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md](./SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md): P64 boundary RFC for protected subject kernel and evolvable world seed.
- [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) / [RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md): P65 document-only contract RFC for future reconstruction reducers before any reducer execution.
- [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) / [PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md): P66 document-only policy RFC for target-path payload, diff, snapshot, and reference-only treatment.
- [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) / [FOUNDATION_ROADMAP_ZH.md](./FOUNDATION_ROADMAP_ZH.md): P67 synthesis roadmap for stable foundation, blocked runtime work, future contracts, and low-risk consolidation.
- [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) / [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md): architecture boundaries that prevent concept collapse and premature product expansion.
- [GLOSSARY.md](./GLOSSARY.md) / [GLOSSARY_ZH.md](./GLOSSARY_ZH.md): shared terms for growth, drift, meaning shift, governance, and temporal awareness.
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

## First Runnable Step

This repository now includes a minimal local prototype:

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

Run the local API:

```bash
python3 -m one_core.cli serve
```

Connect AstrBot:

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

Test the generic adapter protocol locally:

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
