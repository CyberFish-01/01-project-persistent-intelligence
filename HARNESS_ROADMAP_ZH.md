# 试验台路线图

English version: [HARNESS_ROADMAP.md](./HARNESS_ROADMAP.md)

状态：`P109`、`roadmap`、`document-only`、`non-runtime`。

P109 说明 P102-P108 之后，当前 `harness-dry-run` 现在能看见什么、仍然看不见什么。它不新增功能、
不调用模型、不执行 retrieval、不写 state、不写 memory、不写 recall event、不执行工具、不创建
review lifecycle、不接 adapter、不进入 UI/product，也不授权 P110 之后的 implementation。

## 路线图规则

```text
harness 是压力观察器，不是交互 runtime。
classification 不是理解。
preview 不是 persistence。
review routing 不是 lifecycle。
next-step recommendation 不是 execution。
```

## 当前 Harness 形状

已实现命令：

```bash
python3 -m one_core.cli harness-dry-run
```

它是本地、deterministic、no-write dry-run。它接收一句输入，输出 Markdown 或 JSON，展示这条输入会如何经过：

- 输入预览；
- deterministic pressure classification；
- 上下文包预览；
- 候选项预览；
- 审查队列预览；
- 边界监视器；
- 观察台快照；
- 非执行边界。

## Harness 现在能看见什么

| 区域 | 能看见什么 | 当前证据 |
|---|---|---|
| 输入信封 | 用户输入、session id、actor id、privacy scope、CLI 来源、no-write flag。 | `intake_preview` |
| 压力类型 | deterministic keyword / rule-based pressure type。 | `input_pressure_type`、`matched_signals` |
| 场景 profile | founder-facing route、reason、risks、do-not-do list、manual next step。 | `scenario_profile`、`founder_summary` |
| 上下文主题 | 与 pressure class 相关的静态 foundation refs。 | `context_package_preview` |
| 候选形状 | 按 pressure 专门化的 candidates，含 intent、selection reason、blocked promotion 和 manual review target。 | `candidate_preview` |
| 审查门形状 | 按 pressure 专门化的 review gates，含 queue intent、gate reason、blocked lifecycle 和 manual-review-only next action。 | `review_queue_preview` |
| 边界可见性 | disabled forbidden capabilities 和当前最高相关边界。 | `boundary_monitor` |
| 观察台摘要 | 与当前 pressure 对齐的短状态快照。 | `observatory_snapshot` |

## Harness 仍然看不见什么

| 缺失区域 | 为什么重要 | 为什么仍然 blocked |
|---|---|---|
| 真实记忆相关性 | harness 不知道哪些真实 memories 重要。 | 真实 retrieval 可能被误读成 continuity 或 prompt construction。 |
| 真实说法证据 | 它不能把输入和真实 claim graph 对比。 | claim mutation 和 automatic belief revision 仍 blocked。 |
| 真实任务状态 | 它不能读取或更新 live tasks。 | task writes 和 automatic roadmap execution 仍 blocked。 |
| 真实 event payload 缺口 | 它不能检查 events 是否有足够 payload/diff。 | reducer execution 和 event compaction 仍 blocked。 |
| 真实时间状态 | 它不能计算 elapsed-time effects 或 staleness。 | temporal runtime 和 temporal event writes 仍 blocked。 |
| 真实工具证据 | 它不能验证 tool success、failure 或 reproducibility。 | tool execution 和 automatic tool promotion 仍 blocked。 |
| 真实 adapter/session 压力 | 它不能观察 AstrBot、platform sessions 或外部流量。 | adapter integration 仍 blocked。 |

## 边界状态

这些继续明确 disabled：

- identity mutation；
- memory rewrite；
- recall event write；
- growth execution；
- temporal runtime；
- CTM runtime；
- tool execution；
- automatic tool promotion；
- policy executor；
- Companion layer；
- UI/Web/product layer；
- AstrBot/adapter integration；
- reconstruction reducer execution；
- event compaction；
- harness state write；
- automatic next-step execution。

## 是否适合进入 Read-Only Context Preview Refinement？

可以规划，但要带约束。

P108 表明 harness 已经足够可读，可以规划下一步只读 context preview refinement。这个 future refinement
仍应 fixture-first 或 static-source-first。它不应做 live memory retrieval、不应构造 prompt、不应调用模型、
不应修改 context、不应写 trace、不应写 recall event、不应分配 durable review ownership。

安全候选方向：

- 让 `context_package_preview` 更清楚解释 selected refs、omitted refs 和 missing evidence；
- 使用 deterministic static fixture refs，而不是真实 retrieval；
- 增加测试证明 state directory 不变化；
- 所有 candidate 和 review queue 输出继续 preview-only；
- 所有 forbidden boundary flags 继续 false/disabled。

现在还不安全：

- live memory retrieval；
- event-log reducer checks；
- claim graph mutation；
- task writes；
- adapter session import；
- model-generated context selection；
- thought trace storage；
- temporal runtime。

## 推荐下一步只读工作

| 优先级 | 候选 | 为什么现在做 | 风险 |
|---|---|---|---|
| 1 | Harness Work Summary | 在继续变化前，先收口 P102-P110 审计摘要。 | 低；document-only。 |
| 2 | Founder / CTO Review | 让人判断 harness 是否已经足够好懂。 | 低；防止系统自己越做越远。 |
| 3 | Read-Only Context Preview Plan | 先定义 selected/omitted/gap fields，再谈代码。 | 中；容易诱发真实 retrieval。 |
| 4 | Fixture-First Context Preview Implementation | 只有明确批准后才做；使用 deterministic fixtures。 | 中；必须证明 no writes 和 no retrieval。 |
| 5 | Harness Output Contract Stabilization | founder-facing 形状接受后，再冻结字段名。 | 中；可能过早固化。 |

## 后推工作

不要从 P109 开始这些：

- Companion behavior；
- UI、Web、dashboard runtime 或 product surface；
- AstrBot 或 adapter integration；
- model calls 或 external APIs；
- real retrieval；
- memory writes 或 recall event writes；
- growth lifecycle；
- temporal runtime；
- tool execution 或 tool promotion；
- policy executor；
- reconstruction reducers 或 event compaction。

## 与近期 phases 的关系

| Phase | 关系 |
|---|---|
| P100 | 实现第一版 no-write dry-run command。 |
| P101 | 发现第一版太静态，评分 6.5/10。 |
| P102 | 加入 deterministic pressure classification 和 scenario routing。 |
| P103 | 加入 founder summary、人话风险、下一步和 do-not-do list。 |
| P104 | 记录 scenario profile test matrix。 |
| P105 | 强化 boundary monitor output。 |
| P106 | 专门化 candidate preview rows。 |
| P107 | 专门化 review queue preview rows。 |
| P108 | 复评 usability，当前形状评分 8.0/10。 |

## P110 候选

推荐 P110：**Overnight Harness Work Summary / 夜间 Harness 工作总结**。

它应记录：

- 起止 commits；
- P102-P110 phase summaries 和 hashes；
- tests 和 smoke checks；
- boundary status；
- usability score 从 P101 到 P108 的变化；
- 明天候选方向；
- 明确 stop before P111。

## 非执行声明

P109 只是 roadmap。它不授权 runtime implementation、product work、adapter integration、
Companion behavior、model calls、真实 retrieval、event writes、memory writes、recall writes、
identity mutation、growth execution、temporal runtime、tool execution、policy execution、
reconstruction reducer execution、event compaction、automatic tool promotion 或 automatic roadmap
execution。
