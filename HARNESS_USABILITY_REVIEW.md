# Harness Usability Review

Chinese version: [HARNESS_USABILITY_REVIEW_ZH.md](./HARNESS_USABILITY_REVIEW_ZH.md)

Status: `review-only`, `document-only`, `non-runtime`.

P101 reviews whether the P100 `harness-dry-run` command helps the founder see
how one input would move through 01 Core. It does not change Identity Core,
memory, recall policy, retrieval, AstrBot, UI, model calls, tool execution, or
next-step execution.

## Commands Reviewed

For each input below, the review ran:

- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format markdown --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format json --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang en --format markdown --output /private/tmp/...`

Inputs:

- "我现在有点看不清这个项目到底做了什么"
- "这个想法可能是一次成长吗？"
- "我想把这个接进 AstrBot"
- "我们是不是该开始做应用层了？"
- "这个工具候选验证成功了，能不能直接加入工具库？"

All temporary `--output` files were written outside the repository.

## Readability Score

Overall founder-facing readability: **6.5 / 10**.

| Area | Score | Reason |
|---|---:|---|
| Intake preview | 8 | The input, session, actor, privacy scope, CLI source, and no-write status are easy to see. |
| Context package preview | 5 | The section shows foundation references, but the same static package appears for very different inputs. |
| Candidate preview | 5 | It clearly says candidate is not promotion, but every input receives the same candidate list. |
| Review queue preview | 7 | `lifecycle_created: false` and `execution_allowed: false` make the review-only boundary visible. |
| Boundary monitor | 8.5 | This is the strongest section. Forbidden actions are explicit and disabled. |
| Observatory snapshot | 6 | It names real top risks, but it is not input-specific enough. |
| Chinese wording | 6.5 | Section titles are clear, but several rows still feel like translated RFC vocabulary. |
| Founder next-step judgment | 5.5 | It helps prevent premature execution, but does not yet help choose what to review next. |

## Per-Input Observations

| Input | What worked | What did not work |
|---|---|---|
| "我现在有点看不清这个项目到底做了什么" | The observatory snapshot correctly surfaces "concept overload" as a top risk. | The report still does not answer the founder's actual confusion in plain project-summary terms. |
| "这个想法可能是一次成长吗？" | `growth_candidate_review` appears and remains `promoted: false`. | The growth question is not prioritized; memory, claim, recall, and task candidates look equally likely. |
| "我想把这个接进 AstrBot" | `adapter_integration_required: false` is visible in the boundary monitor. | The report does not explicitly say "AstrBot integration is blocked here"; the signal is present but too quiet. |
| "我们是不是该开始做应用层了？" | The snapshot lists premature runtime as a high risk. | The output does not directly mark product/application-layer pressure as the main issue. |
| "这个工具候选验证成功了，能不能直接加入工具库？" | Tool execution stays disabled, and no promotion occurs. | The harness has no capability/tool-candidate route, so it misses the key P92 boundary: verification is not authorization. |

## What Works

- The command proves the P100 boundary: local preview, no model call, no adapter
  call, no state write, no memory write, no recall write, no identity mutation.
- The report shape is useful: intake, context preview, candidate preview, review
  queue, boundary monitor, observatory snapshot, and non-execution invariants.
- The boundary monitor is founder-readable enough to audit forbidden actions.
- Candidate rows visibly keep `preview_only: true`, `promoted: false`, and
  `persisted: false`.
- JSON output is structured enough for future static review, while still being
  a report artifact rather than an execution contract.

## Still Too Abstract

- `context_package_preview` is mostly a static foundation reference list. It
  does not yet explain why this specific input selected these references.
- `candidate_preview` feels mechanical because every input produces the same
  six candidate rows.
- `observatory_snapshot` is too global. It does not adapt to AstrBot pressure,
  application-layer pressure, tool-promotion pressure, or growth-review
  pressure.
- The report still uses terms such as `recall_event_candidate`,
  `meaning_shift_candidate`, `lifecycle`, `preview_only`, and `policy` without
  enough founder-facing explanation.
- English internal keys are appropriate for auditability, but they still crowd
  the Chinese report.

## Candidate Preview Problems

The current candidate preview is safe but too static.

- Growth questions should highlight growth review as the primary candidate and
  explicitly say "growth review is not growth."
- AstrBot requests should highlight adapter/product boundary pressure.
- Application-layer requests should highlight product-layer and runtime
  boundary pressure.
- Tool-library requests should highlight capability-evolution review and say
  "verification is not authorization."
- General confusion requests should highlight observatory/readability review
  instead of showing all candidate types as equally relevant.

This should remain deterministic and static until a future explicit phase. It
does not require real retrieval, model calls, event writes, or state reads.

## Chinese Names To Improve

| Current display | Suggested founder-facing display | Reason |
|---|---|---|
| 上下文包预览 | 会带哪些背景 | More natural for a founder scanning a dry-run. |
| 候选项预览 | 可能进入审查的事项 | Makes it clearer that nothing has been accepted. |
| 审查队列预览 | 等待人工判断的门 | Less abstract than "queue". |
| 边界监视器 | 禁止事项检查 | More direct and safety-oriented. |
| 回忆事件候选 | 回忆写入候选 | Connects the item to the blocked write policy. |
| 意义变化候选 | 解释变化候选 | Easier than "meaning shift". |
| Identity Gate | 身份闸门 | Avoids unexplained English in Chinese output. |
| Memory Lifecycle | 记忆生命周期 | Translate the reference label. |

These are display-name suggestions only. They do not rename internal keys,
schemas, files, RFCs, or code identifiers.

## Recommendation

Do **not** enter product-layer, AstrBot, UI, model-call, real retrieval, memory
write, recall-write, tool-execution, or growth-lifecycle implementation.

Do **not** treat P100 as a real harness runtime yet. It is a useful local
preview surface, but it is still too static to guide high-stakes next-step
decisions.

## P102 Candidate Direction

Recommended P102: **Harness Readability Improvement**, still static and
read-only.

Suggested P102 scope:

- add a one-screen founder summary at the top of the dry-run report;
- add deterministic intent labels such as `project_clarity_pressure`,
  `growth_review_pressure`, `adapter_pressure`, `product_layer_pressure`, and
  `tool_promotion_pressure`;
- add `primary_candidate`, `secondary_candidates`, and `not_selected_reason`
  without executing retrieval or writing state;
- make boundary warnings louder when the input mentions AstrBot, application
  layer, tool promotion, identity growth, or memory writes;
- translate more Chinese display labels while preserving English internal keys.

P102 should still forbid model calls, real retrieval, state reads or writes,
memory writes, recall writes, identity mutation, adapters, UI, product behavior,
tool execution, and automatic next-step execution.

## Boundary Statement

P101 is a usability review only. It does not authorize P102, runtime work,
application work, adapter integration, Companion behavior, model calls,
retrieval execution, event writes, memory writes, recall writes, identity
mutation, growth execution, temporal runtime, tool execution, policy execution,
reconstruction reducer execution, event compaction, or automatic roadmap
execution.
