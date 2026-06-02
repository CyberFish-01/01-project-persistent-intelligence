# 01 Core Adapter Protocol

Chinese mirror: [ADAPTER_PROTOCOL_ZH.md](./ADAPTER_PROTOCOL_ZH.md)

This is the generic adapter protocol for 01 Core.

Current protocol version:

```text
0.2
```

We build the generic version first, then specialize for AstrBot.

Core rule:

```text
01 Core owns state.
Adapters translate platforms.
Platforms do not own identity.
```

Meaning:

- 01 Core stores identity, memory, dreams, conflicts, and State Transfer Packages.
- adapters translate external platform events into protocol requests.
- AstrBot, Web UI, Telegram, and Discord should follow the same protocol first.
- after the protocol stabilizes, AstrBot can receive a deeper specialized adapter.

## Local Port

First version default:

```text
http://127.0.0.1:8765
```

Start:

```bash
python3 -m one_core.cli serve
```

## Generic Requests

### Health

```text
GET /health
```

### Status

```text
GET /v1/status
```

### Context

```text
GET /v1/context
```

### Interaction

```text
POST /v1/interact
```

Legacy-compatible request:

Request:

```json
{
  "message": "user or platform input",
  "user_id": "platform user ID",
  "channel": "platform or adapter name",
  "session_id": "platform session ID"
}
```

### Adapter Ingest

```text
POST /v1/adapter/ingest
```

This is the recommended v0.2 entry point.

Request:

```json
{
  "adapter_id": "astrbot_thin_adapter",
  "dry_run": false,
  "event": {
    "event_id": "platform event ID",
    "event_type": "message",
    "text": "user or platform input",
    "user": {
      "id": "platform user ID"
    },
    "source": {
      "adapter_id": "astrbot_thin_adapter",
      "channel": "astrbot",
      "session_id": "platform session ID"
    },
    "salience_hint": 0.6,
    "metadata": {
      "platform": "astrbot",
      "message_kind": "private"
    }
  }
}
```

Fields:

- `adapter_id`: external adapter identity, such as `astrbot_thin_adapter`.
- `event_id`: original platform event ID, reserved for future audit and deduplication.
- `event_type`: currently mostly `message`; future values may include `reaction`, `system_event`, and `task_event`.
- `text`: the text that enters episode preview or recording.
- `source.channel`: external platform or channel name.
- `source.session_id`: external session ID.
- `salience_hint`: adapter-provided salience suggestion from 0 to 1. 01 Core treats it as a suggestion, not an unconditional score.
- `metadata`: low-risk platform metadata. Do not put passwords, tokens, or full private payloads here.
- `dry_run`: when true, returns an episode preview without writing state.

Recorded response:

```json
{
  "protocol_version": "0.2",
  "agent_id": "01",
  "status": "recorded",
  "dry_run": false,
  "episode_id": "episode_xxx",
  "episode": {},
  "state_transfer_package": {}
}
```

Dry-run response:

```json
{
  "protocol_version": "0.2",
  "agent_id": "01",
  "status": "preview",
  "dry_run": true,
  "would_record_episode": {},
  "state_transfer_package": {}
}
```

### Dream

```text
POST /v1/dream
```

Request:

```json
{
  "limit": 20
}
```

## Local Generic Client

The repository now provides a generic client:

```python
from one_core.client import AdapterEvent, OneCoreClient

client = OneCoreClient("http://127.0.0.1:8765")
client.interact(
    AdapterEvent(
        message="Continue 01 Core.",
        user_id="cyberfish",
        channel="local_generic_adapter",
        session_id="local-dev",
    )
)
```

You can also test it through CLI:

```bash
python3 -m one_core.cli remote health
python3 -m one_core.cli remote status
python3 -m one_core.cli remote context
python3 -m one_core.cli remote interact "Continue 01 Core."
python3 -m one_core.cli remote interact "Preview only." --dry-run --salience-hint 0.8
python3 -m one_core.cli remote dream --limit 50
```

Choose a port:

```bash
python3 -m one_core.cli remote --api-base-url http://127.0.0.1:8765 status
```

## Current AstrBot Role

The current AstrBot plugin should remain a thin adapter:

```text
AstrBot event
  ↓
generic adapter protocol
  ↓
01 Core API
```

It should not yet:

- interpret long-term identity by itself;
- manage 01 Core state;
- automatically absorb every chat message;
- write into Angel Memory;
- mutate `state.json` directly.

After the generic protocol stabilizes, we can enter the AstrBot specialization stage:

- automatic session allowlists;
- State Transfer Package injection before replies;
- group-chat noise filtering;
- deeper integration with AstrBot providers and personas;
- read-only migration or review-based synchronization with Angel Memory.
