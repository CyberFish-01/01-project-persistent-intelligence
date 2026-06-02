# Literature Map 中文版

英文原文：[LITERATURE_MAP.md](./LITERATURE_MAP.md)

这份文档把 01 Project 与 LLM agents、认知架构、心理学、神经科学和 continual learning 的现有工作连接起来。

它不是完整 bibliography，而是第一版 orientation map。

## 1. LLM Agents 与 Long-Term Memory

### Generative Agents

论文：[Generative Agents: Interactive Simulacra of Human Behavior](https://arxiv.org/abs/2304.03442)

相关性：

- 使用 observation、reflection、planning；
- 用自然语言保存 agent experience；
- 把 memories 合成为更高层 reflections；
- 展示 reflection 能改善可信的长期行为模拟。

与 01 的关系：

Generative Agents 很接近 Dream Engine 的想法，但它主要关注 believable human-like simulation。

01 更关注 identity persistence、state transfer、memory lifecycle 和 continuity evaluation。

### MemGPT

论文：[MemGPT: Towards LLMs as Operating Systems](https://arxiv.org/abs/2310.08560)

相关性：

- 把有限上下文类比为有限 RAM；
- 把外部存储类比为长期 memory；
- 使用 OS-inspired virtual context management；
- 支持 memory tiers 之间的有意迁移。

与 01 的关系：

MemGPT 支持 State Transfer 和 Memory Lifecycle 的工程直觉。

01 把问题从 context management 扩展到 identity、conflict、dream 和 life history。

### LongMem

论文：[Augmenting Language Models with Long-Term Memory](https://arxiv.org/abs/2306.07174)

相关性：

- 探索语言模型的 long-term memory augmentation；
- 处理 long-context language modeling 和 memory-augmented in-context learning。

与 01 的关系：

LongMem 与 memory mechanism 相关，但 01 更关心 structured state growth，而不只是 language modeling。

### Memory-Agent Benchmarks

例子：

- [MemoryAgentBench: Evaluating Memory in LLM Agents via Incremental Multi-Turn Interactions](https://arxiv.org/abs/2507.05257)
- [MemoryCD: Lifelong Cross-Domain Personalization](https://memorypapers.org/papers/memorycd-benchmarking-long-context-user-memory-of-llm-agents-for-lifelong-cross-domain-personalization)

相关性：

- long-term memory evaluation，
- incremental interaction，
- personalization，
- selective forgetting，
- memory update quality。

与 01 的关系：

01 应该借鉴这些想法，但把 evaluation 从 recall 扩展到 identity stability、conflict repair 和 drift resistance。

## 2. Cognitive Architectures

### Soar

参考：[The Soar Cognitive Architecture](https://mitpress.mit.edu/9780262122962/the-soar-cognitive-architecture/)

相关性：

- working memory，
- procedural knowledge，
- semantic memory，
- episodic memory，
- reinforcement learning，
- 后续版本中的 appraisal-based emotion models。

与 01 的关系：

Soar 支持一个判断：persistent intelligence 需要多种 memory systems 和 learning mechanisms，而不是一个不分层的 memory store。

### ACT-R

参考：[ACT-R official site](http://act-r.psy.cmu.edu/)

相关性：

- declarative memory，
- procedural memory，
- activation-based retrieval，
- cognitive modeling，
- 心理学基础架构。

与 01 的关系：

ACT-R 提醒 01 未来不仅要区分 episodic 和 semantic memory，还要区分 procedural habits 和 action policies。

## 3. Psychology

### Narrative Identity

参考：[Narrative Identity: What Is It? What Does It Do? How Do You Measure It?](https://journals.sagepub.com/doi/pdf/10.1177/0276236618756704)

相关性：

- identity 是内化并持续演化的 life story；
- 重构过去并想象未来；
- 在生命中形成 unity 和 purpose。

与 01 的关系：

它直接支持：

```text
Personality != Sum of Memories
Personality = Memory Interpreter
```

01 应该把 identity 理解为 interpretive narrative，而不只是 stored facts。

### Self-Determination Theory

参考：[Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being](https://pubmed.ncbi.nlm.nih.gov/11392867/)

相关性：

- autonomy，
- competence，
- relatedness，
- intrinsic motivation，
- social development。

与 01 的关系：

如果 01 发展 motivation model，应避免任意目标列表，并研究 autonomy、competence、relatedness 是否可以成为功能变量。

### Cognitive Dissonance and Conflict

相关性：

- beliefs、values、actions 之间的冲突可以触发变化；
- identity maintenance 涉及不一致的解决。

与 01 的关系：

这支持 conflict-driven growth 和 Dream Engine conflict detection。

## 4. Neuroscience and Memory Consolidation

### Sleep and Systems Consolidation

参考：[System consolidation of memory during sleep](https://pmc.ncbi.nlm.nih.gov/articles/PMC3278619/)

相关性：

- 临时存储中的 memories 可以被 reactivated 和 redistributed；
- sleep 支持 consolidation；
- memory 会跨系统重组。

与 01 的关系：

Dream Engine 应该被表述为 consolidation 的工程类比，而不是字面意义的生物梦。

### Complementary Learning Systems

参考：[Complementary Learning Systems theory overview](https://stanford.edu/~jlmcc/papers/McCGoddard96.pdf)

相关性：

- fast learning system 负责具体 episodes；
- slow learning system 负责 general knowledge；
- 系统之间通过 consolidation 迁移。

与 01 的关系：

这支持 Memory Lifecycle：

```text
Episode -> Dream -> Semantic Memory -> Identity Memory
```

也支持慢速 identity updates，以避免 catastrophic overwriting。

## 5. Neural Networks and Continual Learning

### Continual Learning

参考：[A Comprehensive Survey of Continual Learning: Theory, Method and Application](https://pubmed.ncbi.nlm.nih.gov/38407999/)

相关性：

- 随时间学习；
- catastrophic forgetting；
- stability-plasticity tradeoff；
- rehearsal、regularization、modularity、replay methods。

与 01 的关系：

01 当前关注 State Growth，而不是 Weight Growth。

这很重要，因为 parameter updates 会引入 catastrophic forgetting 和安全挑战。

但 01 仍应向 continual learning 学习：

- 保护重要知识；
- 允许适应；
- 测试遗忘；
- 测量 stability-plasticity tradeoff。

## 6. 可借鉴的工程领域

### Operating Systems

可借鉴：

- virtual memory，
- paging，
- snapshots，
- process state，
- garbage collection，
- logs，
- recovery，
- permission boundaries。

### Databases

可借鉴：

- schema migration，
- transactions，
- provenance，
- audit logs，
- rollback，
- access control，
- data retention policies。

### Distributed Systems

可借鉴：

- state synchronization，
- eventual consistency，
- conflict-free replicated data types，
- consensus，
- versioning，
- fault recovery。

### Software Testing

可借鉴：

- state transition unit tests，
- session recovery integration tests，
- memory bug regression tests，
- identity overwrite adversarial tests，
- cross-user leakage privacy tests。

## 7. Open Research Gap

现有工作覆盖了许多部件：

- memory retrieval，
- reflection，
- context management，
- cognitive architectures，
- narrative identity，
- sleep consolidation，
- continual learning。

01 Project 的缺口是整合：

> 如何把这些部件变成一个 state-continuous artificial identity，使其 memory、task state、self-model、relationships 和 conflicts 能够跨时间保持可审计连续？

这就是研究纲领。
