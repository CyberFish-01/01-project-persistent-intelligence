# 01 Project

**How Can Intelligence Persist Through Time?**

[English README](./README.md)

01 Project 是一个关于 **Persistent Intelligence（连续存在智能）** 的研究纲领：研究一个 AI 系统如何在多次对话、多项任务、记忆、梦境整理、冲突和社会互动之间保持连续状态。

项目从一个简单问题开始：

> 现有 AI 系统太容易重新开始。

即使模型很强、上下文很长、Agent 框架很复杂，它仍然可能丢失状态、发生身份漂移、忘记长期意图，或者在时间中变成另一个行为主体。

## 文档入口

本仓库保留英文原文，并补充中文并行版本。以后默认 **中文优先起草，英文并行保留**。

- [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md)：Persistent Intelligence、State Transfer、Dream Engine、Memory Lifecycle、Identity Growth、Cognitive Ecology 的完整研究愿景。
- [FOUNDATION.md](./FOUNDATION.md) / [FOUNDATION_ZH.md](./FOUNDATION_ZH.md)：项目级工程地基，定义后续实现必须服从的边界、不变量和阶段顺序。
- [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md)：人工生命史、虚假历史、生成历史、Identity Seed。
- [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md)：中文原始研究记录，保留两条思想链的完整展开。
- [NON_CLAIMS.md](./NON_CLAIMS.md) / [NON_CLAIMS_ZH.md](./NON_CLAIMS_ZH.md)：项目不主张什么，包括意识、生物情绪、人格权等边界。
- [ARCHITECTURE.md](./ARCHITECTURE.md) / [ARCHITECTURE_ZH.md](./ARCHITECTURE_ZH.md)：Identity-first persistent agent 的第一版技术架构。
- [STATE_SCHEMA.md](./STATE_SCHEMA.md) / [STATE_SCHEMA_ZH.md](./STATE_SCHEMA_ZH.md)：State Transfer 的状态 schema。
- [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md) / [DREAM_ENGINE_SPEC_ZH.md](./DREAM_ENGINE_SPEC_ZH.md)：Dream Engine 的离线反思、巩固、冲突检测和遗忘机制。
- [EVALUATION.md](./EVALUATION.md) / [EVALUATION_ZH.md](./EVALUATION_ZH.md)：如何评估连续性、认知漂移、记忆生命周期和身份稳定性。
- [LITERATURE_MAP.md](./LITERATURE_MAP.md) / [LITERATURE_MAP_ZH.md](./LITERATURE_MAP_ZH.md)：与 LLM Agent、认知架构、心理学、神经科学、持续学习相关的文献地图。
- [THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md) / [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md)：当前缺口、外部理论和 P7-P13 工程计划的综合。
- [PHASE_INDEX.md](./PHASE_INDEX.md) / [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md)：P0-P51 foundation phase index，按核心命题和所属主线整理。
- [CONCEPT_MAP.md](./CONCEPT_MAP.md) / [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md)：当前 foundation concept map 和跨层关系。
- [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) / [FOUNDATION_STATUS_ZH.md](./FOUNDATION_STATUS_ZH.md)：基础层已具备什么、缺什么、哪些仍在探索或需要后推。
- [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) / [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md)：P51 之后仍未关闭的基础层问题。
- [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) / [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md)：防止概念互相吞并和过早产品化的架构边界。
- [GLOSSARY.md](./GLOSSARY.md) / [GLOSSARY_ZH.md](./GLOSSARY_ZH.md)：growth、drift、meaning shift、governance 和 temporal awareness 等共享术语。
- [IMPLEMENTATION_START.md](./IMPLEMENTATION_START.md) / [IMPLEMENTATION_START_ZH.md](./IMPLEMENTATION_START_ZH.md)：第一版可运行本地 01 Core 原型。
- [MEMORY_IMPORT.md](./MEMORY_IMPORT.md) / [MEMORY_IMPORT_ZH.md](./MEMORY_IMPORT_ZH.md)：如何把 AstrBot、Angel Memory 或其他系统的记忆以通用文本形式导入。
- [API.md](./API.md) / [API_ZH.md](./API_ZH.md)：给 AstrBot 等 adapter 使用的本地 HTTP API。
- [ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) / [ADAPTER_PROTOCOL_ZH.md](./ADAPTER_PROTOCOL_ZH.md)：通用 adapter 协议。本地通用版先稳定，再做 AstrBot 特化。
- [adapters/astrbot/astrbot_plugin_01_core](./adapters/astrbot/astrbot_plugin_01_core)：第一版 AstrBot adapter。AstrBot 作为入口，01 Core 保存连续性状态。
- [CLOUD_DEPLOYMENT.md](./CLOUD_DEPLOYMENT.md) / [CLOUD_DEPLOYMENT_ZH.md](./CLOUD_DEPLOYMENT_ZH.md)：把 01 Core 部署为云服务器常驻服务。

## 核心命题

```text
Continuity != Memory Retrieval
Continuity = State Transfer
```

连续性不是把旧记忆检索回来。

连续性是把一个智能体的状态穿过时间迁移下去。

01 不是最强模型、超级 Agent、数字女友，或者一个带完整虚构传记的角色。

01 是一个 **Identity Seed（身份种子）**：第一次尝试给智能一个起点、一个方向、一个世界，以及足够的连续性，让它自己长出生命史。

## 第一版可运行原型

本仓库现在包含一个最小本地 01 Core：

```bash
python3 -m one_core.cli init
python3 -m one_core.cli interact "我们开始实现 01 Core。"
python3 -m one_core.cli dream
python3 -m one_core.cli status
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
```

默认状态目录是 `work/01_state`。

启动本地 API：

```bash
python3 -m one_core.cli serve
```

接入 AstrBot：

```bash
cp -R adapters/astrbot/astrbot_plugin_01_core /root/data/plugins/
```

然后在 AstrBot 中使用：

```text
/01 ping
/01 status
/01 chat <内容>
/01 dream
```

通用 adapter 协议本地测试：

```bash
python3 -m one_core.cli remote health
python3 -m one_core.cli remote adapters
python3 -m one_core.cli remote interact "继续推进 01 Core。"
python3 -m one_core.cli remote status
```

```text
01 Project

We are not trying to build a smarter model.
We are trying to build an intelligence that can pass through time,
carry a life history,
and remain recognizably itself.
```
