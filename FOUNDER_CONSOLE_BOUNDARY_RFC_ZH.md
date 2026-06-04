# 创始人控制台边界 RFC

English version: [FOUNDER_CONSOLE_BOUNDARY_RFC.md](./FOUNDER_CONSOLE_BOUNDARY_RFC.md)

状态：`P131`、`RFC-only`、`document-only`、`non-runtime`。

P131 定义 future Thin Founder Console 的边界。它不实现 console、CLI command、Web UI、Companion behavior、adapter integration、model call、state write、memory write、recall write、identity mutation、tool execution、policy executor 或 rebuild。

## 问题说明

harness 和 lockdown blocks 之后，founder 需要一个本地表面，让 01 Core 的状态变得可读，但不能假装自己已经是产品。

console 应该回答 founder 的问题：

- core 现在能看见什么？
- 哪些仍然 blocked？
- 哪些风险最高？
- 哪些 candidates 只是 previews？
- 哪个下一步需要 founder approval？

它不应该变成聊天产品、agent loop、dashboard runtime、social companion 或 adapter entry point。

## 边界规则

```text
founder console 是 local control surface。
control surface 不是 product。
visibility 不是 execution。
review 不是 write permission。
```

## 允许范围

未来 Thin Founder Console 可以：

- 读取 approved local Markdown 和 static reports；
- 调用 existing read-only report generators；
- 展示 harness dry-run previews；
- 展示 source inventory summaries；
- 展示 boundary status；
- 展示 risk 和 open-question summaries；
- 仅在 founder 要求 output file 时写 report outputs；
- 在有帮助时使用 founder-facing 中文显示名。

## 禁止范围

它绝不能：

- 实现 Web UI 或 dashboard runtime；
- 扮演 Companion 或用户产品；
- 连接 AstrBot、Telegram、QQ、browser adapters 或任何 external adapter；
- 调用 LLMs 或 external APIs；
- 执行工具；
- 写正式 state、events、memory、recall、identity、growth、temporal 或 capability records；
- 修改 Identity Core；
- 重写 memory；
- 运行 reconstruction reducers；
- 压缩 events；
- 执行 policy；
- 自动选择 roadmap；
- 开始 rebuild。

## 最小表面

console 未来可以暴露这些 read-only panels：

| Surface | Purpose | Boundary |
|---|---|---|
| observatory snapshot | 显示 foundation status。 | display-only |
| harness dry-run | 显示一条输入会如何 route。 | preview-only |
| source inventory | 显示 approved local sources。 | whitelist-only |
| lockdown status | 显示 blocked external pressure。 | no enforcement |
| review queue preview | 显示 candidates 未来会在哪里被 review。 | no lifecycle |
| next-step candidates | 显示可能方向。 | no automatic roadmap |

## CTM-Inspired Temporal Dynamics 位置

console 可以显示 symbolic temporal cues：

- temporal pressure；
- elapsed-time warning；
- review depth suggestion；
- unresolved tension note；
- thought-trace policy reminder。

它不能把这些显示为 CTM runtime、thought execution、neural synchronization、temporal events、recall writes 或 identity updates。

## Tool-First Self-Evolution 位置

console 可以显示 capability cues：

- tool candidate；
- procedure candidate；
- verification evidence preview；
- cautionary procedural memory candidate；
- capability review gate。

它不能执行工具、授权工具、晋升 procedures、安装依赖，或把 capability evolution 当成 subject growth。

## Founder 控制要求

未来 console 必须明确显示：

- 每个 next step 都是 candidate；
- 每个 write-like action 都 blocked；
- 每个 external connection 都 blocked；
- 每个 promotion 都需要 founder review；
- 每个 output file 都是 user-requested 且 report-only；
- 任何 warning 都不能自动触发下一步。

## 未来验收方向

P131 不批准 implementation。如果后续 implementation 被批准，最低 acceptance bar 应要求：

- local-only execution；
- no external network；
- no model call；
- no state directory mutation；
- deterministic output；
- clear boundary monitor；
- founder-readable Chinese labels；
- 所有 write-like capabilities disabled。

## 完成声明

P131 把 Thin Founder Console 定义为 local、founder-only、no-write visibility layer。它是用来看见和决定的 control surface，不是用来行动的 product surface。
