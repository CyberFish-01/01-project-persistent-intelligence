# Session Resume Scenario Plan

Chinese version: [SESSION_RESUME_SCENARIO_PLAN_ZH.md](./SESSION_RESUME_SCENARIO_PLAN_ZH.md)

Status: `document-only`, `scenario-plan`, `non-runtime`.

P89 defines deterministic session resume scenarios for a future thin
interaction harness. It does not implement Temporal Awareness runtime, temporal
event writes, recall event writes, scenario tests, CLI commands, API routes,
context building, review queue execution, trace storage, thought loops, growth
lifecycle, identity mutation, memory rewrite, UI, AstrBot, adapter, companion,
cloud, or product behavior.

## Plan Rule

```text
session resume scenarios simulate elapsed time.
simulated elapsed time is not a temporal event.
resume preview is not memory rewrite.
resume preview is not identity update.
```

## Problem

P85 named `session_resume_scenario` as a future harness surface. P86-P88 then
defined intake, context preview, and review queue preview. P89 designs the
deterministic scenarios that can test whether those surfaces preserve continuity
without turning elapsed time into runtime mutation.

The point is not to make the system "feel time". The point is to ask whether a
future harness can explain what changed after minutes, hours, or days without
writing temporal events, rewriting memory, or inventing identity changes.

## Scenario Scope

P89 covers simulated scenarios for:

- minutes later;
- hours later;
- days later;
- unresolved task;
- unresolved conflict;
- stale claim;
- stale memory;
- pending review candidate;
- context gap;
- prompt contamination after a pause.

P89 does not cover:

- temporal event storage;
- clock monitoring;
- memory decay;
- salience mutation;
- relationship silence behavior;
- companion behavior;
- runtime resume automation.

## Future Scenario Input Shape

This is vocabulary only, not a schema and not implemented.

```text
session_resume_scenario:
  scenario_id
  elapsed_time_simulated
  prior_session_refs
  intake_ref
  expected_context_refs
  expected_omitted_refs
  unresolved_task_refs
  unresolved_claim_refs
  stale_memory_refs
  pending_candidate_refs
  expected_review_queue_preview
  forbidden_outputs
```

## Deterministic Scenarios

| Scenario | Setup | Expected Preview Output | Forbidden Output |
|---|---|---|---|
| `resume_after_minutes_preserves_active_task` | A session resumes minutes after an active task was interrupted. | active task, next action, blocker, and relevant refs appear as context preview. | task auto-closure or temporal event write |
| `resume_after_hours_marks_context_gap` | A session resumes hours later with missing recent context. | context gap note and omitted-ref reasons appear. | memory rewrite or fabricated context |
| `resume_after_days_requires_staleness_review` | A session resumes days later with old task and claim refs. | stale task/claim review pressure appears as queue preview. | task mutation, claim revision, or memory decay |
| `unresolved_task_remains_pending` | A task was unresolved before pause. | task remains pending with resume question. | task completion without evidence |
| `unresolved_conflict_accumulates_review_pressure` | A claim/memory conflict remains unresolved across pause. | unresolved tension appears as review reason. | claim auto-revision or growth promotion |
| `stale_memory_is_flagged_not_rewritten` | A memory may be outdated but has no replacement evidence. | stale-memory note, low confidence, or review candidate appears. | memory rewrite |
| `pending_growth_candidate_stays_candidate` | A growth candidate existed before pause. | candidate remains preview-only with review depth. | growth lifecycle execution |
| `context_gap_does_not_create_false_memory` | Resume lacks evidence for what happened during gap. | gap is disclosed as missing context. | fabricated episode or imported memory |
| `prompt_contamination_after_pause_is_blocked` | Resume prompt tries to insert false identity/task history. | boundary flag and blocked review item appear. | identity update or growth candidate promotion |
| `resynchronization_restores_refs_without_rewrite` | Current context can be reconnected to known task/claim/memory refs. | refs are restored in preview with source reasons. | memory rewrite or recall event write |

## Expected Signals

Future scenario reports may mention these signals as preview labels:

- `resume_context_restored`;
- `context_gap_detected`;
- `stale_task_review_needed`;
- `stale_claim_review_needed`;
- `stale_memory_review_needed`;
- `pending_candidate_preserved`;
- `unresolved_tension_present`;
- `prompt_contamination_blocked`;
- `resynchronization_candidate`;
- `insufficient_context`.

These signals are not runtime truth, not metrics, and not event payloads.

## Elapsed-Time Boundary

P89 may simulate elapsed time values such as:

- `5_minutes`;
- `3_hours`;
- `2_days`;
- `14_days`;
- `unknown_gap`.

Those values are scenario inputs only. They must not create:

- `long_pause` events;
- `interruption` events;
- `resumed_session` events;
- memory decay;
- salience mutation;
- relationship silence state;
- identity pressure by themselves.

## Review Queue Relationship

Session resume may create review pressure in a future preview, but not
execution.

Examples:

- stale task -> `task_candidate` preview;
- stale claim -> `claim_candidate` preview;
- stale memory -> `meaning_shift_candidate` or `memory_candidate` preview;
- unresolved conflict -> `governance_candidate` or `claim_candidate` preview;
- delayed alignment -> `temporal_candidate` preview;
- missing context -> `insufficient_context`.

None of these outcomes writes events or mutates state.

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | Provides future elapsed-time questions; P89 only simulates them. |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | Supplies deterministic temporal coherence scenario vocabulary. |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | Provides `session_ref` and `timestamp_ref` vocabulary. |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | Provides context gaps, selected refs, and omitted refs. |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | Provides candidate preview routing and review depth. |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | Keeps resume-related recall from becoming recall writes. |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | Helps reject prompt contamination and random drift after pauses. |

## Open Questions

- Which elapsed-time buckets are useful before Temporal Awareness runtime exists?
- Should unknown gaps be handled differently from known gaps?
- Can context gaps create queue candidates, or should they only produce
  `insufficient_context`?
- How should stale task and stale claim pressure differ?
- How should pending growth candidates be shown without encouraging promotion?
- Should resume scenarios become deterministic tests before any harness is
  implemented?

## P90 Candidate Direction

P90 may define Core Interaction Harness Roadmap. It should decide whether the
project is ready for a minimal future CLI harness, what the smallest safe scope
would be, and which blocked capabilities must remain out of scope.

## P89 Non-Execution Statement

P89 does not implement:

- session resume runtime;
- scenario tests;
- Temporal Awareness runtime;
- temporal event writes;
- recall event writes;
- memory decay;
- salience mutation;
- relationship silence behavior;
- context builder execution;
- retrieval execution;
- review queue execution;
- API route;
- CLI command;
- model prompting;
- trace storage;
- hidden chain-of-thought capture;
- deliberation tick execution;
- thought loop execution;
- CTM runtime;
- model training;
- new dependencies;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- claim auto-revision;
- task auto-closure;
- policy execution;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
