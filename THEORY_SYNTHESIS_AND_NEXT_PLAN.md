# Theory Synthesis and Next Plan

Chinese version: [THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md](./THEORY_SYNTHESIS_AND_NEXT_PLAN_ZH.md)

This document synthesizes the current 01 Core foundation after P0-P6, the Cognitive OS reference direction, and external theory that is useful for the next engineering loop.

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

- no executable stateless / retrieval-only / summary-only baseline comparison;
- no broad scenario runner;
- limited quantitative metrics;
- multi-user boundary was not yet executable;
- interrupted project / long gap / context loss needed integration tests;
- lifecycle actions needed retrieval-effect evaluation.

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
- no executable baseline comparison;
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
3. failure reflection - not done yet;
4. workflow candidate - first pass done;
5. procedural memory review - pending candidate schema only; no review command yet.

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

- no failure reflection schema yet;
- no procedural candidate review/promote command yet;
- no durable procedural memory store yet;
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
- replay validates event `update_id` references and reports coverage;
- rollback preview links snapshot metadata to affected events without mutating state;
- scenario evaluation adds `event_log_replay_rollback`.

Remaining gaps:

- replay does not reconstruct full state from an empty seed yet;
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

## 6. Current Recommendation

Do P15 next:

```text
P15 Context Builder v0.3
```

Reason:

- P8 gave context activation a first explainable form, but activation trace is still response-only and policy is hardcoded;
- P11-P14 now add identity gate, event log, Dream package, and claim review material that should influence context selection;
- P15 should add configurable context policy, persistent activation traces, and source attribution budget;
- this will make session start more like bounded state transfer rather than ad hoc memory retrieval.
