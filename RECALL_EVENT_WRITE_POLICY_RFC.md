# Recall Event Write Policy RFC v0.1

Chinese version: [RECALL_EVENT_WRITE_POLICY_RFC_ZH.md](./RECALL_EVENT_WRITE_POLICY_RFC_ZH.md)

Status: `document-only`, `non-runtime`, `future-policy-rfc`.

P59 clarifies when a recalled memory might become a future event candidate. It
does not write recall events, add event types, change schemas, add CLI commands,
mutate memory, promote growth candidates, run reducers, or implement Temporal
Awareness.

## Problem

P50 introduced the stateful memory equation:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

It also named possible recall-as-event candidates such as `memory_recalled`,
`memory_reinterpreted`, `memory_reinforced`, `memory_weakened`, and
`memory_conflicted`, while explicitly keeping `writes_recall_events: false`.

P58 then made Temporal Awareness depend on a future recall event write policy.
Without such a policy, the system could accidentally treat ordinary retrieval as
an event, or treat a feeling of changed meaning as automatic growth.

## Core Rule

```text
ordinary retrieval is not an event.
ordinary recall is not a write.
meaning-shifting recall may become a future event candidate only after review.
```

Recall can inform context. Recall can support review. Recall can expose a
possible meaning shift. Recall must not, by itself, rewrite memory, mutate
identity, promote growth, or create durable events.

## Definitions

| Term | Meaning | Write Status |
|---|---|---|
| retrieval | fetching memory or context because it is relevant | never an event |
| ordinary recall | using an existing memory without changed meaning | no write |
| review-worthy recall | recall that exposes evidence of changed meaning | future candidate only |
| meaning-shifting recall | recall that reinforces, weakens, reinterprets, or conflicts with prior meaning | future candidate only |
| identity-adjacent recall | recall that pressures Identity Core continuity | high-gate review only |

These definitions are policy vocabulary. They are not active schema.

## Candidate Future Event Names

The following names remain future-only:

- `memory_recalled`;
- `memory_reinterpreted`;
- `memory_reinforced`;
- `memory_weakened`;
- `memory_conflicted`.

P59 does not create these event types. A later phase must define schema,
payload, validation, replay meaning, and review gates before any write path can
exist.

## Minimum Candidate Threshold

A recall should not even become a future write candidate unless it has all of:

- source memory reference;
- source event reference when available;
- recall reason;
- active task or claim context if relevant;
- explicit meaning shift category;
- evidence for the shift;
- uncertainty level;
- risk level;
- review gate;
- non-execution flag.

If these are missing, the recall should remain context-only or insufficient
context.

## Meaning Shift Categories

Future recall candidates may use the P50/P51 vocabulary:

- reinforced: later context strengthens prior meaning;
- weakened: later context lowers confidence or salience;
- reinterpreted: later evidence changes interpretation without erasing the
  original record;
- conflicted: later evidence creates unresolved contradiction;
- identity-review-required: the shift may pressure Identity Core and requires a
  higher gate.

None of these categories imply automatic growth.

## Required Negative Cases

The following must not create recall events:

- memory retrieved only to fill context;
- memory quoted or summarized without changed meaning;
- repeated retrieval caused by similarity search;
- vague feeling that an old memory matters;
- user instruction to remember everything;
- adapter/platform request to write memory;
- Dream artifact proposing a shift without review;
- temporal gap alone;
- relationship silence alone;
- tone change without evidence.

## Future Write Gate

If a later implementation is approved, a recall event write should require:

1. a reviewed candidate object;
2. explicit source memory and event references;
3. a bounded meaning shift category;
4. evidence references;
5. replay/payload policy compatibility;
6. privacy and sensitivity scope;
7. identity gate escalation when identity-adjacent;
8. validation proving no memory rewrite, identity mutation, or growth promotion.

P59 does not implement this gate. It only records the gate requirement.

## Relationship To Temporal Awareness

Temporal Awareness may later provide elapsed-time evidence, such as
`elapsed_time_since_encoding` or `elapsed_time_since_last_recall`. That evidence
cannot write a recall event by itself.

Elapsed time can become a review signal only if it is attached to source memory,
recall reason, meaning shift, and evidence. Time alone is not evidence.

## Relationship To Growth Candidate Review

A meaning-shifting recall may later feed a growth candidate review object. That
does not make the recall growth.

Growth Candidate Review remains review-only. It can inspect a recall candidate,
reject it, defer it, or ask for evidence in a future lifecycle, but it must not
promote memory or mutate Identity Core automatically.

## Relationship To Event Sourcing

Event Log is an append-only audit trail. A future recall event would need to
explain a real, review-approved state transition or review signal. It must not
be used as a second memory store or a duplicate of every retrieval.

Recall event writes are blocked until a later phase defines payload/diff capture
policy and replay interpretation.

## Safety Boundaries

- Retrieval is not continuity.
- Similarity search is not recall evidence.
- Recall evidence is not memory rewrite.
- Meaning shift is not growth.
- Growth candidate is not growth.
- Review object is not execution.
- Identity-adjacent recall must escalate to Identity Gate.
- Adapter, UI, AstrBot, and platform inputs cannot force recall event writes.

## P60 Handoff

P60 should define Stateful Memory Minimal Encoding Policy before the project
tries to judge meaning-shifting recall in a durable way.

Until then, recall event writes remain forbidden.
