# Visual Naming Guide

Chinese version: [VISUAL_NAMING_GUIDE_ZH.md](./VISUAL_NAMING_GUIDE_ZH.md)

Status: `P93`, `document-only`, `planning`, `non-runtime`.

P93 defines founder-facing vocabulary for future observatory, dashboard,
readiness, and concept-graph views. It does not implement those views. The goal
is to keep future visual surfaces readable to the founder while preserving the
English internal terms needed by papers, RFCs, code, and audits.

## Purpose

Future foundation views must feel like an instrument panel, not a paper table of
contents. The founder-facing layer should answer:

```text
What is this thing?
What is it for?
Is it implemented, report-only, RFC-only, future-only, or too early?
What risk does it carry?
What should happen next?
```

The English term remains the `internal_key`. The Chinese display name is the
primary label shown to the founder.

## Naming Principles

- Use the Chinese display name first in founder-facing views.
- Preserve the English name as the stable `internal_key`.
- Make every display name explain what the concept does, not only what it is.
- Avoid paper-like, overly abstract, or fashionable wording in visible titles.
- Prefer plain nouns such as `状态库`, `任务中心`, and `边界状态` over long theory labels.
- Do not show RFC-only concepts as implemented capabilities.
- Do not show a candidate as a promoted result.
- Do not show a review object as execution.
- When maturity is uncertain, display the lower-maturity status.
- Keep one bilingual mapping table; do not let dashboard language drift away
  from RFC, paper, or code language.

## Mapping Table

| internal_key | Chinese Display Name | What It Does | Visual Status | Boundary |
|---|---|---|---|---|
| Identity Core | 身份核心 | Protects the stable identity anchors that should not change casually. | 报告层 | Does not allow automatic identity mutation. |
| Identity Gate | 身份闸门 | Reviews high-risk identity pressure before any identity-facing change is considered. | 报告层 | Review gate, not identity update. |
| State Transfer | 状态传递 | Carries continuity by moving state through time instead of only retrieving memories. | 报告层 | Foundation proposition, not a standalone runtime feature. |
| StateStore | 状态库 | Stores durable local state such as state, episodes, dreams, and imports. | 已实现 | Storage is not identity ownership. |
| Event Log | 事件日志 | Records auditable transitions so later review can trace what happened. | 已实现 | Logging is not reconstruction execution. |
| Replay | 回放检查 | Checks whether state transitions can be replayed or projected for audit. | 报告层 | Replay check is not state rebuild. |
| Reconstruction | 状态重建 | Future ability to rebuild or explain subject history from evidence. | RFC 层 | Reducer execution remains blocked. |
| Claim Graph | 信念证据图 | Tracks claims, evidence, conflict, and belief status. | 报告层 | Does not absorb every meaning shift. |
| Task Hub | 任务中心 | Tracks durable tasks, procedures, and work state. | 报告层 | Does not replace governance review. |
| Dream Engine | 离线整理器 | Consolidates episodes and imported memory into semantic material. | 已实现 | Dream proposes; review decides. |
| Memory Lifecycle | 记忆生命周期 | Explains how memory may be staged, retained, consolidated, or forgotten. | 已实现 | Lifecycle status is not memory rewrite. |
| Stateful Memory | 状态化记忆 | Treats memory meaning as event plus encoding state, recall state, and meaning shift. | RFC 层 | Semantics, not a new memory store. |
| Meaning Shift | 意义变化 | Describes how a remembered item changes meaning under later recall state. | RFC 层 | Not claim revision by itself. |
| Growth Candidate Review | 成长候选审查 | Reviews possible meaning-bearing state transitions before any growth claim. | RFC 层 | Candidate is not promoted growth. |
| Governance Surface | 跨层审查区 | Holds review objects that reference memory, claims, tasks, identity, and evidence. | 报告层 | Review surface, not policy executor. |
| Temporal Awareness | 时间感知 | Studies elapsed time as part of subject-state transition. | RFC 层 | No temporal runtime or temporal event writes. |
| Temporal Coherence | 时间一致性 | Checks whether later interpretation still fits earlier state and evidence. | RFC 层 | Evaluation signal, not truth or identity update. |
| Deliberation Tick | 思考刻度 | Names possible future review steps for risk-calibrated deliberation. | RFC 层 | Not thought-loop execution. |
| Thought Trace | 思考痕迹 | Names a possible future review artifact summarizing review-state movement. | RFC 层 | Not hidden chain-of-thought or consciousness proof. |
| Capability Evolution | 能力进化 | Reviews durable improvement in tools, skills, and procedures. | RFC 层 | Capability improvement is not identity growth. |
| Tool-First Self-Evolution | 工具优先自进化 | Puts verifiable tool and procedure improvement before subject evolution. | RFC 层 | Does not approve tool execution or promotion. |
| Tool Candidate | 工具候选 | Proposes a possible tool for review. | RFC 层 | Candidate is not trusted tool. |
| Procedure Candidate | 流程候选 | Proposes a repeatable workflow for review. | RFC 层 | Candidate is not procedural memory. |
| Skill Memory | 技能记忆 | Future reviewed reusable capability knowledge. | 未来方向 | Not policy execution or automatic invocation. |
| Procedural Memory | 程序性记忆 | Durable knowledge about reviewed procedures and workflows. | 报告层 | Not an automatic tool runner. |
| Cautionary Memory | 警示记忆 | Preserves warnings from failures or unsafe patterns. | 报告层 | Warning is not enforcement code. |
| Thin Interaction Harness | 轻量交互试验台 | Future local preview surface for intake, context, review queue, and boundary flags. | RFC 层 | No harness runtime, CLI, UI, or adapter work. |
| Context Package Preview | 上下文包预览 | Explains which context references would be selected or omitted. | RFC 层 | Not retrieval execution or prompt construction. |
| Review Queue Preview | 审查队列预览 | Shows candidate review pressure, ordering signals, and blocked boundaries. | RFC 层 | Not queue execution or approval. |
| Session Resume Scenario | 会话恢复场景 | Simulates how paused sessions might recover references and context. | 报告层 | Not resume runtime or temporal event write. |
| Core Boundary Monitor | 核心边界监视器 | Future view explaining blocked, deferred, and review-needed actions. | 未来方向 | Not runtime enforcement. |
| Foundation Observatory | 地基观察台 | Future founder-facing view over foundation status, risks, concepts, and gaps. | 未来方向 | No dashboard runtime in P93. |
| Readiness Matrix | 就绪度矩阵 | Shows whether a concept is ready, blocked, or missing required gates. | 报告层 | Readiness is not authorization. |
| Risk Heatmap | 风险热力图 | Shows where concept, runtime, identity, memory, or tool risk is concentrated. | 未来方向 | Risk view is not governance execution. |
| Open Questions | 未决问题 | Lists unresolved foundation questions and their current routing. | 报告层 | Open question is not approval. |
| Boundary Status | 边界状态 | Shows whether a concept is allowed, blocked, RFC-only, or future-only. | 报告层 | Status label is not enforcement. |

## Display Card Format

Every future visual card should use this minimum shape:

| Field | Requirement |
|---|---|
| Chinese display name | The first visible title, written for the founder. |
| English internal_key | The stable term used by RFCs, papers, code, and audits. |
| One-sentence explanation | Plain answer to "what does this do?" |
| Current status | One of `已实现`, `报告层`, `RFC 层`, `未来方向`, `危险过早`. |
| Risk level | Low, medium, high, or blocked, with a short reason. |
| Next recommendation | The safest next action, usually review, document, defer, or block. |

Example card:

| Field | Example |
|---|---|
| Chinese display name | 成长候选审查 |
| English internal_key | Growth Candidate Review |
| One-sentence explanation | Reviews possible meaning-bearing state transitions before any growth claim. |
| Current status | RFC 层 |
| Risk level | High if treated as automatic growth. |
| Next recommendation | Keep review-only until promotion gates and evidence contracts exist. |

## Paper Naming Mode

English terms should remain available for:

- papers;
- RFCs;
- whitepapers;
- code identifiers;
- schemas;
- audits;
- cross-project comparison.

Chinese terms should be used first for:

- founder-facing dashboard summaries;
- future Foundation Observatory views;
- README summaries;
- readiness views;
- risk views;
- concept graph labels.

The two modes must stay mapped. A Chinese display name may be simpler than the
English term, but it must not change the concept boundary. An English
`internal_key` may be precise, but it must not force the founder-facing surface
to look like a research paper.

## Boundary Rules

P93 does not implement:

- Web UI;
- dashboard runtime;
- Foundation Observatory runtime;
- product layer;
- observability CLI;
- runtime changes;
- new features;
- Temporal Awareness runtime;
- CTM runtime;
- thought loop execution;
- tool execution;
- tool promotion;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- recall event writes;
- reconstruction reducer execution;
- companion, relationship, AstrBot, adapter, cloud, or product integration;
- P94.

## Non-Execution Statement

This guide is a naming contract for future visual surfaces. It is not a UI
specification, implementation plan, dashboard schema, CLI contract, runtime
report, status API, or approval to build the Foundation Observatory.
