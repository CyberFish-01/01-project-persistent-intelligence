# 创始人控制台路线图

English version: [FOUNDER_CONSOLE_ROADMAP.md](./FOUNDER_CONSOLE_ROADMAP.md)

状态：`P136`、`roadmap`、`document-only`、`non-runtime`。

P136 收口 Thin Founder Console planning block。它不实现 console、CLI command、Web UI、Companion、adapter integration、model call、tool execution、write path、policy executor 或 rebuild。

## P131-P136 建立了什么

| Phase | Contribution |
|---|---|
| P131 | Boundary：local、founder-only、no-write visibility，不是 product behavior。 |
| P132 | Flow：看状态、预览输入路径、检查边界、人工选择。 |
| P133 | Contract：只有 explicit report outputs，不写 formal state 或 memory。 |
| P134 | Acceptance criteria：visibility without autonomy。 |
| P135 | Risk review：product、Companion、roadmap、write、adapter、model、temporal 和 capability creep。 |

## Roadmap 位置

founder console 默认不是下一个要实现的东西。

更安全的下一步，是先定义 **Context Package Builder planning**，因为 future console 不应临场发明 context packaging。它应该显示或预览一个已经定义好的 package shape。

## 未来 Console Milestones

如果后续批准 implementation，roadmap 应该是：

1. Static founder report surface。
2. Read-only source inventory panel。
3. Harness dry-run panel。
4. Boundary monitor panel。
5. Review queue preview panel。
6. P137-P142 定义 package contract 后，再做 Context package preview panel。
7. P148-P154 定义 verification gate 后，再做 Pre-rebuild verification panel。

每个 milestone 都必须通过 P133 no-write contract 和 P134 acceptance criteria。

## 暂时不要做

不要做：

- Web UI；
- Companion layer；
- chat product；
- adapter panel；
- live old 01 import view；
- model response view；
- tool execution view；
- temporal runtime view；
- rebuild execution button。

## 通向 P137-P142

P137-P142 应定义 01 Core 如何为 future model call 准备 context，但不调用模型。

founder console 未来应该能显示：

- `identity_pack`
- `state_pack`
- `task_pack`
- `claim_pack`
- `memory_pack`
- `boundary_pack`
- `temporal_pack`
- `capability_pack`
- `response_strategy_pack`

但 P136 不详细定义这些 packs。它只把它们识别为下一组 planning block。

## CTM-Inspired Temporal Roadmap

Temporal console content 应等待 `temporal_pack` contract。未来这个 pack 可以把 elapsed-time cues、review-depth suggestions、unresolved tension 和 delayed alignment signals 显示为 symbolic review material。

不允许 CTM runtime、thought loop、thought trace storage、temporal event write、recall write 或 identity update。

## Tool-First Roadmap

Capability console content 应等待 `capability_pack` contract。未来这个 pack 可以把 tool candidates、procedure candidates、verification evidence 和 capability review gates 显示为 candidate/evidence/review material。

不允许 tool execution、tool promotion、dependency installation、policy executor 或 subject-growth claim。

## Roadmap 决策

P131-P136 已足够完整，可以先进入 **Context Package Builder planning**，而不是 console implementation。

下一步进入：

- Context Package Builder RFC；
- Context Package Preview CLI Plan；
- Source Selection Matrix；
- Boundary Injection RFC；
- CTM Temporal Context Pack RFC；
- Capability Context Pack RFC。

## 完成声明

P136 收口 Thin Founder Console block。项目现在知道 founder console 必须是什么、不能是什么。下一条安全前沿是在 model orchestration、console implementation、adapter work 或 rebuild 前，先定义 context packages。
