# 夜间 Harness 工作总结

English version: [OVERNIGHT_HARNESS_WORK_SUMMARY.md](./OVERNIGHT_HARNESS_WORK_SUMMARY.md)

状态：`P110`、`summary`、`audit`、`document-only`、`non-runtime`。

P110 收口夜间 harness 改进周期。它记录 P102-P110 改了什么、验证了什么、哪些边界保持 blocked，
以及明天应审查什么。它不进入 P111，也不 push 到 GitHub。

## Commit 范围

本轮前起点 commit：`2e1fdca Add harness usability review`

夜间第一条 commit：`3fa9888 Add harness input scenario routing`

P110 summary 前终点 commit：`d33a5db Add harness roadmap`

P110 summary commit：等待本文件提交后确定。

## Phase 总结

| Phase | Commit | 实际变化 | 边界 |
|---|---|---|---|
| P102 | `3fa9888` | 加入 deterministic input pressure classification 和 scenario routing，覆盖 observability、growth、adapter、product、capability、temporal、reconstruction、unknown。 | 不检索、不写入、不接 adapter、不执行工具或 runtime。 |
| P103 | `f120f75` | 改进 founder-facing readability，加入 summary、人话风险、具体 next step 和 do-not-do list。 | 只报告，不自动执行下一步。 |
| P104 | `58c9c4a` | 加入双语 Scenario Profile Test Matrix。 | document-only expected-output matrix。 |
| P105 | `22748de` | 强化 boundary monitor，显示 disabled capabilities、unchanged state、active violations 和 all-disabled status。 | 只是 audit output，不是 policy executor。 |
| P106 | `de6addb` | 专门化 candidate previews，加入 intent、selection reason、blocked promotion reason 和 manual review target。 | candidate 不是 promotion，也不是 persistence。 |
| P107 | `cc6e63f` | 专门化 review queue previews，加入 queue intent、gate reason、blocked lifecycle 和 manual-review-only next action。 | review routing 不是 lifecycle。 |
| P108 | `719f838` | 对八类输入复评 harness usability，诚实评分从 P101 6.5/10 提升到 P108 8.0/10。 | review-only，不新增能力。 |
| P109 | `d33a5db` | 加入 Harness Roadmap，说明 harness 能看见什么、看不见什么，以及下一步只能规划哪些只读工作。 | roadmap 不是 implementation approval。 |
| P110 | pending | 加入本夜间总结和最终 stop condition。 | summary-only；stop before P111。 |

## Harness 现在能做什么

- 接收一句本地 CLI 输入。
- 把输入分类到 deterministic pressure profile。
- 显示 matched signals 和 route reason。
- 显示 profile-specific context references。
- 显示 pressure-specific candidates。
- 显示 pressure-specific review gates。
- 解释为什么 candidates 不能 promotion。
- 解释为什么 review gates 不能创建 lifecycle。
- 突出最相关的 disabled boundaries。
- 输出 Markdown 或 JSON。
- 只在显式 `--output` 时写 report 文件，从不写 state。

## Harness 仍不能做什么

- 真实 memory retrieval。
- 检查或修改 claim graph。
- 读取或写入 live task state。
- 写 events、episodes、memories、recalls 或 temporal events。
- 修改 Identity Core。
- 执行 growth lifecycle。
- 执行工具或提升工具。
- 调用模型或 external API。
- 接 AstrBot 或 adapters。
- 进入 Companion、UI、Web、dashboard runtime 或 product behavior。
- 执行 reconstruction reducers。
- 压缩 events。
- 执行 policy 或 automatic next steps。

## 边界审计

以下边界在整个周期中保持 false/disabled：

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

没有任何 phase 实现 CTM、Temporal Awareness runtime、thought loops、真实 retrieval、state writes、
product layer、adapter integration 或 tool execution。

## 验证

P110 summary 前的最新检查：

- `git diff --check`：通过。
- Markdown local link check：通过。
- Forbidden active-pattern search：无命中。
- `env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest`：通过，149 tests。
- CLI smoke checks：P102-P109 期间跑过 markdown/json 与 zh/en route。
- P108 batch run：八类输入都跑过 zh markdown、zh json、en markdown，输出写在仓库外。
- P108 state check：传入的 `--state-dir` 没有被创建。

## 可用性变化

P101 baseline：**6.5 / 10**。

P108 re-review：**8.0 / 10**。

提升来自：

- pressure-specific routing；
- matched signal display；
- founder-facing one-screen summary；
- profile-specific risks 和 next step；
- specialized candidate previews；
- specialized review queue previews；
- 更强的 boundary monitor。

仍然不足：

- context package preview 仍是静态的；
- risk explanations 仍有模板感；
- 不检查真实 evidence 或 memory relevance；
- English internal keys 在部分中文 rows 里仍偏多。

## 明天候选方向

推荐明天顺序，需要 founder / CTO 确认：

1. Founder / CTO review of the harness output shape。
2. Read-only Context Preview Plan，document-only。
3. Fixture-first context preview implementation，仅在明确批准后。
4. Harness output contract stabilization，仅在 founder-facing 形状被接受后。

不要自动开始 P111。

## Stop Condition

P110 停止夜间 harness cycle。本 summary commit 后，仓库应保持 clean。不执行 push。P111 保持未进入。

## 非执行声明

P110 是 summary 和 audit artifact。它不授权 runtime implementation、product work、adapter
integration、Companion behavior、model calls、真实 retrieval、event writes、memory writes、
recall writes、identity mutation、growth execution、temporal runtime、tool execution、policy
execution、reconstruction reducer execution、event compaction、automatic tool promotion 或 automatic
roadmap execution。
