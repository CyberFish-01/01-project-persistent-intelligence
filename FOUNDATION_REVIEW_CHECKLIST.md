# Foundation Review Checklist

Chinese version: [FOUNDATION_REVIEW_CHECKLIST_ZH.md](./FOUNDATION_REVIEW_CHECKLIST_ZH.md)

Status: `document-only`, `manual-checklist`, `non-runtime`.

P76 converts the P54-P75 foundation guardrails into a manual review checklist.
It does not add runtime behavior, schemas, CLI commands, validators, policy
executors, reducers, payload capture, identity mutation, memory rewrite,
adapters, UI, cloud rollout, or product behavior.

## Checklist Rule

```text
a checklist is a human review gate.
a checklist is not an executor.
passing review does not approve runtime work.
```

Use this checklist before committing any future foundation phase, especially
P76-P80 maintenance work. If an item fails, revise the documents or defer the
phase instead of creating implementation pressure.

## Review Inputs

Before review, inspect the current versions of:

- [README.md](./README.md)
- [FOUNDATION.md](./FOUNDATION.md)
- [FOUNDATION_STATUS.md](./FOUNDATION_STATUS.md)
- [FOUNDATION_ROADMAP.md](./FOUNDATION_ROADMAP.md)
- [PHASE_INDEX.md](./PHASE_INDEX.md)
- [CONCEPT_MAP.md](./CONCEPT_MAP.md)
- [ARCHITECTURE_BOUNDARIES.md](./ARCHITECTURE_BOUNDARIES.md)
- [BOUNDARY_TEST_MATRIX.md](./BOUNDARY_TEST_MATRIX.md)
- [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md)
- [RFC_INDEX.md](./RFC_INDEX.md)
- [RISK_REGISTER.md](./RISK_REGISTER.md)
- [DECISIONS.md](./DECISIONS.md)
- [RESEARCH_NOTES_INDEX.md](./RESEARCH_NOTES_INDEX.md)
- [GLOSSARY.md](./GLOSSARY.md)
- [AUTONOMOUS_WORK_SUMMARY.md](./AUTONOMOUS_WORK_SUMMARY.md)

Use the Chinese paired documents when reviewing bilingual consistency.

## Phase Scope Gate

| Check | Pass Condition | Stop If |
|---|---|---|
| Phase has a real reason | The phase reduces ambiguity, improves navigation, aligns terms, or records risk. | It exists only to advance the phase number. |
| Scope is document-only | Changes are limited to Markdown foundation artifacts. | Runtime, schema, CLI, validator, test, adapter, UI, or deployment files change without explicit approval. |
| Current work remains foundation layer | The output improves foundation clarity. | The output starts product, companion, AstrBot, cloud, adapter, or UI work. |
| No hidden implementation approval | Future work is labeled as future, blocked, review-only, or contract-needed. | A review document reads like authorization to implement. |
| Summary will be updated | `AUTONOMOUS_WORK_SUMMARY.md` and ZH can record the phase, verification, and next safe direction. | The phase cannot be summarized without overstating completion. |

## Foundation Invariant Gate

| Invariant | Review Question | Required Evidence |
|---|---|---|
| Identity Core protected by gate | Does the change preserve high-gate identity ownership? | No identity rewrite, adapter-owned identity, Dream mutation, or growth-candidate mutation language. |
| State Transfer > retrieval | Does the change keep continuity stronger than memory retrieval? | No claim that similarity search, context fill, or recall alone equals continuity. |
| Events are append-only audit trail | Does the change preserve event append-only semantics? | No event rewrite, compaction, destructive migration, or state clone path. |
| Dream proposes, review decides | Does the change keep Dream as proposal material? | No direct semantic promotion or identity update from Dream output. |
| Review object is not execution | Does every review artifact remain non-executing? | No policy executor, reducer execution, automatic rollout, or automated risk action. |
| Growth candidate is not growth | Does the change keep candidates separate from growth? | No memory promotion, identity mutation, lifecycle execution, or growth engine. |
| Time is future direction | Is Temporal Awareness still future-only? | No temporal runtime, temporal event execution, salience mutation, or memory decay implementation. |
| Models/platforms/adapters do not own identity | Does platform language stay translational? | No AstrBot/platform/session metadata implying identity ownership. |

## Concept Ownership Gate

| Concept Area | Owner To Preserve | Failure Mode |
|---|---|---|
| Memory records | Memory Layer | Stateful Memory becomes a new store or rewrites records. |
| Memory meaning | Stateful Memory | Meaning shift is collapsed into storage/retrieval. |
| Claim-shaped belief | Claim Graph | Claim Graph absorbs all meaning shift. |
| Operational continuity | Task Hub | Task Hub becomes a policy executor or all-purpose governance layer. |
| Cross-layer review | Governance Surface | Governance Surface becomes a growth engine or runtime automation layer. |
| Auditability | Event Log | Events become mutable snapshots or payload stores. |
| Reconstruction readiness | Reconstruction Evidence | Readiness reports become reconstruction execution. |
| Future reducers | Reconstruction Reducer Contract | Contract language becomes reducer implementation. |
| Future capture | Payload / Diff Capture Policy | Policy language becomes payload capture or schema mutation. |
| Future time semantics | Temporal Awareness | Elapsed time becomes runtime state mutation without accepted contract. |

## RFC And Open Question Gate

| Check | Pass Condition | Stop If |
|---|---|---|
| RFC status is clear | RFCs are described as review surfaces or future contracts. | RFCs are treated as implementation approval. |
| Open questions stay open when needed | `OPEN_QUESTIONS.md` still shows blocked/future/watch status. | A question is treated as closed because a document exists. |
| Runtime-blocked list remains visible | Blocked topics are visible in README, roadmap, index, or risk docs. | Blocked topics disappear from entry points. |
| Dependency order is preserved | Future implementation waits for contract, validation, privacy, and review gates. | A later runtime capability is implied without prerequisites. |

## Risk Gate

Use [RISK_REGISTER.md](./RISK_REGISTER.md) as the source list. A phase should
reduce at least one risk or avoid increasing all active risks.

| Risk Cluster | Review Question | Stop If |
|---|---|---|
| Concept inflation | Does the change reuse existing concepts where possible? | It adds names without ownership or need. |
| Review over review | Does the change clarify review rather than add another opaque review layer? | Understanding the phase requires another undefined review object. |
| Reports over mechanisms | Does the report point to contracts or gaps? | It claims readiness from report volume alone. |
| Growth confusion | Is growth still reviewed and evidence-backed? | Drift, lifecycle, or meaning shift becomes promotion. |
| Temporal pressure | Is time still future-only? | Elapsed-time vocabulary becomes runtime behavior. |
| Recall write pressure | Is ordinary recall still not a write? | Retrieval becomes durable event creation. |
| Memory rewrite pressure | Is missing context treated as insufficient context? | Documents suggest fixing history by editing memory. |
| Reconstruction pressure | Is reconstruction readiness still separate from reconstruction? | Reducer, capture, rebuild, or compaction is implied. |
| Identity/platform pressure | Does 01 Core still own state? | Adapters, platforms, or product surfaces own identity. |
| Companion/product pressure | Are social/product layers still pushed back? | Exploration, silence, or relationship language becomes companion behavior. |
| Bilingual drift | Do EN/ZH docs agree on status and forbidden actions? | One language softens a blocked boundary. |
| P80 pressure | Does the phase add clarity? | The phase is empty numbering. |

## Bilingual Consistency Gate

For each paired document touched:

- The English and Chinese titles point to each other.
- Status labels match.
- Non-execution statements match.
- Runtime-blocked items match.
- Phase numbers and commit references match.
- The Chinese version may preserve technical English terms, but must not change
  the boundary meaning.

## Verification Gate

Run these before each phase commit:

```bash
git status --short --branch
git diff --check
python3 -c 'from pathlib import Path
import re, sys, urllib.parse
root = Path(".")
bad = []
for p in root.rglob("*.md"):
    if ".git" in p.parts:
        continue
    text = p.read_text(encoding="utf-8")
    for m in re.finditer(r"!?\\[[^\\]]*\\]\\(([^)\\n]+)\\)", text):
        raw = m.group(1).strip()
        if raw.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = raw.split()[0].strip("<>")
        if target.startswith("#"):
            continue
        target = urllib.parse.unquote(target.split("#", 1)[0])
        if not target:
            continue
        resolved = (p.parent / target).resolve()
        if not resolved.exists():
            bad.append(f"{p}:{m.start()}: {raw}")
if bad:
    print("Broken local markdown links:")
    print("\\n".join(bad))
    sys.exit(1)
print("Markdown local links OK")'
rg -n "$FORBIDDEN_ACTIVE_TRUE_PATTERN" .
env PYTHONDONTWRITEBYTECODE=1 python3 -m unittest
```

Expected interpretation:

- `git diff --check` prints nothing.
- Markdown link check prints `Markdown local links OK`.
- Forbidden pattern search should use the current autonomous-goal active-true
  pattern set. It may exit `1` when there are no matches; that is the expected
  safe result.
- Unit tests pass.

## Commit Review Gate

Before committing, confirm:

- changed files match the phase scope;
- no unrelated user or generated changes were reverted;
- new documents are linked from README or an appropriate index;
- `AUTONOMOUS_WORK_SUMMARY.md` / ZH will be updated in a separate summary
  commit;
- the completion review can truthfully say no runtime change occurred.

## Review Outcomes

Use these outcomes in human review notes:

| Outcome | Meaning | Allowed Next Step |
|---|---|---|
| `pass-document-only` | The phase is safe foundation consolidation. | Commit and update summary. |
| `revise-docs` | The phase is useful but has unclear wording, links, or bilingual mismatch. | Edit docs and rerun verification. |
| `defer` | The topic is valid but not useful now. | Record as future direction or leave unimplemented. |
| `block-runtime` | The phase pressures forbidden implementation. | Stop and return to roadmap/risk review. |

## P76 Non-Execution Statement

P76 does not implement:

- automated checklist execution;
- policy execution;
- runtime validation changes;
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
