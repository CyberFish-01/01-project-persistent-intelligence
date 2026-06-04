# Rebuild Entry Gate Checklist

Chinese version: [REBUILD_ENTRY_GATE_CHECKLIST_ZH.md](./REBUILD_ENTRY_GATE_CHECKLIST_ZH.md)

Status: `P148`, `checklist`, `document-only`, `non-runtime`.

P148 defines the checklist that must be satisfied before local 01 rebuild can
even be considered. It does not run verification, start rebuild, read old 01,
write state, migrate memory, connect adapters, call models, execute tools, run
reducers, compact events, or mutate identity.

## Readiness Distinction

```text
ready for verification is not ready for rebuild.
ready for rebuild requires verification evidence and founder checkpoint.
```

P148 only defines gates.

## Required Gates

| Gate | Requirement | Evidence Needed |
|---|---|---|
| git cleanliness | Worktree clean after final prep. | `git status --short` empty |
| format check | No whitespace diff errors. | `git diff --check` passes |
| markdown links | Local Markdown links resolve. | link check passes |
| forbidden search | No forbidden active pattern. | forbidden search no matches |
| unit tests | Existing tests pass. | `python3 -m unittest` passes |
| phase index | PHASE_INDEX covers latest phase. | P154 row present later |
| README status | README reflects current phase. | README / ZH updated |
| RFC index | New RFC/review docs indexed. | RFC_INDEX / ZH current |
| source safety | No old 01 read occurred. | source boundary statement |
| no-write proof | No formal state/memory/event mutation. | before/after evidence |
| model boundary | No LLM call occurred. | command audit |
| adapter boundary | No AstrBot/external adapter connection. | boundary audit |
| tool boundary | No tool execution/promotion. | boundary audit |
| temporal boundary | No temporal/CTM runtime. | boundary audit |
| founder checkpoint | Founder explicitly approves rebuild start. | future manual approval |

## Current Expected Status

At P148, the expected status is:

- documentation gates are being prepared;
- verification suite may be planned later;
- rebuild is not approved;
- old 01 is not read;
- no migration is executed.

## Blockers For Rebuild

Rebuild must remain blocked if:

- any test fails;
- any forbidden pattern appears;
- markdown links fail;
- worktree is dirty without explanation;
- source trust is unclear;
- old 01 material has not been quarantined;
- founder checkpoint is missing;
- verification report is missing;
- rebuild scope is ambiguous.

## CTM And Tool-First Gates

The entry gate must confirm:

- CTM-inspired work remains symbolic and review-only;
- no thought loop or temporal runtime exists;
- Tool-First work remains candidate/evidence/review only;
- no automatic tool execution or promotion exists.

## Completion Statement

P148 defines the entry checklist for future local rebuild. It does not make the
project rebuild-ready; it defines what later evidence must prove.
