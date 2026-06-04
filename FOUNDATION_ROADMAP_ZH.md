# Foundation Roadmap / 基础层路线图

English version: [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md)

状态：`document-only`、`synthesis`、`non-runtime`。

P67 把 P54-P66 综合成 foundation roadmap。它不新增 runtime behavior、新 schemas、
adapters、product surfaces、reconstruction reducers、payload capture、identity mutation、
memory rewrite、recall event writes、growth execution 或 Temporal Awareness runtime。

## Roadmap Principle / 路线图原则

```text
foundation work should reduce ambiguity before it adds power.
```

P54-P66 已经把一组很宽的 open questions 收束成有边界的 review surfaces。下一步应该先做
consolidation、index 和边界可见性维护，再考虑任何新的 runtime capability。

## Current Foundation Lanes / 当前基础层主线

| Lane | Current Status | Main Artifacts | Next Safe Work |
|---|---|---|---|
| Foundation Integrity | stable document foundation | P54-P56 audit、overlap review、boundary matrix | 持续维护 consistency checks |
| Open Question Governance | triaged | P57 triage、P58-P66 RFCs | 维护 RFC index 和 open question status |
| Stateful Memory / Growth | bounded review semantics | P59-P62 policy/RFCs | 保持 growth candidate 与 growth 分离 |
| Exploration / Subject Boundary | future-only boundary language | P63-P64 RFCs | 避免 product、companion 或 identity rewrite paths |
| Reconstruction Readiness | contract/policy defined, execution blocked | P65-P66 RFCs 加 P41-P49 reports | 不执行 reducers；只做文档细化 |
| Product / Adapter Layer | pushed back | foundation/product boundary docs | foundation loop 内不做 AstrBot/UI/product work |

## Stable Foundation / 稳定地基

下面这些应被视为项目稳定地基：

- 01 Core owns state.
- State Transfer is stronger than retrieval.
- Identity Core is protected by gate.
- Events are append-only audit evidence.
- Dream proposes; review decides.
- Review object is not execution.
- Growth candidate is not growth.
- Reconstruction evidence is not reconstruction.
- Capture policy is not payload capture.
- Reducer contract is not reducer execution.
- Time remains future direction unless explicitly planned.
- Models, platforms, and adapters do not own identity.

## P54-P66 Results / P54-P66 结果

| Range | Result |
|---|---|
| P54-P56 | 审计 foundation integrity，收敛 concept overlap，并建立 boundary test matrix。 |
| P57 | 把 open questions 分诊为 safe RFC、wait-for-contract、watch 和 blocked runtime work。 |
| P58-P60 | 澄清 Temporal Awareness、recall event write policy 和 stateful memory encoding，不做 runtime writes。 |
| P61-P62 | 澄清 growth candidate lifecycle 和 productive drift vs collapse，不执行 growth。 |
| P63-P64 | 澄清 exploration/serendipity 和 subject kernel/world seed，不进入 companion/product 或 identity rewrite。 |
| P65-P66 | 定义 reconstruction reducer contract 和 payload/diff capture policy，不执行 reducer 或 payload capture。 |

## Blocked Runtime Work / 阻塞的 Runtime 工作

除非未来明确进入 implementation phase，否则以下仍然 blocked：

- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- automatic growth classification；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- object-level 或 full-state rebuild；
- event compaction；
- policy executor；
- companion、relationship memory、UI、AstrBot、adapter 或 product layer。

## Future Contract Dependencies / 未来契约依赖

进入 runtime 前，项目仍需要：

| Future Area | Required Before Implementation |
|---|---|
| Temporal Awareness | recall event write policy、temporal review placement、elapsed-time evidence rules |
| Recall Events | accepted write gate、payload/diff policy、validation invariants |
| Growth Lifecycle | promotion boundary、identity gate integration、no-execution validation |
| Reconstruction Reducer | accepted reducer contract、target-path capture policy、deterministic validation |
| Payload Capture | privacy/redaction policy、schema review、event compatibility plan |
| Subject Kernel / World Seed | identity boundary review、reconstruction path distinction、no runtime split |
| Exploration | signal schema、quarantine rules、anti-companion evaluation |

P67 不批准这些 dependencies。

## P68-P80 Low-Risk Backlog / P68-P80 低风险待办

后续只应继续低风险 consolidation：

- docs consistency pass；
- glossary deduplication；
- Chinese/English sync；
- README entrance optimization；
- phase index extension for P52-P67；
- concept map extension for P58-P66；
- open questions status update；
- risk register；
- architecture boundary refresh；
- RFC index；
- `DECISIONS.md` foundation decisions log；
- `RESEARCH_NOTES_INDEX.md` source-note traceability index；
- `FOUNDATION_REVIEW_CHECKLIST.md` manual phase review gate。

不要为了到 P80 而打开新的 runtime capability phase。

## Suggested Next Order / 建议顺序

1. P68 RFC Index。
2. P69 Phase Index Extension。
3. P70 Concept Map Update。
4. P71 Open Questions Status Update。
5. P72 Risk Register。
6. P73 Architecture Boundary Refresh。
7. P74 Glossary Deduplication。
8. P75 README Entrance Optimization。
9. P76 Foundation Review Checklist。
10. P77 Decisions Log。
11. P78 Research Notes Index。
12. P79 Bilingual Consistency Pass。
13. P80 Final Foundation Maintenance Review。

这个顺序只是建议。如果某一步不能增加清晰度，可以跳过或合并。

P76 已由 [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md)
及其中文配对文档满足。该 checklist 是 manual review gate，不是 automated
executor。

P77 已由 [DECISIONS.md](./DECISIONS.md) 及其中文配对文档满足。该 decisions
log 记录 project stance；它不是 approval engine。

P78 已由 [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) 及其中文配对文档
满足。该 index 把 origin notes 映射到当前 foundation artifacts；它不新增 theory 或
implementation approval。

P79 已由 [BILINGUAL_CONSISTENCY_REVIEW.md](./BILINGUAL_CONSISTENCY_REVIEW.md)
及其中文配对文档满足。该 review 记录 paired-document consistency 和 boundary
alignment；它不自动执行 translation checks，也不批准 runtime work。

P80 已由 [FOUNDATION_MAINTENANCE_REVIEW.md](./FOUNDATION_MAINTENANCE_REVIEW.md)
及其中文配对文档满足。该 review 关闭 P54-P80 maintenance cycle；它不批准 runtime
implementation 或 product work。

## Completion Definition For Foundation Layer / 基础层完成定义

基础层不是因为所有想法都被实现才算完成。一个周期足够完成，指的是：

- stable principles 容易找到；
- open questions 已被 triaged；
- blocked runtime work 清晰可见；
- RFCs 已被 indexed；
- bilingual docs 对边界保持一致；
- 未来 implementation 不能错误地从 review-only documents 中声称自己已被批准。

## Current Recommendation / 当前建议

继续低风险 consolidation。不要进入 runtime work。不要连接 AstrBot。不要 productize。
不要实现 growth、Temporal Awareness、payload capture、reducer execution 或 event compaction。
