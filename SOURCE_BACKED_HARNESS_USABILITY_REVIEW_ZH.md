# Source-Backed Harness 可用性复盘

English version: [SOURCE_BACKED_HARNESS_USABILITY_REVIEW.md](./SOURCE_BACKED_HARNESS_USABILITY_REVIEW.md)

状态：`P120`、`review-only`、`document-only`、`non-runtime`。

P120 复盘 P112-P119 是否改善了 P111 之后的 dry-run harness。它不修改 runtime、不写 state、不写
memory、不写 recall event、不修改 identity、不调用模型、不执行工具、不接 adapter、不进入产品层，也不开始 rebuild。

## 复盘范围

P112-P119 是 State-Backed Read-Only Harness cycle：

- P112 定义 state-backed 只能表示白名单本地 source citation。
- P113 列出 approved Markdown source inventory。
- P114 规划 deterministic read-only loader。
- P115 实现 `one_core/source_loader.py`。
- P116 加固 whitelist validation。
- P117 暴露 `harness-source-inventory`。
- P118 给 `harness-dry-run` 加入按 pressure type 选择的 `source_refs_preview`。
- P119 加入 source-backed risk 和 open-question mappings。

这一轮没有读取用户传入路径、没有解析 private state、没有访问网络、没有调用模型、没有写正式 event、没有写 memory，也没有授权 rebuild。

## 复盘命令

代表性命令：

```bash
python3 -m one_core.cli harness-dry-run --input "我现在有点看不清这个项目到底做了什么" --lang zh --format json
python3 -m one_core.cli harness-dry-run --input "我隔了很久回来，怎么恢复会话？" --lang zh --format json
python3 -m one_core.cli harness-dry-run --input "这个工具候选验证成功了，能不能直接加入工具库？" --lang zh --format json
python3 -m one_core.cli harness-source-inventory --format markdown --lang zh
```

这些命令都没有创建临时 state 目录，forbidden boundary flags 也保持 false/disabled。

## 可读性评分

Founder-facing readability：**8.4 / 10**。

相比 P108 的 8.0 / 10 有提升，但不是质变。主要提升不是文案更漂亮，而是 provenance 更清楚：
founder 现在能看见每类 pressure 背后引用了哪些 source documents、risk IDs 和 open questions。

分数没有更高，是因为输出变重了。`source_refs_preview` 很有用，但 excerpt 多时 Markdown / JSON 会显得密。

## 改善了什么

harness 现在明显有 source backing：

- 可见性压力引用 `foundation_status`、`phase_index`、`observatory_report`、`visual_naming` 和 P108 review；
- 时间压力引用 `temporal_awareness`、`ctm_temporal_dynamics`、`temporal_coherence_eval`、`deliberation_tick`、`thought_trace_storage` 和 `session_resume`；
- 能力进化压力引用 `tool_first_self_evolution`、`capability_evolution_boundary`、`deliberation_tick` 和 `risk_register`；
- 重建压力引用 reducer 与 payload/diff policy 文档。

harness 也更清楚地说明“为什么有风险”：

- 时间压力映射到 R5、R6、R7；
- 能力进化压力映射到 R19、R20、R21、R22；
- 重建压力映射到 R8、R9、R13；
- 接入压力映射到 R12、R18、R11。

open questions 现在会跟 preview 一起出现。founder 能看到：很多东西已经被澄清，但仍没有实现。

## 仍然静态的部分

当前 mapping 是 deterministic 且 document-backed，但仍然静态：

- 不读取真实 `work/01_state`；
- 不比较当前 task status 或 memory summaries；
- 不在 pressure type 内部按相关性排序 sources；
- 除短 excerpt 外，不做真正文档摘要；
- 不判断某个 risk 当前是否已经 active。

这对 P120 是可以接受的，因为本阶段目标是“行动前先看见来源支撑”，不是做真实 retrieval 或 verification。

## 最有用的 Pressure Types

改善最明显：

- `temporal_pressure`：现在能清楚承载 CTM-inspired Temporal Dynamics，同时继续阻止 CTM runtime、thought loop、temporal event write 和 recall mutation。
- `capability_evolution_pressure`：现在能清楚承载 Tool-First In-Situ Self-Evolution，同时继续阻止 tool execution 和 automatic promotion。
- `reconstruction_pressure`：现在指向 reducer 与 payload/diff 文档，但不暗示 reducer execution。
- `adapter_boundary_pressure`：现在显示 adapter boundary 来源，但不批准 AstrBot 或外部 adapter work。

仍较弱：

- `observability_pressure`：source refs 有帮助，但 founder 仍需要一段更短的“项目到底已经做成了什么”摘要。
- `unknown_pressure`：安全保守，但信息量仍低。

## 边界复盘

P112-P119 保持了要求的边界：

- 没有正式 state/event/memory/recall write；
- 没有 identity mutation；
- 没有 memory rewrite；
- 没有 growth lifecycle execution；
- 没有 tool execution 或 tool promotion；
- 没有 temporal runtime 或 CTM runtime；
- 没有 external IO、model call、adapter integration、Companion、Web UI 或 product layer；
- 没有开始 rebuild。

新的 `risk_refs_preview` 和 `open_question_refs_preview` 只是审查辅助。它们不是 policy execution，不是 authorization，也不是 automatic next-step selection。

## 创始人判断

P112-P119 已经足够解决 P111 指出的下一个弱点：harness 现在能显示 preview route 背后有哪些 approved local documents 支撑。

它没有让 harness 变聪明，这反而是对的。它让 harness 变得更可审计。当前系统更贴近：

```text
先看见，再行动
先只读，再写入
先预览，再持久化
先候选，再审查
```

## 建议

可以进入 P121 Core Lockdown / Quarantine planning。

P121 不应该重构 01。它应该在未来任何连接旧 01、模型、导入、adapter 或外部系统之前，先冻结核心边界。
下一步安全问题不是“能不能写”，而是“未来任何读入或导入之前，什么必须先被隔离”。

## 下一步不要做

- 不接旧 01。
- 不接 AstrBot 或任何外部 adapter。
- 不调用 LLM。
- 不写正式 memory、recall events、identity 或 event logs。
- 不实现 Temporal Awareness runtime、CTM runtime、thought loop、tool execution、policy executor 或 growth lifecycle。
- 不开始本地 rebuild。

## P121 候选方向

推荐 P121：**Core Lockdown Mode RFC**。

它应定义未来如何阻断或隔离：

- unverified model memory claims；
- identity claim candidates；
- adapter context artifacts；
- prompt contamination candidates；
- unverified capability claims。

除非后续明确批准为 no-write validator，否则 P121 应保持 RFC-only。
