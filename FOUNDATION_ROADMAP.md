# Foundation Roadmap

Chinese version: [FOUNDATION_ROADMAP_ZH.md](./FOUNDATION_ROADMAP_ZH.md)

Status: `document-only`, `synthesis`, `non-runtime`.

P67 synthesizes P54-P66 into a foundation roadmap. It does not add runtime
behavior, new schemas, adapters, product surfaces, reconstruction reducers,
payload capture, identity mutation, memory rewrite, recall event writes, growth
execution, or Temporal Awareness runtime.

## Roadmap Principle

```text
foundation work should reduce ambiguity before it adds power.
```

P54-P66 turned a wide set of open questions into bounded review surfaces. The
next work should consolidate, index, and keep boundaries visible before any new
runtime capability is considered.

## Current Foundation Lanes

| Lane | Current Status | Main Artifacts | Next Safe Work |
|---|---|---|---|
| Foundation Integrity | stable document foundation | P54-P56 audit, overlap review, boundary matrix | keep consistency checks current |
| Open Question Governance | triaged | P57 triage, P58-P66 RFCs | maintain RFC index and open question status |
| Stateful Memory / Growth | bounded review semantics | P59-P62 policy/RFCs | keep growth candidate separate from growth |
| Exploration / Subject Boundary | future-only boundary language | P63-P64 RFCs | avoid product, companion, or identity rewrite paths |
| Reconstruction Readiness | contract/policy defined, execution blocked | P65-P66 RFCs plus P41-P49 reports | do not execute reducers; refine documentation only |
| Product / Adapter Layer | pushed back | foundation/product boundary docs | no AstrBot/UI/product work in foundation loop |

## Stable Foundation

The following should be treated as stable project ground:

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

## P54-P66 Results

| Range | Result |
|---|---|
| P54-P56 | Audited foundation integrity, reduced concept overlap, and created a boundary test matrix. |
| P57 | Triaged open questions into safe RFCs, wait-for-contract items, watch items, and blocked runtime work. |
| P58-P60 | Clarified Temporal Awareness, recall event write policy, and stateful memory encoding without runtime writes. |
| P61-P62 | Clarified growth candidate lifecycle and productive drift vs collapse without growth execution. |
| P63-P64 | Clarified exploration/serendipity and subject kernel/world seed without companion/product or identity rewrite. |
| P65-P66 | Defined reconstruction reducer contract and payload/diff capture policy without reducer execution or payload capture. |

## Blocked Runtime Work

These remain blocked until a future explicit implementation phase:

- Temporal Awareness runtime;
- recall event writes;
- growth lifecycle execution;
- automatic growth classification;
- identity mutation;
- memory rewrite;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- object-level or full-state rebuild;
- event compaction;
- policy executor;
- companion, relationship memory, UI, AstrBot, adapter, or product layer.

## Future Contract Dependencies

Before runtime work can be considered, the project still needs:

| Future Area | Required Before Implementation |
|---|---|
| Temporal Awareness | recall event write policy, temporal review placement, elapsed-time evidence rules |
| Recall Events | accepted write gate, payload/diff policy, validation invariants |
| Growth Lifecycle | promotion boundary, identity gate integration, no-execution validation |
| Reconstruction Reducer | accepted reducer contract, target-path capture policy, deterministic validation |
| Payload Capture | privacy/redaction policy, schema review, event compatibility plan |
| Subject Kernel / World Seed | identity boundary review, reconstruction path distinction, no runtime split |
| Exploration | signal schema, quarantine rules, anti-companion evaluation |

P67 does not approve any of these dependencies.

## P68-P80 Low-Risk Backlog

Only low-risk consolidation should continue:

- docs consistency pass;
- glossary deduplication;
- Chinese/English sync;
- README entrance optimization;
- phase index extension for P52-P67;
- concept map extension for P58-P66;
- open questions status update;
- risk register;
- architecture boundary refresh;
- RFC index;
- `DECISIONS.md` foundation decisions log;
- `RESEARCH_NOTES_INDEX.md`;
- `FOUNDATION_REVIEW_CHECKLIST.md` manual phase review gate.

Do not open new runtime capability phases merely to reach P80.

## Suggested Next Order

1. P68 RFC Index.
2. P69 Phase Index Extension.
3. P70 Concept Map Update.
4. P71 Open Questions Status Update.
5. P72 Risk Register.
6. P73 Architecture Boundary Refresh.
7. P74 Glossary Deduplication.
8. P75 README Entrance Optimization.
9. P76 Foundation Review Checklist.
10. P77 Decisions Log.
11. P78 Research Notes Index.
12. P79 Bilingual Consistency Pass.
13. P80 Final Foundation Maintenance Review.

This order is advisory. Skip or merge steps if they do not add clarity.

P76 is satisfied by [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md)
and its Chinese pair. The checklist is a manual review gate, not an automated
executor.

P77 is satisfied by [DECISIONS.md](./DECISIONS.md) and its Chinese pair. The
decisions log records project stance; it is not an approval engine.

## Completion Definition For Foundation Layer

The foundation layer is not complete because all ideas are implemented. It is
complete enough for a cycle when:

- stable principles are easy to find;
- open questions are triaged;
- blocked runtime work is visible;
- RFCs are indexed;
- bilingual docs agree on boundaries;
- future implementation cannot accidentally claim approval from review-only
  documents.

## Current Recommendation

Continue with low-risk consolidation. Do not enter runtime work. Do not connect
AstrBot. Do not productize. Do not implement growth, Temporal Awareness,
payload capture, reducer execution, or event compaction.
