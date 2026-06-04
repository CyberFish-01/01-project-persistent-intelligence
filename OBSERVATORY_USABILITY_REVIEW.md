# Observatory Usability Review

Chinese version: [OBSERVATORY_USABILITY_REVIEW_ZH.md](./OBSERVATORY_USABILITY_REVIEW_ZH.md)

Status: `review-only`, `document-only`, `non-runtime`.

P97 reviews whether the P96 `foundation-observatory-report` command is actually
readable for the project founder. It does not change runtime behavior, Identity
Core, memory, recall policy, harness implementation, UI, AstrBot, adapters, or
next-step execution.

## Commands Reviewed

The review ran:

- `python3 -m one_core.cli foundation-observatory-report`
- `python3 -m one_core.cli foundation-observatory-report --lang zh`
- `python3 -m one_core.cli foundation-observatory-report --format json`
- `python3 -m one_core.cli foundation-observatory-report --format json --lang zh`
- `python3 -m one_core.cli --state-dir /tmp/.../state foundation-observatory-report --output /tmp/.../report.md`

The temporary `--output` check succeeded and did not create the temporary state
directory.

## Readability Score

Overall founder-facing readability: **7 / 10**.

| Area | Score | Reason |
|---|---:|---|
| Snapshot | 8 | Quickly says 01 Core is a continuity foundation, not a product or executor. |
| Main axes map | 7 | Useful grouping, but several axes still rely on abstract English internal keys. |
| Readiness matrix | 7 | Status is visible, but labels such as `rfc_only` and `report_only` need founder-facing Chinese meanings. |
| Boundary status | 8 | Forbidden and disabled boundaries are visible through `enabled: false`. |
| Risk heatmap | 5 | It names risks, but many mitigations are too generic to guide action. |
| Next-step recommendations | 7 | Conservative and non-automatic, but should separate "review next" from "build next" more strongly. |

## What Works

- The report makes it clear that P96 is read-only and does not mutate state.
- `implemented`, `rfc_only`, `evaluation_only`, `future_direction`, and
  `blocked` are visible enough for a technical reader.
- The boundary table is the strongest section: forbidden work is easy to scan,
  especially identity mutation, memory rewrite, growth engine, temporal
  runtime, tool execution, policy executor, and event compaction.
- The Chinese report now uses Chinese display names for the most important
  concepts while preserving English `internal_key` values.
- JSON output is structurally useful for future static reporting, but it should
  remain a report artifact, not an execution contract.

## Still Too Abstract

- The report still assumes the founder understands terms such as `rfc_only`,
  `report_only`, `evaluation_only`, `symbolic`, `review evidence`,
  `reconstruction reducer`, `meaning shift`, and `policy executor`.
- The main axes map is conceptually correct but still looks like a research
  index. It does not yet answer "what should I care about this week?" in plain
  language.
- The readiness matrix says what each item is, but not why the status matters.
- The risk heatmap lacks concrete symptoms. For example, "concept inflation" is
  real, but the report should show what would count as a warning sign.
- Some Chinese text still mixes English abstractions heavily. This is acceptable
  for internal keys, but not for founder-facing explanations.

## Chinese Names To Improve

| Current name | Suggested founder-facing name | Reason |
|---|---|---|
| 状态化记忆 | 带状态的记忆 | More concrete and less academic. |
| 成长候选审查 | 成长提案审查 | "提案" makes it clearer that it is not completed growth. |
| 时间一致性 | 时间线一致性检查 | Sounds like an evaluable check, not a mental property. |
| 能力进化 | 能力改进边界 | Reduces the risk of confusing capability work with subject growth. |
| 工具优先自进化 | 先改工具，不改身份 | Founder-facing and boundary-first. |
| 轻量交互试验台 | 本地交互预演 | Easier to understand than "harness". |
| 信念证据图 | 说法证据图 | More intuitive for non-research reading. |
| 治理表面 / Governance Surface | 跨层审查区 | Better matches the actual role. |

These are display-name suggestions only. They do not rename internal keys,
schemas, files, RFCs, or code identifiers.

## Modules Needing Simpler Explanation

- Identity Core: explain as "the protected answer to who 01 is."
- Event Log: explain as "a ledger of important state changes."
- Replay: explain as "checking whether history can be followed again."
- Reconstruction: explain as "rebuilding a past state from evidence, not doing
  it yet."
- Claim Graph: explain as "which claims are supported, conflicting, or still
  open."
- Stateful Memory: explain as "memory plus the conditions under which it was
  formed and recalled."
- Temporal Coherence: explain as "whether a change still fits the timeline."
- Capability Evolution: explain as "tool and workflow improvement that must not
  change identity."
- Thin Interaction Harness: explain as "a future local preview surface, not a
  chat product."

## Risk Display Gaps

The heatmap should become more actionable before any harness work:

- Add a `symptom` column: what would the founder observe if this risk is active?
- Add a `current_guardrail` column: what currently prevents the risk?
- Add a `next_manual_check` column: what should be checked by a human next?
- Translate mitigation text in the Chinese report.
- Group risks by severity and layer: identity, memory, temporal, tool,
  observability, product.
- Avoid generic mitigations such as "use glossary" unless paired with a concrete
  action.

## Harness Recommendation

Do **not** enter minimal CLI harness implementation yet.

The observatory is useful enough as a static status report, but not yet strong
enough as the foundation visibility layer before interaction work. The report
should first make status, risk, and blocked boundaries clearer for the founder
without requiring prior knowledge of P0-P96 terminology.

## Needed Before Harness

Recommended next observatory-only improvements:

- Add Chinese display labels for readiness status:
  `已实现`, `报告层`, `RFC 层`, `评估层`, `未来方向`, `已阻塞`, `过早危险`.
- Add one-sentence "why this matters" text for each readiness row.
- Add `symptom`, `guardrail`, and `manual_check` fields to risk heatmap output.
- Add a short "current safe next step" section that clearly says review first.
- Add a compact founder summary that fits in one screen.
- Keep all improvements static and read-only.

## Boundary Statement

P97 recommends improving observatory clarity before any minimal CLI harness. It
does not authorize harness implementation, product UI, AstrBot integration,
companion behavior, policy execution, tool execution, identity mutation, memory
rewrite, recall event writes, growth execution, Temporal Awareness runtime,
reconstruction reducer execution, event compaction, or automatic roadmap
execution.
