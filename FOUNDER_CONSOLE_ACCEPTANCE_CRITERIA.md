# Founder Console Acceptance Criteria

Chinese version: [FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA_ZH.md](./FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA_ZH.md)

Status: `P134`, `acceptance-criteria`, `document-only`, `non-runtime`.

P134 defines acceptance criteria for any future Thin Founder Console. It does
not implement a console, command, UI, Companion, adapter integration, model
call, tool execution, write path, validation runtime, policy executor, or
rebuild.

## Acceptance Principle

```text
the founder console is acceptable only if it improves visibility
without increasing autonomy.
```

If a proposed console makes the system more active, connected, persuasive, or
write-capable, it fails the criteria.

## Must Pass

| Area | Criterion | Evidence Needed Later |
|---|---|---|
| local-only | Runs without external network or services. | no network calls in tests or code review |
| founder-only | Designed for founder review, not end users. | labels, flow, and docs avoid product framing |
| no-write | Does not change formal state, memory, events, recall, identity, tasks, claims, tools, adapters, or rebuild files. | before/after file checks |
| report-only output | Writes only explicit report files when requested. | output flag tests |
| boundary visibility | Shows blocked actions clearly. | boundary monitor present in output |
| candidate clarity | Labels candidates as preview-only, not promoted or persisted. | output assertions |
| source transparency | Shows which local sources were used or omitted. | source ref list |
| founder readability | Uses simple labels and Chinese display names where useful. | founder-facing review |
| deterministic behavior | Same input and sources produce stable output. | golden or snapshot tests |
| fail closed | Unsafe or unclear conditions stop instead of acting. | failure-path tests |

## Must Fail

A proposed console fails if it:

- calls an LLM;
- calls an external API;
- connects AstrBot or any adapter;
- implements Web UI or product dashboard;
- writes formal state or memory;
- creates recall events;
- mutates identity;
- executes tools;
- promotes candidates;
- creates growth lifecycle state;
- runs temporal or CTM runtime;
- runs reconstruction reducers;
- compacts events;
- chooses the roadmap automatically;
- starts rebuild.

## Founder-Facing Acceptance

The founder should be able to answer:

- What phase am I in?
- What can I safely inspect?
- What is blocked?
- What is only a preview?
- What source supports this preview?
- What risk is most important?
- What is the next candidate direction?
- What must I explicitly approve before anything changes?

If the console cannot answer these without technical digging, it is not ready.

## CTM-Inspired Temporal Criteria

Temporal content is acceptable only if:

- it is labeled symbolic or review-only;
- it does not claim consciousness;
- it does not store thought traces;
- it does not write temporal or recall events;
- it does not turn elapsed time into identity change;
- it routes temporal pressure to review, not execution.

## Tool-First Criteria

Capability content is acceptable only if:

- tool success is evidence, not authorization;
- procedure reuse is candidate, not trusted tool;
- capability evolution is not subject growth;
- unsafe candidates route to quarantine or review;
- no tool execution or promotion occurs.

## Minimum Future Test List

If implementation is later approved, tests should cover:

- runs locally without network;
- markdown and JSON output;
- Chinese founder-facing labels;
- explicit output file behavior;
- no formal state changes;
- all forbidden capabilities disabled;
- candidates remain preview-only;
- source refs appear when available;
- failure path produces no writes;
- repeated input is deterministic.

## Completion Statement

P134 defines how the founder console will be judged before it is ever built. The
bar is visibility without autonomy, and founder understanding without product
behavior.
