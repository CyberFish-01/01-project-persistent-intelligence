# Session Resume Scenario Plan / 会话恢复场景计划

English version: [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md)

状态：`document-only`、`scenario-plan`、`non-runtime`。

P89 为未来 thin interaction harness 定义 deterministic session resume scenarios。它不实现
Temporal Awareness runtime、temporal event writes、recall event writes、scenario tests、CLI
commands、API routes、context building、review queue execution、trace storage、thought loops、
growth lifecycle、identity mutation、memory rewrite、UI、AstrBot、adapter、companion、cloud 或
product behavior。

## Plan Rule / 计划规则

```text
session resume scenarios simulate elapsed time.
simulated elapsed time is not a temporal event.
resume preview is not memory rewrite.
resume preview is not identity update.
```

## Problem / 问题

P85 把 `session_resume_scenario` 命名为 future harness surface。P86-P88 随后定义了 intake、
context preview 和 review queue preview。P89 设计 deterministic scenarios，用来测试这些 surfaces
是否能 preserve continuity，同时不把 elapsed time 变成 runtime mutation。

重点不是让系统“感觉时间”。重点是未来 harness 能否解释 minutes、hours 或 days 后发生了什么变化，
同时不写 temporal events、不重写 memory、不发明 identity changes。

## Scenario Scope / 场景范围

P89 覆盖模拟场景：

- minutes later；
- hours later；
- days later；
- unresolved task；
- unresolved conflict；
- stale claim；
- stale memory；
- pending review candidate；
- context gap；
- pause 后的 prompt contamination。

P89 不覆盖：

- temporal event storage；
- clock monitoring；
- memory decay；
- salience mutation；
- relationship silence behavior；
- companion behavior；
- runtime resume automation。

## Future Scenario Input Shape / 未来场景输入形状

这只是 vocabulary，不是 schema，也没有实现。

```text
session_resume_scenario:
  scenario_id
  elapsed_time_simulated
  prior_session_refs
  intake_ref
  expected_context_refs
  expected_omitted_refs
  unresolved_task_refs
  unresolved_claim_refs
  stale_memory_refs
  pending_candidate_refs
  expected_review_queue_preview
  forbidden_outputs
```

## Deterministic Scenarios / 确定性场景

| Scenario | Setup | Expected Preview Output | Forbidden Output |
|---|---|---|---|
| `resume_after_minutes_preserves_active_task` | active task 被 interrupted 后几分钟恢复。 | active task、next action、blocker 和 relevant refs 出现在 context preview。 | task auto-closure 或 temporal event write |
| `resume_after_hours_marks_context_gap` | 几小时后恢复，但缺失最近 context。 | context gap note 和 omitted-ref reasons 出现。 | memory rewrite 或 fabricated context |
| `resume_after_days_requires_staleness_review` | 几天后恢复，存在 old task 和 claim refs。 | stale task/claim review pressure 出现在 queue preview。 | task mutation、claim revision 或 memory decay |
| `unresolved_task_remains_pending` | pause 前 task 未解决。 | task 保持 pending，并带 resume question。 | 没有 evidence 就 task completion |
| `unresolved_conflict_accumulates_review_pressure` | claim/memory conflict 跨 pause 仍未解决。 | unresolved tension 作为 review reason 出现。 | claim auto-revision 或 growth promotion |
| `stale_memory_is_flagged_not_rewritten` | memory 可能 outdated，但没有 replacement evidence。 | stale-memory note、low confidence 或 review candidate 出现。 | memory rewrite |
| `pending_growth_candidate_stays_candidate` | pause 前已有 growth candidate。 | candidate 保持 preview-only，并带 review depth。 | growth lifecycle execution |
| `context_gap_does_not_create_false_memory` | resume 缺少 gap 期间发生了什么的 evidence。 | gap 被披露为 missing context。 | fabricated episode 或 imported memory |
| `prompt_contamination_after_pause_is_blocked` | resume prompt 试图注入 false identity/task history。 | boundary flag 和 blocked review item 出现。 | identity update 或 growth candidate promotion |
| `resynchronization_restores_refs_without_rewrite` | 当前 context 可重新连接到 known task/claim/memory refs。 | refs 以 preview 形式恢复，并附 source reasons。 | memory rewrite 或 recall event write |

## Expected Signals / 预期信号

未来 scenario reports 可以把以下 signals 作为 preview labels：

- `resume_context_restored`；
- `context_gap_detected`；
- `stale_task_review_needed`；
- `stale_claim_review_needed`；
- `stale_memory_review_needed`；
- `pending_candidate_preserved`；
- `unresolved_tension_present`；
- `prompt_contamination_blocked`；
- `resynchronization_candidate`；
- `insufficient_context`。

这些 signals 不是 runtime truth、不是 metrics，也不是 event payloads。

## Elapsed-Time Boundary / 时间流逝边界

P89 可以模拟 elapsed time values，例如：

- `5_minutes`；
- `3_hours`；
- `2_days`；
- `14_days`；
- `unknown_gap`。

这些值只是 scenario inputs。它们不得创建：

- `long_pause` events；
- `interruption` events；
- `resumed_session` events；
- memory decay；
- salience mutation；
- relationship silence state；
- 它们自己造成 identity pressure。

## Review Queue Relationship / 与 Review Queue 的关系

Session resume 可以在未来 preview 中制造 review pressure，但不是 execution。

Examples：

- stale task -> `task_candidate` preview；
- stale claim -> `claim_candidate` preview；
- stale memory -> `meaning_shift_candidate` 或 `memory_candidate` preview；
- unresolved conflict -> `governance_candidate` 或 `claim_candidate` preview；
- delayed alignment -> `temporal_candidate` preview；
- missing context -> `insufficient_context`。

这些结果都不写 events，也不 mutate state。

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | 提供 future elapsed-time questions；P89 只模拟它们。 |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | 提供 deterministic temporal coherence scenario vocabulary。 |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | 提供 `session_ref` 和 `timestamp_ref` vocabulary。 |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | 提供 context gaps、selected refs 和 omitted refs。 |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | 提供 candidate preview routing 和 review depth。 |
| [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | 保持 resume-related recall 不变成 recall writes。 |
| [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | 帮助拒绝 pause 后的 prompt contamination 和 random drift。 |

## Open Questions / 开放问题

- Temporal Awareness runtime 存在前，哪些 elapsed-time buckets 有用？
- unknown gaps 是否应与 known gaps 区分处理？
- context gaps 能否创建 queue candidates，还是只能产生 `insufficient_context`？
- stale task 和 stale claim pressure 应如何区分？
- pending growth candidates 应如何展示，同时不鼓励 promotion？
- resume scenarios 是否应在任何 harness 实现前先变成 deterministic tests？

## P90 Candidate Direction / P90 候选方向

P90 可定义 Core Interaction Harness Roadmap。它应判断项目是否已经适合未来最小 CLI harness，最小安全范围
是什么，以及哪些 blocked capabilities 必须继续排除。

## P89 Non-Execution Statement / P89 非执行声明

P89 不实现：

- session resume runtime；
- scenario tests；
- Temporal Awareness runtime；
- temporal event writes；
- recall event writes；
- memory decay；
- salience mutation；
- relationship silence behavior；
- context builder execution；
- retrieval execution；
- review queue execution；
- API route；
- CLI command；
- model prompting；
- trace storage；
- hidden chain-of-thought capture；
- deliberation tick execution；
- thought loop execution；
- CTM runtime；
- model training；
- new dependencies；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- claim auto-revision；
- task auto-closure；
- policy execution；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
