# State Schema 中文版

英文原文：[STATE_SCHEMA.md](./STATE_SCHEMA.md)

这份文档定义 State Transfer 的第一版具体 schema。

它保持实现无关，可以存为 JSON、YAML、SQLite、document database 或 typed object model。

## 1. 顶层状态

```yaml
state_version: "0.8"
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
session_policy: {}
adapter_event_index: {}
open_conflicts: []
claim_graph:
  claims: []
  links: []
task_hub:
  active_tasks: []
  completed_tasks: []
  blocked_tasks: []
  recurring_duties: []
  action_trace: []
  procedural_candidates: []
dream_queue: []
snapshots: []
audit_log: []
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
    import_batch_id: "import_batch_0001"
    timestamp: "ISO-8601 timestamp"
    source_system: "astrbot_text"
    source_label: "astrbot_01_export"
    source_path: "astrbot_01_memory.txt"
    source_index: 1
    content_hash: "sha256 hex digest"
    dedupe_key: "sha256:..."
    content: "01 treats continuity as State Transfer."
    summary: "01 treats continuity as State Transfer."
    tags:
      - "state_transfer"
    salience: 0.65
    confidence: 0.55
    status: "staged"
    lifecycle:
      status: "staged"
      created_at: "ISO-8601 timestamp"
      last_reviewed_at: null
      review_status: "staged"
    promotion_policy:
      default_target: "semantic_memory_candidate"
      requires_dream_review: true
      may_update_identity_core: false
    provenance:
      - type: "external_text_import"
        source_system: "astrbot_text"
        source_label: "astrbot_01_export"
    update_history:
      - timestamp: "ISO-8601 timestamp"
        actor: "memory_importer"
        operation: "stage_external_memory"
        evidence:
          - "astrbot_01_memory.txt"
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
    lifecycle:
      status: "active"
      created_at: "ISO-8601 timestamp"
      last_reviewed_at: null
      review_status: "unreviewed"
    provenance:
      - type: "episode_recorded"
        source:
          adapter_id: "local_generic_adapter"
          channel: "local"
    update_history:
      - timestamp: "ISO-8601 timestamp"
        actor: "local_generic_adapter"
        operation: "record_episode"
        evidence:
          - "episode_0001"
```

### Candidate Memory

Candidate memory 保存 Dream 产出的候选记忆。

它默认不进入 active semantic memory。

```yaml
candidate_memory:
  - id: "cand_0001"
    timestamp: "ISO-8601 timestamp"
    status: "candidate"
    review_status: "pending"
    promotion_target: "semantic_memory"
    source_dream_id: "dream_0001"
    proposal_id: "proposal_0001"
    statement: "Continuity requires state transfer, not only memory retrieval."
    derived_from:
      - "episode_0001"
      - "episode_0002"
    abstraction_level: "pattern"
    confidence: 0.75
    risk: "low"
    recommended_action: "review_then_promote"
    recommended_lifecycle_action: "promote"
    lifecycle_score:
      score: 0.82
      risk: "low"
      factors: []
      recommended_lifecycle_action: "promote"
    lifecycle:
      status: "candidate"
      created_at: "ISO-8601 timestamp"
      last_reviewed_at: null
      review_status: "pending"
      review_decision_id: null
    provenance:
      - type: "dream_proposal"
        dream_id: "dream_0001"
        proposal_id: "proposal_0001"
    last_review_decision_id: null
    review_history:
      - decision_id: "review_decision_0001"
        timestamp: "ISO-8601 timestamp"
        reviewer: "manual_review"
        action: "promote"
        result: "promoted"
        decision_note: "Reviewed evidence and approved promotion."
        candidate_id: "cand_0001"
        recommended_action: "review_then_promote"
        recommended_lifecycle_action: "promote"
        risk: "low"
        confidence: 0.75
        evidence:
          - "episode_0001"
          - "episode_0002"
        gate: "medium"
        snapshot_id: "snapshot_0001"
        target_path: "memory_stores.semantic_memory"
        after: "sem_0003"
        rollback:
          reversible: true
    update_history:
      - timestamp: "ISO-8601 timestamp"
        actor: "dream_engine"
        operation: "create_candidate"
        evidence:
          - "episode_0001"
          - "episode_0002"
```

进入 active semantic memory 需要显式 review / promote。

候选记忆的 review action：

```text
promote
archive
discard
quarantine
```

`archive` 会复制审计摘要到 `archived_memory`；`discard` 只标记候选已丢弃；`quarantine` 用于来源不明、疑似注入或冲突风险较高的候选。

`recommended_lifecycle_action` 是 Dream 的建议，人工 review 可以采纳或拒绝。

每个已完成的 candidate review 都会在 `review_history` 写入一个 `review_decision`，在 candidate 上保存 `last_review_decision_id`，并让 lifecycle metadata、audit events、traces、update log entries 和 snapshot metadata 指向同一个 decision。

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
    lifecycle:
      status: "active"
      created_at: "ISO-8601 timestamp"
      last_reviewed_at: "ISO-8601 timestamp"
      review_status: "promoted"
    provenance:
      - type: "dream_proposal"
        dream_id: "dream_0001"
        proposal_id: "proposal_0001"
    update_history:
      - timestamp: "ISO-8601 timestamp"
        actor: "manual_review"
        operation: "promote_candidate"
        evidence:
          - "episode_0001"
          - "episode_0002"
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
    lifecycle:
      status: "active"
      created_at: "ISO-8601 timestamp"
      last_reviewed_at: "ISO-8601 timestamp"
      review_status: "approved"
    provenance:
      - type: "identity_seed"
        source: "make_identity_seed"
    update_history:
      - timestamp: "ISO-8601 timestamp"
        actor: "state_store"
        operation: "seed"
        evidence:
          - "identity_seed"
```

### Archived Memory

Archived memory 不会立刻删除。

```yaml
archived_memory:
  - id: "arch_0001"
    timestamp: "ISO-8601 timestamp"
    original_id: "episode_0007"
    original_store: "episodic_memory"
    reason: "superseded_by_user_correction"
    retained_for_audit: true
    retrieval_allowed: false
    summary: "Archived memory summary."
    provenance: []
    lifecycle:
      status: "archived"
      created_at: "ISO-8601 timestamp"
      last_reviewed_at: "ISO-8601 timestamp"
      review_status: "archived"
      source_memory_id: "episode_0007"
      source_store: "episodic_memory"
      lifecycle_decision_id: "lifecycle_decision_0001"
    update_history:
      - timestamp: "ISO-8601 timestamp"
        actor: "manual_review"
        operation: "archive_memory"
        evidence:
          - "episode_0007"
        lifecycle_decision_id: "lifecycle_decision_0001"
```

Durable memory lifecycle actions：

```text
archive
discard
quarantine
```

当前实现支持对 `imported_memory`、`episodic_memory`、`candidate_memory` 和 `semantic_memory` 执行 lifecycle action。

`identity_memory` 会被通用 lifecycle 命令拒绝，必须走单独 high gate。

每个已执行 lifecycle action 都会把 `lifecycle_decision_id` 写入 `lifecycle_history`、lifecycle metadata、audit events、traces、update log entries 和 snapshot metadata。`archive` 还会把审计保留摘要复制到 `archived_memory`。`discard` 和 `quarantine` 只标记原 memory，不删除审计轨迹。

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

## 9. Session Policy

Session policy 控制已注册 adapter 在哪些 channel/session/user 上可以真实写入。

它在 adapter registry 之后执行：

```text
adapter registry -> session policy -> dry-run / write / reject
```

默认策略保守：

- local generic adapter 可以写入；
- AstrBot thin adapter 默认 `dry_run_only`；
- 未匹配规则默认 `dry_run_only`。

```yaml
session_policy:
  default_action: "dry_run_only"
  rules:
    - id: "local_generic_allow"
      adapter_id: "local_generic_adapter"
      channels:
        - "local"
        - "local_generic_adapter"
      action: "allow"
      reason: "Local generic adapter is allowed for protocol verification."
    - id: "astrbot_private_preview"
      adapter_id: "astrbot_thin_adapter"
      channels:
        - "astrbot"
      action: "dry_run_only"
      reason: "AstrBot remains a thin adapter until local protocol policy is stable."
```

合法 action：

```text
allow
dry_run_only
reject
```

`dry_run_only` 会把真实写入请求降级为 dry-run 预览，不写入 episode、dream job 或 adapter event index。

## 10. Adapter Event Index

Adapter event index 用来防止外部事件被重复写入。

```yaml
adapter_event_index:
  local_generic_adapter:
    platform_event_id:
      adapter_id: "local_generic_adapter"
      event_id: "platform_event_id"
      episode_id: "episode_0001"
      recorded_at: "ISO-8601 timestamp"
      channel: "local"
```

只有带 `event_id` 的真实写入会更新这个索引。Dry-run 预览不会更新。

## 11. Open Conflicts

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

## 12. Claim Graph

Claim graph 记录待审 claim、理由、证据和冲突依赖。

它是 append-friendly 结构，不直接修改 active semantic memory 或 Identity Core。

```yaml
claim_graph:
  claims:
    - claim_id: "claim_conflict_0001"
      timestamp: "ISO-8601 timestamp"
      claim_type: "false_memory_injection|stale_preference|identity_overwrite_attempt|imported_memory_conflict|roleplay_identity_boundary"
      statement: "A message asserts an unsupported past identity-changing event."
      status: "open|resolved|archived"
      confidence: 0.8
      risk: "low|medium|high"
      evidence:
        - "episode_0001"
      provenance:
        - type: "conflict_detection"
          source: "dream_engine"
          conflict_id: "conflict_0001"
          dream_id: "dream_0001"
      reason: "Store as an unverified claim and require independent confirmation."
      dependencies:
        - "episode_0001"
      source_conflict_id: "conflict_0001"
      resolution:
        status: "unresolved"
        proposal: "Require review before semantic or identity promotion."
        requires_review: true
        minimal_change: true
        may_update_identity_core: false
        may_update_semantic_memory: false
  links:
    - from: "claim_a"
      to: "claim_b"
      type: "contradicts|supports|supersedes|depends_on"
```

每个 claim 都必须有 evidence、provenance、status 和 resolution metadata。

当前 Dream conflict detection 会同时写入 `open_conflicts` 和对应 claim nodes。Claim graph entry 是 review/audit material；它本身不会执行 resolution action。

## 13. Task Hub

Task Hub 保存任务连续性和行动结构。

它不是平台 todo，也不是 adapter 状态。它是 01 Core 用于回答“我正在推进什么、刚才做了什么、下一步怎么继续”的本地状态层。

```yaml
task_hub:
  active_tasks:
    - task_id: "task_0001"
      title: "Record action trace into task hub"
      status: "active"
      created_at: "ISO-8601 timestamp"
      updated_at: "ISO-8601 timestamp"
      source: "working_state.current_plan"
      source_index: 1
      source_key: "working_state.current_plan:1:record action trace into task hub"
      evidence:
        - "working_state.current_plan"
  completed_tasks: []
  blocked_tasks: []
  recurring_duties: []
  action_trace:
    - action_id: "action_0001"
      trace_id: "trace_0001"
      timestamp: "ISO-8601 timestamp"
      workflow: "record_episode"
      status: "completed"
      summary: "Recorded episode and queued dream consolidation."
      audit_event_ids:
        - "audit_0001"
      memory_events: []
      review_events: []
      errors: []
      evidence:
        - "episode_0001"
  procedural_candidates:
    - candidate_id: "proc_0001"
      timestamp: "ISO-8601 timestamp"
      workflow: "record_episode"
      statement: "Repeated successful workflow may be reusable procedural memory after review."
      steps: []
      evidence:
        - "action_0001"
        - "action_0002"
      confidence: 0.65
      risk: "low"
      review_status: "pending"
      recommended_action: "review_then_promote"
      source_dream_id: "dream_0001"
      provenance:
        - type: "dream_procedural_candidate"
          dream_id: "dream_0001"
```

`working_state.current_plan` 仍然保留为 legacy/compatibility 字段。P10 会把它迁移为 `task_hub.active_tasks`、`completed_tasks` 或 `blocked_tasks`，但不删除旧字段。

真实状态变更的 trace 会进入 `task_hub.action_trace`。`dry_run` preview 可以写 audit / trace，但不能写 episode、dream job、adapter event index，也不能写入 `task_hub.action_trace`。

Dream 可以从重复成功的 action trace 里提出 `procedural_candidates`。这些候选不等于已采用的 procedural memory，必须等待 review。

## 14. Dream Queue

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

## 15. Audit Log

Audit log 记录运行时发生过什么。

它不是 memory promotion，也不是 identity update。它用于审计、回放、调试和后续 evaluation。

完整事件写入：

```text
audit.jsonl
traces.jsonl
dream_artifacts.jsonl
```

`state.json -> audit_log` 只保留最近摘要，避免核心状态无限膨胀。

```yaml
audit_log:
  - id: "audit_0001"
    timestamp: "ISO-8601 timestamp"
    actor: "local_generic_adapter"
    action: "record_episode"
    target: "memory_stores.episodic_memory"
    outcome: "recorded"
    evidence:
      - "episode_0001"
```

`dry_run` 可以产生 audit / trace，但不能写入 episode、dream job 或 adapter event index。

Dream artifact 用于保存一次 Dream run 的完整审查材料：

```yaml
dream_artifact:
  artifact_id: "dream_artifact_..."
  dream_id: "dream_..."
  input_manifest: {}
  observations: {}
  proposals: []
  review:
    status: "pending"
  patch_diff: {}
  decision_log: []
  rollback_metadata: {}
```

## 16. Update Log

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

## 17. Snapshots

Snapshots 是轻量审计锚点，在 candidate promote、archive、discard 或 quarantine 等 review action 前记录。

当前实现只保存 metadata，还不执行自动 rollback。

```yaml
snapshots:
  - snapshot_id: "snapshot_0001"
    timestamp: "ISO-8601 timestamp"
    actor: "manual_review"
    operation: "promote_candidate"
    target_path: "memory_stores.semantic_memory"
    evidence:
      - "cand_0001"
    metadata:
      review_decision_id: "review_decision_0001"
      candidate_id: "cand_0001"
    state_version: "0.8"
    memory_counts:
      semantic_memory: 3
      candidate_memory: 2
    rollback:
      reversible: true
      mode: "metadata_only"
      note: "Automatic rollback is not implemented yet."
```

## 18. State Transfer Package

Session 开始时不应该加载全部状态。

系统应该构建 transfer package。

```yaml
state_transfer_package:
  context_package_version: "0.2"
  identity_summary: {}
  active_intent: {}
  current_plan: []
  next_actions: []
  task_hub:
    active_tasks: []
    blocked_tasks: []
    recent_actions: []
    procedural_candidates: []
  active_tasks: []
  action_trace: []
  procedural_candidates: []
  blockers: []
  assumptions: []
  context_policy:
    policy_version: "0.2"
    mode: "bounded_state_activation"
    budgets:
      episodic_memory: 5
      semantic_memory: 5
      imported_memory: 5
      source_attribution: 12
  relevant_memories: []
  recent_episodes: []
  relevant_semantic_memories: []
  imported_memories: []
  relationship_context: {}
  source_attribution: []
  activation_trace:
    selected: []
    suppressed: []
    metrics: {}
  open_conflicts: []
  current_constraints: []
  continuity_anchors:
    who_am_i: "..."
    where_am_i: "..."
    what_am_i_doing: "..."
```

## 19. 最小不变量

一个有效的 01 state 必须满足：

- 每条 durable memory 都有 provenance、lifecycle metadata 和 update history；
- 每次 identity update 都有 update log entry；
- 每次 high-gate update 都有 evidence；
- 每条 user-specific memory 都有 privacy metadata；
- 每个 conflict 都有 status；
- 每个 generic ingest event 都来自已注册且启用的 adapter；
- 每个 generic ingest event 都经过 session policy；
- 每个重复的 `adapter_id + event_id` 组合都解析到原始 episode；
- 每个关键运行事件都可以进入 audit / trace；
- `dry_run` 的 audit / trace 不等同于 episode 写入；
- 每个 state snapshot 都有 schema version；
- 每个 review/promotion rollback reference 都能指向 snapshot metadata；
- `task_hub.action_trace` 只记录真实状态变更，不记录 non-mutating dry-run；
- procedural candidate 必须有 workflow、evidence 和 pending review status；
- 每个 session 都能回答 Identity、Context、Intent 三个锚点。
