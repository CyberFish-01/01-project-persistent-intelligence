# Boundary Test Matrix / 边界测试矩阵

English version: [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md)

P56 把 P54/P55 的边界转成 document-level test matrix。它不新增 runtime tests、policy execution、reducer execution、event writes、adapter work 或 product behavior。

## Matrix Legend / 矩阵说明

- Boundary：需要保护的规则。
- Allowed output：系统可以输出什么。
- Forbidden output：必须禁止什么。
- Current evidence：当前已有的文档、validation 或 evaluation 证据。
- Status：`covered`、`documented`、`watch` 或 `defer`。

## Foundation Boundary Matrix / 基础层边界矩阵

| Boundary | Allowed Output | Forbidden Output | Current Evidence | Status |
|---|---|---|---|---|
| Identity Core protected by gate | identity proposal、review 后 append identity memory、audit metadata | automatic Identity Core mutation | P11、validation、foundation evaluation、architecture boundaries | covered |
| State Transfer > retrieval | context package、state summary、activation trace | 把 similar-text retrieval 当作 continuity | README、Foundation、Context Builder docs | documented |
| Events are append-only audit trail | event envelope、replay report、projection coverage | event compaction、event rewrite、destructive migration | P12/P38/P41 docs、tests | covered |
| Dream proposes, review decides | dream artifact、candidate、review queue | direct semantic promotion 或 identity rewrite | Dream spec、P13 tests | covered |
| Review object is not execution | RFC、report、proposal、review decision | executable policy、reducer execution、automatic rollout | P24-P51 invariants | covered |
| Growth candidate is not growth | growth candidate review object、rejection reason、review gate | memory promotion、growth engine execution、identity mutation | P50/P51 validation and evaluation | covered |
| Time is future direction | Temporal Awareness RFC candidate | temporal runtime、temporal event execution | P51/P53/P54 docs | defer |
| Models/platforms/adapters do not own identity | adapter event、source metadata、session policy | adapter-required identity change、platform-owned identity | Adapter protocol、architecture boundaries | documented |
| Reconstruction evidence is not reconstruction | evidence schema、gap report、checklist、evidence request | reducer execution、payload capture、full state rebuild | P41-P49 docs and tests | covered |
| Governance Surface owns cross-layer review | review object with memory/claim/task/event refs | Task Hub swallowing all review semantics | P51/P55 docs | watch |
| Claim Graph owns claim-shaped belief revision | claim、evidence、support/contradiction link | Claim Graph swallowing all meaning shift | P14/P55 docs | watch |
| Memory Layer owns storage and lifecycle | memory record、archive/quarantine decision | Memory Layer rewriting meaning shift semantics | P50/P55 docs | watch |
| Task Hub owns operational work state | task、queue、procedural/cautionary review | Task Hub becoming policy executor | P10-P28 docs and tests | covered |

## Forbidden Output Checks / 禁止输出检查

这些 flags 不应以 `true` value 作为 active truth claims 出现在 foundation artifacts 或 runtime outputs 中：

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

Forbidden search 应检查这些 keys 是否和 true value 成对出现。Negative test fixtures 只有在测试断言 validation 会拒绝它们时，才可以包含 forbidden values。

## Evidence Gaps / 证据缺口

- Temporal Awareness 没有 runtime test，因为它被有意保持为非 runtime。
- Recall event write policy 没有 write test，因为 recall event writes 在未来 RFC 被接受前仍被禁止。
- Reconstruction reducer 没有 execution test，因为 reducer execution 被有意阻断。
- Governance Surface 在未来 schema formalized 后，需要更清晰的 ownership tests。

## P57 Input / P57 输入

P57 应按 risk 和 order triage open questions：

- Temporal Awareness 保持 document-only；
- 判断 Growth Candidate Lifecycle 是否需要先 RFC，再 lifecycle；
- Recall Event Write Policy 继续和 P50/P51 semantics 分离；
- payload/diff implementation 之前，优先澄清 Reconstruction Reducer Contract。
