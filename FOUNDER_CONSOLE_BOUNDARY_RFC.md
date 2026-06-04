# Founder Console Boundary RFC

Chinese version: [FOUNDER_CONSOLE_BOUNDARY_RFC_ZH.md](./FOUNDER_CONSOLE_BOUNDARY_RFC_ZH.md)

Status: `P131`, `RFC-only`, `document-only`, `non-runtime`.

P131 defines the boundary for a future Thin Founder Console. It does not
implement a console, CLI command, Web UI, Companion behavior, adapter
integration, model call, state write, memory write, recall write, identity
mutation, tool execution, policy executor, or rebuild.

## Problem Statement

After the harness and lockdown blocks, the founder needs a local surface that
can make 01 Core's status legible without pretending to be a product.

The console should answer founder questions like:

- What can the core see?
- What remains blocked?
- Which risks are highest?
- Which candidates are only previews?
- Which next step requires founder approval?

It should not become a chat product, agent loop, dashboard runtime, social
companion, or adapter entry point.

## Boundary Rule

```text
founder console is a local control surface.
control surface is not product.
visibility is not execution.
review is not write permission.
```

## Allowed Scope

A future Thin Founder Console may:

- read approved local Markdown and static reports;
- call existing read-only report generators;
- display harness dry-run previews;
- display source inventory summaries;
- display boundary status;
- display risk and open-question summaries;
- write explicit report outputs only when the founder asks for an output file;
- use founder-facing Chinese display names where useful.

## Forbidden Scope

It must not:

- implement Web UI or dashboard runtime;
- act as Companion or user product;
- connect AstrBot, Telegram, QQ, browser adapters, or any external adapter;
- call LLMs or external APIs;
- execute tools;
- write formal state, events, memory, recall, identity, growth, temporal, or
  capability records;
- mutate Identity Core;
- rewrite memory;
- run reconstruction reducers;
- compact events;
- execute policy;
- automatically choose the roadmap;
- start rebuild.

## Minimum Surface Areas

The console may later expose read-only panels for:

| Surface | Purpose | Boundary |
|---|---|---|
| observatory snapshot | Show foundation status. | display-only |
| harness dry-run | Show how an input would route. | preview-only |
| source inventory | Show approved local sources. | whitelist-only |
| lockdown status | Show blocked external pressure. | no enforcement |
| review queue preview | Show where candidates would be reviewed. | no lifecycle |
| next-step candidates | Show possible directions. | no automatic roadmap |

## CTM-Inspired Temporal Dynamics Placement

The console may display symbolic temporal cues:

- temporal pressure;
- elapsed-time warning;
- review depth suggestion;
- unresolved tension note;
- thought-trace policy reminder.

It must not display these as CTM runtime, thought execution, neural
synchronization, temporal events, recall writes, or identity updates.

## Tool-First Self-Evolution Placement

The console may display capability cues:

- tool candidate;
- procedure candidate;
- verification evidence preview;
- cautionary procedural memory candidate;
- capability review gate.

It must not execute tools, authorize tools, promote procedures, install
dependencies, or treat capability evolution as subject growth.

## Founder Control Requirements

The future console must make these controls explicit:

- every next step is a candidate;
- every write-like action is blocked;
- every external connection is blocked;
- every promotion requires founder review;
- every output file is user-requested and report-only;
- no automatic step can be taken from a warning.

## Future Acceptance Direction

P131 does not approve implementation. If implementation is later approved, the
minimum acceptance bar should require:

- local-only execution;
- no external network;
- no model call;
- no state directory mutation;
- deterministic output;
- clear boundary monitor;
- founder-readable Chinese labels;
- all write-like capabilities disabled.

## Completion Statement

P131 defines the Thin Founder Console as a local, founder-only, no-write
visibility layer. It is a control surface for seeing and deciding, not a product
surface for acting.
