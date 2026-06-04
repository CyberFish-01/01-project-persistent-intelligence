# Thought Trace Storage Policy RFC

Chinese version: [THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md)

Status: `document-only`, `policy-rfc`, `non-runtime`.

P84 defines storage boundaries for any future `thought_trace`-like artifact. It
does not implement trace storage, capture private reasoning, expose hidden
chain-of-thought, execute deliberation ticks, run a thought loop, write recall
events, mutate Identity Core, rewrite memory, execute growth lifecycle, or add
companion, UI, AstrBot, adapter, cloud, or product behavior.

## Policy Rule

```text
a thought trace, if ever stored, is an auditable review artifact.
a thought trace is not hidden chain-of-thought.
a thought trace is not model-internal state.
a thought trace is not proof of consciousness.
```

## Problem

P81 introduced `thought_trace` as a possible future vocabulary for how review
state evolved. P82 made it testable only as simulated review-step summaries. P83
defined deliberation ticks as review-planning units, not runtime thoughts.

The remaining risk is that future work may treat "trace" as permission to store
private model reasoning, model internals, hidden chain-of-thought, or
pseudo-consciousness artifacts. P84 exists to block that interpretation before
thin harness planning begins.

## Storage Boundary

| Item | Future Storage Stance | Why |
|---|---|---|
| public review summary | allowed candidate, after future schema | Can explain review outcome without exposing private reasoning. |
| evidence references | allowed candidate, after future schema | Supports audit and reconstruction evidence. |
| boundary flags | allowed candidate, after future schema | Shows which forbidden boundary shaped review. |
| review depth reason | allowed candidate, after future schema | Explains why shallow, normal, deep, or blocked review was suggested. |
| unresolved questions | allowed candidate, after future schema | Preserves what still requires human or gate review. |
| hidden chain-of-thought | forbidden | Private reasoning is not a durable project artifact. |
| model internal activations or latent state | forbidden | 01 Core is not inspecting neural state or implementing CTM. |
| private model reasoning transcript | forbidden | It would confuse review evidence with internal cognition. |
| consciousness or inner-experience claims | forbidden | The project must not use trace language as pseudo-cognition. |

## Allowed Future Trace Shape

This is policy vocabulary only, not a schema and not implemented.

```text
thought_trace_candidate:
  candidate_id
  source_event_refs
  review_depth
  review_summary
  evidence_refs
  boundary_flags
  unresolved_questions
  reviewer_or_gate_ref
  storage_decision
```

The allowed shape records the review surface, evidence, and boundary outcome.
It must not record hidden chain-of-thought, model internals, private reasoning
text, or deliberation tick execution.

## Non-Storable Categories

The following must remain non-storable unless a future explicit policy says
otherwise, and even then hidden model reasoning remains forbidden:

- hidden chain-of-thought;
- raw private reasoning transcripts;
- model internal activations;
- latent temporal state claims;
- generated "mind state" narratives;
- simulated consciousness reports;
- unreviewed tick-by-tick deliberation logs;
- prompt contamination framed as self-knowledge;
- trace records that imply identity update or memory rewrite.

## Relationship To Deliberation Ticks

P83 defines deliberation ticks as review-planning vocabulary. P84 adds that a
future trace may summarize review questions and evidence references, but must
not persist the tick-by-tick private reasoning that produced an answer.

Allowed:

- "candidate required deep review because evidence was ambiguous";
- "Identity Gate was required because an anchor was pressured";
- "review stopped because a boundary flag was hit".

Forbidden:

- "the model's hidden reasoning was stored";
- "the trace proves the system thought internally";
- "the tick sequence was executed as runtime cognition";
- "trace storage created a memory, recall event, or identity change".

## Relationship To Reconstruction

Future traces may become reconstruction evidence only if they are review
artifacts with stable references and accepted capture policy. They are not
reconstruction reducers, event compaction, memory contents, or identity state.

Until future contracts exist, `thought_trace` remains a candidate evidence
surface, not part of replay or rebuild.

## Relationship To Thin Harness

A future thin interaction harness may preview trace candidates by showing:

- which evidence references were considered;
- which boundary flags were triggered;
- which review depth was suggested;
- which unresolved questions remain;
- whether the trace candidate should be stored, deferred, or discarded.

P84 does not implement that harness and does not create a storage backend.

## Anti-Pseudocognition Boundary

P84 forbids:

- claiming a trace proves consciousness, sentience, or inner experience;
- equating trace summaries with real thoughts;
- equating symbolic review summaries with neural synchronization;
- storing hidden chain-of-thought or private model reasoning;
- using `thought_trace` language to bypass review-only boundaries;
- treating trace existence as evidence for identity update, memory rewrite, or
  growth promotion.

## Relationship To Existing Artifacts

| Artifact | Relationship |
|---|---|
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | Introduces `thought_trace` as a CTM-inspired future concept; P84 narrows storage boundaries. |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | Treats trace only as simulated review-step summaries and evidence references. |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | Keeps ticks as review planning; P84 prevents tick traces from becoming thought-loop storage. |
| [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) | Future traces may be evidence only after reducer contracts define whether they are replayable. |
| [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | Future trace storage would need capture policy before any durable payload exists. |
| [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | P84 closes one ambiguity but keeps runtime and storage implementation blocked. |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | P84 responds to pseudo-cognition, concept inflation, and premature runtime risks. |

## Open Questions

- Should trace candidates be stored at all, or remain ephemeral preview output?
- If stored later, are traces events, report artifacts, or governance records?
- What redaction policy is required for user-provided sensitive content?
- Should trace candidates be linked to review queues without becoming lifecycle
  execution?
- Can reconstruction use trace summaries without depending on private reasoning?
- Who or what can approve a trace storage decision?

## P85 Candidate Direction

P85 may define a Thin Interaction Harness RFC. It should use P84 boundaries to
ensure harness previews can explain review surfaces without storing hidden
reasoning, executing thought loops, or creating product behavior.

## P84 Non-Execution Statement

P84 does not implement:

- trace storage;
- hidden chain-of-thought capture;
- private model reasoning persistence;
- model internal trace capture;
- deliberation tick execution;
- thought loop execution;
- Temporal Awareness runtime;
- CTM runtime;
- model training;
- new dependencies;
- temporal event writes;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- policy execution;
- reconstruction reducer execution;
- event compaction;
- companion, UI, AstrBot, adapter, cloud rollout, or product layer.
