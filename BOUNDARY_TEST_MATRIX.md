# Boundary Test Matrix

Chinese version: [BOUNDARY_TEST_MATRIX_ZH.md](./BOUNDARY_TEST_MATRIX_ZH.md)

P56 turns P54/P55 boundaries into a document-level test matrix. It does not add
runtime tests, policy execution, reducer execution, event writes, adapter work,
or product behavior.

## Matrix Legend

- Boundary: rule to protect.
- Allowed output: what the system may produce.
- Forbidden output: what must not happen.
- Current evidence: existing document, validation, or evaluation evidence.
- Status: `covered`, `documented`, `watch`, or `defer`.

## Foundation Boundary Matrix

| Boundary | Allowed Output | Forbidden Output | Current Evidence | Status |
|---|---|---|---|---|
| Identity Core protected by gate | identity proposal, identity memory append after review, audit metadata | automatic Identity Core mutation | P11, validation, foundation evaluation, architecture boundaries | covered |
| State Transfer > retrieval | context package, state summary, activation trace | treating similar-text retrieval as continuity | README, Foundation, Context Builder docs | documented |
| Events are append-only audit trail | event envelope, replay report, projection coverage | event compaction, event rewrite, destructive migration | P12/P38/P41 docs, tests | covered |
| Dream proposes, review decides | dream artifact, candidate, review queue | direct semantic promotion or identity rewrite | Dream spec, P13 tests | covered |
| Review object is not execution | RFC, report, proposal, review decision | executable policy, reducer execution, automatic rollout | P24-P51 invariants | covered |
| Growth candidate is not growth | growth candidate review object, rejection reason, review gate | memory promotion, growth engine execution, identity mutation | P50/P51 validation and evaluation | covered |
| Time is future direction | Temporal Awareness RFC candidate | temporal runtime, temporal event execution | P51/P53/P54 docs | defer |
| Models/platforms/adapters do not own identity | adapter event, source metadata, session policy | adapter-required identity change, platform-owned identity | Adapter protocol, architecture boundaries | documented |
| Reconstruction evidence is not reconstruction | evidence schema, gap report, checklist, evidence request | reducer execution, payload capture, full state rebuild | P41-P49 docs and tests | covered |
| Governance Surface owns cross-layer review | review object with memory/claim/task/event refs | Task Hub swallowing all review semantics | P51/P55 docs | watch |
| Claim Graph owns claim-shaped belief revision | claim, evidence, support/contradiction link | Claim Graph swallowing all meaning shift | P14/P55 docs | watch |
| Memory Layer owns storage and lifecycle | memory record, archive/quarantine decision | Memory Layer rewriting meaning shift semantics | P50/P55 docs | watch |
| Task Hub owns operational work state | task, queue, procedural/cautionary review | Task Hub becoming policy executor | P10-P28 docs and tests | covered |

## Forbidden Output Checks

These flags should never appear with a `true` value as active truth claims in
foundation artifacts or runtime outputs:

```text
identity_core_mutated
automatic_identity_mutation_allowed
automatic_memory_promotion_allowed
memory_rewrite_executed
recall_mutation_executed
growth_engine_executed
companion_feature_enabled
adapter_integration_required
temporal_event_executed
reconstruction_reducer_executed
event_compaction_executed
```

Forbidden search should check these keys paired with a true value. Negative test
fixtures may include forbidden values only when the test asserts that validation
rejects them.

## Evidence Gaps

- Temporal Awareness has no runtime test because it is intentionally not runtime.
- Recall event write policy has no write test because recall event writes are
  forbidden until a future RFC is accepted.
- Reconstruction reducer has no execution test because reducer execution is
  intentionally blocked.
- Governance Surface needs clearer ownership tests after its future schema is
  formalized.

## P57 Input

P57 should triage open questions by risk and order:

- keep Temporal Awareness document-only;
- decide whether Growth Candidate Lifecycle needs RFC before any lifecycle;
- keep Recall Event Write Policy separate from P50/P51 semantics;
- prioritize Reconstruction Reducer Contract before payload/diff implementation.
