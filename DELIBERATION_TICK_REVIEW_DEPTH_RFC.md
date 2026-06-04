# Deliberation Tick / Review Depth RFC

Chinese version: [DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md)

Status: `document-only`, `RFC-only`, `non-runtime`.

P83 defines `deliberation_tick`, `review_depth`, and `risk_level` vocabulary for
future review planning. It does not implement tick runtime, thought loops,
Temporal Awareness runtime, CTM runtime, recall event writes, growth lifecycle,
identity mutation, memory rewrite, companion, UI, AstrBot, or adapter behavior.

## RFC Rule

```text
a deliberation tick is a review planning unit.
a review depth is a risk-calibrated review requirement.
neither is a thought loop or runtime execution.
```

## Problem

P81 and P82 introduced temporal dynamics and temporal coherence vocabulary. The
next boundary problem is review effort: low-risk candidates should not require
heavy deliberation, while identity-threatening or ambiguous candidates should
not pass with shallow review.

Without a vocabulary for review depth, future harness work may either overbuild
governance for every candidate or under-review high-risk changes.

## Core Concepts

| Concept | Definition | Input References | Output | Explicitly Not |
|---|---|---|---|---|
| `deliberation_tick` | A future symbolic unit for one bounded review consideration step. | candidate id, evidence refs, risk level, unresolved questions | tick count or tick plan in preview | thought loop, model trace, runtime step |
| `review_depth` | The required review effort for a candidate. | risk level, evidence ambiguity, identity pressure, boundary flags | `shallow`, `normal`, `deep`, or `blocked` | approval, execution, mutation |
| `risk_level` | A classification of candidate risk before review. | identity pressure, memory rewrite risk, recall write pressure, product pressure | low, medium, high, identity-threatening, blocked | automatic decision |
| `review_depth_budget` | A future cap or target for how many review steps should be considered. | candidate type, risk level, available evidence | maximum planned ticks or "needs human review" | adaptive compute runtime |

## Risk-Level To Review-Depth Mapping

| Risk Level | Example Candidate | Required Review Depth | Boundary |
|---|---|---|---|
| `low` | typo-level context clarification or harmless candidate preview | `shallow` | no mutation, no durable write |
| `medium` | meaning-shift candidate with clear event and memory refs | `normal` | no promotion or lifecycle execution |
| `high` | claim conflict, stale task pressure, or ambiguous memory provenance | `deep` | no claim auto-revision or memory rewrite |
| `identity_threatening` | candidate pressures Identity Core anchors | `deep` plus Identity Gate routing | no identity mutation |
| `blocked` | requests companion behavior, temporal runtime, recall write, or adapter integration | `blocked` | reject or defer; do not execute |

## Deliberation Tick Preview Shape

This is preview vocabulary only, not a schema.

```text
deliberation_tick_preview:
  tick_index
  review_question
  evidence_refs
  unresolved_questions
  boundary_flags
  next_review_need
```

The preview may help a future harness explain why a candidate needs deeper
review. It must not store private model reasoning, hidden chain-of-thought, or
neural internal state.

## Review Depth Inputs

Future review depth planning may inspect:

- source event references;
- encoding_state and recall_state references;
- meaning_shift candidate type;
- claim/task/memory alignment;
- unresolved_tension level;
- temporal_coherence_score as future evaluation signal;
- identity pressure;
- privacy and provenance gaps;
- forbidden boundary flags.

## Review Depth Outputs

Allowed future outputs:

- recommended review depth;
- reason for review depth;
- candidate should remain preview-only;
- candidate should be deferred;
- candidate requires Identity Gate;
- candidate is blocked by boundary.

Forbidden outputs:

- identity update;
- memory rewrite;
- recall event write;
- growth promotion;
- claim auto-revision;
- temporal event write;
- adapter or product action.

## Relationship To Thin Harness

P83 can inform future thin interaction harness previews:

- context preview can show why a candidate requires shallow or deep review;
- candidate preview can expose risk and review-depth reasons;
- review queue preview can sort by review depth without executing lifecycle;
- boundary monitor can mark blocked candidates before runtime work.

P83 does not implement the harness.

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | Introduces deliberation tick and review depth vocabulary as CTM-inspired concepts. |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | Defines future scenarios where review depth should vary by risk. |
| [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | Lifecycle status remains blocked; review depth can only preview review effort. |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | Review depth helps distinguish weak drift from evidence-backed evolution. |
| [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | Boundary flags define when review depth becomes blocked. |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | Risk clusters provide review-depth pressure signals. |

## Open Questions

- Should `review_depth` be manually assigned or computed by future evaluation?
- How many preview ticks are useful before review becomes too heavy?
- Should high-risk candidates always require human review?
- Should `blocked` be a review depth or a separate boundary outcome?
- Can review depth be tested without thought-loop execution?
- How should review depth interact with future thought trace storage policy?

## P84 Candidate Direction

P84 may define Thought Trace Storage Policy. It should keep deliberation tick
previews separate from hidden chain-of-thought, private model reasoning, and
model internal traces.

## P83 Non-Execution Statement

P83 does not implement:

- deliberation tick runtime;
- thought loop execution;
- thought trace storage;
- Temporal Awareness runtime;
- CTM runtime;
- model training;
- new dependencies;
- temporal event writes;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- policy execution;
- reconstruction reducer execution;
- companion, UI, AstrBot, adapter, cloud rollout, or product layer.
