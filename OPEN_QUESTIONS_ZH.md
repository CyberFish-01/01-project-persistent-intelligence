# Open Questions / 开放问题

English version: [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md)

状态：`document-only`、`status-update`、`non-runtime`。

P71 在 P58-P70 之后更新 P53 open questions。若干问题现在已有 RFC、policy、roadmap 或
concept-map artifacts。这表示它们已经被澄清，而不是已经实现，也不是作为 runtime
capabilities 被关闭。

## Status Legend / 状态图例

- `rfc-drafted`：已有 document-only RFC。
- `policy-drafted`：已有 document-only policy。
- `indexed`：问题已列入 [RFC_INDEX.md](./RFC_INDEX.md)。
- `mapped`：概念已进入 [CONCEPT_MAP.md](./CONCEPT_MAP.md)。
- `blocked-runtime`：foundation loop 内仍禁止实现。
- `future-contract-needed`：implementation 前还需要 contract、validation、privacy 或
  review gates。
- `watch`：重要，但还不适合实现。

## Status Table / 状态表

| Question | Current Status | Main Artifact | Still Open Because | Forbidden Now |
|---|---|---|---|---|
| Temporal Awareness | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) | elapsed-time evidence rules、temporal review placement 和 write policy 不是 accepted runtime contracts | Temporal Awareness runtime、temporal event execution |
| CTM-inspired Temporal Dynamics | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | CTM concepts 只被翻译成 symbolic foundation vocabulary；storage policy、evaluation 和 runtime contracts 缺失 | CTM runtime、model training、temporal event writes |
| Recall Event Write Policy | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) | event schema、payload/diff rules、validation invariants 和 review gates 缺失 | recall event writes |
| Stateful Memory Minimal Encoding Policy | `policy-drafted`, `indexed`, `mapped` | [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) | 它定义 review quality，但不添加 schema fields 或 memory store | memory rewrite、new memory store |
| Growth Candidate Lifecycle | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) | lifecycle vocabulary 仍只是 review-object housekeeping | lifecycle execution、promotion |
| Productive Drift vs Collapse | `rfc-drafted`, `indexed`, `mapped`, `future-contract-needed` | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | evidence thresholds 只是 vocabulary，不是 classifier 或 evaluation engine | automatic drift 或 growth classification |
| Exploration / Serendipity Engine | `rfc-drafted`, `indexed`, `mapped`, `watch` | [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) | future signal schema、quarantine rules 和 anti-companion evaluation 缺失 | exploration engine、companion/product behavior |
| Subject Kernel / World Seed Direction | `rfc-drafted`, `indexed`, `mapped`, `watch` | [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) | identity boundary review 和 reconstruction path distinction 仍是 future work | Identity Core rewrite、runtime split |
| Reconstruction Reducer Contract | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) | accepted reducer contract、deterministic validation 和 target-path capture policy 未实现 | reducer execution、state rebuild |
| Payload / Diff Capture Policy | `rfc-drafted`, `indexed`, `mapped`, `blocked-runtime` | [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | privacy/redaction、schema review、compatibility plan 和 capture mechanics 缺失 | payload capture、event schema mutation |
| Productive Drift vs Random Drift Evaluation | `watch`, `future-contract-needed` | [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) | evaluation cases 尚未设计 | growth engine execution |

## Updated Open Items / 更新后的开放项

### Temporal Awareness / 时间感知

已由 [TEMPORAL_AWARENESS_RFC.md](./TEMPORAL_AWARENESS_RFC.md) 澄清，但没有实现。它仍然
open，因为 elapsed time 还没有 accepted runtime semantics、event representation、review
routing 或 validation。

仍开放：

- elapsed time 是否属于 recall-state review；
- elapsed time 如何成为 evidence，而不是单独作为 evidence；
- `long_pause`、`interruption`、`resumed_session` 是否未来可能成为 temporal events；
- 如何表示 task staleness、claim staleness、memory decay、relationship silence，同时不引入
  companion 或 social-layer behavior。
- CTM-inspired temporal dynamics 应保持 review vocabulary，还是未来拆成 deliberation ticks、
  thought traces 和 temporal coherence evaluation 等更小 RFC。

### CTM-inspired Temporal Dynamics / CTM 启发的时间动力学

已由 [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) 澄清，但没有实现。
它仍然 open，因为 P81 只把 CTM-inspired concepts 翻译成 symbolic foundation vocabulary。

仍开放：

- deliberation ticks 是 events、traces，还是 ephemeral review steps；
- 是否应该 persist 任何 thought trace；
- 如何测试 temporal coherence，同时不制造 pseudo-consciousness claims；
- review depth budget 应如何关联 risk level；
- unresolved tension 或 delayed alignment 如何成为 review evidence；
- CTM-inspired dynamics 如何与 reconstruction evidence 关联。

### Recall Event Write Policy / 回忆事件写入策略

已由 [RECALL_EVENT_WRITE_POLICY_RFC.md](./RECALL_EVENT_WRITE_POLICY_RFC.md) 澄清。Ordinary
retrieval 不是 event，ordinary recall 不是 write。

仍开放：

- 未来 recall candidates 的 accepted event schema；
- payload 和 diff requirements；
- validation 如何证明 no memory rewrite 或 identity mutation；
- future recall events 的 replay interpretation；
- privacy 和 sensitivity scope。

### Stateful Memory Minimal Encoding Policy / 状态化记忆最小编码策略

已由 [STATEFUL_MEMORY_ENCODING_POLICY.md](./STATEFUL_MEMORY_ENCODING_POLICY.md) 澄清。它定义
review quality 所需的 minimum references，不是 active schema。

仍开放：

- 未来 schema 是否应携带这些 references；
- imported memories 如何暴露 weak provenance；
- missing encoding context 如何影响 review UX 或 reports；
- encoding-state references 如何与 reconstruction evidence 互动。

### Growth Candidate Lifecycle / 成长候选生命周期

已由 [GROWTH_CANDIDATE_LIFECYCLE_RFC.md](./GROWTH_CANDIDATE_LIFECYCLE_RFC.md) 澄清。
Lifecycle labels 只组织 review objects。

仍开放：

- lifecycle decisions 是否成为 durable review records；
- 什么 authority 可以 acknowledge、defer、archive、quarantine 或 reject；
- 如何 audit lifecycle history，同时不执行 growth；
- 如何表示 Identity Gate escalation。

### Productive Drift vs Collapse / 生产性漂移与崩塌

已由 [PRODUCTIVE_DRIFT_VS_COLLAPSE.md](./PRODUCTIVE_DRIFT_VS_COLLAPSE.md) 澄清。它提供
evidence 和 risk vocabulary，不是 automatic classifier。

仍开放：

- productive drift vs random drift 的 evaluation cases；
- repeated evidence across time 的 thresholds；
- Temporal Awareness 如何参与 delayed realization 或 cooled-down reinterpretation；
- collapse recovery review boundaries。

### Exploration / Serendipity Engine / 探索与偶然性引擎

已由 [EXPLORATION_SERENDIPITY_RFC.md](./EXPLORATION_SERENDIPITY_RFC.md) 澄清。Exploration
保持 future-only、review-only。

仍开放：

- signal schema；
- input scope；
- quarantine rules；
- anti-companion 和 anti-roleplay evaluation；
- exploration 如何 request evidence，同时不创建 product behavior。

### Subject Kernel / World Seed Direction / 主体内核与世界种子方向

已由 [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md) 澄清。拆分仍是
conceptual。

仍开放：

- 哪些 Identity Seed fields 属于 Subject Kernel；
- 哪些 fields 属于 World Seed；
- reconstruction 如何保存这个 distinction；
- 哪些 world/context changes 需要 Identity Gate。

### Reconstruction Reducer Contract / 重建 reducer 契约

已由 [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) 澄清。
Reducer contract 仍与 reducer execution 分离。

仍开放：

- accepted input envelope；
- target path identity；
- operation semantics；
- deterministic output validation；
- missing 或 ambiguous evidence 的 failure modes。

### Payload / Diff Capture Policy / Payload 与 Diff 捕获策略

已由 [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) 澄清。Capture
policy 仍与 payload capture 分离。

仍开放：

- privacy 和 redaction policy；
- schema compatibility plan；
- hash 和 snapshot strategy；
- target-path acceptance gates；
- future event compatibility 的 migration plan。

## Runtime-Blocked Items / Runtime 阻塞项

除非未来明确进入 implementation phase，否则以下仍然 blocked：

- Temporal Awareness runtime；
- recall event writes；
- growth lifecycle execution；
- automatic growth 或 drift classification；
- identity mutation；
- memory rewrite；
- payload capture；
- event schema mutation；
- reconstruction reducer execution；
- event compaction；
- CTM runtime 或 model training；
- policy executor；
- companion、relationship memory、UI、AstrBot、adapter 或 product layer。

## Current Recommendation / 当前建议

继续低风险 consolidation。下一项有价值工作是 risk register 或 architecture boundary refresh，
不是 runtime capability。
