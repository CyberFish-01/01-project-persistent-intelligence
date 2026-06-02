# State Schema

This document defines a first concrete schema for State Transfer.

The schema is intentionally implementation-neutral. It can be stored as JSON, YAML, SQLite rows, a document database, or a typed object model.

## 1. Top-Level State

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

### Imported Memory

Imported memory contains external material brought in from AstrBot, Angel Memory, or any other memory system.

It is staged by default.

It must not update Identity Core directly.

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

Candidate memory stores Dream-produced memory candidates.

It does not enter active semantic memory by default.

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

Entering active semantic memory requires explicit review / promote.

Candidate memory review actions:

```text
promote
archive
discard
quarantine
```

`archive` copies an audit summary into `archived_memory`; `discard` only marks the candidate as discarded; `quarantine` is for candidates with unclear source, possible injection, or high conflict risk.

`recommended_lifecycle_action` is a Dream recommendation. Human review can accept or reject it.

Every completed candidate review writes a `review_decision` into `review_history`, stores `last_review_decision_id` on the candidate, and references the same decision from lifecycle metadata, audit events, traces, update log entries, and snapshot metadata.

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

Archived memory is not deleted immediately.

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

Durable memory lifecycle actions:

```text
archive
discard
quarantine
```

Current implementation supports lifecycle actions for `imported_memory`, `episodic_memory`, `candidate_memory`, and `semantic_memory`.

`identity_memory` is intentionally rejected by the generic lifecycle command and requires a separate high gate.

Every executed lifecycle action writes a `lifecycle_decision_id` into `lifecycle_history`, lifecycle metadata, audit events, traces, update log entries, and snapshot metadata. `archive` also copies an audit-retained summary into `archived_memory`. `discard` and `quarantine` mark the original memory but do not delete its audit trail.

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

## 8. Adapter Registry

Adapter registry controls which external adapters may use the generic ingest path.

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

`POST /v1/adapter/ingest` requires a registered and enabled `adapter_id`.

## 9. Session Policy

Session policy controls which registered adapters may perform real writes for specific channels, sessions, or users.

It runs after adapter registry validation:

```text
adapter registry -> session policy -> dry-run / write / reject
```

The default policy is conservative:

- local generic adapter can write;
- AstrBot thin adapter defaults to `dry_run_only`;
- unmatched rules default to `dry_run_only`.

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

Valid actions:

```text
allow
dry_run_only
reject
```

`dry_run_only` downgrades real write requests to dry-run previews. It must not write an episode, dream job, or adapter event index entry.

## 10. Adapter Event Index

Adapter event index prevents duplicate external events from being recorded twice.

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

Only real writes with an `event_id` update this index. Dry-run previews do not.

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

Claim graph records reviewable claims, reasons, evidence, and conflict dependencies.

It is append-friendly and does not directly mutate active semantic memory or Identity Core.

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
  review_decisions: []
  policy:
    revision_mode: "minimal_change_preview"
    allow_direct_memory_mutation: false
    allow_identity_core_mutation: false
    requires_review: true
```

Every claim must have evidence, provenance, status, dependencies, revision policy, review history, and resolution metadata.

Current Dream conflict detection writes `open_conflicts`, corresponding claim nodes, and support/contradiction/dependency links. Claim graph entries are review/audit material; `review-claim` creates a minimal-change patch preview and review decision, but does not directly mutate semantic memory or Identity Core.

## 13. Task Hub

Task Hub preserves task continuity and action structure.

It is not a platform todo list or adapter state. It is the local 01 Core state layer for answering: what am I working on, what did I just do, and how should work resume?

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

`working_state.current_plan` is retained as a legacy/compatibility field. P10 migrates it into `task_hub.active_tasks`, `completed_tasks`, or `blocked_tasks` without deleting the legacy field.

Trace entries for real state mutations enter `task_hub.action_trace`. `dry_run` preview may write audit / trace, but it must not write episodes, dream jobs, adapter event index entries, or `task_hub.action_trace`.

Dream may propose `procedural_candidates` from repeated successful action traces. These candidates are not adopted procedural memory until reviewed. P16 adds `review-procedural-candidate`; approval creates `task_hub.procedural_memory` with decision, snapshot, audit, trace, update log, and rollback metadata. It still does not execute workflow policy.

P17 adds explicit failure reflection. `record-failure-reflection` records a failed or blocked workflow lesson in `task_hub.failure_reflections` and creates a pending `task_hub.cautionary_procedural_candidates` entry. Cautionary candidates are warning proposals, not executable workflow policy, and they must not mutate Identity Core.

P18 adds procedural lifecycle retention. `procedural-lifecycle` can archive, discard, or quarantine reviewed `task_hub.procedural_memory` entries. It writes snapshot, audit, trace, update log, lifecycle history, and `task_hub.procedural_lifecycle_decisions`, but it still does not execute workflow policy. Context packages only expose active procedural memory.

P19 adds cautionary procedural review. `review-cautionary-procedural-candidate` can approve, reject, archive, or quarantine warning candidates. Approval creates active `task_hub.cautionary_procedural_memory`, which enters future context as an active warning. It explicitly records `executable_policy: false`, writes snapshot, audit, trace, update log, review decision, rollback metadata, and still does not execute workflow policy.

P20 adds cautionary warning lifecycle retention. `cautionary-warning-lifecycle` can archive, discard, or quarantine active `task_hub.cautionary_procedural_memory`. It writes snapshot, audit, trace, update log, lifecycle history, `task_hub.cautionary_lifecycle_decisions`, and preserves `executable_policy: false`. Context packages only expose active cautionary warnings.

## 14. Identity Update Gate

Identity Update Gate manages slow identity growth.

The P11 implementation can create and review identity proposals, but it does not directly rewrite `identity_core`. Even when a proposal passes the high gate, the current target is appending `memory_stores.identity_memory`.

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

Gate rules:

- high gate requires at least 3 supporting evidence ids,
- evidence must point to known memory/action/claim ids,
- non-claims check blocks biological emotion, consciousness, human identity, and similar claims,
- proposals whose drift score exceeds the threshold cannot be approved,
- identity_core patching is blocked in v0.9,
- approval creates snapshot, audit, trace, update_log, and appends identity_memory.

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

Audit log records what happened at runtime.

It is not memory promotion and it is not an identity update. It exists for auditability, replay, debugging, and later evaluation.

Full events are written to:

```text
audit.jsonl
traces.jsonl
events.jsonl
dream_artifacts.jsonl
```

`state.json -> audit_log` keeps only recent summaries so the core state does not grow without bound.

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

`dry_run` may produce audit / trace records, but must not write an episode, dream job, or adapter event index entry.

`events.jsonl` is the P12 append-only state transition envelope. It links a completed runtime trace to the durable `update_log` entry it produced. It is a replay/audit ledger, not a second copy of the whole state.

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

P12 replay support is intentionally conservative:

- `replay-events` validates that event `update_id` values still reference current `update_log` entries,
- it reports coverage for old state updates but does not require pre-P12 updates to have events,
- `rollback-preview <snapshot_id>` reports snapshot and affected event metadata without mutating state,
- `dry_run` previews do not write state events.

Dream artifacts keep the full review material for one Dream run:

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

Dream artifact package v1.0 follows a local PROV/trace shape:

- `input_manifest` records the concrete episodes/imported memories used by the Dream run,
- `provenance` links Dream activity, used entities, and generated candidate/review entities,
- `review.queue` names proposals, risks, evidence, and whether human review is required,
- `patch_diff.mode: candidate_only` documents that Dream produced candidates/review material, not direct active memory or Identity Core writes,
- `rollback_metadata.affected_ids` lists candidate memory, claim graph, identity gate, and procedural candidate ids affected by this Dream run,
- `package_completeness` is validated so future runs do not silently lose audit material.

## 17. Update Log

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

## 18. Snapshots

Snapshots are lightweight audit anchors recorded before review actions such as candidate promotion, archive, discard, or quarantine.

The current implementation stores metadata only; it does not yet perform automatic rollback.

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

At session start, the system should not load everything.

It should build a transfer package.

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
    cautionary_procedural_memory: []
    cautionary_lifecycle_decisions: []
    procedural_memory: []
    procedural_lifecycle_decisions: []
  active_tasks: []
  action_trace: []
  failure_reflections: []
  procedural_candidates: []
  cautionary_procedural_candidates: []
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

## 20. Minimal Invariants

A valid 01 state must satisfy:

- every durable memory has provenance, lifecycle metadata, and update history,
- every identity update has an update log entry,
- every high-gate update has evidence,
- every user-specific memory has privacy metadata,
- every conflict has status,
- every generic ingest event comes from a registered and enabled adapter,
- every generic ingest event passes through session policy,
- every repeated `adapter_id + event_id` pair resolves to the original episode,
- every important runtime event can enter audit / trace,
- `dry_run` audit / trace is not equivalent to episode writing,
- every state snapshot has a schema version,
- every review/promotion rollback reference points to snapshot metadata,
- every state event references an existing update_log entry,
- `task_hub.action_trace` records real state mutations, not non-mutating dry-runs,
- every failure reflection has workflow, summary, lesson, evidence, provenance, and status,
- every procedural candidate has workflow, evidence, and pending review status,
- every cautionary procedural candidate has a source reflection, avoid guidance, evidence, and pending or reviewed status with review history,
- every cautionary procedural memory has evidence, lifecycle metadata, provenance, update history, and `executable_policy: false`,
- every cautionary lifecycle decision has memory id, workflow, reviewer, action, result, snapshot metadata, and `executable_policy_created: false`,
- every procedural lifecycle decision has memory id, workflow, reviewer, action, result, and snapshot metadata,
- every identity update enters `identity_update_gate` and keeps gate_result, non_claims_check, and drift_score,
- P11 must not directly patch `identity_core`; approval can only append identity_memory,
- every session can answer Identity, Context, and Intent anchors.
