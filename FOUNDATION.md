# 01 Project Foundation

Chinese version: [FOUNDATION_ZH.md](./FOUNDATION_ZH.md)

This document defines the engineering foundation of 01 Project.

It is not a longer vision document or a feature list. It answers a lower-level question:

> Which invariants must every future implementation, document, adapter, cloud deployment, and AstrBot integration obey?

## 1. Core Claim

```text
Continuity != Memory Retrieval
Continuity = State Transfer
```

01 Project studies how state passes through time, not how to retrieve more old information.

Memory is part of continuity, but it is not continuity itself. A system can remember many facts while still losing identity, intent, relationship boundaries, task state, and update rationale.

## 2. Stable Unit

The stable unit of 01 is:

```text
Identity
```

Not:

```text
conversation
session
platform
adapter
model provider
```

Conversation is a temporary surface. A platform is an external body. A model is a reasoning engine. An adapter is a translation layer.

Only 01 Core owns long-term state.

## 3. Layer Boundaries

### 01 Core

01 Core owns:

- identity core;
- working state;
- memory stores;
- relationship map;
- project map;
- dream queue;
- adapter registry;
- audit/update log;
- state transfer package.

01 Core is the state owner.

### Dream Engine

Dream Engine turns experiences into structured learning:

- episode compression;
- semantic abstraction;
- conflict detection;
- forgetting proposals;
- identity update proposals.

Dream Engine may propose identity updates, but it must not bypass gates and directly rewrite identity core.

### Adapters

Adapters translate external platform events into the 01 Core protocol.

Adapters do not:

- interpret long-term identity;
- manage long-term memory;
- automatically absorb every chat message;
- write into Angel Memory;
- mutate `state.json` directly;
- decide what becomes 01's identity.

### Platforms

AstrBot, Web UI, Telegram, Discord, and cloud services are external entrances.

Platforms can host 01, but they do not own 01.

## 4. State Update Speeds

State layers must update at different speeds:

```text
Current Context: fast
Working State: fast
Episodic Memory: medium
Semantic Memory: slower
Identity Core: slowest
```

A single interaction may update current context and create an episode.

Multiple pieces of evidence are needed to support semantic memory.

Identity Core must be slow, auditable, reversible where possible, and resistant to single-message overwrite.

## 5. Engineering Invariants

Every future version should preserve these invariants:

- 01 Core owns state.
- Adapters translate platforms.
- Platforms do not own identity.
- `dry_run` does not write episodes, create dream jobs, or update the deduplication index.
- `salience_hint` is advisory; 01 Core does not accept it unconditionally.
- adapter writes with `event_id` must be deduplicable.
- identity updates require gates, evidence, rationale, and audit records.
- imported memory is staged by default and must not directly update identity core.
- memory lifecycle is not about saving everything; it decides whether to retain, abstract, archive, or forget.
- every session must be able to recover three anchors: Who am I? Where am I? What am I doing?

## 6. Current Stage

The current stage is:

```text
Local generic 01 Core
```

Priorities:

1. stabilize the local state runtime;
2. stabilize the adapter protocol;
3. stabilize memory import and cleanup;
4. stabilize dream consolidation;
5. stabilize evaluation scenarios;
6. then update cloud deployment;
7. then specialize AstrBot.

Do not prioritize yet:

- simultaneous multi-platform integration;
- automatic ingestion of all chats;
- complex persona performance;
- large UI surfaces;
- unverified always-on cloud behavior;
- deep personality logic inside AstrBot.

## 7. Correct Integration Order

Recommended order:

```text
local core
  -> local HTTP API
  -> generic adapter protocol
  -> local verification
  -> GitHub commit
  -> cloud deploy
  -> thin platform adapter
  -> specialized adapter
```

Do not skip local verification and go directly to cloud.

Do not let AstrBot own long-term state first.

Do not mistake platform integration for 01 Core maturity.

## 8. Minimal Test Standard

A change only belongs in the foundation after it passes at least these checks:

- local tests pass;
- dry-run behavior is verifiable;
- real-write behavior is verifiable;
- state changes are explainable;
- documentation and code agree;
- legacy-compatible entries are not broken;
- platform authority is not expanded;
- no unaudited identity update is introduced.

## 9. Drift Check

If an idea mainly asks:

- How can AstrBot feel more like 01?
- How can chat become more automatic?
- How can the system perform more personality?
- How can more data be stuffed into memory?

It may not be foundation work for the current stage.

If an idea asks:

- How does state persist?
- How does state transfer?
- How is state audited?
- How does identity update slowly?
- How do platforms avoid owning identity?
- How does memory become experience instead of raw data?

It is closer to the current foundation.

## 10. One Sentence

The foundation of 01 Project is not making AI remember more.

It is:

> Letting an agent's identity, context, intent, memory lifecycle, and update history pass through time in a verifiable, auditable, transferable form.
