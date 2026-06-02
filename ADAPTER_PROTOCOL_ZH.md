# 01 Core Adapter Protocol

英文镜像：[ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md)

这是 01 Core 的通用接入协议。

当前协议版本：

```text
0.6
```

我们先做通用版，再做 AstrBot 特化版。

核心原则：

```text
01 Core owns state.
Adapters translate platforms.
Platforms do not own identity.
```

也就是说：

- 01 Core 保存 identity、memory、dream、conflict、state transfer package；
- adapter 只负责把外部平台事件翻译成协议请求；
- AstrBot、Web UI、Telegram、Discord 都应该先遵守同一套协议；
- 等协议稳定后，再给 AstrBot 做更深的特化适配。

## 本地端口

第一版默认：

```text
http://127.0.0.1:8765
```

启动：

```bash
python3 -m one_core.cli serve
```

## 通用请求

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

### Adapter Registry

```text
GET /v1/adapters
```

返回当前 adapter registry 和已注册 adapter。

Protocol v0.3 引入了本地 adapter allowlist：

- `/v1/adapter/ingest` 要求 `adapter_id` 已注册且启用；
- 未知 adapter 会在预览或写入前被拒绝；
- `/v1/interact` 继续保持旧版兼容，暂时不强制检查 adapter registry。

Protocol v0.5 引入 session policy：

- adapter 通过 registry 后，还要通过 session policy；
- policy action 支持 `allow`、`dry_run_only`、`reject`；
- `dry_run_only` 会把真实写入请求降级成 dry-run 预览；
- 默认 AstrBot thin adapter 是 `dry_run_only`，避免早期自动吸收聊天。

Protocol v0.6 加固 auditability：

- disabled adapter 会在 registry validation 阶段被拒绝，即使是 dry-run；
- 成功的真实 ingest 除 episode 写入外，还会生成 adapter-level audit / trace；
- deduplication 依赖持久化 `adapter_event_index`，API 实例重启后仍能识别重复的 `adapter_id + event_id`。

默认注册的 adapter：

```text
generic_adapter
local_generic_adapter
astrbot_thin_adapter
```

### Interaction

```text
POST /v1/interact
```

旧版兼容请求：

请求：

```json
{
  "message": "用户或外部平台输入",
  "user_id": "平台内用户 ID",
  "channel": "平台或 adapter 名称",
  "session_id": "平台内会话 ID"
}
```

### Adapter Ingest

```text
POST /v1/adapter/ingest
```

推荐从 v0.6 起使用这个入口。

请求：

```json
{
  "adapter_id": "astrbot_thin_adapter",
  "dry_run": false,
  "event": {
    "event_id": "平台内事件 ID",
    "event_type": "message",
    "text": "用户或外部平台输入",
    "user": {
      "id": "平台内用户 ID"
    },
    "source": {
      "adapter_id": "astrbot_thin_adapter",
      "channel": "astrbot",
      "session_id": "平台内会话 ID"
    },
    "salience_hint": 0.6,
    "metadata": {
      "platform": "astrbot",
      "message_kind": "private"
    }
  }
}
```

字段含义：

- `adapter_id`：外部接入器身份，例如 `astrbot_thin_adapter`。
- `adapter_id` 必须存在于 01 Core adapter registry，并且处于启用状态。
- `event_id`：外部平台原始事件 ID。存在时，01 Core 会用 `adapter_id + event_id` 对真实写入去重。
- `event_type`：当前主要是 `message`，后续可扩展为 `reaction`、`system_event`、`task_event`。
- `text`：真正进入 episode 预览或记录的文本。
- `source.channel`：外部平台或通道名。
- `source.session_id`：外部会话 ID。
- `salience_hint`：adapter 给出的显著性建议，范围 0 到 1。01 Core 会把它当建议，不会无条件采用。
- `metadata`：平台原始信息的低风险摘要，不应该塞入密码、token 或完整隐私 payload。
- `dry_run`：为 `true` 时只返回 episode 预览，不写入 state，也不更新去重索引。

响应会包含：

```json
{
  "protocol_version": "0.6",
  "agent_id": "01",
  "status": "recorded",
  "dry_run": false,
  "episode_id": "episode_xxx",
  "episode": {},
  "state_transfer_package": {}
}
```

dry-run 响应：

```json
{
  "protocol_version": "0.6",
  "agent_id": "01",
  "status": "preview",
  "dry_run": true,
  "policy_forced_dry_run": false,
  "session_policy": {},
  "would_record_episode": {},
  "state_transfer_package": {}
}
```

重复事件响应：

```json
{
  "protocol_version": "0.6",
  "agent_id": "01",
  "status": "duplicate",
  "dry_run": false,
  "error": "duplicate_event",
  "episode_id": "episode_xxx",
  "duplicate_event": {}
}
```

只有带 `event_id` 的真实写入会更新 `adapter_event_index`。Dry-run 预览不会更新。

真实写入在通过 registry 和 session policy 后，也会创建 protocol-level `adapter_ingest` audit event 和 trace。它和底层 `record_episode` audit event 分开记录。

### Dream

```text
POST /v1/dream
```

请求：

```json
{
  "limit": 20
}
```

## 本地通用客户端

仓库现在提供一个通用客户端：

```python
from one_core.client import AdapterEvent, OneCoreClient

client = OneCoreClient("http://127.0.0.1:8765")
client.interact(
    AdapterEvent(
        message="继续推进 01 Core。",
        user_id="cyberfish",
        channel="local_generic_adapter",
        session_id="local-dev",
    )
)
```

也可以用 CLI 测试：

```bash
python3 -m one_core.cli remote health
python3 -m one_core.cli remote status
python3 -m one_core.cli remote context
python3 -m one_core.cli remote adapters
python3 -m one_core.cli remote interact "继续推进 01 Core。"
python3 -m one_core.cli remote interact "先预览，不写入。" --dry-run --salience-hint 0.8
python3 -m one_core.cli remote dream --limit 50
```

指定端口：

```bash
python3 -m one_core.cli remote --api-base-url http://127.0.0.1:8765 status
```

## AstrBot 当前定位

当前 AstrBot 插件应保持为 thin adapter：

```text
AstrBot event
  ↓
generic adapter protocol
  ↓
01 Core API
```

它暂时不应该：

- 自己解释长期身份；
- 自己管理 01 Core state；
- 自动吸收所有聊天；
- 写入 Angel Memory；
- 直接改 `state.json`。

等通用协议稳定后，再进入 AstrBot 特化阶段：

- 自动会话 allowlist；
- 回复前注入 State Transfer Package；
- 群聊噪声过滤；
- 与 AstrBot provider / persona 的更深集成；
- 对 Angel Memory 的只读迁移或审查式同步。
