# 创始人控制台无写入契约

English version: [FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md](./FOUNDER_CONSOLE_NO_WRITE_CONTRACT.md)

状态：`P133`、`contract`、`document-only`、`non-runtime`。

P133 定义 future Thin Founder Console 的 no-write contract。它不实现 console、command、validator、Web UI、Companion、adapter、model call、tool execution、state write、memory write、recall write、identity mutation、policy executor 或 rebuild。

## 契约规则

```text
console 可以生成 reports。
console 不能改变 core state。
report output 不是 memory。
preview output 不是 event。
```

## 允许读取

future console 只能读取 explicitly approved local sources：

- foundation Markdown documents；
- RFC 和 review Markdown documents；
- explicitly selected 的 existing read-only report output；
- source loader whitelist records；
- 同一 no-write session 中生成的 deterministic harness dry-run output。

它不能读取：

- 旧 01 material；
- external network sources；
- adapter exports；
- private chat logs；
- credentials 或 environment files；
- unapproved local directories；
- formal state directories，除非后续 phase 明确批准 read-only state inspection。

## 允许写入

future console 唯一可能的写入，是 founder 明确要求的 report file。

这个 report file 必须：

- founder-requested；
- 位于 formal state/event/memory/identity stores 之外；
- 标记为 report-only；
- 包含 non-execution invariants；
- 不成为 automatic promotion 的输入；
- 不创建 candidate lifecycle state。

## 禁止写入

console 绝不能写：

- `state.json`；
- `episodes.jsonl`；
- `dreams.jsonl`；
- `imports.jsonl`；
- formal event logs；
- memory stores；
- recall events；
- identity files；
- task state；
- claim graph state；
- growth candidate lifecycle files；
- tool library files；
- adapter queues；
- quarantine storage；
- rebuild migration files。

## 必需不变量

未来每份 console report 都应包含：

- `founder_console_report_only: true`
- `execution_prohibited: true`
- `state_unchanged: true`
- `formal_state_write_allowed: false`
- `memory_write_allowed: false`
- `event_write_allowed: false`
- `recall_write_allowed: false`
- `identity_mutation_allowed: false`
- `tool_execution_allowed: false`
- `adapter_integration_allowed: false`
- `model_call_allowed: false`
- `rebuild_allowed: false`

这些字段在 P133 是 contract language，不是已实现 runtime flags。

## 验证预期

如果 console 后续被实现，tests 必须验证：

- 运行 console 不改变 formal state directories；
- 只有显式 `--output` 或等价参数时才创建 output files；
- report output 不包含 promotion claim；
- boundary monitor 保持可见；
- 不发生 external IO；
- 不发生 model call；
- 不发生 adapter 或 tool execution；
- 所有 candidates 保持 preview-only。

## CTM-Inspired Temporal 边界

Temporal report sections 可以把 pressure、delay、unresolved tension 或 review depth 摘要为 symbols。它们不得写 temporal events、recall events、thought traces、salience changes、CTM runtime state 或 identity updates。

## Tool-First 边界

Capability report sections 可以把 tool/procedure candidates 和 verification evidence 摘要为 review material。它们不得执行工具、晋升工具、修改工具库、安装依赖或授权 procedures。

## Failure Handling

如果 future console 不能证明 no-write behavior，它必须 fail closed：

- 停止运行；
- 如果安全，则生成 report-only error；
- 除非明确标记 incomplete，否则避免 partial outputs；
- 绝不继续进入 execution。

## 完成声明

P133 把 future founder console 定义为 report-output-only。它可以帮助 founder 看见和决定，但不能写 core history、修改 identity、晋升 candidates、连接 adapters、调用模型、执行工具或开始 rebuild。
