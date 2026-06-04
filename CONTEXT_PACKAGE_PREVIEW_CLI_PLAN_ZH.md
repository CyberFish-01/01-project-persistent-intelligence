# 上下文包预览 CLI 计划

English version: [CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md](./CONTEXT_PACKAGE_PREVIEW_CLI_PLAN.md)

状态：`P138`、`CLI-plan`、`document-only`、`non-runtime`。

P138 规划 future read-only context package preview CLI。它不实现 command、parser、builder、retrieval engine、model call、prompt execution、state write、memory write、recall write、identity mutation、adapter integration、tool execution、policy executor 或 rebuild。

## 未来命令形状

可能的 future command：

```bash
python3 -m one_core.cli context-package-preview
```

可能的 future parameters：

- `--input TEXT`
- `--session-id ID`
- `--actor-id ID`
- `--lang en|zh`
- `--format markdown|json`
- `--output PATH`
- `--pressure-type TYPE`
- `--no-write`

P138 不新增这个命令。

## 输出 Sections

未来 preview 应包含：

- `package_summary`
- `identity_pack`
- `state_pack`
- `task_pack`
- `claim_pack`
- `memory_pack`
- `boundary_pack`
- `temporal_pack`
- `capability_pack`
- `response_strategy_pack`
- `selected_sources`
- `omitted_sources`
- `risk_flags`
- `non_execution_invariants`

## CLI 边界

future CLI 必须是：

- local-only；
- deterministic；
- read-only；
- report-output-only；
- source-transparent；
- founder-readable；
- no model call；
- no external IO；
- no adapter integration；
- no formal state mutation；
- no rebuild。

## No-Write Invariants

未来 output 应明确包含：

- `context_package_preview_only: true`
- `model_call_enabled: false`
- `external_io_enabled: false`
- `state_unchanged: true`
- `memory_write_allowed: false`
- `recall_write_allowed: false`
- `identity_mutation_allowed: false`
- `tool_execution_allowed: false`
- `adapter_integration_allowed: false`
- `rebuild_allowed: false`

这些是 planned output fields，不是 P138 已实现 flags。

## Founder-Facing Markdown 形状

Markdown report 应按这个顺序可读：

1. 这个 package 用来做什么。
2. 哪些 sources 被 selected。
3. 哪些被 omitted，为什么。
4. 哪些 boundaries active。
5. 哪些 temporal 和 capability cues 只是 review material。
6. 未来 model 作为 resource 会被要求做什么。
7. 明确没有发生什么。

## JSON 形状

JSON 应保持和 Markdown 相同结构，方便未来 tests 断言：

- all required packs exist；
- all trust levels are explicit；
- all selected sources have reasons；
- all omitted sources have reasons；
- all forbidden capabilities remain false；
- no package item claims promotion or persistence。

## CTM-Inspired Temporal CLI 边界

future `temporal_pack` preview 可以显示 elapsed time、interruption、delayed alignment、unresolved tension 和 review depth suggestions。CLI 不能执行 ticks、写 thought traces、创建 temporal events、创建 recall events 或声称 consciousness。

## Tool-First CLI 边界

future `capability_pack` preview 可以显示 tool candidates、procedure candidates、verification evidence 和 review routes。CLI 不能执行工具、授权工具、晋升工具、安装依赖或修改任何 tool library。

## 未来 Tests Plan

如果后续批准 implementation，tests 应验证：

- CLI 在 Markdown 和 JSON 下运行；
- zh output 使用 founder-facing labels；
- all nine required packs appear；
- selected 和 omitted sources 存在；
- forbidden capabilities disabled；
- no formal state changes；
- output file 只在明确请求时写入；
- repeated input deterministic；
- invalid input fail closed。

## 完成声明

P138 规划 context package preview CLI，但不实现它。它把 P137 的 package contract 转成 future local、deterministic、read-only report surface，同时保持 model calls 和 writes blocked。
