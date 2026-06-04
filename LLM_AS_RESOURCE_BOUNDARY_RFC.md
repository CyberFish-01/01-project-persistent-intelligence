# LLM-as-Resource Boundary RFC

Chinese version: [LLM_AS_RESOURCE_BOUNDARY_RFC_ZH.md](./LLM_AS_RESOURCE_BOUNDARY_RFC_ZH.md)

Status: `P144`, `RFC-only`, `document-only`, `non-runtime`.

P144 defines the boundary for treating future LLM calls as resource usage, not
subject ownership. It does not call a model, implement an adapter, build a
prompt engine, execute tools, write state, write memory, write recall events,
mutate identity, run policy, or rebuild.

## Core Rule

```text
LLM is resource.
01 Core owns state.
model output is untrusted by default.
resource output is not subject continuity.
```

## What The LLM May Do Later

A future approved LLM call may help with:

- drafting a response;
- summarizing source-backed context;
- comparing candidate routes;
- phrasing uncertainty;
- explaining boundaries to the founder;
- proposing review questions.

Only after a later implementation gate.

## What The LLM May Not Own

The LLM may not own:

- Identity Core;
- memory;
- recall policy;
- claim truth;
- task authority;
- growth promotion;
- tool authorization;
- adapter interpretation;
- temporal state transition;
- reconstruction truth;
- roadmap decisions.

## Default Treatment Of Output

Future LLM output must be treated as:

- untrusted;
- temporary;
- source-checkable;
- candidate-extractable;
- quarantine-eligible;
- founder-reviewable;
- non-persistent unless explicitly reviewed later.

It must not be treated as:

- memory;
- identity;
- event;
- recall;
- tool trust;
- growth;
- policy;
- rebuild approval.

## Prompt Boundary Requirements

Any future prompt must include:

- model is resource, not subject;
- do not claim to be 01 Core;
- do not invent memories;
- do not change identity;
- do not promote candidates;
- do not authorize tools;
- do not recommend adapter connection as action;
- do not imply rebuild has started;
- mark uncertainty and missing evidence.

## CTM-Inspired Temporal Boundary

The LLM may later discuss temporal review cues only as symbolic context. It must
not claim consciousness, CTM runtime, thought loop execution, neural
synchronization, thought-trace capture, temporal event creation, recall event
creation, or identity update from elapsed time.

## Tool-First Boundary

The LLM may later discuss tool/procedure candidates only as review material. It
must not authorize tools, execute tools, promote tools, install dependencies,
write a tool library, create a policy executor, or describe capability
evolution as subject growth.

## Future Review Gate

Before any LLM output can influence durable project state, it must pass:

1. source attribution review;
2. boundary violation review;
3. candidate extraction review;
4. founder approval;
5. lowest-risk write policy, if such policy exists later.

P144 does not create that write policy.

## Completion Statement

P144 keeps the model outside the subject. It may later be useful as a language
and reasoning resource, but it cannot own continuity, state, identity, memory,
tools, policy, or rebuild decisions.
