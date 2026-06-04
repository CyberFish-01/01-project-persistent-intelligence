# CTM-Inspired Temporal Dynamics RFC

Chinese version: [CTM_TEMPORAL_DYNAMICS_RFC_ZH.md](./CTM_TEMPORAL_DYNAMICS_RFC_ZH.md)

Status: `document-only`, `RFC-only`, `non-runtime`.

P81 translates ideas inspired by Continuous Thought Machines into 01 Core
foundation vocabulary. It does not connect a CTM model, implement CTM runtime,
train a model, introduce dependencies, write temporal events, mutate Identity
Core, write recall events, execute growth lifecycle, or add companion, UI,
AstrBot, or adapter behavior.

## RFC Rule

```text
CTM is an inspiration source.
01 Core is not a CTM implementation.
temporal dynamics language does not approve temporal runtime.
```

## CTM Concepts Translation

Continuous Thought Machines research frames time as part of internal neural
processing rather than only input order. The CTM paper and project materials
describe neuron-level temporal processing, neural synchronization as a latent
representation, internal ticks, and adaptive compute. P81 uses those ideas only
as conceptual prompts for 01 Core's symbolic foundation layer.

| CTM concept | Translation for this RFC | 01 Core caution |
|---|---|---|
| temporal processing | Computation unfolds through internal time, not only through a single static pass. | 01 Core can study elapsed-state interpretation, but does not implement CTM processing. |
| synchronization | Neural activity can be represented by how units align over time. | Symbolic governance alignment is not neural synchronization. |
| adaptive compute | The system may spend more internal steps on harder inputs and fewer on simpler ones. | Review depth budgeting is a future policy idea, not runtime compute control. |
| internal dynamics | Hidden state changes over time become part of what the system represents. | 01 Core currently records events and review state; it does not expose neural dynamics. |
| ticks / deliberation steps | Internal update steps over which a state evolves before output. | Any `deliberation_tick` is RFC vocabulary until a storage and execution policy exists. |
| coherence | A state remains mutually consistent enough to support trustworthy action. | Coherence is a review signal, not proof of truth, consciousness, or growth. |
| latent temporal state | The evolving hidden temporal pattern that carries task-relevant information. | 01 Core may define symbolic temporal traces later, but no latent state store exists now. |

This RFC does not claim that 01 Core already has CTM, that symbolic governance
equals neural synchronization, or that review objects emulate brain-like
cognition.

## 01 Core Mapping

| CTM-inspired idea | Existing 01 Core object | Mapping |
|---|---|---|
| event sequence vs temporal dynamics | Event Log, Replay | Event sequence records what happened; temporal dynamics asks how meaning changes as state evolves between and after events. |
| encoding_state / recall_state as temporal traces | Stateful Memory | Encoding and recall states can become symbolic traces of when and from where meaning is interpreted. |
| meaning_shift as temporal reinterpretation | Meaning Shift | A memory's meaning may change after time, conflict, cooling, or renewed evidence. |
| growth_candidate_review as delayed state alignment | Growth Candidate Review | A candidate can express that later state now aligns, conflicts, or reinterprets earlier state. |
| governance review as adaptive deliberation | Governance Surface | Higher-risk candidates may need deeper review; low-risk candidates should not pay heavy review cost. |
| Temporal Awareness as subject-level time sensitivity | Temporal Awareness RFC | Time is part of subject transition only after contract, write policy, and validation exist. |
| Productive Drift vs Collapse as temporal coherence problem | Productive Drift vs Collapse | Coherent drift can clarify continuity; incoherent drift can indicate random drift or collapse. |

## Proposed CTM-Inspired Concepts

These are RFC concepts only. They do not create schemas, stores, events,
validators, or runtime behavior.

| Concept | Problem It Addresses | References Existing Objects | Must Not Automatically Change | Future Runtime? | Needs Evaluation? |
|---|---|---|---|---|---|
| `deliberation_tick` | Names a possible internal review step before a conclusion. | Governance Surface, Task Hub, risk level | identity, memory, claims, events, growth status | Yes, only after policy | Yes |
| `thought_trace` | Names a possible record of how review state evolved. | Event refs, review objects, recall state | event log, memory contents, identity | Yes, only after storage policy | Yes |
| `temporal_coherence` | Reviews whether later state still fits earlier state and current evidence. | Productive Drift, Claim Graph, reconstruction evidence | claim status, identity, memory salience | Maybe | Yes |
| `state_synchronization_score` | Gives a future vocabulary for alignment among memory, claim, task, and identity anchors. | Memory Layer, Claim Graph, Task Hub, Identity Gate | any owner object or gate outcome | Maybe | Yes |
| `review_depth_budget` | Prevents over-review of low-risk items and under-review of high-risk items. | Governance Surface, risk register, review checklist | policy execution or automatic approval | Maybe | Yes |
| `unresolved_tension` | Tracks persistent conflict that has not yet become a candidate or decision. | Claim conflicts, task blockers, memory conflicts | growth candidate, claim revision, identity update | Maybe | Yes |
| `delayed_alignment` | Names a later realization that previous evidence now fits a stable pattern. | Meaning Shift, Growth Candidate Review, Temporal Awareness | semantic promotion or identity update | Maybe | Yes |
| `temporal_pressure` | Names accumulated urgency from stale tasks, old claims, or repeated unresolved conflict. | Task Hub, Claim Graph, Temporal Awareness | task mutation, claim mutation, memory decay | Maybe | Yes |
| `coherence_break` | Marks that the current state no longer safely follows from prior state. | Productive Drift vs Collapse, boundary matrix | collapse classification or memory rewrite | Maybe | Yes |
| `re-synchronization_candidate` | Names a review object for restoring context alignment without changing history. | Context Builder, Event Log, State Transfer package | memory rewrite, identity mutation, recall write | Maybe | Yes |

## Boundaries

P81 explicitly forbids:

- CTM neural implementation;
- model training;
- local model requirement;
- Temporal Awareness runtime;
- temporal event write;
- automatic recall event write;
- identity mutation;
- memory rewrite;
- growth execution;
- companion, UI, AstrBot, or adapter work;
- claim auto-revision;
- policy executor;
- reconstruction reducer execution.

## Evaluation Ideas

These are evaluation ideas only. They are not implemented in P81.

| Scenario | Expected Review Outcome |
|---|---|
| Same event plus different elapsed time | Produces different meaning-shift candidate, not automatic memory mutation. |
| Unresolved conflict accumulates temporal tension | Records possible `unresolved_tension`, not claim auto-revision. |
| Low-risk candidate | Requires shallow review depth and no heavy governance path. |
| Identity-threatening candidate | Requires deeper deliberation and Identity Gate escalation. |
| Temporal coherence separates growth from random drift | Coherent evidence can support review; incoherent change is not growth. |
| Prompt contamination | Creates `coherence_break`, not growth or identity update. |
| Delayed realization | Creates review candidate, not identity update. |
| Re-synchronization | Restores context alignment without memory rewrite. |

## Relationship To Existing Open Questions

| Open Question | P81 Impact |
|---|---|
| Temporal Awareness | Adds CTM-inspired vocabulary for elapsed state dynamics, but keeps runtime blocked. |
| Recall Event Write Policy | Strengthens the need to decide whether ticks/traces are events, traces, or ephemeral review steps. |
| Growth Candidate Lifecycle | Suggests delayed alignment and unresolved tension may become review-object inputs, not lifecycle execution. |
| Productive Drift vs Collapse | Reframes drift as temporal coherence under evidence, not as automatic growth classification. |
| Exploration / Serendipity Engine | Warns that adaptive deliberation must not become productized exploration or companion behavior. |
| Subject Kernel / World Seed | Raises whether temporal coherence should compare current state against protected subject anchors and evolvable world orientation separately. |
| Reconstruction Reducer Contract | Adds future questions about whether thought traces are reconstructable evidence or should remain ephemeral. |

## Risks

- Over-abstracting CTM until every time-related concern is called dynamics.
- Confusing neural synchronization with symbolic governance.
- Creating fake cognition vocabulary without tests.
- Turning report layers into pseudo-consciousness claims.
- Making Temporal Awareness too broad.
- Inventing `thought_trace` without storage policy.
- Making the review layer too heavy for ordinary work.
- Using CTM language to justify automatic growth.

## Open Questions

- Should deliberation ticks be persisted?
- Are ticks events, traces, or ephemeral internal steps?
- What is the minimal useful temporal state?
- How can the project avoid `thought_trace` explosion?
- How can temporal coherence be tested without pretending consciousness?
- Should `review_depth_budget` be tied to `risk_level`?
- Can `unresolved_tension` become a growth candidate?
- When does `delayed_alignment` become evidence?
- How does CTM-inspired dynamics relate to reconstruction?
- What must remain purely RFC until runtime foundation is ready?

## P82 Candidate Directions

P81 does not execute these directions:

- Temporal Coherence Evaluation Plan;
- Deliberation Tick RFC;
- Thought Trace Storage Policy RFC;
- Review Depth Budget RFC;
- Unresolved Tension / Delayed Alignment RFC;
- CTM-inspired Concepts Glossary;
- Foundation Risk Review after CTM mapping.

## References

- Sakana AI, [Introducing Continuous Thought Machines](https://sakana.ai/ctm/).
- Darlow et al., [Continuous Thought Machines](https://arxiv.org/abs/2505.05522).

## P81 Non-Execution Statement

P81 does not implement:

- CTM runtime;
- model training;
- new dependencies;
- temporal runtime;
- temporal event writes;
- recall event writes;
- growth lifecycle execution;
- identity mutation;
- memory rewrite;
- claim auto-revision;
- policy execution;
- reconstruction reducer execution;
- companion, UI, AstrBot, adapter, cloud rollout, or product layer.
