# Growth Candidate Lifecycle RFC v0.1

Chinese version: [GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md)

Status: `document-only`, `non-execution`, `future-lifecycle-rfc`.

P61 defines a future review-object lifecycle vocabulary for
`growth_candidate_review`. It does not execute lifecycle decisions, promote
growth, rewrite memory, mutate identity, write recall events, implement policy
executors, or change runtime behavior.

## Problem

P51 defined Growth Candidate Review as:

```text
Growth candidate is not growth.
It is a review object for a possible meaning-bearing state transition.
```

P53/P57 left one open question: should growth candidate reviews later support
acknowledge, archive, quarantine, or defer decisions?

The risk is that lifecycle language can be mistaken for promotion. P61 prevents
that by defining lifecycle as review-object housekeeping only.

## Core Rule

```text
growth candidate lifecycle manages review object state.
growth candidate lifecycle does not manage subject state.
```

A lifecycle decision can organize, suppress, preserve, or request more evidence
for a candidate. It cannot make the candidate true, promote memory, mutate
Identity Core, create growth, or execute a state transition.

## Lifecycle Vocabulary

The following labels are future review-object states, not current schema:

| State | Meaning | Explicit Non-Meaning |
|---|---|---|
| `open` | candidate awaits review | not growth |
| `acknowledged` | reviewer has seen the candidate and accepts it as worth tracking | not accepted growth |
| `deferred` | review waits for more evidence or a better contract | not rejection and not promotion |
| `archived` | candidate is kept for audit but removed from active review | not memory archive |
| `quarantined` | candidate is isolated because it may be contaminated or risky | not identity change |
| `rejected` | candidate lacks evidence or violates boundaries | not memory deletion |
| `evidence_requested` | candidate needs specific evidence before review can proceed | not schema approval |

These labels must not be connected to automatic actions.

## Allowed Lifecycle Effects

A future lifecycle system may be allowed to:

- record reviewer intent;
- route candidates out of active review;
- preserve audit history;
- request evidence;
- mark insufficient context;
- mark boundary risk;
- reduce review noise;
- explain why a candidate remains unresolved.

These are governance effects only.

## Forbidden Lifecycle Effects

A lifecycle decision must not:

- promote a growth candidate into growth;
- promote memory;
- rewrite memory;
- mutate Identity Core;
- write recall events;
- execute temporal events;
- revise Claim Graph automatically;
- close Task Hub work automatically;
- compact or rewrite events;
- execute a reconstruction reducer;
- create executable policy;
- trigger adapter, UI, AstrBot, companion, or product behavior.

## Minimum Future Lifecycle Record

If implemented later, a lifecycle decision should require:

- `candidate_id`;
- `previous_review_state`;
- `next_review_state`;
- `decision_reason`;
- `evidence_refs`;
- `reviewer_ref` or review authority reference;
- `risk_level`;
- `boundary_flags`;
- `created_at`;
- `execution_prohibited`;
- `subject_state_unchanged`.

P61 does not add this schema. It only records the contract shape a future phase
must satisfy.

## Boundary Flags

A lifecycle decision should explicitly preserve negative flags:

```yaml
promoted: false
memory_rewrite_executed: false
recall_event_written: false
identity_core_mutated: false
growth_engine_executed: false
policy_executor_created: false
subject_state_unchanged: true
```

These flags are RFC vocabulary. They do not create runtime validation in P61.

## Relationship To Growth

Growth remains a separate, higher-gated concept:

- evidence-backed;
- reviewed;
- meaning-bearing;
- state-transition relevant;
- not automatic.

Lifecycle can prepare a candidate for future review, but it cannot perform the
state transition that would make growth real.

## Relationship To Memory Lifecycle

Growth candidate lifecycle is not memory lifecycle.

Archiving a growth candidate review does not archive the memory it references.
Quarantining a growth candidate review does not quarantine the memory it
references. Rejecting a candidate does not delete memory or erase evidence.

## Relationship To Claim Graph

Only claim-shaped evidence belongs in Claim Graph. Lifecycle decisions may refer
to related claims, but they must not revise claims automatically.

If a candidate is rejected because it lacks claim evidence, that is a governance
decision, not a claim revision.

## Relationship To Identity Gate

Identity-adjacent candidates require Identity Gate escalation. A lifecycle
decision can mark `identity_gate_required`, but it cannot perform the identity
decision.

Identity Core remains protected by gate.

## Anti-Growth Rejection Reasons

Future lifecycle review may preserve P51 rejection reasons:

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

These reasons support rejection or quarantine, not automatic repair.

## P62 Handoff

P62 should define Productive Drift vs Collapse boundaries. That work should
decide how evidence, risk, and rejection reasons separate bounded drift from
random drift or identity-threatening collapse.

Until then, lifecycle remains document-only review-object governance.
