# Bilingual Consistency Review

Chinese version: [BILINGUAL_CONSISTENCY_REVIEW_ZH.md](./BILINGUAL_CONSISTENCY_REVIEW_ZH.md)

Status: `document-only`, `bilingual-consistency`, `non-runtime`.

P79 records a bilingual consistency pass for the foundation layer. It does not
add runtime behavior, schemas, CLI commands, validators, policy executors,
reducers, payload capture, identity mutation, memory rewrite, adapters, UI,
cloud rollout, or product behavior.

## Review Rule

```text
bilingual documents are paired boundary surfaces.
translation may preserve technical terms.
translation must not soften blocked actions.
```

P79 exists because the project now depends on both Chinese-first research notes
and English technical boundary language. If one language drifts, later work can
accidentally treat a future-only or review-only document as implementation
approval.

## Inspection Scope

The pass inspected:

- root Markdown documents and adapter README pairs;
- P54-P78 foundation consolidation artifacts;
- foundation entrance documents such as README, roadmap, checklist, RFC index,
  risk register, open questions, decisions, research notes index, glossary,
  phase index, concept map, and architecture boundaries;
- current autonomous work summaries.

`RESEARCH_NOTES_ZH.md` is intentionally preserved as a Chinese-only original
source note. It is not treated as a missing English pair.

Older historical/runtime references were checked as existing documentation
pairs, but were not mechanically normalized. Broad header churn in old files
would create noise without improving the current foundation boundary.

## Inspection Results

| Check | Result | Follow-up |
|---|---|---|
| Pair presence | All Markdown documents have expected English/Chinese pairs, except the intentional source-only `RESEARCH_NOTES_ZH.md`. | Keep paired edits as the default for future foundation work. |
| Reciprocal links | P54-P78 foundation artifacts and current entrance documents maintain reciprocal links. | Older historical/runtime references may be normalized later only if useful. |
| Status labels | Current foundation artifacts use aligned `document-only` and `non-runtime` status language. | Preserve matching status labels when adding future review artifacts. |
| Non-execution statements | Current foundation docs agree that review, RFC, checklist, roadmap, index, and risk language do not execute runtime behavior. | Keep non-execution statements explicit in both languages. |
| Blocked runtime terms | Core blocked topics remain visible across README, roadmap, RFC index, checklist, risk register, and boundary docs. | Treat any one-language weakening as a review failure. |
| Phase and summary alignment | `AUTONOMOUS_WORK_SUMMARY.md` tracks P54-P78 and will be updated after P79 commit. | Update both summary files after each phase commit. |

## Checked Areas

| Area | Main Documents | P79 Reading |
|---|---|---|
| Project entrance | [README.md](./README.md), [README_ZH.md](./README_ZH.md) | Stable/future/blocked status is visible to new readers in both languages. |
| Foundation route | [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md), [FOUNDATION_REVIEW_CHECKLIST.md](./FOUNDATION_REVIEW_CHECKLIST.md) | P68-P80 remains low-risk consolidation, and the checklist remains manual. |
| Governance and risk | [RFC_INDEX.md](./RFC_INDEX.md), [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md), [RISK_REGISTER.md](./RISK_REGISTER.md), [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md) | Review surfaces are not implementation approvals. |
| Traceability | [DECISIONS.md](./DECISIONS.md), [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md) | Decision and source-note records agree on accepted, deferred, blocked, and watch status. |
| Shared vocabulary | [GLOSSARY.md](./GLOSSARY.md), [CONCEPT_MAP.md](./CONCEPT_MAP.md), [PHASE_INDEX.md](./PHASE_INDEX.md) | Core terms preserve ownership boundaries across languages. |
| Work record | [AUTONOMOUS_WORK_SUMMARY.md](./AUTONOMOUS_WORK_SUMMARY.md) | Phase commits, verification, and remaining work should be mirrored after each phase. |

## Future Paired-Edit Policy

For future foundation documents:

- update English and Chinese files in the same phase;
- keep status labels identical;
- preserve technical English terms in Chinese when translation would blur the
  concept boundary;
- if the two versions conflict, use the stricter boundary until reconciled;
- avoid broad mechanical edits to older historical documents unless they reduce
  an active risk.

## Watch Items

| Risk | Why It Matters | Control |
|---|---|---|
| Bilingual boundary drift | A blocked action could appear softer in one language. | Compare non-execution and blocked-runtime lists before commit. |
| Loose term translation | Concepts such as growth, drift, review, and reconstruction can become broader than intended. | Keep glossary and concept map terms aligned. |
| Summary drift | One summary can miss a phase commit or verification result. | Update both autonomous summary files after the phase artifact commit. |
| Legacy normalization churn | Rewriting old headers can obscure meaningful foundation changes. | Normalize old docs only when the benefit is concrete. |
| Index overload | Too many links can make the entrance harder to scan. | Link new artifacts from the smallest useful set of entrances. |

## P79 Non-Execution Statement

P79 does not implement:

- automated bilingual checking;
- runtime validation changes;
- policy execution;
- Temporal Awareness runtime;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- payload capture;
- event schema mutation;
- reconstruction reducer execution;
- event compaction;
- companion, relationship memory, UI, AstrBot, adapter, cloud rollout, or
  product layer.
