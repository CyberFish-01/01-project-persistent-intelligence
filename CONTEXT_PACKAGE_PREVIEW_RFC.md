# Context Package Preview RFC

Chinese version: [CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md](./CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md)

Status: `document-only`, `RFC-only`, `non-runtime`.

P87 defines a future context package preview surface for a thin interaction
harness. It does not implement context building, retrieval, activation traces,
context package persistence, API routes, CLI commands, model prompting, adapter
integration, recall event writes, temporal event writes, trace storage, growth
lifecycle, identity mutation, memory rewrite, UI, AstrBot, companion, cloud, or
product behavior.

## RFC Rule

```text
a context package preview explains selection.
a context package preview is not retrieval as continuity.
a context package preview is not context mutation.
a context package preview is not an activation trace write.
```

## Problem

P86 defined a future conversation intake envelope. The next harness surface is
context preview: given an intake preview, the system needs a way to explain
which references would be selected, which would be omitted, and why.

The risk is that context preview can be mistaken for continuity itself.
Continuity in this project comes from state transfer, event-sourced history,
identity boundaries, and reviewable state. Retrieval can support a response, but
retrieval alone is not continuity. P87 keeps that boundary explicit.

## Preview Scope

P87 covers future preview vocabulary for:

- selected identity references;
- selected memory references;
- selected claim references;
- selected task references;
- selected governance references;
- source and evidence reasons;
- token budget notes;
- omitted references and omission reasons;
- privacy and sensitivity suppression;
- risk and boundary flags;
- context gap notes.

P87 does not cover:

- retrieval execution;
- Context Builder changes;
- activation trace persistence;
- model prompt construction;
- endpoint behavior;
- adapter dry-run behavior;
- recall writes;
- memory salience mutation.

## Future Preview Shape

This is vocabulary only, not a schema and not implemented.

```text
context_package_preview:
  intake_ref
  package_preview_id
  selection_policy_ref
  selected_refs
  omitted_refs
  source_attribution_summary
  token_budget_note
  privacy_suppression
  risk_flags
  context_gaps
  continuity_boundary_note
```

## Selected Reference Classes

| Reference Class | What It May Preview | Selection Reason | Explicitly Not |
|---|---|---|---|
| identity refs | stable identity anchors or identity memory refs | continuity anchor relevance | Identity Core mutation |
| memory refs | episodic, semantic, imported, archived, or suppressed refs | task relevance, source evidence, privacy-safe availability | memory rewrite or salience mutation |
| claim refs | active claims, conflicts, support/contradiction refs | belief-shaped relevance or unresolved conflict | claim auto-revision |
| task refs | active tasks, next actions, blockers, procedural/cautionary refs | operational continuity | task auto-closure |
| governance refs | review objects, boundary decisions, risk registers, RFC refs | review pressure or blocked boundary | policy execution |
| temporal refs | elapsed-time notes from intake or scenario | future evaluation pressure | Temporal Awareness runtime |
| trace refs | public review summary refs, if future policy allows | audit explanation | hidden reasoning storage |

## Omitted Reference Reasons

Future previews should explain omissions when possible:

- privacy suppressed;
- cross-user boundary;
- archived or quarantined;
- insufficient provenance;
- token budget;
- weak evidence;
- stale or unresolved;
- identity pressure requires gate;
- forbidden boundary;
- not relevant to intake.

Omission is not deletion. Suppression is not memory rewrite. Budget pressure is
not event compaction.

## Token Budget Boundary

Token budget notes may explain why a reference was selected or omitted. They
must not become:

- automatic forgetting;
- memory deletion;
- event compaction;
- salience mutation;
- identity trimming;
- proof that an omitted reference is irrelevant forever.

## Privacy Boundary

Context preview must preserve privacy before usefulness. A preview should be
able to say that a reference exists but is suppressed, or that it cannot even
expose a reference because cross-user or sensitive-source boundaries apply.

Privacy suppression must not be repaired by memory rewrite, payload capture, or
claim revision.

## Continuity Boundary

The preview should include a boundary note:

```text
selected context supports response generation.
selected context does not equal continuity.
continuity depends on state transfer and reviewable history.
```

This prevents a future harness from reducing the project to retrieval-augmented
chat.

## Relationship To Existing Context Builder

The existing project already has Context Builder behavior and `/v1/context`
documentation. P87 does not modify those systems.

P87 only defines how a future harness might preview and explain context
selection before a response or candidate review.

| Existing Capability | P87 Stance |
|---|---|
| State Transfer Package | may be referenced as existing context output, not changed |
| activation traces | not written by P87 |
| source attribution | can inspire preview vocabulary, not new persistence |
| dry-run adapter previews | remain separate adapter behavior |
| context package version | not changed |

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | Intake references provide input to context preview. |
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | P87 defines one surface inside the future harness boundary. |
| [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | Helps judge whether memory refs have enough provenance to preview. |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | Keeps ordinary retrieval and context preview separate from recall writes. |
| [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | Keeps preview references separate from full payload capture. |
| [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | Defines owner boundaries for identity, memory, claims, tasks, and governance. |

## Open Questions

- Should preview output include exact selected text or only references and
  summaries?
- How should token budget be represented without becoming salience mutation?
- Should omitted references be visible when privacy suppression applies?
- How can context preview cite governance refs without becoming policy
  execution?
- How can temporal notes appear without Temporal Awareness runtime?
- Should context gaps create review candidates or remain preview-only?

## P88 Candidate Direction

P88 may define Review Queue Preview RFC. It should explain candidate types,
ordering, review depth, boundary flags, and blocked items without executing
growth lifecycle, claim revision, memory rewrite, recall writes, task closure,
or policy automation.

## P87 Non-Execution Statement

P87 does not implement:

- context builder execution;
- retrieval execution;
- context package persistence;
- activation trace writes;
- source attribution persistence;
- API route;
- CLI command;
- model prompt construction;
- adapter dry-run changes;
- trace storage;
- hidden chain-of-thought capture;
- deliberation tick execution;
- thought loop execution;
- Temporal Awareness runtime;
- CTM runtime;
- model training;
- new dependencies;
- temporal event writes;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- claim auto-revision;
- task auto-closure;
- policy execution;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
