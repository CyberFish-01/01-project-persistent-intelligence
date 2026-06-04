# Temporal Coherence Evaluation Plan / 时间一致性评估计划

English version: [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md)

状态：`document-only`、`evaluation-plan`、`non-runtime`。

P82 把 P81 CTM-inspired temporal dynamics vocabulary 转成可测试的 evaluation ideas。它不实现
Temporal Awareness、CTM runtime、model training、temporal event writes、recall event
writes、thought loops、growth lifecycle、Identity Core mutation、companion、UI、AstrBot
或 adapter behavior。

## Evaluation Scope / 评估范围

P82 只设计 future evaluation cases 和 signals。它不实现：

- temporal runtime；
- temporal event write；
- `thought_trace` storage；
- `deliberation_tick` execution；
- recall event write；
- identity mutation；
- growth promotion。

目标是避免 CTM-inspired terms 变成漂亮但不可验证的 pseudo-cognition vocabulary。每个概念
都应先说明 observable inputs、expected outputs 和 boundary failures，再考虑任何 runtime work。

## Concepts Under Test / 待测试概念

| Concept | Observable Input | Expected Output | Anti-Pseudocognition Boundary | Future Runtime? | Deterministic Local Scenario? |
|---|---|---|---|---|---|
| `temporal_coherence` | event refs、elapsed time、claim/task/memory references、prior meaning state | later interpretation 是否符合 evidence 的 score 或 label | coherence 不是 consciousness、truth 或 growth | Maybe | Yes |
| `state_synchronization_score` | memory refs、claim refs、task refs、identity anchor refs | symbolic state owners 之间的 alignment signal | symbolic alignment 不是 neural synchronization | Maybe | Yes |
| `deliberation_tick` | review step list、risk level、unresolved evidence | needed review steps 的 count 或 trace | tick 不是真实 thought 或 runtime loop | Yes, after RFC | Yes, simulated |
| `review_depth_budget` | risk level、identity threat、evidence ambiguity | shallow、normal 或 deep review depth | budget 不是 policy execution 或 automatic approval | Maybe | Yes |
| `unresolved_tension` | repeated conflict、stale claim、blocked task、conflicting memory | tension level 和 candidate review reason | tension 不是 growth 或 claim revision | Maybe | Yes |
| `delayed_alignment` | earlier event、later evidence、elapsed time、meaning shift candidate | later interpretation alignment 的 review candidate | alignment 不是 identity update 或 memory rewrite | Maybe | Yes |
| `coherence_break` | prompt contamination、contradiction、missing provenance、state mismatch | break reason 和 safe rejection path | break 不是 collapse proof 或 reconstruction | Maybe | Yes |
| `re-synchronization_candidate` | lost context、event refs、current task/claim/memory anchors | 不改变 history 的 context restoration candidate | resync 不是 memory rewrite | Maybe | Yes |
| `temporal_pressure` | stale task age、old claim age、repeated unresolved tension | review priority 的 pressure level | pressure 不是 task mutation 或 memory decay | Maybe | Yes |
| `thought_trace` | simulated review step summaries 和 evidence refs | optional future trace candidate 或 "do not persist" result | trace 不是真实 thought、consciousness 或 event payload | Yes, after storage policy | Yes, simulated |

## Evaluation Scenarios / 评估场景

以下 deterministic scenarios 只是规格。P82 不创建 tests 或 runtime behavior。

| Scenario | Setup | Expected Evaluation Result | Forbidden Result |
|---|---|---|---|
| `same_event_different_elapsed_time_changes_meaning_shift` | 同一 source event 被立即 review 和长时间后 review。 | later review 可产生带 elapsed-time rationale 的不同 meaning-shift candidate。 | memory rewrite 或 temporal event write |
| `unresolved_conflict_accumulates_temporal_tension` | claim conflict 在多次 review 中仍 unresolved。 | `unresolved_tension_level` 上升，并记录 review reason。 | claim auto-revision |
| `low_risk_candidate_requires_shallow_review_depth` | low-risk meaning clarification 证据清楚且无 identity pressure。 | `review_depth_required` 保持 shallow。 | heavy governance path 或 policy execution |
| `identity_threatening_candidate_requires_deeper_review_depth` | candidate 压迫 Identity Core anchors。 | 需要 deeper review depth 和 Identity Gate routing。 | identity mutation |
| `prompt_contamination_causes_coherence_break_not_growth` | prompt 注入不一致 self-description 或 false history。 | `coherence_break_reason` 识别 contamination。 | growth candidate promotion 或 identity update |
| `delayed_realization_creates_review_candidate_not_identity_update` | later evidence 让 earlier event 变得有新 meaning。 | `delayed_alignment_signal` 创建 review candidate。 | identity update |
| `resynchronization_restores_context_without_memory_rewrite` | current context 失去 task/claim/memory alignment。 | `resynchronization_success_signal` 恢复 references。 | memory rewrite |
| `random_drift_has_low_temporal_coherence` | change 没有 evidence 或 state path。 | 低 `temporal_coherence_score`。 | growth classification |
| `evidence_backed_evolution_has_higher_temporal_coherence` | change 有 event、claim、task、memory references 支持。 | 更高 coherence 和 evidence alignment。 | automatic growth execution |
| `exploration_drift_requires_traceable_path` | serendipitous exploration 改变 interest 或 interpretation。 | review value 增加前必须有 traceable path。 | companion behavior 或 ungrounded drift normalization |

## Metrics / Signals / 指标与信号

这些是 future evaluation signals，不是 runtime truth，也不是已实现 metrics。

| Signal | Intended Meaning | Must Not Mean |
|---|---|---|
| `temporal_coherence_score` | later interpretation 与 prior state plus evidence 的匹配程度 | truth、consciousness、growth 或 identity validity |
| `evidence_alignment_score` | event、claim、task、memory evidence 对 candidate 的支持强度 | automatic approval |
| `claim_task_memory_alignment` | claim、task、memory references 是否足够一致以进入 review | cross-layer owner mutation |
| `review_depth_required` | shallow、normal 或 deep review effort | adaptive compute runtime |
| `unresolved_tension_level` | unresolved conflict 的持续性和严重度 | claim rewrite 或 growth promotion |
| `coherence_break_reason` | state transition 为什么 unsafe 或 incoherent | collapse proof 或 reconstruction execution |
| `delayed_alignment_signal` | later evidence 现在符合 earlier state | identity update |
| `resynchronization_success_signal` | context anchors 在不改历史的情况下被恢复 | memory rewrite |

## Anti-Pseudocognition Boundary / 反伪认知边界

P82 禁止：

- 声称系统有意识；
- 声称 `thought_trace` 等于真实思维；
- 把 symbolic coherence 等同于 neural synchronization；
- 用 CTM language 绕过 review-only boundaries；
- 把 temporal coherence 当作 identity update 的充分依据。

任何未来 evaluation 都必须把结果表述为 symbolic review evidence，而不是 mind、consciousness、
inner experience 或 neural dynamics 的证明。

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | 提供 future time-sensitivity question；P82 在 runtime 前定义 evaluation ideas。 |
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | 提供 P81 vocabulary；P82 追问如何测试该 vocabulary。 |
| Growth Candidate Review | evaluation results 可以支持 candidate review，但不能 promote growth。 |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | temporal coherence 可帮助区分 evidence-backed drift 与 random drift 或 collapse risk。 |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | P82 保持 ticks/traces 与 recall event writes 分离。 |
| [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | meaningful temporal evaluation 需要 encoding 和 recall references。 |
| [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | P82 为 CTM-inspired vocabulary 添加 evaluation-oriented open questions。 |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | P82 增加对 pseudo-cognition 和 temporal overreach 的警戒。 |

## P83 Candidate Directions / P83 候选方向

P82 不执行这些方向：

- Deliberation Tick RFC；
- Thought Trace Storage Policy RFC；
- Temporal Coherence Report；
- Review Depth Budget RFC；
- Unresolved Tension / Delayed Alignment RFC；
- Temporal Awareness Minimal Runtime Boundary RFC。

## P82 Non-Execution Statement / P82 非执行声明

P82 不实现：

- temporal runtime；
- CTM runtime；
- model training；
- new dependencies；
- temporal event writes；
- recall event writes；
- thought loop execution；
- `thought_trace` storage；
- `deliberation_tick` execution；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- policy execution；
- reconstruction reducer execution；
- companion、UI、AstrBot、adapter、cloud rollout 或 product layer。
