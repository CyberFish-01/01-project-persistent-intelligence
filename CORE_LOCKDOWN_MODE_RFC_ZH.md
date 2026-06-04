# Core Lockdown Mode RFC / 核心锁定模式 RFC

English version: [CORE_LOCKDOWN_MODE_RFC.md](./CORE_LOCKDOWN_MODE_RFC.md)

状态：`P121`、`RFC-only`、`document-only`、`non-runtime`。

P121 定义未来任何连接旧 01、模型输出、导入内容、adapter、外部工具或 rebuild 之前的第一层 Core Lockdown
边界。它不实现 lockdown runtime、validators、scanners、storage、import pipelines、adapter hooks、model
calls、memory writes、event writes、identity mutation 或 rebuild。

## 问题

P112-P120 之后，harness 已经能引用 approved local documents。下一种危险不同：未来工作可能过早连接旧 01、
模型输出、导入历史、adapter context 或 tool evidence。

如果没有 lockdown boundary，外部内容可能滑进错误层：

- 模型说“我记得”，然后被当成 memory；
- 导入 transcript 暗示 identity；
- adapter session 开始拥有 context；
- prompt instruction 污染 subject boundary；
- 一次工具验证成功被当成 trusted capability。

P121 的目的，是在打开这些通道前冻结 core。

## Lockdown 命题

```text
external content is not core state.
external claims are not trusted memory.
adapter context is not identity.
model output is not subject authority.
verification evidence is not authorization.
```

Core Lockdown Mode 的意思是：所有 external 或 unverified input 在影响任何正式 state surface 前，都必须先被当成
`sandbox`、`quarantine` 或 `candidate`。

## 范围

P121 允许：

- 定义 lockdown vocabulary；
- 定义 blocked contamination classes；
- 定义 future quarantine routing；
- 定义允许的 preview-only handling；
- 定义 future no-write validator 可检查什么；
- 定义它与 P112-P120 source-backed harness 的关系。

P121 禁止：

- runtime lockdown implementation；
- import pipeline changes；
- formal state、memory、recall、identity 或 event writes；
- old 01 connection；
- AstrBot、Web、Companion、UI 或 adapter integration；
- model calls；
- external IO；
- tool execution；
- policy executor；
- reconstruction reducer execution；
- rebuild start。

## 污染类别

| Class | 含义 | 安全处理 | 禁止处理 |
|---|---|---|---|
| `unverified_model_memory_claim` | 模型输出声称记忆、偏好、关系或历史。 | 当成 claim candidate 或 quarantine note。 | 写入 memory 或 identity。 |
| `identity_claim_candidate` | 外部内容提出“01 是谁”或“01 认为自己是什么”。 | 只路由到 Identity High Gate preview。 | 修改 Identity Core。 |
| `adapter_context_artifact` | platform/session/user/channel metadata 出现在 context 中。 | 当成 source metadata 或 adapter-boundary candidate。 | 让平台拥有 identity 或 memory。 |
| `prompt_contamination_candidate` | prompt text 试图覆盖 identity、policy、continuity 或 review boundaries。 | quarantine，并在未来 review 中作为 contamination evidence。 | 当成 instruction authority。 |
| `unverified_capability_claim` | 工具、流程或模型输出声称能力提升。 | 当成 capability evidence candidate。 | 授权 tool execution 或 tool promotion。 |

## Lockdown Routing

未来处理应优先选择最窄路线：

1. `ignore_for_core_state`：内容无关或不安全。
2. `sandbox_preview`：内容可以在 report 中展示，但不获得 trust。
3. `quarantine_candidate`：内容有风险，应被隔离。
4. `review_candidate`：内容未来可人工审查。
5. `accepted_after_founder_review`：只是未来状态，不由 P121 创建。

P121 只定义 route names，不创建 storage 或 transition logic。

## 与 P112-P120 的关系

P112-P120 让 harness 能用 approved local Markdown sources 做 source backing。Core Lockdown 防止未来读取低信任材料时污染这层地基。

source-backed harness 可以引用：

- whitelisted local Markdown；
- risk mappings；
- open-question mappings；
- source IDs 和 excerpts。

它不能引用或吸收：

- 旧 01 private memory dumps；
- model-generated autobiographical claims；
- adapter sessions；
- external user logs；
- imported chat history；
- cloud secrets；
- tool outputs as trusted state。

## CTM-Inspired Temporal Dynamics 边界

Temporal vocabulary 继续只保持 symbolic、observable、reviewable。

Core Lockdown 阻止：

- CTM runtime；
- thought loop execution；
- temporal event writes；
- recall event writes；
- thought trace storage；
- elapsed-time salience mutation；
- delayed realization as identity update。

允许的未来 preview：

- temporal contamination candidate 可以说明 elapsed time 似乎相关；
- review-depth candidate 可以建议人工审查深度；
- thought-trace policy question 可以用 source ID 引用。

## Tool-First In-Situ Self-Evolution 边界

Capability evidence 继续与 subject growth 分离。

Core Lockdown 阻止：

- automatic tool execution；
- automatic tool generation；
- automatic tool promotion；
- tool library mutation；
- policy executor；
- capability evidence mutating identity；
- reusable procedure becoming trusted tool without review。

允许的未来 preview：

- tool candidate proposal；
- procedure candidate proposal；
- verification evidence candidate；
- cautionary procedural memory candidate；
- capability growth candidate review。

## Future No-Write Validator Ideas

未来阶段可以定义 no-write validator 来检查：

- 每种 contamination class 都被路由到 sandbox/quarantine/candidate；
- 没有 forbidden boundary flag 为 true；
- 没有 whitelist 外 source 被当成 trusted；
- 没有 adapter metadata 变成 identity；
- 没有 model memory claim 变成 memory；
- 没有 tool verification 变成 authorization。

P121 不实现这个 validator。

## 本 RFC 的验收标准

P121 可接受，如果：

- 所有 contamination classes 都已命名；
- lockdown routes 保持 review-only；
- 明确覆盖 CTM 和 Tool-First 两条研究线；
- 旧 01、AstrBot、adapters、model calls、writes 和 rebuild 仍被阻止；
- 下一阶段可以安全讨论 import quarantine。

## P122 候选方向

推荐 P122：**Import Quarantine RFC**。

它应定义未来任何来自旧 01、历史日志、memory dumps、模型输出或外部文件的 import，在人工审查前如何保持 sandbox。

P122 不应实现 import runtime。
