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
  next_questions:
    - "What is the smallest runnable 01 prototype?"
```

## 12. Failure Modes

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

## 13. MVP Dream Engine

The first Dream Engine can be simple:

1. read recent episode logs,
2. summarize each episode,
3. extract candidate facts, preferences, conflicts, and project updates,
4. compare them to existing memories,
5. write proposals rather than direct updates,
6. require manual approval for identity changes.

This is enough to test whether dream-like consolidation improves continuity across sessions.
