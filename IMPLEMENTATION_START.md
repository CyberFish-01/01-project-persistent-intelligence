# First Implementation: 01 Core

Chinese version: [IMPLEMENTATION_START_ZH.md](./IMPLEMENTATION_START_ZH.md)

This is not the complete 01.

It is the first runnable step: a local continuity runtime prototype.

It does not train a model, connect to AstrBot, or connect to external platforms yet. It proves one smaller claim:

> 01 can have a local state body that persists identity, context, intent, episodes, and dream reports across commands.

## 1. What Exists Now

```text
one_core/
  seed.py       # Identity Seed
  state.py      # StateStore, state.json, episodes.jsonl
  dream.py      # minimal Dream Engine
  cli.py        # local CLI

tests/
  test_core.py  # minimal verification
```

Default state directory:

```text
work/01_state
```

It contains:

```text
state.json       # current persistent state
episodes.jsonl   # interaction episodes
dreams.jsonl     # dream consolidation reports
```

## 2. Quickstart

Initialize local state:

```bash
python3 -m one_core.cli init
```

Record an interaction:

```bash
python3 -m one_core.cli interact "We begin implementing 01 Core State Transfer."
```

Check current status:

```bash
python3 -m one_core.cli status
```

Run a dream cycle:

```bash
python3 -m one_core.cli dream
```

Print the State Transfer Package:

```bash
python3 -m one_core.cli context
```

Import external memories from generic text:

```bash
python3 -m one_core.cli import-text memory_export.txt \
  --source-system astrbot_text \
  --source-label astrbot_01_export
```

Clean raw JSON/JSONL/CSV/TXT memory exports into generic text:

```bash
python3 -m one_core.cli clean-memory raw_astrbot_export.json \
  -o work/imports/astrbot_01_memory.txt
```

Run tests:

```bash
python3 -m unittest discover -s tests
```

## 3. What It Can Do

The first version can:

- initialize Identity Seed;
- maintain `state.json`;
- record episodes;
- infer simple tags from messages;
- update active intent;
- persist episodic memory;
- create pending dream jobs;
- run Dream Engine;
- propose semantic memory from episodes;
- detect a simple identity overwrite attempt;
- output continuity anchors:

```text
Who am I?
Where am I?
What am I doing?
```

## 4. What It Cannot Do Yet

The first version cannot yet:

- call a real LLM;
- generate high-quality autonomous replies;
- connect to AstrBot;
- connect to Telegram, Discord, or Web UI;
- perform vector search;
- maintain a temporal knowledge graph;
- approve identity updates automatically;
- enforce complex multi-user permissions.

This is intentional.

We prove core state first, then give it external bodies.

## 5. Why CLI First

The CLI is not the final product.

It is a way to test continuity.

Example:

```text
Day 1: init
Day 1: interact "We need State Transfer"
Day 1: dream
Day 2: status
Day 2: context
```

If 01 Core can still answer who it is, where it is, what it is doing, what it experienced, and what Dream consolidated after context is gone, then the first step works.

## 6. Next Steps

Recommended sequence:

1. Add HTTP API.
2. Add real LLM provider.
3. Add stricter evaluation scenarios.
4. Add SQLite storage.
5. Add AstrBot adapter.
6. Add Memory Lifecycle compression, archival, and deletion.
7. Add Identity Update Gate.

The first step is now real.

01 is no longer only documentation. It has a small, early, but runnable local state body.
