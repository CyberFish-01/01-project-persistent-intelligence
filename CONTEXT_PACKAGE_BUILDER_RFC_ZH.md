# 上下文包构建器 RFC

English version: [CONTEXT_PACKAGE_BUILDER_RFC.md](./CONTEXT_PACKAGE_BUILDER_RFC.md)

状态：`P137`、`RFC-only`、`document-only`、`non-runtime`。

P137 在任何 model call 前，定义 01 Core 未来 context package 的形状。它不实现 builder、CLI、retrieval engine、model call、prompt execution、state write、memory write、recall write、identity mutation、adapter integration、tool execution、policy executor 或 rebuild。

## 问题说明

01 Core 在安全地把模型当作资源使用之前，需要一个明确的 context package contract。

如果没有 contract，未来 orchestration 可能意外：

- 把 retrieval 当成 continuity；
- 省略 boundaries；
- 混合 trusted state 和 quarantined content；
- 让 model output 定义 identity；
- 过度使用 temporal 或 capability language；
- 让 response strategy 变得隐式且不可审查。

## 核心规则

```text
context package 是 preparation。
preparation 不是 model call。
selection 不是真相。
package output 不是 state mutation。
```

## 必需 Packs

每个 future context package preview 都应包含：

| Pack | Purpose | Must Preserve |
|---|---|---|
| `identity_pack` | Stable identity anchors 和 protected boundaries。 | Identity Core 不被修改。 |
| `state_pack` | Current local operational status 和 relevant static state。 | State reading 不是 state writing。 |
| `task_pack` | Active 或 relevant task context。 | Task preview 不是 task update。 |
| `claim_pack` | Relevant claims 和 evidence references。 | Claim selection 不是 claim truth。 |
| `memory_pack` | Relevant memory references 或 summaries。 | Memory retrieval 不是 continuity。 |
| `boundary_pack` | Forbidden actions 和 review gates。 | Boundary display 不是 enforcement。 |
| `temporal_pack` | Elapsed-time 和 review-depth cues。 | Temporal cues 是 symbolic，不是 runtime。 |
| `capability_pack` | Tool/procedure/capability candidates 和 evidence。 | Capability evidence 不是 authorization。 |
| `response_strategy_pack` | 模型作为资源时应如何回应。 | Strategy 不是 execution。 |

## Trust Levels

每个 pack 应把条目标为：

- `trusted_foundation`
- `source_backed`
- `review_only`
- `candidate_only`
- `quarantined`
- `omitted`
- `blocked`

任何 future context package 都不能默默把 lower-trust content 晋升成 trusted state。

## Source References

每个 selected item 都应包含：

- `source_id`
- `source_path`
- `source_class`
- `selection_reason`
- omitted 时的 `omission_reason`；
- `risk_flags`；
- 需要时的 `review_gate`。

## CTM-Inspired Temporal Pack

`temporal_pack` 可以包含：

- elapsed-time cue；
- interruption 或 session gap cue；
- unresolved tension note；
- delayed alignment candidate；
- review depth suggestion；
- thought-trace policy reminder。

它不能包含：

- CTM runtime；
- thought loop execution；
- hidden chain-of-thought；
- temporal event write；
- recall event write；
- identity update；
- memory salience mutation。

## Tool-First Capability Pack

`capability_pack` 可以包含：

- tool candidate；
- procedure candidate；
- verification evidence preview；
- cautionary procedural memory candidate；
- capability growth candidate review route。

它不能包含：

- tool execution；
- tool authorization；
- automatic tool promotion；
- dependency installation；
- policy executor；
- subject growth claim。

## Response Strategy Pack

`response_strategy_pack` 应告诉未来模型：

- 作为 resource 回答，而不是作为 subject；
- 保持 boundaries；
- 标记 uncertainty；
- 避免 identity claims；
- 除非 source-backed，否则避免声称 memory；
- 避免把 candidates 变成 decisions；
- 需要时请求 founder review。

这个 pack 只是 future instruction contract。它不调用模型。

## 未来 Builder 要求

如果后续批准 builder，它必须：

- 本地运行；
- deterministic；
- 只读取 approved local sources；
- 显示 selected 和 omitted sources；
- 包含所有 required packs；
- 包含 boundary invariants；
- 只生成 preview/report output；
- 证明 formal state 没有变化。

## 完成声明

P137 把 context package 定义为 structured、reviewable preparation layer。它是当前 source-backed previews 和未来 LLM-as-resource orchestration 之间的桥，同时保持 model calls 和 writes blocked。
