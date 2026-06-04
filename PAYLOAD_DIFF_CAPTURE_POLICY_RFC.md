# Payload / Diff Capture Policy RFC v0.1

Chinese version: [PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md)

Status: `document-only`, `policy-rfc`, `non-runtime`.

P66 defines future target-path policy for payload, diff, snapshot, and
reference-only treatment. It does not capture payloads, mutate event schemas,
rewrite events, compact events, execute reducers, rebuild state, roll back
state, or mutate identity.

## Problem

P39 showed that current events are mostly transition-reference complete but not
object-diff complete. P40 created a review-only capture policy proposal layer.
P65 then defined what a future reconstruction reducer contract would require.

P66 connects those threads by defining target-path policy vocabulary before any
schema work or payload capture exists.

## Core Rule

```text
capture policy is not capture.
payload recommendation is not schema mutation.
diff requirement is not reducer execution.
```

No existing event record is modified by P66.

## Capture Modes

Future target paths may use these policy modes:

| Mode | Meaning | Typical Use |
|---|---|---|
| `reference_only_ok` | event reference and provenance are enough | derived reports, non-state summaries |
| `payload_hint_required` | lightweight description is needed, but full object is not | low-risk review artifacts |
| `snapshot_link_required` | stable before/after snapshot references are required | lifecycle suppression, rollback preview |
| `object_diff_required` | explicit field-level or object-level diff is required | claims, tasks, review decisions |
| `full_payload_and_diff` | full object payload and explicit diff are required | memory records, protected state transitions |
| `blocked_until_contract` | reducer or schema contract is missing | protected identity or ambiguous paths |

These modes are policy vocabulary, not active schema.

## Target Path Policy Matrix

| Target Path Class | Recommended Mode | Reason | Gate |
|---|---|---|---|
| event/audit records | `blocked_until_contract` | event logs must not be rewritten by capture | governance review |
| Identity Core | `blocked_until_contract` | protected identity path | Identity Gate |
| Subject Kernel | `blocked_until_contract` | protected subject anchor | Identity Gate |
| identity-adjacent memory | `full_payload_and_diff` | future reconstruction must preserve evidence and change boundary | high-gate review |
| episodic memory | `full_payload_and_diff` | object state matters for future meaning shift | memory review |
| semantic memory | `full_payload_and_diff` | abstraction needs provenance and diff | memory review |
| imported memory | `snapshot_link_required` or `full_payload_and_diff` | external provenance and privacy matter | privacy/governance review |
| claim graph records | `object_diff_required` | claim revision needs explicit before/after evidence | claim review |
| task hub records | `object_diff_required` | operational continuity needs lifecycle clarity | task review |
| Dream artifacts | `snapshot_link_required` | artifacts are proposals and should not rewrite active memory | Dream review |
| governance review objects | `object_diff_required` | review state must be auditable | governance review |
| derived reports | `reference_only_ok` | reports can be regenerated or cited | report review |
| world/context orientation | `snapshot_link_required` or `blocked_until_contract` | may drift into identity if mishandled | governance or Identity Gate |

The matrix is a starting policy map. It does not approve capture.

## Required Provenance

Future capture policy should require:

- `event_id`;
- `sequence`;
- `timestamp`;
- `operation_class`;
- `target_path`;
- `target_identity`;
- `source_update_id`;
- `actor_or_process_ref`;
- `evidence_refs`;
- `policy_decision_refs`;
- `privacy_scope`;
- `review_gate`.

P66 does not add these fields to events.

## Diff Requirements

When `object_diff_required` or `full_payload_and_diff` is chosen, future design
must define:

- canonical object identity;
- before reference;
- after reference;
- changed fields;
- added fields;
- removed fields;
- redaction policy;
- hash strategy;
- reversible snapshot availability;
- missing-field behavior.

If these are not defined, the path remains `blocked_until_contract`.

## Snapshot Requirements

Snapshot links may be required when:

- a lifecycle decision suppresses active context;
- rollback preview needs before/after comparison;
- imported memory provenance is sensitive;
- Dream artifact state must remain proposal-only;
- world/context orientation changes may affect continuity.

Snapshot link does not mean automatic rollback is allowed.

## Privacy And Redaction

Payload capture can increase privacy risk. Future policy must define:

- sensitive source handling;
- imported log redaction;
- user/session boundary;
- payload hashing;
- selective omission;
- audit-safe summaries;
- governance access level.

If privacy scope is unclear, full payload capture should be blocked.

## Forbidden Outcomes

P66 must not be interpreted as permission to:

- capture payloads;
- mutate event schemas;
- rewrite existing event records;
- compact events;
- delete or summarize event history;
- execute reconstruction reducers;
- rebuild object state;
- approve automatic rollback;
- mutate Identity Core;
- promote memory or growth.

## Relationship To P40

P40 created a review-only event payload capture policy proposal mechanism.

P66 is a foundation RFC that revisits the same problem after P65's reducer
contract boundary. It clarifies target-path policy vocabulary before future
implementation work.

Neither P40 nor P66 captures payloads.

## Relationship To P65

P65 says reducers require payload/diff preconditions. P66 says how target paths
may be classified for those preconditions.

Reducer contract still comes before reducer execution. Capture policy still
comes before payload capture.

## Non-Execution Flags

P66 artifacts must preserve:

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

These are policy boundary reminders, not runtime outputs.

## P67 Handoff

P67 should synthesize P54-P66 into a Foundation Roadmap, separating stable
foundation, future contracts, blocked runtime work, and low-risk consolidation.

Until then, payload/diff capture remains unimplemented.
