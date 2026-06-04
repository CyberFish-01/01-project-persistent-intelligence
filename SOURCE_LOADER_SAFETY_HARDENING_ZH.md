# Source Loader Safety Hardening / 来源加载器安全加固

English version: [SOURCE_LOADER_SAFETY_HARDENING.md](./SOURCE_LOADER_SAFETY_HARDENING.md)

状态：`P116`、`hardening`、`read-only`、`non-runtime`。

P116 在添加 CLI 或 harness integration 前加固 minimal read-only source loader。loader 仍限制在 P113
白名单内，并新增明确的 safety validation output。

## 加固内容

loader 现在暴露：

```text
validate_source_whitelist()
```

validation 会检查：

- duplicate `source_id`；
- unknown source class；
- unknown research line；
- missing pressure types；
- unknown pressure types；
- unsafe whitelist paths；
- missing whitelisted files；
- pressure mappings 引用 unknown source IDs；
- empty pressure mappings。

## Report 新增字段

`build_source_inventory_report()` 现在包含：

- `safety_status`；
- `safety_issues`；
- checked source count；
- checked pressure mapping count；
- validation result 中的 no-write 和 no-external-IO markers；
- unchanged non-execution invariants。

## 保持的边界

P116 不增加：

- CLI command；
- harness integration；
- user path input；
- directory scanning；
- glob expansion；
- state reads；
- state writes；
- adapter reads；
- memory dump reads；
- model calls；
- network calls；
- tool execution；
- policy execution；
- rebuild。

## 保持的研究线边界

CTM-inspired Temporal Dynamics 仍只作为 symbolic source refs：

- temporal awareness；
- temporal coherence；
- review depth / deliberation tick；
- thought trace storage boundary；
- session resume scenarios。

Tool-First In-Situ Self-Evolution 仍只作为 capability source refs：

- tool-first self-evolution；
- capability boundary；
- verification is not authorization；
- tool candidate is not promotion。

## P117 输入

P117 只有在复用 hardened report 且保持以下边界时，才可以添加 `harness-source-inventory` CLI：

- 不创建 state directory；
- 只允许 optional `--output` report write；
- 不接受 user source paths；
- no external IO；
- no model calls；
- 不改 harness runtime。

## 非授权声明

P116 不自动授权 P117，也不授权 runtime、product、adapter、model、tool、memory、recall、identity、
temporal、CTM、reconstruction、policy 或 rebuild work。
