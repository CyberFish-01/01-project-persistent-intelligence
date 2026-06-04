# 重构前验证套件

English version: [PRE_REBUILD_VERIFICATION_SUITE.md](./PRE_REBUILD_VERIFICATION_SUITE.md)

状态：`P151`、`implementation`、`read-only`、`pre-rebuild-verification`。

P151 新增一个本地只读验证套件命令：

```bash
python3 -m one_core.cli pre-rebuild-verification
```

它生成一份报告，说明仓库是否已经准备好进入最终验证报告阶段。它不开始 rebuild、不连接旧
01、不连接 AstrBot、不调用模型、不执行工具、不写 state、不写 memory、不写 recall event、不修改
identity、不执行 temporal runtime、不执行 reconstruction reducer、不压缩 event，也不自动批准下一阶段。

## 为什么需要它

P150 已经定义 rebuild 前完整验证计划，但计划本身还需要一个 deterministic local report surface。P151
把这个计划落成只读套件，让 P152 可以基于证据出验证报告，而不是只写人工判断。

这个套件回答：

- P112-P151 必需文档是否都有中英文版本；
- PHASE_INDEX、RFC_INDEX 和 README 是否指向当前阶段；
- local Markdown links 是否可解析；
- active forbidden true flags 是否缺席；
- 既有只读 report builders 是否仍能生成安全输出；
- CTM-inspired 和 Tool-First 两条线是否仍保持 symbolic、candidate/evidence、review-only；
- rebuild 是否仍明确没有开始。

## CLI

```bash
python3 -m one_core.cli pre-rebuild-verification
python3 -m one_core.cli pre-rebuild-verification --format json
python3 -m one_core.cli pre-rebuild-verification --lang zh
python3 -m one_core.cli pre-rebuild-verification --format markdown --output /tmp/pre_rebuild_verification.md
```

参数：

| Option | Values | Meaning |
|---|---|---|
| `--format` | `markdown`, `json` | 输出形状；默认 `markdown`。 |
| `--lang` | `en`, `zh` | 报告语言；默认 `en`。 |
| `--output` | path | 可选，显式写出报告文件。 |

命令只有在提供 `--output` 时才写文件，并且只写用户请求的报告 artifact。它不创建或修改 state
目录。

## 报告内容

报告包含：

- `verification_summary`
- `gate_results`
- `required_artifacts`
- `future_artifacts`
- `phase_index_status`
- `index_status`
- `readme_status`
- `forbidden_pattern_status`
- `markdown_link_status`
- `read_only_cli_status`
- `boundary_status`
- `ctm_temporal_status`
- `tool_first_status`
- `verification_commands_for_p152`
- `non_execution_invariants`

## 内部检查什么

P151 只做 deterministic local checks：

- artifact presence；
- Markdown local link resolution；
- forbidden active-pattern search；
- PHASE_INDEX、RFC_INDEX 和 README current-phase coverage；
- in-process 生成既有只读报告：
  - `foundation-observatory-report`；
  - `harness-source-inventory`；
  - `harness-dry-run` reconstruction pressure。

它内部不 shell out 到 Git，不运行完整 unit test suite，也不运行 format checks。这些保留为 P152 的显式验证命令，方便直接记录输出证据。

## 非执行边界

套件输出会显式记录：

- `pre_rebuild_verification_report_only`
- `execution_prohibited`
- `state_unchanged`
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

带危险含义的字段在生成报告中保持禁用。

## 和 P152 的关系

P151 创建套件。

P152 应运行该套件，运行 P150 要求的 shell checks，并写出
`VERIFICATION_REPORT.md` / `VERIFICATION_REPORT_ZH.md`。

P151 不决定可以开始 rebuild。

## 停止边界

P151 之后，安全下一阶段是 P152 Verification Report。直到 founder 收到并批准最终 pre-rebuild
checkpoint 之前，rebuild 继续保持 blocked。
