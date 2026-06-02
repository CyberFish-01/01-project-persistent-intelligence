# 01 Core Adapter Protocol

Chinese mirror: [ADAPTER_PROTOCOL_ZH.md](./ADAPTER_PROTOCOL_ZH.md)

This is the generic adapter protocol for 01 Core.

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

Request:

```json
{
  "message": "user or platform input",
  "user_id": "platform user ID",
  "channel": "platform or adapter name",
  "session_id": "platform session ID"
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
