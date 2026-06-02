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
  next_questions:
    - "What is the smallest runnable 01 prototype?"
```

## 12. Failure Modes

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

## 13. MVP Dream Engine

第一版 Dream Engine 可以很简单：

1. 读取最近 episode logs；
2. 总结每个 episode；
3. 提取 candidate facts、preferences、conflicts 和 project updates；
4. 与现有 memories 对比；
5. 写 proposal，而不是直接更新；
6. identity change 需要人工批准。

这已经足够测试 dream-like consolidation 是否能改善跨 session 连续性。
