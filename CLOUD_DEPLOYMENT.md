# 01 Core Cloud Deployment

Chinese mirror: [CLOUD_DEPLOYMENT_ZH.md](./CLOUD_DEPLOYMENT_ZH.md)

01 Core is better suited to a cloud server than a local laptop.

Persistent Intelligence needs a continuous state home. If the runtime only exists on a local computer, shutdowns, network interruptions, sleep, and travel interrupt continuity.

Recommended first deployment shape:

```text
AstrBot
  ↓ localhost
01 Core API
  ↓
/root/01_state
```

## Server Paths

Recommended:

```text
/root/01-project-persistent-intelligence  # repository
/root/01_state                            # 01 Core state
/root/01_imports                          # one-time import artifacts
/root/data/plugins/astrbot_plugin_01_core # AstrBot adapter
```

## Clone Repository

```bash
git clone https://github.com/CyberFish-01/01-project-persistent-intelligence.git /root/01-project-persistent-intelligence
```

Update:

```bash
cd /root/01-project-persistent-intelligence
git pull --ff-only
```

## Initialize State

```bash
cd /root/01-project-persistent-intelligence
python3 -m one_core.cli --state-dir /root/01_state init
```

If importing old AstrBot / Angel Memory data:

```bash
mkdir -p /root/01_imports
find /root/data/plugin_data/astrbot_plugin_angel_memory /root/data/plugin_data/astrbot_plugin_01_dreams \
  -type f \
  \( -name '*.db' -o -name '*.sqlite' -o -name '*.sqlite3' -o -name '*.json' -o -name '*.jsonl' -o -name '*.md' -o -name '*.txt' \) \
  > /root/01_imports/source_files.txt

python3 -m one_core.cli clean-memory $(cat /root/01_imports/source_files.txt) \
  -o /root/01_imports/astrbot_angel_memory_cleaned.txt

python3 -m one_core.cli --state-dir /root/01_state import-text \
  /root/01_imports/astrbot_angel_memory_cleaned.txt \
  --source-label astrbot_angel_memory_cloud_seed \
  --source-system astrbot_angel_memory

python3 -m one_core.cli --state-dir /root/01_state dream --limit 1000
```

## systemd Service

The repository provides a service template:

```text
deploy/systemd/01-core.service
```

Install:

```bash
cp /root/01-project-persistent-intelligence/deploy/systemd/01-core.service /etc/systemd/system/01-core.service
systemctl daemon-reload
systemctl enable --now 01-core.service
```

Check:

```bash
systemctl status 01-core.service --no-pager -l
curl http://127.0.0.1:8765/health
curl http://127.0.0.1:8765/v1/status
```

## Install AstrBot Adapter

```bash
rm -rf /root/data/plugins/astrbot_plugin_01_core
cp -R /root/01-project-persistent-intelligence/adapters/astrbot/astrbot_plugin_01_core \
  /root/data/plugins/astrbot_plugin_01_core
systemctl restart astrbot.service
```

Then use in AstrBot:

```text
/01 ping
/01 status
/01 context
/01 chat <message>
/01 dream [limit]
```

## Security Boundary

The first API listens only on:

```text
127.0.0.1:8765
```

Do not expose it directly to the public internet.

Remote access should wait for:

- tokens;
- TLS;
- path allowlists;
- adapter identity;
- audit logs.

## Current Server Validation

On 2026-06-03, one cloud deployment was validated:

```text
01 Core service: active, enabled
01 Core API: http://127.0.0.1:8765
state dir: /root/01_state
imported memories: 1005
semantic memories after dream: 9
pending dream jobs: 0
AstrBot service: active
AstrBot adapter import under AstrBot runtime: ok
```
