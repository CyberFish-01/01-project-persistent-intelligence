# State Schema

This document defines a first concrete schema for State Transfer.

The schema is intentionally implementation-neutral. It can be stored as JSON, YAML, SQLite rows, a document database, or a typed object model.

## 1. Top-Level State

```yaml
state_version: "0.1"
agent_id: "01"
created_at: "ISO-8601 timestamp"
updated_at: "ISO-8601 timestamp"

identity_core: {}
working_state: {}
memory_stores: {}
relationship_map: {}
project_map: {}
affective_state: {}
open_conflicts: []
dream_queue: []
evaluation_trace: []
update_log: []
```

## 2. Identity Core

Identity Core is slow-changing.

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

Working state is fast-changing.

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

Archived memory is not deleted immediately.

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

Affective state is functional, not biological.

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

## 8. Open Conflicts

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

## 9. Dream Queue

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

## 10. Update Log

Every durable update must be recorded.

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

## 11. State Transfer Package

At session start, the system should not load everything.

It should build a transfer package.

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

## 12. Minimal Invariants

A valid 01 state must satisfy:

- every durable memory has provenance,
- every identity update has an update log entry,
- every high-gate update has evidence,
- every user-specific memory has privacy metadata,
- every conflict has status,
- every state snapshot has a schema version,
- every session can answer Identity, Context, and Intent anchors.
