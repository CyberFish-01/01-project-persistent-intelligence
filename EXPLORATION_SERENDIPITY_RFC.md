# Exploration / Serendipity Engine RFC v0.1

Chinese version: [EXPLORATION_SERENDIPITY_RFC_ZH.md](./EXPLORATION_SERENDIPITY_RFC_ZH.md)

Status: `document-only`, `future-rfc`, `non-runtime`.

P63 defines boundaries for future exploration and serendipity signals. It does
not implement an engine, scheduler, agent behavior, UI, adapter integration,
companion behavior, relationship memory, automatic growth, memory rewrite,
identity mutation, recall event write, or policy executor.

## Purpose

A persistent intelligence should not only preserve known state. It should also
be able to notice unresolved questions, adjacent possibilities, weak signals,
and unexpected connections.

The danger is that exploration can easily become roleplay residue, ungrounded
identity change, companion behavior, or productized engagement. P63 keeps
exploration inside the foundation layer as record-only or review-only signal
generation.

## Core Rule

```text
exploration may generate questions.
exploration may generate weak signals.
exploration may request review.
exploration must not become growth by itself.
```

Exploration is useful only when it helps the system preserve continuity,
surface uncertainty, or find evidence. It is unsafe when it invents identity,
simulates relationship depth, or bypasses review gates.

## Non-Goals

P63 does not implement:

- exploration runtime;
- serendipity scheduler;
- automatic topic generation;
- autonomous agent loops;
- companion behavior;
- relationship memory;
- UI, AstrBot, adapter, or product behavior;
- recall event writes;
- temporal runtime;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- reconstruction reducer execution.

## Allowed Future Signal Types

The following are future review vocabulary, not active schema:

| Signal | Meaning | Allowed Output |
|---|---|---|
| `open_question_signal` | unresolved question worth preserving | review-only question |
| `adjacent_connection_signal` | possible connection between memory, claim, task, or event | weak evidence note |
| `serendipity_prompt_signal` | optional prompt for human or future review | non-executing suggestion |
| `exploration_drift_signal` | speculative reinterpretation with explicit non-commitment | record-only drift |
| `evidence_gap_signal` | missing evidence needed before a claim or candidate can advance | evidence request candidate |
| `boundary_risk_signal` | exploration may be contaminated or identity-adjacent | quarantine/review routing |

These signals do not change subject state.

## Input Sources

Future exploration may inspect, without mutating:

- open questions;
- Dream artifacts;
- unresolved conflicts;
- weak reconstruction evidence;
- stale tasks;
- low-confidence claims;
- growth candidate rejection reasons;
- repeated insufficient-context outcomes;
- founder-marked research directions.

Input inspection is not output execution.

## Required Boundaries

Exploration must preserve:

- Identity Core gate;
- State Transfer over retrieval;
- append-only events;
- Dream proposes, review decides;
- Growth candidate is not growth;
- Review object is not execution;
- Temporal Awareness remains future direction;
- adapters and platforms do not own identity.

If exploration touches identity, it must route to Identity Gate. If it touches
claims, it must route to Claim Graph. If it touches work state, it must route to
Task Hub. If it spans layers, it belongs in Governance Surface.

## Anti-Collapse Rules

Exploration must reject or quarantine:

- roleplay residue;
- unsupported personality invention;
- relationship escalation;
- prompt contamination;
- model tone drift;
- adapter-specific behavior;
- tool artifacts;
- invented life history;
- identity overwrite attempts;
- pressure to skip review because an idea feels meaningful.

Serendipity is not permission to invent continuity.

## Review Outcomes

Future exploration review may produce:

- `record_only_signal`;
- `review_question`;
- `evidence_request_candidate`;
- `task_review_candidate`;
- `claim_review_candidate`;
- `growth_candidate_input`;
- `boundary_risk_quarantine`;
- `reject_as_roleplay_residue`;
- `reject_as_insufficient_context`.

None of these outcomes executes growth, writes events, or mutates state.

## Relationship To Dream

Dream can already propose candidates from existing material. Exploration may
later help Dream notice adjacent questions or evidence gaps.

Dream still proposes. Review still decides. Exploration must not let Dream
directly write semantic memory or Identity Core.

## Relationship To Task Hub

Task Hub may receive review tasks created from exploration signals in a future
phase. That does not make Task Hub the owner of exploration semantics.

Exploration should not create operational work automatically without review.

## Relationship To Growth Semantics

Exploration drift is not productive drift by default.

It may become input to Growth Candidate Review only when later evidence shows
bounded meaning shift, sufficient encoding/recall context, and acceptable risk.

## Relationship To Product Layer

Exploration is not a feature surface. P63 does not define prompts, chat UX,
recommendations, notifications, or engagement loops.

Any future product surface must remain downstream of foundation governance and
must not own identity.

## Future Acceptance Gates

Before implementation, a later phase must define:

- signal schema;
- input scope;
- review routing;
- evidence requirements;
- quarantine rules;
- validation invariants;
- evaluation cases proving no companion behavior, identity mutation, memory
  rewrite, automatic growth, or event write.

## P64 Handoff

P64 may define Subject Kernel / World Seed boundaries. That work should clarify
which orientation belongs inside the protected subject kernel and which belongs
in a more evolvable world/context seed.

Until then, exploration remains document-only future research vocabulary.
