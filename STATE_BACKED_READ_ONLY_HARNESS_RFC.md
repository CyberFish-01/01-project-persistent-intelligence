# State-Backed Read-Only Harness RFC

Chinese version: [STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md)

Status: `P112`, `RFC`, `planning`, `document-only`, `non-runtime`.

P112 defines the boundary for a future state-backed read-only harness. It does
not implement a source loader, CLI command, context preview change, state read
execution, retrieval, model call, adapter integration, memory write, recall
write, identity mutation, tool execution, or rebuild.

## Problem

P102-P110 made `harness-dry-run` legible: different inputs now route to
different pressure profiles, candidates, review gates, boundaries, and next
manual steps.

The remaining weakness is that the harness still cannot show whether any
existing project evidence supports the preview. It can say "this looks like
adapter pressure" or "this looks like temporal pressure," but it cannot yet cite
the local documents that define those boundaries.

The next safe frontier is therefore not runtime. It is **read-only source
backing**.

## Definition

State-backed read-only harness means:

```text
read approved local project sources
  -> summarize source refs and gaps
  -> attach source_refs to preview output
  -> keep all candidates preview-only
  -> keep all review gates manual-review-only
  -> write nothing to state, memory, recall, identity, events, tools, or tasks
```

The word `state-backed` does not mean identity state mutation, memory retrieval,
event replay, reducer execution, or context persistence. It only means the
harness can read a narrow whitelist of existing local project artifacts and cite
them in a dry-run report.

## Allowed Sources

The first allowed source class is whitelisted Markdown in the repository root:

- foundation maps and indexes;
- RFCs and policy documents;
- usability reviews;
- roadmaps and summaries;
- open questions and risk registers;
- boundary and glossary documents.

Allowed sources must be explicit by filename. Directory traversal, globbing from
user input, network fetches, adapter exports, cloud files, hidden files, `.env`
files, state JSONL logs, and imported memory dumps are out of scope.

## Allowed Output

Future harness output may add:

- `source_refs_preview`;
- `selected_source_refs`;
- `omitted_source_refs`;
- `missing_source_evidence`;
- `source_backing_status`;
- `source_loader_boundaries`;
- source-derived open questions and risk hints.

These outputs are report fields only. They are not context persistence, prompt
construction, retrieval execution, memory activation, or review lifecycle
creation.

## Non-Execution Invariants

Every future state-backed harness report must continue to assert:

```yaml
read_only_source_backing: true
state_unchanged: true
execution_prohibited: true
identity_core_mutated: false
memory_rewrite_executed: false
recall_mutation_executed: false
growth_engine_executed: false
temporal_event_executed: false
tool_execution_enabled: false
auto_tool_promotion_enabled: false
policy_executor_enabled: false
companion_feature_enabled: false
adapter_integration_required: false
harness_write_enabled: false
external_io_enabled: false
model_call_enabled: false
source_loader_write_enabled: false
rebuild_started: false
```

## CTM-Inspired Temporal Dynamics Boundary

Temporal Dynamics may be represented only as symbolic, observable, reviewable
source refs:

- Temporal Awareness RFC references;
- temporal coherence evaluation references;
- review depth / deliberation tick vocabulary;
- unresolved tension and delayed alignment notes;
- thought trace storage boundary notes.

This RFC does not permit neural CTM claims, model training, real thought loops,
temporal runtime, temporal event writes, hidden chain-of-thought capture, or
automatic deliberation execution.

## Tool-First In-Situ Self-Evolution Boundary

Capability evolution may be represented only as source refs and review objects:

- tool candidate references;
- procedure candidate references;
- verification evidence references;
- procedural memory candidate references;
- capability growth candidate review references.

Capability improvement does not imply subject growth. Tool verification does not
imply authorization. A tool candidate does not enter a tool library. This RFC
does not permit tool execution, automatic tool promotion, policy execution, or
self-modifying runtime.

## Risks

| Risk | Why It Matters | Guardrail |
|---|---|---|
| Source backing becomes retrieval | The project could confuse document citation with continuity. | Use `source_refs_preview`, not memory activation. |
| Whitelist drifts into broad file access | Sensitive files or imported memory could leak into reports. | Explicit filenames only; no user-supplied paths. |
| Report fields become prompt construction | Read-only refs could be mistaken for a model context pack. | No model calls and no prompt generation. |
| Source refs become authority | A cited document may be stale or exploratory. | Include status and missing evidence. |
| State-backed becomes state-mutating | The phrase could invite writes. | All mutation flags stay false/disabled. |

## P113-P120 Candidate Sequence

P112 authorizes planning only. Candidate next phases:

1. P113 Harness Source Inventory.
2. P114 Read-Only Source Loader Plan.
3. P115 Minimal `one_core/source_loader.py` for whitelisted Markdown.
4. P116 Source Loader Safety Hardening.
5. P117 `harness-source-inventory` CLI.
6. P118 Harness context preview source refs.
7. P119 Source-backed risk/open-question mapping.
8. P120 Source-backed usability review.

Each phase must remain no-write, no external IO, no model call, and no state
mutation.

## Non-Authorization

P112 does not authorize P113-P120 implementation automatically. Each phase must
be separately committed and checked. P112 also does not authorize P121, P155,
local 01 rebuild, old 01 connection, AstrBot, adapters, product work, Companion,
formal memory writes, identity mutation, event writes, recall writes, temporal
runtime, CTM runtime, tool execution, policy execution, or automatic roadmap
execution.
