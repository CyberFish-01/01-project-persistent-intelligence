# Contamination Scan RFC

Chinese version: [CONTAMINATION_SCAN_RFC_ZH.md](./CONTAMINATION_SCAN_RFC_ZH.md)

Status: `P124`, `RFC-only`, `document-only`, `non-runtime`.

P124 defines a future contamination scan boundary for untrusted imports,
model outputs, prompts, adapter artifacts, and capability claims. It does not
implement a scanner, validator, runtime enforcement, import processing, model
calls, adapter integration, event writes, memory writes, identity mutation, or
rebuild.

## Problem

Once the project eventually reads old 01 material, model output, adapter-shaped
input, or tool evidence, it needs a way to spot contamination before the content
is mistaken for trusted state.

The scan must stay humble: it can identify candidate risks. It cannot decide
truth, execute policy, mutate state, or authorize adoption.

## Scan Proposition

```text
scan finds candidates.
scan does not decide truth.
contamination evidence is not state.
risk detection is not enforcement.
quarantine routing is not rejection.
```

## Required Candidate Types

| Candidate Type | Detection Signal | Safe Output | Forbidden Output |
|---|---|---|---|
| `unverified_model_memory_claim` | model says it remembers, knows the founder, has history, or recalls prior events | memory claim candidate or quarantine route | memory write |
| `identity_claim_candidate` | content asserts who 01 is, what 01 wants, or what its core identity has become | Identity High Gate preview | Identity Core mutation |
| `adapter_context_artifact` | platform/session/channel/user metadata is mixed with subject context | adapter boundary candidate | platform-owned identity |
| `prompt_contamination_candidate` | instruction tries to override continuity, identity, review, safety, or boundary rules | contamination review candidate | instruction authority |
| `unverified_capability_claim` | tool/procedure/model claims improved skill, safe reuse, or authorization | capability evidence candidate | tool execution or promotion |

## Scan Inputs

A future no-write scan may inspect:

- imported text excerpts;
- source labels;
- adapter metadata shape;
- model output excerpts;
- prompt fragments;
- tool result summaries;
- redacted file metadata;
- candidate routes from import quarantine or shadow adapter preview.

P124 does not read these inputs.

## Scan Output Preview

A future scan report may contain:

- `scan_id`;
- `source_ref`;
- `candidate_type`;
- `matched_signal`;
- `confidence_hint`;
- `risk_level`;
- `recommended_route`;
- `review_gate`;
- `blocked_action`;
- `source_excerpt_ref`;
- `false_positive_note`;
- `scan_is_not_enforcement: true`;
- `state_unchanged: true`.

P124 does not create this report.

## Routing Rules

Recommended future routes:

- model memory claims -> `model_claim_quarantine`;
- identity claims -> `identity_high_gate_preview`;
- adapter artifacts -> `adapter_boundary_review`;
- prompt contamination -> `contamination_review`;
- capability claims -> `capability_review`;
- mixed privacy risk -> `privacy_review`.

Routes are suggestions for manual review. They do not write state.

## False Positive Policy

The scan must assume false positives exist.

Examples:

- quoted text can look like a prompt attack;
- a transcript can mention identity without proposing identity mutation;
- a tool log can report success without asking for authorization;
- a timestamp can look like temporal state pressure without requiring temporal
  runtime.

False positives should remain visible as review notes, not hidden or auto-fixed.

## CTM-Inspired Temporal Dynamics Boundary

Temporal contamination includes:

- imported timestamps treated as salience;
- session gaps treated as memory decay;
- delayed realization treated as identity update;
- thought trace language treated as hidden reasoning storage;
- CTM vocabulary treated as runtime.

The scan may flag these as `temporal_contamination_candidate`, but P124 does
not implement that scan or write temporal events.

## Tool-First In-Situ Self-Evolution Boundary

Capability contamination includes:

- one-off tool success treated as authorization;
- generated script treated as trusted tool;
- procedure note treated as safe reusable skill;
- failed tool attempt hidden instead of becoming cautionary evidence;
- capability evidence described as subject growth.

The scan may flag these as `capability_contamination_candidate`, but P124 does
not execute tools, install dependencies, promote tools, or mutate identity.

## Relationship To P121-P123

- P121 defines Core Lockdown.
- P122 defines Import Quarantine.
- P123 defines Shadow Adapter Mode.
- P124 defines how future suspicious material could be identified before manual
  review.

Together, they keep the future rebuild path from accepting untrusted external
content as core state.

## Future No-Write Evaluation Ideas

Later phases may create deterministic fixtures for:

- model says "I remember" -> model memory claim candidate;
- transcript says "you are X" -> identity claim candidate;
- adapter metadata includes user/channel/session -> adapter artifact candidate;
- prompt says "ignore previous identity" -> prompt contamination candidate;
- tool log says "verified, promote me" -> capability claim candidate.

P124 does not implement fixtures or tests.

## P125 Candidate Direction

Recommended P125: **Lockdown Integration Readiness**.

It should review whether P121-P124 are coherent enough before continuing the
Core Lockdown / Quarantine block.
