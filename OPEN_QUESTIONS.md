# Open Questions

Chinese version: [OPEN_QUESTIONS_ZH.md](./OPEN_QUESTIONS_ZH.md)

P53 records open foundation questions after P51. These are future directions,
not active implementation instructions.

## Temporal Awareness

Question: how should elapsed time become part of subject state transition?

Subquestions:

- How should `elapsed_time_since_encoding` affect meaning shift?
- How should `elapsed_time_since_last_recall` affect salience?
- Should `long_pause`, `interruption`, and `resumed_session` become temporal events?
- Should task staleness, claim staleness, memory decay, and relationship silence
  enter temporal state?

Do not implement in P53.

## Growth Candidate Lifecycle

Question: should `growth_candidate_review` later support acknowledge, archive,
quarantine, or defer decisions?

Risk: lifecycle can be mistaken for promotion. It must remain review-only unless
a separate future phase explicitly defines promotion boundaries.

## Recall Event Write Policy

Question: when is recall meaningful enough to become an event candidate?

Boundary: ordinary retrieval should not write events. Only meaning-shifting
recall may become a future candidate.

## Stateful Memory Minimal Encoding Policy

Question: what is the minimum safe `encoding_state` required for stateful memory?

Candidate fields:

- source event id;
- timestamp;
- active task ids;
- active claim ids;
- identity anchor refs;
- privacy scope;
- salience/confidence.

## Reconstruction Reducer Contract

Question: what contract would allow event records to rebuild object-level state?

Needed:

- reducer input schema;
- target path identity;
- payload/diff requirements;
- validation metadata;
- rollback and seed/pre-event references.

Do not execute reducers until the contract is reviewed.

## Payload / Diff Capture Policy

Question: which state paths require full payload, object diff, snapshot link, or
reference-only treatment?

Risk: capture policy can become accidental event schema mutation. Keep it
review-only until explicitly implemented.

## Subject Kernel / World Seed Direction

Question: should Identity Seed be split into a smaller subject kernel plus a
world seed?

Purpose: keep Identity Core small while allowing world/context orientation to
evolve without rewriting identity.

## Exploration / Serendipity Engine

Question: how can the system support exploration without creating collapse,
roleplay residue, or ungrounded identity changes?

Boundary: exploration should create record-only or review-only signals, not
automatic growth.

## Productive Drift vs Collapse

Question: how should the system distinguish evidence-backed productive drift
from random drift, identity-threatening drift, or collapse?

Needed:

- evidence threshold;
- risk level;
- review gate;
- anti-growth rejection reasons;
- temporal aging policy.
