# Reconstruction Reducer Contract RFC v0.1 / 重建 Reducer 契约 RFC v0.1

English version: [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md)

状态：`document-only`、`contract-rfc`、`non-runtime`。

P65 定义未来 reconstruction reducer 在 object-level 或 full-state reconstruction 被考虑前
必须满足的最小 contract。它不实现 reducers，不执行 reconstruction，不 rebuild state，
不 capture payloads，不 mutate event schemas，不 rewrite events，不 compact events，不 rollback
state，也不 mutate identity。

## Problem / 问题

P41 已确认当前 events 可用于 deterministic replay 和 transition projection，但还不足以支撑
object-level 或 full-state reconstruction。

P42-P49 随后建立了 reconstruction evidence vocabulary、coverage mapping、prioritization、
checklist review、evidence request tracking 和 evidence request lifecycle decisions。这些仍然
是 governance artifacts。它们还没有定义 reducer 的 execution contract。

P65 定义这个未来 contract 的边界。

## Core Rule / 核心规则

```text
reducer contract is not reducer execution.
reconstruction evidence is not reconstruction.
payload policy is not payload capture.
```

在未来 phase 定义并验证 runtime implementation 之前，reducer execution 仍然 forbidden。

## Required Contract Sections / 必需契约章节

未来 reducer contract 必须定义：

| Section | Required Question |
|---|---|
| input envelope | reducer 可以消费什么 event/evidence object？ |
| target path identity | 正在 reconstruction 的 state path 是哪个？ |
| operation semantics | 该 transition 表示什么 operation？ |
| payload/diff preconditions | 需要哪些 payload、diff、snapshot 或 reference evidence？ |
| protected path gates | 哪些 target paths 需要 Identity Gate 或 governance review？ |
| deterministic output | reducer 必须产生什么 exact output？ |
| validation metadata | 如何在不盲信 reducer 的情况下检查 output？ |
| audit trail | reducer reasoning 如何可检查？ |
| failure mode | evidence 缺失或模糊时怎么办？ |
| non-execution flags | contract 如何证明 P65 没有执行任何东西？ |

P65 只把这些章节记录为未来 contract requirements。

## Candidate Future Input Envelope / 候选未来输入 Envelope

未来 reducer input 应明确且有边界：

- `event_id`；
- `sequence`；
- `timestamp`；
- `operation_class`；
- `target_path`；
- `target_identity`；
- `source_update_id`；
- `transition_reference`；
- `before_ref`；
- `after_ref`；
- `object_payload_ref`；
- `object_diff_ref`；
- `rollback_snapshot_ref`；
- `seed_state_ref`；
- `validation_context_ref`；
- `policy_decision_refs`。

这些 names 是 RFC vocabulary，不是当前 schema。

## Target Path Identity / Target Path 身份

Reducer contracts 必须区分 target path classes：

- protected subject paths；
- Identity Core 或 identity-adjacent paths；
- world/context orientation paths；
- memory records；
- claim graph records；
- task hub records；
- event/audit records；
- derived reports。

Protected identity paths 需要更高 gate。Event/audit paths 绝不能被 reconstruction rewrite。

## Operation Semantics / Operation 语义

未来 reducer contract 必须先定义 operation classes，才能考虑执行：

- append record；
- update review status；
- lifecycle decision；
- archive or suppress from active context；
- add evidence link；
- create report-only artifact；
- preview rollback impact；
- derived projection。

Contract 也必须定义 forbidden operations：

- direct Identity Core rewrite；
- memory rewrite；
- event rewrite；
- event compaction；
- policy execution；
- automatic rollback；
- automatic growth；
- platform-owned identity update。

## Payload / Diff Preconditions / Payload 与 Diff 前置条件

除非相关 target path 已有 accepted payload/diff policy，否则不能考虑 reducer execution。

可能的未来 precondition types：

- reference-only is sufficient；
- payload hint required；
- full object payload required；
- object diff required；
- snapshot link required；
- seed/pre-event state required；
- rollback snapshot required；
- payload hash required。

P65 不选择这些 policies。P66 可以定义 target-path capture policy。

## Protected Path Gates / 受保护路径 Gate

Reducers 不能把所有 target paths 等同处理。

未来 contracts 必须为以下路径要求 high-gate review：

- Identity Core；
- Subject Kernel；
- identity-adjacent memory；
- continuity anchors；
- 可能变成 identity 的 world/context orientation；
- privacy-sensitive imported memory。

如果 gate 缺失，reducer outcome 必须 blocked，而不是 guessed。

## Determinism Requirements / 确定性要求

Reducer contract 必须定义：

- stable input ordering；
- deterministic operation semantics；
- canonical target path identity；
- explicit missing-evidence behavior；
- reproducible output representation；
- versioned reducer contract id；
- hashable input and output references。

如果相同 evidence 的两次运行产生不同 output，该 reducer contract 不可接受。

## Failure Modes / 失败模式

Missing evidence 必须产生 reviewable failure，而不是 reconstruction：

- `missing_payload`；
- `missing_diff`；
- `missing_snapshot`；
- `ambiguous_target_path`；
- `protected_gate_missing`；
- `schema_contract_missing`；
- `event_sequence_gap`；
- `source_update_missing`；
- `identity_path_blocked`；
- `insufficient_context`。

Failure 是未来 governance 的 evidence。它不是推断 state 的许可。

## Validation Metadata / 验证元数据

未来 reducer output 必须携带 validation metadata：

- reducer contract id；
- input evidence refs；
- target path class；
- operation class；
- precondition status；
- gate status；
- output hash；
- validation result；
- rejected assumptions；
- state mutation flag；
- reconstruction execution flag。

P65 不创建 validation code。

## Non-Execution Flags / 非执行标记

P65 artifacts 必须保留：

```yaml
reconstruction_reducer_executed: false
reconstruction_executed: false
event_payload_capture_executed: false
event_schema_mutation_allowed: false
event_compaction_executed: false
events_modified: false
state_rebuilt: false
state_mutated: false
identity_core_mutated: false
```

这些 flags 是 RFC vocabulary 和 boundary reminders。它们不是 P65 runtime outputs。

## Relationship To Replay / 与 Replay 的关系

Replay 当前验证 transition projection 和 audit references。

Reconstruction reducer 会更严格。它需要足够的 payload/diff evidence 来 rebuild object
state，而不只是证明 transition 发生过。

P65 不改变 replay。

## Relationship To Payload / Diff Capture Policy / 与 Payload/Diff Capture Policy 的关系

P65 定义 reducer contract 需要什么。P66 应定义哪些 target paths 需要 full payload、
object diff、snapshot link 或 reference-only treatment。

Reducer contract comes before reducer execution. Capture policy comes before
payload capture。

## P66 Handoff / P66 交接

P66 应定义按 target path 组织的 Payload / Diff Capture Policy RFC。

在此之前，reconstruction reducer execution 仍然 blocked。
