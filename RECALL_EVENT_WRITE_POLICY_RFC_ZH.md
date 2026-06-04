# Recall Event Write Policy RFC v0.1 / 回忆事件写入策略 RFC v0.1

English version: [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md)

状态：`document-only`、`non-runtime`、`future-policy-rfc`。

P59 澄清 recalled memory 什么时候未来可能成为 event candidate。它不写 recall
events，不增加 event types，不修改 schemas，不增加 CLI commands，不 mutate memory，
不 promote growth candidates，不执行 reducers，也不实现 Temporal Awareness。

## Problem / 问题

P50 引入 stateful memory equation：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

它也命名了未来可能的 recall-as-event candidates，例如 `memory_recalled`、
`memory_reinterpreted`、`memory_reinforced`、`memory_weakened` 和
`memory_conflicted`，同时明确保持 `writes_recall_events: false`。

P58 又说明 Temporal Awareness 依赖未来的 recall event write policy。没有这个
policy，系统可能会误把 ordinary retrieval 当作 event，或者把“感觉意义变了”误当成
automatic growth。

## Core Rule / 核心规则

```text
ordinary retrieval is not an event.
ordinary recall is not a write.
meaning-shifting recall may become a future event candidate only after review.
```

Recall 可以影响 context。Recall 可以支持 review。Recall 可以暴露 possible meaning
shift。Recall 本身不能 rewrite memory、mutate identity、promote growth 或创建
durable events。

## Definitions / 定义

| Term | Meaning | Write Status |
|---|---|---|
| retrieval | 因相关性而取回 memory 或 context | never an event |
| ordinary recall | 使用已有 memory，但 meaning 没有变化 | no write |
| review-worthy recall | recall 暴露 changed meaning 的 evidence | future candidate only |
| meaning-shifting recall | recall reinforces、weakens、reinterprets 或 conflicts with prior meaning | future candidate only |
| identity-adjacent recall | recall 对 Identity Core continuity 形成压力 | high-gate review only |

这些定义只是 policy vocabulary，不是 active schema。

## Candidate Future Event Names / 候选未来事件名

下面这些名字仍然是 future-only：

- `memory_recalled`；
- `memory_reinterpreted`；
- `memory_reinforced`；
- `memory_weakened`；
- `memory_conflicted`。

P59 不创建这些 event types。未来 phase 必须先定义 schema、payload、validation、
replay meaning 和 review gates，才能存在任何 write path。

## Minimum Candidate Threshold / 最小候选门槛

一个 recall 只有同时具备以下信息时，未来才可以考虑成为 write candidate：

- source memory reference；
- source event reference when available；
- recall reason；
- active task 或 claim context，如果相关；
- explicit meaning shift category；
- evidence for the shift；
- uncertainty level；
- risk level；
- review gate；
- non-execution flag。

如果这些缺失，recall 应保持为 context-only 或 insufficient context。

## Meaning Shift Categories / Meaning Shift 分类

未来 recall candidates 可以使用 P50/P51 vocabulary：

- reinforced：后续 context 强化 prior meaning；
- weakened：后续 context 降低 confidence 或 salience；
- reinterpreted：后续 evidence 改变 interpretation，但不擦除 original record；
- conflicted：后续 evidence 产生 unresolved contradiction；
- identity-review-required：该 shift 可能影响 Identity Core，需要更高 gate。

这些分类都不意味着 automatic growth。

## Required Negative Cases / 必须排除的情况

下面这些情况不得创建 recall events：

- memory 只是为了填充 context 被 retrieved；
- memory 被 quote 或 summarize，但 meaning 没有变化；
- similarity search 导致的重复 retrieval；
- 模糊地感觉旧 memory 很重要；
- 用户要求 remember everything；
- adapter/platform 要求写入 memory；
- Dream artifact 未经 review 就提出 shift；
- temporal gap alone；
- relationship silence alone；
- 没有 evidence 的 tone change。

## Future Write Gate / 未来写入门槛

如果未来 implementation 被批准，recall event write 应要求：

1. reviewed candidate object；
2. explicit source memory and event references；
3. bounded meaning shift category；
4. evidence references；
5. replay/payload policy compatibility；
6. privacy and sensitivity scope；
7. identity-adjacent 时升级到 Identity Gate；
8. validation 证明没有 memory rewrite、identity mutation 或 growth promotion。

P59 不实现这个 gate。它只记录 gate requirement。

## Relationship To Temporal Awareness / 与 Temporal Awareness 的关系

Temporal Awareness 未来可能提供 elapsed-time evidence，例如
`elapsed_time_since_encoding` 或 `elapsed_time_since_last_recall`。这些 evidence
本身不能写 recall event。

Elapsed time 只有在绑定 source memory、recall reason、meaning shift 和 evidence 时，
才可能成为 review signal。Time alone is not evidence.

## Relationship To Growth Candidate Review / 与 Growth Candidate Review 的关系

Meaning-shifting recall 未来可能进入 growth candidate review object。这不意味着 recall
就是 growth。

Growth Candidate Review 仍然是 review-only。它未来可以 inspect recall candidate、
reject、defer，或 ask for evidence，但不能自动 promote memory 或 mutate Identity Core。

## Relationship To Event Sourcing / 与 Event Sourcing 的关系

Event Log 是 append-only audit trail。未来 recall event 必须能解释一个真正经过 review
批准的 state transition 或 review signal。它不能被用作第二个 memory store，也不能复制
每一次 retrieval。

在未来定义 payload/diff capture policy 和 replay interpretation 前，recall event writes
仍然 blocked。

## Safety Boundaries / 安全边界

- Retrieval is not continuity.
- Similarity search is not recall evidence.
- Recall evidence is not memory rewrite.
- Meaning shift is not growth.
- Growth candidate is not growth.
- Review object is not execution.
- Identity-adjacent recall 必须升级到 Identity Gate。
- Adapter、UI、AstrBot 和 platform inputs 不能强制 recall event writes。

## P60 Handoff / P60 交接

P60 应先定义 Stateful Memory Minimal Encoding Policy，然后项目才能可靠判断
meaning-shifting recall。

在此之前，recall event writes 仍然 forbidden。
