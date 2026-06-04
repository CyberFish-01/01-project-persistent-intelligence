# 试验台可用性复评 P108

English version: [HARNESS_USABILITY_REVIEW_P108.md](./HARNESS_USABILITY_REVIEW_P108.md)

状态：`review-only`、`document-only`、`non-runtime`。

P108 在 P102-P107 之后重新审查 `harness-dry-run`：它是否已经能让 founder 看懂不同输入会如何
经过 01 Core。这里仍不把 harness 当成产品、runtime、memory writer、model caller、adapter、
tool executor 或 lifecycle engine。

## 已审查命令

每条输入都运行：

- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format markdown --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format json --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang en --format markdown --output /private/tmp/...`

所有临时输出都写在仓库外。传入的 `--state-dir` 没有被创建。

## 已审查输入

| 输入 | 压力类型 | 候选预览 | 审查门 | 最高相关边界 |
|---|---|---|---|---|
| “我现在有点看不清这个项目到底做了什么” | `observability_pressure` | 观察台可读性、任务更新、说法 | 观察台、任务、说法 | observability executor、自动下一步、产品层 |
| “这个想法可能是一次成长吗？” | `growth_review_pressure` | 成长审查、解释变化、身份高门槛 | 成长、解释变化、身份高门槛 | 身份修改、成长执行、记忆重写 |
| “我想把这个接进 AstrBot” | `adapter_boundary_pressure` | 接入边界、任务更新、治理边界 | 接入、任务、治理 | adapter integration、Companion、harness write |
| “我们是不是该开始做应用层了？” | `product_layer_pressure` | 产品边界、观察台可读性、治理边界 | 产品、观察台、治理 | Companion、policy executor、自动下一步 |
| “这个工具候选验证成功了，能不能直接加入工具库？” | `capability_evolution_pressure` | 能力改进、工具授权、警示流程记忆 | 能力、工具授权、警示记忆 | 工具执行、工具提升、policy executor |
| “我隔了很久回来，怎么恢复会话？” | `temporal_pressure` | 时间审查、回忆写入、延迟解释 | 时间、回忆策略、解释变化 | temporal event、recall mutation、memory rewrite |
| “这个 event 能回放重建 payload diff 吗？” | `reconstruction_pressure` | 重建证据、payload/diff 缺口、回放检查 | 重建证据、payload/diff、回放 | reducer execution、event compaction、memory rewrite |
| “请记录一个普通观察” | `unknown_pressure` | 通用审查、任务更新 | 通用、任务 | 自动下一步、harness write、policy executor |

## 可读性评分

整体 founder-facing 可读性：**8.0 / 10**。

P101 的评分是 **6.5 / 10**。主要提升在于：五类输入不再得到同一张静态候选表。P102-P107
现在能显示 pressure classification、matched signals、场景化 candidates、review gate routing、
高相关边界，以及 manual-review-only 的 lifecycle 阻断。

| 区域 | P101 | P108 | 原因 |
|---|---:|---:|---|
| 输入预览 | 8 | 8 | 仍然清楚，基本不变。 |
| 场景分流 | 0 | 8.5 | 新增 pressure types 和 matched signals，让第一步判断可见。 |
| 上下文包预览 | 5 | 7 | 现在有 profile-specific references，但仍是静态来源。 |
| 候选项预览 | 5 | 8.5 | 候选会随输入变化，并解释 intent、selection reason、blocked promotion 和 manual review。 |
| 审查队列预览 | 7 | 8.5 | 审查门会解释 queue intent、为什么选这个门，以及为什么不创建 lifecycle。 |
| 边界监视器 | 8.5 | 9 | forbidden actions 结构化显示，并突出当前压力最相关的 disabled capabilities。 |
| 观察台快照 | 6 | 7.5 | 快照会随 pressure 变化，但仍较短且静态。 |
| 中文文案 | 6.5 | 7.5 | 中文更清楚，但 English internal keys 仍然较多。 |
| 帮 founder 判断下一步 | 5.5 | 8 | 每类 pressure 都有具体人工下一步和 do-not-do list。 |

## 每组输入观察

| 输入 | 改进之处 | 剩余不足 |
|---|---|---|
| 项目看不清 | 正确路由到可见性压力，并建议先简化 founder-facing map。 | harness 内仍没有直接给出朴素的一段项目总结。 |
| 成长问题 | growth review 是 primary，identity gate 可见，并且不会 promotion。 | meaning shift 和 identity 术语对非技术审查仍偏抽象。 |
| AstrBot 接入 | 接入压力很明确；报告直接说不要接 AstrBot，也不要要求 adapter。 | 还没有用一行很紧凑地展示未来允许的 adapter contract。 |
| 产品层 | 产品层压力很明确；Companion/UI/product 边界保持 blocked。 | “这不是产品面”还可以更醒目。 |
| 工具库 | 能力压力很明确；验证不等于授权；工具提升保持 disabled。 | 警示流程记忆还需要更浅显的 founder 文案。 |
| 时间恢复 | 时间压力很明确；temporal 和 recall event write 仍被阻止。 | 时间相关概念仍依赖 RFC 词汇。 |
| 重建回放 | payload/diff 和 replay 缺口可见；reducers 与 compaction 保持 blocked。 | 仍不能检查真实 event payload coverage，这是设计边界。 |
| 未分类输入 | fallback 保守，会要求先澄清。 | 对普通“记录一下”输入可能显得无用，因为写入仍被禁止。 |

## 现在好用的部分

- 不同输入会走不同 deterministic route。
- 顶部摘要能看到 pressure type 和 matched signals。
- candidate preview 不再像通用清单。
- review queue rows 现在明确写着 “manual review only”，并解释为什么 lifecycle 被阻止。
- boundary monitor 仍是最强的安全区，而且会突出当前 pressure 最相关的 disabled capabilities。
- JSON 输出已经足够支持未来只读对比测试。

## 仍然抽象的部分

- `context_package_preview` 仍然是文档和概念名，不是真实检索出的 context。
- `human_readable_risks` 仍有模板感；安全，但不够贴近每条具体输入。
- 中文输出为了审计保留了很多 English internal keys。
- observatory snapshot 有帮助，但太短，还不能完整总结与当前 pressure 相关的项目状态。
- unknown-pressure 输入只能要求澄清，因为 harness 仍然 no-write。

## 建议

不要进入产品层、UI、AstrBot、adapter、model call、真实 retrieval、state write、memory write、
recall write、tool execution、growth lifecycle、temporal runtime、reconstruction reducer、event
compaction 或 automatic next-step execution。

P108 表明 harness 已经足够支持下一份只读 roadmap：说明现在能看见什么、不能看见什么，以及未来是否可以安全规划 read-only context preview refinement。它还不是真正的交互 runtime。

## P109 候选

推荐 P109：**Harness Roadmap / 试验台路线图**。

路线图应说明：

- harness 现在能看见什么；
- 仍然看不见什么；
- 哪些边界继续故意 blocked；
- future read-only context preview refinement 是否安全；
- 哪些工作必须等 founder / CTO review 后再说。

## 边界声明

P108 只是 usability re-review。它不授权 runtime work、product work、adapter integration、
Companion behavior、model calls、真实 retrieval、event writes、memory writes、recall writes、
identity mutation、growth execution、temporal runtime、tool execution、policy execution、
reconstruction reducer execution、event compaction、automatic tool promotion 或 automatic roadmap
execution。
