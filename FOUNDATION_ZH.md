# 01 Project Foundation

英文镜像：[FOUNDATION.md](./FOUNDATION.md)

这份文档定义 01 Project 的工程地基。

它不是愿景扩写，也不是功能清单。它回答一个更底层的问题：

> 后续所有实现、文档、adapter、云端部署和 AstrBot 集成，必须服从哪些不变量？

## 1. 核心命题

```text
Continuity != Memory Retrieval
Continuity = State Transfer
```

01 Project 研究的是“状态如何穿过时间”，而不是“怎样检索更多旧信息”。

记忆是连续性的一部分，但不是连续性本身。一个系统可以记得很多事实，却仍然丢失身份、意图、关系边界、任务状态和更新理由。

## 2. 稳定单位

01 的稳定单位是：

```text
Identity
```

不是：

```text
conversation
session
platform
adapter
model provider
```

对话是临时表面。平台是外部身体。模型是推理引擎。adapter 是翻译层。

只有 01 Core 拥有长期状态。

## 3. 分层边界

### 01 Core

01 Core 负责：

- identity core；
- working state；
- memory stores；
- relationship map；
- project map；
- dream queue；
- adapter registry；
- audit/update log；
- state transfer package。

01 Core 是状态所有者。

### Dream Engine

Dream Engine 负责把经历整理为经验：

- episode compression；
- semantic abstraction；
- conflict detection；
- forgetting proposals；
- identity update proposals。

Dream Engine 可以提出身份更新，但不能绕过 gate 直接改写 identity core。

### Adapters

Adapter 负责把外部平台事件翻译成 01 Core 协议。

Adapter 不负责：

- 解释长期身份；
- 管理长期记忆；
- 自动吸收全部聊天；
- 写入 Angel Memory；
- 直接修改 `state.json`；
- 替 01 Core 决定什么应该成为 identity。

### Platforms

AstrBot、Web UI、Telegram、Discord、云服务都只是外部入口。

平台可以承载 01，但不拥有 01。

## 4. 状态层更新速度

状态层必须按不同速度更新：

```text
Current Context: fast
Working State: fast
Episodic Memory: medium
Semantic Memory: slower
Identity Core: slowest
```

单次交互可以更新当前上下文和 episode。

多次证据才能支持 semantic memory。

Identity Core 必须慢、可审计、可回滚，并且不能被单次消息覆盖。

## 5. 工程不变量

后续每个版本都应该保护这些不变量：

- 01 Core owns state.
- Adapters translate platforms.
- Platforms do not own identity.
- `dry_run` 不写入 episode，不创建 dream job，不更新去重索引。
- `salience_hint` 只是建议，01 Core 不无条件采纳。
- 有 `event_id` 的 adapter 写入必须可去重。
- identity update 必须有 gate、证据、理由和审计记录。
- imported memory 默认 staged，不直接更新 identity core。
- memory lifecycle 的目标不是保存一切，而是决定保留、抽象、归档或遗忘。
- 每个 session 都必须能恢复三个锚点：Who am I? Where am I? What am I doing?

## 6. 当前阶段

当前阶段是：

```text
Local generic 01 Core
```

优先级：

1. 本地 state runtime 稳定；
2. adapter protocol 稳定；
3. memory import / cleanup 稳定；
4. dream consolidation 稳定；
5. evaluation scenarios 稳定；
6. 再更新云端；
7. 再做 AstrBot 特化。

现在不追求：

- 多平台同时接入；
- 自动吸收所有聊天；
- 复杂人格表现；
- 大规模 UI；
- 未经验证的云端常驻逻辑；
- AstrBot 内部深度人格化。

## 7. 正确的集成顺序

推荐顺序：

```text
local core
  -> local HTTP API
  -> generic adapter protocol
  -> local verification
  -> GitHub commit
  -> cloud deploy
  -> thin platform adapter
  -> specialized adapter
```

不要跳过本地验证直接上云。

不要让 AstrBot 先拥有长期状态。

不要把平台适配误认为 01 Core 成熟。

## 8. 最小可测标准

一个改动只有在至少通过这些检查后，才算进入地基：

- 本地测试通过；
- dry-run 行为可验证；
- 真实写入行为可验证；
- state 变化可解释；
- 文档和代码一致；
- 不破坏旧兼容入口；
- 不扩大平台权限；
- 不引入不可审计的 identity update。

## 9. 判断一个想法是否偏离

如果一个想法主要在回答：

- 怎样让 AstrBot 更像 01？
- 怎样让聊天更自动？
- 怎样表现得更人格化？
- 怎样把更多数据塞进记忆？

它可能还不是当前阶段的地基。

如果一个想法在回答：

- 状态如何持久？
- 状态如何迁移？
- 状态如何被审计？
- 身份如何慢更新？
- 平台如何不拥有身份？
- 记忆如何从 raw data 变成 experience？

它更接近当前阶段的地基。

## 10. 一句话

01 Project 的地基不是“让 AI 记得更多”。

它是：

> 让一个智能体的身份、上下文、意图、记忆生命周期和更新历史，以可验证、可审计、可迁移的形式穿过时间。
