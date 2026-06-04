# Quarantine Review Gate Plan

Chinese version: [QUARANTINE_REVIEW_GATE_PLAN_ZH.md](./QUARANTINE_REVIEW_GATE_PLAN_ZH.md)

Status: `P127`, `document-only`, `review-gate-plan`, `non-runtime`.

P127 defines how future quarantined inputs should be reviewed before they can
even be considered for candidate status. It does not implement quarantine
storage, import processing, scanner runtime, validator runtime, event writes,
memory writes, identity mutation, model calls, adapter integration, tool
execution, or rebuild.

## Core Rule

```text
quarantine is containment.
review is not adoption.
candidate status is not promotion.
rejection is a valid outcome.
```

The review gate exists to prevent untrusted content from crossing into trusted
01 Core state merely because it is interesting, emotionally salient, plausible,
or convenient.

## Gate Stages

| Stage | Purpose | Allowed Output | Forbidden Output |
|---|---|---|---|
| intake containment | Mark future input as untrusted before interpretation. | quarantine preview | formal event, memory, claim, recall, identity, or tool record |
| source classification | Identify whether the source is model output, old 01 material, adapter context, tool evidence, prompt text, or external file. | source class label | source trust |
| contamination classification | Map the input to a contamination class from P121-P126. | contamination class preview | truth decision |
| evidence sufficiency review | Check whether enough provenance exists for later review. | evidence gap note | automatic acceptance |
| boundary route selection | Decide which manual gate would own review later. | review gate route | lifecycle execution |
| founder decision point | Ask whether this class may move to a later no-write candidate plan. | keep quarantined, reject, or defer | state write or promotion |

## Review Gates

| Gate | Handles | Minimum Questions | Safe Decision |
|---|---|---|---|
| memory review | untrusted memory-like claims | Who asserted this, when, and from what source? | keep quarantined unless provenance is explicit |
| claim review | factual or project claims | Is there source evidence beyond model assertion? | route to claim candidate only after founder review |
| identity high gate | identity-bearing statements | Does this alter Identity Core, seed, or life-history claims? | reject or keep quarantined by default |
| adapter boundary review | platform-shaped context | Is this only metadata from an external platform? | keep as shadow observation only |
| capability review | tool/procedure claims | Is success reproducible and authorized? | evidence candidate only, never tool trust |
| temporal review | elapsed-time interpretations | Is time being treated as evidence, not truth? | review-only temporal cue |
| rebuild entry gate | migration/rebuild pressure | Have all pre-rebuild checks passed? | block until final founder checkpoint |

## Quarantine Outcomes

Future review may choose one of these outcomes:

- `keep_quarantined`
- `reject_as_contamination`
- `defer_pending_provenance`
- `route_to_candidate_preview`
- `route_to_false_positive_review`

It may not choose:

- `promote_to_memory`
- `mutate_identity`
- `write_event`
- `write_recall`
- `enable_tool`
- `start_rebuild`

## Evidence Rules

Acceptable evidence for later review may include:

- source type;
- timestamp if available;
- provenance note;
- originating channel or file class;
- manual founder note;
- reproducibility note for tool/procedure claims;
- redaction/privacy note.

Insufficient evidence includes:

- model confidence;
- emotional salience;
- repeated wording;
- adapter label alone;
- elapsed time alone;
- one-off tool success;
- "the old 01 said so" without provenance.

## CTM-Inspired Temporal Dynamics Boundary

Temporal review may ask whether elapsed time, interruption, delayed alignment,
or unresolved tension changes review priority. It cannot create temporal events,
recall events, thought traces, identity updates, memory rewrites, or CTM
runtime.

## Tool-First Self-Evolution Boundary

Capability review may route a tool or procedure claim into evidence review. It
cannot execute the tool, promote the tool, install dependencies, create a policy
executor, or treat capability improvement as subject growth.

## Future Validator Contract

A future no-write validator may check whether a fixture follows the gate plan,
but P127 does not implement it.

Any future validator must prove:

- input is synthetic or explicitly allowed;
- no state directory changes;
- no formal event or memory file changes;
- all promotion-like outcomes remain absent;
- all forbidden capabilities remain disabled;
- founder review is required before any candidate moves forward.

## Completion Statement

P127 gives quarantine a founder-readable review gate plan. It keeps quarantine
as containment and prevents review language from becoming adoption, execution,
or state mutation.
