# Harness Roadmap

Chinese version: [HARNESS_ROADMAP_ZH.md](./HARNESS_ROADMAP_ZH.md)

Status: `P109`, `roadmap`, `document-only`, `non-runtime`.

P109 describes what the current `harness-dry-run` can and cannot see after
P102-P108. It does not add features, call a model, run retrieval, write state,
write memory, write recall events, execute tools, create review lifecycles,
integrate adapters, enter UI/product work, or authorize P110+ implementation.

## Roadmap Rule

```text
the harness is a pressure viewer, not an interaction runtime.
classification is not understanding.
preview is not persistence.
review routing is not lifecycle.
next-step recommendation is not execution.
```

## Current Harness Shape

The implemented command is:

```bash
python3 -m one_core.cli harness-dry-run
```

It is a local, deterministic, no-write dry-run. It accepts a single input string
and emits Markdown or JSON showing how that input would be previewed through:

- intake preview;
- deterministic pressure classification;
- context package preview;
- candidate preview;
- review queue preview;
- boundary monitor;
- observatory snapshot;
- non-execution invariants.

## What The Harness Can See Now

| Surface | What It Can See | Current Evidence |
|---|---|---|
| Input envelope | User message, session id, actor id, privacy scope, CLI source, no-write flag. | `intake_preview` |
| Pressure class | Deterministic keyword/rule-based pressure type. | `input_pressure_type`, `matched_signals` |
| Scenario profile | Founder-facing route, reason, risks, do-not-do list, next manual step. | `scenario_profile`, `founder_summary` |
| Context theme | Static foundation refs relevant to the pressure class. | `context_package_preview` |
| Candidate shape | Pressure-specific candidates with intent, selection reason, blocked promotion, and manual review target. | `candidate_preview` |
| Review gate shape | Pressure-specific review gates with queue intent, gate reason, blocked lifecycle, and manual-review-only next action. | `review_queue_preview` |
| Boundary visibility | Disabled forbidden capabilities and highlighted high-relevance boundaries. | `boundary_monitor` |
| Observatory summary | Short status snapshot aligned with the selected pressure. | `observatory_snapshot` |

## What The Harness Cannot See Yet

| Missing Surface | Why It Matters | Why It Is Still Blocked |
|---|---|---|
| Real memory relevance | The harness cannot know which actual memories matter. | Real retrieval could be mistaken for continuity or prompt construction. |
| Real claim evidence | It cannot compare the input against a real claim graph. | Claim mutation and automatic belief revision remain blocked. |
| Real task state | It cannot inspect or update live tasks. | Task writes and automatic roadmap execution remain blocked. |
| Real event payload gaps | It cannot inspect whether events have enough payload/diff data. | Reducer execution and event compaction remain blocked. |
| Real temporal state | It cannot measure elapsed-time effects or staleness. | Temporal runtime and temporal event writes remain blocked. |
| Real tool evidence | It cannot verify tool success, failure, or reproducibility. | Tool execution and automatic tool promotion remain blocked. |
| Real adapter/session pressure | It cannot observe AstrBot, platform sessions, or external traffic. | Adapter integration remains blocked. |

## Boundary Status

These stay explicitly disabled:

- identity mutation;
- memory rewrite;
- recall event write;
- growth execution;
- temporal runtime;
- CTM runtime;
- tool execution;
- automatic tool promotion;
- policy executor;
- Companion layer;
- UI/Web/product layer;
- AstrBot/adapter integration;
- reconstruction reducer execution;
- event compaction;
- harness state write;
- automatic next-step execution.

## Is The Harness Ready For Read-Only Context Preview Refinement?

Yes, with constraints.

P108 suggests the harness is now readable enough to plan a next read-only
refinement focused on context preview. That future refinement should still be
fixture-first or static-source-first. It should not retrieve live memory, build a
prompt, call a model, mutate context, write traces, write recall events, or
assign durable review ownership.

Safe candidate direction:

- make `context_package_preview` explain selected refs, omitted refs, and missing
  evidence more clearly;
- use deterministic static fixture refs, not live retrieval;
- add tests proving the state directory stays unchanged;
- keep all candidate and review queue output preview-only;
- keep all forbidden boundary flags false/disabled.

Not safe yet:

- live memory retrieval;
- event-log reducer checks;
- claim graph mutation;
- task writes;
- adapter session import;
- model-generated context selection;
- thought trace storage;
- temporal runtime.

## Recommended Next Read-Only Work

| Priority | Candidate | Why Now | Risk |
|---|---|---|---|
| 1 | Harness Work Summary | Close P102-P110 with an audit summary before more changes. | Low; document-only. |
| 2 | Founder / CTO Review | Let a human decide whether the harness is understandable enough. | Low; prevents self-directed overbuild. |
| 3 | Read-Only Context Preview Plan | Define selected/omitted/gap fields before any code. | Medium; may tempt real retrieval. |
| 4 | Fixture-First Context Preview Implementation | Only after explicit approval; use deterministic fixtures. | Medium; must prove no writes and no retrieval. |
| 5 | Harness Output Contract Stabilization | Freeze field names once founder-facing shape is accepted. | Medium; can ossify too early. |

## Deferred Work

Do not start these from P109:

- Companion behavior;
- UI, Web, dashboard runtime, or product surface;
- AstrBot or adapter integration;
- model calls or external APIs;
- real retrieval;
- memory writes or recall event writes;
- growth lifecycle;
- temporal runtime;
- tool execution or tool promotion;
- policy executor;
- reconstruction reducers or event compaction.

## Relationship To Recent Phases

| Phase | Relationship |
|---|---|
| P100 | Implemented the first no-write dry-run command. |
| P101 | Found the first version too static, scoring 6.5/10. |
| P102 | Added deterministic pressure classification and scenario routing. |
| P103 | Added founder summary, human-readable risks, next step, and do-not-do list. |
| P104 | Documented the scenario profile test matrix. |
| P105 | Hardened boundary monitor output. |
| P106 | Specialized candidate preview rows. |
| P107 | Specialized review queue preview rows. |
| P108 | Re-reviewed usability and scored the current shape 8.0/10. |

## P110 Candidate

Recommended P110: **Overnight Harness Work Summary**.

It should record:

- start and end commits;
- P102-P110 phase summaries and hashes;
- tests and smoke checks;
- boundary status;
- usability score change from P101 to P108;
- suggested next-day options;
- explicit stop before P111.

## Non-Execution Statement

P109 is a roadmap only. It does not authorize runtime implementation, product
work, adapter integration, Companion behavior, model calls, real retrieval,
event writes, memory writes, recall writes, identity mutation, growth execution,
temporal runtime, tool execution, policy execution, reconstruction reducer
execution, event compaction, automatic tool promotion, or automatic roadmap
execution.
