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
| Temporal Coherence Evaluation | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | deterministic scenarios 和 future signals 已规划，但还没有 tests 或 runtime metrics | temporal runtime、thought loop execution、event writes |
| Deliberation Tick / Review Depth | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | tick 和 review-depth vocabulary 已存在，但没有 tick runtime、thought loop 或 review policy executor | tick runtime、thought loop execution、policy execution |
| Thought Trace Storage Policy | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md) | storage boundaries 已定义，但没有 trace schema、storage backend、redaction policy 或 approval gate | trace storage、hidden chain-of-thought capture、private reasoning persistence |
| Thin Interaction Harness | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | preview surfaces 已命名，但没有 CLI、runtime、context builder、review queue 或 boundary monitor | harness runtime、UI、adapter integration、mutation path |
| Conversation Intake Contract | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | envelope fields 已命名，但没有 intake runtime、API、CLI、adapter ingest、privacy validation 或 storage policy | conversation runtime、adapter ingest、event write |
| Context Package Preview | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | selected/omitted reference vocabulary 已存在，但没有 harness preview、retrieval execution、activation trace write 或 storage policy | retrieval as continuity、context mutation、activation trace writes |
| Review Queue Preview | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | candidate preview 和 ordering vocabulary 已存在，但没有 queue runtime、storage、lifecycle execution 或 approval path | queue execution、lifecycle execution、candidate approval |
| Session Resume Scenario Plan | `planned`, `indexed`, `future-contract-needed`, `blocked-runtime` | [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) | deterministic scenarios 已存在，但没有 harness、tests、temporal runtime、temporal events 或 salience policy | session runtime、temporal event write、memory decay |
| Core Interaction Harness Roadmap | `roadmap-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) | readiness 已评估，但缺 fixture contract、output contract、boundary test plan 和 explicit implementation approval | harness implementation、CLI commands、runtime work |
| Tool-First Self-Evolution | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) | capability evolution vocabulary 已存在，但没有 tool execution、verification schema、review schema、safe tool library policy 或 promotion gate | tool execution、auto tool generation、auto tool promotion、policy executor |
| Capability Evolution Boundary | `rfc-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) | allowed / forbidden scope 已定义，但缺 verification evidence model、candidate review schema、safe tool library policy 和 implementation gates | automatic tool execution、automatic promotion、policy executor、identity mutation |
| Visual Naming / Founder-Facing Vocabulary | `guide-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) | internal keys 已映射为中文显示名，但仍缺 visual surface contract、status assignment policy 和 dashboard approval | Web UI、dashboard runtime、observability CLI、product layer |
| Foundation Observatory Report | `report-drafted`, `indexed`, `future-contract-needed`, `blocked-runtime` | [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) | 已有 Markdown founder-facing report，但没有 CLI、dashboard runtime、status API、automatic report generator 或 product surface | dashboard runtime、observability CLI、status API、product UI |
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
  companion 或 social-layer behavior；
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

### Temporal Coherence Evaluation / 时间一致性评估

已由 [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md)
澄清，但没有实现。它仍然 open，因为 P82 只定义 deterministic scenario ideas 和 future
evaluation signals。

仍开放：

- temporal coherence 未来应成为 report、validator，还是 manual review checklist；
- 如何 score evidence alignment，同时不把 score 变成 runtime truth；
- 如何 simulate deliberation ticks，同时不执行 thought loop；
- 如何在没有 storage policy 时测试 thought traces；
- 如何把 coherence evaluation 接到 reconstruction evidence，同时不执行 reducer。

### Deliberation Tick / Review Depth / 审议 Tick 与审查深度

已由 [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md)
澄清，但没有实现。它仍然 open，因为 P83 只定义 review-planning vocabulary。

仍开放：

- review depth 应手动指定，还是由 future evaluation 计算；
- `blocked` 是 review depth，还是 separate boundary outcome；
- preview ticks 多少才有用，超过多少会让 review 过重；
- review depth 应如何与 future thought trace storage policy 互动；
- thin harness 如何 preview review depth，同时不执行 thought loop。

### Thought Trace Storage Policy / 思考轨迹存储策略

已由 [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md)
澄清，但没有实现。它仍然 open，因为 P84 只定义 storage boundaries，没有创建 trace
storage、schemas、redaction rules 或 approval gates。

仍开放：

- trace candidates 是否应该被存储；
- 未来 traces 是 events、reports、governance records，还是 ephemeral preview output；
- sensitive user content 需要什么 redaction policy；
- reconstruction 如何使用 trace summaries，同时不依赖 private reasoning；
- 谁或什么 gate 可以批准 future trace storage decision。

### Thin Interaction Harness / 薄交互试验台

已由 [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) 澄清，但没有实现。
它仍然 open，因为 P85 只定义 preview-only surfaces，没有创建 CLI、runtime、context builder、
review queue、boundary monitor、UI 或 adapter integration。

仍开放：

- 第一个 harness 应该是 CLI-only、report-only，还是 fixture-only；
- 什么 minimal conversation envelope 能证明 platform does not own identity；
- 哪些 preview output 可以被存储，同时不变成 trace storage 或 event writes；
- context preview 如何避免把 continuity 降成 retrieval；
- review queue preview 如何避免 lifecycle execution。

### Conversation Intake Contract / 对话输入合同

已由 [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) 澄清，
但没有实现。它仍然 open，因为 P86 只定义 envelope boundary，没有创建 runtime intake、
adapter ingestion、event writes、privacy validation 或 context building。

仍开放：

- `content_ref` 应指向 fixture text、redacted text，还是 source metadata；
- `privacy_scope` 是否应在 harness work 前固定；
- 多少 timestamp information 是安全的，同时不会制造 Temporal Awareness runtime pressure；
- `context_request` 应 explicit、inferred，还是 absent；
- interaction work 前需要什么 minimal cross-user privacy test。

### Context Package Preview / 上下文包预览

已由 [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) 澄清，但没有实现。
它仍然 open，因为 P87 只定义 selected/omitted reference vocabulary，没有执行 retrieval、mutate
context、persist activation traces 或 build prompts。

仍开放：

- preview output 应包含 exact selected text，还是只包含 references 和 summaries；
- token budget notes 如何避免变成 salience mutation；
- privacy-suppressed omitted references 是否可见；
- governance refs 如何出现，同时不变成 policy execution；
- context gaps 应创建 review candidates，还是保持 preview-only。

### Review Queue Preview / 审查队列预览

已由 [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) 澄清，但没有实现。它仍然
open，因为 P88 只定义 candidate preview 和 ordering vocabulary，没有创建 queue runtime、storage、
lifecycle execution 或 approval paths。

仍开放：

- queue previews 应按 risk、age、evidence strength，还是 owner boundary 排序；
- blocked candidates 应保持可见，还是移到 separate blocked view；
- queue preview reports 能否被存储，同时不变成 lifecycle history；
- future harness 中 context gaps 能否创建 review candidates；
- low-risk items 如何避免 review overload。

### Session Resume Scenario Plan / 会话恢复场景计划

已由 [SESSION_RESUME_SCENARIO_PLAN.md](./SESSION_RESUME_SCENARIO_PLAN.md) 澄清，但没有实现。
它仍然 open，因为 P89 只定义 deterministic scenario plans，没有创建 tests、harness runtime、
temporal events、memory decay、salience mutation 或 resume automation。

仍开放：

- Temporal Awareness runtime 存在前，哪些 elapsed-time buckets 有用；
- unknown gaps 是否应与 known gaps 区分；
- context gaps 能否创建 queue candidates；
- stale task pressure 与 stale claim pressure 应如何区分；
- resume scenarios 是否应在 harness implementation 前变成 deterministic tests。

### Core Interaction Harness Roadmap / Core 交互试验台路线图

已由 [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) 澄清，但没有
实现。它仍然 open，因为 P90 只是 roadmap，不批准 CLI commands、schemas、tests、runtime work 或
harness implementation。

仍开放：

- fixture input contract；
- preview output contract；
- no-write validation invariants；
- forbidden-output test plan；
- privacy 和 redaction policy；
- 任何 future implementation phase 都需要 explicit founder approval。

### Tool-First Self-Evolution / 工具优先自进化

已由 [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md) 澄清，但没有实现。
它仍然 open，因为 P91 只把 capability evolution layer 定义为 review vocabulary，没有创建 tool
execution、auto tool generation、auto tool promotion、tool library mutation、policy execution 或
identity mutation。

仍开放：

- future tool candidate review schema 应包含什么；
- verification evidence 如何表示，同时不变成 authorization；
- failed tool candidates 如何成为 cautionary procedural memory candidates；
- 什么 gate 区分 capability growth candidate review 和 subject growth candidate review；
- safe tool library policy 如何阻止 pollution、unsafe reuse、dependency risk、network risk 和
  filesystem risk；
- capability evidence 是否只能通过 reference 进入 Event Log，以及需要哪种 future event policy。

### Capability Evolution Boundary / 能力演化边界

已由 [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md) 澄清，但没有实现。
它仍然 open，因为 P92 只定义 allowed / forbidden scope，没有定义 verification evidence model、tool
candidate review schema、safe tool library policy、procedural memory alignment contract 或 capability
growth evaluation plan。

仍开放：

- future tool verification evidence 应包含哪些确切字段；
- tool candidate review 如何区分 proposal、verification、authorization 和 promotion；
- reusable procedure candidates 如何与 Procedural Memory 对齐，同时不变成 trusted tools；
- safe tool library policy 如何阻止 contamination 和 unsafe reuse；
- 哪些 evaluation cases 能证明 capability candidates 不 mutate identity；
- future tool authorization 前需要什么 human / founder review gate。

### Visual Naming / Founder-Facing Vocabulary / 视觉命名与创始人可读词汇

已由 [VISUAL_NAMING_GUIDE.md](./VISUAL_NAMING_GUIDE.md) 澄清，但没有实现。它仍然 open，
因为 P93 只定义 naming rules 和 display-card shape。它不创建 Foundation Observatory、
dashboard、Web UI、observability CLI、report generator、status API 或 product surface。

仍开放：

- 哪些概念未来值得放入 founder-facing visual cards；
- 谁来分配 `已实现`、`报告层`、`RFC 层`、`未来方向` 和 `危险过早`；
- 如何防止 RFC-only concepts 被显示成已实现；
- 如何防止 candidate labels 被显示成 promoted results；
- 如何审查 bilingual display names 与 English internal keys 的 drift；
- 未来 Observatory 在创始人明确批准后应是 docs-only、report-only、CLI-only，还是 UI-based。

### Foundation Observatory Report / 地基观察台报告

已由 [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) 澄清，但没有实现成
runtime surface。它仍然 open，因为 P94 只创建 Markdown report。它不创建 dashboard runtime、
Web UI、observability CLI、automatic report generator、status API、product surface 或 runtime
monitor。

仍开放：

- future observatory output 应保持 Markdown-only，还是获得 CLI report boundary；
- status assignment 是否需要单独的 Visual Status Assignment Policy；
- future CLI 如何避免变成 dashboard runtime；
- report 应从文件生成、手动维护，还是作为 phase artifact 保留；
- 任何 observability tool 出现前需要什么 founder-approved gate。

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
- thought loop execution；
- tick runtime execution；
- hidden chain-of-thought capture；
- private model reasoning persistence；
- thought trace storage；
- thin harness runtime；
- conversation intake runtime；
- adapter ingestion for harness work；
- context builder execution；
- retrieval execution as continuity；
- activation trace writes for harness previews；
- review queue execution；
- queue storage；
- candidate approval；
- session resume runtime；
- scenario tests for harness work；
- memory decay；
- salience mutation；
- tool execution runtime；
- automatic tool generation；
- automatic tool promotion；
- tool library mutation；
- self-modifying runtime；
- unreviewed dependency installation；
- uncontrolled filesystem 或 network access；
- Web UI；
- dashboard runtime；
- Foundation Observatory runtime；
- observability CLI；
- status API；
- automatic report generator；
- product-layer visual surface；
- harness implementation；
- fixture schema；
- output schema；
- policy executor；
- companion、relationship memory、UI、AstrBot、adapter 或 product layer。

## Current Recommendation / 当前建议

继续 document-only planning，除非项目创始人明确批准 implementation phase。P94 report 建议先做
founder / CTO review；如果创始人选择继续 observability 路线，再考虑 Minimal Observatory CLI RFC。
