# State-Backed Read-Only Harness RFC

English version: [STATE_BACKED_READ_ONLY_HARNESS_RFC.md](./STATE_BACKED_READ_ONLY_HARNESS_RFC.md)

状态：`P112`、`RFC`、`planning`、`document-only`、`non-runtime`。

P112 定义 future state-backed read-only harness 的边界。它不实现 source loader、CLI command、
context preview change、state read execution、retrieval、model call、adapter integration、memory
write、recall write、identity mutation、tool execution 或 rebuild。

## 问题

P102-P110 让 `harness-dry-run` 变得可读：不同输入现在会路由到不同 pressure profiles、candidates、
review gates、boundaries 和人工下一步。

剩余弱点是：harness 仍不能显示现有项目证据是否支持这个 preview。它能说“这像 adapter pressure”或
“这像 temporal pressure”，但还不能引用定义这些边界的本地文档。

所以下一条安全边界不是 runtime，而是 **read-only source backing**。

## 定义

State-backed read-only harness 指：

```text
读取批准过的本地项目资料
  -> 总结 source refs 和 gaps
  -> 把 source_refs 附到 preview output
  -> 所有 candidates 继续 preview-only
  -> 所有 review gates 继续 manual-review-only
  -> 不写 state、memory、recall、identity、events、tools 或 tasks
```

`state-backed` 不等于 identity state mutation、memory retrieval、event replay、reducer execution 或
context persistence。它只表示 harness 可以读取一个很窄的本地项目 artifact 白名单，并在 dry-run report
里引用它们。

## 允许读取的来源

第一类允许来源是仓库根目录下白名单 Markdown：

- foundation maps and indexes；
- RFCs and policy documents；
- usability reviews；
- roadmaps and summaries；
- open questions and risk registers；
- boundary and glossary documents。

允许来源必须按文件名显式列出。禁止 directory traversal、来自用户输入的 glob、network fetches、adapter
exports、cloud files、hidden files、`.env` files、state JSONL logs 和 imported memory dumps。

## 允许输出

future harness output 可以增加：

- `source_refs_preview`；
- `selected_source_refs`；
- `omitted_source_refs`；
- `missing_source_evidence`；
- `source_backing_status`；
- `source_loader_boundaries`；
- source-derived open questions and risk hints。

这些只是 report fields。它们不是 context persistence、prompt construction、retrieval execution、
memory activation 或 review lifecycle creation。

## 非执行不变量

每个 future state-backed harness report 必须继续声明：

```yaml
read_only_source_backing: true
state_unchanged: true
execution_prohibited: true
identity_core_mutated: false
memory_rewrite_executed: false
recall_mutation_executed: false
growth_engine_executed: false
temporal_event_executed: false
tool_execution_enabled: false
auto_tool_promotion_enabled: false
policy_executor_enabled: false
companion_feature_enabled: false
adapter_integration_required: false
harness_write_enabled: false
external_io_enabled: false
model_call_enabled: false
source_loader_write_enabled: false
rebuild_started: false
```

## CTM-Inspired Temporal Dynamics 边界

Temporal Dynamics 只能作为 symbolic、observable、reviewable source refs 出现：

- Temporal Awareness RFC references；
- temporal coherence evaluation references；
- review depth / deliberation tick vocabulary；
- unresolved tension 和 delayed alignment notes；
- thought trace storage boundary notes。

本 RFC 不允许 neural CTM claims、model training、真实 thought loops、temporal runtime、temporal event
writes、hidden chain-of-thought capture 或 automatic deliberation execution。

## Tool-First In-Situ Self-Evolution 边界

Capability evolution 只能作为 source refs 和 review objects 出现：

- tool candidate references；
- procedure candidate references；
- verification evidence references；
- procedural memory candidate references；
- capability growth candidate review references。

Capability improvement 不等于 subject growth。Tool verification 不等于 authorization。Tool candidate
不进入 tool library。本 RFC 不允许 tool execution、automatic tool promotion、policy execution 或
self-modifying runtime。

## 风险

| 风险 | 为什么重要 | 护栏 |
|---|---|---|
| Source backing 变成 retrieval | 项目可能把文档引用误解成 continuity。 | 使用 `source_refs_preview`，不是 memory activation。 |
| 白名单漂移成宽文件访问 | 敏感文件或 imported memory 可能进入报告。 | 只允许显式文件名；不接受用户路径。 |
| Report fields 变成 prompt construction | 只读 refs 可能被误当作模型上下文包。 | 不调用模型，也不生成 prompt。 |
| Source refs 变成权威 | 被引用文档可能过期或仍是探索性。 | 输出 status 和 missing evidence。 |
| State-backed 被误解成 state-mutating | 这个词可能诱发写入。 | 所有 mutation flags 继续 false/disabled。 |

## P113-P120 候选顺序

P112 只授权 planning。候选后续 phases：

1. P113 Harness Source Inventory。
2. P114 Read-Only Source Loader Plan。
3. P115 Minimal `one_core/source_loader.py` for whitelisted Markdown。
4. P116 Source Loader Safety Hardening。
5. P117 `harness-source-inventory` CLI。
6. P118 Harness context preview source refs。
7. P119 Source-backed risk/open-question mapping。
8. P120 Source-backed usability review。

每个 phase 都必须保持 no-write、no external IO、no model call、no state mutation。

## 非授权声明

P112 不自动授权 P113-P120 implementation。每个 phase 都必须单独 commit 和检查。P112 也不授权 P121、
P155、本地 01 rebuild、连接旧 01、AstrBot、adapters、product work、Companion、正式 memory writes、
identity mutation、event writes、recall writes、temporal runtime、CTM runtime、tool execution、policy
execution 或 automatic roadmap execution。
