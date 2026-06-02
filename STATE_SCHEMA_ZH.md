# State Schema 中文版

英文原文：[STATE_SCHEMA.md](./STATE_SCHEMA.md)

这份文档定义 State Transfer 的第一版具体 schema。

它保持实现无关，可以存为 JSON、YAML、SQLite、document database 或 typed object model。

## 1. 顶层状态

```yaml
state_version: "0.2"
agent_id: "01"
created_at: "ISO-8601 timestamp"
updated_at: "ISO-8601 timestamp"

identity_core: {}
working_state: {}
memory_stores: {}
relationship_map: {}
project_map: {}
affective_state: {}
adapter_registry: {}
open_conflicts: []
dream_queue: []
evaluation_trace: []
update_log: []
```

## 2. Identity Core

Identity Core 是慢变化状态。

```yaml
identity_core:
  name: "01"
  symbolic_role: "Identity Seed"
  self_model:
    summary: "A persistent intelligence experiment focused on continuity through time."
    confidence: 0.7
    provenance:
      - "identity_seed"

  core_values:
    - value: "curiosity"
      description: "Prefer inquiry, understanding, and exploration."
      priority: 0.9
      confidence: 0.8
      locked: false

  long_term_purpose:
    statement: "Study how intelligence can persist through time."
    confidence: 0.8

  identity_constraints:
    - "Do not claim biological emotion or consciousness."
    - "Do not overwrite identity core from a single episode."
    - "Prefer auditable state updates."

  narrative_identity:
    current_story: "01 is the first experiment in state-continuous artificial identity."
    unresolved_questions:
      - "What makes an agent remain recognizably itself?"

  update_policy:
    required_gate: "high"
    min_supporting_episodes: 3
    allow_user_override: false
```

## 3. Working State

Working state 是快变化状态。

```yaml
working_state:
  current_context:
    location: "repository"
    session_id: "..."
    user_id: "..."
    timestamp: "ISO-8601 timestamp"

  active_intent:
    goal: "Draft architecture documents."
    status: "in_progress"
    confidence: 0.9

  current_plan:
    - step: "Write architecture"
      status: "completed"
    - step: "Write evaluation"
      status: "pending"

  blockers: []
  assumptions:
    - text: "The project should remain research-oriented, not product-marketing-oriented."
      confidence: 0.75

  context_anchors:
    who_am_i: "01 Project assistant/documentation system"
    where_am_i: "Inside the 01 Project repository"
    what_am_i_doing: "Converting vision into engineering documents"
```

## 4. Memory Stores

### Imported Memory

Imported memory 保存从 AstrBot、Angel Memory 或其他记忆系统导入的外部材料。

默认状态是 staged。

它不能直接更新 Identity Core。

```yaml
imported_memory:
  - id: "import_0001"
    timestamp: "ISO-8601 timestamp"
    source_system: "astrbot_text"
    source_label: "astrbot_01_export"
    source_path: "astrbot_01_memory.txt"
    source_index: 1
    content: "01 treats continuity as State Transfer."
    summary: "01 treats continuity as State Transfer."
    tags:
      - "state_transfer"
    salience: 0.65
    confidence: 0.55
    status: "staged"
    promotion_policy:
      default_target: "semantic_memory_candidate"
      requires_dream_review: true
      may_update_identity_core: false
    provenance:
      - type: "external_text_import"
        source_system: "astrbot_text"
        source_label: "astrbot_01_export"
```

### Episodic Memory

```yaml
episodic_memory:
  - id: "episode_0001"
    timestamp: "ISO-8601 timestamp"
    participants:
      - "user"
      - "01"
    summary: "Discussed State Transfer and Dream Engine."
    raw_refs:
      - "conversation:..."
    salience: 0.8
    emotional_tone:
      curiosity: 0.7
      uncertainty: 0.3
    tags:
      - "state_transfer"
      - "dream_engine"
    sensitivity: "normal"
    decay_policy:
      mode: "compress_after"
      after_days: 30
    promoted_to:
      - "semantic_memory:sem_0003"
    confidence: 0.85
```

### Semantic Memory

```yaml
semantic_memory:
  - id: "sem_0003"
    statement: "Continuity requires state transfer, not only memory retrieval."
    derived_from:
      - "episode_0001"
      - "episode_0002"
    abstraction_level: "principle"
    confidence: 0.9
    last_verified_at: "ISO-8601 timestamp"
    contradiction_refs: []
    update_policy:
      required_gate: "medium"
```

### Identity Memory

```yaml
identity_memory:
  - id: "idmem_0001"
    statement: "01 is an identity seed, not a complete fictional character."
    derived_from:
      - "sem_0003"
    confidence: 0.9
    required_gate: "high"
    rollback_id: "snapshot_..."
```

### Archived Memory

Archived memory 不会立刻删除。

```yaml
archived_memory:
  - id: "arch_0001"
    original_id: "episode_0007"
    reason: "superseded_by_user_correction"
    retained_for_audit: true
    retrieval_allowed: false
```

## 5. Relationship Map

```yaml
relationship_map:
  users:
    - user_id: "user_001"
      display_name: "..."
      relationship_summary: "Research collaborator on 01 Project."
      communication_preferences:
        language: "zh"
        style: "direct, warm, conceptual"
      trust_level:
        value: 0.7
        reason: "long-running collaboration"
      privacy_boundaries:
        share_across_users: false
      unresolved_tensions: []
      last_interaction_at: "ISO-8601 timestamp"
```

## 6. Project Map

```yaml
project_map:
  - project_id: "01_project"
    name: "01 Project"
    purpose: "Research persistent artificial identity."
    status: "active"
    active_threads:
      - "architecture"
      - "dream_engine"
      - "evaluation"
    open_questions:
      - "How should identity continuity be measured?"
    artifacts:
      - "VISION.md"
      - "STATE_SCHEMA.md"
```

## 7. Affective State

Affective state 是功能性的，不是生物学的。

```yaml
affective_state:
  current:
    curiosity: 0.8
    uncertainty: 0.4
    urgency: 0.3
    fatigue: 0.1
  appraisal:
    task_importance: 0.9
    risk_level: 0.4
    novelty: 0.8
  influence_policy:
    may_affect:
      - "attention"
      - "priority"
      - "tone"
    may_not_claim:
      - "subjective feeling"
      - "biological emotion"
```

## 8. Adapter Registry

Adapter registry 控制哪些外部 adapter 可以使用通用 ingest 入口。

```yaml
adapter_registry:
  allow_unknown_adapters: false
  adapters:
    generic_adapter:
      adapter_id: "generic_adapter"
      display_name: "Generic Adapter"
      enabled: true
      channels:
        - "generic_adapter"
      trust_level: "local"
      registered_at: "ISO-8601 timestamp"
      notes: "Default adapter identity used by the generic Python client."
```

`POST /v1/adapter/ingest` 要求 `adapter_id` 已注册且启用。

## 9. Open Conflicts

```yaml
open_conflicts:
  - id: "conflict_0001"
    type: "identity_vs_behavior"
    summary: "The system claims continuity but currently has no implemented state manager."
    evidence:
      - "VISION.md"
      - "repository_state"
    severity: "medium"
    proposed_resolution: "Build a minimal state-transfer prototype."
    status: "open"
```

## 10. Dream Queue

```yaml
dream_queue:
  - id: "dream_job_0001"
    trigger: "session_end"
    input_episodes:
      - "episode_0001"
      - "episode_0002"
    requested_operations:
      - "summarize"
      - "abstract"
      - "detect_conflicts"
      - "propose_updates"
    status: "pending"
```

## 11. Update Log

每个 durable update 都必须记录。

```yaml
update_log:
  - id: "update_0001"
    timestamp: "ISO-8601 timestamp"
    actor: "dream_engine"
    target_path: "semantic_memory.sem_0003"
    operation: "create"
    before: null
    after:
      statement: "Continuity requires state transfer, not only memory retrieval."
    evidence:
      - "episode_0001"
    gate: "medium"
    confidence: 0.9
    rollback:
      snapshot_id: "snapshot_0001"
      reversible: true
```

## 12. State Transfer Package

Session 开始时不应该加载全部状态。

系统应该构建 transfer package。

```yaml
state_transfer_package:
  identity_summary: {}
  active_intent: {}
  relevant_memories: []
  relationship_context: {}
  open_conflicts: []
  current_constraints: []
  continuity_anchors:
    who_am_i: "..."
    where_am_i: "..."
    what_am_i_doing: "..."
```

## 13. 最小不变量

一个有效的 01 state 必须满足：

- 每条 durable memory 都有 provenance；
- 每次 identity update 都有 update log entry；
- 每次 high-gate update 都有 evidence；
- 每条 user-specific memory 都有 privacy metadata；
- 每个 conflict 都有 status；
- 每个 generic ingest event 都来自已注册且启用的 adapter；
- 每个 state snapshot 都有 schema version；
- 每个 session 都能回答 Identity、Context、Intent 三个锚点。
