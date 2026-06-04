# Glossary

## Growth Candidate

A possible meaning-bearing state transition identified by growth semantics.
It is not growth and must not promote itself.

## Growth Candidate Review

A review-only governance object for inspecting a growth candidate. In P51 it is
represented by `growth_candidate_review_v0.1` and references source events,
related memories, related claims, related tasks, encoding state, recall state,
meaning shift, evidence, rejection reasons, risk level, and review gate.

## Governance Surface

A review layer that can reference Memory Layer, Claim Graph, Task Hub, Identity
Gate, and event evidence without belonging to any single layer. P51 recommends
placing `growth_candidate_review` here.

## Meaning Shift

The interpretive change between an encoded memory and a recalled memory state.
P51 requires evidence for `reinforced`, `weakened`, `reinterpreted`, and
`conflicted` shifts. A meaning shift without `evidence_refs` is `random_drift`
or `insufficient_context`, not growth.

## Anti-Growth Filter

A rejection filter for signals that must not count as growth: single-turn style
change, unsupported personality change, prompt contamination, adapter-specific
behavior, isolated preference flip, model tone drift, tool artifact, roleplay
residue, ungrounded identity statement, and unsupported relationship escalation.

## Temporal Awareness

A P52/P53 future direction, not a P51 implementation. Principle: time is not
only metadata; time is part of subject state transition.
