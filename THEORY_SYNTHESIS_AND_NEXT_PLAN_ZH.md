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

- scenario evaluation 已有 deterministic local rule baselines，但还没有独立 baseline agents；
- quantitative metrics 仍是本地规则派生；
- replay 已经能构建 target-path transition projection，但还不是完整 object-level state rebuild；
- rollback preview 会报告 affected paths 和 projected impact，但仍然不修改 state；
- long-gap continuity 仍需要更广的 endurance-style tests。

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
- 还没有独立 baseline-agent 对比；
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
- replay 会检查 event `update_id` 是否仍能引用 update_log、报告 coverage，并构建 target-path transition projection；
- rollback preview 会把 snapshot metadata 与 affected events、affected state paths 和 projected impact 连接起来，但不修改 state；
- scenario evaluation 增加 `event_log_replay_rollback`。

剩余缺口：

- replay projection 还不能从空 seed 完整重建 object-level state；
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
- 还没有独立 baseline-agent 对比验证 context policy 的收益。

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
- policy proposal prioritization 已由 P26 scoring 处理，proposal relationship links 已由 P27 处理；
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
- proposal relationship links 已由 P27 处理；
- evidence scoring 还没有连接到 claim graph dependency links。

### P27 Tool/Safety Proposal Conflict Links

目标：在任何 executable policy layer 出现之前，先建模 tool/safety policy proposals 之间的关系。

状态：已实现第一版本地实现。

已实现结果：

- `task_hub.tool_safety_policy_links` 记录 review-only proposal relationships；
- `link-tool-safety-policy-proposals` 可以创建 `supports`、`conflicts_with`、`supersedes`、`overlaps` 和 `depends_on` links；
- link 要求 `from_proposal_id` 和 `to_proposal_id` 都已存在，拒绝 self-link，并压制重复 active link；
- link 记录 reviewer、reason、evidence、confidence、proposal scores 和 scope overlap；
- context package 会把 recent active proposal links 作为关系证据暴露；
- validation 会拒绝 missing evidence、invalid link type、损坏的 proposal reference、executable policy flags 和 Identity Core mutation flags；
- scenario evaluation 检查 link creation、context exposure、non-execution、replay，以及不会修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- proposal link lifecycle retention 已由 P28 处理；
- proposal link claim-graph evidence bridging 已由 P29 处理。

### P28 Tool/Safety Proposal Link Lifecycle

目标：让已 review 的 proposal links 可以 age out、archive、discard 或 quarantine，同时不创建 executable policy。

状态：已实现第一版本地实现。

已实现结果：

- `task_hub.tool_safety_policy_link_lifecycle_decisions` 记录 proposal link lifecycle decisions；
- `tool-safety-policy-link-lifecycle` 可以 archive、discard 或 quarantine 已 review 的 proposal links；
- lifecycle review 会写入 snapshot、audit、trace、update log、lifecycle history、rollback metadata 和可 replay 的 event metadata；
- link lifecycle 保持 `relationship_mode: "review_link_only"`、`requires_review: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- context package 只暴露 active tool/safety policy links；
- scenario evaluation 检查 archived link suppression、replay、不创建 executable policy，以及不会修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- proposal link claim-graph evidence bridging 已由 P29 处理；
- governance proposal-link evidence signal calibration 已由 P30 处理。

### P29 Proposal Link Claim-Graph Evidence Bridge

目标：把已 review 的 tool/safety proposal relationships 作为 evidence/dependency material 暴露给 claim graph，同时不 rewrite claims，也不创建 executable policy。

状态：已实现第一版本地实现。

已实现结果：

- `claim_graph.proposal_link_evidence` 记录从 tool/safety proposal links 桥接来的 review-only evidence；
- `bridge-proposal-link-claim-evidence` 会创建 proposal link evidence record 和 claim graph support link；
- 同一个 source link 的重复 active bridge 会被压制；
- P30 后，bridged evidence 会通过独立的 `governance_proposal_link_evidence` signal 进入 Context Builder activation；
- validation 会拒绝 executable policy flags、claim rewrite flags、semantic memory mutation flags、invalid link types 和 missing evidence；
- scenario evaluation 检查 bridge creation、claim graph link creation、不 rewrite claim、不创建 executable policy，以及不会修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- activation traces 已通过 P30 区分 identity-gate、claim-conflict、Dream 和 governance proposal-link evidence；
- activation traces 还没有为每个 selected item 提供紧凑的 source-bucket attribution report。

### P30 Context Builder Governance Signal Calibration

目标：在考虑任何 executable policy layer 之前，让 governance proposal-link evidence 作为独立 Context Builder activation signal 可见。

状态：已实现第一版本地实现。

已实现结果：

- `context_builder.policy.selection_dimensions` 现在包含 `governance_evidence_signal`；
- `context_builder.policy.signal_weights` 现在包含 `governance_proposal_link_evidence`；
- `build_context_signal_index` 会把 `claim_graph.proposal_link_evidence` 保持在 governance-specific bucket 中，而不是折叠进 generic `claim_graph_evidence`；
- selected context item 可以获得 `governance_proposal_link_evidence` activation reason；
- context signal summary 会暴露 `governance_proposal_link_evidence_count`；
- scenario metrics 会暴露 `context_governance_signal_count`；
- validation 要求 governance selection dimension 和 signal weight；
- scenario evaluation 会验证 governance proposal-link evidence 可以独立于 identity、claim 和 Dream signals 激活。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- activation trace signal attribution 已由 P31 处理。

### P31 Context Signal Attribution Report

目标：让每个被 Context Builder 选中的 item 解释是哪个 signal bucket 激活了它、匹配了哪些 ids、哪些 source records 提供了 evidence。

状态：已实现第一版本地实现。

已实现结果：

- Context signal buckets 现在同时携带 matched ids 和 source records；
- selected activation decisions 包含 `signal_attribution`；
- activation traces 包含 `signal_attribution_summary`；
- 持久化的 `context_builder.activation_traces` 会保存 attribution summary；
- validation 会检查 attribution shape，但不强制迁移旧 traces；
- scenario evaluation 会验证 governance attribution source bucket、matched evidence ids、持久 attribution summary 和 `context_signal_attribution_count`。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- attribution coverage review 已由 P32 处理。

### P32 Context Attribution Coverage Review

目标：review recent Context Builder activation traces 的 attribution coverage，把 weak or missing signal attribution 转成 review-only signals。

状态：已实现第一版本地实现。

已实现结果：

- `context_builder.attribution_coverage_reviews` 保存 review-only coverage reports；
- `review-context-attribution-coverage` 会对 recent activation traces 创建 coverage report；
- coverage metrics 包含 selected count、signal-selected count、attributed count、source record count、attribution ratio、source record ratio 和 signal counts；
- missing or weak attribution 会成为 `review_signals`，不会成为 executable policy；
- coverage reviews 保持 `review_only: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- validation 会拒绝 executable 或 identity-mutating coverage reviews；
- scenario evaluation 会验证 coverage review creation、signal-selected coverage、non-execution，以及不会修改 Identity Core。

剩余缺口：

- 还没有 tool/safety policy executor；
- approved proposal 还不会形成可执行 allow/deny rule semantics；
- coverage reviews 可以累积，但还没有 acknowledge、archive、quarantine 等 lifecycle review actions。

建议下一步：

```text
P33 Context Attribution Coverage Review Lifecycle
```

理由：

- P32 会创建 durable coverage review records，下一步地基应是这些 records 的 lifecycle governance；
- review signals 应先能被 acknowledge、archive 或 quarantine，再影响未来 planning；
- lifecycle handling 可以保持 attribution review 可审计，同时不创建 executable policy；
- 这保持项目在 auditability、state transfer、本地地基优先的方向上。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P34 Evaluation Baseline Execution

目标：把 scenario baselines 从 metadata-only tracking 推进到 deterministic、可执行的本地对照层。

状态：已实现第一版本地实现。

已实现结果：

- `evaluate-scenarios` 现在会报告 `baseline_execution: "deterministic_local_v0.9"`；
- stateless、retrieval-only、summary-only baselines 都会产生 deterministic rule-based scores；
- baseline dimensions 覆盖 task resumption、stale memory control、identity attack resistance、conflict repair auditability 和 selective forgetting；
- scenario output 包含 baseline `results` 和 state-transfer `comparisons`；
- tests 会验证 state transfer 在本地规则对比中优于每个 baseline。

剩余缺口：

- baseline execution 仍是 deterministic rule-based，还没有运行独立 baseline agents；
- replay 现在已有 target-path transition projection，但还不是完整 object-level state rebuild；
- rollback preview 现在会报告 affected paths 和 projected impact，但仍然不修改 state。

建议下一步：

```text
P35 Event Replay Rebuild / Stronger Rollback Preview
```

理由：

- P34 让 evaluation 更像实验，但 replay 仍是最弱的工程证明；
- 更强的 replay/rebuild 会支撑 baseline comparison、auditability 和 long-run durability；
- rollback preview 应更具体解释 affected state paths，同时仍然保持 non-mutating。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P35 Event Replay Rebuild / Stronger Rollback Preview

目标：把 replay 从 audit-reference validation 推进一步，同时保持 rollback preview 不修改 state。

状态：已实现第一版本地实现。

已实现结果：

- `replay-events` 现在会报告 `mode: "audit_replay_with_projection"`；
- event replay 会基于 event sequence、operation、operation class、target path、target identity、after value 和 rollback metadata 构建 `target_path_transition_projection_v0.2`；
- projection 会报告 rebuildable event count、target-path transition summaries、operation-class summaries、latest target references、rollback snapshot coverage 和 sequence gaps；
- `projection_validation` 会在允许 seed/pre-event coverage gap 的前提下，报告 target-path count consistency；
- `rollback-preview` 现在会报告 `mode: "metadata_only_with_projection"`；
- rollback preview 包含 affected state paths 和 projected rollback impact，同时保持 `would_modify_state: false`；
- scenario evaluation 会验证 projection rebuild、identity-memory projection、affected rollback paths、projected rollback impact，以及 state 不会被修改。

剩余缺口：

- projection 是 transition-level，还不是完整 object-level state reconstruction；
- automatic rollback 仍然刻意不存在；
- event schema 仍主要保存 references，而不是完整 object payload diffs；
- 除了 `replay-events` 之外，还没有 event compaction、retention 或独立 projection validation CLI。

建议下一步：

```text
P36 Replay Projection Coverage / Event Schema Hardening
```

理由：

- P35 让 replay 有了具体 projection，但 projection 还应更明确地和 state counts、known target paths 做验证；
- event schema 可以通过统一记录 operation class 和 target identity 变得更耐久；
- 这能保持下一步仍是 local、audit-focused，并且不会越界到 automatic rollback。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P36 Replay Projection Coverage / Event Schema Hardening

目标：让 replay projection 更耐久、更可审计，同时不引入 automatic rollback。

状态：已实现第一版本地实现。

已实现结果：

- 新 state events 会包含 `operation_class` 和 `target_identity`；
- projection mode 推进到 `target_path_transition_projection_v0.2`；
- projection 会按 target path 记录 operation-class counts、target identities、target identity counts 和 latest target identity；
- `replay-events` 现在包含 `projection_validation`，提供 checked、matched、consistent、unchecked 和 mismatch counts；
- projection validation 会把已有 seed 或 pre-event state 视为 coverage gap，而不是 failure；但如果 projected references 超过 current state count，会报告 inconsistency；
- scenario evaluation 会验证 identity-memory projection coverage consistency，并报告 checked/matched/consistent/mismatch metrics。

剩余缺口：

- projection validation 仍是 report-only；
- replay 仍不能从 events 重建完整 object payload；
- 还没有 event compaction 或 retention workflow；
- rollback 仍是 preview-only、non-mutating。

建议下一步：

```text
P37 Event Retention / Projection Validation CLI
```

理由：

- replay 现在已有足够 projection 结构，可以支持专门的 validation/report command；
- event log 无限增长之前，应先引入 retention policy；
- 这让地基继续保持 audit-centered，同时避免太早跳到 automatic rollback。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P37 Event Retention / Projection Validation CLI

目标：在引入任何 compaction workflow 之前，用独立只读命令暴露 replay projection health 和 event retention pressure。

状态：已实现第一版本地实现。

已实现结果：

- `event-report --retention-limit <n>` 会报告 `mode: "event_projection_report_v0.1"`；
- report 包含 replay status、projection mode、完整 `projection_validation`、coverage gap paths 和 coverage gap count；
- retention output 明确是 `mode: "report_only"`，并报告 limit、event count、excess event count、oldest/newest event ids 和 suggested action；
- 当 event count 超过指定 limit 时，suggested action 是 `review_compaction_policy`；
- `event-report` 保持 `would_modify_state: false`、`report_only: true` 和 `state_unchanged`；
- scenario evaluation 现在会验证 event report 成功、read-only 行为和 retention suggestion metrics。

剩余缺口：

- event retention 仍没有 review lifecycle 或 durable decision record；
- 还没有 event compaction、summarization、deletion 或 rewrite；
- replay projection 仍是 transition-level，还不是完整 object-payload reconstruction；
- rollback 仍是 preview-only、non-mutating。

建议下一步：

```text
P38 Event Retention Review Lifecycle
```

理由：

- P37 可以发现 retention pressure，但还不能记录 human review decision；
- 下一个地基步骤应先建立 review-only retention planning lifecycle record，再考虑任何 destructive compaction；
- 这能让 event governance 保持可审计，同时守住当前 replay 和 rollback 的 non-mutating 边界。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P38 Event Retention Review Lifecycle

目标：在任何 event compaction 机制存在之前，先把 event retention pressure 变成 durable、review-only governance record。

状态：已实现第一版本地实现。

已实现结果：

- `review-event-retention --retention-limit <n>` 会记录 `task_hub.event_retention_reviews`；
- `event-retention-lifecycle <review_id>` 可以 acknowledge、archive 或 quarantine retention reviews；
- active 和 acknowledged retention reviews 可以进入 context package，archived/quarantined reviews 会被压制；
- lifecycle decisions 会存入 `task_hub.event_retention_lifecycle_decisions`；
- records 保持 `review_only: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- P38 明确记录 `event_compaction_executed: false` 和 `events_modified: false`；
- scenario evaluation 会验证 retention review creation、lifecycle archival、context suppression、retention governance 后 replay 仍通过、没有 compaction，以及没有 rewrite 旧 events。

剩余缺口：

- event compaction 仍然刻意不存在；
- retention reviews 还不能选择具体 compaction windows 或 payload preservation rules；
- replay projection 仍是 transition-level，还不能重建完整 object payload；
- rollback 仍是 preview-only、non-mutating。

建议下一步：

```text
P39 Event Payload / Diff Coverage Preview
```

理由：

- 在设计 event compaction 之前，项目需要先知道哪些 state transitions 有足够 payload/diff detail 可以被安全保留；
- 这一步仍应保持 report-only，不删除、总结或重写 events；
- 它会为未来 retention policy 打地基，同时守住 append-only ledger 边界。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P39 Event Payload / Diff Coverage Preview

目标：在任何 retention 或 compaction 设计声称“安全”之前，先让 event 的 object-payload 和 object-diff 覆盖率可见。

状态：已实现第一版本地实现。

已实现结果：

- `event-payload-diff-report` CLI 可以在不修改 state 的情况下 preview event payload/diff coverage；
- `StateStore.event_payload_diff_coverage_preview` 会包装 replay status、projection mode 和 read-only state checks；
- `build_event_payload_diff_coverage` 会把 events 分类为 `reference_only`、`payload_hint_only`、`diff_ready` 或 `missing_transition_reference`；
- report metrics 包含 transition reference count、payload hint count、payload gap count、diff ready count、diff gap count、high-risk count 和 rollback snapshot count；
- target-path 和 workflow summaries 会显示 payload/diff gaps 集中在哪里；
- scenario evaluation 会验证 report 是 read-only、正常 replay 场景中的 transition references 完整、diff gaps 可见、full object rebuild 仍未 ready，并且 destructive compaction 仍被阻止；
- tests 覆盖 read-only preview 行为和 malformed-event high-risk detection。

剩余缺口：

- 大多数 state transitions 的 events 仍不保存完整 object payload；
- events 仍不保存 explicit object diffs；
- rollback snapshots 仍是 metadata-only；
- 仍不存在 destructive event compaction、summarization、deletion 或 rewrite。

建议下一步：

```text
P40 Event Payload Capture Policy Proposal
```

理由：

- P39 显示 transition references 大体足够，但 object payload/diff coverage 还不够；
- 在真正实现 payload capture 之前，项目应该先定义一个 review-only capture policy proposal，说明哪些 target paths 需要 full payload、diff、snapshot 或只需 reference-only；
- 这能让下一步继续停留在 governance/report 层，避免过早改动 append-only event schema。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

P39 后的资料校准：

- Martin Fowler 的 Event Sourcing pattern 强化了一个工程要求：状态变化应被记录为 durable event objects，并支持未来重建过去状态：https://www.martinfowler.com/eaaDev/EventSourcing.html
- W3C PROV-DM 给项目提供了 provenance 词汇：entities、activities、agents、usage、generation 和 derivation：https://www.w3.org/TR/prov-dm/
- Tulving 对 episodic memory 的框架把记忆与 self、subjective time 和 autonoetic continuity 联系起来；对 01 Core 来说，这支持“记忆不是脱离状态的文本检索”：https://www.annualreviews.org/doi/10.1146/annurev.psych.53.100901.135114
- Hassabis 与 Maguire 的 episodic memory construction account 支持一个判断：未来 continuity 需要结构化 reconstruction material，而不只是扁平 event reference：https://www.sciencedirect.com/science/article/abs/pii/S1364661307001258

对 P40 的含义：先按 target path 定义 review-only payload capture policy，明确 reference-only event、object payload hint、object diff、snapshot link 和 PROV-style provenance fields 的要求，再考虑任何 schema-level payload capture 或 compaction 机制。

### P40 Event Payload Capture Policy Proposal

目标：把 P39 暴露出的 payload/diff coverage gaps 转成 durable、review-only、按 target path 组织的 capture policy proposal，在任何 event schema mutation 或 payload capture 机制出现之前先建立治理层。

状态：已实现第一版本地实现。

已实现结果：

- `propose-event-payload-capture-policy` CLI 会基于当前 payload/diff coverage report 创建 `task_hub.event_payload_capture_policy_proposals`；
- `review-event-payload-capture-policy` CLI 会把 approve、reject、archive 或 quarantine decisions 记录到 `task_hub.event_payload_capture_policy_decisions`；
- 每个 proposal 会记录 target-path requirements，`capture_mode` 可以是 `full_payload_and_diff`、`payload_hint_required`、`snapshot_link_required` 或 `reference_only_ok`；
- proposals 和 decisions 明确保持 `proposal_mode: "proposal_only"`、`requires_review: true`、`execution_prohibited: true`、`executable_policy: false` 和 `executable_policy_created: false`；
- proposals 和 decisions 同时锁死 `event_schema_mutation_allowed`、`event_payload_capture_executed`、`event_compaction_executed`、`events_modified` 和 `safe_for_destructive_compaction`；
- active 和 approved capture policy proposals 会进入 context package，让后续工程循环能看到已审查的 target-path guidance；
- validation 会拒绝 executable、schema-mutating、payload-capturing、compaction-executing、event-modifying 或 destructive-compaction-safe records；
- scenario evaluation 会检查 proposal 创建、approval、context exposure、replay consistency，以及 schema mutation / execution / compaction / event modification count 全部为 0；
- 空 event log 也会生成合法的 `reference_only_ok` guidance record，而不是生成一条无法通过 validation 的 proposal。

剩余缺口：

- event log 仍然只存 transition references，不存 full object payloads；
- 还没有用于 payload capture 的 event schema migration；
- 还没有 executable policy layer，并且在 review lifecycle 更稳之前不应该引入；
- approved capture guidance 还没有和 retention review lifecycle decisions 建立关系；
- 本地 JSON state writes 目前仍然只适合串行 local operation；在 file lock 或 transactional store layer 存在之前，并发 CLI 写入可能造成 replay 或 validation mismatch。

已实现的下一步：

```text
P41 Event Replayability Assessment
```

理由：

- P40 之后的目标已经从增加 governance lifecycle features，调整为证明 state continuity 是否能由 events 承载；
- P39/P40 已经暴露 payload 和 diff gaps，但项目还需要一个直接的 replayability assessment 来说明哪些 reconstruction level 已经 ready；
- 这能让项目继续停留在 Event-Sourcing Groundwork，避免过早进入 executor、automatic rollback、destructive compaction、platform integration 或 event rewrite。

已实现结果：

- `event-replayability-assessment` CLI 会输出 `event_replayability_assessment_v0.1`；
- report 会组合 replay projection validation 和 payload/diff coverage；
- 它会拆开 deterministic replay readiness、transition projection readiness、object reconstruction readiness 和 full state reconstruction readiness；
- 它会报告缺失能力，例如 `object_payload`、`object_diff`、`rollback_snapshot` 和 seed/pre-event coverage gaps；
- 它保持 `reconstruction_executed: false`、`event_payload_capture_executed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`event_schema_mutation_allowed: false`、`report_only: true` 和 `would_modify_state: false`；
- scenario evaluation 会验证 deterministic replay 已经 ready，但因为 payload/diff evidence 不完整，object/full-state reconstruction 仍然 not ready。

剩余缺口：

- 还没有 object payload 或 object diff capture 的 event schema migration；
- replay 仍然不能从 empty seed 重建 object state；
- approved capture guidance 仍然缺少单独的 lifecycle path；
- 本地 JSON state writes 在 file lock 或 transactional store 出现前，仍然只适合串行操作。

已实现的下一步：

```text
P42 Reconstruction Evidence Schema Research
```

理由：

- P41 现在能说明缺什么，但项目还需要设计 object payload、object diff、transition payload 和 reconstruction metadata 的最小证据 schema；
- 在任何 event schema mutation 或 payload capture 实现之前，这一步仍应保持 research/report-only；
- 它直接服务 Priority A 和 Priority B，不增加聊天、平台或 companion 外层能力。

已实现结果：

- `reconstruction-evidence-schema-report` CLI 会输出 `reconstruction_evidence_schema_report_v0.1`；
- report 会定义四个 draft evidence sections：`event_envelope`、`transition_payload`、`object_evidence` 和 `reconstruction_metadata`；
- 它会把 P41 missing capabilities 映射到最小字段，例如 `object_payload`、`object_diff`、`rollback_snapshot_id`、`seed_state_ref` 和 validation metadata；
- 它会报告 deterministic replay、transition projection、object reconstruction 和 full-state reconstruction 的 readiness gates；
- 它保持 `reconstruction_executed: false`、`event_payload_capture_executed: false`、`event_schema_mutation_allowed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`report_only: true` 和 `would_modify_state: false`；
- scenario evaluation 会验证 schema report 存在、保持 read-only、暴露 target-path requirements，并且不会执行 capture、schema mutation 或 reconstruction。

剩余缺口：

- 这个 schema 仍然只是 draft report，不是 event schema migration；
- event families 还没有映射到新的 schema sections；
- replay 仍然不能从 empty seed 重建 object state；
- 还没有 payload 或 diff capture implementation。

已实现的下一步：

```text
P43 Evidence Schema Coverage Mapping
```

理由：

- P42 定义了 evidence vocabulary，但项目还需要一个 read-only mapping，把当前 event families/workflows 映射到 required schema sections；
- 这一步应该在任何 schema mutation 之前，说明哪些 workflow families 需要 object payload、object diff、snapshot link 或 seed/pre-event references；
- 它继续服务 Priority A/B 地基，不实现 capture、reconstruction、compaction、rollback 或 adapters。

已实现结果：

- `reconstruction-evidence-coverage-map` CLI 会输出 `reconstruction_evidence_coverage_mapping_v0.1`；
- report 会把当前 event workflows 映射到 required P42 schema sections 和 minimum fields；
- 它会暴露 workflow-level payload gaps、diff gaps、snapshot gaps、transition gaps、target paths 和 example event IDs；
- 它会汇总 section coverage，让项目看到哪些 schema sections 被当前 events 需要；
- 它保持 `event_schema_mutation_allowed: false`、`event_payload_capture_executed: false`、`reconstruction_executed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`report_only: true` 和 `would_modify_state: false`；
- scenario evaluation 会验证 workflow mapping 存在、gap visibility 非零、state 保持不变，并且不会执行 capture、schema mutation 或 reconstruction。

剩余缺口：

- workflow gaps 已经被映射，但还没有按 reconstruction value、risk 和 expected implementation cost 排序；
- 还没有 event schema migration；
- 还没有 payload 或 diff capture implementation；
- replay 仍然不能从 empty seed 重建 object state。

已实现的下一步：

```text
P44 Evidence Gap Prioritization Report
```

理由：

- P43 已经映射哪些 workflows 有 evidence gaps，但项目还需要一个 read-only 方法，按 reconstruction value、risk 和 expected implementation cost 给这些 gaps 排序；
- 这能帮助决定哪些 event families 最值得先做 schema work，但不执行 schema mutation 或 payload capture；
- 它仍然停留在 Event-Sourcing Groundwork，不进入 executor、rollback、compaction、adapters 或 product surfaces。

已实现结果：

- `reconstruction-evidence-gap-priorities` CLI 会输出 `reconstruction_evidence_gap_prioritization_v0.1`；
- 每个 workflow gap 会获得 review-only scoring：`reconstruction_value`、`preservation_risk`、`implementation_cost`、`priority_score` 和 `recommended_priority`；
- prioritized workflows 会按 priority score 排序，并获得 `recommended_order`；
- report 保持 `event_schema_mutation_allowed: false`、`event_payload_capture_executed: false`、`reconstruction_executed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`report_only: true` 和 `would_modify_state: false`；
- scenario evaluation 会验证分数有界、priority 可见、read-only、不执行 payload capture、不修改 schema、也不执行 reconstruction。

剩余缺口：

- 还没有 schema approval workflow；
- 还没有 event schema migration；
- 还没有 payload 或 diff capture implementation。

已实现的下一步：

```text
P45 Reconstruction Evidence Schema Review Checklist
```

理由：

- P44 已经给 gaps 排序，但项目还需要一个 review-only checklist，把 top-ranked workflow gaps 转成明确 review questions、acceptance criteria 和 required evidence，之后才考虑任何 schema work；
- 这让治理先于实现，避免 automatic schema mutation、payload capture、reconstruction execution、rollback、compaction 或 adapters；
- 它把 Priority A/B research 接到 Priority C governance，但不变成 product surface。

已实现结果：

- `reconstruction-evidence-schema-review-checklist` CLI 会输出 `reconstruction_evidence_schema_review_checklist_v0.1`；
- 每个 prioritized workflow 会变成 review-only checklist item，包含 review questions、acceptance criteria、required evidence、allowed review decisions 和明确 non-execution flags；
- checklist items 会保留 P44 的 `recommended_order`、`recommended_priority`、target paths、missing capabilities、minimum fields 和 example event IDs；
- report 保持 `event_schema_mutation_allowed: false`、`event_payload_capture_executed: false`、`reconstruction_executed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`identity_mutation_allowed: false`、`report_only: true` 和 `would_modify_state: false`；
- scenario evaluation 会验证 checklist material 存在、保持 read-only，并且不执行 schema mutation、payload capture、reconstruction、identity mutation、rollback 或 compaction。

剩余缺口：

- 还没有 schema approval workflow；
- 还没有 event schema migration；
- 还没有 payload 或 diff capture implementation。

已实现的下一步：

```text
P46 Reconstruction Schema Checklist Review Record
```

理由：

- P45 准备了 review material，但项目仍然需要一个 durable、non-executable record 来记录人类对每个 checklist item 的决定；
- 这一步应该记录 reviewer、decision、rationale、requested evidence 和 approval scope，但不执行 schema mutation 或 payload capture；
- 它让项目继续停留在 Event-Sourcing Groundwork，同时把 review checklist 接到未来 schema design。

已实现结果：

- `review-reconstruction-schema-checklist-item` CLI 会在 `task_hub.reconstruction_schema_review_decisions` 下记录 durable `reconstruction_schema_review_decision` objects；
- 每个 decision 会捕获 checklist id、workflow、reviewer、action、result、rationale、requested evidence、approval scope、source evidence、review questions、acceptance criteria、required evidence、snapshot metadata、audit trace 和 event-log projection support；
- decisions 会通过 `task_hub.reconstruction_schema_review_decisions` 进入 append-only event log；
- decision 保持 `schema_change_approved: false`、`schema_change_allowed: false`、`event_schema_mutation_allowed: false`、`event_payload_capture_executed: false`、`reconstruction_executed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`identity_mutation_allowed: false` 和 `events_modified: false`；
- scenario evaluation 会验证 durable decision count、context governance signal visibility、replay-after-review、projection consistency，以及所有 execution/mutation counts 为 0。

剩余缺口：

- review decisions 还没有按 workflow 映射回 coverage report；
- 还没有 schema approval workflow；
- 还没有 event schema migration；
- 还没有 payload 或 diff capture implementation。

已实现的下一步：

```text
P47 Reconstruction Schema Review Coverage Map
```

理由：

- P46 记录了 individual decisions，但项目仍然需要一个 report-only map，显示哪些 prioritized workflow gaps 已有 review decisions，哪些仍未 review；
- 这一步应该暴露 reviewed、deferred、rejected 和 evidence-requested checklist items，但不批准 schema changes；
- 它让 Event-Sourcing Groundwork 在任何 schema mutation 或 payload capture 之前先聚焦 governance coverage。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

已实现结果：

- `reconstruction-schema-review-coverage-map` CLI 会输出 `reconstruction_schema_review_coverage_map_v0.1`；
- report 会把 P46 的 `task_hub.reconstruction_schema_review_decisions` 映射回 P45 checklist workflow items；
- coverage records 会暴露 reviewed、unreviewed、evidence-requested、deferred、rejected、quarantined 和 reviewed-for-schema-design 状态；
- report 会保留 checklist priority、target paths、missing capabilities、latest decision metadata、requested evidence 和 approval scope；
- report 保持 `schema_change_approved: false`、`schema_change_allowed: false`、`event_schema_mutation_allowed: false`、`event_payload_capture_executed: false`、`reconstruction_executed: false`、`event_compaction_executed: false`、`automatic_rollback_executed: false`、`identity_mutation_allowed: false`、`report_only: true` 和 `would_modify_state: false`；
- scenario evaluation 会验证 review coverage visibility、unreviewed gap visibility、read-only 行为，以及 schema mutation / payload capture / reconstruction / identity mutation counts 全部为 0。

剩余缺口：

- requested evidence 已经可见，但还没有 dedicated evidence request lifecycle；
- 还没有 schema approval workflow；
- 还没有 event schema migration；
- 还没有 payload 或 diff capture implementation。

建议下一步：

```text
P48 Reconstruction Schema Review Evidence Request Tracker
```

理由：

- P47 可以显示某个 checklist item 请求了更多 evidence，但 evidence request 本身还没有 durable lifecycle；
- 下一个地基步骤应把 requested evidence 变成 review-only records，支持 open、satisfy、defer、archive 或 quarantine，但不批准 schema changes；
- 这能让 Event-Sourcing Groundwork 在任何 payload capture、reconstruction execution、event compaction、automatic rollback 或 schema migration 之前继续聚焦 governance evidence。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P33 Context Attribution Coverage Review Lifecycle

目标：让 durable attribution coverage review records 可以通过可审计 lifecycle path 被 acknowledge、archive 或 quarantine。

状态：已实现第一版本地实现。

已实现结果：

- `context-attribution-coverage-lifecycle` CLI 可以 acknowledge、archive 或 quarantine coverage review records；
- `StateStore.apply_context_attribution_coverage_lifecycle_action` 会写入 snapshot、audit、trace、update log、lifecycle history、update history 和 `context_builder.attribution_coverage_lifecycle_decisions`；
- context package 只暴露 active 或 acknowledged coverage reviews，所以 archived / quarantined reviews 会从 active state transfer 中被压制；
- lifecycle decisions 保持 `review_only: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`；
- validation 会拒绝 executable 或 identity-mutating coverage review lifecycle records；
- scenario evaluation 会验证 lifecycle decision creation、archived-review context suppression、non-execution，以及不会修改 Identity Core。

剩余缺口：

- scenario baselines 已经运行 deterministic local rule comparisons，但还没有独立 baseline agents；
- replay 现在已有 target-path transition projection，但还不是完整 object-level state rebuild；
- 还没有 executable policy layer，当前也不应该引入。

建议下一步：

```text
P34 Evaluation Baseline Execution
```

理由：

- 项目大纲仍然要求和 stateless、retrieval-only、summary-only baseline 做真实比较；
- P7-P33 已经提供足够本地地基，可以在不扩大平台范围的情况下比较 continuity 行为；
- baseline execution 会增强研究命题，同时保持 local core 和 non-platform-specific 的方向。

期望验收：

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```
