# 创始人控制台验收标准

English version: [FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md](./FOUNDER_CONSOLE_ACCEPTANCE_CRITERIA.md)

状态：`P134`、`acceptance-criteria`、`document-only`、`non-runtime`。

P134 定义任何 future Thin Founder Console 的 acceptance criteria。它不实现 console、command、UI、Companion、adapter integration、model call、tool execution、write path、validation runtime、policy executor 或 rebuild。

## 验收原则

```text
founder console 只有在增加 visibility
且不增加 autonomy 时才可接受。
```

如果一个 proposed console 让系统更主动、更连接外部、更像说服工具或更有写入能力，它就不通过。

## 必须通过

| Area | Criterion | Evidence Needed Later |
|---|---|---|
| local-only | 不依赖 external network 或 services 运行。 | tests 或 code review 中无 network calls |
| founder-only | 为 founder review 设计，不面向 end users。 | labels、flow 和 docs 避免 product framing |
| no-write | 不改变 formal state、memory、events、recall、identity、tasks、claims、tools、adapters 或 rebuild files。 | before/after file checks |
| report-only output | 只在明确请求时写 explicit report files。 | output flag tests |
| boundary visibility | 清楚显示 blocked actions。 | output 中有 boundary monitor |
| candidate clarity | 把 candidates 标成 preview-only，不是 promoted 或 persisted。 | output assertions |
| source transparency | 显示使用或省略了哪些 local sources。 | source ref list |
| founder readability | 使用简单标签，并在有帮助时使用中文显示名。 | founder-facing review |
| deterministic behavior | 相同 input 和 sources 产生稳定 output。 | golden 或 snapshot tests |
| fail closed | 不安全或不清楚时停止，而不是行动。 | failure-path tests |

## 必须失败

如果 proposed console 做了这些，就必须失败：

- 调用 LLM；
- 调用 external API；
- 连接 AstrBot 或任何 adapter；
- 实现 Web UI 或 product dashboard；
- 写 formal state 或 memory；
- 创建 recall events；
- 修改 identity；
- 执行工具；
- 晋升 candidates；
- 创建 growth lifecycle state；
- 运行 temporal 或 CTM runtime；
- 运行 reconstruction reducers；
- 压缩 events；
- 自动选择 roadmap；
- 开始 rebuild。

## Founder-Facing 验收

founder 应该能回答：

- 我现在在哪个 phase？
- 我可以安全检查什么？
- 什么被 blocked？
- 什么只是 preview？
- 哪些 source 支持这个 preview？
- 当前最重要风险是什么？
- 下一条 candidate direction 是什么？
- 什么必须由我明确批准后才会改变？

如果 console 不能在不深挖技术细节的情况下回答这些问题，它就还没准备好。

## CTM-Inspired Temporal Criteria

Temporal content 只有在以下情况下可接受：

- 标为 symbolic 或 review-only；
- 不声称 consciousness；
- 不存储 thought traces；
- 不写 temporal 或 recall events；
- 不把 elapsed time 变成 identity change；
- 把 temporal pressure 路由到 review，而不是 execution。

## Tool-First Criteria

Capability content 只有在以下情况下可接受：

- tool success 是 evidence，不是 authorization；
- procedure reuse 是 candidate，不是 trusted tool；
- capability evolution 不是 subject growth；
- unsafe candidates 路由到 quarantine 或 review；
- 不发生 tool execution 或 promotion。

## 最小未来测试列表

如果后续 implementation 被批准，tests 应覆盖：

- 本地运行且无 network；
- markdown 和 JSON output；
- 中文 founder-facing labels；
- explicit output file behavior；
- no formal state changes；
- 所有 forbidden capabilities disabled；
- candidates 保持 preview-only；
- 有 source refs 时显示；
- failure path 不写入；
- repeated input deterministic。

## 完成声明

P134 定义 founder console 在被建造前如何被判断。门槛是 visibility without autonomy，以及 founder understanding without product behavior。
