# Growth Candidate Lifecycle RFC v0.1 / 成长候选生命周期 RFC v0.1

English version: [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md)

状态：`document-only`、`non-execution`、`future-lifecycle-rfc`。

P61 为 `growth_candidate_review` 定义未来 review-object lifecycle vocabulary。它不执行
lifecycle decisions，不 promote growth，不 rewrite memory，不 mutate identity，不写
recall events，不实现 policy executors，也不改变 runtime behavior。

## Problem / 问题

P51 定义 Growth Candidate Review：

```text
Growth candidate is not growth.
It is a review object for a possible meaning-bearing state transition.
```

P53/P57 留下一个开放问题：growth candidate reviews 未来是否应该支持 acknowledge、
archive、quarantine 或 defer decisions？

风险在于 lifecycle language 容易被误解为 promotion。P61 通过把 lifecycle 限定为
review-object housekeeping 来防止这个误解。

## Core Rule / 核心规则

```text
growth candidate lifecycle manages review object state.
growth candidate lifecycle does not manage subject state.
```

Lifecycle decision 可以整理、压制、保留或请求 candidate 的更多 evidence。它不能让
candidate 成真，不能 promote memory，不能 mutate Identity Core，不能 create growth，也不能
execute state transition。

## Lifecycle Vocabulary / 生命周期词汇

下面这些 labels 是未来 review-object states，不是当前 schema：

| State | Meaning | Explicit Non-Meaning |
|---|---|---|
| `open` | candidate 等待 review | not growth |
| `acknowledged` | reviewer 已看到 candidate，并认为值得 tracking | not accepted growth |
| `deferred` | review 等待更多 evidence 或更好的 contract | not rejection and not promotion |
| `archived` | candidate 保留用于 audit，但移出 active review | not memory archive |
| `quarantined` | candidate 因可能 contaminated 或 risky 被隔离 | not identity change |
| `rejected` | candidate 缺少 evidence 或违反 boundaries | not memory deletion |
| `evidence_requested` | candidate 需要特定 evidence 才能继续 review | not schema approval |

这些 labels 不能连接到 automatic actions。

## Allowed Lifecycle Effects / 允许的生命周期效果

未来 lifecycle system 可以被允许：

- record reviewer intent；
- route candidates out of active review；
- preserve audit history；
- request evidence；
- mark insufficient context；
- mark boundary risk；
- reduce review noise；
- explain why a candidate remains unresolved。

这些都只是 governance effects。

## Forbidden Lifecycle Effects / 禁止的生命周期效果

Lifecycle decision 不得：

- promote a growth candidate into growth；
- promote memory；
- rewrite memory；
- mutate Identity Core；
- write recall events；
- execute temporal events；
- revise Claim Graph automatically；
- close Task Hub work automatically；
- compact or rewrite events；
- execute a reconstruction reducer；
- create executable policy；
- trigger adapter、UI、AstrBot、companion 或 product behavior。

## Minimum Future Lifecycle Record / 最小未来生命周期记录

如果未来实现，lifecycle decision 应要求：

- `candidate_id`；
- `previous_review_state`；
- `next_review_state`；
- `decision_reason`；
- `evidence_refs`；
- `reviewer_ref` 或 review authority reference；
- `risk_level`；
- `boundary_flags`；
- `created_at`；
- `execution_prohibited`；
- `subject_state_unchanged`。

P61 不新增这个 schema。它只记录未来 phase 必须满足的 contract shape。

## Boundary Flags / 边界标记

Lifecycle decision 应显式保留 negative flags：

```yaml
promoted: false
memory_rewrite_executed: false
recall_event_written: false
identity_core_mutated: false
growth_engine_executed: false
policy_executor_created: false
subject_state_unchanged: true
```

这些 flags 是 RFC vocabulary。P61 不创建 runtime validation。

## Relationship To Growth / 与 Growth 的关系

Growth 仍然是单独的、更高 gate 的概念：

- evidence-backed；
- reviewed；
- meaning-bearing；
- state-transition relevant；
- not automatic。

Lifecycle 可以为未来 review 准备 candidate，但不能执行让 growth 成真的 state transition。

## Relationship To Memory Lifecycle / 与 Memory Lifecycle 的关系

Growth candidate lifecycle 不是 memory lifecycle。

Archiving a growth candidate review 不会 archive 它引用的 memory。Quarantining a growth
candidate review 不会 quarantine 它引用的 memory。Rejecting a candidate 不会 delete memory
或 erase evidence。

## Relationship To Claim Graph / 与 Claim Graph 的关系

只有 claim-shaped evidence 属于 Claim Graph。Lifecycle decisions 可以引用 related claims，
但不得自动 revise claims。

如果 candidate 因缺少 claim evidence 被 rejected，那是 governance decision，不是 claim
revision。

## Relationship To Identity Gate / 与 Identity Gate 的关系

Identity-adjacent candidates 需要 Identity Gate escalation。Lifecycle decision 可以标记
`identity_gate_required`，但不能执行 identity decision。

Identity Core remains protected by gate.

## Anti-Growth Rejection Reasons / Anti-Growth 拒绝理由

未来 lifecycle review 可以保留 P51 rejection reasons：

- single-turn style change；
- unsupported personality change；
- prompt contamination；
- adapter-specific behavior；
- isolated preference flip；
- model tone drift；
- tool artifact；
- roleplay residue；
- ungrounded identity statement；
- unsupported relationship escalation。

这些 reasons 支持 rejection 或 quarantine，不支持 automatic repair。

## P62 Handoff / P62 交接

P62 应定义 Productive Drift vs Collapse boundaries。它需要说明 evidence、risk 和 rejection
reasons 如何区分 bounded drift、random drift 或 identity-threatening collapse。

在此之前，lifecycle 仍然是 document-only review-object governance。
