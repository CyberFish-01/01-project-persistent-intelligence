# Open Questions Triage

Chinese version: [OPEN_QUESTIONS_TRIAGE_ZH.md](./OPEN_QUESTIONS_TRIAGE_ZH.md)

P57 triages open foundation questions after P54-P56. It does not close the
questions and does not implement runtime behavior.

## Triage Levels

- `next-rfc`: safe to turn into a document-only RFC next.
- `wait-for-contract`: requires another contract or boundary first.
- `watch`: important but should be monitored rather than advanced immediately.
- `blocked-runtime`: must not be implemented in the foundation layer yet.

## Triage Table

| Question | Level | Why | Next Safe Action | Forbidden Action |
|---|---|---|---|---|
| Temporal Awareness | next-rfc | Important for subject continuity, but runtime is risky. | P58 document-only RFC. | temporal runtime or temporal event execution. |
| Recall Event Write Policy | next-rfc | P50 introduced recall semantics but writes remain forbidden. | P59 document-only policy RFC. | writing recall events. |
| Stateful Memory Minimal Encoding Policy | next-rfc | P50 needs minimum encoding references before any deeper semantics. | P60 policy document. | creating a new memory store or rewrite path. |
| Growth Candidate Lifecycle | wait-for-contract | Lifecycle can be mistaken for promotion. | P61 RFC with non-execution invariants. | lifecycle execution or promotion. |
| Productive Drift vs Collapse | next-rfc | Needed to keep growth semantics safe. | P62 RFC defining evidence/risk/rejection boundaries. | automatic growth classification. |
| Exploration / Serendipity Engine | watch | Useful but can drift toward companion or roleplay behavior. | P63 document-only RFC if boundaries stay strict. | productized exploration engine. |
| Subject Kernel / World Seed | watch | May clarify identity/world boundary, but can over-expand identity theory. | P64 RFC only after identity boundary review. | Identity Core rewrite. |
| Reconstruction Reducer Contract | wait-for-contract | Needed before reducer execution, but must not execute. | P65 document-only contract RFC. | reducer execution or state rebuild. |
| Payload / Diff Capture Policy | wait-for-contract | Needs reducer contract and target-path rules. | P66 policy RFC after P65 draft. | payload capture or event schema mutation. |
| Productive Drift vs Random Drift Evaluation | watch | Evaluation may help later, but current docs are enough for foundation triage. | Add to future evaluation backlog. | growth engine execution. |

## Recommended Order

1. P58 Temporal Awareness RFC v0.1, document-only.
2. P59 Recall Event Write Policy RFC, document-only.
3. P60 Stateful Memory Minimal Encoding Policy.
4. P61 Growth Candidate Lifecycle RFC, document-only.
5. P62 Productive Drift vs Collapse RFC.
6. P65 Reconstruction Reducer Contract RFC before any payload/diff implementation.

P63/P64 can wait unless the foundation needs subject/world clarification before
reconstruction work continues.

## Explicit Non-Goals

- No runtime Temporal Awareness.
- No recall event write.
- No growth lifecycle execution.
- No identity mutation.
- No memory rewrite.
- No reconstruction reducer execution.
- No companion, relationship, UI, AstrBot, adapter, or product layer.
