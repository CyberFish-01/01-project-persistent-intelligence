# 01 Project

**How Can Intelligence Persist Through Time?**

[English README](./README.md)

01 Project 是一个关于 **Persistent Intelligence（连续存在智能）** 的研究纲领：研究一个 AI 系统如何在多次对话、多项任务、记忆、梦境整理、冲突和社会互动之间保持连续状态。

项目从一个简单问题开始：

> 现有 AI 系统太容易重新开始。

即使模型很强、上下文很长、Agent 框架很复杂，它仍然可能丢失状态、发生身份漂移、忘记长期意图，或者在时间中变成另一个行为主体。

本仓库现在有两层：

- foundation documents：定义 continuity、identity、event sourcing、review、reconstruction readiness 和 blocked future work；
- earlier prototype references：记录本地 01 Core runtime 和 adapter surfaces 的早期工程参考。

当前工作状态：P68-P80 是低风险 foundation consolidation。下面的 runtime 和 adapter references 是历史/工程参考；它们不是扩展 UI、AstrBot、product、Temporal Awareness runtime、growth execution、memory rewrite 或 reconstruction reducers 的授权。

## 文档入口

新加入项目、交接给另一个 agent，或者回看当前地基时，先读这些：

- [FOUNDATION.md](./FOUNDATION.md) / [FOUNDATION_ZH.md](./FOUNDATION_ZH.md)：项目级边界、不变量和阶段顺序。
- [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) / [FOUNDATION_STATUS_ZH.md](./FOUNDATION_STATUS_ZH.md)：基础层已具备什么、缺什么、哪些仍在探索或需要后推。
- [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md) / [FOUNDATION_ROADMAP_ZH.md](./FOUNDATION_ROADMAP_ZH.md)：稳定地基、blocked runtime work、future contracts 和低风险 consolidation。
- [PHASE_INDEX.md](./PHASE_INDEX.md) / [PHASE_INDEX_ZH.md](./PHASE_INDEX_ZH.md)：P0-P68 foundation phase index，按核心命题和所属主线整理。
- [CONCEPT_MAP.md](./CONCEPT_MAP.md) / [CONCEPT_MAP_ZH.md](./CONCEPT_MAP_ZH.md)：当前 foundation concept map 和跨层关系。
- [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) / [ARCHITECTURE_BOUNDARIES_ZH.md](./ARCHITECTURE_BOUNDARIES_ZH.md)：P73 architecture boundary refresh，覆盖 identity、memory、growth、temporal、reconstruction、governance 和 product layers。
- [GLOSSARY.md](./GLOSSARY.md) / [GLOSSARY_ZH.md](./GLOSSARY_ZH.md)：P74 去重后的共享术语和边界，覆盖 growth、drift、stateful memory、governance、reconstruction 和 temporal awareness。
- [RISK_REGISTER.md](./RISK_REGISTER.md) / [RISK_REGISTER_ZH.md](./RISK_REGISTER_ZH.md)：P72 foundation risk register，记录 concept inflation、过早 runtime pressure 和 boundary drift。
- [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) / [FOUNDATION_REVIEW_CHECKLIST_ZH.md](./FOUNDATION_REVIEW_CHECKLIST_ZH.md)：P76 manual review checklist，用于后续 document-only foundation phases。
- [DECISIONS.md](./DECISIONS.md) / [DECISIONS_ZH.md](./DECISIONS_ZH.md)：P77 document-only log，记录 accepted、deferred、blocked 和 watch foundation decisions。
- [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) / [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md)：当前 open foundation questions 和状态。
- [RFC_INDEX.md](./RFC_INDEX.md) / [RFC_INDEX_ZH.md](./RFC_INDEX_ZH.md)：foundation RFC、policy、review、audit 和 matrix artifacts 索引。
- [AUTONOMOUS_WORK_SUMMARY.md](./AUTONOMOUS_WORK_SUMMARY.md) / [AUTONOMOUS_WORK_SUMMARY_ZH.md](./AUTONOMOUS_WORK_SUMMARY_ZH.md)：最新 autonomous foundation work summary 和下一步安全方向。

## Foundation Review Artifacts / 地基审查文档

检查新的 foundation work 是否仍在 guardrails 内时，使用这些：

- [FOUNDATION_INTEGRITY_AUDIT.md](./FOUNDATION_INTEGRITY_AUDIT.md) / [FOUNDATION_INTEGRITY_AUDIT_ZH.md](./FOUNDATION_INTEGRITY_AUDIT_ZH.md)：P54 foundation principles、边界和重叠风险完整性审计。
- [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md) / [CONCEPT_OVERLAP_REVIEW_ZH.md](./CONCEPT_OVERLAP_REVIEW_ZH.md)：P55 foundation ownership boundaries 概念重叠收敛。
- [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) / [BOUNDARY_TEST_MATRIX_ZH.md](./BOUNDARY_TEST_MATRIX_ZH.md)：P56 allowed / forbidden foundation outputs 文档级边界测试矩阵。
- [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md) / [OPEN_QUESTIONS_TRIAGE_ZH.md](./OPEN_QUESTIONS_TRIAGE_ZH.md)：P57 open questions 分诊，排序 safe RFC 和 blocked runtime work。
- [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) / [FOUNDATION_REVIEW_CHECKLIST_ZH.md](./FOUNDATION_REVIEW_CHECKLIST_ZH.md)：P76 human review gate，覆盖 phase scope、invariants、risks、bilingual consistency、verification 和 commit review。

## Future RFC And Policy Artifacts / 未来 RFC 与策略文档

这些文档定义 review surfaces 和 future contracts。它们不授权执行：

- [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) / [TEMPORAL_AWARENESS_RFC_ZH.md](./TEMPORAL_AWARENESS_RFC_ZH.md)：P58 document-only RFC，把 elapsed time 作为未来 subject-state transition evidence 研究。
- [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) / [RECALL_EVENT_WRITE_POLICY_RFC_ZH.md](./RECALL_EVENT_WRITE_POLICY_RFC_ZH.md)：P59 document-only RFC，定义未来 recall event write policy 边界。
- [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) / [STATEFUL_MEMORY_ENCODING_POLICY_ZH.md](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md)：P60 policy，定义 meaning-shift review 前所需的最小安全 encoding references。
- [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) / [GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md)：P61 document-only RFC，定义 growth candidate review-object lifecycle 边界。
- [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) / [PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md)：P62 boundary RFC，区分 productive drift、random drift、identity-threatening drift 和 collapse。
- [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) / [EXPLORATION_SERENDIPITY_RFC_ZH.md](./EXPLORATION_SERENDIPITY_RFC_ZH.md)：P63 document-only RFC，定义 exploration 和 serendipity signal 边界。
- [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) / [SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md](./SUBJECT_KERNEL_WORLD_SEED_RFC_ZH.md)：P64 boundary RFC，区分受保护的 subject kernel 和可演化的 world seed。
- [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) / [RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md)：P65 document-only contract RFC，在任何 reducer execution 前定义未来 reconstruction reducer contract。
- [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) / [PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md)：P66 document-only policy RFC，定义 target-path payload、diff、snapshot 和 reference-only treatment。

## Original Research Base / 原始研究基础

阅读项目愿景、理论和早期架构时，使用这些：

- [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md)：Persistent Intelligence、State Transfer、Dream Engine、Memory Lifecycle、Identity Growth、Cognitive Ecology 的完整研究愿景。
- [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) / [RESEARCH_NOTES_INDEX_ZH.md](./RESEARCH_NOTES_INDEX_ZH.md)：P78 source-note index，把原始思想链映射到当前 foundation documents。
- [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md)：人工生命史、虚假历史、生成历史、Identity Seed。
- [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md)：中文原始研究记录，保留两条思想链的完整展开。
- [NON_CLAIMS.md](./NON_CLAIMS.md) / [NON_CLAIMS_ZH.md](./NON_CLAIMS_ZH.md)：项目不主张什么，包括意识、生物情绪、人格权等边界。
- [ARCHITECTURE.md](./ARCHITECTURE.md) / [ARCHITECTURE_ZH.md](./ARCHITECTURE_ZH.md)：Identity-first persistent agent 的第一版技术架构。
- [STATE_SCHEMA.md](./STATE_SCHEMA.md) / [STATE_SCHEMA_ZH.md](./STATE_SCHEMA_ZH.md)：State Transfer 的状态 schema。
- [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md) / [DREAM_ENGINE_SPEC_ZH.md](./DREAM_ENGINE_SPEC_ZH.md)：Dream Engine 的离线反思、巩固、冲突检测和遗忘机制。
- [EVALUATION.md](./EVALUATION.md) / [EVALUATION_ZH.md](./EVALUATION_ZH.md)：如何评估连续性、认知漂移、记忆生命周期和身份稳定性。
- [LITERATURE_MAP.md](./LITERATURE_MAP.md) / [LITERATURE_MAP_ZH.md](./LITERATURE_MAP_ZH.md)：与 LLM Agent、认知架构、心理学、神经科学、持续学习相关的文献地图。
- [THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md) / [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md)：当前缺口、外部理论和 P7-P13 工程计划的综合。

## Runtime And Adapter References / Runtime 与 Adapter 参考

这些文档描述已有 prototype surfaces。它们不是当前 foundation work：

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

## Prototype Reference / 原型参考

本仓库包含一个最小本地 01 Core。P68-P80 foundation consolidation 期间，
这些命令只作为验证和理解方向的参考：

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

本地 API 参考：

```bash
python3 -m one_core.cli serve
```

AstrBot adapter 参考：

```bash
cp -R adapters/astrbot/astrbot_plugin_01_core /root/data/plugins/
```

AstrBot 使用参考：

```text
/01 ping
/01 status
/01 chat <内容>
/01 dream
```

通用 adapter 协议参考：

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
