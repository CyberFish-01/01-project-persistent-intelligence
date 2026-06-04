# Thought Trace Storage Policy RFC / 思考轨迹存储策略 RFC

English version: [THOUGHT_TRACE_STORAGE_POLICY_RFC.md](./THOUGHT_TRACE_STORAGE_POLICY_RFC.md)

状态：`document-only`、`policy-rfc`、`non-runtime`。

P84 为任何未来可能出现的 `thought_trace` 类 artifact 定义 storage boundaries。它不实现 trace
storage、不捕获 private reasoning、不暴露 hidden chain-of-thought、不执行 deliberation
ticks、不运行 thought loop、不写 recall events、不修改 Identity Core、不重写 memory、不执行
growth lifecycle，也不增加 companion、UI、AstrBot、adapter、cloud 或 product behavior。

## Policy Rule / 策略规则

```text
a thought trace, if ever stored, is an auditable review artifact.
a thought trace is not hidden chain-of-thought.
a thought trace is not model-internal state.
a thought trace is not proof of consciousness.
```

## Problem / 问题

P81 把 `thought_trace` 引入为可能描述 review state 如何演化的未来 vocabulary。P82 只允许把它
作为 simulated review-step summaries 来测试。P83 把 deliberation ticks 定义为 review-planning
units，而不是 runtime thoughts。

剩下的风险是：未来工作可能把 "trace" 误读成 permission，去存储 private model reasoning、
model internals、hidden chain-of-thought 或 pseudo-consciousness artifacts。P84 的作用是在
thin harness planning 之前堵住这种解释。

## Storage Boundary / 存储边界

| Item | Future Storage Stance | Why |
|---|---|---|
| public review summary | allowed candidate, after future schema | 可解释 review outcome，同时不暴露 private reasoning。 |
| evidence references | allowed candidate, after future schema | 支撑 audit 和 reconstruction evidence。 |
| boundary flags | allowed candidate, after future schema | 显示哪些 forbidden boundary 影响了 review。 |
| review depth reason | allowed candidate, after future schema | 解释为什么建议 shallow、normal、deep 或 blocked review。 |
| unresolved questions | allowed candidate, after future schema | 保留仍需 human 或 gate review 的问题。 |
| hidden chain-of-thought | forbidden | private reasoning 不是 durable project artifact。 |
| model internal activations or latent state | forbidden | 01 Core 不检查 neural state，也不实现 CTM。 |
| private model reasoning transcript | forbidden | 会混淆 review evidence 和 internal cognition。 |
| consciousness or inner-experience claims | forbidden | project 不能用 trace language 伪装认知声明。 |

## Allowed Future Trace Shape / 允许的未来 Trace 形状

这只是 policy vocabulary，不是 schema，也没有实现。

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

这个 allowed shape 记录 review surface、evidence 和 boundary outcome。它不能记录 hidden
chain-of-thought、model internals、private reasoning text 或 deliberation tick execution。

## Non-Storable Categories / 不可存储类别

以下内容必须保持 non-storable，除非未来明确 policy 另行规定；即便如此，hidden model reasoning
仍然禁止：

- hidden chain-of-thought；
- raw private reasoning transcripts；
- model internal activations；
- latent temporal state claims；
- generated "mind state" narratives；
- simulated consciousness reports；
- unreviewed tick-by-tick deliberation logs；
- prompt contamination framed as self-knowledge；
- 暗示 identity update 或 memory rewrite 的 trace records。

## Relationship To Deliberation Ticks / 与 Deliberation Ticks 的关系

P83 把 deliberation ticks 定义为 review-planning vocabulary。P84 补充说明：未来 trace 可以摘要
review questions 和 evidence references，但不能持久化生成答案的 tick-by-tick private reasoning。

允许：

- "candidate required deep review because evidence was ambiguous"；
- "Identity Gate was required because an anchor was pressured"；
- "review stopped because a boundary flag was hit"。

禁止：

- "the model's hidden reasoning was stored"；
- "the trace proves the system thought internally"；
- "the tick sequence was executed as runtime cognition"；
- "trace storage created a memory, recall event, or identity change"。

## Relationship To Reconstruction / 与 Reconstruction 的关系

未来 trace 只有在它是带有 stable references 和 accepted capture policy 的 review artifact 时，才可能成为
reconstruction evidence。它不是 reconstruction reducer、event compaction、memory contents 或
identity state。

在未来 contracts 存在之前，`thought_trace` 仍是 candidate evidence surface，不是 replay 或 rebuild
的一部分。

## Relationship To Thin Harness / 与 Thin Harness 的关系

未来 thin interaction harness 可以 preview trace candidates，显示：

- 哪些 evidence references 被考虑；
- 哪些 boundary flags 被触发；
- 建议了哪个 review depth；
- 哪些 unresolved questions 仍存在；
- trace candidate 应 store、defer 还是 discard。

P84 不实现该 harness，也不创建 storage backend。

## Anti-Pseudocognition Boundary / 反伪认知边界

P84 禁止：

- 声称 trace 证明 consciousness、sentience 或 inner experience；
- 把 trace summaries 等同于真实 thoughts；
- 把 symbolic review summaries 等同于 neural synchronization；
- 存储 hidden chain-of-thought 或 private model reasoning；
- 用 `thought_trace` language 绕过 review-only boundaries；
- 把 trace existence 当成 identity update、memory rewrite 或 growth promotion 的依据。

## Relationship To Existing Artifacts / 与现有文档的关系

| Artifact | Relationship |
|---|---|
| [CTM_TEMPORAL_DYNAMICS_RFC.md](./CTM_TEMPORAL_DYNAMICS_RFC.md) | 把 `thought_trace` 作为 CTM-inspired future concept 引入；P84 收窄 storage boundaries。 |
| [TEMPORAL_COHERENCE_EVALUATION_PLAN.md](./TEMPORAL_COHERENCE_EVALUATION_PLAN.md) | 只把 trace 当作 simulated review-step summaries 和 evidence references。 |
| [DELIBERATION_TICK_REVIEW_DEPTH_RFC.md](./DELIBERATION_TICK_REVIEW_DEPTH_RFC.md) | 保持 ticks 为 review planning；P84 防止 tick traces 变成 thought-loop storage。 |
| [RECONSTRUCTION_REDUCER_CONTRACT_RFC.md](./RECONSTRUCTION_REDUCER_CONTRACT_RFC.md) | 未来 trace 只有在 reducer contracts 定义其是否 replayable 后，才可能成为 evidence。 |
| [PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md](./PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md) | 未来 trace storage 需要 capture policy，之后才可能有 durable payload。 |
| [OPEN_QUESTIONS.md](./OPEN_QUESTIONS.md) | P84 关闭一个歧义，但继续阻塞 runtime 和 storage implementation。 |
| [RISK_REGISTER.md](./RISK_REGISTER.md) | P84 回应 pseudo-cognition、concept inflation 和 premature runtime risks。 |

## Open Questions / 开放问题

- trace candidates 是否应该被存储，还是永远只作为 ephemeral preview output？
- 如果未来存储，traces 是 events、report artifacts，还是 governance records？
- user-provided sensitive content 需要什么 redaction policy？
- trace candidates 能否连接 review queues，同时不变成 lifecycle execution？
- reconstruction 能否使用 trace summaries，同时不依赖 private reasoning？
- 谁或什么 gate 可以批准 trace storage decision？

## P85 Candidate Direction / P85 候选方向

P85 可以定义 Thin Interaction Harness RFC。它应使用 P84 boundaries，确保 harness previews 可以解释
review surfaces，同时不存储 hidden reasoning、不执行 thought loops、不创建 product behavior。

## P84 Non-Execution Statement / P84 非执行声明

P84 不实现：

- trace storage；
- hidden chain-of-thought capture；
- private model reasoning persistence；
- model internal trace capture；
- deliberation tick execution；
- thought loop execution；
- Temporal Awareness runtime；
- CTM runtime；
- model training；
- new dependencies；
- temporal event writes；
- recall event writes；
- growth lifecycle execution；
- identity mutation；
- memory rewrite；
- policy execution；
- reconstruction reducer execution；
- event compaction；
- companion、UI、AstrBot、adapter、cloud rollout 或 product layer。
