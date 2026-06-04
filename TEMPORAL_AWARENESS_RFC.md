# Temporal Awareness RFC v0.1

Chinese version: [TEMPORAL_AWARENESS_RFC_ZH.md](./TEMPORAL_AWARENESS_RFC_ZH.md)

Status: `document-only`, `non-runtime`, `future-direction`.

P58 turns the P51/P53 Temporal Awareness open question into an RFC. It does not
add runtime behavior, schema fields, event types, CLI commands, validation,
evaluation, reducers, adapters, UI, or product behavior.

## Principle

```text
time is not only metadata.
time is part of subject state transition.
```

The current foundation already records timestamps. Temporal Awareness asks a
different question: how does the passage of time change what a subject can
reasonably remember, reinterpret, resume, defer, or treat as stale?

## Problem

P50 defined stateful memory as:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

That model is incomplete if `recall_state` only means the immediate context at
the moment of recall. A memory recalled after five minutes, five days, or five
months may carry different salience, uncertainty, emotional cooling, task
staleness, relationship silence, or unresolved-conflict pressure.

The open problem is not timestamp storage. The open problem is whether elapsed
time should become an explicit input to meaning shift review.

## Non-Goals

P58 does not implement:

- temporal runtime;
- temporal event execution;
- recall event writes;
- memory salience mutation;
- memory rewrite;
- identity mutation;
- growth candidate lifecycle;
- reconstruction reducer execution;
- adapter, UI, AstrBot, companion, or relationship feature behavior.

## Candidate Future Vocabulary

The following names are research vocabulary only. They are not current schema
fields and must not be treated as accepted runtime payload.

| Candidate | Future Question |
|---|---|
| `elapsed_time_since_encoding` | How long has passed since the memory was encoded? |
| `elapsed_time_since_last_recall` | How long has passed since the memory was last meaningfully recalled? |
| `last_recall_ref` | Which prior recall, if any, should anchor comparison? |
| `temporal_gap_type` | Is the gap ordinary passage, long pause, interruption, or resumed session? |
| `staleness_hint` | Does the passage of time make a task, claim, or plan less reliable? |
| `silence_interval` | Does a long absence in a relationship or collaboration context matter? |

These candidates should remain outside runtime until a later phase defines write
policy, review gates, and audit requirements.

## Candidate Temporal Events

The following are possible future event candidates, not active event types:

- `long_pause`;
- `interruption`;
- `resumed_session`;
- `unresolved_conflict_aging`;
- `forgotten_but_resurfaced_memory`.

Before any temporal event can be written, the project needs a recall event write
policy and an event payload/diff policy. Otherwise, temporal events could become
unreviewed identity or memory mutation.

## Research Questions

1. How should elapsed time since encoding affect meaning shift?
2. How should elapsed time since last recall affect salience without mutating
   salience automatically?
3. Should a resumed session be represented as an event, a context annotation, a
   review signal, or no durable record?
4. When does task staleness become operationally important enough for Task Hub?
5. When does claim staleness become evidence for Claim Graph review?
6. Can memory decay be represented without rewriting memory?
7. Can relationship silence be represented without implementing a companion or
   social layer?
8. What evidence distinguishes delayed realization from random drift?
9. What evidence distinguishes cooled-down reinterpretation from loss of
   commitment?
10. How should unresolved conflict aging produce review material without
    forcing growth?

## Meaning Shift Examples

Temporal Awareness may later help describe:

- delayed realization: an old event gains meaning after later evidence;
- cooled-down reinterpretation: intensity decreases, but evidence remains;
- unresolved conflict aging: unresolved contradiction becomes more salient over
  time;
- forgotten-but-resurfaced memory: a rarely recalled memory becomes relevant
  again;
- long-term consistency evidence: repeated stability across time supports a
  claim or identity-adjacent review.

These are review candidates only. None of them imply automatic growth.

## Safety Boundaries

- Time alone is not evidence.
- Elapsed time alone cannot mutate Identity Core.
- Elapsed time alone cannot promote memory.
- Elapsed time alone cannot create growth.
- Temporal signals, if implemented later, should request review rather than
  execute state transition.
- Temporal Awareness must stay separate from ordinary event metadata until a
  future accepted contract says otherwise.

## Relationship To Existing Concepts

Event metadata can record timestamps. Temporal Awareness asks how those
timestamps might later become subject-state evidence.

Stateful Memory can describe encoding and recall context. Temporal Awareness
asks whether elapsed time belongs inside future recall-state review.

Claim Graph can review stale or contradicted claims. Temporal Awareness should
only enter Claim Graph when there is a claim-shaped stale belief, not whenever
time passes.

Task Hub can review stale tasks. Temporal Awareness should not make Task Hub own
all governance around time.

Growth Candidate Review can later receive temporal evidence. It must not become
a growth engine.

## Future Acceptance Gates

Before implementation, a later phase must define:

- recall event write policy;
- minimum stateful memory encoding policy;
- temporal review object placement;
- payload/diff capture rules;
- validation invariants;
- evaluation cases that prove no automatic mutation occurs.

## P59 Handoff

P59 should clarify Recall Event Write Policy before any temporal event writes are
considered.

Until then, Temporal Awareness remains an RFC-level future direction.
