# Exploration / Serendipity Engine RFC v0.1 / 探索与偶然性引擎 RFC v0.1

English version: [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md)

状态：`document-only`、`future-rfc`、`non-runtime`。

P63 定义未来 exploration 和 serendipity signals 的边界。它不实现 engine、scheduler、
agent behavior、UI、adapter integration、companion behavior、relationship memory、
automatic growth、memory rewrite、identity mutation、recall event write 或 policy executor。

## Purpose / 目的

一个 persistent intelligence 不应只保存已知状态。它也应该能注意到 unresolved
questions、adjacent possibilities、weak signals 和 unexpected connections。

危险在于 exploration 很容易变成 roleplay residue、ungrounded identity change、companion
behavior 或 productized engagement。P63 把 exploration 限定在 foundation layer 内，只能
生成 record-only 或 review-only signals。

## Core Rule / 核心规则

```text
exploration may generate questions.
exploration may generate weak signals.
exploration may request review.
exploration must not become growth by itself.
```

Exploration 只有在帮助系统 preserve continuity、surface uncertainty 或 find evidence 时才有
价值。当它 invents identity、simulates relationship depth 或 bypasses review gates 时，就是
不安全的。

## Non-Goals / 不做什么

P63 不实现：

- exploration runtime；
- serendipity scheduler；
- automatic topic generation；
- autonomous agent loops；
- companion behavior；
- relationship memory；
- UI、AstrBot、adapter 或 product behavior；
- recall event writes；
- temporal runtime；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- reconstruction reducer execution。

## Allowed Future Signal Types / 允许的未来信号类型

下面这些是 future review vocabulary，不是 active schema：

| Signal | Meaning | Allowed Output |
|---|---|---|
| `open_question_signal` | 值得保留的 unresolved question | review-only question |
| `adjacent_connection_signal` | memory、claim、task 或 event 之间的 possible connection | weak evidence note |
| `serendipity_prompt_signal` | 给 human 或 future review 的 optional prompt | non-executing suggestion |
| `exploration_drift_signal` | 带明确 non-commitment 的 speculative reinterpretation | record-only drift |
| `evidence_gap_signal` | claim 或 candidate 前进前缺失的 evidence | evidence request candidate |
| `boundary_risk_signal` | exploration 可能被 contamination 或 identity-adjacent | quarantine/review routing |

这些 signals 不改变 subject state。

## Input Sources / 输入来源

未来 exploration 可以 inspect，但不能 mutate：

- open questions；
- Dream artifacts；
- unresolved conflicts；
- weak reconstruction evidence；
- stale tasks；
- low-confidence claims；
- growth candidate rejection reasons；
- repeated insufficient-context outcomes；
- founder-marked research directions。

Input inspection 不是 output execution。

## Required Boundaries / 必须保留的边界

Exploration 必须保留：

- Identity Core gate；
- State Transfer over retrieval；
- append-only events；
- Dream proposes, review decides；
- Growth candidate is not growth；
- Review object is not execution；
- Temporal Awareness remains future direction；
- adapters and platforms do not own identity。

如果 exploration 触及 identity，必须 route to Identity Gate。如果触及 claims，必须 route
to Claim Graph。如果触及 work state，必须 route to Task Hub。如果跨多层，则属于
Governance Surface。

## Anti-Collapse Rules / 反崩塌规则

Exploration 必须 reject 或 quarantine：

- roleplay residue；
- unsupported personality invention；
- relationship escalation；
- prompt contamination；
- model tone drift；
- adapter-specific behavior；
- tool artifacts；
- invented life history；
- identity overwrite attempts；
- pressure to skip review because an idea feels meaningful。

Serendipity 不是 invent continuity 的许可。

## Review Outcomes / Review 输出

未来 exploration review 可以产生：

- `record_only_signal`；
- `review_question`；
- `evidence_request_candidate`；
- `task_review_candidate`；
- `claim_review_candidate`；
- `growth_candidate_input`；
- `boundary_risk_quarantine`；
- `reject_as_roleplay_residue`；
- `reject_as_insufficient_context`。

这些 outcomes 都不 execute growth、不 write events、不 mutate state。

## Relationship To Dream / 与 Dream 的关系

Dream 已经可以从 existing material 中提出 candidates。Exploration 未来可以帮助 Dream
注意 adjacent questions 或 evidence gaps。

Dream 仍然 proposes。Review 仍然 decides。Exploration 不得让 Dream 直接写 semantic memory
或 Identity Core。

## Relationship To Task Hub / 与 Task Hub 的关系

Task Hub 未来可以接收由 exploration signals 生成的 review tasks。这不意味着 Task Hub 拥有
exploration semantics。

Exploration 不应未经 review 自动创建 operational work。

## Relationship To Growth Semantics / 与 Growth Semantics 的关系

Exploration drift 默认不是 productive drift。

只有当未来 evidence 显示 bounded meaning shift、sufficient encoding/recall context 和
acceptable risk 时，它才可能成为 Growth Candidate Review 的输入。

## Relationship To Product Layer / 与产品层的关系

Exploration 不是 feature surface。P63 不定义 prompts、chat UX、recommendations、
notifications 或 engagement loops。

任何未来 product surface 都必须位于 foundation governance 下游，并且不能 own identity。

## Future Acceptance Gates / 未来接受门槛

进入实现前，未来 phase 必须定义：

- signal schema；
- input scope；
- review routing；
- evidence requirements；
- quarantine rules；
- validation invariants；
- evaluation cases，证明没有 companion behavior、identity mutation、memory rewrite、
  automatic growth 或 event write。

## P64 Handoff / P64 交接

P64 可以定义 Subject Kernel / World Seed boundaries。它应该澄清哪些 orientation 属于受保护
的 subject kernel，哪些属于更可演化的 world/context seed。

在此之前，exploration 仍然只是 document-only future research vocabulary。
