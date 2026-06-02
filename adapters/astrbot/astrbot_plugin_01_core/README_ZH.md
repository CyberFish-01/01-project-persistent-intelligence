# 01 Core AstrBot Adapter

英文镜像：[README.md](./README.md)

这是 01 Core 的第一版 AstrBot 适配器。

它的定位很窄：

```text
AstrBot = 外部入口
01 Core = 连续性状态所有者
```

适配器不直接读写 `state.json`，也不复用 AstrBot 或 Angel Memory 的内部记忆结构。它只通过 01 Core HTTP API 交互。

## 准备

先在 01 Project 仓库里启动 01 Core API：

```bash
python3 -m one_core.cli serve
```

默认地址：

```text
http://127.0.0.1:8765
```

## 安装

把整个目录复制到 AstrBot 插件目录：

```text
adapters/astrbot/astrbot_plugin_01_core
```

目标目录示例：

```text
/root/data/plugins/astrbot_plugin_01_core
```

然后在 AstrBot 中重载或重启插件。

## 命令

```text
/01 ping
/01 status
/01 context
/01 chat <内容>
/01 dream [limit]
```

含义：

- `/01 ping`：检查 01 Core API 是否在线。
- `/01 status`：查看当前身份、目标、记忆数量、待整理 dream job。
- `/01 context`：查看压缩后的 State Transfer Package 摘要。
- `/01 chat <内容>`：把一次 AstrBot 消息写入 01 Core episode。
- `/01 dream [limit]`：触发一次 Dream consolidation。

## 第一版边界

这一版故意不默认监听全部聊天。

原因是：01 的连续性状态应该先可审查、可回滚、可解释。自动吸收所有消息很容易把噪声、群聊上下文、无关用户内容混入身份成长过程。

后续可以加：

- allowlist 会话；
- 自动记录高显著性消息；
- 回复前自动注入 State Transfer Package；
- AstrBot provider 前置上下文 adapter；
- token 权限；
- 远程 API TLS。
