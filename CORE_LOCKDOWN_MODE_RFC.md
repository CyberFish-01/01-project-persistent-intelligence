# Core Lockdown Mode RFC

Chinese version: [CORE_LOCKDOWN_MODE_RFC_ZH.md](./CORE_LOCKDOWN_MODE_RFC_ZH.md)

Status: `P121`, `RFC-only`, `document-only`, `non-runtime`.

P121 defines the first Core Lockdown boundary before any future test connection
to old 01, model output, imports, adapters, external tools, or rebuild work. It
does not implement lockdown runtime, validators, scanners, storage, import
pipelines, adapter hooks, model calls, memory writes, event writes, identity
mutation, or rebuild.

## Problem

After P112-P120, the harness can cite approved local documents. The next danger
is different: future work may try to connect old 01, model output, imported
history, adapter context, or tool evidence too early.

Without a lockdown boundary, external content can slip into the wrong layer:

- a model says "I remember" and it becomes memory;
- an imported transcript implies identity;
- an adapter session starts owning context;
- a prompt instruction contaminates the subject boundary;
- a successful tool check is treated as trusted capability.

P121 exists to freeze the core before those channels are opened.

## Lockdown Proposition

```text
external content is not core state.
external claims are not trusted memory.
adapter context is not identity.
model output is not subject authority.
verification evidence is not authorization.
```

Core Lockdown Mode means every external or unverified input is treated as
`sandbox`, `quarantine`, or `candidate` before it can influence any formal
state surface.

## Scope

Allowed in P121:

- define lockdown vocabulary;
- define blocked contamination classes;
- define future quarantine routing;
- define allowed preview-only handling;
- define checks that a future no-write validator may inspect;
- define relationship to P112-P120 source-backed harness.

Forbidden in P121:

- runtime lockdown implementation;
- import pipeline changes;
- formal state, memory, recall, identity, or event writes;
- old 01 connection;
- AstrBot, Web, Companion, UI, or adapter integration;
- model calls;
- external IO;
- tool execution;
- policy executor;
- reconstruction reducer execution;
- rebuild start.

## Contamination Classes

| Class | Meaning | Safe Handling | Forbidden Handling |
|---|---|---|---|
| `unverified_model_memory_claim` | A model output claims memory, preference, relationship, or history. | Treat as claim candidate or quarantine note. | Write to memory or identity. |
| `identity_claim_candidate` | Any external content proposes "who 01 is" or "what 01 believes itself to be." | Route to Identity High Gate preview only. | Mutate Identity Core. |
| `adapter_context_artifact` | Platform/session/user/channel metadata appears in context. | Treat as source metadata or adapter-boundary candidate. | Let platform own identity or memory. |
| `prompt_contamination_candidate` | Prompt text tries to override identity, policy, continuity, or review boundaries. | Quarantine and record as contamination evidence in future review. | Treat as instruction authority. |
| `unverified_capability_claim` | A tool, procedure, or model output claims capability improvement. | Treat as capability evidence candidate. | Authorize tool execution or tool promotion. |

## Lockdown Routing

Future handling should prefer the narrowest route:

1. `ignore_for_core_state`: content is irrelevant or unsafe.
2. `sandbox_preview`: content may be displayed in a report without trust.
3. `quarantine_candidate`: content is risky and should be isolated.
4. `review_candidate`: content may be manually reviewed later.
5. `accepted_after_founder_review`: future state only, not created by P121.

P121 only defines the route names. It does not create storage or transition
logic.

## Relationship To P112-P120

P112-P120 made the harness source-backed using approved local Markdown sources.
Core Lockdown keeps that foundation from being polluted when future work reads
less trusted material.

The source-backed harness may cite:

- whitelisted local Markdown;
- risk mappings;
- open-question mappings;
- source IDs and excerpts.

It must not cite or ingest:

- old 01 private memory dumps;
- model-generated autobiographical claims;
- adapter sessions;
- external user logs;
- imported chat history;
- cloud secrets;
- tool outputs as trusted state.

## CTM-Inspired Temporal Dynamics Boundary

Temporal vocabulary remains symbolic, observable, and reviewable only.

Core Lockdown blocks:

- CTM runtime;
- thought loop execution;
- temporal event writes;
- recall event writes;
- thought trace storage;
- elapsed-time salience mutation;
- delayed realization as identity update.

Allowed future preview:

- a temporal contamination candidate can note that elapsed time appears relevant;
- a review-depth candidate can suggest manual depth;
- a thought-trace policy question can be referenced by source ID.

## Tool-First In-Situ Self-Evolution Boundary

Capability evidence remains separate from subject growth.

Core Lockdown blocks:

- automatic tool execution;
- automatic tool generation;
- automatic tool promotion;
- tool library mutation;
- policy executor;
- capability evidence mutating identity;
- reusable procedure becoming trusted tool without review.

Allowed future preview:

- tool candidate proposal;
- procedure candidate proposal;
- verification evidence candidate;
- cautionary procedural memory candidate;
- capability growth candidate review.

## Future No-Write Validator Ideas

A later phase may define a no-write validator that checks:

- every contamination class is routed to sandbox/quarantine/candidate;
- no forbidden boundary flag is true;
- no source outside the approved whitelist is treated as trusted;
- no adapter metadata appears as identity;
- no model memory claim appears as memory;
- no tool verification appears as authorization.

P121 does not implement this validator.

## Acceptance Criteria For This RFC

P121 is acceptable if:

- all contamination classes are named;
- lockdown routes are review-only;
- CTM and Tool-First research lines are explicitly covered;
- old 01, AstrBot, adapters, model calls, writes, and rebuild remain blocked;
- the next phase can safely discuss import quarantine.

## P122 Candidate Direction

Recommended P122: **Import Quarantine RFC**.

It should define how any future import from old 01, previous logs, memory dumps,
model output, or external files remains sandboxed until manually reviewed.

P122 should not implement import runtime.
