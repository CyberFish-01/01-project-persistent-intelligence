# Glossary

Chinese version: [GLOSSARY_ZH.md](./GLOSSARY_ZH.md)

P74 keeps this glossary focused on foundation concepts and term boundaries.
These definitions do not create runtime behavior.

## Deduplication Rule

When two terms overlap, prefer the narrower owner:

- use Memory Layer for stored memory objects and retrieval;
- use Stateful Memory for meaning-bearing memory semantics;
- use Claim Graph for claim status and evidence relations;
- use Governance Surface for cross-layer review objects;
- use Event Log and Reconstruction Evidence for auditability and replay
  readiness;
- use RFC terms for future contracts, not implemented mechanisms.

## Growth

An evidence-backed, reviewed, meaning-bearing state transition that may affect
future continuity.

Boundary: growth is not automatic and is not equivalent to memory promotion,
identity mutation, tone drift, or a lifecycle label.

## Growth Candidate

A possible meaning-bearing state transition identified for review by growth
semantics.

Boundary: a growth candidate is not growth; it cannot promote itself and does
not rewrite memory or identity.

## Growth Candidate Review

A review-only governance object for inspecting a growth candidate. In P51 it is
represented by `growth_candidate_review_v0.1` and references source events,
related memories, related claims, related tasks, encoding state, recall state,
meaning shift, evidence, rejection reasons, risk level, and review gate.

Boundary: this object belongs to the Governance Surface, not to Memory Layer,
Claim Graph, Task Hub, or Identity Core alone.

## Growth Candidate Lifecycle

A future review-object housekeeping vocabulary for states such as open,
deferred, archived, quarantined, or rejected.

Boundary: lifecycle status is not subject growth, not memory promotion, and not
an execution engine.

## Drift

A change in interpretation, behavior, salience, belief, or identity pressure
across time. Drift can be productive, random, exploratory, conflict-driven, or
identity-threatening.

Boundary: drift is a signal category; it is not automatically good, bad, or
growth.

## Productive Drift

Drift with evidence, bounded review value, and a plausible relationship to
continuity improvement or meaning clarification.

Boundary: productive drift may become a growth candidate review object, but it
still does not become growth by itself.

## Random Drift

Unsupported change without enough evidence, event context, or state context.

Boundary: random drift should be rejected, marked insufficient context, or routed
for review; it should not be normalized as growth.

## Identity-Threatening Drift

A drift signal that pressures Identity Core continuity or attempts identity
overwrite.

Boundary: it requires high-gate review and must not mutate Identity Core
automatically.

## Collapse

A loss of continuity, coherence, or reviewability where state transfer no longer
preserves the subject history well enough to explain how the current state was
reached.

Boundary: collapse is not a strong form of growth; it is a failure mode or
high-risk condition.

## Meaning Shift

The interpretive change between encoded memory and recalled memory state. P51
requires evidence for `reinforced`, `weakened`, `reinterpreted`, and
`conflicted` shifts.

Boundary: meaning shift is not the same as claim revision. Claim revision changes
claim status; meaning shift explains how a memory's meaning changes under recall.

## Recall State

The state from which a memory is recalled: task context, claim context, retrieval
reason, active identity anchors, and future temporal fields. Recall state can
change what a memory means.

Boundary: recall state is not a recall event write. It can be referenced in
review without adding new events.

## Encoding State

The state in which a memory was originally recorded: source event, timestamp,
active task, active claims, identity anchors, confidence, salience, privacy
scope, and state version.

Boundary: encoding state is a minimal context reference for later interpretation,
not a full snapshot of the subject.

## Recall Event Write Policy

A future policy surface for deciding when a recall should become an auditable
event.

Boundary: the RFC defines questions and constraints only; it does not authorize
recall event writes.

## Stateful Memory

The memory semantics that treat memory as:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

Boundary: Stateful Memory is not a replacement for the Memory Layer. The Memory
Layer stores and retrieves; Stateful Memory explains how remembered meaning
changes across state transitions.

## Review-Only

A non-executing artifact or decision mode. Review-only objects may record,
summarize, rank, route, or request evidence.

Boundary: review-only objects do not mutate identity, rewrite memory, execute
policy, compact events, run reducers, or promote growth.

## Governance Surface

A cross-layer review surface that can reference Memory Layer, Claim Graph, Task
Hub, Identity Gate, and event evidence without belonging to any single layer.
P51 recommends placing `growth_candidate_review` here.

Boundary: Governance Surface owns review objects; it is not a policy executor,
Task Hub substitute, or growth engine.

## Temporal Awareness

A future direction for treating elapsed time as part of subject state transition,
not only metadata.

Boundary: P58 is document-only. Temporal Awareness is not runtime behavior,
temporal event execution, task staleness automation, or memory decay.

## Subject Kernel

The protected continuity nucleus of the subject: identity anchors, core
invariants, and the minimum interpretive frame that must not be casually
overwritten.

Boundary: Subject Kernel is a future boundary concept, not a current runtime
split or identity rewrite.

## World Seed

The evolvable world-facing starting frame around the subject: assumptions,
environment, interests, orientation, and exploratory context.

Boundary: World Seed can evolve under review, but it must not smuggle changes
into the protected Subject Kernel.

## Reconstruction Evidence

The evidence vocabulary and report layer for judging whether subject history is
auditable, replayable, and ready for future reconstruction.

Boundary: reconstruction evidence is not reconstruction execution or state
rebuild.

## Reconstruction Reducer Contract

A future contract for any reducer that might rebuild or project state from
events.

Boundary: the contract names required guarantees and gaps before implementation;
it does not run a reducer.

## Payload / Diff Capture Policy

A future capture policy for deciding when events need payloads, diffs,
snapshots, or reference-only records.

Boundary: the policy describes future requirements and risks; it does not
capture new payloads or mutate event schemas.

## Risk Register

The document-level watchlist for foundation risks such as concept inflation,
premature runtime pressure, boundary drift, and bilingual drift.

Boundary: the risk register records risk; it is not governance execution.
