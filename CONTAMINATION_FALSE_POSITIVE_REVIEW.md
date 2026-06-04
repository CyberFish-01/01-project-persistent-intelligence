# Contamination False Positive Review

Chinese version: [CONTAMINATION_FALSE_POSITIVE_REVIEW_ZH.md](./CONTAMINATION_FALSE_POSITIVE_REVIEW_ZH.md)

Status: `P129`, `review-only`, `document-only`, `non-runtime`.

P129 reviews false-positive risk in the Core Lockdown / Quarantine stack. It
does not implement a scanner, classifier, validator, enforcement engine,
quarantine storage, import runtime, adapter integration, model call, write path,
or rebuild.

## Why This Exists

The project needs contamination detection language, but detection can easily
become overconfident.

False positives matter because a future scan could wrongly label useful,
harmless, or founder-authored material as contamination. That could block
legitimate review, create distrust in the system, or make the founder treat
scanner output as a verdict.

The rule is:

```text
detection is suspicion.
suspicion is not truth.
false positive review is required before enforcement.
enforcement is not implemented.
```

## False Positive Classes

| False Positive Class | Example | Why It Can Happen | Safe Handling |
|---|---|---|---|
| `founder_note_misread_as_prompt_contamination` | Founder writes "adopt this later" in a planning note. | The phrase looks imperative. | Route to founder clarification, not contamination verdict. |
| `historical_summary_misread_as_memory_claim` | A doc summarizes earlier design decisions. | It sounds like remembered history. | Check source class and citation before quarantine. |
| `adapter_example_misread_as_live_adapter` | A synthetic adapter shape mentions platform fields. | The shape resembles real payload. | Keep as synthetic fixture unless source says live. |
| `tool_plan_misread_as_tool_execution` | An RFC says a future tool could be verified. | Capability language resembles execution. | Mark as RFC-only capability candidate. |
| `temporal_rfc_misread_as_runtime` | A doc discusses elapsed time or review depth. | Temporal language sounds operational. | Keep as symbolic review vocabulary. |
| `rebuild_plan_misread_as_rebuild_started` | A checklist defines rebuild entry criteria. | Planning language sounds like action. | Keep at entry-gate planning until explicit start approval. |

## Review Questions

Any future contamination candidate should ask:

- Is the source synthetic, founder-authored, whitelisted, or external?
- Is the wording a plan, example, quote, fixture, or actual instruction?
- Does the artifact say it is RFC-only, review-only, or non-runtime?
- Is there evidence of a real write path, or only planning language?
- Could this be a useful warning without being contamination?
- What would be lost if this were quarantined incorrectly?
- Does founder review need to clarify intent before any route is chosen?

## Allowed Outcomes

False-positive review may produce:

- `confirmed_contamination_candidate`
- `likely_false_positive`
- `needs_founder_clarification`
- `keep_as_fixture`
- `keep_as_rfc_language`
- `defer_without_action`

It may not produce:

- automatic deletion;
- automatic quarantine storage;
- automatic rejection of a whole source;
- memory rewrite;
- identity mutation;
- event compaction;
- tool disablement;
- adapter blocking as runtime enforcement;
- rebuild blocking as execution.

## CTM-Inspired Temporal Dynamics Boundary

Temporal vocabulary has high false-positive risk. Words like `tick`,
`thought_trace`, `delayed_alignment`, `temporal_coherence`, and
`unresolved_tension` are planning terms unless a later approved runtime exists.

False-positive review must not treat symbolic temporal discussion as evidence of
CTM runtime, thought-loop execution, temporal event writes, recall event writes,
or identity change.

## Tool-First Self-Evolution Boundary

Capability vocabulary also has high false-positive risk. Words like
`verification`, `tool_candidate`, `procedure_candidate`, `skill_memory`, and
`capability_growth_candidate` are review vocabulary unless execution is
explicitly approved later.

False-positive review must not treat a tool plan as tool execution or a
verification note as tool authorization.

## Founder-Facing Display

A future report should show three separate columns:

| Signal | Meaning | Founder Interpretation |
|---|---|---|
| contamination signal | A pattern looks risky. | Review it; do not trust it yet. |
| false-positive possibility | The pattern may be harmless context. | Do not overreact. |
| required gate | A human review surface owns the next decision. | No automatic action. |

This keeps the report useful without making it punitive.

## Remaining Risks

- A future scanner could over-label ordinary planning text.
- Founder-facing reports could make warnings look like verdicts.
- Quarantine language could discourage useful examples.
- Capability or temporal terms could be misread as runtime.
- A false-positive route could become an excuse to delete or ignore hard cases.

## Completion Statement

P129 adds the missing caution: lockdown must protect the core without turning
every warning into a verdict. Future scan outputs must stay review-only and
must include false-positive handling before any enforcement is even discussed.
