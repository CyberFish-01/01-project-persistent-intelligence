# Read-Only Source Loader Plan

Chinese version: [READ_ONLY_SOURCE_LOADER_PLAN_ZH.md](./READ_ONLY_SOURCE_LOADER_PLAN_ZH.md)

Status: `P114`, `plan`, `document-only`, `non-runtime`.

P114 turns the P113 source inventory into an implementation plan for a minimal
read-only source loader. It does not create `one_core/source_loader.py`, add CLI
commands, read state logs, write state, call models, run retrieval, integrate
adapters, execute tools, or rebuild 01.

## Plan Rule

```text
source loader reads approved local Markdown only.
source refs support preview explanation only.
source loader never writes, never calls external IO, never accepts arbitrary paths.
```

## Minimal Future Module

Future implementation target:

```text
one_core/source_loader.py
```

The module should expose deterministic helpers:

| Function | Purpose | Boundary |
|---|---|---|
| `load_source_inventory(lang="en")` | Return all approved source records for one language. | No user paths, no glob expansion. |
| `load_source_record(source_id, lang="en")` | Return one whitelisted Markdown record. | Reject unknown IDs. |
| `source_refs_for_pressure(pressure_type, lang="en")` | Return the approved source refs mapped to a harness pressure type. | No dynamic search or retrieval. |
| `build_source_inventory_report(lang="en")` | Return a read-only inventory report for CLI/report use. | Report only; no state read. |
| `render_source_inventory_report(report, output_format)` | Render Markdown or JSON. | Output formatting only. |

## Source Record Shape

Each source record should contain:

```yaml
source_id: string
path: string
paired_path: string
lang: en|zh
class: foundation_status|governance_boundary|harness_boundary|temporal_ctm_boundary|capability_boundary|reconstruction_boundary|founder_readability
pressure_types: [string]
research_line: both|CTM-inspired Temporal Dynamics|Tool-First In-Situ Self-Evolution
exists: boolean
heading: string
excerpt: string
read_mode: read_only
source_status: approved_whitelist
missing_reason: string
```

The excerpt should be short, deterministic, and taken from the beginning of the
file after the first heading. It should not summarize with a model.

## Whitelist Rules

The future loader must:

- store the whitelist as constants inside `one_core/source_loader.py`;
- use source IDs, not arbitrary paths, as public input;
- support English and Chinese paired Markdown paths;
- resolve files relative to repository root only;
- reject absolute paths and path traversal;
- read only `.md` files named in the whitelist;
- keep deterministic source ordering;
- return missing records as `exists: false` rather than scanning for
  alternatives.

## Disallowed Reads

The loader must not read:

- `work/01_state`;
- event logs, memories, recalls, dreams, imports, or state JSON/JSONL files;
- imported memory exports;
- adapter directories;
- cloud deployment secrets;
- hidden files;
- credentials or `.env` files;
- generated caches;
- files outside the repository;
- network URLs;
- user-provided file paths.

## Harness Integration Plan

Future P118 can use:

```text
source_refs_for_pressure(report["input_pressure_type"], lang)
```

and add the result to `context_package_preview` as:

- `source_refs_preview`;
- `selected_source_refs`;
- `missing_source_evidence`;
- `source_backing_status`;
- `source_loader_boundaries`.

The harness must keep existing static refs. Source refs explain where the
preview language comes from; they do not become prompt context, memory
activation, or authority.

## CLI Plan

Future P117 command:

```bash
python3 -m one_core.cli harness-source-inventory
```

Allowed options:

- `--lang en|zh`;
- `--format markdown|json`;
- `--output PATH`.

The command may write only the explicit report path. It must not create or
modify the state directory.

## Tests Required For P115-P117

Future tests must prove:

- inventory loads in English and Chinese;
- all whitelist paths are repository-root relative Markdown paths;
- unknown source IDs are rejected;
- pressure mappings return different source refs for temporal, capability,
  adapter, product, reconstruction, growth, observability, and unknown pressure;
- rendered Markdown and JSON include non-execution boundaries;
- CLI output works with `--output`;
- state directory remains unchanged;
- source files remain unchanged;
- forbidden flags remain false or absent as active true flags.

## CTM-Inspired Temporal Dynamics Handling

The loader may expose CTM-related source refs only from whitelisted documents:

- `ctm_temporal_dynamics`;
- `temporal_coherence_eval`;
- `deliberation_tick`;
- `thought_trace_storage`;
- `temporal_awareness`;
- `session_resume`.

It must not infer consciousness, neural synchronization, thought loops, model
training, private reasoning, or temporal runtime.

## Tool-First In-Situ Self-Evolution Handling

The loader may expose capability source refs only from whitelisted documents:

- `tool_first_self_evolution`;
- `capability_evolution_boundary`;
- `deliberation_tick`;
- `risk_register`.

It must not authorize tool execution, automatic tool promotion, tool-library
mutation, policy execution, dependency installation, or subject growth.

## Failure Mode

If a source cannot be read, the loader should report:

```yaml
exists: false
missing_reason: missing_whitelisted_file
```

It should not search nearby files, fetch remote content, or substitute another
source.

## P115 Exit Criteria

P115 should be considered complete only when:

- `one_core/source_loader.py` exists;
- it reads only the P113 whitelist;
- tests prove it is deterministic and no-write;
- no CLI or harness integration is added yet unless explicitly scoped in later
  phases;
- all forbidden pattern searches pass.

## Non-Authorization

P114 is only a plan. It does not implement the source loader, source inventory
CLI, harness source refs, source-backed risks/open questions, state-backed
verification, runtime work, product work, adapter integration, model calls, real
retrieval, state writes, memory writes, recall writes, identity mutation, tool
execution, CTM runtime, temporal runtime, policy execution, rebuild, or external
IO.
