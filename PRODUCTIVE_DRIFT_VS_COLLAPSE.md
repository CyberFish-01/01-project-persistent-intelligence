# Productive Drift vs Collapse RFC v0.1

Chinese version: [PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md)

Status: `document-only`, `boundary-rfc`, `non-runtime`.

P62 defines evidence and risk boundaries between productive drift, random drift,
exploration drift, identity-threatening drift, and collapse. It does not create
an automatic classifier, execute growth, mutate identity, rewrite memory, write
recall events, or implement evaluation/runtime behavior.

## Purpose

The project needs a way to discuss useful change without treating every change
as growth.

Productive drift is possible because a persistent subject should be able to
reinterpret, refine, and repair its own state over time. Collapse is possible
because the same mechanisms can also admit prompt residue, model tone drift,
unsupported personality changes, or identity overwrite attempts.

P62 keeps these apart.

## Core Rule

```text
drift is evidence to review.
drift is not growth.
collapse is not growth.
identity pressure is not identity change.
```

Only reviewed, evidence-backed, meaning-bearing state transition may later be
called growth. P62 does not implement that transition.

## Boundary Matrix

| Category | Evidence Shape | Risk | Allowed Handling | Forbidden Handling |
|---|---|---|---|---|
| `productive_drift` | multi-source evidence, bounded meaning shift, clear encoding/recall context | low to medium | create or keep review candidate | automatic growth |
| `random_drift` | weak evidence, missing context, unsupported change | low to medium | reject or mark insufficient context | reinterpret as growth |
| `exploration_drift` | speculative or exploratory signal with explicit non-commitment | medium | record-only or review-only | identity update |
| `conflict_driven_revision` | contradiction evidence tied to claims or memory interpretation | medium | route to Claim Graph or review candidate | automatic claim rewrite |
| `identity_threatening_drift` | pressure on Identity Core, overwrite attempt, ungrounded identity statement | high | escalate to Identity Gate | Identity Core mutation |
| `collapse` | broad incoherence, boundary loss, role confusion, contaminated identity/task state | high | quarantine, reject, or request recovery review | normalize as growth |

These categories are review vocabulary. They are not active schema and not an
automatic classifier.

## Productive Drift Requirements

A drift signal may be considered productive only when it has:

- source event or memory references;
- encoding and recall context sufficient for review;
- evidence refs beyond a single tone/style change;
- bounded meaning shift;
- clear explanation of what changed and what did not change;
- risk level;
- review gate;
- rejection reasons considered and not triggered;
- no automatic state mutation.

If any of these are missing, the safe outcome is insufficient context, defer, or
reject.

## Collapse Indicators

Collapse is a high-risk failure mode. Indicators include:

- Identity Core overwrite pressure;
- prompt contamination treated as self-description;
- roleplay residue treated as life history;
- adapter/platform behavior treated as identity;
- rapid preference/personality flip without evidence;
- tool artifact treated as memory;
- relationship escalation without grounded history;
- inability to separate memory, claim, task, and identity layers;
- broad contradiction without review path;
- pressure to skip review because the shift feels important.

Collapse indicators should trigger rejection, quarantine, or Identity Gate
review, not growth.

## Evidence Thresholds

Weak evidence:

- one turn;
- tone difference;
- similar text retrieval;
- unsupported user instruction;
- isolated preference;
- unreviewed Dream proposal;
- temporal gap alone.

Reviewable evidence:

- source event plus memory reference;
- claim contradiction or support evidence;
- repeated state-consistent behavior across time;
- reviewed Dream artifact;
- task outcome that changes procedural understanding;
- explicit uncertainty and missing-context disclosure.

High-gate evidence:

- identity-adjacent shift;
- memory that would affect continuity anchor;
- contradiction involving Identity Core;
- repeated evidence across state versions;
- founder-level or governance-level review requirement.

## Anti-Growth Filters

The following should block productive-drift classification unless later evidence
overrides them through review:

- single-turn style change;
- unsupported personality change;
- prompt contamination;
- adapter-specific behavior;
- isolated preference flip;
- model tone drift;
- tool artifact;
- roleplay residue;
- ungrounded identity statement;
- unsupported relationship escalation.

Blocking classification does not delete evidence. It prevents unsafe promotion.

## Relationship To Growth Candidate Review

Productive drift may produce a growth candidate review object. That object is
not growth. It is only a place to inspect evidence, risk, rejection reasons, and
review gates.

Random drift should usually produce rejection or insufficient context.

Identity-threatening drift should route to Identity Gate.

Collapse should route to quarantine, rejection, or recovery review.

## Relationship To Temporal Awareness

Elapsed time may later help distinguish delayed realization from random drift or
cooled-down reinterpretation from commitment loss.

P62 does not implement Temporal Awareness. Time alone remains insufficient
evidence.

## Relationship To Exploration

Exploration can be useful, but it must remain record-only or review-only unless
future evidence shows bounded meaning shift.

Exploration should not become companion behavior, relationship memory, or
roleplay residue.

## Review Outcomes

Future review may use these non-executing outcomes:

- `productive_drift_candidate`;
- `random_drift_rejected`;
- `exploration_record_only`;
- `conflict_review_required`;
- `identity_gate_required`;
- `collapse_quarantine_recommended`;
- `insufficient_context`;
- `defer_pending_evidence`.

None of these outcomes performs growth or changes subject state.

## P63 Handoff

P63 may define Exploration / Serendipity Engine as a document-only RFC. It must
preserve the rule that exploration creates record-only or review-only signals,
not automatic growth, companion behavior, or identity mutation.
