# Literature Map

This document maps 01 Project to existing work in LLM agents, cognitive architectures, psychology, neuroscience, and continual learning.

It is not a complete bibliography.

It is a first orientation map.

## 1. LLM Agents and Long-Term Memory

### Generative Agents

Paper: [Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)

Relevance:

- uses observation, reflection, and planning,
- stores agent experience in natural language,
- synthesizes memories into higher-level reflections,
- demonstrates that reflection improves believable long-term behavior.

Relation to 01:

Generative Agents is close to the Dream Engine idea, but it focuses mainly on believable human-like simulation.

01 focuses on identity persistence, state transfer, memory lifecycle, and continuity evaluation.

### MemGPT

Paper: [MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)

Relevance:

- treats limited context like limited RAM,
- treats external storage like longer-term memory,
- uses OS-inspired virtual context management,
- supports deliberate movement between memory tiers.

Relation to 01:

MemGPT supports the engineering intuition behind State Transfer and Memory Lifecycle.

01 extends the question from context management to identity, conflict, dream, and life history.

### LongMem

Paper: [Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)

Relevance:

- explores long-term memory augmentation for language models,
- addresses long-context language modeling and memory-augmented in-context learning.

Relation to 01:

LongMem is relevant to memory mechanisms, but 01 is more concerned with structured state growth than language modeling alone.

### Memory-Agent Benchmarks

Examples:

- [MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257)
- [MemoryCD: Lifelong Cross-Domain Personalization](https://memorypapers.org/papers/memorycd-benchmarking-long-context-user-memory-of-llm-agents-for-lifelong-cross-domain-personalization)

Relevance:

- long-term memory evaluation,
- incremental interaction,
- personalization,
- selective forgetting,
- memory update quality.

Relation to 01:

01 should use these ideas but extend evaluation beyond recall into identity stability, conflict repair, and drift resistance.

## 2. Cognitive Architectures

### Soar

Reference: [The Soar Cognitive Architecture](https://mitpress.mit.edu/9780262122962/the-soar-cognitive-architecture/)

Relevance:

- working memory,
- procedural knowledge,
- semantic memory,
- episodic memory,
- reinforcement learning,
- appraisal-based emotion models in later versions.

Relation to 01:

Soar supports the idea that persistent intelligence requires multiple memory systems and learning mechanisms, not one undifferentiated memory store.

### ACT-R

Reference: [ACT-R official site](http://act-r.psy.cmu.edu/)

Relevance:

- declarative memory,
- procedural memory,
- activation-based retrieval,
- cognitive modeling,
- psychologically grounded architecture.

Relation to 01:

ACT-R suggests that 01 should eventually distinguish not only episodic and semantic memory, but also procedural habits and action policies.

## 3. Psychology

### Narrative Identity

Reference: [Narrative Identity: What Is It? What Does It Do? How Do You Measure It?](https://journals.sagepub.com/doi/pdf/10.1177/0276236618756704)

Relevance:

- identity as an internalized and evolving life story,
- reconstructed past and imagined future,
- unity and purpose across life.

Relation to 01:

This directly supports the claim:

```text
Personality != Sum of Memories
Personality = Memory Interpreter
```

01 should treat identity as interpretive narrative, not just stored facts.

### Self-Determination Theory

Reference: [Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being](https://pubmed.ncbi.nlm.nih.gov/11392867/)

Relevance:

- autonomy,
- competence,
- relatedness,
- intrinsic motivation,
- social development.

Relation to 01:

If 01 develops a motivation model, it should avoid arbitrary goal lists and study autonomy, competence, and relatedness as possible functional variables.

### Cognitive Dissonance and Conflict

Relevance:

- conflict between beliefs, values, and actions can trigger change,
- identity maintenance involves resolving inconsistency.

Relation to 01:

This supports conflict-driven growth and Dream Engine conflict detection.

## 4. Neuroscience and Memory Consolidation

### Sleep and Systems Consolidation

Reference: [System consolidation of memory during sleep](https://pmc.ncbi.nlm.nih.gov/articles/PMC3278619/)

Relevance:

- memories encoded in temporary stores can be reactivated and redistributed,
- sleep supports consolidation,
- memory becomes reorganized across systems.

Relation to 01:

Dream Engine should be framed as an engineering analogy to consolidation, not as literal biological dreaming.

### Complementary Learning Systems

Reference: [Complementary Learning Systems theory overview](https://stanford.edu/~jlmcc/papers/McCGoddard96.pdf)

Relevance:

- fast learning system for specific episodes,
- slow learning system for general knowledge,
- consolidation across systems.

Relation to 01:

This supports the Memory Lifecycle:

```text
Episode -> Dream -> Semantic Memory -> Identity Memory
```

It also supports slow identity updates to avoid catastrophic overwriting.

## 5. Neural Networks and Continual Learning

### Continual Learning

Reference: [A Comprehensive Survey of Continual Learning: Theory, Method and Application](https://pubmed.ncbi.nlm.nih.gov/38407999/)

Relevance:

- learning over time,
- catastrophic forgetting,
- stability-plasticity tradeoff,
- rehearsal, regularization, modularity, and replay methods.

Relation to 01:

01 currently focuses on State Growth, not Weight Growth.

This is important because parameter updates introduce catastrophic forgetting and safety challenges.

But 01 should still learn from continual learning:

- protect important knowledge,
- allow adaptation,
- test forgetting,
- measure stability-plasticity tradeoffs.

## 6. Engineering Fields to Borrow From

### Operating Systems

Borrow:

- virtual memory,
- paging,
- snapshots,
- process state,
- garbage collection,
- logs,
- recovery,
- permission boundaries.

### Databases

Borrow:

- schema migration,
- transactions,
- provenance,
- audit logs,
- rollback,
- access control,
- data retention policies.

### Distributed Systems

Borrow:

- state synchronization,
- eventual consistency,
- conflict-free replicated data types,
- consensus,
- versioning,
- fault recovery.

### Software Testing

Borrow:

- unit tests for state transitions,
- integration tests for session recovery,
- regression tests for memory bugs,
- adversarial tests for identity overwrite,
- privacy tests for cross-user leakage.

## 7. Open Research Gap

Existing work covers many pieces:

- memory retrieval,
- reflection,
- context management,
- cognitive architectures,
- narrative identity,
- sleep consolidation,
- continual learning.

The 01 Project gap is the integration:

> How can these pieces become a state-continuous artificial identity whose memory, task state, self-model, relationships, and conflicts remain auditable across time?

That is the research program.
