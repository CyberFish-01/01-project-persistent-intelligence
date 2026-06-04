# Foundation Review Checklist / 基础层审查清单

English version: [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md)

Status: `document-only`, `manual-checklist`, `non-runtime`.

P76 把 P54-P75 的 foundation guardrails 转成 manual review checklist。它不新增
runtime behavior、schemas、CLI commands、validators、policy executors、reducers、
payload capture、identity mutation、memory rewrite、adapters、UI、cloud rollout 或
product behavior。

## Checklist Rule / 清单规则

```text
a checklist is a human review gate.
a checklist is not an executor.
passing review does not approve runtime work.
```

未来提交任何 foundation phase 前，尤其是 P76-P80 maintenance work 前，使用这个
checklist。若某项失败，应修改文档或后推 phase，而不是制造 implementation pressure。

## Review Inputs / 审查输入

review 前检查当前版本：

- [README.md](./README.md)
- [FOUNDATION.md](./FOUNDATION.md)
- [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md)
- [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md)
- [PHASE_INDEX.md](./PHASE_INDEX.md)
- [CONCEPT_MAP.md](./CONCEPT_MAP.md)
- [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md)
- [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md)
- [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md)
- [RFC_INDEX.md](./RFC_INDEX.md)
- [RISK_REGISTER.md](./RISK_REGISTER.md)
- [DECISIONS.md](./DECISIONS.md)
- [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md)
- [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)
- [GLOSSARY.md](./GLOSSARY.md)
- [AUTONOMOUS_WORK_SUMMARY.md](./AUTONOMOUS_WORK_SUMMARY.md)

审查 bilingual consistency 时，同时检查对应中文文档。

## Phase Scope Gate / 阶段范围 Gate

| Check | Pass Condition | Stop If |
|---|---|---|
| Phase 有真实理由 | phase 减少 ambiguity、改善 navigation、对齐术语，或记录风险。 | 它只是为了推进 phase number。 |
| Scope 是 document-only | 修改只限 Markdown foundation artifacts。 | 未明确授权就修改 runtime、schema、CLI、validator、test、adapter、UI 或 deployment files。 |
| 当前工作仍属于 foundation layer | 输出提升 foundation clarity。 | 输出开始 product、companion、AstrBot、cloud、adapter 或 UI work。 |
| 没有隐藏 implementation approval | Future work 被标注为 future、blocked、review-only 或 contract-needed。 | review document 读起来像 implementation 授权。 |
| Summary 可以更新 | `AUTONOMOUS_WORK_SUMMARY.md` 和 ZH 能记录 phase、verification 和 next safe direction。 | phase 无法在不夸大 completion 的情况下被总结。 |

## Foundation Invariant Gate / 基础不变量 Gate

| Invariant | Review Question | Required Evidence |
|---|---|---|
| Identity Core protected by gate | change 是否保持 high-gate identity ownership？ | 没有 identity rewrite、adapter-owned identity、Dream mutation 或 growth-candidate mutation language。 |
| State Transfer > retrieval | change 是否保持 continuity 强于 memory retrieval？ | 没有声称 similarity search、context fill 或 recall alone 等于 continuity。 |
| Events are append-only audit trail | change 是否保持 event append-only semantics？ | 没有 event rewrite、compaction、destructive migration 或 state clone path。 |
| Dream proposes, review decides | change 是否保持 Dream 只是 proposal material？ | 没有从 Dream output 直接 semantic promotion 或 identity update。 |
| Review object is not execution | 每个 review artifact 是否仍然 non-executing？ | 没有 policy executor、reducer execution、automatic rollout 或 automated risk action。 |
| Growth candidate is not growth | change 是否保持 candidates 与 growth 分离？ | 没有 memory promotion、identity mutation、lifecycle execution 或 growth engine。 |
| Time is future direction | Temporal Awareness 是否仍是 future-only？ | 没有 temporal runtime、temporal event execution、salience mutation 或 memory decay implementation。 |
| Models/platforms/adapters do not own identity | platform language 是否仍保持 translation 边界？ | 没有 AstrBot/platform/session metadata 暗示 identity ownership。 |

## Concept Ownership Gate / 概念归属 Gate

| Concept Area | Owner To Preserve | Failure Mode |
|---|---|---|
| Memory records | Memory Layer | Stateful Memory 变成 new store 或 rewrite records。 |
| Memory meaning | Stateful Memory | Meaning shift 被压扁成 storage/retrieval。 |
| Claim-shaped belief | Claim Graph | Claim Graph 吞掉所有 meaning shift。 |
| Operational continuity | Task Hub | Task Hub 变成 policy executor 或 all-purpose governance layer。 |
| Cross-layer review | Governance Surface | Governance Surface 变成 growth engine 或 runtime automation layer。 |
| Auditability | Event Log | Events 变成 mutable snapshots 或 payload stores。 |
| Reconstruction readiness | Reconstruction Evidence | Readiness reports 变成 reconstruction execution。 |
| Future reducers | Reconstruction Reducer Contract | Contract language 变成 reducer implementation。 |
| Future capture | Payload / Diff Capture Policy | Policy language 变成 payload capture 或 schema mutation。 |
| Future time semantics | Temporal Awareness | Elapsed time 在没有 accepted contract 时变成 runtime state mutation。 |

## RFC And Open Question Gate / RFC 与开放问题 Gate

| Check | Pass Condition | Stop If |
|---|---|---|
| RFC status 清楚 | RFC 被描述为 review surfaces 或 future contracts。 | RFC 被当成 implementation approval。 |
| Open questions 该开放时仍开放 | `OPEN_QUESTIONS.md` 仍显示 blocked/future/watch status。 | 因为有了文档，就把问题当成 closed。 |
| Runtime-blocked list 仍可见 | Blocked topics 在 README、roadmap、index 或 risk docs 中可见。 | Blocked topics 从入口文档消失。 |
| Dependency order 被保留 | Future implementation 等待 contract、validation、privacy 和 review gates。 | 暗示后续 runtime capability 可以跳过 prerequisites。 |

## Risk Gate / 风险 Gate

以 [RISK_REGISTER.md](./RISK_REGISTER.md) 为风险源。一个 phase 至少应降低一个风险，或避免提高所有 active risks。

| Risk Cluster | Review Question | Stop If |
|---|---|---|
| Concept inflation | change 是否尽量复用现有 concepts？ | 添加没有 ownership 或必要性的名字。 |
| Review over review | change 是澄清 review，而不是再加一层不透明 review 吗？ | 理解该 phase 需要另一个未定义 review object。 |
| Reports over mechanisms | report 是否指向 contracts 或 gaps？ | 仅凭 report 数量声称 readiness。 |
| Growth confusion | growth 是否仍是 reviewed 且 evidence-backed？ | Drift、lifecycle 或 meaning shift 变成 promotion。 |
| Temporal pressure | time 是否仍 future-only？ | Elapsed-time vocabulary 变成 runtime behavior。 |
| Recall write pressure | ordinary recall 是否仍不是 write？ | Retrieval 变成 durable event creation。 |
| Memory rewrite pressure | missing context 是否被视作 insufficient context？ | 文档建议通过 editing memory 修补历史。 |
| Reconstruction pressure | reconstruction readiness 是否仍区别于 reconstruction？ | 暗示 reducer、capture、rebuild 或 compaction。 |
| Identity/platform pressure | 01 Core 是否仍 owns state？ | Adapters、platforms 或 product surfaces owns identity。 |
| Companion/product pressure | social/product layers 是否仍 pushed back？ | Exploration、silence 或 relationship language 变成 companion behavior。 |
| Bilingual drift | EN/ZH docs 是否同意 status 和 forbidden actions？ | 某个语言版本弱化 blocked boundary。 |
| P80 pressure | phase 是否增加 clarity？ | phase 只是空编号。 |

## Bilingual Consistency Gate / 双语一致性 Gate

对每个被修改的 paired document：

- English 和 Chinese title 互相链接。
- Status labels 一致。
- Non-execution statements 一致。
- Runtime-blocked items 一致。
- Phase numbers 和 commit references 一致。
- 中文版本可以保留技术英文术语，但不能改变 boundary meaning。
- 使用 [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)
  作为最新 manual baseline，而不是 automated checker。

## Verification Gate / 验证 Gate

每个 phase commit 前执行：

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
import re, sys, urllib.parse
root = Path(".")
bad = []
for p in root.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text = p.read_text(encoding="utf-8")
    for m in re.finditer(r"!?\\[[^\\]]*\\]\\(([^)\\n]+)\\)", text):
        raw = m.group(1).strip()
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = raw.split()[0].strip("<>")
        if target.startswith("#"):
            continue
        target = urllib.parse.unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (p.parent / target).resolve()
        if not resolved.exists():
            bad.append(f"{p}:{m.start()}: {raw}")
if bad:
    print("Broken local markdown links:")
    print("\\n".join(bad))
    sys.exit(1)
print("Markdown local links OK")'
rg -n "$FORBIDDEN_ACTIVE_TRUE_PATTERN" .
env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest
```

Expected interpretation：

- `git diff --check` 不输出内容。
- Markdown link check 输出 `Markdown local links OK`。
- Forbidden pattern search 应使用当前 autonomous-goal active-true pattern
  set。在没有匹配时可能 exit `1`；这是安全结果。
- Unit tests pass。

## Commit Review Gate / 提交审查 Gate

commit 前确认：

- changed files 符合 phase scope；
- 没有 revert unrelated user 或 generated changes；
- 新文档已经从 README 或合适 index 链接；
- `AUTONOMOUS_WORK_SUMMARY.md` / ZH 会在单独 summary commit 中更新；
- completion review 可以真实地说没有 runtime change。

## Review Outcomes / 审查结果

human review notes 中使用这些结果：

| Outcome | Meaning | Allowed Next Step |
|---|---|---|
| `pass-document-only` | phase 是安全的 foundation consolidation。 | Commit 并更新 summary。 |
| `revise-docs` | phase 有价值，但 wording、links 或 bilingual mismatch 不清楚。 | 修改 docs 并重跑 verification。 |
| `defer` | topic 有效，但现在不值得做。 | 记录为 future direction 或保持未实现。 |
| `block-runtime` | phase 正在推动 forbidden implementation。 | 停止并回到 roadmap/risk review。 |

## P76 Non-Execution Statement / P76 非执行声明

P76 不实现：

- automated checklist execution；
- policy execution；
- runtime validation changes；
- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- companion、relationship memory、UI、AstrBot、adapter、cloud rollout 或 product layer。
