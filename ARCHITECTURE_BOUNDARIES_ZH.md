# Architecture Boundaries / 架构边界

English version: [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md)

P53 记录 P51 之后的架构边界。这些边界用于避免概念互相吞并，以及过早进入产品层。

## Identity Core Boundary / 身份核心边界

Identity Core 不应被自动 mutation。

允许：

- high-gate review；
- evidence-backed identity memory append；
- explicit audit 和 rollback metadata。

除非未来 phase 明确改变，否则禁止：

- direct Identity Core rewrite；
- adapter-driven identity change；
- Dream-driven identity mutation；
- growth-candidate-driven identity mutation。

## Memory Layer Boundary / 记忆层边界

Memory Layer 不应吞掉 Stateful Memory semantics。

Memory Layer 负责 records、provenance、lifecycle、sensitivity 和 retrieval eligibility。Stateful Memory 是 semantic interpretation model：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

不要把每个 semantic concept 都变成 memory store。

## Claim Graph Boundary / Claim Graph 边界

Claim Graph 不应吞掉所有 meaning shift。

Claim Graph 负责 claim-shaped evidence、contradiction、support 和 revision。只有当 meaning shift 生成或修改 explicit claim 时，才进入 Claim Graph。

## Task Hub Boundary / Task Hub 边界

Task Hub 不应吞掉所有 governance review。

Task Hub 负责 operational continuity：tasks、procedural memory、reflections、warnings、queues 和 reviewed work records。引用多个层的 cross-layer review object 应放入 Governance Surface。

## Governance Surface Boundary / 治理表层边界

Governance Surface 管跨层 review objects。

例子：

- growth candidate review；
- reconstruction schema review material；
- evidence request governance；
- review-only policy proposal objects。

Governance Surface 不应变成 policy executor 或 growth engine。

## Temporal Awareness Boundary / 时间感知边界

Temporal Awareness 仍是 future direction。

原则：

```text
time is not only metadata.
time is part of subject state transition.
```

P53 不实现 elapsed-time runtime、temporal events、temporal salience 或 temporal growth candidates。

## Product Boundary / 产品边界

Companion、relationship memory、social layer、UI、AstrBot specialization 和 adapter expansion 继续后推。

当前项目中心仍是 foundation continuity：

- identity protection；
- state transfer；
- audit/replay；
- reconstruction readiness；
- review-only growth semantics。
