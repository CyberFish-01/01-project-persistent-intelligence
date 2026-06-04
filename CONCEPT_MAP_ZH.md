# Concept Map / 概念地图

English version: [CONCEPT_MAP.md](./CONCEPT_MAP.md)

P53 把 P0-P51 形成的地基概念收敛成一张图。这份地图只描述关系，不定义新的 runtime 行为。

## Core Flow / 核心流

```text
Identity Core
  protected by Identity Gate
  informed by Claim Graph, Identity Memory, and Growth Candidate Review
  never automatically mutated

State Transfer
  carried by StateStore, Context Builder, and Event Log
  stronger than memory retrieval

Event Log -> Replay -> Reconstruction Evidence
  Event Log records transitions
  Replay validates transition projection
  Reconstruction Evidence records what payload/diff/schema proof is missing

Memory Layer -> Stateful Memory -> Meaning Shift
  Memory Layer stores records and lifecycle status
  Stateful Memory interprets memory as event + encoding_state + recall_state + meaning_shift
  Meaning Shift is reviewable only when evidence-backed

Productive Drift -> Growth Candidate Review -> Governance Surface
  Productive Drift can create a review candidate
  Growth Candidate Review is not growth
  Governance Surface owns cross-layer review objects

Temporal Awareness
  future direction only
  time is not only metadata
  time is part of subject state transition
```

## Concept Roles / 概念角色

### Identity Core

受保护的 identity anchor。它应该小而稳定，并通过 high gate 保护。它可以被 reviewed evidence 影响，但不应被 Dream、adapter input、recall、growth candidate 或普通 memory update 直接改写。

### State Transfer

核心连续性机制。State transfer 表示下一次运行拿到 structured state package，而不是只检索相似文本。

### Claim Graph

evidence 和 belief-revision 层。它管理 claim、support、contradiction、provenance 和 reviewable repair。它不应吞掉所有 meaning shift；只有可表达为 claim 的 shift 才属于这里。

### Task Hub

操作连续性层。它跟踪 task、procedural memory、reflection、cautionary warning 和 review queue。它不应成为所有 governance object 的所有者。

### Dream

离线 consolidation engine。Dream 可以提出 semantic candidate、procedural candidate、conflict 和 review material。Dream 不直接 mutate Identity Core。

### Event Log

append-only audit ledger，记录 state transitions。它不是 state 的第二份副本，而是 replay 和未来 reconstruction 的基础。

### Replay

证明 event records 能解释 state transitions 的本地机制。当前 replay 支持 transition projection 和 readiness assessment，不支持 full object-level state rebuild。

### Reconstruction Evidence

未来 reconstruction readiness 的 evidence vocabulary 和 governance surface：payload coverage、object diff、rollback snapshot、seed/pre-event reference 和 evidence request。

### Stateful Memory

P50 引入的语义模型：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

它不是新的 memory store，而是一种解释同一段 memory 在不同 recall state 下为什么会产生不同意义的方式。

### Meaning Shift

encoding memory 和 recalled memory 之间的 interpretive delta。P51 要求 reinforced、weakened、reinterpreted、conflicted shift 必须有 evidence。没有 evidence 的 shift 是 random drift 或 insufficient context。

### Productive Drift

有边界、有 evidence 的 drift category，可能值得 review。Productive drift 不是自动正确，也不会自动成为 growth。

### Growth Candidate Review

用于审查 possible meaning-bearing state transition 的 review-only governance object。它引用 memory、claim、task 和 event evidence；它不 promote memory、不 rewrite identity、不 write recall events，也不执行 growth engine。

### Governance Surface

跨层 review surface，负责那些引用多个地基层、但不应完全放入 Memory Layer、Claim Graph、Task Hub 或 Identity Gate 的 review objects。

### Temporal Awareness

未来方向。它研究 elapsed time 如何影响 recall、salience、staleness、resumed session 和 meaning shift。P53 不实现它。
