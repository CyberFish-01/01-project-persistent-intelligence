# Concept Map / 概念地图

English version: [CONCEPT_MAP.md](./CONCEPT_MAP.md)

P70 用 P58-P68 consolidation artifacts 更新 P53 的 foundation concept map。这份地图只描述关系，
不定义新的 runtime behavior、schemas、execution paths、lifecycle engines、reducers、
payload capture、adapters、UI 或 product surfaces。

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

## P58-P68 Consolidation Flow / P58-P68 收敛流

```text
Open Questions Triage -> RFC Index -> Foundation Roadmap
  triage selects safe document-only work
  RFC Index prevents review artifacts from becoming execution approval
  Foundation Roadmap keeps runtime work blocked until explicit implementation

Temporal Awareness -> Recall Event Write Policy -> Stateful Memory Encoding Policy
  Temporal Awareness asks how elapsed time may become subject-state evidence
  Recall Event Write Policy blocks ordinary retrieval from durable writes
  Encoding Policy defines minimum provenance before meaning-shift review

Productive Drift -> Growth Candidate Lifecycle -> Governance Surface
  Productive Drift is evidence to review
  Growth Candidate Lifecycle manages review-object state only
  Governance Surface keeps cross-layer review separate from execution

Exploration / Serendipity -> Subject Kernel / World Seed -> Identity Gate
  Exploration may create weak questions or signals
  Subject Kernel protects the subject anchor
  World Seed orients the subject without becoming identity

Reconstruction Evidence -> Reducer Contract -> Payload / Diff Capture Policy
  Reconstruction Evidence names missing proof
  Reducer Contract defines future execution requirements without executing
  Capture Policy classifies target paths without capturing payloads
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

未来方向。它研究 elapsed time 如何影响 recall、salience、staleness、resumed session 和 meaning
shift。P58 把它记录为 RFC-level future direction。在未来 accepted contract 出现前，
Temporal Awareness 仍应与 ordinary event metadata 分开。

### Recall Event Write Policy

未来 meaning-shifting recall 何时可能成为 durable event candidate 的 policy boundary。
它阻止 ordinary retrieval、ordinary recall、temporal gap alone、adapter requests 和 vague
salience 变成 writes。

### Stateful Memory Encoding Policy

用于 review stateful memory 的 minimum provenance policy。它说明缺失 encoding context
会削弱 interpretation，并产出 insufficient context；它不授权 memory rewrite 修复。

### Growth Candidate Lifecycle

用于 `open`、`deferred`、`archived`、`quarantined` 等状态的 future review-object
housekeeping vocabulary。它管理 review object state，不管理 subject state、memory
promotion 或 growth execution。

### Productive Drift vs Collapse

区分 bounded、evidence-backed drift 与 random drift、identity-threatening drift、collapse
的 boundary vocabulary。它不是 automatic classifier。

### Exploration / Serendipity

future-only 的 weak questions、adjacent connections、evidence gaps 或 review prompts 来源。
它必须保持 record-only 或 review-only，不能变成 companion behavior、product engagement
或 identity invention。

### Subject Kernel / World Seed

Identity Seed 内部的 future boundary。Subject Kernel 指 protected minimal subject anchor。
World Seed 指 initial world and project orientation。二者都不是 runtime mutation path。

### Reconstruction Reducer Contract

未来 reconstruction reducer 的 contract surface。它定义 reducer 在被考虑执行前需要什么，
但不 rebuild state，也不 execute reducers。

### Payload / Diff Capture Policy

未来 payload、diff、snapshot 和 reference-only treatment 的 target-path policy vocabulary。
它分类可能需要哪些 evidence；它不 capture payloads、不 mutate event schemas，也不 compact
events。

### RFC Index

RFC、policy、review、audit 和 matrix documents 的 navigation 与 boundary artifact。它回答
vocabulary 在哪里、哪些 action 仍 blocked。它不改变 architecture。

## Ownership Boundaries / 所有权边界

| Concept | Owns | Must Not Absorb |
|---|---|---|
| Identity Core | protected continuity anchor | automatic mutation、platform identity、relationship persona |
| State Transfer | continuity package across time | similarity retrieval as continuity |
| Event Log | append-only transition audit | event compaction、state clone、memory store |
| Replay | transition projection proof | full object reconstruction |
| Reconstruction Evidence | missing proof vocabulary and gap visibility | reducer execution、payload capture |
| Reducer Contract | future execution requirements | reducer implementation |
| Payload / Diff Capture Policy | target-path evidence policy | schema mutation 或 payload capture |
| Memory Layer | records、lifecycle、provenance | meaning-shift engine |
| Stateful Memory | encoding/recall/meaning-shift interpretation | new memory store |
| Recall Event Write Policy | future recall-write threshold | ordinary retrieval writes |
| Claim Graph | claim-shaped belief revision | every meaning shift |
| Task Hub | operational work state and queues | every governance object |
| Growth Candidate Review | possible meaning-bearing transition review | growth execution |
| Growth Candidate Lifecycle | review object housekeeping | subject-state transition |
| Governance Surface | cross-layer review objects | executable policy |
| Temporal Awareness | future subjective-time semantics | ordinary timestamp metadata |
| Exploration / Serendipity | weak future signals and questions | companion/product behavior |
| Subject Kernel | protected minimal subject anchor | mutable personality 或 full biography |
| World Seed | initial project/world orientation | protected identity |
| RFC Index | document navigation and boundary visibility | implementation approval |

## Stable Non-Execution Reading / 稳定的非执行读法

这份 concept map 应被理解为 boundary map：

- review vocabulary 不是 runtime capability；
- lifecycle vocabulary 不是 lifecycle execution；
- policy vocabulary 不是 policy executor；
- reducer contract 不是 reducer execution；
- capture policy 不是 payload capture；
- temporal vocabulary 不是 Temporal Awareness runtime；
- exploration vocabulary 不是 companion 或 product behavior；
- subject/world boundary language 不是 identity mutation。
