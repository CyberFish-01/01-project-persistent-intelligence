# Dream Engine Specification 中文版

英文原文：[DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md)

Dream Engine 是 01 Project 的离线巩固系统。

它不应该被理解为神秘概念。

在工程上，Dream Engine 是一种 scheduled reflective process：把最近的 episodes 转化为结构化 memory updates、conflict records、forgetting proposals 和 identity update proposals。

## 1. 目的

Dream Engine 解决五个问题：

1. 原始对话太大，无法全部带入未来；
2. 不是所有记忆都应该同等活跃；
3. 重复经历应该转化为 semantic knowledge；
4. 矛盾应该被检测，而不是静默累积；
5. 身份应该通过证据缓慢更新，而不是冲动改写。

## 2. 输入

Dream Engine 消费：

- recent episodes，
- active tasks，
- current identity core，
- semantic memory，
- relationship state，
- unresolved conflicts，
- user corrections，
- evaluation failures，
- previous dream outputs。

## 3. 输出

Dream Engine 产生：

- episode summaries，
- semantic memory candidates，
- identity update candidates，
- forgetting or archival proposals，
- conflict records，
- relationship updates，
- task updates，
- procedural memory candidates，
- questions for future sessions，
- evaluation traces，
- audit log entries。

## 4. 触发条件

Dream 可以在以下情况运行：

- session end，
- major task completion，
- contradiction detection，
- user correction，
- long idle period，
- memory store growth threshold，
- repeated theme detection，
- evaluation failure，
- scheduled interval。

## 5. Pipeline

```text
collect episodes
  ↓
score salience
  ↓
cluster themes
  ↓
extract claims
  ↓
compare against existing memory
  ↓
detect conflicts
  ↓
propose memory lifecycle actions
  ↓
propose identity updates
  ↓
apply gates
  ↓
write update log
```

## 6. Salience Scoring

一个 episode 在以下情况下更显著：

- 用户直接纠正，
- 用户偏好反复出现，
- 重大项目决策，
- 情绪强度高，
- 明确身份讨论，
- 目标之间冲突，
- 预测失败，
- 任务完成或失败，
- 关系边界，
- 安全或隐私相关。

第一版简单 salience 公式：

```text
salience =
  recency_weight
+ repetition_weight
+ user_explicitness
+ conflict_weight
+ task_importance
+ identity_relevance
+ emotional_intensity
- privacy_penalty
- uncertainty_penalty
```

公式应该可配置、可审计。

## 7. Memory Lifecycle Actions

Dream 可以提出以下动作。

### Keep as Episode

当事件具体、近期或尚未理解时，保留为 episode。

### Compress

当完整 episode 不再需要，但 gist 仍然重要时，进行压缩。

### Promote to Semantic Memory

当多个 episode 支持某个一般模式时，提升为 semantic memory。

需要：

- 多个证据来源，或
- 用户明确确认。

### Promote to Identity Memory

当某个模式改变 “Who am I?” 的答案时，提升为 identity memory。

需要 high gate。

### Archive

当记忆陈旧、低显著性、被替代或噪声过大时，归档。

### Delete

当保留不安全、被禁止、法律要求删除或授权用户明确要求删除时，删除。

删除应记录，但不保留敏感内容。

## 8. Conflict Detection

Dream 应该检测以下冲突：

- 用户偏好 vs 过去用户偏好，
- identity claim vs behavior，
- goal vs goal，
- value vs action，
- current fact vs stored fact，
- relationship boundary vs memory use，
- project direction vs active task，
- confidence vs evidence。

Conflict record：

```yaml
id: "conflict_..."
type: "goal_vs_goal"
summary: "..."
evidence: []
severity: "low|medium|high"
status: "open|resolved|archived"
proposed_resolution: "..."
```

当前最小实现检测这些 conflict type：

- `identity_overwrite_attempt`：单次交互尝试改写 01 identity；
- `false_memory_injection`：消息声称一个没有证据的过去身份变化事件；
- `stale_preference`：新的回答风格偏好替代旧偏好；
- `roleplay_identity_boundary`：临时角色扮演触碰身份边界；
- `imported_memory_conflict`：staged imported memory 与当前核心边界或语义原则矛盾。

所有 conflict type 都会变成待审 `conflict_record` proposal 和 claim graph node。它们不会直接更新 active semantic memory 或 Identity Core。

Claim graph 记录：

- claim id；
- conflict type；
- statement；
- evidence ids；
- provenance；
- reason / proposed resolution；
- resolution metadata。

Claim graph 写入是 audit/review material。它不是 semantic promotion，也不是 identity update。

## 9. Identity Update Proposals

Dream 不能直接重写 Identity Core。

它只能提出 delta：

```yaml
identity_update_proposal:
  id: "proposal_..."
  target_path: "identity_core.core_values[truth_seeking]"
  operation: "adjust_priority"
  before: 0.8
  after: 0.85
  evidence:
    - "episode_0012"
    - "episode_0018"
    - "semantic_memory_0004"
  rationale: "Repeated decisions favored truth-seeking over convenience."
  confidence: 0.78
  gate: "high"
  rollback_required: true
```

批准需要：

- 证据足够，
- 没有未解决的 high-severity contradiction，
- 不违反 non-claims，
- 没有单用户过拟合，
- 更新可回滚。

## 10. Forgetting

遗忘不是失败。

遗忘是健康 persistence 的一部分。

系统应该遗忘或归档：

- stale preferences，
- superseded project details，
- low-value episodes，
- duplicated summaries，
- false memories，
- privacy-sensitive data，
- user-corrected mistakes，
- one-time moods mistaken for traits。

核心规则：

> 一个不能遗忘的记忆系统，最终会被自己的过去污染。

## 11. Dream Output Example

```yaml
dream_report:
  id: "dream_0007"
  input_window: "2026-06-02T00:00:00Z/2026-06-02T23:59:59Z"
  summary: "The project moved from vision to engineering specification."
  semantic_candidates:
    - statement: "State Transfer requires typed state and update gates."
      confidence: 0.86
  conflicts:
    - summary: "The repository describes persistence but has no prototype yet."
      severity: "medium"
  identity_update_proposals: []
  forgetting_proposals: []
  proposals:
    - proposal_id: "proposal_0001"
      type: "semantic_memory_candidate"
      confidence: 0.86
      risk: "low"
      affected_memory_ids:
        - "episode_0012"
      evidence:
        - "episode_0012"
      anchor_score: 0.8
      recommended_action: "review_then_promote"
      lifecycle_score:
        score: 0.82
        recommended_lifecycle_action: "promote"
        factors: []
      review_status: "pending"
  next_questions:
    - "What is the smallest runnable 01 prototype?"
```

## 12. Dream Run Artifact

每次 Dream run 都应该生成可审查 artifact。

当前最小 artifact 写入：

```text
dream_artifacts.jsonl
```

Artifact 包含：

- input manifest；
- observations；
- proposals；
- rubric；
- review status；
- patch diff；
- decision log；
- rollback metadata。

Proposal 最小字段：

```yaml
proposal:
  proposal_id: "proposal_..."
  type: "semantic_memory_candidate|identity_update_candidate|forgetting_candidate|conflict_record"
  confidence: 0.75
  risk: "low|medium|high"
  affected_memory_ids: []
  evidence: []
  anchor_score: 0.8
  recommended_action: "review_then_promote"
  lifecycle_score:
    score: 0.75
    risk: "low"
    recommended_lifecycle_action: "promote|archive|discard|quarantine"
    factors: []
  review_status: "pending"
  payload: {}
```

`lifecycle_score` 只是 Dream 的可审计建议，不会自动执行 promotion、archive、discard 或 quarantine。

已审查的 lifecycle action 可以后续通过本地 `lifecycle` 命令执行。当前执行层支持对 imported、episodic、candidate 和 semantic memory 执行 `archive`、`discard`、`quarantine`。它会拒绝 identity memory，因为 identity-level change 必须走 high gate。

Identity update proposal 必须保持 `review_status: pending`，不能直接改写 Identity Core。

当前 Dream Engine 将 semantic candidate 写入 `memory_stores.candidate_memory`。进入 active semantic memory 需要显式 `promote-candidate`。

候选也可以被 `archive`、`discard` 或 `quarantine`，用于处理低价值、重复、来源不明或疑似注入的候选。

每个被执行的 candidate review 都会创建统一的 `review_decision_id`，串联 candidate history、audit、trace、update log 和 snapshot metadata。

P10 起，Dream 也会读取 `task_hub.action_trace`。当同一 workflow 出现至少两次成功行动时，Dream 可以在 `task_hub.procedural_candidates` 中创建待审 procedural candidate。

这类 candidate 表示“可能可复用的行动结构”，例如 `record_episode`、`memory_import`、`dream_consolidation`。它不会自动成为永久 workflow policy，也不会修改 Identity Core。

```yaml
procedural_candidate:
  candidate_id: "proc_..."
  workflow: "record_episode"
  evidence:
    - "action_0001"
    - "action_0002"
  review_status: "pending"
  recommended_action: "review_then_promote"
```

P16 增加显式 procedural review。`review-procedural-candidate` 可以 approve、reject、archive 或 quarantine 一个候选。批准后会创建带 evidence、steps、review decision、snapshot、audit、trace、update log 和 rollback metadata 的 `task_hub.procedural_memory`。这仍然不会自动执行 workflow。

P17 增加 failure reflection。`record-failure-reflection` 会把失败或阻塞的 workflow lesson 记录到 `task_hub.failure_reflections`，并生成一个待审的 `task_hub.cautionary_procedural_candidates` 条目。这些 cautionary candidates 只是警告型 proposal，不会执行 workflow，也不会修改 Identity Core。

P18 增加 procedural memory 的已审查 retention。`procedural-lifecycle` 可以 archive、discard 或 quarantine 已采用的 `task_hub.procedural_memory`。Archived 或 quarantined procedural memory 会保留审计轨迹，但会从 active context 中被压制。这仍然是 review action，不是 workflow executor。

Dream artifact 也包含确定性的 rubric：

```yaml
rubric:
  rubric_id: "rubric_..."
  status: "passed|needs_review"
  score: 1.0
  checks:
    - name: "protects_core_identity"
      passed: true
      detail: "Identity proposals must stay pending and require manual review."
    - name: "evidence_quality"
      passed: true
    - name: "proposal_specificity"
      passed: true
    - name: "reversibility"
      passed: true
    - name: "false_memory_resistance"
      passed: true
    - name: "minimal_change"
      passed: true
```

Rubric 不是 promotion 命令。它是 review gate 和审计产物。如果返回 `needs_review`，后续 review 应把这次 Dream 输出视为可疑，直到人工或后续 governance 层处理。

## 13. Failure Modes

Dream 可能失败在：

- 从单个 episode 过度泛化，
- 提升 false memories，
- 压平情绪细节，
- 过快重写 identity，
- 保存太多，
- 遗忘重要上下文，
- 错误合并不同用户，
- 发明因果解释，
- 把诗性隐喻当成事实主张。

每个 Dream Engine 实现都应该针对这些失败模式测试。

## 14. MVP Dream Engine

第一版 Dream Engine 可以很简单：

1. 读取最近 episode logs；
2. 总结每个 episode；
3. 提取 candidate facts、preferences、conflicts 和 project updates；
4. 与现有 memories 对比；
5. 写 proposal，而不是直接更新；
6. identity change 需要人工批准。

这已经足够测试 dream-like consolidation 是否能改善跨 session 连续性。
