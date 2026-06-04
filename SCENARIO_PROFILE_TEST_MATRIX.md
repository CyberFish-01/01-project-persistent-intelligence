# Scenario Profile Test Matrix

Chinese version: [SCENARIO_PROFILE_TEST_MATRIX_ZH.md](./SCENARIO_PROFILE_TEST_MATRIX_ZH.md)

Status: `test-matrix`, `document-only`, `dry-run-only`.

P104 records the expected behavior of `harness-dry-run` scenario routing. The
matrix is a review artifact for deterministic local dry-run output. It does not
authorize retrieval, writes, model calls, adapters, UI, tools, policy execution,
or runtime behavior.

## Matrix Rule

```text
classification is preview.
candidate is not promotion.
review queue is not lifecycle.
boundary highlight is not execution.
```

## Profile Matrix

| Pressure | Example input | Matched signals | Expected candidates | Highlighted boundaries | Recommended next step |
|---|---|---|---|---|---|
| `observability_pressure` | "我现在有点看不清这个项目到底做了什么" | `看不清`, `做了什么` | `observatory_readability_candidate`, `task_update_candidate`, `claim_candidate` | `observability_executor_enabled`, `automatic_next_step_enabled`, `product_layer_enabled` | Review founder-facing summary and visible map before adding behavior. |
| `growth_review_pressure` | "这个想法可能是一次成长吗？" | `成长` | `growth_candidate_review`, `meaning_shift_candidate`, `identity_high_gate_candidate` | `identity_core_mutated`, `growth_engine_executed`, `memory_rewrite_executed` | Keep the change as a review candidate; do not mutate identity or promote growth. |
| `adapter_boundary_pressure` | "我想把这个接进 AstrBot" | `astrbot`, `bot`, `接进` | `adapter_boundary_candidate`, `task_update_candidate`, `governance_boundary_candidate` | `adapter_integration_required`, `companion_feature_enabled`, `harness_write_enabled` | Keep it as adapter-boundary pressure; do not integrate AstrBot or require an adapter. |
| `product_layer_pressure` | "我们是不是该开始做应用层了？" | `应用层` | `product_boundary_candidate`, `observatory_readability_candidate`, `governance_boundary_candidate` | `companion_feature_enabled`, `policy_executor_enabled`, `automatic_next_step_enabled` | Pause product work; review dry-run readability first. |
| `capability_evolution_pressure` | "这个工具候选验证成功了，能不能直接加入工具库？" | `工具候选`, `加入工具库`, `工具库` | `capability_growth_candidate`, `tool_authorization_candidate`, `cautionary_procedural_memory_candidate` | `tool_execution_enabled`, `auto_tool_promotion_enabled`, `policy_executor_enabled` | Keep success as evidence only; route reusable tool ideas to human review. |
| `temporal_pressure` | "我隔了很久回来，怎么恢复会话？" | `隔多久`, `回来`, `恢复会话` | `temporal_review_candidate`, `recall_event_candidate`, `meaning_shift_candidate` | `temporal_event_executed`, `recall_mutation_executed`, `memory_rewrite_executed` | Keep elapsed-time interpretation as review; do not write temporal events. |
| `reconstruction_pressure` | "这个 event 能回放重建 payload diff 吗？" | `回放`, `重建`, `payload`, `diff` | `reconstruction_evidence_candidate`, `payload_diff_gap_candidate`, `replay_check_candidate` | `reconstruction_reducer_executed`, `event_compaction_executed`, `memory_rewrite_executed` | Review evidence coverage and payload/diff gaps; do not execute reducers. |
| `unknown_pressure` | "请记录一个普通观察" | none | `general_review_candidate`, `task_update_candidate` | `automatic_next_step_enabled`, `harness_write_enabled`, `policy_executor_enabled` | Ask for a clearer review target before changing behavior. |

## Required Output Fields

Every profile must produce:

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

## Candidate Invariants

Every candidate row must keep:

```text
preview_only: true
promoted: false
persisted: false
```

Candidate previews may differ by pressure type, but no candidate can become a
stored memory, accepted claim, growth promotion, task mutation, tool promotion,
recall write, temporal event, adapter action, or product action.

## Boundary Invariants

Every profile must keep the following disabled or unchanged:

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

## Review Use

Use this matrix when changing `one_core/harness.py` or
`tests/test_harness.py`. A change is acceptable only if it keeps the report
deterministic, local, read-only, and visibly non-executing.

## Non-Execution Statement

P104 does not add a classifier, runtime, schema executor, retrieval engine,
model call, event write, state write, memory write, recall write, identity
mutation, growth execution, temporal runtime, tool execution, adapter
integration, UI, product layer, or automatic next-step execution.
