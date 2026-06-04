# Payload / Diff Capture Policy RFC v0.1 / Payload 与 Diff 捕获策略 RFC v0.1

English version: [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md)

状态：`document-only`、`policy-rfc`、`non-runtime`。

P66 定义未来按 target path 处理 payload、diff、snapshot 和 reference-only 的 policy。它不
capture payloads，不 mutate event schemas，不 rewrite events，不 compact events，不执行
reducers，不 rebuild state，不 rollback state，也不 mutate identity。

## Problem / 问题

P39 显示当前 events 大多已经 transition-reference complete，但还不是 object-diff complete。
P40 创建了 review-only capture policy proposal layer。P65 又定义了未来 reconstruction
reducer contract 需要什么。

P66 把这些线索连接起来，在任何 schema work 或 payload capture 存在前定义 target-path
policy vocabulary。

## Core Rule / 核心规则

```text
capture policy is not capture.
payload recommendation is not schema mutation.
diff requirement is not reducer execution.
```

P66 不修改任何现有 event record。

## Capture Modes / 捕获模式

未来 target paths 可以使用这些 policy modes：

| Mode | Meaning | Typical Use |
|---|---|---|
| `reference_only_ok` | event reference 和 provenance 足够 | derived reports、non-state summaries |
| `payload_hint_required` | 需要 lightweight description，但不需要 full object | low-risk review artifacts |
| `snapshot_link_required` | 需要 stable before/after snapshot references | lifecycle suppression、rollback preview |
| `object_diff_required` | 需要 explicit field-level 或 object-level diff | claims、tasks、review decisions |
| `full_payload_and_diff` | 需要 full object payload 和 explicit diff | memory records、protected state transitions |
| `blocked_until_contract` | reducer 或 schema contract 缺失 | protected identity 或 ambiguous paths |

这些 modes 是 policy vocabulary，不是 active schema。

## Target Path Policy Matrix / Target Path 策略矩阵

| Target Path Class | Recommended Mode | Reason | Gate |
|---|---|---|---|
| event/audit records | `blocked_until_contract` | event logs 不能被 capture rewrite | governance review |
| Identity Core | `blocked_until_contract` | protected identity path | Identity Gate |
| Subject Kernel | `blocked_until_contract` | protected subject anchor | Identity Gate |
| identity-adjacent memory | `full_payload_and_diff` | future reconstruction 必须保留 evidence 和 change boundary | high-gate review |
| episodic memory | `full_payload_and_diff` | object state 对未来 meaning shift 重要 | memory review |
| semantic memory | `full_payload_and_diff` | abstraction 需要 provenance 和 diff | memory review |
| imported memory | `snapshot_link_required` 或 `full_payload_and_diff` | external provenance 和 privacy 重要 | privacy/governance review |
| claim graph records | `object_diff_required` | claim revision 需要 explicit before/after evidence | claim review |
| task hub records | `object_diff_required` | operational continuity 需要 lifecycle clarity | task review |
| Dream artifacts | `snapshot_link_required` | artifacts 是 proposals，不应 rewrite active memory | Dream review |
| governance review objects | `object_diff_required` | review state 必须可审计 | governance review |
| derived reports | `reference_only_ok` | reports 可以 regenerate 或 cite | report review |
| world/context orientation | `snapshot_link_required` 或 `blocked_until_contract` | 处理不当会滑向 identity | governance 或 Identity Gate |

这个 matrix 是起始 policy map。它不 approve capture。

## Required Provenance / 必需 Provenance

未来 capture policy 应要求：

- `event_id`；
- `sequence`；
- `timestamp`；
- `operation_class`；
- `target_path`；
- `target_identity`；
- `source_update_id`；
- `actor_or_process_ref`；
- `evidence_refs`；
- `policy_decision_refs`；
- `privacy_scope`；
- `review_gate`。

P66 不把这些 fields 加入 events。

## Diff Requirements / Diff 要求

当选择 `object_diff_required` 或 `full_payload_and_diff` 时，未来 design 必须定义：

- canonical object identity；
- before reference；
- after reference；
- changed fields；
- added fields；
- removed fields；
- redaction policy；
- hash strategy；
- reversible snapshot availability；
- missing-field behavior。

如果这些没有定义，该 path 保持 `blocked_until_contract`。

## Snapshot Requirements / Snapshot 要求

以下情况可能需要 snapshot links：

- lifecycle decision suppresses active context；
- rollback preview 需要 before/after comparison；
- imported memory provenance 敏感；
- Dream artifact state 必须保持 proposal-only；
- world/context orientation changes 可能影响 continuity。

Snapshot link 不意味着 automatic rollback 被允许。

## Privacy And Redaction / 隐私与脱敏

Payload capture 可能增加 privacy risk。未来 policy 必须定义：

- sensitive source handling；
- imported log redaction；
- user/session boundary；
- payload hashing；
- selective omission；
- audit-safe summaries；
- governance access level。

如果 privacy scope 不清楚，full payload capture 应被 blocked。

## Forbidden Outcomes / 禁止结果

P66 不得被解释为允许：

- capture payloads；
- mutate event schemas；
- rewrite existing event records；
- compact events；
- delete or summarize event history；
- execute reconstruction reducers；
- rebuild object state；
- approve automatic rollback；
- mutate Identity Core；
- promote memory or growth。

## Relationship To P40 / 与 P40 的关系

P40 创建了 review-only event payload capture policy proposal mechanism。

P66 是在 P65 reducer contract boundary 之后重新整理同一问题的 foundation RFC。它在未来
implementation work 之前澄清 target-path policy vocabulary。

P40 和 P66 都不 capture payloads。

## Relationship To P65 / 与 P65 的关系

P65 说明 reducers 需要 payload/diff preconditions。P66 说明 target paths 可以如何为这些
preconditions 分类。

Reducer contract still comes before reducer execution. Capture policy still
comes before payload capture。

## Non-Execution Flags / 非执行标记

P66 artifacts 必须保留：

```yaml
event_payload_capture_executed: false
event_schema_mutation_allowed: false
events_modified: false
event_compaction_executed: false
reconstruction_reducer_executed: false
reconstruction_executed: false
state_rebuilt: false
state_mutated: false
identity_core_mutated: false
```

这些是 policy boundary reminders，不是 runtime outputs。

## P67 Handoff / P67 交接

P67 应把 P54-P66 综合成 Foundation Roadmap，区分 stable foundation、future contracts、
blocked runtime work 和 low-risk consolidation。

在此之前，payload/diff capture 仍未实现。
