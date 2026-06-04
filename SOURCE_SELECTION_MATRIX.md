# Source Selection Matrix

Chinese version: [SOURCE_SELECTION_MATRIX_ZH.md](./SOURCE_SELECTION_MATRIX_ZH.md)

Status: `P139`, `matrix`, `document-only`, `non-runtime`.

P139 defines source selection rules for future context package previews. It does
not implement retrieval, ranking, a builder, CLI command, model call, prompt
execution, state write, memory write, recall write, identity mutation, adapter
integration, tool execution, policy executor, or rebuild.

## Selection Principle

```text
source selection is explanation.
selection is not truth.
omission must be visible.
trust level must travel with the source.
```

## Pack Selection Matrix

| Pack | Preferred Sources | Include When | Omit When | Required Explanation |
|---|---|---|---|---|
| `identity_pack` | `FOUNDATION`, identity seed docs, architecture boundaries | Identity anchors or high gates are relevant. | Source is candidate, external, or identity-changing. | Explain protected anchor and mutation block. |
| `state_pack` | current phase index, observatory reports, readiness reviews | Current project status is needed. | Source is stale or not local/approved. | Explain status date and source class. |
| `task_pack` | roadmap, phase plan, review artifacts | Next-step or blocked-work context is needed. | The task implies automatic execution. | Explain candidate status and manual approval need. |
| `claim_pack` | RFCs, reviews, evidence maps | A claim needs citation or uncertainty. | Claim lacks provenance or is model-only. | Explain evidence level and review gate. |
| `memory_pack` | memory policy, stateful memory docs, source-backed refs | Memory semantics are relevant. | It would imply memory restoration or rewrite. | Explain retrieval is not continuity. |
| `boundary_pack` | boundary RFCs, risk register, no-write contracts | Any forbidden action is relevant. | Never omit global safety boundaries. | Explain blocked capabilities. |
| `temporal_pack` | temporal awareness, CTM RFC, coherence evaluation | Time, delay, review depth, or tension is relevant. | It would imply runtime or thought execution. | Explain symbolic/review-only status. |
| `capability_pack` | Tool-First RFC, capability boundary, risk reviews | Tool/procedure/evidence pressure is relevant. | It would imply authorization or execution. | Explain evidence is not authorization. |
| `response_strategy_pack` | LLM-as-resource future boundary, context package RFC, non-claims | A future model response needs guardrails. | Strategy would act as execution approval. | Explain model is resource, not subject. |

## Source Trust Matrix

| Trust Level | Meaning | Allowed Use |
|---|---|---|
| `trusted_foundation` | Stable project boundary or accepted foundation text. | Can anchor pack explanations. |
| `source_backed` | Whitelisted local doc or report with citation. | Can support previews. |
| `review_only` | Review/RFC language that does not authorize action. | Can route decisions to gates. |
| `candidate_only` | Proposed concept, next step, or unreviewed item. | Can appear only as candidate. |
| `quarantined` | External or untrusted material awaiting review. | Can be shown only as risk. |
| `omitted` | Relevant but excluded source. | Must include omission reason. |
| `blocked` | Source or action is outside allowed boundary. | Must show block reason. |

## Omission Reasons

Future previews should distinguish:

- `not_relevant`
- `stale`
- `not_approved_source`
- `external_or_untrusted`
- `identity_risk`
- `write_path_risk`
- `adapter_risk`
- `model_call_risk`
- `tool_execution_risk`
- `rebuild_risk`

Omission is part of the report, not a silent failure.

## CTM-Inspired Temporal Selection

Temporal sources may be selected only when the input or phase involves:

- elapsed time;
- resumed session;
- interruption;
- unresolved tension;
- delayed alignment;
- review depth;
- thought-trace boundary.

They must be labeled symbolic and review-only. They cannot justify temporal
events, recall events, thought loops, hidden traces, salience mutation, or
identity change.

## Tool-First Capability Selection

Capability sources may be selected only when the input or phase involves:

- tool candidate;
- procedure candidate;
- verification evidence;
- capability review;
- cautionary procedural memory;
- tool authorization boundary.

They must be labeled candidate/evidence/review only. They cannot justify tool
execution, tool promotion, dependency installation, tool-library mutation, or
subject growth.

## Future Test Expectations

If source selection is later implemented, tests should verify:

- every selected source has a reason;
- every omitted relevant source has a reason;
- trust level is present on every source;
- no quarantined source is promoted;
- boundary sources cannot be omitted when forbidden actions are relevant;
- temporal and capability sources remain review-only;
- no selection mutates state.

## Completion Statement

P139 turns source selection into a visible matrix. It prevents future context
packages from hiding trust, omission, or review boundaries behind retrieval
language.
