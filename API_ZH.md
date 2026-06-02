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
candidate_memories
semantic_memories
open_conflicts
registered_adapters
session_policy_rules
indexed_adapter_events
audit_events
traces
dream_artifacts
pending_dream_jobs
```

## GET /v1/context

返回当前 State Transfer Package。

```bash
curl http://127.0.0.1:8765/v1/context
```

这个端点适合 adapter 在生成回复前获取：

- context package version；
- identity summary；
- active intent；
- continuity anchors；
- context policy；
- relationship context；
- activation trace；
- source attribution；
- unified relevant memories；
- recent episodes；
- relevant semantic memories；
- imported memories；
- open conflicts；
- current constraints。

`context_package_version: "0.2"` 表示这个 package 通过 bounded state activation 构建。它保留旧的 `recent_episodes`、`relevant_semantic_memories` 和 `imported_memories` 字段以兼容 adapter，同时额外暴露 memory 为什么被选择或压制。

## GET /v1/adapters

返回本地 adapter registry 和已注册 adapter。

```bash
curl http://127.0.0.1:8765/v1/adapters
```

默认注册的 adapter：

```text
generic_adapter
local_generic_adapter
astrbot_thin_adapter
```

`POST /v1/adapter/ingest` 要求 `adapter_id` 已注册且启用。

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

## POST /v1/adapter/ingest

通用 adapter protocol v0.5 的推荐入口。

```bash
curl -X POST http://127.0.0.1:8765/v1/adapter/ingest \
  -H "Content-Type: application/json" \
  -d '{
    "adapter_id": "local_generic_adapter",
    "dry_run": true,
    "event": {
      "event_type": "message",
      "text": "先预览这条外部事件，不写入 state。",
      "user": {"id": "cyberfish"},
      "source": {
        "channel": "local",
        "session_id": "local-dev"
      },
      "salience_hint": 0.8
    }
  }'
```

`dry_run: true` 时只返回 `would_record_episode`，不会写入 episode，也不会创建 dream job。

未知或禁用 adapter 会在 dry-run 预览或真实写入前被拒绝。

已注册 adapter 还会经过 session policy：

- `allow`：允许真实写入；
- `dry_run_only`：真实写入请求会被降级成 dry-run 预览；
- `reject`：拒绝请求。

当前默认策略中，AstrBot thin adapter 是 `dry_run_only`。

当 `event.event_id` 存在时，真实写入会用 `adapter_id + event_id` 去重。重复事件返回 `status: "duplicate"`，不会再写入 episode，也不会再创建 dream job。Dry-run 不更新去重索引。

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
POST /v1/adapter/ingest
  ↓
01 Core
  ↓
Episode + State Transfer Package
  ↓
Adapter sends reply
```

当前协议响应版本：

```text
protocol_version: "0.6"
```

对于 `/v1/adapter/ingest`，成功真实写入会同时创建 protocol-level `adapter_ingest` audit/trace 和底层 `record_episode` audit/trace。Dry-run 预览仍然不写入 state，也不会更新 `adapter_event_index`。

外部 adapter 不应该直接修改：

```text
state.json
identity_core
memory_stores
dream_queue
```

## AstrBot Adapter

仓库内已经包含第一版 AstrBot adapter：

```text
adapters/astrbot/astrbot_plugin_01_core
```

安装到 AstrBot 插件目录后，可以使用：

```text
/01 ping
/01 status
/01 context
/01 chat <内容>
/01 dream [limit]
```

这一版是命令式桥接，不默认监听全部聊天。它适合先验证 01 Core 的状态迁移、episode 记录和 Dream consolidation。

## 为什么没有 import-text API

第一版 HTTP API 暂时不提供文件导入端点。

原因是：文件导入涉及本地路径读取，风险比普通对话高。

目前导入旧记忆仍然使用 CLI：

```bash
python3 -m one_core.cli clean-memory ...
python3 -m one_core.cli import-text ...
```

等后续加入权限、token、路径白名单之后，再考虑开放导入 API。
