# CTM Temporal Context Pack RFC

Chinese version: [CTM_TEMPORAL_CONTEXT_PACK_RFC_ZH.md](./CTM_TEMPORAL_CONTEXT_PACK_RFC_ZH.md)

Status: `P141`, `RFC-only`, `document-only`, `non-runtime`.

P141 defines the future `temporal_pack` for context packages using
CTM-inspired symbolic vocabulary. It does not implement temporal runtime, CTM
runtime, thought loops, thought-trace storage, recall event writes, temporal
event writes, state mutation, memory mutation, identity mutation, model calls,
adapter integration, tool execution, policy executor, or rebuild.

## Core Rule

```text
temporal_pack is symbolic review context.
symbolic temporal context is not thought execution.
elapsed time is evidence cue, not identity update.
```

## Pack Purpose

The future `temporal_pack` helps a model-as-resource or founder-facing preview
see time-related review pressure without pretending the system has biological
time awareness or neural CTM dynamics.

## Allowed Fields

The pack may include:

- `elapsed_time_since_encoding_hint`
- `elapsed_time_since_last_review_hint`
- `session_gap_hint`
- `interruption_hint`
- `unresolved_tension_note`
- `delayed_alignment_candidate`
- `review_depth_suggestion`
- `temporal_coherence_question`
- `thought_trace_policy_reminder`
- `temporal_boundary_reminder`

## Forbidden Fields

The pack must not include:

- hidden chain-of-thought;
- private model reasoning;
- neural synchronization claim;
- CTM runtime state;
- thought loop state;
- temporal event record;
- recall event record;
- salience mutation;
- identity mutation;
- memory rewrite.

## Temporal Cue Matrix

| Cue | Meaning | Allowed Use | Forbidden Interpretation |
|---|---|---|---|
| elapsed time | Time may affect review framing. | Ask whether meaning should be re-reviewed. | Time automatically changes memory. |
| session gap | A pause may affect context confidence. | Mark context freshness risk. | Pause creates temporal event. |
| unresolved tension | A conflict remains open. | Suggest deeper manual review. | Conflict ages into identity change. |
| delayed alignment | Later evidence may clarify earlier meaning. | Create review candidate only. | Automatically promote growth. |
| review depth | Risk may require more careful review. | Suggest shallow/medium/deep review. | Execute deliberation ticks. |
| thought-trace policy | Trace storage is sensitive. | Remind what cannot be stored. | Capture hidden thoughts. |

## CTM-Inspired Mapping

P141 uses CTM only as inspiration for symbolic review vocabulary:

- temporal dynamics -> state-over-time review cues;
- synchronization -> symbolic coherence question;
- ticks -> review-depth planning language;
- trace -> storage-policy reminder;
- coherence break -> review risk signal.

It does not claim:

- consciousness;
- biological equivalence;
- neural synchronization;
- actual internal thought cycles;
- model training or CTM implementation.

## Boundary Injection

Every `temporal_pack` must include:

- `symbolic_only: true`
- `ctm_runtime_allowed: false`
- `thought_loop_allowed: false`
- `thought_trace_storage_allowed: false`
- `temporal_event_write_allowed: false`
- `recall_event_write_allowed: false`
- `identity_update_allowed: false`

These are planned contract fields, not implemented runtime flags in P141.

## Relationship To Other Packs

The `temporal_pack` should not replace:

- `memory_pack`: memory references still need source backing;
- `claim_pack`: claims still need evidence;
- `boundary_pack`: forbidden actions remain global;
- `response_strategy_pack`: future model instructions still need explicit
  wording.

## Future Test Expectations

If implemented later, tests should verify:

- temporal pack appears only when relevant;
- every cue has a review-only label;
- forbidden temporal actions remain false;
- no thought trace is stored;
- no recall or temporal event is written;
- temporal cues do not mutate identity or memory.

## Completion Statement

P141 gives CTM-inspired temporal dynamics a safe place inside future context
packages: symbolic, visible, bounded, and review-only.
