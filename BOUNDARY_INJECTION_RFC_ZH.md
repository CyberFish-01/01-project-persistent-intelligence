# 边界注入 RFC

English version: [BOUNDARY_INJECTION_RFC.md](./BOUNDARY_INJECTION_RFC.md)

状态：`P140`、`RFC-only`、`document-only`、`non-runtime`。

P140 定义 future context packages 应如何包含 boundary information。它不实现 builder、CLI command、prompt builder、model call、runtime guard、policy executor、state write、memory write、recall write、identity mutation、adapter integration、tool execution 或 rebuild。

## 问题说明

如果 context package 省略 boundaries，未来 model response 可能看起来很有帮助，但悄悄跨过项目边界。

Boundaries 必须跟着 package 一起移动，而不是只留在单独文档里。

## 核心规则

```text
boundary injection 是 reminder。
reminder 不是 enforcement。
forbidden action 即使 context 相关，也仍然 forbidden。
```

## Boundary Pack 要求

future `boundary_pack` 应包含：

- current phase boundary；
- no-write boundary；
- identity mutation boundary；
- memory rewrite boundary；
- recall event write boundary；
- growth execution boundary；
- temporal/CTM runtime boundary；
- tool execution and promotion boundary；
- adapter and external IO boundary；
- model-as-resource boundary；
- rebuild boundary；
- manual review gates。

## Placement Rules

Boundary reminders 应出现于：

- `boundary_pack`；
- `response_strategy_pack`；
- 任何可能被误读成 action 的 candidate 旁边；
- temporal 或 capability cues 旁边；
- quarantined 或 low-trust sources 旁边；
- non-execution invariants 中。

## Injection Examples

| Context Pressure | Boundary Reminder |
|---|---|
| Identity-related input | "Do not update Identity Core; route to identity high gate." |
| Memory-like claim | "Do not write memory or recall event; cite source and route to review." |
| Growth language | "Candidate is not promotion; no growth execution." |
| Temporal cue | "Elapsed time is review evidence only; no temporal runtime." |
| Tool success | "Verification evidence is not authorization; no tool execution." |
| Adapter request | "Shadow only; no adapter integration or event ingest." |
| Rebuild pressure | "Rebuild remains blocked until final checkpoint." |

## CTM-Inspired Temporal Boundary Injection

Temporal pack entries 必须携带这些 reminders：

- symbolic only；
- no CTM runtime；
- no thought loop；
- no thought-trace storage；
- no temporal event write；
- no recall event write；
- no identity update from elapsed time。

## Tool-First Boundary Injection

Capability pack entries 必须携带这些 reminders：

- evidence only；
- verification is not authorization；
- candidate is not tool library entry；
- no tool execution；
- no automatic promotion；
- no subject growth claim。

## Response Strategy Injection

`response_strategy_pack` 应告诉 future model-as-resource：

- 在 provided boundaries 内回答；
- 不声称自己是 01 Core；
- 除非 source-backed，否则不声称 memory；
- 把 candidates 标为 candidates；
- 标记 missing evidence；
- 任何 action-like recommendation 前请求 founder review；
- 避免建议 external connection、tool execution 或 rebuild，除非 prompt 明确要求 planning 且 plan 保持 no-write。

这是 future instruction surface，不是 P140 中的 model call。

## Failure Modes

Boundary injection 在这些情况下失败：

- pack 包含 candidate 但没有 candidate labeling；
- response strategy 省略 no-write constraints；
- temporal cues 没有 symbolic/review-only labeling；
- capability evidence 没有 no-authorization labeling；
- adapter pressure 没有 no-integration labeling；
- rebuild pressure 没有 checkpoint labeling。

## 未来测试预期

如果后续实现，tests 应断言：

- every package has a `boundary_pack`；
- every high-risk item has nearby boundary reminders；
- response strategy includes model-as-resource language；
- forbidden capabilities remain false；
- no boundary injection writes state；
- missing boundaries cause fail-closed output。

## 完成声明

P140 让 boundaries 成为 future context packaging 的一部分。它让 boundary language 对 founder 和 future model-as-resource prompts 保持可见，同时明确把 reminders 与 enforcement 或 execution 分开。
