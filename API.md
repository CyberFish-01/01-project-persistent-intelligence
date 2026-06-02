# 01 Core API

Chinese version: [API_ZH.md](./API_ZH.md)

This is the first local HTTP API for 01 Core.

Its purpose is to let AstrBot, Web UI, Telegram bots, Discord bots, or other adapters connect to 01 Core without owning 01's core state.

By default it listens only on:

```text
127.0.0.1:8765
```

This is intentional. The first API is meant for local adapters.

## Start

```bash
python3 -m one_core.cli serve
```

Choose host and port:

```bash
python3 -m one_core.cli serve --host 127.0.0.1 --port 8765
```

Choose state directory:

```bash
python3 -m one_core.cli --state-dir work/01_state serve
```

## GET /health

Health check.

```bash
curl http://127.0.0.1:8765/health
```

Response:

```json
{
  "status": "ok",
  "agent_id": "01"
}
```

## GET /v1/status

Returns current state summary.

```bash
curl http://127.0.0.1:8765/v1/status
```

Fields:

```text
agent_id
updated_at
identity
active_intent
anchors
imported_memories
episodes
semantic_memories
open_conflicts
registered_adapters
indexed_adapter_events
pending_dream_jobs
```

## GET /v1/context

Returns the current State Transfer Package.

```bash
curl http://127.0.0.1:8765/v1/context
```

This endpoint is useful before response generation:

- identity summary;
- active intent;
- continuity anchors;
- recent episodes;
- relevant semantic memories;
- imported memories;
- open conflicts;
- current constraints.

## GET /v1/adapters

Returns the local adapter registry and registered adapters.

```bash
curl http://127.0.0.1:8765/v1/adapters
```

Default registered adapters:

```text
generic_adapter
local_generic_adapter
astrbot_thin_adapter
```

`POST /v1/adapter/ingest` requires a registered and enabled `adapter_id`.

## POST /v1/interact

Records one external interaction and returns a local reply plus State Transfer Package.

```bash
curl -X POST http://127.0.0.1:8765/v1/interact \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Continue 01 Core API.",
    "user_id": "cyberfish",
    "channel": "astrbot"
  }'
```

Request:

```json
{
  "message": "required",
  "user_id": "optional",
  "channel": "optional",
  "session_id": "optional"
}
```

Response fields:

```text
episode_id
summary
tags
salience
reply
anchors
state_transfer_package
```

## POST /v1/adapter/ingest

Recommended entry point for generic adapter protocol v0.4.

```bash
curl -X POST http://127.0.0.1:8765/v1/adapter/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "adapter_id": "local_generic_adapter",
    "dry_run": true,
    "event": {
      "event_type": "message",
      "text": "Preview this external event without writing state.",
      "user": {"id": "cyberfish"},
      "source": {
        "channel": "local",
        "session_id": "local-dev"
      },
      "salience_hint": 0.8
    }
  }'
```

When `dry_run` is true, the API returns `would_record_episode` without writing an episode or creating a dream job.

Unknown or disabled adapters are rejected before dry-run preview or recording.

When `event.event_id` is present, real writes are deduplicated by `adapter_id + event_id`. Repeated events return `status: "duplicate"` and do not write another episode or dream job. Dry-runs do not update the deduplication index.

## POST /v1/dream

Runs one Dream consolidation cycle.

```bash
curl -X POST http://127.0.0.1:8765/v1/dream \
  -H "Content-Type: application/json" \
  -d '{"limit": 50}'
```

Response includes:

```text
dream report
semantic candidates
conflicts
identity update proposals
forgetting proposals
next questions
```

## Adapter Pattern

External projects should connect like this:

```text
AstrBot / Web UI / Telegram
  ↓
Adapter
  ↓
POST /v1/adapter/ingest
  ↓
01 Core
  ↓
Episode + State Transfer Package
  ↓
Adapter sends reply
```

Adapters should not directly mutate:

```text
state.json
identity_core
memory_stores
dream_queue
```

## AstrBot Adapter

The repository now includes the first AstrBot adapter:

```text
adapters/astrbot/astrbot_plugin_01_core
```

After installing it into AstrBot's plugin directory, use:

```text
/01 ping
/01 status
/01 context
/01 chat <message>
/01 dream [limit]
```

This first version is command-based and does not listen to every chat message by default. It is intended to validate state transfer, episode recording, and Dream consolidation through 01 Core.

## Why No import-text API Yet

The first HTTP API does not expose file import.

File import reads local paths and has a higher risk profile than normal interaction.

Use CLI for memory migration:

```bash
python3 -m one_core.cli clean-memory ...
python3 -m one_core.cli import-text ...
```

After adding auth, tokens, and path allowlists, import APIs can be considered.
