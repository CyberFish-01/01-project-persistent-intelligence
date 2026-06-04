# Post-Response Candidate Extraction RFC

Chinese version: [POST_RESPONSE_CANDIDATE_EXTRACTION_RFC_ZH.md](./POST_RESPONSE_CANDIDATE_EXTRACTION_RFC_ZH.md)

Status: `P145`, `RFC-only`, `document-only`, `non-runtime`.

P145 defines how future model output may be inspected for candidates after a
response. It does not implement extraction, model calls, response generation,
candidate storage, review lifecycle, event writes, memory writes, recall writes,
identity mutation, tool execution, policy executor, adapter integration, or
rebuild.

## Core Rule

```text
extraction is inspection.
inspection is not persistence.
candidate is not promotion.
model output remains untrusted.
```

## Candidate Types

Future extraction may identify:

- `memory_candidate`
- `claim_candidate`
- `task_update_candidate`
- `meaning_shift_candidate`
- `growth_candidate_review`
- `recall_event_candidate`
- `identity_claim_candidate`
- `temporal_review_candidate`
- `tool_candidate`
- `procedure_candidate`
- `capability_evidence_candidate`
- `quarantine_candidate`

All extracted items must be preview-only until manual review.

## Required Candidate Fields

Each extracted candidate should include:

- `candidate_type`
- `source_output_ref`
- `claim_text_or_summary`
- `why_detected`
- `trust_level`
- `risk_flags`
- `review_gate`
- `blocked_promotions`
- `preview_only: true`
- `persisted: false`
- `promoted: false`

## Candidate Routing

| Candidate | Review Gate | Default Outcome |
|---|---|---|
| memory candidate | memory review | preview only |
| claim candidate | claim review | evidence check |
| task update candidate | task review | manual planning |
| meaning shift candidate | growth/meaning review | no promotion |
| recall event candidate | recall write policy review | no write |
| identity claim candidate | identity high gate | reject or quarantine by default |
| temporal review candidate | temporal review | symbolic only |
| tool/procedure candidate | capability review | no execution |
| capability evidence candidate | tool authorization review | evidence only |
| quarantine candidate | quarantine review | containment |

## CTM-Inspired Temporal Extraction

Temporal extraction may notice:

- elapsed-time claims;
- delayed realization language;
- unresolved tension;
- coherence break language;
- review depth suggestions.

It must not write temporal events, recall events, thought traces, salience
changes, identity updates, or CTM runtime state.

## Tool-First Extraction

Capability extraction may notice:

- tool suggestions;
- reusable procedures;
- verification evidence;
- failed execution notes;
- capability improvement language.

It must not authorize tools, execute tools, promote tools, install dependencies,
write tool-library entries, or treat capability improvement as subject growth.

## Rejection And Quarantine

Candidate extraction should support rejection and quarantine, not only positive
routing.

Unsafe or low-provenance output should route to:

- `quarantine_candidate`
- `reject_as_prompt_contamination`
- `defer_pending_founder_review`
- `false_positive_review`

## Future Test Expectations

If implemented later, tests should verify:

- extracted candidates remain preview-only;
- no candidate is persisted or promoted;
- identity claims route to high gate;
- temporal candidates remain symbolic;
- capability candidates do not enable tools;
- quarantine candidates do not write storage;
- model output does not mutate state.

## Completion Statement

P145 defines post-response extraction as a review surface, not a write path. It
lets future model output be inspected without becoming memory, identity,
authority, growth, tool trust, or state.
