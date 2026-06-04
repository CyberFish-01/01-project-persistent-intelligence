# CTM-Inspired Temporal Dynamics RFC / CTM 启发的时间动力学 RFC

English version: [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md)

状态：`document-only`、`RFC-only`、`non-runtime`。

P81 把 Continuous Thought Machines 启发的思想翻译进 01 Core 的 foundation
vocabulary。它不接入 CTM model，不实现 CTM runtime，不训练模型，不引入依赖，不写
temporal events，不修改 Identity Core，不写 recall events，不执行 growth lifecycle，也不添加
companion、UI、AstrBot 或 adapter behavior。

## RFC Rule / RFC 规则

```text
CTM is an inspiration source.
01 Core is not a CTM implementation.
temporal dynamics language does not approve temporal runtime.
```

## CTM Concepts Translation / CTM 概念翻译

Continuous Thought Machines research 把 time 视为 internal neural processing 的一部分，
而不只是输入顺序。CTM paper 和 project materials 描述了 neuron-level temporal
processing、作为 latent representation 的 neural synchronization、internal ticks 和 adaptive
compute。P81 只把这些想法作为 01 Core symbolic foundation layer 的概念启发。

| CTM concept | Translation for this RFC | 01 Core caution |
|---|---|---|
| temporal processing | computation 通过 internal time 展开，而不只是一次 static pass。 | 01 Core 可以研究 elapsed-state interpretation，但不实现 CTM processing。 |
| synchronization | neural activity 可以由 units 随时间如何对齐来表示。 | symbolic governance alignment 不是 neural synchronization。 |
| adaptive compute | 系统可对更难输入使用更多 internal steps，对简单输入使用更少 steps。 | review depth budgeting 是 future policy idea，不是 runtime compute control。 |
| internal dynamics | hidden state 随时间变化，本身成为 system representation 的一部分。 | 01 Core 当前记录 events 和 review state；它不暴露 neural dynamics。 |
| ticks / deliberation steps | output 前 state 演化的 internal update steps。 | 任何 `deliberation_tick` 在 storage 和 execution policy 存在前都只是 RFC vocabulary。 |
| coherence | state 具有足够 mutual consistency，可支持可信 action。 | coherence 是 review signal，不是真理、意识或 growth 的证明。 |
| latent temporal state | 携带 task-relevant information 的 evolving hidden temporal pattern。 | 01 Core 未来可定义 symbolic temporal traces，但当前没有 latent state store。 |

本 RFC 不声称 01 Core 已经具备 CTM，不声称 symbolic governance 等价于 neural
synchronization，也不声称 review objects 模拟 brain-like cognition。

## 01 Core Mapping / 01 Core 映射

| CTM-inspired idea | Existing 01 Core object | Mapping |
|---|---|---|
| event sequence vs temporal dynamics | Event Log, Replay | Event sequence 记录发生了什么；temporal dynamics 追问 events 之间和之后 state 演化如何改变 meaning。 |
| encoding_state / recall_state as temporal traces | Stateful Memory | Encoding 和 recall states 可成为 meaning 从何时、何处被解释的 symbolic traces。 |
| meaning_shift as temporal reinterpretation | Meaning Shift | memory meaning 可能因时间、冲突、冷却或新 evidence 而变化。 |
| growth_candidate_review as delayed state alignment | Growth Candidate Review | candidate 可以表达 later state 与 earlier state 的 alignment、conflict 或 reinterpretation。 |
| governance review as adaptive deliberation | Governance Surface | 高风险 candidate 可能需要更深 review；低风险 candidate 不应付出重治理成本。 |
| Temporal Awareness as subject-level time sensitivity | Temporal Awareness RFC | 只有在 contract、write policy 和 validation 存在后，time 才能进入 subject transition。 |
| Productive Drift vs Collapse as temporal coherence problem | Productive Drift vs Collapse | coherent drift 可澄清 continuity；incoherent drift 可能表示 random drift 或 collapse。 |

## Proposed CTM-Inspired Concepts / 拟议 CTM 启发概念

以下只是 RFC concepts。它们不创建 schemas、stores、events、validators 或 runtime behavior。

| Concept | Problem It Addresses | References Existing Objects | Must Not Automatically Change | Future Runtime? | Needs Evaluation? |
|---|---|---|---|---|---|
| `deliberation_tick` | 命名 conclusion 前可能存在的 internal review step。 | Governance Surface, Task Hub, risk level | identity, memory, claims, events, growth status | Yes, only after policy | Yes |
| `thought_trace` | 命名 review state 如何演化的可能记录。 | Event refs, review objects, recall state | event log, memory contents, identity | Yes, only after storage policy | Yes |
| `temporal_coherence` | review later state 是否仍能与 earlier state 和 current evidence 相容。 | Productive Drift, Claim Graph, reconstruction evidence | claim status, identity, memory salience | Maybe | Yes |
| `state_synchronization_score` | 为 memory、claim、task、identity anchors 的 alignment 提供未来 vocabulary。 | Memory Layer, Claim Graph, Task Hub, Identity Gate | any owner object or gate outcome | Maybe | Yes |
| `review_depth_budget` | 防止低风险项 over-review、高风险项 under-review。 | Governance Surface, risk register, review checklist | policy execution or automatic approval | Maybe | Yes |
| `unresolved_tension` | 跟踪尚未成为 candidate 或 decision 的 persistent conflict。 | Claim conflicts, task blockers, memory conflicts | growth candidate, claim revision, identity update | Maybe | Yes |
| `delayed_alignment` | 命名后来发现旧 evidence 符合稳定 pattern 的 realization。 | Meaning Shift, Growth Candidate Review, Temporal Awareness | semantic promotion or identity update | Maybe | Yes |
| `temporal_pressure` | 命名 stale tasks、old claims 或 repeated unresolved conflict 累积出的 urgency。 | Task Hub, Claim Graph, Temporal Awareness | task mutation, claim mutation, memory decay | Maybe | Yes |
| `coherence_break` | 标记 current state 已不能安全地从 prior state 推导。 | Productive Drift vs Collapse, boundary matrix | collapse classification or memory rewrite | Maybe | Yes |
| `re-synchronization_candidate` | 命名在不改写历史的情况下恢复 context alignment 的 review object。 | Context Builder, Event Log, State Transfer package | memory rewrite, identity mutation, recall write | Maybe | Yes |

## Boundaries / 边界

P81 明确禁止：

- CTM neural implementation；
- model training；
- local model requirement；
- Temporal Awareness runtime；
- temporal event write；
- automatic recall event write；
- identity mutation；
- memory rewrite；
- growth execution；
- companion、UI、AstrBot 或 adapter work；
- claim auto-revision；
- policy executor；
- reconstruction reducer execution。

## Evaluation Ideas / Evaluation 设想

以下只是 evaluation ideas。P81 不实现它们。

| Scenario | Expected Review Outcome |
|---|---|
| Same event plus different elapsed time | 生成不同 meaning-shift candidate，不自动 memory mutation。 |
| Unresolved conflict accumulates temporal tension | 记录可能的 `unresolved_tension`，不自动 claim revision。 |
| Low-risk candidate | 只需要 shallow review depth，不走重治理路径。 |
| Identity-threatening candidate | 需要 deeper deliberation 和 Identity Gate escalation。 |
| Temporal coherence separates growth from random drift | coherent evidence 可以支持 review；incoherent change 不是 growth。 |
| Prompt contamination | 产生 `coherence_break`，不是 growth 或 identity update。 |
| Delayed realization | 产生 review candidate，不是 identity update。 |
| Re-synchronization | 不 rewrite memory，只恢复 context alignment。 |

## Relationship To Existing Open Questions / 与现有开放问题的关系

| Open Question | P81 Impact |
|---|---|
| Temporal Awareness | 增加 elapsed state dynamics 的 CTM-inspired vocabulary，但继续 blocked runtime。 |
| Recall Event Write Policy | 强化一个问题：ticks/traces 是 events、traces，还是 ephemeral review steps？ |
| Growth Candidate Lifecycle | 提示 delayed alignment 和 unresolved tension 可作为 review-object inputs，而不是 lifecycle execution。 |
| Productive Drift vs Collapse | 把 drift 重新表述为 evidence 下的 temporal coherence，而不是 automatic growth classification。 |
| Exploration / Serendipity Engine | 提醒 adaptive deliberation 不能变成 productized exploration 或 companion behavior。 |
| Subject Kernel / World Seed | 提出 temporal coherence 是否应分别比较 protected subject anchors 与 evolvable world orientation。 |
| Reconstruction Reducer Contract | 增加 future question：thought traces 是 reconstructable evidence，还是应保持 ephemeral。 |

## Risks / 风险

- 过度抽象 CTM，把所有 time-related concern 都叫 dynamics。
- 混淆 neural synchronization 与 symbolic governance。
- 创造没有 tests 的 fake cognition vocabulary。
- 把 report layers 变成 pseudo-consciousness claims。
- 让 Temporal Awareness 过宽。
- 在没有 storage policy 的情况下发明 `thought_trace`。
- review layer 变得过重。
- 用 CTM language 为 automatic growth 找理由。

## Open Questions / 开放问题

- Should deliberation ticks be persisted?
- Are ticks events, traces, or ephemeral internal steps?
- What is the minimal useful temporal state?
- How can the project avoid `thought_trace` explosion?
- How can temporal coherence be tested without pretending consciousness?
- Should `review_depth_budget` be tied to `risk_level`?
- Can `unresolved_tension` become a growth candidate?
- When does `delayed_alignment` become evidence?
- How does CTM-inspired dynamics relate to reconstruction?
- What must remain purely RFC until runtime foundation is ready?

## P82 Candidate Directions / P82 候选方向

P81 不执行这些方向：

- Temporal Coherence Evaluation Plan；
- Deliberation Tick RFC；
- Thought Trace Storage Policy RFC；
- Review Depth Budget RFC；
- Unresolved Tension / Delayed Alignment RFC；
- CTM-inspired Concepts Glossary；
- Foundation Risk Review after CTM mapping。

## References / 参考

- Sakana AI, [Introducing Continuous Thought Machines](https://sakana.ai/ctm/)。
- Darlow et al., [Continuous Thought Machines](https://arxiv.org/abs/2505.05522)。

## P81 Non-Execution Statement / P81 非执行声明

P81 不实现：

- CTM runtime；
- model training；
- new dependencies；
- temporal runtime；
- temporal event writes；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- claim auto-revision；
- policy execution；
- reconstruction reducer execution；
- companion、UI、AstrBot、adapter、cloud rollout 或 product layer。
