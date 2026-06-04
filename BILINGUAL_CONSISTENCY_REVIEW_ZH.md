# Bilingual Consistency Review / 双语一致性审查

English version: [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)

状态：`document-only`、`bilingual-consistency`、`non-runtime`。

P79 记录一次 foundation layer 的 bilingual consistency pass。它不新增 runtime behavior、
schemas、CLI commands、validators、policy executors、reducers、payload capture、
identity mutation、memory rewrite、adapters、UI、cloud rollout 或 product behavior。

## Review Rule / 审查规则

```text
bilingual documents are paired boundary surfaces.
translation may preserve technical terms.
translation must not soften blocked actions.
```

P79 存在的原因是：项目现在同时依赖中文优先的研究记录和英文技术边界语言。如果某一种语言漂移，
后续工作可能会把 future-only 或 review-only 文档误读成 implementation approval。

## Inspection Scope / 检查范围

本次检查覆盖：

- root Markdown documents 和 adapter README pairs；
- P54-P78 foundation consolidation artifacts；
- README、roadmap、checklist、RFC index、risk register、open questions、
  decisions、research notes index、glossary、phase index、concept map、
  architecture boundaries 等 foundation entrance documents；
- 当前 autonomous work summaries。

`RESEARCH_NOTES_ZH.md` 被有意保留为中文原始 source note。它不被视为缺少英文配对。

较早的 historical/runtime references 被作为既有 documentation pairs 检查，但不做机械式统一。
大规模改旧文件 header 会制造噪声，却不能明显改善当前 foundation boundary。

## Inspection Results / 检查结果

| Check | Result | Follow-up |
|---|---|---|
| Pair presence | 所有 Markdown documents 都有预期的中英文配对，除了有意 source-only 的 `RESEARCH_NOTES_ZH.md`。 | 后续 foundation work 默认 paired edits。 |
| Reciprocal links | P54-P78 foundation artifacts 和当前 entrance documents 保持 reciprocal links。 | 较早 historical/runtime references 只有在确实有用时再统一。 |
| Status labels | 当前 foundation artifacts 使用对齐的 `document-only` 和 `non-runtime` status language。 | 后续新增 review artifacts 时保持 status labels 一致。 |
| Non-execution statements | 当前 foundation docs 一致声明 review、RFC、checklist、roadmap、index 和 risk language 不执行 runtime behavior。 | 两种语言都要显式保留 non-execution statements。 |
| Blocked runtime terms | 核心 blocked topics 在 README、roadmap、RFC index、checklist、risk register 和 boundary docs 中保持可见。 | 任一语言弱化 blocked boundary 都视为 review failure。 |
| Phase and summary alignment | `AUTONOMOUS_WORK_SUMMARY.md` 记录 P54-P78，并会在 P79 commit 后更新。 | 每个 phase commit 后同步更新两份 summary。 |

## Checked Areas / 已检查区域

| Area | Main Documents | P79 Reading |
|---|---|---|
| Project entrance | [README.md](./README.md), [README_ZH.md](./README_ZH.md) | 两种语言都让新读者看见 stable/future/blocked status。 |
| Foundation route | [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md), [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | P68-P80 仍是低风险 consolidation，checklist 仍是 manual。 |
| Governance and risk | [RFC_INDEX.md](./RFC_INDEX.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md), [RISK_REGISTER.md](./RISK_REGISTER.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | Review surfaces 不是 implementation approvals。 |
| Traceability | [DECISIONS.md](./DECISIONS.md), [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) | Decision 和 source-note records 对 accepted、deferred、blocked、watch status 保持一致。 |
| Shared vocabulary | [GLOSSARY.md](./GLOSSARY.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md), [PHASE_INDEX.md](./PHASE_INDEX.md) | 核心 terms 在两种语言中保持 ownership boundaries。 |
| Work record | [AUTONOMOUS_WORK_SUMMARY.md](./AUTONOMOUS_WORK_SUMMARY.md) | Phase commits、verification 和 remaining work 应在每个 phase 后镜像更新。 |

## Future Paired-Edit Policy / 后续配对编辑策略

后续 foundation documents 应遵守：

- English 和 Chinese files 在同一个 phase 更新；
- status labels 保持一致；
- 如果翻译会模糊 concept boundary，中文中保留技术英文 term；
- 如果两个版本冲突，在修正前采用更严格的 boundary；
- 除非能降低 active risk，否则避免对较早 historical documents 做大规模机械编辑。

## Watch Items / 观察项

| Risk | Why It Matters | Control |
|---|---|---|
| Bilingual boundary drift | blocked action 可能在某一种语言里变得更软。 | commit 前比较 non-execution 和 blocked-runtime lists。 |
| Loose term translation | growth、drift、review、reconstruction 等概念可能被翻译得过宽。 | 保持 glossary 和 concept map terms 对齐。 |
| Summary drift | 某份 summary 可能漏掉 phase commit 或 verification result。 | phase artifact commit 后更新两份 autonomous summary。 |
| Legacy normalization churn | 改写旧 headers 可能掩盖真正有意义的 foundation changes。 | 只有收益明确时才统一旧文档。 |
| Index overload | 链接太多会降低入口可读性。 | 从最小且有用的入口集合链接新 artifact。 |

## P79 Non-Execution Statement / P79 非执行声明

P79 不实现：

- automated bilingual checking；
- runtime validation changes；
- policy execution；
- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或
  product layer。
