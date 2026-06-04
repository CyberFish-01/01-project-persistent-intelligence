# Stateful Memory Encoding Policy v0.1

Chinese version: [STATEFUL_MEMORY_ENCODING_POLICY_ZH.md](./STATEFUL_MEMORY_ENCODING_POLICY_ZH.md)

Status: `document-only`, `policy`, `non-runtime`.

P60 defines the minimum safe encoding references needed before the project can
review stateful memory or meaning shift claims. It does not create a new memory
store, change schemas, write recall events, rewrite memory, mutate identity,
promote growth, execute reducers, or implement Temporal Awareness.

## Purpose

P50 introduced:

```text
memory = event + encoding_state + recall_state + meaning_shift
```

P59 clarified that recall event writes remain forbidden. P60 answers the next
foundation question: what must be known about the original encoding context
before any later recall state or meaning shift can be reviewed safely?

Without a minimum encoding policy, the system may over-interpret weak memory
records, mistake missing context for growth, or treat retrieval artifacts as
continuity evidence.

## Core Rule

```text
missing encoding context weakens interpretation.
missing encoding context does not authorize repair by rewrite.
insufficient encoding context must produce insufficient-context review.
```

Stateful Memory is an interpretation model. It is not a new storage layer and it
does not replace Memory Layer provenance.

## Required Minimum Encoding References

A stateful memory review should require these references whenever available:

| Field | Purpose | If Missing |
|---|---|---|
| `source_memory_ref` | identifies the memory record being interpreted | cannot review as stateful memory |
| `source_event_ref` | anchors memory to the event that produced or imported it | mark weak provenance |
| `encoded_at` | establishes original time of encoding | mark temporal gap unknown |
| `encoding_operation` | explains whether the memory was imported, episodic, semantic, identity, procedural, or archived | mark origin ambiguous |
| `state_version_ref` | links encoding to state version or snapshot boundary | mark reconstruction weak |
| `provenance_ref` | records source system, adapter, import, or user/session origin | mark source weak |

These references are policy requirements for review quality. P60 does not add
them as active schema fields.

## Conditional Encoding Context

These references are needed when they are relevant to the memory:

| Context | Needed When | Review Value |
|---|---|---|
| `active_task_refs` | memory was encoded during ongoing work | prevents task-free reinterpretation |
| `active_claim_refs` | memory touched beliefs, decisions, or contradictions | separates meaning shift from claim revision |
| `identity_anchor_refs` | memory was identity-adjacent | triggers Identity Gate review |
| `privacy_scope` | memory may be sensitive or imported from external logs | prevents unsafe review or exposure |
| `salience_at_encoding` | salience existed at encoding time | distinguishes later salience change |
| `confidence_at_encoding` | confidence existed at encoding time | distinguishes later confidence change |
| `dream_artifact_ref` | memory came from Dream proposal or consolidation | preserves Dream-proposes boundary |
| `review_decision_ref` | memory came from a reviewed candidate | separates reviewed state from raw proposal |

If a conditional context is relevant but absent, the review should downgrade to
weak evidence or insufficient context.

## Recall-State Dependency

Recall state must not be judged in isolation. A later recall review should
compare:

- what was known at encoding time;
- why the memory is being recalled now;
- which task, claim, identity, or governance context is active now;
- what evidence supports the alleged meaning shift;
- what remains unknown because encoding context is missing.

If encoding context is too weak, the safe output is `insufficient_context`, not
growth, identity change, claim revision, or memory promotion.

## Meaning Shift Eligibility

A meaning shift can be reviewed only when:

1. the source memory is identified;
2. the encoding context is sufficiently anchored;
3. the recall reason is explicit;
4. evidence references explain the shift;
5. missing context is declared;
6. risk level and review gate are assigned.

If these conditions are not met, the shift should be rejected, deferred, or
marked insufficient context.

## Future-Only Fields

The following remain future-only and are not implemented by P60:

- `elapsed_time_since_encoding`;
- `elapsed_time_since_last_recall`;
- `last_recall_ref`;
- `temporal_gap_type`;
- `staleness_hint`;
- `silence_interval`;
- recall event payload;
- growth lifecycle decision.

These fields depend on future policy and runtime work. P60 only names their
relationship to encoding quality.

## Negative Cases

The system must not:

- infer encoding context from similar text alone;
- backfill missing encoding fields by rewriting memory;
- treat imported logs as identity memory without review;
- treat Dream proposals as accepted semantic memory;
- treat recall state as more authoritative than encoding state;
- turn every retrieved memory into a stateful memory review;
- treat weak provenance as proof of productive drift;
- promote memory because encoding context is incomplete;
- mutate Identity Core because an old memory feels newly important.

## Relationship To Existing Layers

Memory Layer owns storage, provenance, lifecycle, sensitivity, and retrieval
eligibility.

Stateful Memory owns interpretation vocabulary for encoding, recall, and meaning
shift.

Claim Graph receives only claim-shaped shifts with evidence.

Task Hub receives only operationally relevant task context and stale-work
signals.

Identity Gate receives identity-adjacent pressure, but P60 does not allow
automatic identity mutation.

Governance Surface can host future review objects when memory, claim, task,
identity, and event evidence cross layers.

## Review Output Guidance

A future review report should prefer one of these non-executing outcomes:

- sufficient encoding context for review;
- weak provenance;
- missing temporal anchor;
- missing task/claim/identity context;
- insufficient context;
- identity-gate-required;
- defer pending evidence.

None of these outcomes changes state by itself.

## P61 Handoff

P61 may define a Growth Candidate Lifecycle RFC. It must preserve the rule that
a lifecycle decision is not promotion, not memory rewrite, and not identity
mutation.

Until then, stateful memory encoding policy remains a document-level review
policy.
