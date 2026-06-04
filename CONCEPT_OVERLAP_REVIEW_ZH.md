# Concept Overlap Review / 概念重叠审查

English version: [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md)

P55 收敛 P54 标记出的 foundation concept overlap。它只做文档：不引入 runtime behavior、lifecycle execution、recall event write、reducer execution、adapter work 或 product surface。

## Review Method / 审查方法

每组重叠概念记录：

- owner：哪个概念拥有主要责任。
- references：哪些概念可作为 evidence 或 routing context 被引用。
- do not absorb：owner 不应吞掉什么。
- future work：之后是否需要 RFC 或 policy。

## Overlap Matrix / 重叠矩阵

| Pair | Primary Owner | Allowed References | Do Not Absorb | Resolution |
|---|---|---|---|---|
| Growth Candidate Review vs Claim Graph | Governance Surface | Claims、evidence refs、conflict ids | Claim Graph 不应拥有所有 meaning shift | Growth review 拥有 cross-layer candidate；Claim Graph 拥有 claim-shaped belief revision。 |
| Stateful Memory vs Memory Layer | Memory Layer 管存储；Stateful Memory 管语义 | Memory ids、lifecycle status、encoding refs | Memory Layer 不应变成 meaning-shift engine | Stateful Memory 保持 interpretive model，不成为 store。 |
| Governance Surface vs Task Hub | Task Hub 管 work queues；Governance Surface 管 cross-layer review objects | Task ids、review tasks、lifecycle records | Task Hub 不应拥有所有 review object | review work 可通过 Task Hub routing，但 cross-layer objects 留在 Governance Surface。 |
| Meaning Shift vs Claim Revision | Meaning Shift 管 memory interpretation；Claim Graph 管 claim revision | Claim ids、contradiction evidence | Claim Graph 不应把所有 recall changes 变成 claims | 只有 claim-shaped shifts 进入 Claim Graph。 |
| Temporal Awareness vs Event Metadata | Event metadata 管 timestamps；Temporal Awareness 管未来 subjective-time semantics | timestamps、elapsed-time candidates | Event Log 不应暗示 temporal subject state | Temporal Awareness 在 RFC 和 policy 前保持 future-only。 |
| Reconstruction Evidence vs Payload/Diff Capture Policy | Reconstruction Evidence 管 vocabulary；Capture Policy 管未来 target-path treatment | workflow ids、target paths、gaps | Evidence reports 不应 mutate event schema | reports 保持 read-only，直到 policy 和 reducer contract 被 review。 |

## Detailed Resolutions / 详细收敛

### Growth Candidate Review vs Claim Graph

Growth Candidate Review 存在的原因是：一个 possible meaning-bearing state transition 可能同时引用 memory、tasks、claims、events 和 identity risk。只有当 candidate 包含 explicit claims、contradictions、support links 或 belief revision pressure 时，Claim Graph 才参与。

Resolution：

- Growth Candidate Review 拥有 candidate review object。
- Claim Graph 拥有 claim evidence 和 claim revision。
- Identity Gate 拥有 identity-threatening final review。
- Task Hub 可以 route review work，但不拥有 candidate semantics。

### Stateful Memory vs Memory Layer

Memory Layer 拥有具体 records：imported、episodic、candidate、semantic、identity 和 archived memory。Stateful Memory 不是第七种 memory store，而是说明 memory meaning 取决于 event、encoding state、recall state 和 meaning shift 的模型。

Resolution：

- Memory Layer 拥有 storage 和 lifecycle。
- Stateful Memory 拥有 interpretation vocabulary。
- Meaning Shift 不 rewrite stored memory。
- 未来 minimal encoding policy 应定义 required references，而不是创建另一个 memory store。

### Governance Surface vs Task Hub

Task Hub 已经包含许多 review queues 和 decisions，因此它在 operational 上有用，但不应成为所有 cross-layer review object 的 conceptual owner。

Resolution：

- Task Hub 拥有 actionable work state。
- Governance Surface 拥有 cross-layer review semantics。
- Review objects 可以暴露 tasks，但不等于 tasks。
- P56 应把这条边界写成 matrix。

### Meaning Shift vs Claim Revision

Meaning Shift 比 Claim Revision 更宽。一个 memory 可以被 reinforced、weakened、reinterpreted 或 conflicted，但并不一定产生 formal claim。

Resolution：

- Meaning Shift 保持 memory-semantics vocabulary。
- 当 shift 改变 claim statement、confidence、support、contradiction 或 review status 时，才进入 Claim Revision。
- 没有 claim-shaped content 时，不强行塞进 Claim Graph。

### Temporal Awareness vs Event Metadata

Event metadata 记录时间。Temporal Awareness 研究 elapsed time 是否改变 subject state。它们相关，但不是同一个概念。

Resolution：

- Event metadata 拥有 timestamps 和 sequence。
- Temporal Awareness 保持为未来 subject-continuity RFC 方向。
- P58 可以定义 elapsed-time concepts，但不能实现 temporal runtime。

### Reconstruction Evidence vs Payload/Diff Capture Policy

Reconstruction Evidence 描述未来 reconstruction 需要什么 proof。Payload/Diff Capture Policy 决定未来 target path treatment。两者都不执行 reconstruction。

Resolution：

- Reconstruction Evidence 拥有 vocabulary 和 gap visibility。
- Capture Policy 拥有未来 target-path recommendation。
- Reducer Contract 拥有未来 execution interface。
- 任何 report 都不能暗示 event schema mutation 或 event compaction。

## Concepts To Merge Or Rename Later / 未来可合并或重命名概念

- 部分 reconstruction review reports 未来可归入单一 "Reconstruction Governance" index。
- 如果 Governance Surface 名字过宽，可以考虑改成 "Cross-Layer Review Surface"。
- Growth Candidate Review 和 Productive Drift 在 lifecycle RFC 出现前应保持分离。

## P56 Input / P56 输入

P56 应把这些边界转成 test matrix：

- forbidden owner；
- allowed reference；
- allowed output；
- forbidden output；
- validation 或 documentation evidence。
