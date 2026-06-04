# Conversation Intake Contract RFC

Chinese version: [CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md](./CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md)

Status: `document-only`, `contract-rfc`, `non-runtime`.

P86 defines a future conversation intake envelope for thin harness previews. It
does not implement intake runtime, adapter ingestion, API routes, CLI commands,
event writes, session policy execution, deduplication, context building, recall
event writes, temporal event writes, trace storage, growth lifecycle, identity
mutation, memory rewrite, UI, AstrBot, adapter, companion, cloud, or product
behavior.

## Contract Rule

```text
conversation intake normalizes an input for review.
conversation intake is not adapter ingest.
conversation intake is not an event write.
conversation intake does not own identity.
```

## Problem

P85 defined a thin interaction harness as a preview-only local testing surface.
The first surface that needs a boundary is conversation intake: before the
system can preview context or candidates, it must know what input is being
considered, where it came from, what privacy constraints apply, and which actor
is involved.

Without a contract, future harness work may accidentally reuse adapter ingest
semantics, write episodes, treat platform sessions as identity, or store full
private payloads. P86 blocks that by defining intake as a normalized preview
envelope, not a durable event path.

## Contract Scope

P86 covers:

- a future local envelope shape for conversation input previews;
- source and actor references;
- session references that do not own identity;
- timestamp and ordering vocabulary;
- privacy and sensitivity flags;
- content references and redaction stance;
- context request hints;
- blocked boundary flags.

P86 does not cover:

- adapter registry;
- adapter session policy;
- HTTP endpoint behavior;
- deduplication index updates;
- episode writes;
- recall event writes;
- context package construction;
- model prompting;
- UI or product interaction.

## Future Envelope Preview Shape

This is contract vocabulary only, not an implemented schema.

```text
conversation_intake_preview:
  intake_id
  actor_ref
  session_ref
  source_ref
  timestamp_ref
  content_ref
  content_summary
  privacy_scope
  sensitivity_flags
  context_request
  boundary_flags
  storage_stance
```

The envelope may summarize the input and point to content references. It must
not require full payload capture, store sensitive plaintext, or write an event.

## Field Boundaries

| Field | Purpose | Allowed Preview | Explicitly Not |
|---|---|---|---|
| `intake_id` | Local preview identity for this intake candidate. | deterministic local id or fixture id | event id or durable write id |
| `actor_ref` | Identifies who or what produced the input. | user ref, system ref, process ref | identity owner or Identity Core field |
| `session_ref` | Groups interaction context. | session id, resumed-session hint, channel hint | persistent identity or relationship memory |
| `source_ref` | Names platform, adapter, file, or local fixture origin. | source channel, platform label, content origin | adapter integration or platform-owned state |
| `timestamp_ref` | Records when the input claims to occur. | timestamp, received time, ordering note | Temporal Awareness runtime |
| `content_ref` | Points to content without requiring full storage. | text ref, redacted content ref, fixture ref | payload capture or memory record |
| `content_summary` | Audit-safe summary for preview. | short sanitized summary | hidden chain-of-thought or full private transcript |
| `privacy_scope` | Indicates who may see or reuse the preview. | private, project, imported, cross-user-blocked | access-control runtime |
| `sensitivity_flags` | Marks risky content classes. | credentials, personal data, injection risk | secret storage or classifier execution |
| `context_request` | Names what kind of context is being asked for. | identity refs, memory refs, task refs, claim refs | context builder execution |
| `boundary_flags` | Records blocked or risky interpretation. | platform identity pressure, recall-write pressure | runtime enforcement |
| `storage_stance` | Says whether preview should remain ephemeral. | ephemeral, report-only, future-review-needed | durable event write |

## Actor And Session Boundary

Conversation intake must preserve:

```text
actor is not identity core.
session is not life history.
platform is not subject owner.
```

An actor or session reference can help route privacy and context previews. It
must not rewrite identity, create relationship memory, promote user-specific
context into core identity, or let a platform define the subject.

## Privacy And Content Boundary

The envelope should prefer references and summaries over full payloads. Full
payload capture remains governed by [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md)
and is not approved here.

Required future questions:

- Can the content be summarized without storing sensitive plaintext?
- Does the content contain credentials, tokens, private keys, or private logs?
- Is the content cross-user or relationship-sensitive?
- Should the preview remain ephemeral?
- Does the input appear to be prompt contamination or identity pressure?

## Relationship To Adapter Protocol

[ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) defines an existing runtime adapter
ingest path. P86 does not modify it and does not require harness work to call
it.

Difference:

| Concern | Adapter Protocol | P86 Intake Contract |
|---|---|---|
| Current status | implemented runtime protocol | document-only future contract |
| Main purpose | translate platform events into 01 Core requests | normalize local harness preview input |
| Write path | may write episodes when not dry-run | no writes |
| Registry/session policy | runtime adapter boundary | referenced only as caution |
| Platform role | adapter translates | source ref only |
| Identity ownership | 01 Core owns state | 01 Core owns state |

## Relationship To Future Harness Surfaces

P86 feeds later preview RFCs:

- P87 Context Package Preview can consume intake references;
- P88 Review Queue Preview can use boundary flags and candidate pressure;
- P89 Session Resume Scenario Plan can simulate `session_ref` and
  `timestamp_ref` gaps;
- P90 Roadmap can decide whether a minimal local harness is safe.

None of those later documents is approved by P86.

## Forbidden Intake Outcomes

Conversation intake must not:

- write an event;
- record an episode;
- update adapter deduplication;
- execute session policy;
- build context;
- execute retrieval;
- create recall events;
- write temporal events;
- store traces;
- store hidden chain-of-thought;
- mutate identity;
- rewrite memory;
- promote growth;
- revise claims;
- close tasks;
- integrate adapters;
- create UI or companion behavior.

## Open Questions

- Should `content_ref` point to fixture text, redacted text, or external source
  metadata in the first future harness?
- Should `privacy_scope` be a fixed vocabulary before any harness exists?
- How much timestamp information is safe without creating Temporal Awareness
  runtime pressure?
- Should `context_request` be explicit, inferred, or absent in the first
  preview?
- Should every intake preview include a boundary monitor result?
- What is the smallest cross-user privacy test before interaction work begins?

## P87 Candidate Direction

P87 may define Context Package Preview RFC. It should explain selected and
omitted identity, memory, claim, task, and governance references without
executing retrieval as continuity, mutating context, or writing activation
traces.

## P86 Non-Execution Statement

P86 does not implement:

- conversation intake runtime;
- API route;
- CLI command;
- adapter ingestion;
- adapter registry changes;
- session policy execution;
- deduplication;
- event writes;
- episode writes;
- context builder execution;
- retrieval execution;
- recall event writes;
- temporal event writes;
- trace storage;
- hidden chain-of-thought capture;
- deliberation tick execution;
- thought loop execution;
- Temporal Awareness runtime;
- CTM runtime;
- model training;
- new dependencies;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- policy execution;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
