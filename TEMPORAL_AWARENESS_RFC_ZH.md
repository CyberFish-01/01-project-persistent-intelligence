# Temporal Awareness RFC v0.1 / 时间感知 RFC v0.1

English version: [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md)

状态：`document-only`、`non-runtime`、`future-direction`。

P58 把 P51/P53 的 Temporal Awareness 开放问题整理成 RFC。它不新增 runtime
behavior、schema fields、event types、CLI commands、validation、evaluation、
reducers、adapters、UI 或 product behavior。

## Principle / 原则

```text
time is not only metadata.
time is part of subject state transition.
```

当前 foundation 已经记录 timestamp。Temporal Awareness 问的是另一个问题：
时间流逝如何改变一个主体可以如何记忆、重新解释、恢复任务、推迟判断，或者把某些状态视为 stale？

## Problem / 问题

P50 把 stateful memory 定义为：

```text
memory = event + encoding_state + recall_state + meaning_shift
```

如果 `recall_state` 只表示 recall 当下的即时上下文，这个模型仍不完整。同一段
memory 在五分钟、五天、五个月后被 recall，可能带来不同的 salience、不确定性、
情绪冷却、task staleness、relationship silence，或 unresolved conflict pressure。

开放问题不是如何存 timestamp。开放问题是 elapsed time 是否应该成为 meaning
shift review 的显式输入。

## Non-Goals / 不做什么

P58 不实现：

- temporal runtime；
- temporal event execution；
- recall event writes；
- memory salience mutation；
- memory rewrite；
- identity mutation；
- growth candidate lifecycle；
- reconstruction reducer execution；
- adapter、UI、AstrBot、companion 或 relationship feature behavior。

## Candidate Future Vocabulary / 候选未来词汇

下面这些名字只是 research vocabulary。它们不是当前 schema fields，也不能被当成
已经接受的 runtime payload。

| Candidate | Future Question |
|---|---|
| `elapsed_time_since_encoding` | memory 被 encoding 后过去了多久？ |
| `elapsed_time_since_last_recall` | memory 上一次 meaningfully recalled 后过去了多久？ |
| `last_recall_ref` | 如果要比较，应该锚定哪个 prior recall？ |
| `temporal_gap_type` | 这段间隔是普通时间流逝、long pause、interruption，还是 resumed session？ |
| `staleness_hint` | 时间流逝是否让 task、claim 或 plan 变得不可靠？ |
| `silence_interval` | relationship 或 collaboration context 中的长时间沉默是否重要？ |

在未来 phase 定义 write policy、review gates 和 audit requirements 前，这些候选词汇
必须留在 runtime 之外。

## Candidate Temporal Events / 候选时间事件

下面这些只是未来可能的 event candidates，不是当前 active event types：

- `long_pause`；
- `interruption`；
- `resumed_session`；
- `unresolved_conflict_aging`；
- `forgotten_but_resurfaced_memory`。

任何 temporal event 可以被写入之前，项目都需要先定义 recall event write policy 和
event payload/diff policy。否则 temporal events 可能变成未经 review 的 identity 或
memory mutation。

## Research Questions / 研究问题

1. elapsed time since encoding 应该如何影响 meaning shift？
2. elapsed time since last recall 应该如何影响 salience，同时不自动修改 salience？
3. resumed session 应该表示为 event、context annotation、review signal，还是不留下 durable record？
4. task staleness 什么时候重要到需要进入 Task Hub？
5. claim staleness 什么时候可以成为 Claim Graph review 的 evidence？
6. memory decay 能否在不 rewrite memory 的情况下表达？
7. relationship silence 能否在不实现 companion 或 social layer 的情况下表达？
8. 什么 evidence 可以区分 delayed realization 和 random drift？
9. 什么 evidence 可以区分 cooled-down reinterpretation 和 commitment loss？
10. unresolved conflict aging 应该如何生成 review material，而不是强制 growth？

## Meaning Shift Examples / Meaning Shift 示例

Temporal Awareness 未来可能帮助描述：

- delayed realization：旧事件在后续证据出现后获得新意义；
- cooled-down reinterpretation：强度下降，但证据仍保留；
- unresolved conflict aging：未解决的 contradiction 随时间变得更 salient；
- forgotten-but-resurfaced memory：很少被 recall 的 memory 重新变得相关；
- long-term consistency evidence：跨时间的稳定性支持 claim 或 identity-adjacent review。

这些都只是 review candidates。它们不意味着 automatic growth。

## Safety Boundaries / 安全边界

- Time alone is not evidence.
- Elapsed time alone 不能 mutate Identity Core。
- Elapsed time alone 不能 promote memory。
- Elapsed time alone 不能 create growth。
- Temporal signals 如果未来实现，也应该 request review，而不是 execute state transition。
- 在未来 accepted contract 出现前，Temporal Awareness 必须和普通 event metadata 保持分离。

## Relationship To Existing Concepts / 与现有概念的关系

Event metadata 可以记录 timestamps。Temporal Awareness 讨论这些 timestamps 未来是否能成为
subject-state evidence。

Stateful Memory 可以描述 encoding 和 recall context。Temporal Awareness 讨论 elapsed time
是否属于未来 recall-state review。

Claim Graph 可以 review stale 或 contradicted claims。Temporal Awareness 只有在出现
claim-shaped stale belief 时才应进入 Claim Graph，而不是只要时间流逝就进入。

Task Hub 可以 review stale tasks。Temporal Awareness 不应让 Task Hub 吞掉所有关于时间的
governance。

Growth Candidate Review 未来可以接收 temporal evidence。但它不能变成 growth engine。

## Future Acceptance Gates / 未来接受门槛

进入实现前，未来 phase 必须先定义：

- recall event write policy；
- minimum stateful memory encoding policy；
- temporal review object placement；
- payload/diff capture rules；
- validation invariants；
- 能证明没有 automatic mutation 的 evaluation cases。

## P59 Handoff / P59 交接

P59 应先澄清 Recall Event Write Policy，然后才能考虑任何 temporal event writes。

在此之前，Temporal Awareness 仍只是 RFC-level future direction。
