# 术语表

English version: [GLOSSARY.md](./GLOSSARY.md)

P74 让 glossary 聚焦基础层概念和术语边界。这些定义不创建 runtime behavior。

## Deduplication Rule / 去重规则

当两个术语重叠时，优先使用更窄的 owner：

- Memory Layer 用于 stored memory objects 和 retrieval；
- Stateful Memory 用于 meaning-bearing memory semantics；
- Claim Graph 用于 claim status 和 evidence relations；
- Governance Surface 用于跨层 review objects；
- Event Log 和 Reconstruction Evidence 用于 auditability 与 replay readiness；
- RFC terms 表示 future contracts，不表示已经实现的机制。

## Growth / 成长

经过 evidence 支持、review 通过、并带有意义变化的 state transition，可能影响未来 continuity。

边界：Growth 不是自动行为，也不等于 memory promotion、identity mutation、tone drift 或 lifecycle label。

## Growth Candidate / 成长候选

由 growth semantics 标记出来、等待 review 的可能 meaning-bearing state transition。

边界：Growth candidate 不是 growth；它不能自动 promote 自己，也不 rewrite memory 或 identity。

## Growth Candidate Review / 成长候选审查

用于检查 growth candidate 的 review-only governance object。P51 中它由
`growth_candidate_review_v0.1` 表示，引用 source events、related memories、related claims、related tasks、encoding state、recall state、meaning shift、evidence、rejection reasons、risk level 和 review gate。

边界：这个 object 属于 Governance Surface，不单独属于 Memory Layer、Claim Graph、Task Hub 或 Identity Core。

## Growth Candidate Lifecycle / 成长候选生命周期

未来 review-object housekeeping vocabulary，用来描述 open、deferred、archived、quarantined 或 rejected 等状态。

边界：Lifecycle status 不是 subject growth、不是 memory promotion，也不是 execution engine。

## Drift / 漂移

interpretation、behavior、salience、belief 或 identity pressure 随时间发生的变化。Drift 可以是 productive、random、exploratory、conflict-driven 或 identity-threatening。

边界：Drift 是 signal category；它本身不自动等于好、坏或 growth。

## Productive Drift / 生产性漂移

有 evidence、有边界、有 review value，并且可能帮助 continuity improvement 或 meaning clarification 的 drift。

边界：Productive drift 可以成为 growth candidate review object，但它本身仍不是 growth。

## Random Drift / 随机漂移

缺少足够 evidence、event context 或 state context 的 unsupported change。

边界：Random drift 应被 reject、标记为 insufficient context，或路由到 review；它不应该被 normalise 成 growth。

## Identity-Threatening Drift / 身份威胁漂移

对 Identity Core continuity 施加压力或尝试 identity overwrite 的 drift signal。

边界：它需要 high-gate review，并且不能自动 mutate Identity Core。

## Collapse / 坍塌

continuity、coherence 或 reviewability 的丧失；state transfer 已不足以解释当前状态是如何从主体历史中抵达的。

边界：Collapse 不是更强的 growth；它是 failure mode 或 high-risk condition。

## Meaning Shift / 意义变化

encoded memory 和 recalled memory state 之间的 interpretive change。P51 要求
`reinforced`、`weakened`、`reinterpreted` 和 `conflicted` shift 必须有 evidence。

边界：Meaning shift 不等于 claim revision。Claim revision 改变 claim status；meaning shift 解释 memory 在 recall 时意义如何变化。

## Recall State / 回忆状态

memory 被 recall 时的状态：task context、claim context、retrieval reason、active identity anchors，以及未来可能加入的 temporal fields。Recall state 会改变 memory 的意义。

边界：Recall state 不是 recall event write。它可以在 review 中被引用，而不新增 event。

## Encoding State / 编码状态

memory 最初被记录时的状态：source event、timestamp、active task、active claims、identity anchors、confidence、salience、privacy scope 和 state version。

边界：Encoding state 是后续 interpretation 所需的最小 context reference，不是主体的完整 snapshot。

## Recall Event Write Policy / 回忆事件写入策略

未来 policy surface，用来决定一次 recall 什么时候应该成为 auditable event。

边界：RFC 只定义问题和约束；它不授权 recall event writes。

## Stateful Memory / 有状态记忆

把 memory 解释为以下结构的 memory semantics：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

边界：Stateful Memory 不替代 Memory Layer。Memory Layer 负责存储和 retrieval；Stateful Memory 解释 remembered meaning 如何随 state transition 变化。

## Review-Only / 只审查

不执行的 artifact 或 decision mode。Review-only object 可以记录、总结、排序、路由或请求 evidence。

边界：Review-only object 不 mutate identity、不 rewrite memory、不 execute policy、不 compact events、不 run reducers、不 promote growth。

## Governance Surface / 治理表层

一个跨层 review surface，可以引用 Memory Layer、Claim Graph、Task Hub、Identity Gate 和 event evidence，但不直接属于任何单层。P51 推荐把 `growth_candidate_review` 放在这里。

边界：Governance Surface 拥有 review objects；它不是 policy executor、Task Hub 替代品或 growth engine。

## Temporal Awareness / 时间感知

未来方向，把 elapsed time 视为 subject state transition 的一部分，而不只是 metadata。

边界：P58 只是 document-only。Temporal Awareness 不是 runtime behavior、temporal event execution、task staleness automation 或 memory decay。

## Subject Kernel / 主体内核

主体受保护的 continuity nucleus：identity anchors、core invariants，以及不能被随意 overwrite 的最小 interpretive frame。

边界：Subject Kernel 是未来边界概念，不是当前 runtime split 或 identity rewrite。

## World Seed / 世界种子

主体面向世界的可演化起始框架：assumptions、environment、interests、orientation 和 exploratory context。

边界：World Seed 可以在 review 下演化，但不能把变化偷渡进受保护的 Subject Kernel。

## Reconstruction Evidence / 重建证据

用于判断主体历史是否 auditable、replayable、并为未来 reconstruction 做好准备的 evidence vocabulary 和 report layer。

边界：Reconstruction evidence 不是 reconstruction execution 或 state rebuild。

## Reconstruction Reducer Contract / 重建 reducer 合同

未来任何可能从 events rebuild 或 project state 的 reducer 所需遵守的 contract。

边界：该 contract 在 implementation 前命名必要 guarantees 和 gaps；它不运行 reducer。

## Payload / Diff Capture Policy / Payload 与 Diff 捕获策略

未来 capture policy，用来决定 events 什么时候需要 payloads、diffs、snapshots 或 reference-only records。

边界：该 policy 描述未来需求和风险；它不 capture 新 payloads，也不 mutate event schemas。

## Risk Register / 风险登记表

foundation risks 的文档级 watchlist，例如 concept inflation、premature runtime pressure、boundary drift 和 bilingual drift。

边界：Risk register 记录风险；它不是 governance execution。

## CTM-inspired Temporal Dynamics / CTM 启发的时间动力学

一种 RFC-only vocabulary，把 Continuous Thought Machines 的启发翻译成 01 Core 的 symbolic
temporal review concepts。

边界：01 Core 不是 CTM implementation。该 term 不批准 CTM runtime、model training、
temporal event writes 或 neural synchronization claims。

## Deliberation Tick / 审议 tick

未来可能用于表示 conclusion 前 internal review progression 的单位。

边界：deliberation tick 当前不被 persist，不是 event，也不是 runtime step，除非未来 policy 明确定义。
P83 把它视为 review-planning vocabulary，不是 thought loop。

## Review Depth / 审查深度

一种 risk-calibrated review requirement，例如 `shallow`、`normal`、`deep` 或 `blocked`。

边界：review depth 不批准 execution、不 mutate state，也不运行 policy。

## Risk Level / 风险等级

candidate 在 review 前制造多少 boundary pressure 的分类。

边界：risk level 不是 automatic decision，也不能替代 high-risk cases 的 human 或 gate review。

## Thought Trace / 思考轨迹

未来可能用于记录 review state 如何随 deliberation 演化。

边界：P84 把任何未来 thought trace 都视为 auditable review artifact，而不是 hidden
chain-of-thought、private model reasoning、model internals 或 consciousness proof。它不能创建
event payloads、memory rewrites、identity changes、recall writes 或 growth promotion。

## Trace Candidate / 轨迹候选

未来可能用于摘要 review evidence、boundary flags、review depth、unresolved questions 和
storage decision 的 review artifact。

边界：trace candidate 不是 trace storage、不是 thought loop、不是 deliberation tick execution
log，也不是 hidden chain-of-thought。

## Thin Interaction Harness / 薄交互试验台

未来可能用于 preview conversation intake、context package selection、candidate review、review
queue ordering、resume scenarios 和 boundary flags 的本地 testing surface。

边界：thin harness 不是 product、UI、adapter、companion layer、runtime executor、context
mutation path 或 identity owner。

## Boundary Monitor Preview / 边界监视预览

未来可能用于解释 candidate 或 action 为什么被 blocked、deferred 或 needs review 的 harness
surface。

边界：boundary monitor preview 不是 runtime enforcement、policy execution 或 product safety
automation。

## Conversation Intake / 对话输入

未来可能存在的 harness preview step，用于把 user、system、process 或 fixture input 规范化成
audit-safe envelope。

边界：conversation intake 不是 adapter ingest、不是 event write、不是 context building，也不是
actor、session、source 或 platform 对 identity 的 ownership。

## Intake Envelope / 输入信封

未来 preview shape，用于表示 actor、session、source、timestamp、content reference、privacy、
sensitivity、context request、boundary flags 和 storage stance。

边界：intake envelope 不是 implemented schema、不是 full payload capture mechanism，也不是
memory record。

## Context Package Preview / 上下文包预览

未来可能存在的 harness surface，用于解释 selected context references、omitted references、
attribution、token budget、privacy suppression、risk flags 和 context gaps。

边界：context package preview 不是 retrieval as continuity、不是 context mutation、不是 prompt
construction，也不是 activation trace persistence。

## Omitted Reference / 被省略引用

未来 context preview 故意省略的 reference，并附带 privacy、archived status、weak evidence、token
budget 或 forbidden boundary 等原因。

边界：omitted 不表示 deleted、forgotten、永久无关或 rewritten。

## Review Queue Preview / 审查队列预览

未来可能存在的 harness surface，用 candidate type、risk、evidence、review depth、blocked
boundary 和 suggested owner route 来组织 candidate previews。

边界：review queue preview 不是 queue runtime、不是 lifecycle execution、不是 approval、不是
policy execution，也不是 mutation。

## Candidate Preview / 候选预览

未来用于表示 memory、claim、growth、meaning-shift、recall、task、governance、identity、temporal
或 trace review object 的 preview record。

边界：candidate preview 不是 durable candidate、不是 approval，也不是 state transition。

## Session Resume Scenario / 会话恢复场景

未来 deterministic scenario，用于模拟 interrupted 或 paused session 如何恢复 task、claim、memory、
candidate 和 context references。

边界：session resume scenario 不是 session runtime、不是 temporal event、不是 memory decay，也不是
resume automation。

## Context Gap / 上下文缺口

resume 或 context preview 中被披露的 evidence 或 state references 缺失。

边界：context gap 不得通过 fabricated memory、memory rewrite、claim revision 或 identity update 来修复。

## Core Interaction Harness Roadmap / Core 交互试验台路线图

用于判断未来 minimal local CLI harness 是否、以及如何在 fixture、output、boundary、privacy 和 no-write
contracts 之后被考虑的 roadmap。

边界：roadmap 不是 implementation approval，也不创建 CLI commands、schemas、tests、runtime
behavior、adapter integration 或 UI。

## Minimal CLI Harness Implementation Plan / 最小 CLI 试验台实现计划

P99 document-only plan，用于规划 P100 `harness-dry-run` command。它定义 dry-run scope、
input fields、output sections、candidate preview types、boundary rules 和 initial tests plan。

边界：该 plan 不批准 model calls、external API calls、state writes、adapter integration、product
behavior 或 P103。

## Harness Dry-Run / 试验台 Dry-Run

P100 本地 CLI pressure test，并在 P102 增加 deterministic input classification，用于 preview 一条
user message 如何经过 intake、scenario routing、context preview、candidate preview、review queue
preview、boundary monitor 和 observatory snapshot。

边界：dry-run means no writes、no model call、no external API call、no adapter ownership、no
identity mutation、no memory rewrite、no recall event write、no growth execution、no tool execution。

## Input Pressure Type / 输入压力类型

`harness-dry-run` 为解释 user input 可能造成哪类压力而赋予的 deterministic label。P102 支持
observability、growth review、adapter boundary、product layer、capability evolution、temporal、
reconstruction 和 unknown pressure。

边界：input pressure type 是 static dry-run classification。它不是 intent understanding、model
inference、retrieval、event writing、authorization 或 automatic routing。

## Scenario Profile / 场景档案

由 input pressure type 选择的 dry-run profile。它会改变 context preview、candidate preview、review
gates、highlighted boundaries、profile-specific risks 和 recommended next step。

边界：scenario profile 不是 runtime plan、policy executor、adapter flow、tool execution path 或
product workflow。

## Harness Scenario Routing / 试验台场景分流

P102 rule-based dry-run mechanism，在渲染报告前把 matched keywords 映射到 scenario profile。

边界：scenario routing 是 deterministic 和 local 的。它不调用 LLM、不执行真实 retrieval、不读写
state、不接 AstrBot、不执行 tools，也不创建 review lifecycles。

## Founder Summary / 创始人摘要

P103 在 harness dry-run report 前部加入的说明区。它解释分类是什么、为什么命中、preview 现在能做什么、
不能做什么、最安全的人工下一步，以及暂时不要建设什么。

边界：founder summary 是 explanation，不是 authorization、execution、memory write、identity
update、product decision 或 next-step automation。

## Hardened Boundary Monitor / 强化边界监视器

P105 在 `harness-dry-run` 内加入的结构化边界报告。它列出 disabled capabilities、unchanged state、
active boundary violations，以及与当前 pressure profile 最相关的 boundaries。

边界：boundary monitor 是 audit output。它不执行 policy、不执行 action、不修改 state，也不授权 runtime。

## Specialized Candidate Preview / 专门化候选预览

P106 为 `harness-dry-run` 加入的 candidate-row 格式。每个 candidate 会说明 intent、为什么被选中、
为什么不能 promotion，以及未来需要哪个 manual review gate。

边界：specialized candidate preview 仍是 preview-only。它不是 persistence、promotion、lifecycle
creation、tool authorization 或 execution。

## Specialized Review Queue Preview / 专门化审查队列预览

P107 为 `harness-dry-run` 加入的 review-gate 格式。每个 gate 会说明 queue intent、candidate
为什么路由到这里、为什么 lifecycle 被阻止，以及下一步只允许 manual review。

边界：specialized review queue preview 不是真实 queue、lifecycle、authorization、policy executor
或 execution surface。

## Fixture-First Harness / Fixture 优先试验台

一种可能的 future harness approach：在任何 live input、adapter、cloud 或 product surface 前，先使用
local deterministic fixture inputs。

边界：fixture-first 仍不批准 state writes、mutation、model prompting 或 runtime integration。

## Observatory Snapshot / 观察台快照

未来可能附在 harness dry-run report 末尾的 compact summary，让 founder 能把 interaction pressure
和 Foundation Observatory status vocabulary 对齐。

边界：observatory snapshot 不是 decision、authorization、status API、dashboard runtime 或 automatic
next-step executor。

## Non-Execution Invariants / 非执行不变量

报告中显式声明 dry-run 没有执行 forbidden actions 的 flags，例如 state mutation、identity mutation、
memory rewrite、recall writes、growth execution、model calls、external API calls、adapter integration
或 tool execution。

边界：invariants 是 audit/report assertions。除非 future tests 验证，否则它们不是 runtime
capability proof。

## No-Write Harness / 不写入试验台

未来 harness stance：如果 command 不能证明没有 state files、memory files、event files、recall
files 或 identity files 被改变，就必须 fail closed。

边界：no-write 本身不代表 low-risk；它仍需要 privacy、output path、invalid input 和
forbidden-output tests。

## Temporal Coherence / 时间一致性

用于 review later state 是否仍能与 earlier state、current evidence 和 continuity anchors 相容的概念。

边界：temporal coherence 不是真理、growth、consciousness，也不是 automatic claim revision。

## Review Depth Budget / 审查深度预算

未来可能用于让 review effort 匹配 risk level 的 policy concept。

边界：review depth budget 不是 adaptive compute runtime、不是 policy execution，也不是 automatic approval。

## Unresolved Tension / 未解决张力

未来可能用于表示 persistent conflict 的 review signal；该 conflict 尚未成为 decision、claim revision 或 growth candidate。

边界：unresolved tension 不能自动创建 growth candidates、rewrite claims 或 mutate identity。

## Delayed Alignment / 延迟对齐

未来可能表示 later evidence 让 earlier state 或 memory 符合 stable pattern 的 review signal。

边界：delayed alignment 可以提示 review evidence；它不是 semantic promotion、identity update 或 memory rewrite。

## Coherence Break / 一致性断裂

未来可能表示 current state 已不能安全地从 prior state 和 evidence 推导出来。

边界：coherence break 是 review concern，不是 automatic collapse classification 或 reconstruction。

## Temporal Coherence Evaluation / 时间一致性评估

一个 document-only plan，用 deterministic scenarios 和 future signals 来测试 CTM-inspired
temporal coherence vocabulary。

边界：它不是 runtime evaluator、不是 report implementation，也不是 truth engine。

## Temporal Coherence Score / 时间一致性分数

未来可能用于表示 later interpretation 与 prior state 和 evidence 的匹配程度。

边界：该 score 不是真理、consciousness、growth、identity validity 或 runtime authority。

## Evidence Alignment Score / 证据对齐分数

未来可能用于表示 event、claim、task、memory references 对 candidate 的支持强度。

边界：evidence alignment 不批准 candidate，也不 mutate 任何 referenced object。

## Review Depth Required / 所需审查深度

未来可能用于表示需要 shallow、normal 还是 deep review。

边界：它不是 adaptive compute runtime、不是 thought loop，也不是 policy execution。

## Capability Evolution / 能力演化

使用 objective task evidence，在 review 管控下改进 tools、skills 和 procedures。

边界：capability evolution 不是 subject evolution，也不修改 Identity Core。

## Subject Evolution / 主体演化

可能影响 continuity、identity interpretation 或 long-term subject history 的 meaning-bearing
subject-state transition。

边界：subject evolution 仍是 high-gated，不能只由 tool success 触发。

## Tool Candidate / 工具候选

可能帮助完成任务的 proposed tool、script、function、command pattern 或 external capability wrapper。

边界：tool candidate 不是 trusted code、不是 tool-library entry，也不是 execution approval。

## Procedure Candidate / 流程候选

包含 steps、checks、inputs、outputs、rollback notes 和 safety boundaries 的 proposed repeatable
workflow。

边界：procedure candidate 不是 active procedural memory，也不是 executable policy。

## Skill Memory / 技能记忆

未来可能用于保存经过 review 的 reusable capability knowledge 的 memory category。

边界：skill memory 不是 identity memory、不是 policy execution，也不是 automatic tool invocation。

## Capability Growth Candidate / 能力成长候选

一个 review object，用于提出 tool 或 procedure use 的 evidence 可能表示 durable capability
improvement。

边界：capability growth candidate 不是 subject growth、tool promotion、memory rewrite 或 identity
mutation。

## Capability Evidence / 能力证据

来自 task results、verification results、failures、reproducibility、safety checks、dependency checks
或 rollback notes 的 review material。

边界：capability evidence 支持 review；它不授权 action、不 promote tools，也不 mutate identity。

## Tool Authorization / 工具授权

未来可能存在的 explicit permission gate，用于在明确 scope、inputs、outputs、dependencies 和 rollback
conditions 下执行或 promote 工具。

边界：tool authorization 不能只从 verification 推导出来。

## Tool Verification / 工具验证

未来可能存在的 evidence process，用于检查 candidate 是否 worked、failed、reproduced、stayed within
boundaries，并保持 task-relevant。

边界：tool verification 不是 tool authorization。

## Tool Candidate Review / 工具候选审查

未来 review surface，用于检查 proposed tool 是否 safe、relevant、testable、reproducible、bounded
且 dependency-aware。

边界：tool candidate review 不执行 tool、不安装 dependencies，也不把 tool 加入 library。

## Tool-First Self-Evolution / 工具优先自进化

一个 RFC-only direction，把可验证的 tool、skill 和 procedure improvement 放在 subject 或 identity
evolution 之前。

边界：tool-first self-evolution 不批准 tool execution、automatic tool generation、automatic tool
promotion、policy execution 或 Identity Core mutation。

## Capability Evolution Boundary / 能力演化边界

P92 RFC boundary，用于区分允许的 capability proposal、evidence、review，以及禁止的 execution、
promotion、policy execution、identity mutation、memory rewrite、uncontrolled access、dependency
installation 和 self-modifying runtime。

边界：它是 document-only boundary，不是 enforcement code。

## Visual Naming Guide / 视觉命名指南

P93 document-only guide，用于把 English internal keys 映射为未来视觉基础层表面使用的中文
founder-facing display names。

边界：该 guide 不是 Web UI、dashboard runtime、observability CLI、product surface 或
Foundation Observatory implementation。

## Founder-Facing Vocabulary / 创始人可读词汇

面向项目创始人或 CTO 阅读 summaries、readiness views、risk views 或 future observatory surfaces
时使用的朴素标签和解释。

边界：founder-facing vocabulary 简化展示，但不能改变底层 RFC、audit、code 或 paper meaning。

## Display Name / 显示名

未来 visual card 或 summary surface 上优先展示的中文标签。

边界：display name 不是 implementation status、capability claim 或 promotion decision。

## Internal Key / 内部键

RFCs、papers、code identifiers、schemas、audits 和 cross-project comparison 使用的稳定英文术语。

边界：internal key 应保持精确，但不能迫使 founder-facing views 使用论文式标题。

## Foundation Observatory / 地基观察台

未来可能面向 founder 展示 foundation status、concept boundaries、readiness、risks 和 open
questions 的表面。P94 提供这个 observatory layer 的 Markdown report 版本，P96 提供 read-only
static CLI report generator，P98 改进 generated output 的 founder readability。

边界：P98 仍只是 static report generator。它不实现 dashboard runtime、Web UI、status API、
observability executor、live monitor 或 product surface。

## Foundation Observatory Report / 地基观察台报告

P94 founder-facing Markdown report，用 snapshot、main axes map、readiness matrix、boundary
status、risk heatmap 和 next-step recommendation 总结当前 foundation 状态。

边界：它是 report artifact，不是 dashboard、CLI、runtime monitor、status endpoint、product UI
或 implementation approval。

## Founder Snapshot / 创始人快照

用简短 founder-facing 语言说明当前 01 Core 是什么、不是什么，以及现在最重要的状态。

边界：snapshot 不是 release note、product claim 或 runtime status endpoint。

## Main Axes Map / 主轴地图

把 foundation 按 continuity、growth、temporal review、capability evolution、interaction planning
和 observability 等主轴组织起来的 founder-facing report grouping。

边界：axis map 是报告分组，不是 architecture module 或 runtime boundary。

## Minimal Observatory CLI Plan / 最小观察台 CLI 计划

P95 RFC-only plan，用于规划 P96 read-only command。该 command 从 approved documents 和 static
foundation status 生成 Foundation Observatory report。

边界：该 plan 不批准 dashboards、Web UI、product UI、status APIs、runtime monitors、policy
execution 或 executors。

## Minimal Observatory CLI / 最小观察台 CLI

P96 read-only CLI command，P98 改进其 founder-facing readability：

```bash
python3 -m one_core.cli foundation-observatory-report
```

它使用 static foundation artifacts、approved naming/status categories、plain readiness rows、
risk explanations 和 next-step candidates 输出 Markdown 或 JSON founder-facing observatory report。

边界：它只 read and render。它不修改 state、不执行 policy、不推进 roadmap work、不创建 phase，
也不是 dashboard runtime。

## Harness Dry-Run Command / 试验台 Dry-Run 命令

P100 命令：

```bash
python3 -m one_core.cli harness-dry-run
```

边界：该命令只实现为 read-only local preview。它不是聊天应用、model caller、adapter
integration、state writer、memory writer、recall writer、growth lifecycle、product surface 或
automatic next-step executor。

## Observatory CLI Report / 观察台 CLI 报告

由 minimal observatory command 输出的 read-only report。P98 后，它包含 one-screen founder summary、
founder snapshot、axes map、带 can/cannot guidance 的 readiness matrix、boundary status、带人话解释的
risk heatmap、带 benefit/risk 的 next-step recommendations 和 blocked-work list。

边界：report 不是 authorization、execution、mutation 或 phase creation。

## Readiness Category / 就绪度类别

保守状态标签，例如 `implemented`、`report_only`、`rfc_only`、`evaluation_only`、
`future_direction`、`blocked` 或 `dangerous_if_early`。

边界：readiness category 总结当前 evidence；它不是 implementation approval。

## Observability Executor / 观察层执行器

一种被禁止的未来风险：observability surface 开始执行 roadmaps、创建 phases、mutate status 或
enforce decisions。

边界：P98 仍明确阻止 observability execution。除非未来 founder-approved phase 另行定义，
observatory work 必须保持 read-only。

## Readiness Matrix / 就绪度矩阵

未来可能用于显示一个概念是 ready、blocked、RFC-only、future-only，还是缺少 required gates 的
report-style view。

边界：readiness 不是 authorization，也不批准 implementation。

## Risk Heatmap / 风险热力图

未来可能用于把 concept、identity、memory、runtime、tools、governance 和 product boundaries 上的风险压力可视化分组。

边界：heatmap 不是 governance execution、policy enforcement 或 risk resolution。

## Boundary Status / 边界状态

用于说明一个概念是 allowed、blocked、RFC-only、report-only、future-only 还是 dangerously early
的可见标签。

边界：boundary status 不是 runtime enforcement，也不能替代 review。

## Lineage Governance / 谱系治理

P155 governance layer，用于在任何 future local rebuild 前，让 Core history、instance branches、
research branches、quarantine branches、baseline references、tags 和 checkpoints 可追溯。

边界：lineage governance 只是 planning 和 review vocabulary。它不创建 tag、不创建 branch、不 push、
不 merge、不启动 rebuild，也不授权 selected return。

## Core Trunk / 内核主干

保存 reviewed Core history 和稳定项目状态的受保护主连续性线。

边界：Core trunk 不应接收 direct instance、research、quarantine、adapter、synthetic-history 或
tool-candidate merges。

## Core Baseline / 内核基线

用于 rollback、comparison 和 future rebuild planning 的 recoverable known-good Core reference。

边界：baseline 是锚点，不是 mutable experiment space，也不是 rebuild approval。

## Instance Sandbox Branch / 实例沙盒分支

用于探索可能的 01 instance behavior、style、self-hypotheses、synthetic history、tool candidates
或 local behavior 的受控分支。

边界：instance output 只能作为 candidate 或 evidence material。Instance memory 不是 Core memory，
instance identity 不是 Core identity。

## Quarantine Branch / 隔离分支

用于容纳 untrusted、suspicious、imported、adapter-shaped、model-claimed、contaminated 或
synthetic autobiographical material 的 containment branch。

边界：quarantine branches 不得 direct merge 到 Core trunk。

## Manual Selected Return / 人工选择回流

经过 human review 的、小范围、有来源标注的 candidate 或 quarantine material 回流到 Core。

边界：selected return 不是 automatic merge、branch promotion、identity adoption、memory adoption
或 tool trust update。

## Baseline Tag Advisor / 基线 Tag 建议器

可能的 future read-only report，根据 phase index、verification evidence 和 founder criteria 建议
baseline 或 milestone tags 的 candidate commits。

边界：advisor 不创建 tag，也不自动选择 commit。

## Baseline Tagging Plan / 基线 Tag 计划

P156 planning-only document，用于向 founder review 提出 candidate baseline tags、milestone tags、
branch fork points、manual command drafts 和 rebuild safety gates。

边界：plan 不是 Git execution。它不创建 tags、不创建 branches、不 push、不修改 git history，也不启动
rebuild。

## Candidate Baseline Tag / 候选基线 Tag

一个 proposed tag name 和 commit pair。只有在 founder confirmation 后，它未来才可能成为真实 Git tag。

边界：candidate tag 不是 existing tag，也不授权 rebuild、merge、branch creation 或 selected return。

## Manual Command Draft / 人工命令草案

作为 future operator guidance 展示的命令，例如 `git tag <tag> <commit>` 或
`git checkout -b <branch> <tag>`。

边界：draft 不是 execution permission。除非进入单独 founder-approved operation，否则必须保持不执行。
