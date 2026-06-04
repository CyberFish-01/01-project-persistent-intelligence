# Context Package Builder RFC

Chinese version: [CONTEXT_PACKAGE_BUILDER_RFC_ZH.md](./CONTEXT_PACKAGE_BUILDER_RFC_ZH.md)

Status: `P137`, `RFC-only`, `document-only`, `non-runtime`.

P137 defines the future context package shape for 01 Core before any model call.
It does not implement a builder, CLI, retrieval engine, model call, prompt
execution, state write, memory write, recall write, identity mutation, adapter
integration, tool execution, policy executor, or rebuild.

## Problem Statement

Before 01 Core can safely use a model as a resource, it needs a defined context
package contract.

Without a contract, future orchestration may accidentally:

- treat retrieval as continuity;
- omit boundaries;
- mix trusted state with quarantined content;
- let model output define identity;
- overuse temporal or capability language;
- make response strategy implicit and unreviewable.

## Core Rule

```text
context package is preparation.
preparation is not model call.
selection is not truth.
package output is not state mutation.
```

## Required Packs

Every future context package preview should include:

| Pack | Purpose | Must Preserve |
|---|---|---|
| `identity_pack` | Stable identity anchors and protected boundaries. | Identity Core is not mutated. |
| `state_pack` | Current local operational status and relevant static state. | State reading is not state writing. |
| `task_pack` | Active or relevant task context. | Task preview is not task update. |
| `claim_pack` | Relevant claims and evidence references. | Claim selection is not claim truth. |
| `memory_pack` | Relevant memory references or summaries. | Memory retrieval is not continuity. |
| `boundary_pack` | Forbidden actions and review gates. | Boundary display is not enforcement. |
| `temporal_pack` | Elapsed-time and review-depth cues. | Temporal cues are symbolic, not runtime. |
| `capability_pack` | Tool/procedure/capability candidates and evidence. | Capability evidence is not authorization. |
| `response_strategy_pack` | How the model should respond as a resource. | Strategy is not execution. |

## Trust Levels

Each pack should label entries as:

- `trusted_foundation`
- `source_backed`
- `review_only`
- `candidate_only`
- `quarantined`
- `omitted`
- `blocked`

No future context package may silently promote lower-trust content into trusted
state.

## Source References

Each selected item should include:

- `source_id`
- `source_path`
- `source_class`
- `selection_reason`
- `omission_reason` when omitted;
- `risk_flags`;
- `review_gate` when needed.

## CTM-Inspired Temporal Pack

The `temporal_pack` may include:

- elapsed-time cue;
- interruption or session gap cue;
- unresolved tension note;
- delayed alignment candidate;
- review depth suggestion;
- thought-trace policy reminder.

It must not include:

- CTM runtime;
- thought loop execution;
- hidden chain-of-thought;
- temporal event write;
- recall event write;
- identity update;
- memory salience mutation.

## Tool-First Capability Pack

The `capability_pack` may include:

- tool candidate;
- procedure candidate;
- verification evidence preview;
- cautionary procedural memory candidate;
- capability growth candidate review route.

It must not include:

- tool execution;
- tool authorization;
- automatic tool promotion;
- dependency installation;
- policy executor;
- subject growth claim.

## Response Strategy Pack

The `response_strategy_pack` should tell a future model:

- answer as a resource, not as the subject;
- preserve boundaries;
- mark uncertainty;
- avoid identity claims;
- avoid claiming memory unless source-backed;
- avoid turning candidates into decisions;
- ask for founder review when required.

This pack is only a future instruction contract. It does not call a model.

## Future Builder Requirements

If a builder is later approved, it must:

- run locally;
- be deterministic;
- read only approved local sources;
- show selected and omitted sources;
- include all required packs;
- include boundary invariants;
- produce preview/report output only;
- prove no formal state changes.

## Completion Statement

P137 defines the context package as a structured, reviewable preparation layer.
It is the bridge between current source-backed previews and any future
LLM-as-resource orchestration, while keeping model calls and writes blocked.
