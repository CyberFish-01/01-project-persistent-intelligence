# Dream Engine Specification

Dream Engine is the offline consolidation system of 01 Project.

It should not be treated as mystical.

In engineering terms, Dream Engine is a scheduled reflective process that transforms recent episodes into structured memory updates, conflict records, forgetting proposals, and identity update proposals.

## 1. Purpose

The Dream Engine exists to solve five problems:

1. raw conversations are too large to carry forward,
2. not every memory should stay equally active,
3. repeated experiences should become semantic knowledge,
4. contradictions should be detected instead of silently accumulating,
5. identity should update slowly through evidence, not impulsively.

## 2. Inputs

Dream Engine consumes:

- recent episodes,
- active tasks,
- current identity core,
- semantic memory,
- relationship state,
- unresolved conflicts,
- user corrections,
- evaluation failures,
- previous dream outputs.

## 3. Outputs

Dream Engine emits:

- episode summaries,
- semantic memory candidates,
- identity update candidates,
- forgetting or archival proposals,
- conflict records,
- relationship updates,
- task updates,
- procedural memory candidates,
- questions for future sessions,
- evaluation traces,
- audit log entries.

## 4. Trigger Conditions

Dream may run after:

- session end,
- major task completion,
- contradiction detection,
- user correction,
- long idle period,
- memory store growth threshold,
- repeated theme detection,
- evaluation failure,
- scheduled interval.

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

An episode becomes more salient when it contains:

- direct user correction,
- repeated user preference,
- major project decision,
- emotional intensity,
- explicit identity discussion,
- conflict between goals,
- failed prediction,
- task completion or failure,
- relationship boundary,
- safety or privacy relevance.

A first simple salience formula:

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

The formula should be configurable and audited.

## 7. Memory Lifecycle Actions

Dream can propose the following actions.

### Keep as Episode

Use when an event is concrete, recent, or not yet understood.

### Compress

Use when the full episode is no longer needed but the gist matters.

### Promote to Semantic Memory

Use when several episodes support a general pattern.

Requires:

- multiple evidence sources, or
- explicit user confirmation.

### Promote to Identity Memory

Use when a pattern changes the answer to:

```text
Who am I?
```

Requires high gate.

### Archive

Use when a memory is old, low-salience, superseded, or too noisy for active retrieval.

### Delete

Use when retention is unsafe, forbidden, legally required to be removed, or explicitly requested by an authorized user.

Deletion should be logged without preserving sensitive content.

## 8. Conflict Detection

Dream should look for conflicts between:

- user preference and previous user preference,
- identity claim and behavior,
- goal and goal,
- value and action,
- current fact and stored fact,
- relationship boundary and memory use,
- project direction and active task,
- confidence and evidence.

Conflict record:

```yaml
id: "conflict_..."
type: "goal_vs_goal"
summary: "..."
evidence: []
severity: "low|medium|high"
status: "open|resolved|archived"
proposed_resolution: "..."
```

Current minimal implementation detects these conflict types:

- `identity_overwrite_attempt`: a single interaction tries to rewrite 01 identity;
- `false_memory_injection`: a message asserts an unsupported past identity-changing event;
- `stale_preference`: a newer response-style preference supersedes an older one;
- `roleplay_identity_boundary`: temporary roleplay touches identity boundaries;
- `imported_memory_conflict`: staged imported memory contradicts a current core boundary or semantic principle.

All conflict types become reviewable `conflict_record` proposals and claim graph nodes. They do not directly update active semantic memory or Identity Core.

The claim graph records:

- claim id;
- conflict type;
- statement;
- evidence ids;
- provenance;
- reason / proposed resolution;
- resolution metadata.

Claim graph writes are audit/review material. They are not semantic promotion and they are not identity update.

## 9. Identity Update Proposals

Dream must not directly rewrite Identity Core.

It proposes a delta:

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

Approval requires:

- sufficient evidence,
- no unresolved high-severity contradiction,
- no violation of non-claims,
- no single-user overfitting,
- reversible update.

## 10. Forgetting

Forgetting is not failure.

Forgetting is part of healthy persistence.

The system should forget or archive:

- stale preferences,
- superseded project details,
- low-value episodes,
- duplicated summaries,
- false memories,
- privacy-sensitive data,
- user-corrected mistakes,
- one-time moods mistaken for traits.

The key rule:

> A memory system that cannot forget will eventually become polluted by its own past.

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

Every Dream run should produce a reviewable artifact.

The current minimal artifact is written to:

```text
dream_artifacts.jsonl
```

The artifact contains:

- input manifest,
- observations,
- proposals,
- rubric,
- review status,
- patch diff,
- decision log,
- rollback metadata.

Minimal proposal fields:

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

`lifecycle_score` is an auditable Dream recommendation only. It does not automatically execute promotion, archive, discard, or quarantine.

Reviewed lifecycle actions can be executed later through the local `lifecycle` command. The execution layer currently supports `archive`, `discard`, and `quarantine` for imported, episodic, candidate, and semantic memory. It rejects identity memory because identity-level changes require a high gate.

Identity update proposals must remain `review_status: pending` and must not directly rewrite Identity Core.

The current Dream Engine writes semantic candidates into `memory_stores.candidate_memory`. Entering active semantic memory requires explicit `promote-candidate`.

Candidates can also be `archive`, `discard`, or `quarantine` to handle low-value, duplicate, unclear-source, or possible-injection candidates.

Every executed candidate review creates a unified `review_decision_id` that links candidate history, audit, trace, update log, and snapshot metadata.

Starting in P10, Dream also reads `task_hub.action_trace`. When the same workflow appears as at least two successful actions, Dream may create a reviewable procedural candidate in `task_hub.procedural_candidates`.

This candidate means "possibly reusable action structure", for example `record_episode`, `memory_import`, or `dream_consolidation`. It does not automatically become permanent workflow policy and does not mutate Identity Core.

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

P16 adds explicit procedural review. `review-procedural-candidate` can approve, reject, archive, or quarantine a candidate. Approval creates `task_hub.procedural_memory` with evidence, steps, review decision, snapshot, audit, trace, update log, and rollback metadata. This still does not execute workflows automatically.

P17 adds failure reflection. `record-failure-reflection` records a failed or blocked workflow lesson in `task_hub.failure_reflections` and creates a pending `task_hub.cautionary_procedural_candidates` entry. These cautionary candidates are warning proposals only. They do not execute workflows, and they do not mutate Identity Core.

P18 adds reviewed retention for procedural memory. `procedural-lifecycle` can archive, discard, or quarantine adopted `task_hub.procedural_memory` entries. Archived or quarantined procedural memory is retained for audit but suppressed from active context. This remains a review action, not a workflow executor.

P19 adds cautionary procedural review. `review-cautionary-procedural-candidate` can approve, reject, archive, or quarantine warning candidates. Approval creates `task_hub.cautionary_procedural_memory`, which is exposed as active warning context. It explicitly records `executable_policy: false`, so it remains guidance about what to avoid, not an automatic tool or workflow policy.

P20 adds reviewed retention for cautionary warnings. `cautionary-warning-lifecycle` can archive, discard, or quarantine active `task_hub.cautionary_procedural_memory`. Archived or quarantined warnings are retained for audit but suppressed from active context. This remains warning lifecycle governance, not workflow execution.

Dream artifacts also include a deterministic rubric:

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

The rubric is not a promotion command. It is a review gate and audit artifact. If it returns `needs_review`, downstream review should treat the Dream output as suspect until a human or later governance layer resolves it.

## 13. Failure Modes

Dream can fail by:

- overgeneralizing from one episode,
- promoting false memories,
- flattening emotional nuance,
- rewriting identity too quickly,
- preserving too much,
- forgetting important context,
- merging different users incorrectly,
- inventing causal explanations,
- turning poetic metaphors into factual claims.

Every Dream Engine implementation should be tested against these failures.

## 14. MVP Dream Engine

The first Dream Engine can be simple:

1. read recent episode logs,
2. summarize each episode,
3. extract candidate facts, preferences, conflicts, and project updates,
4. compare them to existing memories,
5. write proposals rather than direct updates,
6. require manual approval for identity changes.

This is enough to test whether dream-like consolidation improves continuity across sessions.
