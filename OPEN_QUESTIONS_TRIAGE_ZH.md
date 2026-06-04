# Open Questions Triage / 开放问题分诊

English version: [OPEN_QUESTIONS_TRIAGE.md](./OPEN_QUESTIONS_TRIAGE.md)

P57 对 P54-P56 之后的 foundation open questions 做分诊。它不关闭这些问题，也不实现 runtime behavior。

## Triage Levels / 分诊等级

- `next-rfc`：适合下一步写 document-only RFC。
- `wait-for-contract`：需要先有另一个 contract 或 boundary。
- `watch`：重要，但当前只监控，不立即推进。
- `blocked-runtime`：当前 foundation layer 严禁实现。

## Triage Table / 分诊表

| Question | Level | Why | Next Safe Action | Forbidden Action |
|---|---|---|---|---|
| Temporal Awareness | next-rfc | 对 subject continuity 很重要，但 runtime 风险高。 | P58 document-only RFC。 | temporal runtime 或 temporal event execution。 |
| Recall Event Write Policy | next-rfc | P50 已引入 recall semantics，但 writes 仍禁止。 | P59 document-only policy RFC。 | writing recall events。 |
| Stateful Memory Minimal Encoding Policy | next-rfc | P50 在深入 semantics 前需要 minimum encoding references。 | P60 policy document。 | 创建新 memory store 或 rewrite path。 |
| Growth Candidate Lifecycle | wait-for-contract | lifecycle 容易被误解为 promotion。 | P61 RFC with non-execution invariants。 | lifecycle execution 或 promotion。 |
| Productive Drift vs Collapse | next-rfc | 需要它来保持 growth semantics 安全。 | P62 RFC 定义 evidence/risk/rejection boundaries。 | automatic growth classification。 |
| Exploration / Serendipity Engine | watch | 有价值，但容易滑向 companion 或 roleplay behavior。 | P63 document-only RFC，前提是边界严格。 | productized exploration engine。 |
| Subject Kernel / World Seed | watch | 可能澄清 identity/world boundary，但也可能扩张 identity theory。 | P64 RFC，但要先 review identity boundary。 | Identity Core rewrite。 |
| Reconstruction Reducer Contract | wait-for-contract | reducer execution 前必须定义，但不能执行。 | P65 document-only contract RFC。 | reducer execution 或 state rebuild。 |
| Payload / Diff Capture Policy | wait-for-contract | 需要 reducer contract 和 target-path rules。 | P66 policy RFC after P65 draft。 | payload capture 或 event schema mutation。 |
| Productive Drift vs Random Drift Evaluation | watch | 未来 evaluation 有帮助，但当前文档已足够 triage。 | 加入 future evaluation backlog。 | growth engine execution。 |

## Recommended Order / 推荐顺序

1. P58 Temporal Awareness RFC v0.1，document-only。
2. P59 Recall Event Write Policy RFC，document-only。
3. P60 Stateful Memory Minimal Encoding Policy。
4. P61 Growth Candidate Lifecycle RFC，document-only。
5. P62 Productive Drift vs Collapse RFC。
6. P65 Reconstruction Reducer Contract RFC，在任何 payload/diff implementation 之前。

除非 foundation 在继续 reconstruction work 前需要 subject/world clarification，否则 P63/P64 可以等待。

## Explicit Non-Goals / 明确不做

- 不做 runtime Temporal Awareness。
- 不写 recall event。
- 不执行 growth lifecycle。
- 不做 identity mutation。
- 不做 memory rewrite。
- 不执行 reconstruction reducer。
- 不进入 companion、relationship、UI、AstrBot、adapter 或 product layer。
