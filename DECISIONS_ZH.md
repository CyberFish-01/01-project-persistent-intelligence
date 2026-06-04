# Decisions Log / 决策日志

English version: [DECISIONS.md](./DECISIONS.md)

Status: `document-only`, `decisions-log`, `non-runtime`.

P77 记录 P0-P76 中已经稳定的 foundation decisions。它不新增 runtime behavior、
approval workflow、schemas、CLI commands、validators、policy executors、reducers、
payload capture、identity mutation、memory rewrite、adapters、UI、cloud rollout 或
product behavior。

## Decision Rule / 决策规则

```text
a decision log records project stance.
a decision log is not an approval engine.
blocked decisions remain blocked until an explicit future implementation phase.
```

使用本文档回答：项目已经决定了什么？证据在哪里？不能从该决定中推导出什么？

## Status Legend / 状态说明

- `accepted-foundation`：稳定 foundation stance。
- `accepted-boundary`：稳定 ownership 或 non-execution boundary。
- `deferred-contract`：有效的未来方向，但缺 contract/gate。
- `blocked-runtime`：当前 foundation loop 明确禁止实现。
- `watch`：重要风险或开放问题，需要保持可见。

## Stable Foundation Decisions / 稳定基础决策

| ID | Decision | Status | Evidence | Explicitly Not |
|---|---|---|---|---|
| D01 | Continuity 是穿过时间的 State Transfer，不只是 memory retrieval。 | `accepted-foundation` | [README.md](./README.md), [FOUNDATION.md](./FOUNDATION.md), [VISION.md](./VISION.md), [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) | retrieval-only continuity |
| D02 | 01 Core owns continuity state；models、platforms 和 adapters 不拥有 identity。 | `accepted-foundation` | [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md), [ADAPTER_PROTOCOL.md](./ADAPTER_PROTOCOL.md) | platform-owned identity |
| D03 | Identity Core 受 gate 保护，不能被自动 mutation。 | `accepted-boundary` | [FOUNDATION.md](./FOUNDATION.md), [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | direct identity rewrite |
| D04 | Event Log 是 append-only audit evidence。 | `accepted-boundary` | [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | event rewrite 或 compaction |
| D05 | Dream proposes；review decides。 | `accepted-foundation` | [DREAM_ENGINE_SPEC.md](./DREAM_ENGINE_SPEC.md), [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md) | direct semantic promotion |
| D06 | Review object is not execution。 | `accepted-boundary` | [RFC_INDEX.md](./RFC_INDEX.md), [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | policy executor 或 automatic rollout |
| D07 | Growth candidate is not growth。 | `accepted-boundary` | [CONCEPT_MAP.md](./CONCEPT_MAP.md), [GLOSSARY.md](./GLOSSARY.md), [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | memory promotion 或 growth engine |
| D08 | Reconstruction evidence is not reconstruction。 | `accepted-boundary` | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md), [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | reducer execution 或 state rebuild |
| D09 | Capture policy is not payload capture。 | `accepted-boundary` | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md), [RFC_INDEX.md](./RFC_INDEX.md) | event schema mutation |
| D10 | Foundation consolidation should reduce ambiguity before adding power。 | `accepted-foundation` | [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md), [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | empty phases 或 runtime expansion |

## Concept Ownership Decisions / 概念归属决策

| ID | Decision | Status | Evidence | Explicitly Not |
|---|---|---|---|---|
| D11 | Memory Layer owns memory records、provenance、lifecycle 和 retrieval eligibility。 | `accepted-boundary` | [CONCEPT_MAP.md](./CONCEPT_MAP.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md), [GLOSSARY.md](./GLOSSARY.md) | meaning-shift engine |
| D12 | Stateful Memory owns meaning-bearing memory semantics。 | `accepted-boundary` | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md), [GLOSSARY.md](./GLOSSARY.md) | new memory store |
| D13 | Claim Graph owns claim-shaped belief revision。 | `accepted-boundary` | [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | absorbing all meaning shift |
| D14 | Task Hub owns operational continuity，不拥有全部 governance。 | `accepted-boundary` | [CONCEPT_OVERLAP_REVIEW.md](./CONCEPT_OVERLAP_REVIEW.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | policy executor |
| D15 | Governance Surface owns cross-layer review objects。 | `accepted-boundary` | [CONCEPT_MAP.md](./CONCEPT_MAP.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | growth engine |
| D16 | Subject Kernel 和 World Seed 仍是 future boundary vocabulary。 | `deferred-contract` | [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | runtime split 或 identity rewrite |

## Deferred Future Directions / 后推未来方向

| ID | Direction | Status | Required Before Implementation | Explicitly Blocked Now |
|---|---|---|---|---|
| D17 | Temporal Awareness 作为 subject-state transition evidence。 | `deferred-contract`, `blocked-runtime` | recall write policy、temporal review placement、elapsed-time evidence rules、validation | Temporal Awareness runtime、temporal event execution |
| D18 | 面向 review-worthy recall 的 recall event writes。 | `deferred-contract`, `blocked-runtime` | accepted event schema、payload/diff policy、privacy、replay interpretation、validation | ordinary recall writes |
| D19 | Growth Candidate Lifecycle 作为 durable review-object history。 | `deferred-contract`, `blocked-runtime` | authority model、audit history、Identity Gate escalation、no-execution validation | growth lifecycle execution |
| D20 | Productive Drift vs Random Drift evaluation。 | `deferred-contract`, `watch` | evaluation cases、evidence thresholds、collapse recovery boundaries | automatic drift classifier |
| D21 | Exploration / Serendipity signal handling。 | `deferred-contract`, `watch` | signal schema、quarantine rules、anti-companion evaluation | exploration engine、companion behavior |
| D22 | Reconstruction Reducer implementation。 | `deferred-contract`, `blocked-runtime` | accepted reducer contract、deterministic validation、target-path capture policy | reducer execution、state rebuild |
| D23 | Payload / Diff capture。 | `deferred-contract`, `blocked-runtime` | privacy/redaction policy、schema compatibility plan、capture gates | payload capture、event schema mutation |
| D24 | Product、UI、AstrBot specialization 和 cloud rollout。 | `deferred-contract`, `blocked-runtime` | foundation loop 之后的 explicit product-layer phase | productization、adapter integration required |

## Rejected Or Blocked In Current Loop / 当前循环拒绝或阻塞

以下内容不是 P68-P80 中被接受的 decisions：

- identity mutation；
- memory rewrite；
- recall event write；
- growth lifecycle execution；
- Temporal Awareness runtime；
- temporal event execution；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- policy executor；
- companion、relationship memory、UI、AstrBot、adapter integration、cloud rollout
  或 product layer。

## Decision Review Checklist / 决策审查清单

新增或修改 decision 前：

1. 链接 evidence document。
2. 标记 status 为 accepted、deferred、blocked 或 watch。
3. 写清楚不能从该 decision 推导出什么。
4. 检查 [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md)。
5. 保持中文配对文档同步。
6. 使用 [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) 做 origin tracing，
   但不要把 origin notes 当作 implementation approval。

## P77 Non-Execution Statement / P77 非执行声明

P77 不实现：

- automated decision workflow；
- approval engine；
- policy executor；
- runtime validation changes；
- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
