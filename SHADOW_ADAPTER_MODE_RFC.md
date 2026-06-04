# Shadow Adapter Mode RFC

Chinese version: [SHADOW_ADAPTER_MODE_RFC_ZH.md](./SHADOW_ADAPTER_MODE_RFC_ZH.md)

Status: `P123`, `RFC-only`, `document-only`, `non-runtime`.

P123 defines a future shadow adapter boundary before any live adapter
integration. It does not implement adapter code, AstrBot integration, network
access, message ingestion, event writes, memory writes, identity mutation, model
calls, or rebuild.

## Problem

Adapters are useful because they reveal how real platforms shape interaction.
They are dangerous because they can quietly become owners of identity, memory,
session truth, or social behavior.

Before old 01, AstrBot, Telegram, QQ, Web, or any external adapter is connected,
the project needs a mode where adapter input can be observed without becoming
core state.

## Shadow Proposition

```text
shadow adapter observes shape.
shadow adapter does not ingest.
platform context is not identity.
adapter metadata is not memory.
shadow evidence is not integration approval.
```

Shadow Adapter Mode is a future local, no-write, no-network boundary where
adapter-shaped input may be previewed as an artifact but cannot affect formal
state.

## Allowed Future Shadow Inputs

Future shadow adapter previews may include:

- `adapter_id`;
- `platform_name`;
- `channel`;
- `session_id`;
- `actor_id`;
- `timestamp`;
- `message_shape`;
- `metadata_shape`;
- `privacy_scope`;
- `redaction_status`;
- `source_confidence`;
- `boundary_flags`;

P123 does not create this schema or parser.

## Forbidden Live Integration

Shadow mode forbids:

- live network connection;
- platform API calls;
- AstrBot plugin deployment;
- adapter ingest endpoint calls;
- `/v1/adapter/ingest` writes;
- conversation event writes;
- memory writes;
- recall event writes;
- identity mutation;
- Companion behavior;
- UI or product layer;
- model calls;
- tool execution;
- rebuild start.

## Shadow Output

A future shadow report may show:

- platform shape preview;
- adapter ownership warning;
- privacy and redaction warnings;
- candidate routes;
- quarantine route;
- highest relevant boundaries;
- source-backed RFC refs;
- non-execution invariants.

It must not create real review lifecycle, write state, or authorize integration.

## Candidate Routes

Adapter-shaped input can only become:

- `adapter_context_artifact`;
- `prompt_contamination_candidate`;
- `identity_claim_candidate`;
- `memory_claim_candidate`;
- `task_context_candidate`;
- `privacy_review_candidate`;
- `import_quarantine_candidate`.

Candidate is not adoption. Shadow is not integration. Metadata is not memory.

## Relationship To P121-P122

P121 freezes the core boundary. P122 quarantines imports. P123 applies the same
logic to adapters.

If an adapter exports history, it follows P122 import quarantine. If an adapter
streams live context, it remains shadow-only until a later explicit integration
gate exists.

## CTM-Inspired Temporal Dynamics Boundary

Adapters often carry timestamps, pause/resume signals, and session gaps. Shadow
mode may preview those as temporal pressure, but it must not create temporal
state.

Blocked:

- temporal runtime;
- temporal event writes;
- recall event writes;
- elapsed-time salience mutation;
- thought loop execution;
- thought trace storage.

Allowed future preview:

- mark session gap as `temporal_review_candidate`;
- cite Temporal Awareness / CTM RFC source refs;
- route to manual review depth planning.

## Tool-First In-Situ Self-Evolution Boundary

Adapters may report tool results, commands, or automation suggestions. Shadow
mode treats them as unverified capability claims.

Blocked:

- tool execution;
- automatic tool promotion;
- policy executor;
- tool library mutation;
- dependency installation;
- capability evidence mutating identity.

Allowed future preview:

- `unverified_capability_claim`;
- `tool_candidate`;
- `procedure_candidate`;
- `cautionary_procedural_memory_candidate`;
- `capability_review_candidate`.

## Integration Gate Requirements

Before any future live adapter integration is considered, the project needs:

- import quarantine policy accepted;
- contamination scan policy accepted;
- privacy/redaction policy accepted;
- no-write shadow report tested;
- adapter ownership boundaries visible;
- founder approval;
- explicit rollback plan;
- proof that 01 Core owns state and adapters only translate.

P123 does not satisfy those requirements. It only names them.

## P124 Candidate Direction

Recommended P124: **Contamination Scan RFC**.

It should define how prompt contamination, model memory claims, adapter
artifacts, and unverified capability claims are detected as review candidates
without executing a scanner runtime.
