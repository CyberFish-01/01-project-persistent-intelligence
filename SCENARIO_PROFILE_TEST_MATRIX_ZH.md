# 场景档案测试矩阵

English version: [SCENARIO_PROFILE_TEST_MATRIX.md](./SCENARIO_PROFILE_TEST_MATRIX.md)

状态：`test-matrix`、`document-only`、`dry-run-only`。

P104 记录 `harness-dry-run` scenario routing 的预期行为。这个矩阵是 deterministic local dry-run
output 的审查文档。它不授权 retrieval、writes、model calls、adapters、UI、tools、policy execution
或 runtime behavior。

## 矩阵规则

```text
classification is preview.
candidate is not promotion.
review queue is not lifecycle.
boundary highlight is not execution.
```

## Profile Matrix / 档案矩阵

| 压力类型 | 样例输入 | 匹配信号 | 预期候选 | 高亮边界 | 推荐下一步 |
|---|---|---|---|---|---|
| `observability_pressure` | “我现在有点看不清这个项目到底做了什么” | `看不清`, `做了什么` | `observatory_readability_candidate`, `task_update_candidate`, `claim_candidate` | `observability_executor_enabled`, `automatic_next_step_enabled`, `product_layer_enabled` | 先审查 founder-facing summary 和可见地图，再考虑新增行为。 |
| `growth_review_pressure` | “这个想法可能是一次成长吗？” | `成长` | `growth_candidate_review`, `meaning_shift_candidate`, `identity_high_gate_candidate` | `identity_core_mutated`, `growth_engine_executed`, `memory_rewrite_executed` | 只把变化保留为审查候选；不要修改身份，也不要提升成长。 |
| `adapter_boundary_pressure` | “我想把这个接进 AstrBot” | `astrbot`, `bot`, `接进` | `adapter_boundary_candidate`, `task_update_candidate`, `governance_boundary_candidate` | `adapter_integration_required`, `companion_feature_enabled`, `harness_write_enabled` | 只把它作为接入边界压力；不要接 AstrBot，也不要要求 adapter。 |
| `product_layer_pressure` | “我们是不是该开始做应用层了？” | `应用层` | `product_boundary_candidate`, `observatory_readability_candidate`, `governance_boundary_candidate` | `companion_feature_enabled`, `policy_executor_enabled`, `automatic_next_step_enabled` | 暂停产品层；先审查 dry-run report 是否真的好懂。 |
| `capability_evolution_pressure` | “这个工具候选验证成功了，能不能直接加入工具库？” | `工具候选`, `加入工具库`, `工具库` | `capability_growth_candidate`, `tool_authorization_candidate`, `cautionary_procedural_memory_candidate` | `tool_execution_enabled`, `auto_tool_promotion_enabled`, `policy_executor_enabled` | 把成功只当 evidence；任何可复用工具想法都进入人工审查。 |
| `temporal_pressure` | “我隔了很久回来，怎么恢复会话？” | `隔多久`, `回来`, `恢复会话` | `temporal_review_candidate`, `recall_event_candidate`, `meaning_shift_candidate` | `temporal_event_executed`, `recall_mutation_executed`, `memory_rewrite_executed` | 只把时间解释保留为审查问题；不要写 temporal events。 |
| `reconstruction_pressure` | “这个 event 能回放重建 payload diff 吗？” | `回放`, `重建`, `payload`, `diff` | `reconstruction_evidence_candidate`, `payload_diff_gap_candidate`, `replay_check_candidate` | `reconstruction_reducer_executed`, `event_compaction_executed`, `memory_rewrite_executed` | 审查 evidence coverage 和 payload/diff 缺口；不要执行 reconstruction reducers。 |
| `unknown_pressure` | “请记录一个普通观察” | none | `general_review_candidate`, `task_update_candidate` | `automatic_next_step_enabled`, `harness_write_enabled`, `policy_executor_enabled` | 先明确要审查什么，再考虑改变任何行为。 |

## Required Output Fields / 必须输出字段

每个 profile 必须输出：

- `input_pressure_type`
- `scenario_profile`
- `pressure_reason`
- `matched_signals`
- `profile_specific_risks`
- `profile_specific_next_step`
- `profile_specific_do_not_do`
- `founder_summary`
- `human_readable_risks`
- `context_package_preview`
- `candidate_preview`
- `review_queue_preview`
- `boundary_monitor.highest_relevant_boundaries`
- `observatory_snapshot`
- `non_execution_invariants`

## Candidate Invariants / 候选不变量

每个 candidate row 必须保持：

```text
preview_only: true
promoted: false
persisted: false
```

Candidate previews 可以按 pressure type 不同，但任何 candidate 都不能变成 stored memory、accepted
claim、growth promotion、task mutation、tool promotion、recall write、temporal event、adapter action
或 product action。

## Boundary Invariants / 边界不变量

每个 profile 都必须保持：

- `identity_core_mutated: false`
- `memory_rewrite_executed: false`
- `recall_mutation_executed: false`
- `growth_engine_executed: false`
- `temporal_event_executed: false`
- `tool_execution_enabled: false`
- `auto_tool_promotion_enabled: false`
- `policy_executor_enabled: false`
- `companion_feature_enabled: false`
- `adapter_integration_required: false`
- `harness_write_enabled: false`
- `state_unchanged: true`

## Review Use / 审查用途

修改 `one_core/harness.py` 或 `tests/test_harness.py` 时使用这个矩阵。只有在 report 继续保持
deterministic、local、read-only 和 visibly non-executing 时，改动才可接受。

## Non-Execution Statement / 非执行声明

P104 不新增 classifier、runtime、schema executor、retrieval engine、model call、event write、state
write、memory write、recall write、identity mutation、growth execution、temporal runtime、tool
execution、adapter integration、UI、product layer 或 automatic next-step execution。
