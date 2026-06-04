# Rebuild Migration Protocol RFC

Chinese version: [REBUILD_MIGRATION_PROTOCOL_RFC_ZH.md](./REBUILD_MIGRATION_PROTOCOL_RFC_ZH.md)

Status: `P147`, `RFC-only`, `document-only`, `non-runtime`.

P147 defines the future protocol for entering a local 01 rebuild and migration
path. It does not start rebuild, read old 01, migrate state, import files, run
reducers, compact events, write state, write memory, mutate identity, connect
adapters, call models, execute tools, or run policy.

## Core Rule

```text
rebuild migration requires entry gates.
entry gate is not rebuild start.
migration plan is not migration execution.
old 01 material is untrusted until reviewed.
```

## Entry Preconditions

Before any local rebuild can start later, the project must have:

- clean git status;
- full tests passing;
- markdown link check passing;
- forbidden pattern search passing;
- push readiness decision if needed;
- pre-rebuild verification report;
- founder checkpoint;
- approved source trust policy;
- import quarantine route;
- no-write validation evidence;
- explicit rebuild scope.

## Migration Source Classes

Future migration may consider source classes only after approval:

- foundation documents;
- current source loader whitelist;
- static reports;
- old 01 code references;
- old 01 memory material;
- adapter artifacts;
- logs or exports;
- founder decision notes.

Old 01 memory material, adapter artifacts, logs, and exports are untrusted by
default and must route through quarantine.

## Migration Non-Goals

Future rebuild migration must not:

- preserve old bugs as identity;
- import old memory as truth;
- treat old adapter context as state;
- treat model output as memory;
- compact events without policy;
- rewrite Identity Core;
- auto-promote growth candidates;
- auto-enable tools;
- connect AstrBot;
- start user product behavior.

## Rebuild Gate Sequence

| Gate | Purpose | Failure Outcome |
|---|---|---|
| foundation gate | Confirm boundaries and phase index are current. | stop |
| source trust gate | Confirm which sources may be read. | stop |
| quarantine gate | Route untrusted material before inspection. | stop or quarantine |
| no-write validation gate | Prove preview tooling does not mutate state. | stop |
| context package gate | Confirm context packs are defined. | stop |
| response boundary gate | Confirm LLM is resource only. | stop |
| verification gate | Run pre-rebuild verification suite. | stop or block |
| founder checkpoint | Founder approves local rebuild start. | stop |

## CTM-Inspired Temporal Boundary

Temporal artifacts may inform rebuild review, but they cannot become runtime
state during migration. No temporal events, recall events, thought traces,
salience mutation, CTM runtime, or identity update may be created by migration.

## Tool-First Boundary

Capability artifacts may inform rebuild review, but they cannot become trusted
tools during migration. No tool execution, tool promotion, dependency
installation, tool library mutation, policy executor, or subject-growth claim may
be created by migration.

## First Allowed Future Write Class

If later approved after verification, the first allowed write class should be a
low-risk local founder/review note, not memory, identity, recall, growth, tool,
adapter, or event migration.

P147 does not approve even that write.

## Stop Conditions

Future migration planning must stop if:

- old 01 source trust is unclear;
- tests fail;
- forbidden active pattern appears;
- state changes during no-write preview;
- adapter pressure appears;
- model call is needed to proceed;
- founder approval is missing;
- rebuild scope is ambiguous.

## Completion Statement

P147 defines rebuild migration as a gated future protocol, not an action. It
prepares the project for final pre-rebuild verification while keeping old 01,
adapters, models, writes, and rebuild execution blocked.
