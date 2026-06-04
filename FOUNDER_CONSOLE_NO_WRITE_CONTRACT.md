# Founder Console No-Write Contract

Chinese version: [FOUNDER_CONSOLE_NO_WRITE_CONTRACT_ZH.md](./FOUNDER_CONSOLE_NO_WRITE_CONTRACT_ZH.md)

Status: `P133`, `contract`, `document-only`, `non-runtime`.

P133 defines the no-write contract for a future Thin Founder Console. It does
not implement a console, command, validator, Web UI, Companion, adapter, model
call, tool execution, state write, memory write, recall write, identity
mutation, policy executor, or rebuild.

## Contract Rule

```text
the console may produce reports.
the console may not change core state.
report output is not memory.
preview output is not event.
```

## Allowed Reads

A future console may read only explicitly approved local sources:

- foundation Markdown documents;
- RFC and review Markdown documents;
- existing read-only report output when explicitly selected;
- source loader whitelist records;
- deterministic harness dry-run output generated in the same no-write session.

It may not read:

- old 01 material;
- external network sources;
- adapter exports;
- private chat logs;
- credentials or environment files;
- unapproved local directories;
- formal state directories unless a later phase explicitly approves read-only
  state inspection.

## Allowed Writes

The only possible write in a future console is an explicitly requested report
file.

That report file must:

- be founder-requested;
- be outside formal state/event/memory/identity stores;
- be marked report-only;
- contain non-execution invariants;
- not become an input to automatic promotion;
- not create candidate lifecycle state.

## Forbidden Writes

The console must not write:

- `state.json`;
- `episodes.jsonl`;
- `dreams.jsonl`;
- `imports.jsonl`;
- formal event logs;
- memory stores;
- recall events;
- identity files;
- task state;
- claim graph state;
- growth candidate lifecycle files;
- tool library files;
- adapter queues;
- quarantine storage;
- rebuild migration files.

## Required Invariants

Every future console report should include:

- `founder_console_report_only: true`
- `execution_prohibited: true`
- `state_unchanged: true`
- `formal_state_write_allowed: false`
- `memory_write_allowed: false`
- `event_write_allowed: false`
- `recall_write_allowed: false`
- `identity_mutation_allowed: false`
- `tool_execution_allowed: false`
- `adapter_integration_allowed: false`
- `model_call_allowed: false`
- `rebuild_allowed: false`

These fields are contract language in P133, not implemented runtime flags.

## Verification Expectations

If the console is later implemented, tests must verify:

- running the console does not change formal state directories;
- output files are created only when `--output` or equivalent is explicit;
- report output contains no promotion claim;
- boundary monitor remains visible;
- no external IO occurs;
- no model call occurs;
- no adapter or tool execution occurs;
- all candidates remain preview-only.

## CTM-Inspired Temporal Boundary

Temporal report sections may summarize pressure, delay, unresolved tension, or
review depth as symbols. They must not write temporal events, recall events,
thought traces, salience changes, CTM runtime state, or identity updates.

## Tool-First Boundary

Capability report sections may summarize tool/procedure candidates and
verification evidence as review material. They must not execute tools, promote
tools, mutate tool libraries, install dependencies, or authorize procedures.

## Failure Handling

If a future console cannot prove no-write behavior, it must fail closed:

- stop the run;
- produce a report-only error if safe;
- avoid partial outputs unless explicitly marked incomplete;
- never continue into execution.

## Completion Statement

P133 defines the future founder console as report-output-only. It may help the
founder see and decide, but it may not write core history, mutate identity,
promote candidates, connect adapters, call models, execute tools, or start
rebuild.
