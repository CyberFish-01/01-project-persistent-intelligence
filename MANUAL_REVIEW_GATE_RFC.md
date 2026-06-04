# Manual Review Gate RFC

Chinese version: [MANUAL_REVIEW_GATE_RFC_ZH.md](./MANUAL_REVIEW_GATE_RFC_ZH.md)

Status: `P146`, `RFC-only`, `document-only`, `non-runtime`.

P146 defines the manual review gate that must stand between future candidates
and any durable state change. It does not implement review lifecycle, approval
storage, event writes, memory writes, recall writes, identity mutation, growth
execution, tool execution, policy executor, adapter integration, model calls, or
rebuild.

## Core Rule

```text
manual review is gate.
gate is not approval.
approval is not write execution.
write policy must exist before write.
```

## Gate Purpose

The manual review gate prevents preview candidates from becoming durable state
because they are plausible, useful, emotionally salient, or model-generated.

It creates a place where the founder can decide whether something deserves a
later write-policy path.

## Review Gate Types

| Gate | Owns | Default Decision |
|---|---|---|
| memory review | memory-like candidates | no write |
| claim review | factual/project claims | evidence check |
| task review | task update candidates | manual planning |
| identity high gate | identity-bearing claims | reject or quarantine by default |
| growth review | meaning shift/growth candidates | no promotion |
| recall policy review | recall event candidates | no write |
| temporal review | elapsed-time and coherence cues | symbolic only |
| capability review | tool/procedure/capability candidates | no execution |
| quarantine review | untrusted/external/model output | containment |
| rebuild checkpoint | migration/rebuild pressure | blocked until final verification |

## Required Review Questions

Every gate should ask:

- What is the source?
- What is the trust level?
- What evidence supports it?
- What would change if accepted?
- What boundary could be violated?
- Is there a lower-risk outcome?
- Does a write policy exist for this type?
- Does founder approval explicitly cover this action?

## Allowed Outcomes

Manual review may produce:

- `reject`
- `keep_preview_only`
- `keep_quarantined`
- `defer_pending_evidence`
- `route_to_lower_risk_note`
- `route_to_future_write_policy`

It may not directly produce:

- state write;
- memory write;
- recall event write;
- identity mutation;
- growth promotion;
- tool execution;
- tool authorization;
- adapter integration;
- rebuild start.

## Lowest-Risk Future Write

The first possible future write class, if later approved, should be:

- founder decision note;
- review note;
- low-risk planning note.

Even that requires a later explicit write policy and is not authorized by P146.

## CTM-Inspired Temporal Gate

Temporal review may consider elapsed time, interruption, unresolved tension,
delayed alignment, and review depth. It must not write temporal events, recall
events, thought traces, salience changes, CTM runtime state, or identity
updates.

## Tool-First Gate

Capability review may consider tool candidates, procedure candidates,
verification evidence, and cautionary procedural memory candidates. It must not
execute tools, promote tools, authorize tools, install dependencies, mutate tool
libraries, or claim subject growth.

## Future Test Expectations

If implemented later, tests should verify:

- every candidate routes to a gate;
- gate output remains non-persistent unless a later write policy exists;
- identity and recall gates default to no write;
- temporal and capability gates keep forbidden actions false;
- approval alone cannot write state;
- missing gate causes fail-closed output.

## Completion Statement

P146 defines manual review as the necessary human gate before any future durable
change. It explicitly keeps review separate from approval, and approval separate
from write execution.
