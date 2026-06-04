# Glossary

Chinese version: [GLOSSARY_ZH.md](./GLOSSARY_ZH.md)

P53 keeps this glossary focused on foundation concepts. These definitions do
not create runtime behavior.

## Growth

An evidence-backed, reviewed, meaning-bearing state transition that may affect
future continuity. Growth is not automatic and is not equivalent to memory
promotion, identity mutation, or tone drift.

## Growth Candidate

A possible meaning-bearing state transition identified by growth semantics. It
is not growth and must not promote itself.

## Drift

A change in interpretation, behavior, salience, belief, or identity pressure
across time. Drift can be productive, random, exploratory, conflict-driven, or
identity-threatening.

## Productive Drift

Drift with evidence and bounded review value. Productive drift may become a
growth candidate review object, but it still does not become growth by itself.

## Random Drift

Unsupported change without enough evidence or state context. Random drift should
be rejected or marked insufficient context.

## Meaning Shift

The interpretive change between encoded memory and recalled memory state. P51
requires evidence for `reinforced`, `weakened`, `reinterpreted`, and
`conflicted` shifts.

## Recall State

The state from which a memory is recalled: task context, claim context, retrieval
reason, active identity anchors, and future temporal fields. Recall state can
change what a memory means.

## Encoding State

The state in which a memory was originally recorded: source event, timestamp,
active task, active claims, identity anchors, confidence, salience, privacy
scope, and state version.

## Identity-Threatening Drift

A drift signal that pressures Identity Core continuity or attempts identity
overwrite. It requires high-gate review and must not mutate Identity Core
automatically.

## Review-Only

A non-executing artifact or decision mode. Review-only objects may record,
summarize, rank, route, or request evidence, but they do not mutate identity,
rewrite memory, execute policy, compact events, or promote growth.

## Growth Candidate Review

A review-only governance object for inspecting a growth candidate. In P51 it is
represented by `growth_candidate_review_v0.1` and references source events,
related memories, related claims, related tasks, encoding state, recall state,
meaning shift, evidence, rejection reasons, risk level, and review gate.

## Governance Surface

A cross-layer review surface that can reference Memory Layer, Claim Graph, Task
Hub, Identity Gate, and event evidence without belonging to any single layer.
P51 recommends placing `growth_candidate_review` here.

## Temporal Awareness

A future direction, not a P53 implementation. Principle: time is not only
metadata; time is part of subject state transition.
