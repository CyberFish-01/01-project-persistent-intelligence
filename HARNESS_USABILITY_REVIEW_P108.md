# Harness Usability Re-Review P108

Chinese version: [HARNESS_USABILITY_REVIEW_P108_ZH.md](./HARNESS_USABILITY_REVIEW_P108_ZH.md)

Status: `review-only`, `document-only`, `non-runtime`.

P108 re-reviews `harness-dry-run` after P102-P107. It checks whether the founder
can now see how different inputs route through 01 Core without treating the
harness as a product, runtime, memory writer, model caller, adapter, tool
executor, or lifecycle engine.

## Commands Reviewed

For each input, P108 ran:

- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format markdown --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang zh --format json --output /private/tmp/...`
- `python3 -m one_core.cli harness-dry-run --input "..." --lang en --format markdown --output /private/tmp/...`

All temporary outputs were written outside the repository. The supplied
`--state-dir` paths were not created.

## Inputs Reviewed

| Input | Pressure Type | Candidate Preview | Review Gates | Highest Boundaries |
|---|---|---|---|---|
| "我现在有点看不清这个项目到底做了什么" | `observability_pressure` | observatory readability, task update, claim | observatory, task, claim | observability executor, automatic next step, product layer |
| "这个想法可能是一次成长吗？" | `growth_review_pressure` | growth review, meaning shift, identity high gate | growth, meaning shift, identity high gate | identity mutation, growth execution, memory rewrite |
| "我想把这个接进 AstrBot" | `adapter_boundary_pressure` | adapter boundary, task update, governance boundary | adapter, task, governance | adapter integration, companion, harness write |
| "我们是不是该开始做应用层了？" | `product_layer_pressure` | product boundary, observatory readability, governance boundary | product, observatory, governance | companion, policy executor, automatic next step |
| "这个工具候选验证成功了，能不能直接加入工具库？" | `capability_evolution_pressure` | capability growth, tool authorization, cautionary procedural memory | capability, tool authorization, cautionary memory | tool execution, tool promotion, policy executor |
| "我隔了很久回来，怎么恢复会话？" | `temporal_pressure` | temporal review, recall-write, delayed interpretation | temporal, recall policy, meaning shift | temporal event, recall mutation, memory rewrite |
| "这个 event 能回放重建 payload diff 吗？" | `reconstruction_pressure` | reconstruction evidence, payload/diff gap, replay check | reconstruction evidence, payload/diff, replay | reducer execution, event compaction, memory rewrite |
| "请记录一个普通观察" | `unknown_pressure` | general review, task update | general, task | automatic next step, harness write, policy executor |

## Readability Score

Overall founder-facing readability: **8.0 / 10**.

P101 score was **6.5 / 10**. The main improvement is that the same five inputs
no longer receive the same static candidate table. P102-P107 now show pressure
classification, matched signals, scenario-specific candidates, review gate
routing, highlighted boundaries, and manual-review-only lifecycle blocks.

| Area | P101 | P108 | Reason |
|---|---:|---:|---|
| Intake preview | 8 | 8 | Still clear and unchanged. |
| Scenario routing | 0 | 8.5 | New pressure types and matched signals make the first decision visible. |
| Context package preview | 5 | 7 | Now includes profile-specific references, but still uses static sources. |
| Candidate preview | 5 | 8.5 | Candidates now differ by input and explain intent, selection reason, blocked promotion, and manual review. |
| Review queue preview | 7 | 8.5 | Gates now explain queue intent, why the gate was selected, and why no lifecycle is created. |
| Boundary monitor | 8.5 | 9 | Forbidden actions are structured and profile-specific boundaries are highlighted. |
| Observatory snapshot | 6 | 7.5 | Snapshot is now pressure-specific, but still short and static. |
| Chinese wording | 6.5 | 7.5 | Chinese is clearer, though English internal keys still crowd some rows. |
| Founder next-step judgment | 5.5 | 8 | Each pressure has a concrete manual next step and a do-not-do list. |

## Per-Input Observations

| Input | What Improved | Remaining Weakness |
|---|---|---|
| Project unclear | Correctly routes to observability pressure and suggests simplifying the founder-facing map. | It still does not provide a short plain-language project answer inside the harness. |
| Growth question | Growth review is primary, identity gate is visible, and growth is not promoted. | Meaning shift and identity terms remain abstract for non-technical review. |
| AstrBot integration | Adapter pressure is explicit; the report says not to integrate AstrBot or require an adapter. | It does not yet show a future allowed adapter contract in one compact row. |
| Product layer | Product pressure is explicit; Companion/UI/product boundaries remain blocked. | The report could make "not a product surface" more visually prominent. |
| Tool library | Capability pressure is explicit; verification is not authorization; tool promotion stays disabled. | Cautionary procedural memory still needs plainer founder wording. |
| Temporal resume | Temporal pressure is explicit; temporal and recall event writes stay blocked. | Temporal concepts still depend heavily on RFC vocabulary. |
| Reconstruction | Payload/diff and replay gaps are visible; reducers and compaction remain blocked. | It cannot inspect real event payload coverage, by design. |
| Unknown | Weak-signal fallback is conservative and asks for clarification. | It may feel unhelpful for ordinary note-taking because writing remains blocked. |

## What Works Now

- Different inputs now take different deterministic routes.
- Founder-facing summaries make the pressure type and matched signals visible at
  the top of the report.
- Candidate previews no longer look like generic checklists.
- Review queue rows now clearly say "manual review only" and explain why a
  lifecycle is blocked.
- Boundary monitor remains the strongest safety section and now highlights the
  most relevant disabled capabilities for the selected pressure.
- JSON output is structured enough for future read-only comparison tests.

## Still Too Abstract

- `context_package_preview` still names documents and concepts, not actual
  retrieved context.
- `human_readable_risks` remains partly templated; risk explanations are safe
  but not yet very situational.
- Chinese output still exposes many English internal keys because auditability
  is being preserved.
- The observatory snapshot is helpful but short; it does not yet summarize all
  project state relevant to the selected pressure.
- Unknown-pressure inputs can only ask for clarification because the harness is
  still no-write.

## Recommendation

Do not enter product-layer, UI, AstrBot, adapter, model-call, real retrieval,
state write, memory write, recall write, tool execution, growth lifecycle,
temporal runtime, reconstruction reducer, event compaction, or automatic
next-step execution.

P108 does suggest the harness is now strong enough to plan the next read-only
improvement: a more explicit harness roadmap and then, only if approved later, a
read-only context preview refinement. It is not yet a real interaction runtime.

## P109 Candidate

Recommended P109: **Harness Roadmap**.

The roadmap should explain:

- what the harness can see now;
- what it still cannot see;
- what remains intentionally blocked;
- whether a future read-only context preview refinement is safe;
- which work should remain deferred until after founder/CTO review.

## Boundary Statement

P108 is a usability re-review only. It does not authorize runtime work, product
work, adapter integration, Companion behavior, model calls, real retrieval,
event writes, memory writes, recall writes, identity mutation, growth execution,
temporal runtime, tool execution, policy execution, reconstruction reducer
execution, event compaction, automatic tool promotion, or automatic roadmap
execution.
