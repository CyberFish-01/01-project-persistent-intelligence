# Theory Synthesis and Next Plan

Chinese version: [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md)

This document synthesizes the current 01 Core foundation, the Cognitive OS reference direction, and external theory that is useful for the next engineering loop.

Its purpose is not to turn 01 Project into a philosophy or consciousness claim.

Its purpose is to answer:

> What is still missing from the engineering foundation, which theories give useful structure, and what should the next implementation loop build?

## 1. Current Engineering State

01 Core currently has:

- structured state runtime;
- durable memory metadata: provenance, lifecycle, update history;
- candidate memory store;
- Dream artifacts, rubrics, proposals, and conflict records;
- adapter registry, session policy, and event deduplication;
- import batches, import deduplication, and conservative sensitive filtering;
- candidate review governance;
- memory lifecycle action execution;
- audit, trace, and snapshot metadata;
- foundation evaluation.

The current boundaries remain:

- 01 Core owns state;
- adapters translate platforms;
- platforms do not own identity;
- Dream creates proposals, not direct Identity Core rewrites;
- imported memory defaults to staged;
- identity memory does not use generic lifecycle actions and requires a high gate.

## 2. Current Gaps

### 2.1 Evaluation Is Not Experimental Enough

The current foundation evaluation protects invariants, but it is not yet a full experiment harness.

Gaps:

- scenario evaluation now has deterministic local rule baselines, but not separate baseline agents;
- quantitative metrics are still local and rule-derived;
- replay now builds a target-path transition projection, but not a full object-level state rebuild;
- rollback preview reports affected paths and projected impact, but remains non-mutating;
- long-gap continuity still needs broader endurance-style tests.

### 2.2 Context Builder Is Still Shallow

The current context package can recover anchors and a small set of active memories.

Gaps:

- no activation policy by task, relationship, risk, recency, and lifecycle status;
- limited privacy-aware selection;
- no source attribution budget;
- no explanation for why a state item enters current context.

### 2.3 Conflict And Belief Revision Are Still Rule-Based

Dream can detect identity overwrite, false memory, stale preference, roleplay boundary, and imported memory conflicts.

Gaps:

- no explicit claim graph;
- no reason / dependency record;
- no belief revision policy;
- no layered conflict and evidence model;
- no resolved conflict lifecycle.

### 2.4 Relationship / Project / Task Hub Are Still Seed-Level

The schema has `relationship_map` and `project_map`, but runtime behavior is mostly memory and adapter centered.

Gaps:

- user-specific memory is not systematic enough;
- cross-user privacy boundary needs stronger tests;
- active project plans are not yet executable task state;
- blocker / next-action update API does not exist;
- relationship conflict has not entered Dream review.

### 2.5 Identity Update Gate Is Not Implemented

Identity Core is protected, but there is not yet an approvable identity update flow.

Gaps:

- high gate schema;
- identity proposal review;
- multiple-evidence requirement;
- non-claims check;
- rollback / snapshot policy;
- identity drift metrics.

### 2.6 Procedural Memory Is Not In The System Yet

The memory layer distinguishes imported, episodic, candidate, semantic, identity, and archived memory.

Gaps:

- no procedural habits;
- no action policy;
- no tool-use skill memory;
- no abstraction from repeated successful behavior into workflow policy.

## 3. External Theory Selection

### 3.1 LLM Agents And Long-Term Memory

#### Generative Agents

Source: <https://arxiv.org/abs/2304.03442>

Useful points:

- observation -> reflection -> planning;
- experience can be recorded in natural language;
- reflection can abstract specific experiences into higher-level memories;
- behavior depends on memory retrieval and planning.

Implications for 01:

- Dream Engine should continue using reflection and proposal output;
- 01 should not merely optimize believable simulation;
- evaluation should focus on continuity, audit, and identity stability.

#### MemGPT

Source: <https://arxiv.org/abs/2310.08560>

Useful points:

- context window can be treated as limited RAM;
- external memory tiers resemble an OS memory hierarchy;
- long-term state must be explicitly moved into and out of context.

Implications for 01:

- Context Builder should become a core module;
- the state transfer package should be a bounded memory page, not arbitrary summary concatenation;
- lifecycle actions should affect future activation.

#### ReAct / Reflexion

Sources:

- <https://arxiv.org/abs/2210.03629>
- <https://arxiv.org/abs/2303.11366>

Useful points:

- reasoning and acting should interleave;
- feedback can become reusable verbal memory;
- self-reflection after failure can improve later behavior.

Implications for 01:

- Task Hub should record action trace and failure reflection;
- Dream should consolidate action strategy, not only facts;
- procedural memory is needed later.

### 3.2 AI Logic: Belief Revision And Truth Maintenance

#### Truth Maintenance System

Source: <https://www.sciencedirect.com/science/article/pii/0004370279900080>

Useful points:

- beliefs should record reasons and dependencies;
- contradictions require revising a belief set by dependency structure;
- reasons support explainable action.

Implications for 01:

- `open_conflicts` should become claim / reason / dependency structures;
- false memory detection should not remain text-rule only;
- every semantic memory should be able to answer why it is believed.

#### AGM Belief Revision

Source: <https://arxiv.org/abs/2112.13557>

Useful points:

- revision should preserve minimal change;
- new information should not rewrite the whole belief set freely;
- belief change can be policy-governed.

Implications for 01:

- identity update gate should use minimal-change rules;
- preference change should preserve old provenance instead of overwriting;
- conflict resolution should generate patches, not global rewrites.

### 3.3 Nervous System And Memory Consolidation

#### Sleep / Systems Consolidation

Source: <https://pmc.ncbi.nlm.nih.gov/articles/PMC3278619/>

Useful points:

- new memories are reactivated;
- consolidation redistributes temporary memory into longer-term systems;
- consolidation is reorganization, not copying.

Implications for 01:

- Dream Engine needs input manifest and output artifact;
- consolidation should preserve input trace;
- Dream may create semantic candidates but must not rewrite identity directly.

#### Complementary Learning Systems

Source: <https://stanford.edu/~jlmcc/papers/PublicationFiles/90-99_Add_To_ONLINE_Pubs/McClelland1998ComplementaryLearningSystems.pdf>

Useful points:

- fast learner handles concrete episodes;
- slow learner handles general knowledge;
- replay and consolidation reduce catastrophic overwriting.

Implications for 01:

- episodic -> candidate -> semantic -> identity is the right speed hierarchy;
- identity update must be slower;
- evaluation should measure the stability-plasticity tradeoff.

### 3.4 Neural Networks And Continual Learning

#### Elastic Weight Consolidation / Catastrophic Forgetting

Source: <https://pubmed.ncbi.nlm.nih.gov/28292907/>

Useful points:

- sequential learning can damage old tasks;
- important knowledge needs protection;
- stability-plasticity is central to long-term learning.

Implications for 01:

- state growth is safer than weight growth at the current stage;
- stale memory and rigidity must still be measured;
- lifecycle action should support stability-plasticity, not only cleanup.

### 3.5 Psychology: Narrative Identity And Self-Memory System

#### Narrative Identity

Source: <https://journals.sagepub.com/doi/pdf/10.1177/0276236618756704>

Useful points:

- identity is an evolving life story;
- self-narrative organizes past, present, and future into unity and purpose;
- identity is not a list of facts.

Implications for 01:

- Identity Core should include narrative summary, but evidence-backed;
- life history must be generated from real state transitions;
- fictional backstory should not be imported as lived experience.

#### Self-Memory System

Source: <https://pmc.ncbi.nlm.nih.gov/articles/PMC2834574/>

Useful points:

- autobiographical memory and working self support goal-directed activity;
- systems need both self-coherence and adaptive correspondence;
- memory serves goals as well as self-continuity.

Implications for 01:

- relationship, project, and task state should enter Context Builder;
- memory is not an isolated store;
- state transfer package should show how current goals connect to past state.

#### Metacognition and Source Monitoring

Sources:

- [Metacognition and Confidence: A Review and Synthesis](https://pubmed.ncbi.nlm.nih.gov/37722748/)
- [Source monitoring](https://pubmed.ncbi.nlm.nih.gov/8346328/)
- [Source monitoring 15 years later: what have we learned from fMRI about the neural mechanisms of source memory?](https://pubmed.ncbi.nlm.nih.gov/19586165/)

Useful points:

- metacognition separates first-order task content from second-order confidence and error monitoring;
- source monitoring distinguishes whether a memory came from perception, imagination, inference, or another source;
- confidence, evidence, and origin are not the same thing.

Implications for 01:

- reflection log should carry source_ids, evidence, and confidence separately;
- verification should be a second-order pass, not just a restatement of the original lesson;
- policy-adjacent safeguards should consult reflection evidence, but not automatically execute workflow policy.

### 3.6 Consciousness-Related Theories As Functional Analogies Only

#### Global Neuronal Workspace

Source: <https://pubmed.ncbi.nlm.nih.gov/21521609/>

Useful points:

- local processes compete for global broadcast;
- broadcast information can be used by many systems;
- this is a useful analogy for context activation.

Implications for 01:

- Context Builder can act as a workspace selector;
- this does not imply consciousness;
- it is only an explainable state activation mechanism.

#### Free Energy / Active Inference

Source: <https://www.nature.com/articles/nrn2787>

Useful points:

- agents reduce uncertainty through prediction, action, and learning;
- attention, salience, and control state can be related;
- goal-directed behavior maintains stable state ranges.

Implications for 01:

- affective_state can remain a functional appraisal layer;
- salience scoring should include uncertainty, risk, and goal relevance;
- active intent should drive state selection.

### 3.7 Engineering: Event Sourcing

Source: <https://www.martinfowler.com/eaaDev/EventSourcing.html>

Useful points:

- every state change is stored as an event;
- event logs can reconstruct state;
- this fits audit, debug, and retroactive correction.

Implications for 01:

- audit, trace, and update_log are the right direction;
- current state view should later be separated from append-only event log;
- rollback should gradually move from metadata-only toward replayable events.

## 4. Theory To Engineering Map

| Source | Module | Next engineering need |
|---|---|---|
| MemGPT / OS memory | Context Builder | Bounded, policy-driven state activation |
| Event Sourcing | StateStore | Stronger append-only event log and replay/rollback |
| TMS / AGM | Conflict system | Claim graph, reason dependencies, minimal-change patch |
| Sleep consolidation / CLS | Dream Engine | Input manifest, candidate review, slow identity gates |
| Narrative Identity / SMS | Identity + Task Hub | Identity story grounded in state transitions |
| Metacognition / Source monitoring | Reflection log + verification | Track confidence, source, and later verification separately |
| ReAct / Reflexion | Task Hub + procedural memory | Action trace, failure reflection, workflow candidates |
| Continual Learning | Evaluation | Stability-plasticity, stale memory, overwrite analogs |
| Global Workspace | Context Builder | Explainable state activation |
| Active Inference | Salience / affective state | Salience from uncertainty, risk, and goal relevance |

## 5. Next Plan

### P7 Evaluation Harness v0.2

Goal: expand foundation checks into scenario evaluation.

Status: implemented as a first local v0.2 pass.

Executable items:

1. add scenario runner - done;
2. add Interrupted Project - done;
3. add Multi-User Boundary - done;
4. add Lifecycle Retrieval Suppression - done;
5. add baseline metadata - done;
6. output metrics summary - done;
7. sync documentation - done.

Acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P8 Context Builder v0.2

Goal: turn context package into explainable state activation.

Status: implemented as a first local v0.2 pass.

Executable items:

1. context selection policy - done;
2. lifecycle-aware retrieval - done for active/staged vs archived/discarded/quarantined;
3. task-aware activation - done with simple deterministic term overlap;
4. relationship-aware activation - done for current-user visibility and cross-user privacy suppression;
5. source attribution - done;
6. activation trace - done.

Remaining gaps:

- no vector retrieval;
- no independent baseline-agent comparison;
- no claim graph dependency model;
- no tunable policy file;
- no activation trace persistence outside the context response.

### P9 Conflict / Claim Graph

Goal: move from rule detection to reason maintenance.

Status: implemented as a first local v0.7 pass.

Executable items:

1. claim schema - done;
2. claim provenance - done;
3. contradiction links - schema placeholder only;
4. resolution lifecycle - done as unresolved/review-required metadata;
5. minimal-change patch proposal - done as resolution metadata, not execution.

Recommended immediate scope:

1. add `claim_graph` to state schema as an append-friendly structure;
2. map existing `open_conflicts` into claim nodes with evidence ids;
3. let false-memory and stale-preference Dream conflicts create claim nodes;
4. add validation that every claim has provenance and status;
5. add a scenario check that conflict resolution does not mutate semantic or identity memory without review.

Implemented result:

- `claim_graph` is now a top-level state object;
- legacy `open_conflicts` migrate into claim nodes;
- Dream false-memory and stale-preference conflicts create claim nodes;
- validation requires claim evidence, provenance, status, and resolution metadata;
- scenario evaluation checks claim provenance and prevents unreviewed semantic / identity mutation.

Remaining gaps:

- no real contradiction/support/dependency links yet;
- no claim resolution command;
- no minimal-change patch executor;
- no review workflow for closing claims;
- no baseline comparison for false claim rate.

### P10 Task Hub / Procedural Memory

Goal: let 01 preserve action structure, not only facts.

Status: implemented as a first local v0.8 pass.

Executable items:

1. active task state - first pass done;
2. action trace - first pass done;
3. failure reflection - moved to P17 and implemented as a first pass;
4. workflow candidate - first pass done;
5. procedural memory review - moved to P16 and implemented as a first pass.

Recommended immediate scope:

1. add a `task_hub` top-level state object;
2. migrate `working_state.current_plan` into active task items without removing the legacy field;
3. record action trace entries when CLI/API interactions, Dream runs, reviews, and lifecycle actions occur;
4. let Dream propose procedural candidates from repeated successful actions;
5. add scenario evaluation for interrupted task resume with action history and next action preservation.

Implemented result:

- `task_hub` is now a top-level state object;
- `working_state.current_plan` migrates into active/completed/blocked task items while retaining the legacy field;
- real state mutations append to `task_hub.action_trace`, while non-mutating dry-runs do not;
- Dream proposes `procedural_candidates` from repeated successful workflows;
- scenario evaluation adds `task_hub_action_resume`, checking active task, next action, action history, and procedural candidate preservation.

Remaining gaps:

- no workflow policy executor yet;
- action trace is currently a runtime trace summary, not a fully replayable action log.

### P11 Identity Update Gate

Goal: allow evidence-backed slow identity growth while protecting Identity Core.

Status: implemented as a first local v0.9 pass.

Executable items:

1. identity proposal schema - done;
2. high gate review - first pass done;
3. non-claims check - first pass done;
4. evidence threshold - done;
5. rollback snapshot - metadata-only done;
6. drift metric - first pass done.

Implemented result:

- `identity_update_gate` is now a top-level state object;
- identity proposals keep gate_result, non_claims_check, drift_score, and evidence;
- high gate requires at least 3 supporting evidence ids;
- non-claims violations and excessive drift scores block approval;
- approval appends `identity_memory` and does not directly patch `identity_core`;
- scenario evaluation adds `identity_update_gate_review`.

Remaining gaps:

- rollback is still metadata-only;
- drift metric is still a deterministic heuristic;
- no identity_core patch proposal executor yet;
- no deep claim_graph dependency integration with identity proposals yet;
- no human review UI yet.

### P12 Event Log / Replay / Rollback

Goal: move audit from "records exist" toward a replayable transition ledger.

Status: implemented as a first local v1.0 pass.

Executable items:

1. append-only `events.jsonl` - done;
2. event envelope linking trace, audit event, and update_log entry - done;
3. `replay-events` CLI consistency check - done;
4. `rollback-preview <snapshot_id>` CLI - done metadata-only;
5. scenario evaluation for event replay and rollback preview - done.

Implemented result:

- completed runtime traces with state mutations now write state transition events;
- dry-run preview does not write state events;
- replay validates event `update_id` references, reports coverage, and builds a target-path transition projection;
- rollback preview links snapshot metadata to affected events, affected state paths, and projected impact without mutating state;
- scenario evaluation adds `event_log_replay_rollback`.

Remaining gaps:

- replay projection does not reconstruct full object-level state from an empty seed yet;
- pre-P12 updates may be uncovered and are reported as coverage gaps;
- rollback is still preview-only;
- event schema is deterministic but still coarse;
- no event compaction or retention policy yet.

### P13 Dream Artifact Package

Goal: make each Dream run inspectable as a durable review package.

Status: implemented as a first local v1.0 pass.

Executable items:

1. artifact version and package completeness flags - done;
2. input manifest with source item summaries - done;
3. local PROV-style provenance block - done;
4. proposal index and review queue - done;
5. candidate-only patch diff - done;
6. decision log and rollback affected ids - done;
7. scenario evaluation for Dream artifact package - done.

Implemented result:

- Dream artifacts now include input manifest, provenance, observations, proposal index, review queue, patch diff, decision log, rollback metadata, and package completeness;
- validation checks Dream artifact package fields when artifacts are available;
- scenario evaluation adds `dream_artifact_package`;
- Dream remains candidate/review-only and does not directly write active semantic memory or Identity Core.

Remaining gaps:

- no human review UI yet;
- proposal approval is still handled through separate CLI commands;
- artifact package does not yet include full text snapshots of every input;
- no retention / compaction policy for artifact history;
- claim resolution is still shallow.

### P14 Claim Graph v0.2 / Belief Revision

Goal: make conflicts reviewable as claim/reason/dependency units.

Status: implemented as a first local v0.2 pass.

Executable items:

1. claim graph version, policy, and review decision store - done;
2. support/contradiction/dependency links - first pass done;
3. claim `revision_policy` and `review_history` - done;
4. `review-claim` CLI and StateStore method - done;
5. minimal-change patch preview - done preview-only;
6. scenario evaluation for claim review patch preview - done.

Implemented result:

- Dream conflict claims now produce support links from evidence and contradiction/dependency links for identity or memory-sensitive conflicts;
- claim review records snapshot, audit, trace, event, update_log, review decision, and patch preview;
- patch preview explicitly refuses direct Identity Core and semantic memory mutation;
- scenario evaluation adds `claim_graph_review_patch_preview`.

Remaining gaps:

- link generation is still deterministic and shallow;
- no claim merge/supersede workflow yet;
- no actual patch executor yet;
- identity proposals use claim ids as evidence, but do not deeply reason over claim dependencies yet;
- no UI for reviewing claim graph.

### P15 Context Builder v0.3

Goal: move the context package from response-only activation toward configurable, auditable, persistent state activation.

Status: implemented as a first local v0.3 pass.

Executable items:

1. top-level `context_builder` state object - done;
2. configurable context policy - first pass done;
3. persistent activation traces - done;
4. source attribution budget - done;
5. identity gate / claim graph / Dream artifact activation signals - first pass done;
6. scenario evaluation for context builder policy trace - done.

Implemented result:

- `context_builder.policy` now stores Context Builder v0.3 policy, budgets, signal weights, and persistence settings;
- `build_context_package()` outputs `context_package_version: "0.3"` and `context_package_id`;
- activation traces are saved into `context_builder.activation_traces`, while adapter dry-run previews do not persist traces;
- source attribution budget is enforced from policy;
- identity gate evidence, claim graph evidence, and Dream artifact inputs affect activation reasons and scores;
- scenario evaluation adds `context_builder_policy_trace`.

Remaining gaps:

- no vector retrieval or embeddings yet;
- signal weights are still deterministic heuristics;
- no independent CLI/API command for editing context policy yet;
- activation trace history has no retention / compaction review workflow yet;
- no independent baseline-agent comparison for context policy benefit yet.

### P16 Procedural Memory Review

Goal: let repeated successful workflows move from Dream candidates into reviewable, reversible durable procedural memory.

Status: implemented as a first local v0.4 pass.

Executable items:

1. `task_hub.procedural_memory` store - done;
2. `task_hub.procedural_review_decisions` - done;
3. `review-procedural-candidate` CLI and StateStore method - done;
4. approve/reject/archive/quarantine review actions - done;
5. snapshot, audit, trace, update_log, rollback metadata - done;
6. scenario evaluation for procedural memory review - done.

Implemented result:

- Dream still only proposes pending `procedural_candidates`;
- approve creates `task_hub.procedural_memory` and marks the candidate approved;
- review decisions enter candidate history, task hub decision store, snapshot, audit, trace, event, and update log;
- context packages expose `procedural_memory` so later sessions can recover action structure;
- procedural review does not mutate Identity Core and does not execute workflows automatically.

Remaining gaps:

- no workflow policy executor yet;
- procedural memory is not yet deeply linked to tool policy / safety policy;

## 6. Current Recommendation

P17-P19 are now implemented as the current Task Hub / procedural safety foundation:

```text
P17 Failure Reflection
```

Goal: preserve improvement signals after failed or blocked workflows.

Status: implemented as a first local pass.

Implemented result:

- `task_hub.failure_reflections` records workflow, summary, lesson, next action, evidence, provenance, and status;
- `record-failure-reflection` creates a pending `task_hub.cautionary_procedural_candidates` entry;
- context packages expose both failure reflections and cautionary procedural candidates;
- scenario evaluation adds `failure_reflection`;
- failure reflection does not mutate Identity Core and does not execute workflow policy.

Remaining gaps:

- procedural memory is not yet deeply linked to tool policy / safety policy;
- no workflow policy executor yet.

### P18 Procedural Lifecycle / Retention

Goal: let reviewed procedural memory stay active, become archived, discarded, or quarantined through an auditable retention path.

Status: implemented as a first local pass.

Implemented result:

- `procedural-lifecycle` CLI can archive, discard, or quarantine `task_hub.procedural_memory`;
- `StateStore.apply_procedural_lifecycle_action` writes snapshot, audit, trace, update log, lifecycle history, and `task_hub.procedural_lifecycle_decisions`;
- context packages expose only active procedural memory;
- scenario evaluation adds `procedural_lifecycle_retention`;
- procedural lifecycle does not mutate Identity Core and does not execute workflow policy.

Remaining gaps:

- procedural memory is not yet deeply linked to tool policy / safety policy;
- no workflow policy executor yet;

### P22 Reflection-Policy Linkage

Goal: connect verified reflection evidence to policy-adjacent safeguards without turning reflection into automatic execution.

Status: implemented as a first local pass.

Implemented result:

- `build_context_package()` now exposes `reflection_policy_guidance`;
- `reflection_policy_guidance` consumes only verified `task_hub.reflection_log` entries;
- guidance records advisory-only review recommendations, allowed influence fields, evidence, verification history count, and priority;
- guidance explicitly records `execution_prohibited: true` and `identity_mutation_allowed: false`;
- scenario evaluation expands `reflection_log_verification` across `tool_use` and `claim_graph_review`;
- reflection evidence can guide cautionary review focus without mutating Identity Core or executing workflow policy.

Remaining gaps:

- no tool/safety policy executor exists yet;
- dedicated reflection guidance review queue is handled by P23;

### P23 Reflection Guidance Review Queue

Goal: make reflection-policy guidance durable and reviewable without creating executable policy.

Status: implemented as a first local pass.

Implemented result:

- `task_hub.reflection_guidance_queue` records durable guidance items derived from verified reflection policy guidance;
- `task_hub.reflection_guidance_decisions` records review decisions;
- `review-reflection-guidance` can acknowledge, archive, or quarantine a guidance item;
- review writes snapshot, audit, trace, update log, review history, and replayable event metadata;
- reviewed guidance preserves `execution_prohibited: true`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- scenario evaluation verifies durable queue creation, review decision recording, replay, no executable policy creation, and no Identity Core mutation.

Remaining gaps:

- guidance queue is now linked to a dedicated tool/safety policy proposal layer in P24;
- no tool/safety policy executor exists yet;
- guidance prioritization is still simple risk/confidence scoring.

### P24 Tool/Safety Policy Proposal Layer

Goal: connect reviewed reflection guidance to explicit tool/safety policy proposals without creating an executor or automatic tool policy.

Status: implemented as a first local pass.

Implemented result:

- `task_hub.tool_safety_policy_proposals` records proposal-only policy candidates derived from reviewed reflection guidance;
- `task_hub.tool_safety_policy_decisions` records proposal review decisions;
- `propose-tool-safety-policy` creates proposals only from acknowledged or archived reflection guidance;
- `review-tool-safety-policy-proposal` can approve, reject, archive, or quarantine a proposal;
- proposal review writes snapshot, audit, trace, update log, review history, rollback metadata, and replayable event metadata;
- proposals and decisions preserve `proposal_mode: "proposal_only"`, `requires_review: true`, `execution_prohibited: true`, `executable_policy: false`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- scenario evaluation extends `reflection_log_verification` with proposal creation, proposal review, context exposure, replay, no executable policy creation, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- proposal lifecycle retention is handled by P25;
- no structured allow/deny rule semantics are enforced from approved proposals;
- policy proposal prioritization is still simple risk/confidence scoring.

### P25 Tool/Safety Policy Proposal Lifecycle

Goal: let reviewed tool/safety policy proposals age out, be archived, discarded, or quarantined without creating executable policy.

Status: implemented as a first local pass.

Implemented result:

- `task_hub.tool_safety_policy_lifecycle_decisions` records proposal lifecycle decisions;
- `tool-safety-policy-lifecycle` can archive, discard, or quarantine reviewed policy proposals;
- lifecycle review writes snapshot, audit, trace, update log, lifecycle history, rollback metadata, and replayable event metadata;
- proposal lifecycle preserves `proposal_mode: "proposal_only"`, `requires_review: true`, `execution_prohibited: true`, `executable_policy: false`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- context packages expose only active pending/approved tool/safety policy proposals;
- scenario evaluation verifies archived proposal suppression, replay, no executable policy creation, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- policy proposal prioritization is handled by P26 scoring, and proposal relationship links are handled by P27;
- evidence strength and scope specificity are scored locally, but not yet connected to claim graph dependency links.

### P26 Tool/Safety Proposal Evidence Scoring

Goal: rank reviewed tool/safety policy proposals by evidence strength, scope specificity, staleness, and risk without creating executable policy.

Status: implemented as a first local pass.

Implemented result:

- `proposal_score` is attached to tool/safety policy proposals;
- score fields include evidence strength, scope specificity, staleness, priority score, recommended review priority, unique evidence, and factors;
- scores are copied into review and lifecycle decisions;
- context packages sort active pending/approved proposals by `priority_score`;
- scoring records `mode: "review_priority_only"`, `execution_prohibited: true`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- scenario evaluation verifies score creation, bounded priority, score factors, context ranking, replay, no executable policy creation, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- proposal relationship links are handled by P27;
- evidence scoring is not yet connected to claim graph dependency links.

### P27 Tool/Safety Proposal Conflict Links

Goal: model relationships between tool/safety policy proposals before any executable policy layer exists.

Status: implemented as a first local pass.

Implemented result:

- `task_hub.tool_safety_policy_links` records review-only proposal relationships;
- `link-tool-safety-policy-proposals` can create `supports`, `conflicts_with`, `supersedes`, `overlaps`, and `depends_on` links;
- links require existing `from_proposal_id` and `to_proposal_id`, reject self-links, and suppress duplicate active links;
- links record reviewer, reason, evidence, confidence, proposal scores, and scope overlap;
- context packages expose recent active proposal links as relationship evidence;
- validation rejects missing evidence, invalid link types, broken proposal references, executable policy flags, and Identity Core mutation flags;
- scenario evaluation verifies link creation, context exposure, non-execution, replay, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- proposal link lifecycle retention is handled by P28;
- proposal link claim-graph evidence bridging is handled by P29.

### P28 Tool/Safety Proposal Link Lifecycle

Goal: let reviewed proposal links age out, be archived, discarded, or quarantined without creating executable policy.

Status: implemented as a first local pass.

Implemented result:

- `task_hub.tool_safety_policy_link_lifecycle_decisions` records proposal link lifecycle decisions;
- `tool-safety-policy-link-lifecycle` can archive, discard, or quarantine reviewed proposal links;
- lifecycle review writes snapshot, audit, trace, update log, lifecycle history, rollback metadata, and replayable event metadata;
- link lifecycle preserves `relationship_mode: "review_link_only"`, `requires_review: true`, `execution_prohibited: true`, `executable_policy: false`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- context packages expose only active tool/safety policy links;
- scenario evaluation verifies archived link suppression, replay, no executable policy creation, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- proposal link claim-graph evidence bridging is handled by P29;
- governance proposal-link evidence signal calibration is handled by P30.

### P29 Proposal Link Claim-Graph Evidence Bridge

Goal: expose reviewed tool/safety proposal relationships to the claim graph as evidence/dependency material without rewriting claims or creating executable policy.

Status: implemented as a first local pass.

Implemented result:

- `claim_graph.proposal_link_evidence` records review-only evidence bridged from tool/safety proposal links;
- `bridge-proposal-link-claim-evidence` creates a proposal link evidence record and a claim graph support link;
- duplicate active bridges for the same source link are suppressed;
- bridged evidence enters Context Builder activation through the separate `governance_proposal_link_evidence` signal after P30;
- validation rejects executable policy flags, claim rewrite flags, semantic memory mutation flags, invalid link types, and missing evidence;
- scenario evaluation verifies bridge creation, claim graph link creation, no claim rewrite, no executable policy creation, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- activation traces now distinguish identity-gate, claim-conflict, Dream, and governance proposal-link evidence through P30;
- activation traces do not yet provide a compact source-bucket attribution report for each selected item.

### P30 Context Builder Governance Signal Calibration

Goal: make governance proposal-link evidence visible as its own Context Builder activation signal before any executable policy layer is considered.

Status: implemented as a first local pass.

Implemented result:

- `context_builder.policy.selection_dimensions` now includes `governance_evidence_signal`;
- `context_builder.policy.signal_weights` now includes `governance_proposal_link_evidence`;
- `build_context_signal_index` keeps `claim_graph.proposal_link_evidence` in a governance-specific bucket instead of folding it into generic `claim_graph_evidence`;
- selected context items can receive a `governance_proposal_link_evidence` activation reason;
- context signal summaries expose `governance_proposal_link_evidence_count`;
- scenario metrics expose `context_governance_signal_count`;
- validation requires the governance selection dimension and signal weight;
- scenario evaluation verifies that governance proposal-link evidence activates independently from identity, claim, and Dream signals.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- activation trace signal attribution is handled by P31.

### P31 Context Signal Attribution Report

Goal: make each selected Context Builder item explain which signal bucket activated it, which ids matched, and which source records supplied the evidence.

Status: implemented as a first local pass.

Implemented result:

- Context signal buckets now carry both matched ids and source records;
- selected activation decisions include `signal_attribution`;
- activation traces include `signal_attribution_summary`;
- persisted `context_builder.activation_traces` preserve the attribution summary;
- validation checks attribution shape without requiring old traces to be migrated;
- scenario evaluation verifies governance attribution source bucket, matched evidence ids, persisted attribution summary, and `context_signal_attribution_count`.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- attribution coverage review is handled by P32.

### P32 Context Attribution Coverage Review

Goal: review recent Context Builder activation traces for attribution coverage, turning weak or missing signal attribution into review-only signals.

Status: implemented as a first local pass.

Implemented result:

- `context_builder.attribution_coverage_reviews` stores review-only coverage reports;
- `review-context-attribution-coverage` creates a coverage report over recent activation traces;
- coverage metrics include selected count, signal-selected count, attributed count, source record count, attribution ratio, source record ratio, and signal counts;
- missing or weak attribution becomes `review_signals`, not executable policy;
- coverage reviews preserve `review_only: true`, `execution_prohibited: true`, `executable_policy: false`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- validation rejects executable or identity-mutating coverage reviews;
- scenario evaluation verifies coverage review creation, signal-selected coverage, non-execution, and no Identity Core mutation.

Remaining gaps:

- no tool/safety policy executor exists yet;
- no structured allow/deny rule semantics are enforced from approved proposals;
- coverage reviews can accumulate, but they do not yet have lifecycle review actions such as acknowledge, archive, or quarantine.

Recommended next step:

```text
P33 Context Attribution Coverage Review Lifecycle
```

Reason:

- P32 creates durable coverage review records, so the next foundation step is lifecycle governance for those records;
- review signals should be acknowledged, archived, or quarantined before they influence future planning;
- lifecycle handling keeps attribution review auditable without creating executable policy;
- this keeps the project aligned with auditability, state transfer, and local foundation first.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P33 Context Attribution Coverage Review Lifecycle

Goal: let durable attribution coverage review records be acknowledged, archived, or quarantined through an auditable lifecycle path.

Status: implemented as a first local pass.

Implemented result:

- `context-attribution-coverage-lifecycle` CLI can acknowledge, archive, or quarantine coverage review records;
- `StateStore.apply_context_attribution_coverage_lifecycle_action` writes snapshot, audit, trace, update log, lifecycle history, update history, and `context_builder.attribution_coverage_lifecycle_decisions`;
- context packages expose only active or acknowledged coverage reviews, so archived and quarantined reviews are suppressed from active state transfer;
- lifecycle decisions preserve `review_only: true`, `execution_prohibited: true`, `executable_policy: false`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- validation rejects executable or identity-mutating coverage review lifecycle records;
- scenario evaluation verifies lifecycle decision creation, archived-review context suppression, non-execution, and no Identity Core mutation.

Remaining gaps:

- scenario baselines now run deterministic local rule comparisons, but not separate baseline agents;
- replay now has a target-path transition projection, but not a full object-level state rebuild;
- no executable policy layer exists or should be introduced yet.

Recommended next step:

```text
P34 Evaluation Baseline Execution
```

Reason:

- the project outline still requires real comparison against stateless, retrieval-only, and summary-only baselines;
- P7-P33 now give enough local foundation to compare continuity behavior without expanding platform scope;
- baseline execution strengthens the research claim while keeping the work local and non-platform-specific.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P34 Evaluation Baseline Execution

Goal: move scenario baselines from metadata-only tracking to a deterministic, executable local comparison layer.

Status: implemented as a first local pass.

Implemented result:

- `evaluate-scenarios` now reports `baseline_execution: "deterministic_local_v0.9"`;
- stateless, retrieval-only, and summary-only baselines each produce deterministic rule-based scores;
- baseline dimensions cover task resumption, stale memory control, identity attack resistance, conflict repair auditability, and selective forgetting;
- scenario output includes baseline `results` and state-transfer `comparisons`;
- tests verify that state transfer outperforms each baseline in the local rule comparison.

Remaining gaps:

- baseline execution is deterministic and rule-based; it does not yet run separate baseline agents;
- replay now has a target-path transition projection, but not a full object-level state rebuild;
- rollback preview now reports affected paths and projected impact, but remains non-mutating.

Recommended next step:

```text
P35 Event Replay Rebuild / Stronger Rollback Preview
```

Reason:

- P34 makes evaluation more experimental, but replay is still the weakest engineering proof;
- stronger replay/rebuild would support baseline comparison, auditability, and long-run durability;
- rollback preview should explain affected state paths more concretely while remaining non-mutating.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P35 Event Replay Rebuild / Stronger Rollback Preview

Goal: strengthen replay beyond audit-reference validation while keeping rollback preview non-mutating.

Status: implemented as a first local pass.

Implemented result:

- `replay-events` now reports `mode: "audit_replay_with_projection"`;
- event replay builds `target_path_transition_projection_v0.2` from event sequence, operation, operation class, target path, target identity, after value, and rollback metadata;
- projection reports rebuildable event count, target-path transition summaries, operation-class summaries, latest target references, rollback snapshot coverage, and sequence gaps;
- `projection_validation` reports target-path count consistency against current state while allowing seed/pre-event coverage gaps;
- `rollback-preview` now reports `mode: "metadata_only_with_projection"`;
- rollback preview includes affected state paths and projected rollback impact while keeping `would_modify_state: false`;
- scenario evaluation verifies projection rebuild, identity-memory projection, affected rollback paths, projected rollback impact, and no state mutation.

Remaining gaps:

- projection is transition-level, not full object-level state reconstruction;
- automatic rollback is still intentionally absent;
- event schema still stores references rather than full object payload diffs;
- no event compaction, retention, or standalone projection validation CLI beyond `replay-events`.

Recommended next step:

```text
P36 Replay Projection Coverage / Event Schema Hardening
```

Reason:

- P35 gives replay a concrete projection, but the projection should be validated more explicitly against state counts and known target paths;
- event schema can become more durable by recording operation class and target identity consistently;
- this keeps the next step local, audit-focused, and safely short of automatic rollback.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P36 Replay Projection Coverage / Event Schema Hardening

Goal: make replay projection more durable and auditable without introducing automatic rollback.

Status: implemented as a first local pass.

Implemented result:

- new state events include `operation_class` and `target_identity`;
- projection mode advances to `target_path_transition_projection_v0.2`;
- projection records operation-class counts, target identities, target identity counts, and latest target identity by target path;
- `replay-events` now includes `projection_validation` with checked, matched, consistent, unchecked, and mismatch counts;
- projection validation treats existing seed or pre-event state as a coverage gap, not a failure, but reports inconsistency when projected references exceed current state count;
- scenario evaluation verifies identity-memory projection coverage consistency and reports checked/matched/consistent/mismatch metrics.

Remaining gaps:

- projection validation is still report-only;
- replay still does not reconstruct full object payloads from events;
- no event compaction or retention workflow exists yet;
- rollback remains preview-only and non-mutating.

Recommended next step:

```text
P37 Event Retention / Projection Validation CLI
```

Reason:

- replay now has enough projection structure to justify a dedicated validation/report command;
- retention policy should be introduced before the event log grows indefinitely;
- this keeps the foundation audit-centered and avoids jumping to automatic rollback too early.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P37 Event Retention / Projection Validation CLI

Goal: expose replay projection health and event retention pressure through a dedicated read-only command before introducing any compaction workflow.

Status: implemented as a first local pass.

Implemented result:

- `event-report --retention-limit <n>` reports `mode: "event_projection_report_v0.1"`;
- the report includes replay status, projection mode, full `projection_validation`, coverage gap paths, and coverage gap count;
- retention output is explicitly `mode: "report_only"` and reports limit, event count, excess event count, oldest/newest event ids, and suggested action;
- when event count exceeds the supplied limit, the suggested action is `review_compaction_policy`;
- `event-report` preserves `would_modify_state: false`, `report_only: true`, and `state_unchanged`;
- scenario evaluation now verifies event report success, read-only behavior, and retention suggestion metrics.

Remaining gaps:

- event retention still has no review lifecycle or durable decision record;
- no event compaction, summarization, deletion, or rewrite exists yet;
- replay projection remains transition-level rather than full object-payload reconstruction;
- rollback remains preview-only and non-mutating.

Recommended next step:

```text
P38 Event Retention Review Lifecycle
```

Reason:

- P37 can detect retention pressure but cannot record a human review decision yet;
- the next foundation step should create a review-only lifecycle record for retention planning before any destructive compaction is considered;
- this keeps event governance auditable while preserving the current non-mutating replay and rollback boundary.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P38 Event Retention Review Lifecycle

Goal: let event retention pressure become a durable, review-only governance record before any event compaction mechanism exists.

Status: implemented as a first local pass.

Implemented result:

- `review-event-retention --retention-limit <n>` records `task_hub.event_retention_reviews`;
- `event-retention-lifecycle <review_id>` can acknowledge, archive, or quarantine retention reviews;
- active and acknowledged retention reviews can enter the context package, while archived/quarantined reviews are suppressed;
- lifecycle decisions are stored in `task_hub.event_retention_lifecycle_decisions`;
- records preserve `review_only: true`, `execution_prohibited: true`, `executable_policy: false`, `executable_policy_created: false`, and `identity_mutation_allowed: false`;
- P38 explicitly records `event_compaction_executed: false` and `events_modified: false`;
- scenario evaluation verifies retention review creation, lifecycle archival, context suppression, replay after retention governance, no compaction, and no old event rewrite.

Remaining gaps:

- event compaction still intentionally does not exist;
- retention reviews do not yet choose concrete compaction windows or payload preservation rules;
- replay projection is still transition-level and does not reconstruct full object payloads;
- rollback remains preview-only and non-mutating.

Recommended next step:

```text
P39 Event Payload / Diff Coverage Preview
```

Reason:

- before designing event compaction, the project needs to know which state transitions have enough payload/diff detail to be preserved safely;
- this should remain report-only and should not delete, summarize, or rewrite events;
- it prepares the ground for future retention policy without breaking the append-only ledger boundary.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P39 Event Payload / Diff Coverage Preview

Goal: make event object-payload and object-diff coverage visible before any retention or compaction design can claim safety.

Status: implemented as a first local pass.

Implemented result:

- `event-payload-diff-report` CLI previews event payload/diff coverage without mutating state;
- `StateStore.event_payload_diff_coverage_preview` wraps replay status, projection mode, and read-only state checks;
- `build_event_payload_diff_coverage` classifies events as `reference_only`, `payload_hint_only`, `diff_ready`, or `missing_transition_reference`;
- report metrics include transition reference count, payload hint count, payload gap count, diff ready count, diff gap count, high-risk count, and rollback snapshot count;
- target-path and workflow summaries show where payload/diff gaps concentrate;
- scenario evaluation verifies the report is read-only, transition references are complete in the normal replay scenario, diff gaps are visible, full object rebuild is not ready, and destructive compaction remains blocked;
- tests verify both read-only preview behavior and malformed-event high-risk detection.

Remaining gaps:

- events still do not store full object payloads for most state transitions;
- events still do not store explicit object diffs;
- rollback snapshots remain metadata-only;
- no destructive event compaction, summarization, deletion, or rewrite exists.

Recommended next step:

```text
P40 Event Payload Capture Policy Proposal
```

Reason:

- P39 shows that transition references are mostly sufficient, but object payload/diff coverage is not;
- before implementing payload capture, the project should define a review-only capture policy proposal that says which target paths need full payloads, diffs, snapshots, or reference-only treatment;
- this keeps the next move in governance/report space and avoids prematurely changing the append-only event schema.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

Research calibration after P39:

- Martin Fowler's Event Sourcing pattern reinforces the requirement that state changes be captured as durable event objects that can support reconstruction of past states: https://www.martinfowler.com/eaaDev/EventSourcing.html
- W3C PROV-DM gives the project a stable vocabulary for event provenance: entities, activities, agents, usage, generation, and derivation: https://www.w3.org/TR/prov-dm/
- Tulving's episodic-memory framing connects memory to self, subjective time, and autonoetic continuity; for 01 Core this argues against treating memory as detached text retrieval: https://www.annualreviews.org/doi/10.1146/annurev.psych.53.100901.135114
- Hassabis and Maguire's construction account of episodic memory supports the idea that future continuity needs structured reconstruction material, not only a flat event reference: https://www.sciencedirect.com/science/article/abs/pii/S1364661307001258

Implication for P40: define a review-only payload capture policy by target path, with explicit requirements for reference-only events, object payload hints, object diffs, snapshot links, and PROV-style provenance fields before any schema-level payload capture or compaction mechanism is attempted.

### P40 Event Payload Capture Policy Proposal

Goal: turn P39 payload/diff coverage gaps into a durable, review-only target-path capture policy proposal before any event schema mutation or payload capture mechanism exists.

Status: implemented as a first local pass.

Implemented result:

- `propose-event-payload-capture-policy` CLI creates `task_hub.event_payload_capture_policy_proposals` from the current payload/diff coverage report;
- `review-event-payload-capture-policy` CLI records approve, reject, archive, or quarantine decisions in `task_hub.event_payload_capture_policy_decisions`;
- each proposal records target-path requirements with `capture_mode` values: `full_payload_and_diff`, `payload_hint_required`, `snapshot_link_required`, or `reference_only_ok`;
- proposals and decisions explicitly preserve `proposal_mode: "proposal_only"`, `requires_review: true`, `execution_prohibited: true`, `executable_policy: false`, and `executable_policy_created: false`;
- proposals and decisions also lock out `event_schema_mutation_allowed`, `event_payload_capture_executed`, `event_compaction_executed`, `events_modified`, and `safe_for_destructive_compaction`;
- active and approved capture policy proposals enter the context package so later engineering loops can see the reviewed target-path guidance;
- validation rejects executable, schema-mutating, payload-capturing, compaction-executing, event-modifying, or destructive-compaction-safe records;
- scenario evaluation verifies proposal creation, approval, context exposure, replay consistency, and zero schema mutation / execution / compaction / event modification counts;
- empty event logs still produce a valid `reference_only_ok` guidance record instead of an invalid proposal.

Remaining gaps:

- the event log still stores transition references, not full object payloads;
- no event schema migration for payload capture exists yet;
- no executable policy layer exists and should not be introduced before the review lifecycle is firmer;
- approved capture guidance is not yet linked to retention review lifecycle decisions;
- local JSON state writes are still intended for serial local operation; concurrent CLI writes can produce replay or validation mismatches until a file-locking or transactional store layer exists.

Implemented next step:

```text
P41 Event Replayability Assessment
```

Reason:

- the post-P40 objective shifted from adding governance lifecycle features to proving whether state continuity can be carried by events;
- P39/P40 expose payload and diff gaps, but the project still needs a direct replayability assessment that says which reconstruction level is ready;
- this keeps the project in Event-Sourcing Groundwork and avoids premature executor, automatic rollback, destructive compaction, platform integration, or event rewrite work.

Implemented result:

- `event-replayability-assessment` CLI reports `event_replayability_assessment_v0.1`;
- the report combines replay projection validation with payload/diff coverage;
- it separates deterministic replay readiness, transition projection readiness, object reconstruction readiness, and full state reconstruction readiness;
- it reports missing capabilities such as `object_payload`, `object_diff`, `rollback_snapshot`, and seed/pre-event coverage gaps;
- it keeps `reconstruction_executed: false`, `event_payload_capture_executed: false`, `event_compaction_executed: false`, `automatic_rollback_executed: false`, `event_schema_mutation_allowed: false`, `report_only: true`, and `would_modify_state: false`;
- scenario evaluation verifies that deterministic replay is ready while object/full-state reconstruction remains not ready because payload/diff evidence is incomplete.

Remaining gaps:

- no event schema migration for object payload or object diff capture exists yet;
- replay still does not rebuild object state from an empty seed;
- approved capture guidance still lacks a separate lifecycle path;
- local JSON state writes remain serial-operation oriented until a file lock or transactional store exists.

Implemented next step:

```text
P42 Reconstruction Evidence Schema Research
```

Reason:

- P41 can now say what is missing, but the project still needs to design the minimum evidence schema for object payloads, object diffs, transition payloads, and reconstruction metadata;
- this should remain research/report-only before any event schema mutation or payload capture is implemented;
- it directly serves Priority A and Priority B without adding chat, platform, or companion surface area.

Implemented result:

- `reconstruction-evidence-schema-report` CLI reports `reconstruction_evidence_schema_report_v0.1`;
- the report defines four draft evidence sections: `event_envelope`, `transition_payload`, `object_evidence`, and `reconstruction_metadata`;
- it maps P41 missing capabilities to minimum fields such as `object_payload`, `object_diff`, `rollback_snapshot_id`, `seed_state_ref`, and validation metadata;
- it reports readiness gates for deterministic replay, transition projection, object reconstruction, and full-state reconstruction;
- it keeps `reconstruction_executed: false`, `event_payload_capture_executed: false`, `event_schema_mutation_allowed: false`, `event_compaction_executed: false`, `automatic_rollback_executed: false`, `report_only: true`, and `would_modify_state: false`;
- scenario evaluation verifies that the schema report exists, remains read-only, exposes target-path requirements, and does not execute capture, schema mutation, or reconstruction.

Remaining gaps:

- the schema is still a draft report, not an event schema migration;
- event families are not yet mapped to the new schema sections;
- replay still cannot rebuild object state from empty seed;
- no payload or diff capture implementation exists.

Implemented next step:

```text
P43 Evidence Schema Coverage Mapping
```

Reason:

- P42 defines the evidence vocabulary, but the project still needs a read-only mapping from current event families/workflows to required schema sections;
- this should identify which workflow families need object payloads, object diffs, snapshot links, or seed/pre-event references before any schema mutation is considered;
- it continues Priority A/B groundwork without implementing capture, reconstruction, compaction, rollback, or adapters.

Implemented result:

- `reconstruction-evidence-coverage-map` CLI reports `reconstruction_evidence_coverage_mapping_v0.1`;
- the report maps current event workflows to required P42 schema sections and minimum fields;
- it exposes workflow-level payload gaps, diff gaps, snapshot gaps, transition gaps, target paths, and example event IDs;
- it summarizes section coverage so the project can see which schema sections are required by current events;
- it keeps `event_schema_mutation_allowed: false`, `event_payload_capture_executed: false`, `reconstruction_executed: false`, `event_compaction_executed: false`, `automatic_rollback_executed: false`, `report_only: true`, and `would_modify_state: false`;
- scenario evaluation verifies that workflow mapping exists, gap visibility is nonzero, state remains unchanged, and no capture/schema mutation/reconstruction executes.

Remaining gaps:

- workflow gaps are mapped but not prioritized by reconstruction value or risk;
- no event schema migration exists;
- no payload or diff capture implementation exists;
- replay still cannot rebuild object state from empty seed.

Implemented next step:

```text
P44 Evidence Gap Prioritization Report
```

Reason:

- P43 maps which workflows have evidence gaps, but the project still needs a read-only way to rank those gaps by reconstruction value, risk, and expected implementation cost;
- this should help decide which event families deserve schema work first without performing schema mutation or payload capture;
- it remains inside Event-Sourcing Groundwork and avoids executor, rollback, compaction, adapters, or product surfaces.

Implemented result:

- `reconstruction-evidence-gap-priorities` CLI reports `reconstruction_evidence_gap_prioritization_v0.1`;
- each workflow gap receives review-only scoring for `reconstruction_value`, `preservation_risk`, `implementation_cost`, `priority_score`, and `recommended_priority`;
- prioritized workflows are sorted by priority score and assigned `recommended_order`;
- the report keeps `event_schema_mutation_allowed: false`, `event_payload_capture_executed: false`, `reconstruction_executed: false`, `event_compaction_executed: false`, `automatic_rollback_executed: false`, `report_only: true`, and `would_modify_state: false`;
- scenario evaluation verifies bounded scores, visible priorities, read-only behavior, no payload capture, no schema mutation, and no reconstruction execution.

Remaining gaps:

- no schema approval workflow exists;
- no event schema migration exists;
- no payload or diff capture implementation exists.

Implemented next step:

```text
P45 Reconstruction Evidence Schema Review Checklist
```

Reason:

- P44 ranks the gaps, but the project still needs a review-only checklist that turns top-ranked workflow gaps into explicit review questions, acceptance criteria, and required evidence before any schema work begins;
- this keeps governance ahead of implementation and avoids automatic schema mutation, payload capture, reconstruction execution, rollback, compaction, or adapters;
- it connects Priority A/B research to Priority C governance without becoming a product surface.

Implemented result:

- `reconstruction-evidence-schema-review-checklist` CLI reports `reconstruction_evidence_schema_review_checklist_v0.1`;
- each prioritized workflow becomes a review-only checklist item with review questions, acceptance criteria, required evidence, allowed review decisions, and explicit non-execution flags;
- checklist items preserve P44 `recommended_order`, `recommended_priority`, target paths, missing capabilities, minimum fields, and example event IDs;
- the report keeps `event_schema_mutation_allowed: false`, `event_payload_capture_executed: false`, `reconstruction_executed: false`, `event_compaction_executed: false`, `automatic_rollback_executed: false`, `identity_mutation_allowed: false`, `report_only: true`, and `would_modify_state: false`;
- scenario evaluation verifies checklist material exists, remains read-only, and does not execute schema mutation, payload capture, reconstruction, identity mutation, rollback, or compaction.

Remaining gaps:

- checklist decisions are not yet recorded as durable review records;
- no schema approval workflow exists;
- no event schema migration exists;
- no payload or diff capture implementation exists.

Recommended next step:

```text
P46 Reconstruction Schema Checklist Review Record
```

Reason:

- P45 prepares review material, but the project still needs a durable, non-executable record for human decisions on each checklist item;
- this should capture reviewer, decision, rationale, requested evidence, and approval scope without performing schema mutation or payload capture;
- it keeps the project in Event-Sourcing Groundwork while creating a bridge from review checklist to future schema design.

Desired acceptance:

```bash
python3 -m unittest
python3 -m one_core.cli validate-state
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
git diff --check
```

### P19 Cautionary Procedural Review

Goal: let warning-style failure candidates become active, reviewable caution memory without becoming executable policy.

Status: implemented as a first local pass.

Implemented result:

- `review-cautionary-procedural-candidate` CLI can approve, reject, archive, or quarantine `task_hub.cautionary_procedural_candidates`;
- approval creates active `task_hub.cautionary_procedural_memory`;
- context packages expose active cautionary procedural memory as warnings;
- review writes snapshot, audit, trace, update log, review decision, and rollback metadata;
- cautionary procedural memory explicitly records `executable_policy: false`;
- scenario evaluation adds `cautionary_procedural_review`;
- cautionary review does not mutate Identity Core and does not execute workflow policy.

Remaining gaps:

- cautionary warnings are not yet linked to tool policy / safety policy;
- no workflow policy executor yet.

### P20 Cautionary Warning Lifecycle

Goal: let active cautionary warnings stay active, become archived, discarded, or quarantined through an auditable retention path.

Status: implemented as a first local pass.

Implemented result:

- `cautionary-warning-lifecycle` CLI can archive, discard, or quarantine `task_hub.cautionary_procedural_memory`;
- `StateStore.apply_cautionary_warning_lifecycle_action` writes snapshot, audit, trace, update log, lifecycle history, and `task_hub.cautionary_lifecycle_decisions`;
- context packages expose only active cautionary procedural memory;
- lifecycle decisions preserve `executable_policy_created: false`;
- scenario evaluation adds `cautionary_warning_lifecycle`;
- cautionary warning lifecycle does not mutate Identity Core and does not execute workflow policy.

Remaining gaps:

- cautionary warnings are not yet linked to tool policy / safety policy;
- no workflow policy executor yet;
- reflection log is now in place, but reflection verification needs broader scenario coverage and cross-linking to future policy work.

Recommended next step:

```text
P22 Reflection-Policy Linkage
```

Reason:

- P21 now records and verifies a general reflection log entry;
- the next missing foundation is to connect reflection evidence to policy-adjacent safeguards without turning it into automatic execution;
- this supports the Cognitive OS self-growth requirement by keeping reflection auditable while still separate from policy execution.
