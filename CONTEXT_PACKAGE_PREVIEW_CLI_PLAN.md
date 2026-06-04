# Context Package Preview CLI Plan

Chinese version: [CONTEXT_PACKAGE_PREVIEW_CLI_PLAN_ZH.md](./CONTEXT_PACKAGE_PREVIEW_CLI_PLAN_ZH.md)

Status: `P138`, `CLI-plan`, `document-only`, `non-runtime`.

P138 plans a future read-only context package preview CLI. It does not implement
a command, parser, builder, retrieval engine, model call, prompt execution,
state write, memory write, recall write, identity mutation, adapter integration,
tool execution, policy executor, or rebuild.

## Future Command Shape

Possible future command:

```bash
python3 -m one_core.cli context-package-preview
```

Possible future parameters:

- `--input TEXT`
- `--session-id ID`
- `--actor-id ID`
- `--lang en|zh`
- `--format markdown|json`
- `--output PATH`
- `--pressure-type TYPE`
- `--no-write`

P138 does not add this command.

## Output Sections

A future preview should include:

- `package_summary`
- `identity_pack`
- `state_pack`
- `task_pack`
- `claim_pack`
- `memory_pack`
- `boundary_pack`
- `temporal_pack`
- `capability_pack`
- `response_strategy_pack`
- `selected_sources`
- `omitted_sources`
- `risk_flags`
- `non_execution_invariants`

## CLI Boundaries

The future CLI must be:

- local-only;
- deterministic;
- read-only;
- report-output-only;
- source-transparent;
- founder-readable;
- no model call;
- no external IO;
- no adapter integration;
- no formal state mutation;
- no rebuild.

## No-Write Invariants

Future output should explicitly include:

- `context_package_preview_only: true`
- `model_call_enabled: false`
- `external_io_enabled: false`
- `state_unchanged: true`
- `memory_write_allowed: false`
- `recall_write_allowed: false`
- `identity_mutation_allowed: false`
- `tool_execution_allowed: false`
- `adapter_integration_allowed: false`
- `rebuild_allowed: false`

These are planned output fields, not implemented flags in P138.

## Founder-Facing Markdown Shape

The Markdown report should be readable in this order:

1. What this package is for.
2. What sources were selected.
3. What was omitted and why.
4. What boundaries are active.
5. What temporal and capability cues are only review material.
6. What a future model would be asked to do as a resource.
7. What is explicitly not happening.

## JSON Shape

JSON should preserve the same structure as Markdown, so future tests can assert:

- all required packs exist;
- all trust levels are explicit;
- all selected sources have reasons;
- all omitted sources have reasons;
- all forbidden capabilities remain false;
- no package item claims promotion or persistence.

## CTM-Inspired Temporal CLI Boundary

The future `temporal_pack` preview may show elapsed time, interruption, delayed
alignment, unresolved tension, and review depth suggestions. The CLI must not
execute ticks, write thought traces, create temporal events, create recall
events, or claim consciousness.

## Tool-First CLI Boundary

The future `capability_pack` preview may show tool candidates, procedure
candidates, verification evidence, and review routes. The CLI must not execute
tools, authorize tools, promote tools, install dependencies, or mutate any tool
library.

## Future Tests Plan

If implementation is later approved, tests should verify:

- CLI runs in Markdown and JSON;
- zh output uses founder-facing labels;
- all nine required packs appear;
- selected and omitted sources are present;
- forbidden capabilities are disabled;
- no formal state changes;
- output file is written only when requested;
- repeated input is deterministic;
- invalid input fails closed.

## Completion Statement

P138 plans the context package preview CLI without implementing it. It turns
P137's package contract into a future local, deterministic, read-only report
surface while keeping model calls and writes blocked.
