# Architecture Boundaries / 架构边界

English version: [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md)

状态：`document-only`、`boundary-refresh`、`non-runtime`。

P73 用 P58-P72 foundation artifacts 刷新 P53 architecture boundaries。它不新增 runtime
behavior、schemas、CLI commands、policy executors、reducers、payload capture、identity
mutation、memory rewrite、adapters、UI 或 product behavior。

## Boundary Rule / 边界规则

```text
ownership prevents concept collapse.
review surfaces are not execution paths.
future vocabulary is not runtime permission.
```

本文件应与 [CONCEPT_MAP.md](./CONCEPT_MAP.md)、[OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md)、
[RFC_INDEX.md](./RFC_INDEX.md) 和 [RISK_REGISTER.md](./RISK_REGISTER.md) 一起阅读。

## Boundary Matrix / 边界矩阵

| Boundary | Owner | Allowed | Forbidden |
|---|---|---|---|
| Identity Core | Identity Gate | high-gate review、evidence-backed identity memory append、audit metadata | direct rewrite、adapter-owned identity、Dream-driven mutation、growth-candidate-driven mutation |
| Subject Kernel | future Identity Seed boundary | protected minimal subject anchor vocabulary | runtime split、mutable personality layer、full biography |
| World Seed | future orientation boundary | project/world orientation vocabulary | protected identity、relationship persona、product positioning |
| Memory Layer | memory storage and lifecycle | records、provenance、sensitivity、retrieval eligibility、archive/quarantine | meaning-shift engine、new store for every semantic concept |
| Stateful Memory | interpretation model | encoding/recall/meaning-shift review vocabulary | memory store、memory rewrite、automatic salience mutation |
| Recall Event Write Policy | future write threshold | review-worthy recall vocabulary and negative cases | ordinary retrieval writes、recall event writes now |
| Claim Graph | claim-shaped belief revision | claims、support、contradiction、provenance、reviewed repair | absorbing every meaning shift |
| Task Hub | operational continuity | tasks、queues、procedural memory、warnings、review work items | owning every governance object 或 becoming a policy executor |
| Dream | offline proposal engine | candidates、conflicts、review material、provenance | direct semantic promotion、Identity Core mutation |
| Event Log | append-only transition audit | event envelope、sequence、transition reference、replay evidence | event rewrite、compaction、state clone、memory store |
| Replay | transition projection proof | projection、readiness report、rollback preview | full object reconstruction、reducer execution |
| Reconstruction Evidence | reconstruction readiness vocabulary | payload/diff gaps、evidence requests、coverage reports | reconstruction execution、state rebuild |
| Reconstruction Reducer Contract | future reducer contract | input envelope、target path identity、operation semantics vocabulary | reducer implementation 或 execution |
| Payload / Diff Capture Policy | future target-path evidence policy | reference/payload/diff/snapshot policy vocabulary | payload capture、event schema mutation |
| Growth Candidate Review | cross-layer review object | evidence review for possible meaning-bearing transition | growth、memory promotion、identity mutation |
| Growth Candidate Lifecycle | review-object housekeeping | open/deferred/archived/quarantined/rejected vocabulary | subject-state transition、growth lifecycle execution |
| Productive Drift vs Collapse | drift boundary vocabulary | evidence/risk/rejection categories | automatic classifier、automatic growth |
| Governance Surface | cross-layer review ownership | review objects spanning memory、claim、task、event、identity risk | policy executor、growth engine、all-purpose task hub |
| Temporal Awareness | future subjective-time semantics | elapsed-time research vocabulary and review questions | Temporal Awareness runtime、temporal event execution、salience mutation |
| Exploration / Serendipity | future weak signal boundary | record-only 或 review-only questions、evidence gaps、adjacent signals | companion behavior、product engagement、identity invention |
| RFC Index | document navigation | vocabulary ownership and blocked-action visibility | implementation approval |
| Risk Register | risk visibility | trigger signals and mitigation guidance | risk automation 或 policy execution |
| Product / Adapter Layer | pushed-back integration layer | future adapter translation and deployment notes | AstrBot specialization、UI、companion、product ownership of identity |

## Identity And Subject Boundaries / 身份与主体边界

Identity Core 仍是 protected continuity anchor。Subject Kernel 和 World Seed 未来可以帮助区分
subject identity 与 world orientation，但它们不创建 runtime mutation paths。

禁止：

- Identity Core rewrite；
- automatic identity mutation；
- Subject Kernel runtime split；
- World Seed becoming identity；
- adapter 或 platform identity ownership；
- product persona 或 relationship context becoming identity。

## Memory, Recall, And Meaning Boundaries / 记忆、回忆与意义边界

Memory Layer 存储 records。Stateful Memory 通过下式解释 memory：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

Recall Event Write Policy 仍是 future-only。Ordinary retrieval 不是 event。Missing encoding
context 产生 insufficient context，不通过 rewrite 修复。

禁止：

- memory rewrite；
- new memory store for each semantic concept；
- ordinary recall writes；
- salience mutation from elapsed time alone；
- imported memory becoming identity memory without review。

## Growth And Drift Boundaries / 成长与漂移边界

Growth Candidate Review 是 review object。Growth Candidate Lifecycle 是 review-object
housekeeping。Productive Drift 是待 review 的 evidence。三者都不执行 growth。

禁止：

- automatic growth；
- growth lifecycle execution；
- memory promotion from drift；
- identity mutation from growth candidates；
- treating collapse as growth。

## Reconstruction And Event Boundaries / 重建与事件边界

Event Log 保持 append-only audit evidence。Reconstruction Evidence、Reducer Contract 和
Payload / Diff Capture Policy 是有顺序的 review surfaces：

```text
Reconstruction Evidence -> Reducer Contract -> Capture Policy -> future implementation only if approved
```

这些都不执行 reconstruction，也不 capture payloads。

禁止：

- event rewrite 或 compaction；
- reconstruction reducer execution；
- object-level 或 full-state rebuild；
- payload capture；
- event schema mutation；
- rollback execution。

## Governance Boundaries / 治理边界

Governance Surface 负责那些无法干净放入 Memory Layer、Claim Graph、Task Hub、Event Log 或
Identity Gate 的 cross-layer review objects。它不能变成 all-purpose executor。

允许：

- review object routing；
- evidence requests；
- status visibility；
- manual review checklists。

禁止：

- policy executor；
- automatic growth engine；
- automatic task closure；
- automatic claim revision；
- runtime risk automation。

## Temporal And Exploration Boundaries / 时间与探索边界

Temporal Awareness 和 Exploration / Serendipity 仍是 future directions。Elapsed time 和 weak
signals 未来只有在 explicit contracts 存在后，才可能提供 review evidence。

禁止：

- Temporal Awareness runtime；
- temporal event execution；
- temporal salience mutation；
- exploration engine；
- companion 或 relationship behavior；
- roleplay residue becoming life history。

## Product, Adapter, And Deployment Boundaries / 产品、Adapter 与部署边界

Adapters translate platforms。01 Core owns state。Product 和 deployment work 在 foundation
loop 内继续后推。

P68-P80 consolidation 中禁止：

- AstrBot specialization；
- UI 或 product surface；
- companion/social layer；
- cloud rollout justified by foundation docs；
- adapter-required identity update。

## P73 Non-Execution Statement / P73 非执行声明

P73 只刷新 boundary documentation。它不实现：

- identity mutation；
- memory rewrite；
- recall event write；
- growth lifecycle；
- Temporal Awareness runtime；
- reconstruction reducer execution；
- payload capture；
- event schema mutation；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter 或 product layer。
