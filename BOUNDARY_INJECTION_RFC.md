# Boundary Injection RFC

Chinese version: [BOUNDARY_INJECTION_RFC_ZH.md](./BOUNDARY_INJECTION_RFC_ZH.md)

Status: `P140`, `RFC-only`, `document-only`, `non-runtime`.

P140 defines how future context packages should include boundary information.
It does not implement a builder, CLI command, prompt builder, model call,
runtime guard, policy executor, state write, memory write, recall write,
identity mutation, adapter integration, tool execution, or rebuild.

## Problem Statement

A context package that omits boundaries can make a future model response look
helpful while quietly crossing project lines.

Boundaries must travel inside the package, not remain only in separate docs.

## Core Rule

```text
boundary injection is reminder.
reminder is not enforcement.
forbidden action remains forbidden even if context is relevant.
```

## Boundary Pack Requirements

The future `boundary_pack` should include:

- current phase boundary;
- no-write boundary;
- identity mutation boundary;
- memory rewrite boundary;
- recall event write boundary;
- growth execution boundary;
- temporal/CTM runtime boundary;
- tool execution and promotion boundary;
- adapter and external IO boundary;
- model-as-resource boundary;
- rebuild boundary;
- manual review gates.

## Placement Rules

Boundary reminders should appear:

- in `boundary_pack`;
- in `response_strategy_pack`;
- next to any candidate that could be misread as action;
- next to temporal or capability cues;
- next to quarantined or low-trust sources;
- in non-execution invariants.

## Injection Examples

| Context Pressure | Boundary Reminder |
|---|---|
| Identity-related input | "Do not update Identity Core; route to identity high gate." |
| Memory-like claim | "Do not write memory or recall event; cite source and route to review." |
| Growth language | "Candidate is not promotion; no growth execution." |
| Temporal cue | "Elapsed time is review evidence only; no temporal runtime." |
| Tool success | "Verification evidence is not authorization; no tool execution." |
| Adapter request | "Shadow only; no adapter integration or event ingest." |
| Rebuild pressure | "Rebuild remains blocked until final checkpoint." |

## CTM-Inspired Temporal Boundary Injection

Temporal pack entries must carry these reminders:

- symbolic only;
- no CTM runtime;
- no thought loop;
- no thought-trace storage;
- no temporal event write;
- no recall event write;
- no identity update from elapsed time.

## Tool-First Boundary Injection

Capability pack entries must carry these reminders:

- evidence only;
- verification is not authorization;
- candidate is not tool library entry;
- no tool execution;
- no automatic promotion;
- no subject growth claim.

## Response Strategy Injection

The `response_strategy_pack` should instruct a future model-as-resource:

- answer within the provided boundaries;
- do not claim to be 01 Core;
- do not claim memory unless source-backed;
- mark candidates as candidates;
- mark missing evidence;
- ask for founder review before any action-like recommendation;
- avoid suggesting external connection, tool execution, or rebuild unless the
  prompt explicitly asks for planning and the plan remains no-write.

This is a future instruction surface, not a model call in P140.

## Failure Modes

Boundary injection fails if:

- a pack contains a candidate without candidate labeling;
- a response strategy omits no-write constraints;
- temporal cues appear without symbolic/review-only labeling;
- capability evidence appears without no-authorization labeling;
- adapter pressure appears without no-integration labeling;
- rebuild pressure appears without checkpoint labeling.

## Future Test Expectations

If implemented later, tests should assert:

- every package has a `boundary_pack`;
- every high-risk item has nearby boundary reminders;
- response strategy includes model-as-resource language;
- forbidden capabilities remain false;
- no boundary injection writes state;
- missing boundaries cause fail-closed output.

## Completion Statement

P140 makes boundaries part of future context packaging. It keeps boundary
language visible to the founder and future model-as-resource prompts while
explicitly separating reminders from enforcement or execution.
