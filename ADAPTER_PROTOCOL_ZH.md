# 01 Core Adapter Protocol

英文镜像：[ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md)

这是 01 Core 的通用接入协议。

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

### Interaction

```text
POST /v1/interact
```

请求：

```json
{
  "message": "用户或外部平台输入",
  "user_id": "平台内用户 ID",
  "channel": "平台或 adapter 名称",
  "session_id": "平台内会话 ID"
}
```

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
python3 -m one_core.cli remote interact "继续推进 01 Core。"
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
