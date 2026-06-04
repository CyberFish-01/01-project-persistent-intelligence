# 重构入口门清单

English version: [REBUILD_ENTRY_GATE_CHECKLIST.md](./REBUILD_ENTRY_GATE_CHECKLIST.md)

状态：`P148`、`checklist`、`document-only`、`non-runtime`。

P148 定义本地 01 rebuild 被考虑前必须满足的 checklist。它不运行 verification、不开始 rebuild、不读取旧 01、不写 state、不迁移 memory、不连接 adapters、不调用模型、不执行工具、不运行 reducers、不压缩 events、不修改 identity。

## 就绪度区分

```text
ready for verification 不是 ready for rebuild。
ready for rebuild 需要 verification evidence 和 founder checkpoint。
```

P148 只定义 gates。

## 必需 Gates

| Gate | Requirement | Evidence Needed |
|---|---|---|
| git cleanliness | final prep 后 worktree clean。 | `git status --short` empty |
| format check | 无 whitespace diff errors。 | `git diff --check` passes |
| markdown links | Local Markdown links resolve。 | link check passes |
| forbidden search | 无 forbidden active pattern。 | forbidden search no matches |
| unit tests | Existing tests pass。 | `python3 -m unittest` passes |
| phase index | PHASE_INDEX 覆盖 latest phase。 | 后续存在 P154 row |
| README status | README 反映 current phase。 | README / ZH updated |
| RFC index | 新 RFC/review docs 已索引。 | RFC_INDEX / ZH current |
| source safety | 未读取 old 01。 | source boundary statement |
| no-write proof | 无 formal state/memory/event mutation。 | before/after evidence |
| model boundary | 未发生 LLM call。 | command audit |
| adapter boundary | 未连接 AstrBot/external adapter。 | boundary audit |
| tool boundary | 未执行或晋升 tool。 | boundary audit |
| temporal boundary | 无 temporal/CTM runtime。 | boundary audit |
| founder checkpoint | Founder 明确批准 rebuild start。 | future manual approval |

## 当前预期状态

在 P148，预期状态是：

- documentation gates 正在准备；
- verification suite 以后可以规划；
- rebuild 未被批准；
- 旧 01 未被读取；
- 没有执行 migration。

## Rebuild Blockers

如果出现这些情况，rebuild 必须保持 blocked：

- any test fails；
- any forbidden pattern appears；
- markdown links fail；
- worktree dirty 且无解释；
- source trust unclear；
- old 01 material 未 quarantine；
- founder checkpoint missing；
- verification report missing；
- rebuild scope ambiguous。

## CTM 和 Tool-First Gates

entry gate 必须确认：

- CTM-inspired work 保持 symbolic 和 review-only；
- 不存在 thought loop 或 temporal runtime；
- Tool-First work 保持 candidate/evidence/review only；
- 不存在 automatic tool execution 或 promotion。

## 完成声明

P148 定义 future local rebuild 的 entry checklist。它不让项目变成 rebuild-ready；它定义 later evidence 必须证明什么。
