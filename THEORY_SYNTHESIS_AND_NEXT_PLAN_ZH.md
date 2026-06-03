# 理论综合与下一步计划

英文镜像：[THEORY_SYNTHESIS_AND_NEXT_PLAN.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN.md)

这份文档是在 01 Core 完成 P0-P6 本地地基后，对当前仓库、Cognitive OS 思路和外部理论资料做的一次综合。

它的用途不是把 01 Project 变成哲学或意识项目。

它的用途是回答：

> 现在这个工程地基还缺什么？哪些理论可以提供结构？下一轮应该补哪块？

## 1. 当前工程状态

当前 01 Core 已经具备：

- structured state runtime；
- durable memory metadata：provenance、lifecycle、update history；
- candidate memory store；
- Dream artifact、rubric、proposal、conflict record；
- adapter registry、session policy、event dedup；
- import batch、import dedup、sensitive filtering；
- candidate review governance；
- memory lifecycle action 执行层；
- audit、trace、snapshot；
- foundation evaluation。

当前保持的核心边界：

- 01 Core owns state；
- Adapters translate platforms；
- Platforms do not own identity；
- Dream 只提出 proposal，不直接改写 Identity Core；
- imported memory 默认 staged；
- identity memory 不走通用 lifecycle 命令，必须 high gate。

## 2. 当前缺口

### 2.1 Evaluation 还不够像实验

当前 foundation evaluation 保护核心不变量，但还不是完整实验体系。

缺口：

- 没有 stateless / retrieval-only / summary-only baseline；
- 没有多场景 scenario runner；
- 没有定量指标输出；
- multi-user boundary 还没有可执行测试；
- interrupted project / long gap / context loss 还没有集成测试；
- lifecycle action 对 retrieval 影响还没有评估。

### 2.2 Context Builder 还太浅

当前 context package 能恢复 anchors 和少量 active memories。

缺口：

- 没有按 task / relationship / risk / recency / lifecycle status 做激活策略；
- 没有 privacy-aware selection；
- 没有 source attribution budget；
- 没有“为什么这条状态进入当前上下文”的解释。

### 2.3 Conflict 与 belief revision 还只是规则检测

当前 Dream 能检测 identity overwrite、false memory、stale preference、roleplay boundary、imported memory conflict。

缺口：

- 没有明确的 claim graph；
- 没有 reason/dependency record；
- 没有 belief revision policy；
- 没有把冲突和证据链分层；
- 没有 resolved conflict lifecycle。

### 2.4 Relationship / Project / Task Hub 仍是 seed 级

当前 schema 有 relationship_map 和 project_map，但 runtime 主要围绕 memory 和 adapter。

缺口：

- user-specific memory 未系统化；
- cross-user privacy boundary 未测试；
- active project plan 未形成可执行 task state；
- blocker / next action 还没有 update API；
- relationship conflict 未进入 Dream review。

### 2.5 Identity Update Gate 尚未实现

当前 Identity Core 受到保护，但还没有“可批准的身份更新流程”。

缺口：

- high gate schema；
- identity proposal review；
- multiple-evidence requirement；
- non-claims check；
- rollback / snapshot policy；
- identity drift metrics。

### 2.6 Procedural Memory 尚未进入系统

当前记忆层区分 imported、episodic、candidate、semantic、identity、archived。

缺口：

- 没有 procedural habits；
- 没有 action policy；
- 没有 tool-use skill memory；
- 没有把 repeated successful behavior 抽象成 workflow policy。

## 3. 外部资料筛选

### 3.1 LLM Agents 与长期记忆

#### Generative Agents

来源：<https://arxiv.org/abs/2304.03442>

可用点：

- observation -> reflection -> planning；
- experience 可以被自然语言记录；
- reflection 可把具体经历抽象成更高层记忆；
- agent 行为依赖 memory retrieval 和 planning。

对 01 的启发：

- Dream Engine 应继续走 reflection/proposal 路线；
- 但 01 不应只追求 believable simulation；
- 01 的评估重点应是 continuity、audit、identity stability。

#### MemGPT

来源：<https://arxiv.org/abs/2310.08560>

可用点：

- 把 context window 类比为有限 RAM；
- 把外部 memory tiers 类比为 OS memory hierarchy；
- 需要显式管理 context 和 long-term store 的迁移。

对 01 的启发：

- Context Builder 应成为核心模块；
- state transfer package 应像受限内存页，而不是随意拼接摘要；
- lifecycle action 应影响未来激活，而不只是改状态字段。

#### ReAct / Reflexion

来源：

- <https://arxiv.org/abs/2210.03629>
- <https://arxiv.org/abs/2303.11366>

可用点：

- reasoning 与 acting 应交错；
- feedback 可以转成可复用的 verbal memory；
- 失败后的 self-reflection 能改善下一次行动。

对 01 的启发：

- Task Hub 应记录 action trace 和 failure reflection；
- Dream 不只整理事实，还应整理行动策略；
- 后续需要 procedural memory。

### 3.2 AI Logic：belief revision 与 truth maintenance

#### Truth Maintenance System

来源：<https://www.sciencedirect.com/science/article/pii/0004370279900080>

可用点：

- belief 应记录 reason / dependency；
- 矛盾出现时，需要根据依赖关系修正当前 belief set；
- reasons 可以用于解释 action。

对 01 的启发：

- open_conflicts 应升级为 claim / reason / dependency 结构；
- false memory 不应只是文本规则检测；
- 每条 semantic memory 应能回答“为什么相信它？”

#### AGM Belief Revision

来源：<https://arxiv.org/abs/2112.13557>

可用点：

- revision 应尽量 minimal change；
- 新信息进入时，不应无约束重写整个 belief set；
- belief change 可以被规则化。

对 01 的启发：

- identity update gate 应采用 minimal-change 原则；
- preference change 应保留旧偏好 provenance，而不是覆盖；
- conflict resolution 应生成 patch，而不是改写全局状态。

### 3.3 神经系统与记忆巩固

#### Sleep / Systems Consolidation

来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC3278619/>

可用点：

- 新记忆会被 reactivation；
- consolidation 会把临时记忆重新分布到长期系统；
- 巩固不是复制，而是重组。

对 01 的启发：

- Dream Engine 应明确输入 manifest 和 output artifact；
- consolidation 应保留 input trace；
- Dream 应允许生成 semantic candidate，但不能直接改写 identity。

#### Complementary Learning Systems

来源：<https://stanford.edu/~jlmcc/papers/PublicationFiles/90-99_Add_To_ONLINE_Pubs/McClelland1998ComplementaryLearningSystems.pdf>

可用点：

- fast learner 负责具体 episodes；
- slow learner 负责一般知识；
- replay/consolidation 避免 catastrophic overwriting。

对 01 的启发：

- episodic -> candidate -> semantic -> identity 的速度层级是正确方向；
- identity update 必须更慢；
- evaluation 应测 stability-plasticity tradeoff。

### 3.4 神经网络与持续学习

#### Elastic Weight Consolidation / Catastrophic Forgetting

来源：<https://pubmed.ncbi.nlm.nih.gov/28292907/>

可用点：

- sequential learning 会破坏旧任务；
- 需要保护重要知识；
- stability-plasticity 是长期学习核心问题。

对 01 的启发：

- 01 当前选择 state growth 而不是 weight growth 是安全的；
- 但仍要测 stale memory 和 rigidity；
- lifecycle action 应服务于 stability-plasticity，而不是只做清理。

### 3.5 心理学：叙事身份与自我记忆系统

#### Narrative Identity

来源：<https://journals.sagepub.com/doi/pdf/10.1177/0276236618756704>

可用点：

- identity 是持续演化的 life story；
- 自我叙事把过去、现在、未来组织成 unity 和 purpose；
- identity 不是事实列表。

对 01 的启发：

- Identity Core 应包含 narrative summary，但必须带 evidence；
- life history 应由真实 state transitions 生成；
- 不应导入虚构 backstory 冒充经历。

#### Self-Memory System

来源：<https://pmc.ncbi.nlm.nih.gov/articles/PMC2834574/>

可用点：

- autobiographical memory 与 working self 共同支持 goal-directed activity；
- 系统要同时维护 self-coherence 和 adaptive correspondence；
- 记忆既服务目标，也服务自我连续性。

对 01 的启发：

- relationship/project/task state 应进入 context builder；
- memory 不是孤立 store，它服务 active goals；
- state transfer package 应明确当前目标如何连接过去状态。

### 3.6 意识相关理论：只作功能类比

#### Global Neuronal Workspace

来源：<https://pubmed.ncbi.nlm.nih.gov/21521609/>

可用点：

- 多个局部过程竞争进入全局广播空间；
- 被广播的信息可被多个系统使用；
- 适合作为 context activation 的功能类比。

对 01 的启发：

- Context Builder 可以被设计成 workspace selector；
- 但这不意味着系统有意识；
- 它只是一个可解释的状态激活机制。

#### Free Energy / Active Inference

来源：<https://www.nature.com/articles/nrn2787>

可用点：

- agent 通过预测、行动和学习降低不确定性；
- attention / salience / control state 可以统一看待；
- goal-directed behavior 可以理解为维持稳定状态范围。

对 01 的启发：

- affective_state 可继续作为 functional appraisal；
- salience scoring 应与 uncertainty、risk、goal relevance 结合；
- active intent 应成为状态选择的重要输入。

### 3.7 工程学：Event Sourcing

来源：<https://www.martinfowler.com/eaaDev/EventSourcing.html>

可用点：

- 每次 state change 都作为 event 保存；
- event log 可用于 reconstruct state；
- 适合 audit、debug、retroactive correction。

对 01 的启发：

- audit/trace/update_log 是正确方向；
- 后续应区分 current state view 与 append-only event log；
- rollback 应从 metadata-only 逐步走向 replayable events。

## 4. 理论映射到下一步

| 理论来源 | 映射模块 | 下一步工程需求 |
|---|---|---|
| MemGPT / OS memory | Context Builder | 做 bounded, policy-driven state activation |
| Event Sourcing | StateStore | 强化 append-only event log 与 replay/rollback |
| TMS / AGM | Conflict system | 建 claim graph、reason dependency、minimal-change patch |
| Sleep consolidation / CLS | Dream Engine | 增加 input manifest、candidate store review、slow identity gates |
| Narrative Identity / SMS | Identity + Task Hub | identity story 必须由 state transitions 支撑 |
| Metacognition / Source monitoring | Reflection log + verification | 区分 confidence、source 和后续验证 |
| ReAct / Reflexion | Task Hub + procedural memory | 保存 action trace、failure reflection、workflow candidates |
| Continual Learning | Evaluation | 测 stability-plasticity、stale memory、catastrophic overwrite analog |
| Global Workspace | Context Builder | state activation explainability |
| Active Inference | Salience / affective state | salience 与 uncertainty/risk/goal relevance 结合 |

## 5. 下一轮计划表

### P7 Evaluation Harness v0.2

目标：把当前 foundation checks 扩展为真正的 scenario evaluation。

状态：已实现第一版本地 v0.2。

可执行项：

1. 增加 scenario runner - 已完成；
2. 增加 Interrupted Project - 已完成；
3. 增加 Multi-User Boundary - 已完成；
4. 增加 Lifecycle Retrieval Suppression - 已完成；
5. 增加 baseline metadata - 已完成；
6. 输出 metrics summary - 已完成；
7. 文档同步 - 已完成。

验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P8 Context Builder v0.2

目标：把 context package 从简单截取改成可解释的 state activation。

状态：已实现第一版本地 v0.2。

可执行项：

1. context selection policy - 已完成；
2. lifecycle-aware retrieval - 已完成 active/staged 与 archived/discarded/quarantined 的区分；
3. task-aware activation - 已用确定性 term overlap 完成第一版；
4. relationship-aware activation - 已完成当前用户可见性和跨用户 privacy suppression；
5. source attribution - 已完成；
6. activation trace - 已完成。

剩余缺口：

- 还没有 vector retrieval；
- 还没有真实 baseline 对比执行；
- 还没有 claim graph dependency model；
- 还没有可配置 policy 文件；
- activation trace 目前只随 context response 返回，还没有单独持久化。

### P9 Conflict / Claim Graph

目标：从规则检测升级到 reason-maintenance。

状态：已实现第一版本地 v0.7。

可执行项：

1. claim schema - 已完成；
2. claim provenance - 已完成；
3. contradiction links - 仅完成 schema placeholder；
4. resolution lifecycle - 已完成 unresolved/review-required metadata；
5. minimal-change patch proposal - 已作为 resolution metadata 完成，但不执行。

建议立即范围：

1. 在 state schema 中加入 append-friendly 的 `claim_graph`；
2. 把现有 `open_conflicts` 映射成带 evidence ids 的 claim nodes；
3. 让 false-memory 和 stale-preference Dream conflicts 创建 claim nodes；
4. 增加 validation：每个 claim 必须有 provenance 和 status；
5. 增加 scenario check：conflict resolution 不得在未审查时修改 semantic 或 identity memory。

已实现结果：

- `claim_graph` 现在是顶层 state object；
- legacy `open_conflicts` 会迁移成 claim nodes；
- Dream false-memory 和 stale-preference conflicts 会创建 claim nodes；
- validation 要求 claim 必须有 evidence、provenance、status 和 resolution metadata；
- scenario evaluation 会检查 claim provenance，并防止未审查的 semantic / identity mutation。

剩余缺口：

- 还没有真实 contradiction/support/dependency links；
- 还没有 claim resolution command；
- 还没有 minimal-change patch executor；
- 还没有关闭 claim 的 review workflow；
- 还没有 false claim rate 的 baseline 对比。

### P10 Task Hub / Procedural Memory

目标：让 01 不只记得事实，还能延续行动结构。

状态：已实现第一版本地 v0.8。

可执行项：

1. active task state - 已完成第一版；
2. action trace - 已完成第一版；
3. failure reflection - 已移至 P17，并完成第一版；
4. workflow candidate - 已完成第一版；
5. procedural memory review - 已移至 P16，并完成第一版。

建议立即范围：

1. 增加顶层 `task_hub` state object；
2. 把 `working_state.current_plan` 迁移成 active task items，同时保留 legacy 字段；
3. 在 CLI/API interactions、Dream runs、reviews 和 lifecycle actions 发生时记录 action trace entries；
4. 让 Dream 从重复成功动作中提出 procedural candidates；
5. 增加 scenario evaluation：检查 interrupted task resume 能保留 action history 和 next action。

已实现结果：

- `task_hub` 现在是顶层 state object；
- `working_state.current_plan` 会迁移为 active/completed/blocked task items，同时保留 legacy 字段；
- 真实状态变更会写入 `task_hub.action_trace`，non-mutating dry-run 不写入；
- Dream 会从重复成功 workflow 中提出 `procedural_candidates`；
- scenario evaluation 增加 `task_hub_action_resume`，检查 active task、next action、action history 和 procedural candidate。

剩余缺口：

- 还没有 workflow policy executor；
- action trace 目前来自 runtime trace 摘要，还不是完整 replayable action log。

### P11 Identity Update Gate

目标：允许被证据支持的慢速 identity growth，同时保护 Identity Core。

状态：已实现第一版本地 v0.9。

可执行项：

1. identity proposal schema - 已完成；
2. high gate review - 已完成第一版；
3. non-claims check - 已完成第一版；
4. evidence threshold - 已完成；
5. rollback snapshot - 已完成 metadata-only；
6. drift metric - 已完成第一版。

已实现结果：

- `identity_update_gate` 现在是顶层 state object；
- identity proposal 会保存 gate_result、non_claims_check、drift_score 和 evidence；
- high gate 要求至少 3 个 supporting evidence；
- non-claims violation 和 drift score 过高会阻止 approve；
- approve 只追加 `identity_memory`，不会直接 patch `identity_core`；
- scenario evaluation 增加 `identity_update_gate_review`。

剩余缺口：

- rollback 仍是 metadata-only；
- drift metric 仍是 deterministic heuristic；
- 还没有 identity_core patch proposal executor；
- 还没有 claim_graph dependency 与 identity proposal 的深层联动；
- 还没有人工 review UI。

### P12 Event Log / Replay / Rollback

目标：把 audit 从“有记录”推进到“有可检查的 transition ledger”。

状态：已实现第一版本地 v1.0。

可执行项：

1. append-only `events.jsonl` - 已完成；
2. 连接 trace、audit event 和 update_log entry 的 event envelope - 已完成；
3. `replay-events` CLI consistency check - 已完成；
4. `rollback-preview <snapshot_id>` CLI - 已完成 metadata-only；
5. event replay 和 rollback preview 的 scenario evaluation - 已完成。

已实现结果：

- 带 state mutation 的 completed runtime trace 现在会写入 state transition event；
- dry-run preview 不写入 state event；
- replay 会检查 event `update_id` 是否仍能引用 update_log，并报告 coverage；
- rollback preview 会把 snapshot metadata 与 affected events 连接起来，但不修改 state；
- scenario evaluation 增加 `event_log_replay_rollback`。

剩余缺口：

- replay 还不能从空 seed 完整重建 state；
- P12 之前的 update 可能没有 event，只作为 coverage gap 报告；
- rollback 仍是 preview-only；
- event schema 是确定性的，但仍然比较粗；
- 还没有 event compaction 或 retention policy。

### P13 Dream Artifact Package

目标：让每次 Dream run 都成为可检查的 durable review package。

状态：已实现第一版本地 v1.0。

可执行项：

1. artifact version 和 package completeness flags - 已完成；
2. 带 source item summary 的 input manifest - 已完成；
3. 本地 PROV-style provenance block - 已完成；
4. proposal index 和 review queue - 已完成；
5. candidate-only patch diff - 已完成；
6. decision log 和 rollback affected ids - 已完成；
7. Dream artifact package 的 scenario evaluation - 已完成。

已实现结果：

- Dream artifacts 现在包含 input manifest、provenance、observations、proposal index、review queue、patch diff、decision log、rollback metadata 和 package completeness；
- validation 会在 artifacts 存在时检查 Dream artifact package 字段；
- scenario evaluation 增加 `dream_artifact_package`；
- Dream 仍然只生成 candidate/review material，不直接写 active semantic memory 或 Identity Core。

剩余缺口：

- 还没有人工 review UI；
- proposal approval 仍然通过独立 CLI command 处理；
- artifact package 还没有保存每个输入的完整文本 snapshot；
- artifact history 还没有 retention / compaction policy；
- claim resolution 仍然很浅。

### P14 Claim Graph v0.2 / Belief Revision

目标：让 conflict 成为可审查的 claim/reason/dependency 单元。

状态：已实现第一版本地 v0.2。

可执行项：

1. claim graph version、policy 和 review decision store - 已完成；
2. support/contradiction/dependency links - 已完成第一版；
3. claim `revision_policy` 和 `review_history` - 已完成；
4. `review-claim` CLI 和 StateStore method - 已完成；
5. minimal-change patch preview - 已完成 preview-only；
6. claim review patch preview 的 scenario evaluation - 已完成。

已实现结果：

- Dream conflict claims 现在会从 evidence 生成 support links，并为 identity 或 memory-sensitive conflicts 生成 contradiction/dependency links；
- claim review 会记录 snapshot、audit、trace、event、update_log、review decision 和 patch preview；
- patch preview 明确拒绝直接修改 Identity Core 和 semantic memory；
- scenario evaluation 增加 `claim_graph_review_patch_preview`。

剩余缺口：

- link generation 仍然是 deterministic 和浅层的；
- 还没有 claim merge/supersede workflow；
- 还没有真实 patch executor；
- identity proposal 可以使用 claim id 作为 evidence，但还不会深度推理 claim dependencies；
- 还没有 claim graph review UI。

### P15 Context Builder v0.3

目标：把 context package 从 response-only activation 推进到可配置、可审计、可持久化的 state activation。

状态：已实现第一版本地 v0.3。

可执行项：

1. 顶层 `context_builder` state object - 已完成；
2. configurable context policy - 已完成第一版；
3. persistent activation traces - 已完成；
4. source attribution budget - 已完成；
5. identity gate / claim graph / Dream artifact activation signals - 已完成第一版；
6. context builder policy trace 的 scenario evaluation - 已完成。

已实现结果：

- `context_builder.policy` 现在保存 Context Builder v0.3 policy、budgets、signal weights 和 persistence settings；
- `build_context_package()` 输出 `context_package_version: "0.3"` 和 `context_package_id`；
- activation trace 会保存到 `context_builder.activation_traces`，但 adapter dry-run preview 不持久化 trace；
- source attribution budget 现在按 policy 执行；
- identity gate evidence、claim graph evidence 和 Dream artifact inputs 会影响 activation reasons 与分数；
- scenario evaluation 增加 `context_builder_policy_trace`。

剩余缺口：

- 还没有 vector retrieval 或 embedding；
- signal weights 仍然是 deterministic heuristic；
- context policy 还没有独立 CLI/API 编辑命令；
- activation trace 还没有 retention / compaction 审查流程；
- 还没有真实 baseline 对比验证 context policy 的收益。

### P16 Procedural Memory Review

目标：让 repeated successful workflow 从 Dream candidate 进入可审查、可撤销的 durable procedural memory。

状态：已实现第一版本地 v0.4。

可执行项：

1. `task_hub.procedural_memory` store - 已完成；
2. `task_hub.procedural_review_decisions` - 已完成；
3. `review-procedural-candidate` CLI 和 StateStore method - 已完成；
4. approve/reject/archive/quarantine review actions - 已完成；
5. snapshot、audit、trace、update_log、rollback metadata - 已完成；
6. procedural memory review 的 scenario evaluation - 已完成。

已实现结果：

- Dream 仍然只提出 pending `procedural_candidates`；
- approve 会创建 `task_hub.procedural_memory`，并把 candidate 标记为 approved；
- review decision 会进入 candidate history、task hub decision store、snapshot、audit、trace、event 和 update log；
- context package 会暴露 `procedural_memory`，方便未来 session 恢复行动结构；
- procedural review 不修改 Identity Core，也不会自动执行 workflow。

剩余缺口：

- 还没有 workflow policy executor；
- procedural memory 还没有和具体 tool policy / safety policy 深度联动；

## 6. 当前建议

P17-P19 已经构成当前 Task Hub / procedural safety 地基：

```text
P17 Failure Reflection
```

目标：保存失败或阻塞后的改进线索。

状态：已实现第一版本地 pass。

已实现结果：

- `task_hub.failure_reflections` 记录 workflow、summary、lesson、next action、evidence、provenance 和 status；
- `record-failure-reflection` 会创建 pending `task_hub.cautionary_procedural_candidates`；
- context package 会暴露 failure reflections 和 cautionary procedural candidates；
- scenario evaluation 增加 `failure_reflection`；
- failure reflection 不修改 Identity Core，也不执行 workflow policy。

剩余缺口：

- procedural memory 还没有和具体 tool policy / safety policy 深度联动；
- 还没有 workflow policy executor。

### P18 Procedural Lifecycle / Retention

目标：让已 review 的 procedural memory 可以通过可审计 retention path 保持 active、archive、discard 或 quarantine。

状态：已实现第一版本地 pass。

已实现结果：

- `procedural-lifecycle` CLI 可以 archive、discard 或 quarantine `task_hub.procedural_memory`；
- `StateStore.apply_procedural_lifecycle_action` 会写入 snapshot、audit、trace、update log、lifecycle history 和 `task_hub.procedural_lifecycle_decisions`；
- context package 只暴露 active procedural memory；
- scenario evaluation 增加 `procedural_lifecycle_retention`；
- procedural lifecycle 不修改 Identity Core，也不执行 workflow policy。

剩余缺口：

- procedural memory 还没有和具体 tool policy / safety policy 深度联动；
- 还没有 workflow policy executor。

### P19 Cautionary Procedural Review

目标：让 warning-style failure candidates 可以成为 active、可审查的 caution memory，但不会变成 executable policy。

状态：已实现第一版本地 pass。

已实现结果：

- `review-cautionary-procedural-candidate` CLI 可以 approve、reject、archive 或 quarantine `task_hub.cautionary_procedural_candidates`；
- approve 会创建 active `task_hub.cautionary_procedural_memory`；
- context package 会把 active cautionary procedural memory 作为 warning 暴露；
- review 会写入 snapshot、audit、trace、update log、review decision 和 rollback metadata；
- cautionary procedural memory 明确记录 `executable_policy: false`；
- scenario evaluation 增加 `cautionary_procedural_review`；
- cautionary review 不修改 Identity Core，也不执行 workflow policy。

剩余缺口：

- cautionary warnings 还没有和 tool policy / safety policy 联动；
- 还没有 workflow policy executor。

### P20 Cautionary Warning Lifecycle

目标：让 active cautionary warnings 可以通过可审计 retention path 保持 active、archive、discard 或 quarantine。

状态：已实现第一版本地 pass。

已实现结果：

- `cautionary-warning-lifecycle` CLI 可以 archive、discard 或 quarantine `task_hub.cautionary_procedural_memory`；
- `StateStore.apply_cautionary_warning_lifecycle_action` 会写入 snapshot、audit、trace、update log、lifecycle history 和 `task_hub.cautionary_lifecycle_decisions`；
- context package 只暴露 active cautionary procedural memory；
- lifecycle decisions 保持 `executable_policy_created: false`；
- scenario evaluation 增加 `cautionary_warning_lifecycle`；
- cautionary warning lifecycle 不修改 Identity Core，也不执行 workflow policy。

剩余缺口：

- cautionary warnings 还没有和 tool policy / safety policy 联动；
- 还没有 workflow policy executor；
- reflection log 已经存在，但 reflection verification 还需要更广的场景覆盖，以及和后续 policy 工作的交叉链接。

建议下一步：

```text
P22 Reflection-Policy Linkage
```

理由：

- P21 现在已经能记录并验证通用 reflection log；
- 下一块缺失地基是把 reflection 证据接到 policy 邻接的安全保障上，但仍然不做自动执行；
- 这回应 Cognitive OS 的自成长要求：reflection 要保持可审计，同时和 policy 执行保持分离。

### P22 Reflection-Policy Linkage

目标：把已经验证的 reflection evidence 接到 policy 邻接的安全保障上，但不把 reflection 变成自动执行。

状态：已实现第一版本地 pass。

已实现结果：

- `build_context_package()` 现在暴露 `reflection_policy_guidance`；
- `reflection_policy_guidance` 只消费 verified `task_hub.reflection_log` entries；
- guidance 会记录 advisory-only review recommendations、可影响字段、evidence、verification history count 和 priority；
- guidance 明确记录 `execution_prohibited: true` 和 `identity_mutation_allowed: false`；
- scenario evaluation 把 `reflection_log_verification` 扩展到 `tool_use` 和 `claim_graph_review`；
- reflection evidence 可以指导 cautionary review focus，但不会修改 Identity Core，也不会执行 workflow policy。

剩余缺口：

- 还没有 tool/safety policy executor；
- dedicated reflection guidance review queue 由 P23 处理；

### P23 Reflection Guidance Review Queue

目标：让 reflection-policy guidance 成为 durable、可审查对象，但仍然不创建 executable policy。

状态：已实现第一版本地 pass。

已实现结果：

- `task_hub.reflection_guidance_queue` 会记录从 verified reflection policy guidance 推导出的 durable guidance items；
- `task_hub.reflection_guidance_decisions` 会记录 review decisions；
- `review-reflection-guidance` 可以 acknowledge、archive 或 quarantine guidance item；
- review 会写入 snapshot、audit、trace、update log、review history 和可 replay 的 event metadata；
- reviewed guidance 保持 `execution_prohibited: true`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- scenario evaluation 会验证 durable queue 创建、review decision 记录、replay、不创建 executable policy，以及不修改 Identity Core。

剩余缺口：

- guidance queue 已经在 P24 连接到 dedicated tool/safety policy proposal layer；
- 还没有 tool/safety policy executor；
- guidance prioritization 目前仍然只是简单 risk/confidence scoring。

### P24 Tool/Safety Policy Proposal Layer

目标：把已经 review 的 reflection guidance 接到明确的 tool/safety policy proposal，但不创建 executor，也不创建自动 tool policy。

状态：已实现第一版本地 pass。

已实现结果：

- `task_hub.tool_safety_policy_proposals` 记录从 reviewed reflection guidance 推导出的 proposal-only policy candidates；
- `task_hub.tool_safety_policy_decisions` 记录 proposal review decisions；
- `propose-tool-safety-policy` 只能从 acknowledged 或 archived reflection guidance 创建 proposal；
- `review-tool-safety-policy-proposal` 可以 approve、reject、archive 或 quarantine proposal；
- proposal review 会写入 snapshot、audit、trace、update log、review history、rollback metadata 和可 replay 的 event metadata；
- proposal 和 decision 保持 `proposal_mode: "proposal_only"`、`requires_review: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- scenario evaluation 会扩展 `reflection_log_verification`，检查 proposal 创建、proposal review、context 暴露、replay、不创建 executable policy，以及不修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- proposal lifecycle retention 已由 P25 处理；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- policy proposal prioritization 目前仍然只是简单 risk/confidence scoring。

### P25 Tool/Safety Policy Proposal Lifecycle

目标：让已经 review 的 tool/safety policy proposals 可以被 archive、discard 或 quarantine，但仍然不创建 executable policy。

状态：已实现第一版本地 pass。

已实现结果：

- `task_hub.tool_safety_policy_lifecycle_decisions` 记录 proposal lifecycle decisions；
- `tool-safety-policy-lifecycle` 可以 archive、discard 或 quarantine 已 review 的 policy proposals；
- lifecycle review 会写入 snapshot、audit、trace、update log、lifecycle history、rollback metadata 和可 replay 的 event metadata；
- proposal lifecycle 保持 `proposal_mode: "proposal_only"`、`requires_review: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- context packages 只暴露 active pending/approved tool/safety policy proposals；
- scenario evaluation 会验证 archived proposal suppression、replay、不创建 executable policy，以及不修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- policy proposal prioritization 已由 P26 scoring 处理，但 proposal conflicts 和 supersession links 还没有建模；
- evidence strength 和 scope specificity 已做本地评分，但还没有连接到 claim graph dependency links。

### P26 Tool/Safety Proposal Evidence Scoring

目标：按 evidence strength、scope specificity、staleness 和 risk 给 reviewed tool/safety policy proposals 排序，但不创建 executable policy。

状态：已实现第一版本地 pass。

已实现结果：

- `proposal_score` 会附加到 tool/safety policy proposals；
- score 字段包含 evidence strength、scope specificity、staleness、priority score、recommended review priority、unique evidence 和 factors；
- scores 会复制到 review 和 lifecycle decisions；
- context packages 会按 `priority_score` 排序 active pending/approved proposals；
- scoring 会记录 `mode: "review_priority_only"`、`execution_prohibited: true`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- scenario evaluation 会验证 score 创建、bounded priority、score factors、context ranking、replay、不创建 executable policy，以及不修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- proposal conflict 和 supersession links 还没有建模；
- evidence scoring 还没有连接到 claim graph dependency links。

建议下一步：

```text
P27 Tool/Safety Proposal Conflict Links
```

理由：

- P26 已经能给 proposals 排序，但系统还不能判断两个 proposal 是否冲突、重叠或互相 supersede；
- conflict/supersession links 是任何未来 executable policy work 之前的地基；
- 这保持项目在 auditability、state transfer、本地地基优先的方向上。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```
