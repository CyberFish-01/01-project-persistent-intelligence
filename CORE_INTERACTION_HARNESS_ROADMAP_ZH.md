# Core Interaction Harness Roadmap / Core 交互试验台路线图

English version: [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md)

状态：`document-only`、`roadmap`、`non-runtime`。

P90 评估 foundation 是否已准备好在未来考虑 minimal local interaction harness。它不实现 harness、CLI
command、API route、adapter integration、UI、context builder、review queue、temporal runtime、
recall event write、trace storage、thought loop、growth lifecycle、identity mutation、memory
rewrite、cloud rollout、companion layer 或 product behavior。

## Roadmap Rule / 路线图规则

```text
roadmap is not implementation approval.
minimal harness means preview-only.
preview-only means no writes, no mutation, no lifecycle, no adapter ownership.
```

## Readiness Assessment / 就绪度评估

P82-P89 已经创建足够的文档级 contracts，可以在之后讨论 minimal harness：

- P82：temporal coherence evaluation scenarios；
- P83：review depth 和 deliberation tick vocabulary；
- P84：thought trace storage boundary；
- P85：thin harness boundary；
- P86：conversation intake envelope；
- P87：context package preview；
- P88：review queue preview；
- P89：session resume scenario plan。

这足够做 roadmap，但还不足以 implementation。项目仍缺 accepted schemas、validation contracts、storage
policy、privacy rules，以及 runtime work 的明确批准。

## Future Minimal Scope Candidate / 未来最小范围候选

如果之后明确批准 implementation phase，最小安全 local CLI harness 应该保持 preview-only 和
fixture-first。

候选未来 commands：

| Candidate Command | Future Purpose | Allowed Output | Explicitly Not |
|---|---|---|---|
| `harness-intake-preview` | 把 fixture 或 stdin input 规范化成 intake preview。 | envelope preview、privacy flags、boundary flags | adapter ingest、event write |
| `harness-context-preview` | 从 fixture state 解释 selected 和 omitted refs。 | selected refs、omitted refs、reasons、gaps | retrieval as continuity、activation trace write |
| `harness-review-preview` | 展示 candidate previews 和 ordering reasons。 | candidate type、risk、review depth、blocked reason | lifecycle execution、approval |
| `harness-resume-scenario` | 从 fixtures 运行 deterministic resume scenarios。 | expected refs、gaps、queue preview labels | Temporal Awareness runtime、temporal event write |
| `harness-boundary-check` | 为 fixture report blocked outputs。 | blocked flags 和 source artifact refs | runtime enforcement、policy executor |

P90 不批准任何 command。这些名字只是 roadmap placeholders。

## Required Implementation Gates / 必需实现门槛

任何未来 harness implementation 前，后续 phase 必须定义：

- exact fixture format；
- preview output 是 ephemeral 还是 report-only；
- privacy 和 redaction rules；
- local-only execution boundary；
- no-write validation invariants；
- forbidden-output tests；
- bilingual documentation updates；
- commit-by-phase verification；
- 明确声明 adapter/UI/cloud/product work 仍 out of scope。

## Proposed Future Harness Flow / 候选未来 Harness 流程

这是 roadmap sketch，不是 execution。

```text
fixture or stdin input
  -> intake preview
  -> context preview
  -> review queue preview
  -> optional resume scenario preview
  -> boundary check
  -> no state write
```

该 flow 必须能在不访问 live adapters、cloud services、UI surfaces 或 model-internal traces 的情况下运行。

## Non-Negotiable Boundaries / 不可谈判边界

未来 harness 不得：

- write events；
- write episodes；
- update adapter indexes；
- execute retrieval as continuity；
- persist activation traces；
- mutate context；
- write recall events；
- write temporal events；
- store hidden chain-of-thought；
- 在没有 future accepted policy 前 store thought traces；
- execute deliberation ticks 或 thought loops；
- execute growth lifecycle；
- approve candidates；
- mutate Identity Core；
- rewrite memory；
- 自动 revise claims；
- 自动 close tasks；
- execute policy；
- execute reconstruction reducers；
- compact events；
- call AstrBot、adapters、UI、cloud 或 product layers。

## Roadmap Phases After P90 / P90 后路线候选

仅作为 future directions：

1. `P91 Harness Fixture Contract RFC`
   定义 local fixture inputs 和 redaction rules。
2. `P92 Harness Output Contract RFC`
   定义 preview-only output sections 和 no-write invariants。
3. `P93 Harness Boundary Test Plan`
   在写代码前定义 deterministic forbidden-output tests。
4. `P94 Minimal CLI Harness Implementation`
   只有 P91-P93 后被明确批准才可进入。
5. `P95 Harness Completion Review`
   审计 runtime changes、no-write guarantees 和 blocked boundaries。

P90 不执行这些 phases。

## What Is Ready / 已就绪

- conceptual surfaces 已分离。
- Adapter ownership 被阻塞。
- Context preview 与 continuity 分离。
- Review queue preview 与 lifecycle 分离。
- Resume scenarios 与 Temporal Awareness runtime 分离。
- Thought trace storage boundaries 明确。
- Forbidden outputs 已列出且可搜索。

## What Is Not Ready / 尚未就绪

- 没有 fixture schema。
- 没有 output contract。
- 没有 harness-specific tests。
- 没有 privacy/redaction implementation plan。
- 没有 approved storage stance。
- 没有 CLI implementation approval。
- 没有 runtime boundary enforcement。
- 还不能保证 report output 可安全持久化。

## Risk Assessment / 风险评估

| Risk | Level | Mitigation Before Implementation |
|---|---|---|
| Harness becomes product | high | 保持 fixture-first、local-only、no UI |
| Preview becomes write path | high | no-write validation 和 forbidden-output tests |
| Context preview becomes retrieval continuity | high | mandatory continuity boundary note |
| Review queue becomes lifecycle | high | no approval or lifecycle commands |
| Resume scenarios become Temporal Awareness runtime | high | simulated elapsed time only |
| Trace preview captures hidden reasoning | high | enforce P84 storage boundary |
| Adapter sneaks in through source refs | high | no live adapter calls |
| Reports outnumber mechanisms | medium | code 前必须有 P91-P93 contracts |

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | 定义 P90 roadmaps 的 harness boundary。 |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | 定义 intake preview vocabulary。 |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | 定义 context preview vocabulary。 |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | 定义 review queue preview vocabulary。 |
| [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) | 定义 resume scenarios。 |
| [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | 提供任何 future phase 的 manual gate。 |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | 列出 P90 必须保持可见的 risks。 |

## Recommendation / 建议

暂时不要实现 harness。项目已准备好输出 transition summary；之后如果创始人明确想推进 minimal CLI harness，
可以进入 P91-P93 contracts。

最安全的下一个输出是 P82-P90 harness transition summary。

## P90 Non-Execution Statement / P90 非执行声明

P90 不实现：

- harness runtime；
- CLI command；
- API route；
- fixture schema；
- output schema；
- validation tests；
- context builder execution；
- retrieval execution；
- review queue execution；
- session resume runtime；
- Temporal Awareness runtime；
- temporal event writes；
- recall event writes；
- trace storage；
- hidden chain-of-thought capture；
- deliberation tick execution；
- thought loop execution；
- CTM runtime；
- model training；
- new dependencies；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- claim auto-revision；
- task auto-closure；
- policy execution；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
