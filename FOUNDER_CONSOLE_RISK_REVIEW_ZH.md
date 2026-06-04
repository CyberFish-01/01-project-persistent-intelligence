# 创始人控制台风险复盘

English version: [FOUNDER_CONSOLE_RISK_REVIEW.md](./FOUNDER_CONSOLE_RISK_REVIEW.md)

状态：`P135`、`risk-review`、`document-only`、`non-runtime`。

P135 复盘规划 future Thin Founder Console 带来的风险。它不实现 console、command、UI、Companion layer、adapter integration、model call、tool execution、write path、policy executor 或 rebuild。

## 风险总结

founder console 只有在保持 local visibility surface 时才安全。它最大的危险是心理和架构上的：因为它看起来像应用，所以容易诱导项目过早像产品一样行动。

## Top Risks

| Risk | Why It Matters | Mitigation |
|---|---|---|
| product-layer creep | 一个可读 console 很容易在 core ready 前变成用户产品。 | 保持 founder-only language，不提供 product routes。 |
| Companion creep | 会回答 founder 问题的 console 容易开始像 social agent。 | 保持 report-oriented，而不是 relational。 |
| automatic roadmap creep | next-step candidates 可能被误认为 selected actions。 | 显示 candidate status，并要求 explicit founder approval。 |
| write-path creep | output files 可能变成 formal state writes 的桥。 | reports 留在 state stores 之外，并标记 report-only。 |
| adapter creep | adapter pressure 可能通过“preview”语言回来。 | shadow adapter examples 保持 disconnected 和 no-ingest。 |
| model-call creep | console 加 LLM summary 会看起来更有用。 | 在后续边界出现前，保持 deterministic local reports。 |
| policy-executor creep | boundary warnings 可能变成 automatic enforcement。 | warnings 只 display，不 execution。 |
| founder over-trust | polished report 可能看起来比实际更权威。 | 显示 source refs、omissions 和 uncertainty。 |
| temporal overreach | temporal cues 可能被误读成 thought dynamics。 | CTM-inspired content 保持 symbolic 和 review-only。 |
| capability overreach | tool evidence 可能被误读成 authorized tools。 | Tool-First evidence 保持 candidate/review only。 |

## Founder-Facing Warning

future console 应明确显示：

```text
This is a visibility surface.
It does not decide, write, connect, execute, or rebuild.
```

没有这句话，founder-facing clarity 可能变成 founder-facing overconfidence。

## 避免的危险措辞

避免这些 labels：

- "approved next step"；
- "memory restored"；
- "identity updated"；
- "adapter ready"；
- "tool verified"；
- "temporal state changed"；
- "rebuild ready"，除非 final verification 真的已经通过。

优先使用：

- "candidate next step"；
- "source-backed preview"；
- "manual review required"；
- "blocked boundary"；
- "report-only"；
- "not ready yet"。

## CTM-Inspired Temporal 风险

console 可能让 temporal concepts 更容易看见。这会增加它们被误读成 inner thought 的风险。

缓解：

- 使用 "temporal review cue"，而不是 "thought state"；
- 使用 "review depth suggestion"，而不是 "deliberation executed"；
- 使用 "thought-trace policy reminder"，而不是 "thought trace captured"；
- 绝不声称 consciousness 或 neural equivalence。

## Tool-First 风险

console 可能让 capability candidates 看起来像已经 operational。

缓解：

- 显示 "verification evidence is not authorization"；
- 显示 "candidate is not tool library entry"；
- unsafe candidates 显示为 quarantined 或 deferred；
- tool execution 保持 disabled 且可见。

## 风险决策

founder console block 可以继续，因为当前 document-only planning level 的风险可控。

它不应进入 implementation，除非 P134 acceptance criteria 继续可见，并且未来 implementation phase 证明：

- local-only operation；
- no external IO；
- no model call；
- no state mutation；
- no adapter connection；
- no automatic next step；
- no rebuild。

## 完成声明

P135 记录 founder console 的主要危险：让项目在真正 ready 前感觉已经 ready。缓解方式是保持 console report-only、founder-only、local，清楚显示 blocked actions，并对自己知道什么保持克制。
