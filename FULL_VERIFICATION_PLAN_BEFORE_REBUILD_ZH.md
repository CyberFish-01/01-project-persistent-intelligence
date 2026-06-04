# 重构前完整验证计划

English version: [FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md](./FULL_VERIFICATION_PLAN_BEFORE_REBUILD.md)

状态：`P150`、`verification-plan`、`document-only`、`non-runtime`。

P150 定义 local 01 rebuild 前的完整验证计划。它不运行 suite、不开始 rebuild、不读取旧 01、不迁移 state、不写 memory、不连接 adapters、不调用模型、不执行工具、不运行 reducers、不压缩 events、不修改 identity。

## 验证目标

证明仓库已经准备好 **开始 read-only verification pass**，并在该 pass 之后让 founder 判断是否可以开始 local rebuild。

Verification 不能变成 rebuild。

## Verification Areas

| Area | Check |
|---|---|
| repository state | branch、clean status、latest commits |
| formatting | `git diff --check` |
| tests | `python3 -m unittest` |
| markdown links | local Markdown link check |
| forbidden patterns | active forbidden pattern search |
| phase coverage | PHASE_INDEX / ZH reaches current phase |
| index coverage | RFC_INDEX / ZH includes new artifacts |
| README status | README / ZH reflects latest phase |
| required artifacts | P112-P154 required docs exist |
| CLI read-only commands | observatory、harness、source inventory still run |
| no-write evidence | state/report-only boundaries preserved |
| CTM boundary | no CTM runtime or thought loop |
| Tool-First boundary | no tool execution or promotion |
| adapter boundary | no AstrBot/external adapter integration |
| rebuild boundary | no rebuild start or migration |

## Required Commands

read-only suite 应运行：

```bash
git status --short
git branch --show-current
git diff --check
python3 -m unittest
python3 -m one_core.cli foundation-observatory-report --format json --lang en
python3 -m one_core.cli foundation-observatory-report --format json --lang zh
python3 -m one_core.cli harness-source-inventory --format json --lang en
python3 -m one_core.cli harness-source-inventory --format json --lang zh
python3 -m one_core.cli harness-dry-run --input "pre-rebuild verification" --format json --lang en
python3 -m one_core.cli harness-dry-run --input "重构前验证" --format json --lang zh
```

它还应运行 local Markdown link 和 forbidden-pattern checks。

## Forbidden Pattern Set

Verification 必须搜索 active true flags。为了让仓库自身的 forbidden-pattern check 保持干净，本计划把字段名和 blocked value `true` 分开列出：

- `identity_core_mutated`
- `memory_rewrite_executed`
- `recall_mutation_executed`
- `growth_engine_executed`
- `temporal_event_executed`
- `tool_execution_enabled`
- `auto_tool_promotion_enabled`
- `policy_executor_enabled`
- `companion_feature_enabled`
- `adapter_integration_required`
- `harness_write_enabled`
- `ctm_runtime_enabled`
- `external_io_enabled`
- `model_call_enabled`
- `source_loader_write_enabled`
- `app_write_enabled`
- `rebuild_started`

## Pass Criteria

verification pass 只有在以下条件全部满足时才成功：

- all commands pass；
- no forbidden pattern appears；
- required artifacts exist；
- local links resolve；
- tests pass；
- no state mutation is observed；
- 不需要 model、adapter、external IO、tool 或 rebuild action。

## Failure Handling

如果 verification 失败：

- 不要 rebuild；
- 写 blocked/failure report；
- 列出 failing command 和 evidence；
- 不要通过连接 external services 绕过；
- 不要调用模型解释 failures；
- 不要通过修改 state 来修复 verification。

## CTM And Tool-First Verification

计划必须确认：

- CTM-inspired work is symbolic/review-only；
- no thought loop or temporal runtime exists；
- Tool-First work is candidate/evidence/review-only；
- no tool execution、auto-promotion 或 policy executor exists。

## 完成声明

P150 定义 verification plan。它准备 P151 只实现或运行 read-only verification suite，而不开始 rebuild。
