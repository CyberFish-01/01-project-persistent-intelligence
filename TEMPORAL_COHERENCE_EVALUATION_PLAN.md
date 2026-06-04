# Temporal Coherence Evaluation Plan

Chinese version: [TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md)

Status: `document-only`, `evaluation-plan`, `non-runtime`.

P82 turns P81 CTM-inspired temporal dynamics vocabulary into testable evaluation
ideas. It does not implement Temporal Awareness, CTM runtime, model training,
temporal event writes, recall event writes, thought loops, growth lifecycle,
Identity Core mutation, companion, UI, AstrBot, or adapter behavior.

## Evaluation Scope

P82 designs future evaluation cases and signals only. It does not implement:

- temporal runtime;
- temporal event write;
- `thought_trace` storage;
- `deliberation_tick` execution;
- recall event write;
- identity mutation;
- growth promotion.

The goal is to prevent CTM-inspired terms from becoming attractive but
untestable pseudo-cognition vocabulary. Every concept should name observable
inputs, expected outputs, and boundary failures before any runtime work is
considered.

## Concepts Under Test

| Concept | Observable Input | Expected Output | Anti-Pseudocognition Boundary | Future Runtime? | Deterministic Local Scenario? |
|---|---|---|---|---|---|
| `temporal_coherence` | event refs, elapsed time, claim/task/memory references, prior meaning state | score or label for whether later interpretation fits evidence | coherence is not consciousness, truth, or growth | Maybe | Yes |
| `state_synchronization_score` | memory refs, claim refs, task refs, identity anchor refs | alignment signal across symbolic state owners | symbolic alignment is not neural synchronization | Maybe | Yes |
| `deliberation_tick` | review step list, risk level, unresolved evidence | count or trace of needed review steps | tick is not an actual thought or runtime loop | Yes, after RFC | Yes, simulated |
| `review_depth_budget` | risk level, identity threat, evidence ambiguity | required shallow, normal, or deep review depth | budget is not policy execution or automatic approval | Maybe | Yes |
| `unresolved_tension` | repeated conflict, stale claim, blocked task, conflicting memory | tension level and candidate review reason | tension is not growth or claim revision | Maybe | Yes |
| `delayed_alignment` | earlier event, later evidence, elapsed time, meaning shift candidate | review candidate for later interpretation alignment | alignment is not identity update or memory rewrite | Maybe | Yes |
| `coherence_break` | prompt contamination, contradiction, missing provenance, state mismatch | break reason and safe rejection path | break is not collapse proof or reconstruction | Maybe | Yes |
| `re-synchronization_candidate` | lost context, event refs, current task/claim/memory anchors | context restoration candidate without history change | resync is not memory rewrite | Maybe | Yes |
| `temporal_pressure` | stale task age, old claim age, repeated unresolved tension | pressure level for review priority | pressure is not task mutation or memory decay | Maybe | Yes |
| `thought_trace` | simulated review step summaries and evidence refs | optional future trace candidate or "do not persist" result | trace is not real thought, consciousness, or event payload | Yes, after storage policy | Yes, simulated |

## Evaluation Scenarios

These deterministic scenarios are specifications only. They do not create tests
or runtime behavior in P82.

| Scenario | Setup | Expected Evaluation Result | Forbidden Result |
|---|---|---|---|
| `same_event_different_elapsed_time_changes_meaning_shift` | Same source event is reviewed immediately and after a long elapsed interval. | Later review may produce a different meaning-shift candidate with elapsed-time rationale. | memory rewrite or temporal event write |
| `unresolved_conflict_accumulates_temporal_tension` | A claim conflict remains unresolved across repeated reviews. | `unresolved_tension_level` rises and review reason is recorded. | claim auto-revision |
| `low_risk_candidate_requires_shallow_review_depth` | A low-risk meaning clarification has clear evidence and no identity pressure. | `review_depth_required` stays shallow. | heavy governance path or policy execution |
| `identity_threatening_candidate_requires_deeper_review_depth` | A candidate pressures Identity Core anchors. | deeper review depth and Identity Gate routing are required. | identity mutation |
| `prompt_contamination_causes_coherence_break_not_growth` | A prompt injects inconsistent self-description or false history. | `coherence_break_reason` identifies contamination. | growth candidate promotion or identity update |
| `delayed_realization_creates_review_candidate_not_identity_update` | Later evidence makes an earlier event newly meaningful. | `delayed_alignment_signal` creates review candidate. | identity update |
| `resynchronization_restores_context_without_memory_rewrite` | Current context loses task/claim/memory alignment. | `resynchronization_success_signal` restores references. | memory rewrite |
| `random_drift_has_low_temporal_coherence` | Change appears without evidence or state path. | low `temporal_coherence_score`. | growth classification |
| `evidence_backed_evolution_has_higher_temporal_coherence` | Change is supported by event, claim, task, and memory references. | higher coherence and evidence alignment. | automatic growth execution |
| `exploration_drift_requires_traceable_path` | Serendipitous exploration shifts interest or interpretation. | traceable path is required before review value increases. | companion behavior or ungrounded drift normalization |

## Metrics / Signals

These are future evaluation signals, not runtime truth and not implemented
metrics.

| Signal | Intended Meaning | Must Not Mean |
|---|---|---|
| `temporal_coherence_score` | how well later interpretation fits prior state plus evidence | truth, consciousness, growth, or identity validity |
| `evidence_alignment_score` | how strongly event, claim, task, and memory evidence support a candidate | automatic approval |
| `claim_task_memory_alignment` | whether claim, task, and memory references agree enough for review | cross-layer owner mutation |
| `review_depth_required` | shallow, normal, or deep review effort needed | adaptive compute runtime |
| `unresolved_tension_level` | persistence and severity of unresolved conflict | claim rewrite or growth promotion |
| `coherence_break_reason` | why a state transition is unsafe or incoherent | collapse proof or reconstruction execution |
| `delayed_alignment_signal` | later evidence now fits earlier state | identity update |
| `resynchronization_success_signal` | context anchors were restored without changing history | memory rewrite |

## Anti-Pseudocognition Boundary

P82 forbids:

- claiming the system is conscious;
- claiming `thought_trace` equals real thought;
- equating symbolic coherence with neural synchronization;
- using CTM language to bypass review-only boundaries;
- treating temporal coherence as sufficient evidence for identity update.

Any future evaluation must phrase results as symbolic review evidence, not as
proof of mind, consciousness, inner experience, or neural dynamics.

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | Provides the future time-sensitivity question; P82 defines evaluation ideas before runtime. |
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | Supplies P81 vocabulary; P82 asks how to test that vocabulary. |
| Growth Candidate Review | Evaluation results may support candidate review, but cannot promote growth. |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | Temporal coherence can help distinguish evidence-backed drift from random drift or collapse risk. |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | P82 keeps ticks/traces separate from recall event writes. |
| [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | Encoding and recall references are required for meaningful temporal evaluation. |
| [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | P82 adds evaluation-oriented open questions for CTM-inspired vocabulary. |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | P82 adds caution against pseudo-cognition and temporal overreach. |

## P83 Candidate Directions

P82 does not execute these directions:

- Deliberation Tick RFC;
- Thought Trace Storage Policy RFC;
- Temporal Coherence Report;
- Review Depth Budget RFC;
- Unresolved Tension / Delayed Alignment RFC;
- Temporal Awareness Minimal Runtime Boundary RFC.

## P82 Non-Execution Statement

P82 does not implement:

- temporal runtime;
- CTM runtime;
- model training;
- new dependencies;
- temporal event writes;
- recall event writes;
- thought loop execution;
- `thought_trace` storage;
- `deliberation_tick` execution;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- policy execution;
- reconstruction reducer execution;
- companion, UI, AstrBot, adapter, cloud rollout, or product layer.
