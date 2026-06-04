# Read-Only Source Loader Plan / 只读来源加载器计划

English version: [READ_ONLY_SOURCE_LOADER_PLAN.md](./READ_ONLY_SOURCE_LOADER_PLAN.md)

状态：`P114`、`plan`、`document-only`、`non-runtime`。

P114 把 P113 source inventory 转成 minimal read-only source loader 的实现计划。它不创建
`one_core/source_loader.py`、不加 CLI commands、不读 state logs、不写 state、不调用模型、不执行
retrieval、不接 adapters、不执行工具，也不 rebuild 01。

## 计划规则

```text
source loader 只读取批准过的本地 Markdown。
source refs 只支撑 preview explanation。
source loader 永不写入、永不 external IO、永不接受任意路径。
```

## 最小 Future Module

future implementation target：

```text
one_core/source_loader.py
```

module 应暴露 deterministic helpers：

| Function | 用途 | 边界 |
|---|---|---|
| `load_source_inventory(lang="en")` | 返回某种语言的全部 approved source records。 | 不接受 user paths，不做 glob expansion。 |
| `load_source_record(source_id, lang="en")` | 返回一个 whitelisted Markdown record。 | 拒绝 unknown IDs。 |
| `source_refs_for_pressure(pressure_type, lang="en")` | 返回映射到 harness pressure type 的 approved source refs。 | 不做 dynamic search 或 retrieval。 |
| `build_source_inventory_report(lang="en")` | 返回 read-only inventory report，供 CLI/report 使用。 | 只报告，不读 state。 |
| `render_source_inventory_report(report, output_format)` | 渲染 Markdown 或 JSON。 | 只做 output formatting。 |

## Source Record 形状

每条 source record 应包含：

```yaml
source_id: string
path: string
paired_path: string
lang: en|zh
class: foundation_status|governance_boundary|harness_boundary|temporal_ctm_boundary|capability_boundary|reconstruction_boundary|founder_readability
pressure_types: [string]
research_line: both|CTM-inspired Temporal Dynamics|Tool-First In-Situ Self-Evolution
exists: boolean
heading: string
excerpt: string
read_mode: read_only
source_status: approved_whitelist
missing_reason: string
```

excerpt 应短、deterministic，并从第一个 heading 后的开头内容提取。不能用模型总结。

## 白名单规则

future loader 必须：

- 把 whitelist 作为 constants 存在 `one_core/source_loader.py`；
- 使用 source IDs 作为 public input，而不是任意 paths；
- 支持 English / Chinese paired Markdown paths；
- 只相对 repository root resolve 文件；
- 拒绝 absolute paths 和 path traversal；
- 只读取 whitelist 中命名的 `.md` 文件；
- 保持 deterministic source ordering；
- 对 missing records 返回 `exists: false`，而不是扫描替代文件。

## 禁止读取

loader 不得读取：

- `work/01_state`；
- event logs、memories、recalls、dreams、imports 或 state JSON/JSONL files；
- imported memory exports；
- adapter directories；
- cloud deployment secrets；
- hidden files；
- credentials 或 `.env` files；
- generated caches；
- repository 之外的文件；
- network URLs；
- user-provided file paths。

## Harness Integration Plan

future P118 可以调用：

```text
source_refs_for_pressure(report["input_pressure_type"], lang)
```

并把结果加入 `context_package_preview`：

- `source_refs_preview`；
- `selected_source_refs`；
- `missing_source_evidence`；
- `source_backing_status`；
- `source_loader_boundaries`。

harness 必须保留现有 static refs。Source refs 只解释 preview language 来自哪里；它们不是 prompt context、
memory activation 或 authority。

## CLI Plan

future P117 command：

```bash
python3 -m one_core.cli harness-source-inventory
```

允许参数：

- `--lang en|zh`；
- `--format markdown|json`；
- `--output PATH`。

该 command 只能写显式 report path。它不能创建或修改 state directory。

## P115-P117 需要的测试

future tests 必须证明：

- inventory 能以 English 和 Chinese 加载；
- 所有 whitelist paths 都是 repository-root relative Markdown paths；
- unknown source IDs 会被拒绝；
- pressure mappings 会为 temporal、capability、adapter、product、reconstruction、growth、observability 和 unknown pressure 返回不同 source refs；
- rendered Markdown 和 JSON 包含 non-execution boundaries；
- CLI output 支持 `--output`；
- state directory remains unchanged；
- source files remain unchanged；
- forbidden flags 不会以 active true flags 出现。

## CTM-Inspired Temporal Dynamics 处理

loader 只能从白名单文档暴露 CTM-related source refs：

- `ctm_temporal_dynamics`；
- `temporal_coherence_eval`；
- `deliberation_tick`；
- `thought_trace_storage`；
- `temporal_awareness`；
- `session_resume`。

它不得推断 consciousness、neural synchronization、thought loops、model training、private reasoning 或
temporal runtime。

## Tool-First In-Situ Self-Evolution 处理

loader 只能从白名单文档暴露 capability source refs：

- `tool_first_self_evolution`；
- `capability_evolution_boundary`；
- `deliberation_tick`；
- `risk_register`。

它不得授权 tool execution、automatic tool promotion、tool-library mutation、policy execution、dependency
installation 或 subject growth。

## Failure Mode

如果 source 不能读取，loader 应报告：

```yaml
exists: false
missing_reason: missing_whitelisted_file
```

它不应搜索附近文件、fetch remote content 或替换成其他 source。

## P115 Exit Criteria

只有满足以下条件，P115 才算完成：

- `one_core/source_loader.py` 存在；
- 它只读取 P113 whitelist；
- tests 证明 deterministic 和 no-write；
- 除非后续 phase 明确要求，否则不加 CLI 或 harness integration；
- 所有 forbidden pattern searches 通过。

## 非授权声明

P114 只是计划。它不实现 source loader、source inventory CLI、harness source refs、source-backed
risks/open questions、state-backed verification、runtime work、product work、adapter integration、model
calls、真实 retrieval、state writes、memory writes、recall writes、identity mutation、tool execution、CTM
runtime、temporal runtime、policy execution、rebuild 或 external IO。
