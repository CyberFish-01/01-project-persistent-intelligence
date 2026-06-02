# 01 Project

**How Can Intelligence Persist Through Time?**

[中文 README](./README_ZH.md)

01 Project is a research program about persistent intelligence: how an AI system can remain continuous across conversations, tasks, memories, dreams, conflicts, and social interactions.

The project begins from a simple problem:

> Existing AI systems restart too easily.

Even when a model is powerful, its context is long, and its agent loop is complex, it can still lose state, drift in identity, forget long-term intent, or become a different behavioral subject across time.

This repository records the foundational documents and the first engineering frame:

- [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md): the full research vision for Persistent Intelligence, State Transfer, Dream Engine, Memory Lifecycle, Identity Growth, and Cognitive Ecology.
- [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md): the theory of artificial life history, including false assigned history, generated history, and identity seed.
- [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md): Chinese research notes preserving the two original idea chains in detail.
- [NON_CLAIMS.md](./NON_CLAIMS.md) / [NON_CLAIMS_ZH.md](./NON_CLAIMS_ZH.md): what the project does not claim, including consciousness, biological emotion, and personhood.
- [ARCHITECTURE.md](./ARCHITECTURE.md) / [ARCHITECTURE_ZH.md](./ARCHITECTURE_ZH.md): a first technical architecture for identity-first persistent agents.
- [STATE_SCHEMA.md](./STATE_SCHEMA.md) / [STATE_SCHEMA_ZH.md](./STATE_SCHEMA_ZH.md): a concrete state-transfer schema for identity, memory, tasks, affective state, conflicts, and update logs.
- [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md) / [DREAM_ENGINE_SPEC_ZH.md](./DREAM_ENGINE_SPEC_ZH.md): the proposed offline reflection and consolidation process.
- [EVALUATION.md](./EVALUATION.md) / [EVALUATION_ZH.md](./EVALUATION_ZH.md): how to test persistence, drift, memory lifecycle quality, and identity continuity.
- [LITERATURE_MAP.md](./LITERATURE_MAP.md) / [LITERATURE_MAP_ZH.md](./LITERATURE_MAP_ZH.md): related work in LLM agents, cognitive architecture, psychology, neuroscience, and continual learning.
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
