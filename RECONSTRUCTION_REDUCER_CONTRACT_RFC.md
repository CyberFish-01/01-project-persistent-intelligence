# Reconstruction Reducer Contract RFC v0.1

Chinese version: [RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md)

Status: `document-only`, `contract-rfc`, `non-runtime`.

P65 defines the minimum future contract a reconstruction reducer would need
before any object-level or full-state reconstruction can be considered. It does
not implement reducers, execute reconstruction, rebuild state, capture payloads,
mutate event schemas, rewrite events, compact events, roll back state, or mutate
identity.

## Problem

P41 established that current events are useful for deterministic replay and
transition projection, but not yet ready for object-level or full-state
reconstruction.

P42-P49 then created reconstruction evidence vocabulary, coverage mapping,
prioritization, checklist review, evidence request tracking, and evidence
request lifecycle decisions. These are still governance artifacts. They do not
define the execution contract for a reducer.

P65 defines that future contract boundary.

## Core Rule

```text
reducer contract is not reducer execution.
reconstruction evidence is not reconstruction.
payload policy is not payload capture.
```

Reducer execution remains forbidden until a later phase defines and validates a
runtime implementation.

## Required Contract Sections

A future reducer contract must define:

| Section | Required Question |
|---|---|
| input envelope | What event/evidence object can a reducer consume? |
| target path identity | Which state path is being reconstructed? |
| operation semantics | What transition operation is represented? |
| payload/diff preconditions | Which payload, diff, snapshot, or reference evidence is required? |
| protected path gates | Which target paths require Identity Gate or governance review? |
| deterministic output | What exact output must the reducer produce? |
| validation metadata | How is output checked without trusting the reducer blindly? |
| audit trail | How is reducer reasoning inspectable? |
| failure mode | What happens when evidence is missing or ambiguous? |
| non-execution flags | How does the contract prove P65 did not execute anything? |

P65 records these sections only as future contract requirements.

## Candidate Future Input Envelope

The future reducer input should be explicit and bounded:

- `event_id`;
- `sequence`;
- `timestamp`;
- `operation_class`;
- `target_path`;
- `target_identity`;
- `source_update_id`;
- `transition_reference`;
- `before_ref`;
- `after_ref`;
- `object_payload_ref`;
- `object_diff_ref`;
- `rollback_snapshot_ref`;
- `seed_state_ref`;
- `validation_context_ref`;
- `policy_decision_refs`.

These names are RFC vocabulary, not current schema.

## Target Path Identity

Reducer contracts must distinguish target path classes:

- protected subject paths;
- Identity Core or identity-adjacent paths;
- world/context orientation paths;
- memory records;
- claim graph records;
- task hub records;
- event/audit records;
- derived reports.

Protected identity paths require higher gates. Event/audit paths must never be
rewritten by reconstruction.

## Operation Semantics

A future reducer contract must define operation classes before execution:

- append record;
- update review status;
- lifecycle decision;
- archive or suppress from active context;
- add evidence link;
- create report-only artifact;
- preview rollback impact;
- derived projection.

The contract must also define forbidden operations:

- direct Identity Core rewrite;
- memory rewrite;
- event rewrite;
- event compaction;
- policy execution;
- automatic rollback;
- automatic growth;
- platform-owned identity update.

## Payload / Diff Preconditions

Reducer execution cannot be considered unless the relevant target path has an
accepted payload/diff policy.

Possible future precondition types:

- reference-only is sufficient;
- payload hint required;
- full object payload required;
- object diff required;
- snapshot link required;
- seed/pre-event state required;
- rollback snapshot required;
- payload hash required.

P65 does not choose these policies. P66 may define the target-path capture
policy.

## Protected Path Gates

Reducers must not treat all target paths equally.

Future contracts must require high-gate review for:

- Identity Core;
- Subject Kernel;
- identity-adjacent memory;
- continuity anchors;
- world/context orientation when it could become identity;
- privacy-sensitive imported memory.

If the gate is missing, the reducer outcome must be blocked, not guessed.

## Determinism Requirements

A reducer contract must define:

- stable input ordering;
- deterministic operation semantics;
- canonical target path identity;
- explicit missing-evidence behavior;
- reproducible output representation;
- versioned reducer contract id;
- hashable input and output references.

If two runs with the same evidence produce different outputs, the reducer
contract is not acceptable.

## Failure Modes

Missing evidence must produce reviewable failure, not reconstruction:

- `missing_payload`;
- `missing_diff`;
- `missing_snapshot`;
- `ambiguous_target_path`;
- `protected_gate_missing`;
- `schema_contract_missing`;
- `event_sequence_gap`;
- `source_update_missing`;
- `identity_path_blocked`;
- `insufficient_context`.

Failure is evidence for future governance. It is not permission to infer state.

## Validation Metadata

Future reducer output must carry validation metadata:

- reducer contract id;
- input evidence refs;
- target path class;
- operation class;
- precondition status;
- gate status;
- output hash;
- validation result;
- rejected assumptions;
- state mutation flag;
- reconstruction execution flag.

P65 does not create validation code.

## Non-Execution Flags

P65 artifacts must preserve:

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

These flags are RFC vocabulary and boundary reminders. They are not runtime
outputs in P65.

## Relationship To Replay

Replay currently validates transition projection and audit references.

A reconstruction reducer would be stricter. It would need enough payload/diff
evidence to rebuild object state, not merely prove that a transition happened.

P65 does not change replay.

## Relationship To Payload / Diff Capture Policy

P65 defines what a reducer contract would need. P66 should define which target
paths need full payload, object diff, snapshot link, or reference-only treatment.

Reducer contract comes before reducer execution. Capture policy comes before
payload capture.

## P66 Handoff

P66 should define Payload / Diff Capture Policy RFC by target path.

Until then, reconstruction reducer execution remains blocked.
