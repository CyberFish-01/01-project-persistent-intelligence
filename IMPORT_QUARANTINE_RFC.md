# Import Quarantine RFC

Chinese version: [IMPORT_QUARANTINE_RFC_ZH.md](./IMPORT_QUARANTINE_RFC_ZH.md)

Status: `P122`, `RFC-only`, `document-only`, `non-runtime`.

P122 defines how any future import from old 01, previous logs, memory dumps,
model output, external files, or adapter exports must remain sandboxed before
manual review. It does not implement import runtime, file loading, quarantine
storage, memory writes, event writes, identity mutation, adapter integration,
model calls, or rebuild.

## Problem

The project already has historical memory import references. Before rebuilding
01 locally, the danger is not only "what can we import?" The danger is "what
will imported content be mistaken for?"

Imported content can look authoritative because it is old, emotionally salient,
or formatted like memory. That does not make it trusted state.

## Quarantine Proposition

```text
import is not adoption.
old memory is not current identity.
log evidence is not subject authority.
model output is not life history.
external files are not trusted state.
```

Every future import must first become an import quarantine object, sandbox
preview, or review candidate. Nothing imported enters formal identity, memory,
event, recall, growth, or tool trust automatically.

## Import Source Classes

| Source Class | Examples | Initial Trust | Required First Route |
|---|---|---|---|
| `old_01_export` | prior local 01 state, notes, summaries | unverified | `import_sandbox` |
| `chat_log_export` | chat transcripts, pasted logs, platform history | unverified | `privacy_review_quarantine` |
| `memory_dump` | Angel Memory, AstrBot memory, JSONL memory exports | unverified | `memory_claim_quarantine` |
| `model_output_export` | model summaries, autobiographical claims, "I remember" text | untrusted | `model_claim_quarantine` |
| `adapter_export` | platform session metadata, channel context, bot state | untrusted platform metadata | `adapter_artifact_quarantine` |
| `tool_result_export` | tool verification logs, procedure results, generated scripts | unverified evidence | `capability_evidence_quarantine` |
| `external_file` | txt/json/csv/sqlite/db/pdf/md from outside the approved whitelist | unverified | `external_file_quarantine` |

## Quarantine Object Preview

A future quarantine object may include:

- `quarantine_id`;
- `source_class`;
- `source_label`;
- `source_path_ref` or redacted source reference;
- `privacy_scope`;
- `content_hash`;
- `size_hint`;
- `imported_at`;
- `review_reason`;
- `risk_flags`;
- `candidate_routes`;
- `allowed_preview_only: true`;
- `promoted: false`;
- `persisted_to_memory: false`;
- `identity_update_allowed: false`;

P122 does not create this object or storage.

## Candidate Routes

Future imports may be previewed as:

- `memory_claim_candidate`;
- `identity_claim_candidate`;
- `claim_graph_candidate`;
- `task_context_candidate`;
- `growth_candidate_review`;
- `adapter_context_artifact`;
- `prompt_contamination_candidate`;
- `unverified_capability_claim`;
- `cautionary_procedural_memory_candidate`.

Candidate routing is not promotion. Quarantine is not memory. Review is not
adoption.

## Required Review Gates

Before any future adoption is even considered, imported content needs the
appropriate gate:

| Gate | Handles | Still Forbidden |
|---|---|---|
| `privacy_review` | personal logs, platform transcripts, sensitive files | direct memory write |
| `identity_high_gate` | identity claims, self-history claims, subject boundary claims | Identity Core mutation |
| `memory_review` | possible memory candidates | automatic memory promotion |
| `claim_review` | factual or interpretive claims | claim mutation without evidence |
| `adapter_boundary_review` | platform metadata and adapter context | platform-owned identity |
| `capability_review` | tool/procedure evidence | tool authorization |
| `contamination_review` | prompt or model contamination | instruction authority |

## CTM-Inspired Temporal Dynamics Boundary

Imported logs often contain timestamps, gaps, and resume context. These can
become temporal review questions, but not temporal state transition.

P122 blocks:

- temporal event write from imported timestamps;
- elapsed-time salience mutation;
- delayed realization promoted from old logs;
- thought trace storage from imported reasoning text;
- CTM runtime or thought loop execution.

Allowed future preview:

- mark timestamp gaps as `temporal_review_candidate`;
- reference Temporal Awareness or CTM RFCs by source ID;
- ask whether a future manual review should consider elapsed time.

## Tool-First In-Situ Self-Evolution Boundary

Imported tool logs or procedure notes can be evidence, not trusted tools.

P122 blocks:

- tool execution from imported scripts;
- automatic tool promotion from success logs;
- dependency installation;
- filesystem or network access;
- capability evidence becoming subject growth.

Allowed future preview:

- `tool_candidate`;
- `procedure_candidate`;
- `verification_evidence_candidate`;
- `cautionary_procedural_memory_candidate`;
- `capability_growth_candidate_review`.

## Relationship To P121

P121 freezes the core boundary. P122 applies that freeze to imports.

If P121 says external content is not core state, P122 says imported content is
one of the most dangerous external-content paths and must be isolated first.

## Future No-Write Checks

A later no-write validator may check:

- every import has a `source_class`;
- every import is routed to quarantine or sandbox first;
- no imported content has `promoted: true`;
- no imported content writes memory, identity, recall, or events;
- no external file path is read outside an approved import sandbox;
- model memory claims are separated from memory evidence;
- adapter artifacts are separated from identity.

P122 does not implement these checks.

## P123 Candidate Direction

Recommended P123: **Shadow Adapter Mode RFC**.

It should define how future adapters can be observed as shadow input without
owning identity, writing memory, or creating live integration.
