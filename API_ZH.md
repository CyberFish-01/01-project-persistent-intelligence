# 01 Core API

英文镜像：[API.md](./API.md)

这是 01 Core 的第一版本地 HTTP API。

它的用途是让 AstrBot、Web UI、Telegram bot、Discord bot 或其他 adapter 接入 01 Core，而不是直接拥有 01 的核心状态。

默认只监听：

```text
127.0.0.1:8765
```

这是刻意的。第一版 API 默认只给本机 adapter 使用。

## 启动

```bash
python3 -m one_core.cli serve
```

指定端口：

```bash
python3 -m one_core.cli serve --host 127.0.0.1 --port 8765
```

指定状态目录：

```bash
python3 -m one_core.cli --state-dir work/01_state serve
```

## GET /health

健康检查。

```bash
curl http://127.0.0.1:8765/health
```

返回：

```json
{
  "status": "ok",
  "agent_id": "01"
}
```

## GET /v1/status

返回当前状态摘要。

```bash
curl http://127.0.0.1:8765/v1/status
```

返回字段包括：

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
pending_dream_jobs
```

## GET /v1/context

返回当前 State Transfer Package。

```bash
curl http://127.0.0.1:8765/v1/context
```

这个端点适合 adapter 在生成回复前获取：

- identity summary；
- active intent；
- continuity anchors；
- recent episodes；
- relevant semantic memories；
- imported memories；
- open conflicts；
- current constraints。

## POST /v1/interact

记录一次外部交互，并返回 01 Core 的本地回复与 State Transfer Package。

```bash
curl -X POST http://127.0.0.1:8765/v1/interact \
  -H "Content-Type: application/json" \
  -d '{
    "message": "小鱼说继续 01 Core API。",
    "user_id": "cyberfish",
    "channel": "astrbot"
  }'
```

请求字段：

```json
{
  "message": "required",
  "user_id": "optional",
  "channel": "optional",
  "session_id": "optional"
}
```

返回字段：

```text
episode_id
summary
tags
salience
reply
anchors
state_transfer_package
```

## POST /v1/dream

运行一次 Dream consolidation。

```bash
curl -X POST http://127.0.0.1:8765/v1/dream \
  -H "Content-Type: application/json" \
  -d '{"limit": 50}'
```

返回：

```text
dream report
semantic candidates
conflicts
identity update proposals
forgetting proposals
next questions
```

## Adapter 范式

外部项目应该这样接入：

```text
AstrBot / Web UI / Telegram
  ↓
Adapter
  ↓
POST /v1/interact
  ↓
01 Core
  ↓
Episode + State Transfer Package
  ↓
Adapter sends reply
```

外部 adapter 不应该直接修改：

```text
state.json
identity_core
memory_stores
dream_queue
```

## 为什么没有 import-text API

第一版 HTTP API 暂时不提供文件导入端点。

原因是：文件导入涉及本地路径读取，风险比普通对话高。

目前导入旧记忆仍然使用 CLI：

```bash
python3 -m one_core.cli clean-memory ...
python3 -m one_core.cli import-text ...
```

等后续加入权限、token、路径白名单之后，再考虑开放导入 API。
