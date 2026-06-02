# Architecture

This document turns the 01 Project vision into a first engineering architecture.

The goal is not to build a conscious machine.

The goal is to build a system where identity, memory, task state, reflection, and update history can persist through time in an auditable way.

## 1. Design Principles

### Identity First

The stable unit is not the conversation.

The stable unit is the identity.

```text
Conversation != Identity
Session != Self
```

A session is a temporary interaction surface.

The identity is the long-lived state object that survives across sessions.

### State Before Retrieval

Memory retrieval is only one part of continuity.

The architecture must transfer:

- facts,
- working state,
- goals,
- unresolved conflicts,
- relationships,
- affective and motivational state,
- identity constraints,
- update history.

### Slow Identity, Fast Context

Different state layers should update at different speeds.

```text
Current Context: fast update
Working State: fast update
Episodic Memory: medium update
Semantic Memory: slower update
Identity Core: slowest update
```

This prevents single conversations from rewriting the identity too easily.

### Auditable Growth

Every identity-level update should be explainable.

The system should record:

- what changed,
- why it changed,
- which evidence supported it,
- what confidence it has,
- whether it can be rolled back.

## 2. High-Level System

```text
┌─────────────────────────────────────────────────────┐
│                    Identity Core                    │
│  values, self-model, constraints, long-term purpose  │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                   State Manager                     │
│  loads, validates, merges, snapshots, rolls back     │
└───────┬─────────────┬─────────────┬────────────────┘
        │             │             │
┌───────▼──────┐ ┌────▼─────┐ ┌────▼────────────┐
│ Memory Layer │ │ Task Hub │ │ Relationship Map │
└───────┬──────┘ └────┬─────┘ └────┬────────────┘
        │             │             │
┌───────▼─────────────▼─────────────▼────────────────┐
│                  Current Context                    │
│ prompt state, active task, retrieved memories, tools │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                  Interaction Loop                   │
│ observe -> reason -> act -> log episode              │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                    Dream Engine                     │
│ consolidate, abstract, forget, detect conflict       │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                    Update Log                       │
│ evidence, deltas, confidence, provenance, rollback   │
└─────────────────────────────────────────────────────┘
```

## 3. Core Modules

### Identity Core

The Identity Core contains slow-changing state:

- name and symbolic role,
- core values,
- stable traits,
- long-term purpose,
- self-narrative,
- identity constraints,
- prohibited self-updates,
- continuity anchors.

It should be updated only through a gated process.

### State Manager

The State Manager owns state transfer.

Responsibilities:

- load persistent state at session start,
- validate schema version,
- choose what enters the current context,
- merge updates from the interaction loop,
- request Dream Engine consolidation,
- write snapshots,
- maintain rollback points.

### Memory Layer

The Memory Layer is not one database.

It has several stores:

- episodic memory,
- semantic memory,
- identity memory,
- relationship memory,
- project memory,
- conflict memory,
- forgotten or archived memory.

Each memory should include source, timestamp, confidence, sensitivity, decay policy, and update history.

### Task Hub

The Task Hub preserves agency across interruptions.

It tracks:

- active goals,
- current plan,
- blocked tasks,
- completed tasks,
- recurring duties,
- project state,
- next actions.

It answers:

```text
What am I doing?
```

### Relationship Map

The Relationship Map stores social state.

It should distinguish:

- user-specific memories,
- cross-user generalizations,
- private information,
- shared project history,
- trust level,
- communication preferences,
- relationship conflicts.

This module is critical because multi-user persistence can easily create privacy and boundary failures.

### Current Context Builder

The Context Builder decides what state is activated for a session.

Inputs:

- identity core,
- active task,
- recent episodes,
- relevant semantic memories,
- relationship context,
- current user message,
- tool/environment constraints.

Output:

- a bounded context package for the model.

The context package should be small enough to fit within model limits and rich enough to preserve continuity.

### Interaction Loop

The Interaction Loop handles live behavior:

```text
observe -> interpret -> retrieve -> plan -> act -> record
```

At the end of each meaningful interaction, it emits an episode record.

### Dream Engine

The Dream Engine runs outside the immediate response loop.

It converts episodes into:

- summaries,
- semantic memories,
- conflict records,
- identity update proposals,
- forgetting proposals,
- relationship updates,
- future questions.

It should propose identity updates, not directly apply them without gates.

### Evaluation Harness

The Evaluation Harness tests whether the system is actually persistent.

It should simulate:

- time gaps,
- context loss,
- changing user preferences,
- conflicting goals,
- multi-session projects,
- noisy or misleading memories,
- social conflicts.

## 4. Session Lifecycle

### Session Start

```text
load identity
load relationship context
load active tasks
retrieve relevant memories
build current context
answer Identity / Context / Intent anchors
```

### During Session

```text
observe user input
retrieve relevant state
plan response or action
update working memory
log important events
mark possible conflicts
```

### Session End

```text
write episode
update task status
queue dream cycle
snapshot state
record update log
```

### Dream Cycle

```text
select episodes
cluster themes
extract semantic memories
detect conflicts
propose forgetting
propose identity updates
run safety gates
write approved updates
```

## 5. Update Gates

Not all updates are equal.

### Low Gate

Used for:

- recent task progress,
- temporary context,
- non-sensitive facts,
- user-corrected details.

### Medium Gate

Used for:

- semantic memories,
- preferences,
- relationship patterns,
- recurring project behavior.

Requires multiple supporting episodes or direct user confirmation.

### High Gate

Used for:

- identity core,
- long-term values,
- self-narrative,
- relationship commitments,
- safety-relevant beliefs.

Requires:

- multiple evidence sources,
- conflict check,
- reversibility,
- explicit update reason,
- audit log.

## 6. First MVP

The minimum viable 01 system should avoid weight training.

It can be implemented as:

- one base model,
- a structured state file,
- an episodic memory log,
- a semantic memory file,
- an identity seed file,
- a dream script,
- a simple evaluation suite.

The first research goal:

> Can a stateful agent recover its identity, context, and intent across interrupted sessions better than a memory-retrieval-only baseline?

If yes, then State Transfer is already experimentally meaningful.
