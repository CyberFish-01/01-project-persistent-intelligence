# 重构迁移协议 RFC

English version: [REBUILD_MIGRATION_PROTOCOL_RFC.md](./REBUILD_MIGRATION_PROTOCOL_RFC.md)

状态：`P147`、`RFC-only`、`document-only`、`non-runtime`。

P147 定义未来进入本地 01 rebuild 和 migration path 的协议。它不开始 rebuild、不读取旧 01、不迁移 state、不导入文件、不运行 reducers、不压缩 events、不写 state、不写 memory、不修改 identity、不连接 adapters、不调用模型、不执行工具、不运行 policy。

## 核心规则

```text
rebuild migration requires entry gates。
entry gate 不是 rebuild start。
migration plan 不是 migration execution。
old 01 material 在 review 前默认 untrusted。
```

## Entry Preconditions

未来任何 local rebuild 开始前，项目必须具备：

- clean git status；
- full tests passing；
- markdown link check passing；
- forbidden pattern search passing；
- 需要时的 push readiness decision；
- pre-rebuild verification report；
- founder checkpoint；
- approved source trust policy；
- import quarantine route；
- no-write validation evidence；
- explicit rebuild scope。

## Migration Source Classes

future migration 只能在批准后考虑这些 source classes：

- foundation documents；
- current source loader whitelist；
- static reports；
- old 01 code references；
- old 01 memory material；
- adapter artifacts；
- logs or exports；
- founder decision notes。

Old 01 memory material、adapter artifacts、logs 和 exports 默认 untrusted，必须通过 quarantine。

## Migration Non-Goals

future rebuild migration 不得：

- 把 old bugs 保存成 identity；
- 把 old memory 当成 truth 导入；
- 把 old adapter context 当成 state；
- 把 model output 当成 memory；
- 在没有 policy 时 compact events；
- rewrite Identity Core；
- auto-promote growth candidates；
- auto-enable tools；
- 连接 AstrBot；
- 启动 user product behavior。

## Rebuild Gate Sequence

| Gate | Purpose | Failure Outcome |
|---|---|---|
| foundation gate | 确认 boundaries 和 phase index 当前有效。 | stop |
| source trust gate | 确认哪些 sources 可以读取。 | stop |
| quarantine gate | 检查前先路由 untrusted material。 | stop or quarantine |
| no-write validation gate | 证明 preview tooling 不修改 state。 | stop |
| context package gate | 确认 context packs 已定义。 | stop |
| response boundary gate | 确认 LLM 只是 resource。 | stop |
| verification gate | 运行 pre-rebuild verification suite。 | stop or block |
| founder checkpoint | Founder 批准 local rebuild start。 | stop |

## CTM-Inspired Temporal 边界

Temporal artifacts 可以告知 rebuild review，但不能在 migration 中变成 runtime state。Migration 不得创建 temporal events、recall events、thought traces、salience mutation、CTM runtime 或 identity update。

## Tool-First 边界

Capability artifacts 可以告知 rebuild review，但不能在 migration 中变成 trusted tools。Migration 不得创建 tool execution、tool promotion、dependency installation、tool library mutation、policy executor 或 subject-growth claim。

## 第一类允许的未来写入

如果后续 verification 后批准，第一类 allowed write 应是低风险 local founder/review note，而不是 memory、identity、recall、growth、tool、adapter 或 event migration。

P147 甚至不批准这个写入。

## Stop Conditions

future migration planning 遇到这些情况必须停止：

- old 01 source trust 不清楚；
- tests fail；
- forbidden active pattern appears；
- no-write preview 期间 state 发生变化；
- adapter pressure appears；
- 需要 model call 才能继续；
- 缺少 founder approval；
- rebuild scope ambiguous。

## 完成声明

P147 把 rebuild migration 定义为 gated future protocol，而不是 action。它为 final pre-rebuild verification 做准备，同时保持 old 01、adapters、models、writes 和 rebuild execution blocked。
