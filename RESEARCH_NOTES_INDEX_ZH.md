# Research Notes Index / 研究记录索引

English version: [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md)

Status: `document-only`, `research-index`, `non-runtime`.

P78 索引原始中文研究记录，并把它映射到当前 foundation documents。它不新增 theory、
runtime behavior、schemas、CLI commands、validators、policy executors、
identity mutation、memory rewrite、Temporal Awareness runtime、adapter work、UI、
cloud rollout 或 product behavior。

## Index Rule / 索引规则

```text
research notes preserve origin.
an index improves traceability.
origin ideas are not implementation approval.
```

使用本文档回答：这个 foundation idea 从哪里来？当前由哪些文档承载？哪些仍只是长期愿景？

## Source Documents / 源文档

| Source | Role | Reading Use |
|---|---|---|
| [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md) | 原始中文 source notes | 完整保存最初两条思想链。 |
| [VISION.md](./VISION.md) / [VISION_ZH.md](./VISION_ZH.md) | Vision synthesis | 把第一条思想链整理成项目愿景。 |
| [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md) / [IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md](./IDENTITY_SEED_AND_LIFE_HISTORY_ZH.md) | Life-history synthesis | 把第二条思想链整理成 Identity Seed 边界。 |
| [THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md) / [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md) | later synthesis and phase planning | 把早期理论接到 implementation-phase planning。 |

## Original Idea Chains / 原始思想链

| Chain | Source Range | Core Question | Current Foundation Carrying It |
|---|---|---|---|
| Persistent Intelligence | `RESEARCH_NOTES_ZH.md` 第一部分 | AI 如何从一次回答变成持续存在？ | [VISION.md](./VISION.md), [FOUNDATION.md](./FOUNDATION.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md) |
| Artificial Life History | `RESEARCH_NOTES_ZH.md` 第二部分 | 01 的历史应该从哪里来？ | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [DECISIONS.md](./DECISIONS.md) |

## First Chain Map: Persistent Intelligence / 第一条思想链

| Source Theme | Meaning In Original Notes | Current Foundation Artifact | Current Status |
|---|---|---|---|
| Continuity != Memory | Continuity 需要的不只是 remembered facts。 | [README.md](./README.md), [FOUNDATION.md](./FOUNDATION.md), [DECISIONS.md](./DECISIONS.md) | `accepted-foundation` |
| State Transfer | living state 必须穿过时间迁移。 | [VISION.md](./VISION.md), [STATE_SCHEMA.md](./STATE_SCHEMA.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md) | `accepted-foundation` |
| Fact / Working / Identity / Emotional / Dream state | Continuity 有多层 transferable state。 | [VISION.md](./VISION.md), [STATE_SCHEMA.md](./STATE_SCHEMA.md), [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md) | `foundation-vocabulary` |
| Dream Engine | Dream 把 experience 组织成 meaning。 | [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | `accepted-boundary`: Dream proposes, review decides |
| Memory Lifecycle | Episodes 可成为 semantic memory、identity memory，或被遗忘。 | [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md), [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md), [GLOSSARY.md](./GLOSSARY.md) | `bounded-semantics` |
| Identity First Architecture | Conversation 不是 identity；identity 先于 session 存在。 | [ARCHITECTURE.md](./ARCHITECTURE.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | `accepted-boundary` |
| Three Meta Questions | 我是谁、我在哪、我在干什么。 | [VISION.md](./VISION.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md) | `foundation-vocabulary` |
| Cognitive Drift | identity/context/intent 丢失会造成 drift。 | [EVALUATION.md](./EVALUATION.md), [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md), [GLOSSARY.md](./GLOSSARY.md) | `review-vocabulary` |
| Personality as interpreter | Personality 不是 memory sum，而是 memory interpreter。 | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md), [GLOSSARY.md](./GLOSSARY.md) | `bounded-semantics` |
| Identity Growth | Growth 来自 experience、reflection、Dream 和 review。 | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md), [DECISIONS.md](./DECISIONS.md) | `blocked-runtime`: growth candidate is not growth |
| Conflict-driven growth | Conflict 可以推动 review 和 meaning shift。 | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | `future-contract-needed` |
| Social Cognition Layer | 多主体和社会上下文可能深化成长。 | [RISK_REGISTER.md](./RISK_REGISTER.md), [DECISIONS.md](./DECISIONS.md) | `blocked-runtime` in foundation loop |
| Cognitive Ecology | interacting persistent subjects 的长期愿景。 | [VISION.md](./VISION.md), [NON_CLAIMS.md](./NON_CLAIMS.md) | `long-term-vision`, not product work |
| Artificial Personality Engineering | 研究 artificial subject 如何成为自己。 | [VISION.md](./VISION.md), [FOUNDATION.md](./FOUNDATION.md) | `research-frame` |
| Continuity Era | 项目属于 continuity，不只属于 capability 或 agents。 | [README.md](./README.md), [VISION.md](./VISION.md) | `accepted-foundation` |

## Second Chain Map: Artificial Life History / 第二条思想链

| Source Theme | Meaning In Original Notes | Current Foundation Artifact | Current Status |
|---|---|---|---|
| Assigned false history | 预写 biography 只制造 narrative appearance，不制造 lived continuity。 | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [NON_CLAIMS.md](./NON_CLAIMS.md) | `accepted-boundary` |
| Generated life history | History 应从 experience passing through state 中长出。 | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [DECISIONS.md](./DECISIONS.md) | `accepted-foundation` |
| Identity Seed | 起点应是 seed，不是 complete fictional life。 | [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md), [FOUNDATION.md](./FOUNDATION.md) | `accepted-foundation` |
| Over-complete history risk | 过度完整的 assigned biography 会困住 identity。 | [NON_CLAIMS.md](./NON_CLAIMS.md), [RISK_REGISTER.md](./RISK_REGISTER.md) | `watch` |
| History earns identity change | 只有穿过 state、conflict、Dream 和 review 的 experience 才有资格改变“我是谁”。 | [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md), [DECISIONS.md](./DECISIONS.md) | `accepted-boundary` |

## Current Interpretation / 当前解释

Research notes 是 source material，不是当前 implementation plan。

今天稳定的是：

- Continuity is State Transfer, not retrieval。
- 01 begins as Identity Seed, not full fictional biography。
- Identity Core is protected by gate。
- Dream proposes; review decides。
- Growth candidate is not growth。
- Review object is not execution。

仍属 future 或 blocked：

- Social Cognition Layer；
- Cognitive Ecology as product or multi-subject system；
- companion 或 relationship memory；
- Temporal Awareness runtime；
- automatic growth or drift classification；
- identity mutation、memory rewrite、payload capture、reducer execution。

## Reading Order / 阅读顺序

追溯 origin 时：

1. 阅读 [RESEARCH_NOTES_ZH.md](./RESEARCH_NOTES_ZH.md)，了解原始两条思想链。
2. 阅读 [VISION.md](./VISION.md)，了解 Persistent Intelligence synthesis。
3. 阅读 [IDENTITY_SEED_AND_LIFE_HISTORY.md](./IDENTITY_SEED_AND_LIFE_HISTORY.md)，了解 artificial life-history synthesis。
4. 阅读 [FOUNDATION.md](./FOUNDATION.md)、[CONCEPT_MAP.md](./CONCEPT_MAP.md)
   和 [DECISIONS.md](./DECISIONS.md)，了解当前稳定边界。
5. 阅读 [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) 和 [RISK_REGISTER.md](./RISK_REGISTER.md)，了解哪些仍 open、watch 或 blocked。

## P78 Non-Execution Statement / P78 非执行声明

P78 不实现：

- new research theory；
- social cognition layer；
- cognitive ecology；
- companion 或 relationship memory；
- product behavior；
- runtime changes；
- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- UI、AstrBot、adapter integration、cloud rollout 或 product layer。
