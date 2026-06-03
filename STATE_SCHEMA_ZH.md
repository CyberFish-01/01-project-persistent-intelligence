# State Schema 中文版

英文原文：[STATE_SCHEMA.md](./STATE_SCHEMA.md)

这份文档定义 State Transfer 的第一版具体 schema。

它保持实现无关，可以存为 JSON、YAML、SQLite、document database 或 typed object model。

## 1. 顶层状态

```yaml
state_version: "1.0"
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
  proposal_link_evidence: []
context_builder:
  builder_version: "0.3"
  policy: {}
  activation_traces: []
  last_context_package_id: null
task_hub:
  active_tasks: []
  completed_tasks: []
  blocked_tasks: []
  recurring_duties: []
  action_trace: []
  reflection_log: []
  reflection_guidance_queue: []
  reflection_guidance_decisions: []
  tool_safety_policy_proposals: []
  tool_safety_policy_links: []
  tool_safety_policy_link_lifecycle_decisions: []
  tool_safety_policy_decisions: []
  tool_safety_policy_lifecycle_decisions: []
  procedural_candidates: []
identity_update_gate:
  proposals: []
  review_decisions: []
  drift_events: []
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
  graph_version: "0.2"
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
      revision_policy:
        mode: "minimal_change_preview"
        requires_review: true
        allow_direct_memory_mutation: false
        allow_identity_core_mutation: false
      review_history: []
      source_conflict_id: "conflict_0001"
      resolution:
        status: "unresolved"
        proposal: "Require review before semantic or identity promotion."
        requires_review: true
        minimal_change: true
        may_update_identity_core: false
        may_update_semantic_memory: false
        patch_preview:
          mode: "minimal_change_preview"
          would_mutate_identity_core: false
          would_mutate_semantic_memory: false
  links:
    - link_id: "claim_link_0001"
      timestamp: "ISO-8601 timestamp"
      from: "episode_0001"
      to: "claim_conflict_0001"
      type: "contradicts|supports|supersedes|depends_on"
      reason: "Evidence item supports the existence of this claim record."
      confidence: 0.7
  proposal_link_evidence:
    - evidence_id: "proposal_link_evidence_0001"
      timestamp: "ISO-8601 timestamp"
      source_link_id: "tool_safety_policy_link_0001"
      from_proposal_id: "tool_safety_policy_proposal_0002"
      to_proposal_id: "tool_safety_policy_proposal_0001"
      link_type: "supersedes"
      status: "active"
      reviewer: "manual_review"
      rationale: "Expose proposal relationship as claim graph evidence."
      evidence:
        - "tool_safety_policy_link_0001"
        - "tool_safety_policy_proposal_0002"
        - "tool_safety_policy_proposal_0001"
      confidence: 0.86
      scope_overlap:
        score: 0.67
        shared_terms:
          - "tool_use"
          - "preflight"
      relationship_mode: "review_link_only"
      claim_graph_mode: "evidence_bridge_only"
      requires_review: true
      execution_prohibited: true
      executable_policy: false
      executable_policy_created: false
      identity_mutation_allowed: false
      claim_mutation_allowed: false
      semantic_memory_mutation_allowed: false
      provenance:
        - type: "tool_safety_policy_link_claim_graph_bridge"
          source_link_id: "tool_safety_policy_link_0001"
      rollback:
        snapshot_id: "snapshot_0008"
        reversible: true
  review_decisions: []
  policy:
    revision_mode: "minimal_change_preview"
    allow_direct_memory_mutation: false
    allow_identity_core_mutation: false
    requires_review: true
```

每个 claim 都必须有 evidence、provenance、status、dependencies、revision policy、review history 和 resolution metadata。

当前 Dream conflict detection 会同时写入 `open_conflicts`、对应 claim nodes，以及 support/contradiction/dependency links。Claim graph entry 是 review/audit material；`review-claim` 会创建 minimal-change patch preview 和 review decision，但不会直接修改 semantic memory 或 Identity Core。

P29 增加 proposal link evidence bridges。`bridge-proposal-link-claim-evidence` 会把已 review 的 tool/safety proposal relationship 复制到 `claim_graph.proposal_link_evidence`，并添加一条 review-only claim graph support link。它只把 relationship evidence 暴露给 claim graph，不 rewrite claims，不修改 semantic memory、Identity Core，也不创建 executable policy。

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
  reflection_log:
    - reflection_id: "reflection_0001"
      timestamp: "ISO-8601 timestamp"
      reflection_type: "general"
      workflow: "tool_use"
      observation: "观察到一个可复用的 workflow 模式。"
      lesson: "记录 reflection 以便后续检查行为是否真的改变。"
      expected_behavior: "在后续审查时验证这条 reflection log。"
      actor: "manual_review"
      source_ids:
        - "action_0002"
      evidence:
        - "action_0002"
      risk: "medium"
      confidence: 0.5
      status: "verified"
      verification_status: "verified"
      last_verified_at: "ISO-8601 timestamp"
      last_verification_id: "reflection_verification_0001"
      verification_history:
        - verification_id: "reflection_verification_0001"
          timestamp: "ISO-8601 timestamp"
          reflection_id: "reflection_0001"
          verifier: "manual_review"
          result: "verified"
          note: "在后续审查中确认。"
          evidence:
            - "action_0002"
      provenance:
        - type: "reflection_log"
          workflow: "tool_use"
          actor: "manual_review"
          source_ids:
            - "action_0002"
      update_history:
        - timestamp: "ISO-8601 timestamp"
          actor: "manual_review"
          operation: "record_reflection_log"
          evidence:
            - "action_0002"
  reflection_guidance_queue:
    - guidance_item_id: "reflection_guidance_item_0001"
      timestamp: "ISO-8601 timestamp"
      guidance_id: "reflection_policy_0001"
      context_package_id: "context_package_0001"
      reflection_id: "reflection_0001"
      workflow: "tool_use"
      review_priority: "medium"
      recommended_review_mode: "cautionary_review_only"
      review_focus: "Use verified reflection as cautionary review context."
      recommendation_note: "Record reflections -> Verify later behavior."
      evidence:
        - "action_0002"
      review_status: "pending|acknowledged|archived|quarantined"
      execution_prohibited: true
      executable_policy_created: false
      identity_mutation_allowed: false
      review_history: []
      provenance:
        - type: "reflection_policy_guidance"
          reflection_id: "reflection_0001"
  reflection_guidance_decisions:
    - decision_id: "reflection_guidance_decision_0001"
      timestamp: "ISO-8601 timestamp"
      guidance_item_id: "reflection_guidance_item_0001"
      reflection_id: "reflection_0001"
      workflow: "tool_use"
      reviewer: "manual_review"
      action: "acknowledge"
      result: "acknowledged"
      snapshot_id: "snapshot_0004"
      execution_prohibited: true
      executable_policy_created: false
      identity_mutation_allowed: false
  tool_safety_policy_proposals:
    - proposal_id: "tool_safety_policy_proposal_0001"
      timestamp: "ISO-8601 timestamp"
      policy_scope: "tool_use.preflight"
      proposed_rule: "Require explicit input readiness before tool execution."
      rationale: "Reviewed reflection guidance supports a proposal-only safety layer."
      source_guidance_item_id: "reflection_guidance_item_0001"
      source_reflection_id: "reflection_0001"
      workflow: "tool_use"
      review_priority: "high"
      risk: "high"
      confidence: 0.88
      proposer: "manual_review"
      status: "active"
      review_status: "pending|approved|rejected|archived|quarantined"
      proposal_mode: "proposal_only"
      requires_review: true
      execution_prohibited: true
      executable_policy: false
      executable_policy_created: false
      identity_mutation_allowed: false
      evidence:
        - "reflection_guidance_item_0001"
        - "reflection_0001"
        - "action_0002"
      proposal_score:
        score_id: "tool_safety_policy_score_0001"
        timestamp: "ISO-8601 timestamp"
        mode: "review_priority_only"
        evidence_strength: 0.89
        scope_specificity: 0.71
        staleness: 0.0
        priority_score: 0.77
        recommended_review_priority: "high"
        evidence_count: 3
        unique_evidence:
          - "reflection_guidance_item_0001"
          - "reflection_0001"
          - "action_0002"
        factors: []
        execution_prohibited: true
        executable_policy_created: false
        identity_mutation_allowed: false
      source_ids:
        - "action_0002"
      review_history: []
      lifecycle:
        status: "active"
        created_at: "ISO-8601 timestamp"
        last_reviewed_at: null
        review_status: "pending"
      update_history: []
      provenance:
        - type: "reflection_guidance_policy_proposal"
          guidance_item_id: "reflection_guidance_item_0001"
          reflection_id: "reflection_0001"
  tool_safety_policy_links:
    - link_id: "tool_safety_policy_link_0001"
      timestamp: "ISO-8601 timestamp"
      from_proposal_id: "tool_safety_policy_proposal_0002"
      to_proposal_id: "tool_safety_policy_proposal_0001"
      link_type: "supersedes"
      status: "active"
      reviewer: "manual_review"
      reason: "A narrower input-readiness proposal supersedes the broader preflight proposal."
      evidence:
        - "tool_safety_policy_proposal_0002"
        - "tool_safety_policy_proposal_0001"
        - "reflection_guidance_item_0001"
      confidence: 0.86
      from_policy_scope: "tool_use.preflight.input_readiness"
      to_policy_scope: "tool_use.preflight"
      scope_overlap:
        score: 0.67
        shared_terms:
          - "tool_use"
          - "preflight"
      from_proposal_score:
        mode: "review_priority_only"
        priority_score: 0.84
      to_proposal_score:
        mode: "review_priority_only"
        priority_score: 0.61
      relationship_mode: "review_link_only"
      requires_review: true
      execution_prohibited: true
      executable_policy: false
      executable_policy_created: false
      identity_mutation_allowed: false
      provenance:
        - type: "tool_safety_policy_proposal_link"
          from_proposal_id: "tool_safety_policy_proposal_0002"
          to_proposal_id: "tool_safety_policy_proposal_0001"
  tool_safety_policy_link_lifecycle_decisions:
    - decision_id: "tool_safety_policy_link_lifecycle_decision_0001"
      timestamp: "ISO-8601 timestamp"
      link_id: "tool_safety_policy_link_0001"
      from_proposal_id: "tool_safety_policy_proposal_0002"
      to_proposal_id: "tool_safety_policy_proposal_0001"
      link_type: "supersedes"
      reviewer: "manual_review"
      action: "archive"
      result: "archived"
      decision_note: "Archive stale relationship evidence after review."
      link_status_before: "active"
      snapshot_id: "snapshot_0007"
      evidence:
        - "tool_safety_policy_link_0001"
        - "tool_safety_policy_proposal_0002"
        - "tool_safety_policy_proposal_0001"
      confidence: 0.86
      scope_overlap:
        score: 0.67
        shared_terms:
          - "tool_use"
          - "preflight"
      relationship_mode: "review_link_only"
      requires_review: true
      execution_prohibited: true
      executable_policy: false
      executable_policy_created: false
      identity_mutation_allowed: false
      rollback:
        snapshot_id: "snapshot_0007"
        reversible: true
  tool_safety_policy_decisions:
    - decision_id: "tool_safety_policy_decision_0001"
      timestamp: "ISO-8601 timestamp"
      proposal_id: "tool_safety_policy_proposal_0001"
      policy_scope: "tool_use.preflight"
      source_guidance_item_id: "reflection_guidance_item_0001"
      source_reflection_id: "reflection_0001"
      reviewer: "manual_review"
      action: "approve"
      result: "approved"
      decision_note: "Approve as non-executable policy proposal evidence."
      snapshot_id: "snapshot_0005"
      evidence:
        - "tool_safety_policy_proposal_0001"
        - "reflection_guidance_item_0001"
      risk: "high"
      confidence: 0.88
      requires_review: true
      execution_prohibited: true
      executable_policy: false
      executable_policy_created: false
      identity_mutation_allowed: false
      proposal_score:
        mode: "review_priority_only"
        priority_score: 0.77
        execution_prohibited: true
        executable_policy_created: false
        identity_mutation_allowed: false
      rollback:
        snapshot_id: "snapshot_0005"
        reversible: true
  tool_safety_policy_lifecycle_decisions:
    - decision_id: "tool_safety_policy_lifecycle_decision_0001"
      timestamp: "ISO-8601 timestamp"
      proposal_id: "tool_safety_policy_proposal_0001"
      policy_scope: "tool_use.preflight"
      source_guidance_item_id: "reflection_guidance_item_0001"
      source_reflection_id: "reflection_0001"
      reviewer: "manual_review"
      action: "archive"
      result: "archived"
      decision_note: "Superseded by a more specific proposal."
      proposal_status_before: "approved"
      snapshot_id: "snapshot_0006"
      evidence:
        - "tool_safety_policy_proposal_0001"
        - "reflection_guidance_item_0001"
      risk: "high"
      confidence: 0.88
      proposal_mode: "proposal_only"
      requires_review: true
      execution_prohibited: true
      executable_policy: false
      executable_policy_created: false
      identity_mutation_allowed: false
      proposal_score:
        mode: "review_priority_only"
        priority_score: 0.61
        staleness: 0.75
        execution_prohibited: true
        executable_policy_created: false
        identity_mutation_allowed: false
      rollback:
        snapshot_id: "snapshot_0006"
        reversible: true
  failure_reflections:
    - reflection_id: "failure_reflection_0001"
      timestamp: "ISO-8601 timestamp"
      workflow: "tool_use"
      summary: "A tool workflow failed because required input was missing."
      lesson: "Check required inputs before tool execution."
      next_action: "Ask for or infer required input first."
      source_action_id: "action_0002"
      status: "active"
      reviewer: "manual_review"
      evidence:
        - "action_0002"
      provenance:
        - type: "failure_reflection"
          source_action_id: "action_0002"
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
  cautionary_procedural_candidates:
    - candidate_id: "caution_0001"
      timestamp: "ISO-8601 timestamp"
      workflow: "tool_use"
      statement: "Failure reflection for workflow 'tool_use': Check required inputs before tool execution."
      avoid: "Tried a tool workflow before collecting required input."
      next_action: "Ask for or infer required input first."
      evidence:
        - "failure_reflection_0001"
        - "action_0002"
      confidence: 0.6
      risk: "medium"
      review_status: "pending"
      recommended_action: "review_then_consider"
      source_reflection_id: "failure_reflection_0001"
      provenance:
        - type: "failure_reflection_caution"
          reflection_id: "failure_reflection_0001"
  cautionary_procedural_memory:
    - memory_id: "caution_mem_0001"
      timestamp: "ISO-8601 timestamp"
      workflow: "tool_use"
      statement: "Failure reflection for workflow 'tool_use': Check required inputs before tool execution."
      avoid: "Tried a tool workflow before collecting required input."
      next_action: "Ask for or infer required input first."
      evidence:
        - "failure_reflection_0001"
        - "action_0002"
      confidence: 0.6
      risk: "medium"
      status: "active"
      source_candidate_id: "caution_0001"
      source_reflection_id: "failure_reflection_0001"
      review_decision_id: "cautionary_decision_0001"
      executable_policy: false
      lifecycle:
        status: "active"
        review_status: "approved"
  cautionary_lifecycle_decisions:
    - decision_id: "cautionary_lifecycle_decision_0001"
      timestamp: "ISO-8601 timestamp"
      memory_id: "caution_mem_0001"
      workflow: "tool_use"
      source_reflection_id: "failure_reflection_0001"
      reviewer: "manual_review"
      action: "archive"
      result: "archived"
      decision_note: "Superseded by a more specific warning."
      memory_status_before: "active"
      snapshot_id: "snapshot_0004"
      risk: "medium"
      confidence: 0.6
      evidence:
        - "caution_mem_0001"
        - "failure_reflection_0001"
      executable_policy_created: false
      rollback:
        reversible: true
  procedural_memory:
    - memory_id: "proc_mem_0001"
      timestamp: "ISO-8601 timestamp"
      workflow: "record_episode"
      statement: "Repeated successful workflow may be reusable procedural memory after review."
      steps: []
      evidence:
        - "action_0001"
        - "action_0002"
      confidence: 0.65
      risk: "low"
      status: "active"
      source_candidate_id: "proc_0001"
      review_decision_id: "procedural_decision_0001"
      lifecycle:
        status: "active"
        review_status: "approved"
  procedural_lifecycle_decisions:
    - decision_id: "procedural_lifecycle_decision_0001"
      timestamp: "ISO-8601 timestamp"
      memory_id: "proc_mem_0001"
      workflow: "record_episode"
      reviewer: "manual_review"
      action: "archive"
      result: "archived"
      decision_note: "Superseded by a newer procedural memory."
      memory_status_before: "active"
      snapshot_id: "snapshot_0002"
      risk: "low"
      confidence: 0.65
      evidence:
        - "proc_mem_0001"
        - "action_0001"
      rollback:
        reversible: true
  procedural_review_decisions:
    - decision_id: "procedural_decision_0001"
      timestamp: "ISO-8601 timestamp"
      candidate_id: "proc_0001"
      workflow: "record_episode"
      reviewer: "manual_review"
      action: "approve"
      result: "approved"
      snapshot_id: "snapshot_0001"
  cautionary_review_decisions:
    - decision_id: "cautionary_decision_0001"
      timestamp: "ISO-8601 timestamp"
      candidate_id: "caution_0001"
      workflow: "tool_use"
      source_reflection_id: "failure_reflection_0001"
      reviewer: "manual_review"
      action: "approve"
      result: "approved"
      snapshot_id: "snapshot_0003"
      executable_policy_created: false
```

`working_state.current_plan` 仍然保留为 legacy/compatibility 字段。P10 会把它迁移为 `task_hub.active_tasks`、`completed_tasks` 或 `blocked_tasks`，但不删除旧字段。

真实状态变更的 trace 会进入 `task_hub.action_trace`。`dry_run` preview 可以写 audit / trace，但不能写 episode、dream job、adapter event index，也不能写入 `task_hub.action_trace`。

Dream 可以从重复成功的 action trace 里提出 `procedural_candidates`。这些候选不等于已采用的 procedural memory，必须等待 review。P16 增加 `review-procedural-candidate`；批准后会创建 `task_hub.procedural_memory`，并连接 decision、snapshot、audit、trace、update log 和 rollback metadata。它仍然不会执行 workflow policy。

P17 增加显式 failure reflection。`record-failure-reflection` 会把失败或阻塞的 workflow lesson 记录到 `task_hub.failure_reflections`，并创建 pending `task_hub.cautionary_procedural_candidates` 条目。Cautionary candidates 是警告型 proposal，不是可执行 workflow policy，并且不能修改 Identity Core。

P18 增加 procedural lifecycle retention。`procedural-lifecycle` 可以对已 review 的 `task_hub.procedural_memory` 条目执行 archive、discard 或 quarantine。它会写入 snapshot、audit、trace、update log、lifecycle history 和 `task_hub.procedural_lifecycle_decisions`，但仍然不会执行 workflow policy。context package 只暴露 active procedural memory。

P19 增加 cautionary procedural review。`review-cautionary-procedural-candidate` 可以 approve、reject、archive 或 quarantine warning candidates。批准后会创建 active `task_hub.cautionary_procedural_memory`，未来 context 会把它作为 active warning 暴露。它明确记录 `executable_policy: false`，写入 snapshot、audit、trace、update log、review decision 和 rollback metadata，并且仍然不会执行 workflow policy。

P20 增加 cautionary warning lifecycle retention。`cautionary-warning-lifecycle` 可以 archive、discard 或 quarantine active `task_hub.cautionary_procedural_memory`。它会写入 snapshot、audit、trace、update log、lifecycle history、`task_hub.cautionary_lifecycle_decisions`，并保持 `executable_policy: false`。context package 只暴露 active cautionary warnings。

P21 增加 reflection log。`record-reflection` 可以记录通用 reflection 条目，`verify-reflection` 可以把 reflection 标记为 verified、not_observed、regressed 或 superseded。Reflection log 会保留 observation、lesson、expected_behavior、source_ids、evidence、verification history 和 update history，并暴露最近条目到 context。它仍然不会执行 workflow，也不会修改 Identity Core。

P22 增加 reflection-policy guidance。`build_context_package()` 会从 verified reflection log entries 推导 advisory-only `reflection_policy_guidance`。P23 增加 durable `task_hub.reflection_guidance_queue` 和 `task_hub.reflection_guidance_decisions`；`review-reflection-guidance` 可以 acknowledge、archive 或 quarantine guidance item，并写入 snapshot、audit、trace、update log 和可 replay 的 event metadata。Reflection guidance 仍然不可执行，也不能修改 Identity Core。

P24 增加 tool/safety policy proposal layer。`propose-tool-safety-policy` 只能从已经 review 的 reflection guidance 创建非执行 policy proposal；`review-tool-safety-policy-proposal` 可以 approve、reject、archive 或 quarantine proposal。Proposal 和 decision 会写入 snapshot、audit、trace、update metadata 和可 replay 的 event reference。它们明确保持 `proposal_mode: "proposal_only"`、`requires_review: true`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`。P24 不创建 policy executor，也不会修改 Identity Core。

P25 增加 tool/safety policy proposal lifecycle retention。`tool-safety-policy-lifecycle` 可以 archive、discard 或 quarantine 已 review 的 policy proposal。它会写入 snapshot、audit、trace、update log、lifecycle history 和 `task_hub.tool_safety_policy_lifecycle_decisions`，同时保持 proposal-only 和 non-executable invariants。context package 只暴露 active pending/approved proposals，所以 archived、discarded 和 quarantined proposals 会从 active state transfer 中被压制。

P26 增加 tool/safety proposal evidence scoring。每个 proposal 都会获得 `proposal_score`，包含 evidence strength、scope specificity、staleness、priority score、review priority、factors 和 non-execution invariants。Score 只是 review-priority signal：它会用于 context 中 active proposals 的排序，并写入 review/lifecycle decisions，但不会创建 allow/deny rule、executable policy，也不会修改 Identity Core。

P27 增加 tool/safety proposal relationship links。`link-tool-safety-policy-proposals` 可以记录 proposal 之间的 review-only 关系：`supports`、`conflicts_with`、`supersedes`、`overlaps` 和 `depends_on`。Link 会拒绝 self-link，压制重复 active link，要求 proposal id 已存在且必须有 evidence，写入 audit/trace/update metadata，并保持 `relationship_mode: "review_link_only"`、`execution_prohibited: true`、`executable_policy: false`、`executable_policy_created: false` 和 `identity_mutation_allowed: false`。Context package 只把 recent active links 作为关系证据暴露。

P28 增加 tool/safety proposal link lifecycle retention。`tool-safety-policy-link-lifecycle` 可以 archive、discard 或 quarantine 已 review 的 proposal links。它会写入 snapshot、audit、trace、update log、lifecycle history 和 `task_hub.tool_safety_policy_link_lifecycle_decisions`，同时保持 `relationship_mode: "review_link_only"` 和 non-executable invariants。Context package 只暴露 active proposal links，所以 archived、discarded 和 quarantined links 会从 active state transfer 中被压制。

## 14. Identity Update Gate

Identity Update Gate 管理慢速身份成长。

P11 的实现允许创建和审查 identity proposal，但不会直接改写 `identity_core`。即使 proposal 通过 high gate，当前也只会追加 `memory_stores.identity_memory`。

```yaml
identity_update_gate:
  gate_version: "0.9"
  required_gate: "high"
  min_supporting_evidence: 3
  allow_identity_core_patch: false
  proposals:
    - proposal_id: "identity_proposal_0001"
      timestamp: "ISO-8601 timestamp"
      target_path: "memory_stores.identity_memory"
      statement: "01 identity growth is evidence-backed and reviewable."
      operation: "append_identity_memory"
      proposer: "manual_review"
      rationale: "Three episodes support a slow identity memory."
      evidence:
        - "episode_0001"
        - "episode_0002"
        - "episode_0003"
      confidence: 0.82
      gate: "high"
      review_status: "pending|approved|rejected|quarantined"
      gate_result:
        eligible: true
        required_evidence_count: 3
        evidence_count: 3
        reasons: []
      non_claims_check:
        passed: true
        violations: []
      drift_score:
        score: 0.17
        risk: "low"
        factors: []
      rollback_required: true
      may_update_identity_core: false
  review_decisions:
    - decision_id: "identity_decision_0001"
      proposal_id: "identity_proposal_0001"
      action: "approve|reject|quarantine"
      result: "approved|rejected|quarantined"
      gate: "high"
      snapshot_id: "snapshot_0001"
      gate_result: {}
  drift_events: []
  policy:
    non_claims_check_required: true
    drift_threshold: 0.35
    approved_target: "memory_stores.identity_memory"
    identity_core_update_mode: "blocked_in_v0.9"
```

Gate 规则：

- high gate 至少需要 3 个 supporting evidence；
- evidence 必须能指向已知 memory/action/claim；
- non-claims check 会阻止 biological emotion、consciousness、human identity 等声明；
- drift score 超过阈值时不能 approve；
- identity_core patch 在 v0.9 中被阻止；
- approve 会创建 snapshot、audit、trace、update_log，并追加 identity_memory。

## 15. Dream Queue

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

## 16. Audit Log

Audit log 记录运行时发生过什么。

它不是 memory promotion，也不是 identity update。它用于审计、回放、调试和后续 evaluation。

完整事件写入：

```text
audit.jsonl
traces.jsonl
events.jsonl
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

`events.jsonl` 是 P12 引入的 append-only state transition envelope。它把一个已完成的 runtime trace 与其产生的 durable `update_log` entry 连接起来。它是 replay/audit ledger，不是完整 state 的第二份副本。

```yaml
event:
  event_id: "event_0001"
  sequence: 1
  timestamp: "ISO-8601 timestamp"
  event_type: "state_transition"
  state_version: "1.0"
  workflow: "record_episode"
  trace_id: "trace_0001"
  audit_event_ids:
    - "audit_0001"
  update_id: "update_0001"
  actor: "local_generic_adapter"
  operation: "append"
  target_path: "memory_stores.episodic_memory"
  before: null
  after: "episode_0001"
  evidence:
    - "episode_0001"
  rollback:
    reversible: true
  memory_events: []
  review_events: []
```

P12 replay 支持刻意保持保守：

- `replay-events` 检查 event `update_id` 是否仍能引用当前 `update_log`；
- 它会报告旧 state update 的 coverage，但不要求 P12 之前的 update 必须有 event；
- `rollback-preview <snapshot_id>` 只报告 snapshot 与 affected event metadata，不修改 state；
- `dry_run` preview 不写入 state event。

Dream artifact 用于保存一次 Dream run 的完整审查材料：

```yaml
dream_artifact:
  artifact_id: "dream_artifact_..."
  artifact_version: "1.0"
  dream_id: "dream_..."
  input_manifest:
    episodes: []
    imports: []
    pending_jobs: []
    item_count: 0
    items: []
  provenance:
    agent: "dream_engine"
    activity: "dream_consolidation"
    used_entities: []
    generated_entities: []
  observations:
    summary: "..."
    input_counts: {}
  proposals: []
  proposal_index:
    by_type: {}
    by_risk: {}
    by_recommended_action: {}
  review:
    status: "pending"
    required_for: []
    queue: []
    queue_summary: {}
  patch_diff:
    mode: "candidate_only"
    state_writes: {}
    proposed_changes: {}
    blocked_direct_writes: {}
    summary: {}
  decision_log: []
  rollback_metadata:
    rollback_required: false
    affected_ids: {}
    identity_core_changed: false
    active_memory_direct_write: false
  package_completeness:
    has_input_manifest: true
    has_observations: true
    has_proposals: true
    has_review_queue: true
    has_patch_diff: true
    has_decision_log: true
    has_rollback_metadata: true
```

Dream artifact package v1.0 采用本地 PROV/trace 形状：

- `input_manifest` 记录本次 Dream run 使用的具体 episodes / imported memories；
- `provenance` 连接 Dream activity、used entities 和生成的 candidate/review entities；
- `review.queue` 标明 proposal、risk、evidence，以及是否需要人工 review；
- `patch_diff.mode: candidate_only` 明确 Dream 只生成 candidate/review material，不直接写 active memory 或 Identity Core；
- `rollback_metadata.affected_ids` 列出本次 Dream 影响到的 candidate memory、claim graph、identity gate 和 procedural candidate ids；
- `package_completeness` 会被 validation 检查，避免后续 Dream run 静默丢失审计材料。

## 17. Update Log

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

## 18. Snapshots

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
    state_version: "1.0"
    memory_counts:
      semantic_memory: 3
      candidate_memory: 2
    rollback:
      reversible: true
      mode: "metadata_only"
      note: "Automatic rollback is not implemented yet."
```

## 19. State Transfer Package

Session 开始时不应该加载全部状态。

系统应该构建 transfer package。

```yaml
state_transfer_package:
  context_package_version: "0.3"
  context_package_id: "context_package_..."
  identity_summary: {}
  active_intent: {}
  current_plan: []
  next_actions: []
  task_hub:
    active_tasks: []
    blocked_tasks: []
    recent_actions: []
    failure_reflections: []
    procedural_candidates: []
    cautionary_procedural_candidates: []
    reflection_log: []
    reflection_policy_guidance:
      mode: "advisory_only"
      execution_prohibited: true
      identity_mutation_allowed: false
      verified_reflections: []
      review_recommendations: []
    reflection_guidance_queue: []
    tool_safety_policy_proposals: []
    tool_safety_policy_links: []
    tool_safety_policy_link_lifecycle_decisions: []
    cautionary_procedural_memory: []
    cautionary_lifecycle_decisions: []
    procedural_memory: []
    procedural_lifecycle_decisions: []
  active_tasks: []
  action_trace: []
  failure_reflections: []
  procedural_candidates: []
  cautionary_procedural_candidates: []
  reflection_log: []
  reflection_policy_guidance:
    mode: "advisory_only"
    execution_prohibited: true
    identity_mutation_allowed: false
    verified_reflections: []
    review_recommendations: []
  reflection_guidance_queue: []
  tool_safety_policy_proposals: []
  tool_safety_policy_links: []
  tool_safety_policy_link_lifecycle_decisions: []
  cautionary_procedural_memory: []
  cautionary_lifecycle_decisions: []
  procedural_memory: []
  procedural_lifecycle_decisions: []
  identity_update_gate:
    required_gate: "high"
    pending_proposals: []
    recent_decisions: []
    recent_drift_events: []
  blockers: []
  assumptions: []
  context_policy:
    policy_version: "0.3"
    mode: "bounded_state_activation"
    budgets:
      episodic_memory: 5
      semantic_memory: 5
      imported_memory: 5
      source_attribution: 12
      activation_trace_history: 20
    signal_weights:
      identity_gate_evidence: 0.08
      claim_graph_evidence: 0.08
      dream_artifact_input: 0.06
    persistence:
      activation_trace_history: true
      context_builds_are_state_events: false
  relevant_memories: []
  recent_episodes: []
  relevant_semantic_memories: []
  imported_memories: []
  relationship_context: {}
  source_attribution: []
  activation_trace:
    trace_id: "context_activation_..."
    context_package_id: "context_package_..."
    policy_version: "0.3"
    selected: []
    suppressed: []
    signal_summary: {}
    metrics: {}
  context_signal_summary:
    identity_gate_evidence_count: 0
    claim_graph_evidence_count: 0
    dream_artifact_input_count: 0
    dream_artifact_proposal_count: 0
  open_conflicts: []
  current_constraints: []
  continuity_anchors:
    who_am_i: "..."
    where_am_i: "..."
    what_am_i_doing: "..."
```

## 20. 最小不变量

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
- 每个 state event 都引用现有 update_log entry；
- `task_hub.action_trace` 只记录真实状态变更，不记录 non-mutating dry-run；
- 每个 failure reflection 都有 workflow、summary、lesson、evidence、provenance 和 status；
- procedural candidate 必须有 workflow、evidence 和 pending review status；
- 每个 cautionary procedural candidate 都有 source reflection、avoid 指引、evidence，以及 pending 或带 review history 的已审查状态；
- 每个 cautionary procedural memory 都有 evidence、lifecycle metadata、provenance、update history，并且 `executable_policy: false`；
- 每个 cautionary lifecycle decision 都有 memory id、workflow、reviewer、action、result、snapshot metadata，并且 `executable_policy_created: false`；
- 每个 procedural lifecycle decision 都有 memory id、workflow、reviewer、action、result 和 snapshot metadata；
- 每个 tool/safety policy link 都引用已存在的 proposal，带有 evidence，保持 `review_link_only`，并且不能创建 executable policy 或修改 Identity Core；
- 每个 tool/safety policy link lifecycle decision 都引用已存在的 link，保持 `review_link_only`，并且不能创建 executable policy 或修改 Identity Core；
- 每个 proposal link claim-graph evidence bridge 都保持 `evidence_bridge_only`，不能 rewrite claims，不能修改 semantic memory，也不能创建 executable policy；
- identity update 必须进入 `identity_update_gate`，并保留 gate_result、non_claims_check 和 drift_score；
- P11 不允许直接 patch `identity_core`，approve 只能追加 identity_memory；
- 每个 session 都能回答 Identity、Context、Intent 三个锚点。
