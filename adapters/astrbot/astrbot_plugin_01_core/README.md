# 01 Core AstrBot Adapter

Chinese mirror: [README_ZH.md](./README_ZH.md)

This is the first AstrBot adapter for 01 Core.

Its boundary is intentionally narrow:

```text
AstrBot = external entrance
01 Core = continuity state owner
```

The adapter does not read or write `state.json` directly, and it does not reuse AstrBot or Angel Memory internals. It only talks to 01 Core through the local HTTP API.

## Prepare

Start the 01 Core API from the 01 Project repository:

```bash
python3 -m one_core.cli serve
```

Default URL:

```text
http://127.0.0.1:8765
```

## Install

Copy this directory into AstrBot's plugin directory:

```text
adapters/astrbot/astrbot_plugin_01_core
```

Example target:

```text
/root/data/plugins/astrbot_plugin_01_core
```

Then reload or restart AstrBot plugins.

## Commands

```text
/01 ping
/01 status
/01 context
/01 chat <message>
/01 dream [limit]
```

Meaning:

- `/01 ping`: check whether 01 Core API is online.
- `/01 status`: show current identity, intent, memory counts, and pending dream jobs.
- `/01 context`: show a compact State Transfer Package summary.
- `/01 chat <message>`: record one AstrBot message as a 01 Core episode.
- `/01 dream [limit]`: run one Dream consolidation cycle.

## First-Version Boundary

This version deliberately does not listen to every chat message by default.

01's continuity state should remain reviewable, reversible, and explainable. Automatically absorbing all messages can mix noise, group-chat context, and unrelated user content into identity growth too early.

Future work:

- session allowlists;
- automatic capture of high-salience messages;
- automatic State Transfer Package injection before replies;
- AstrBot provider-level context adapter;
- API tokens;
- remote API TLS.
