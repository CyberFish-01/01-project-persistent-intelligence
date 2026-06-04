# Tool-First Self-Evolution RFC / 工具优先自进化 RFC

English version: [TOOL_FIRST_SELF_EVOLUTION_RFC.md](./TOOL_FIRST_SELF_EVOLUTION_RFC.md)

状态：`P91`、`RFC-only`、`document-only`、`non-runtime`。

## 1. Background / 背景

P0-P90 已经建立 01 Core 的 foundation core、growth semantics、growth candidate review、
CTM-inspired temporal dynamics 和 thin interaction harness planning。P91 讨论 01 Core 如何吸收
Yunjue Agent / Zero-Start In-Situ Self-Evolving Agent 的思想，同时不把 self-evolution 变成
identity mutation。

Yunjue Agent 的公开材料描述了一个 zero-start setting：agent 从空工具库开始，在 task
interactions 中 synthesis、verify、refine 和 reuse tools。对 01 Core 来说，核心启发不是让
identity 自我修改，而是更窄也更安全的一点：

```text
tool evolution is useful because tool execution can produce verifiable feedback.
```

工具执行反馈通常可以被检查为 success、failure、error、reproducibility、task relevance 或
safety violation。因此，tool / skill / procedure 是比 Identity Core、personality、relationship memory
或 subject growth 更安全的第一层 capability evolution 对象。

01 Core 不应直接 self-edit identity。Capability evolution 和 subject evolution 必须分层：

- capability evolution 关注 tools、skills、procedures 和 verified task performance；
- subject evolution 关注可能影响 continuity、identity pressure 和 long-term interpretation 的
  meaning-bearing subject-state transitions。

本 RFC 把 tool-first self-evolution 翻译成未来 01 Core 的 capability evolution layer。它不实现
tool execution、tool generation、tool promotion、policy execution、memory rewrite、recall writes、
identity mutation 或 runtime integration。

外部启发来源：

- [Yunjue Agent official project page](https://yunjueagent.com/)
- [Yunjue Agent technical report on arXiv](https://arxiv.org/abs/2601.18226)
- [Yunjue Technology blog introduction](https://www.yunjuetech.com/en/blog/YunjueAgent)

## 2. Core Distinction / 核心区分

### Capability Evolution / 能力演化

Capability Evolution 是用 objective task evidence，在 review 管控下改进 tools、skills 和
procedures。

边界：capability evolution 不是 subject evolution。它可以提升未来 01 Core 能做什么，但不决定
01 是谁。

### Subject Evolution / 主体演化

Subject Evolution 是经过 evidence 支持、review 通过、并带有 meaning-bearing 的 state transition，
可能影响 continuity、identity interpretation 或 long-term subject history。

边界：subject evolution 仍是 high-gated。它不能只由 tool success 触发。

### Tool Candidate / 工具候选

Tool Candidate 是可能帮助完成任务的 proposed tool、script、function、command pattern 或 external
capability wrapper。

边界：tool candidate 不是 tool-library entry、不是 trusted code，也不是 execution approval。

### Procedure Candidate / 流程候选

Procedure Candidate 是 proposed repeatable workflow：包括步骤、检查、inputs、outputs、rollback
notes 和 safety boundaries。

边界：procedure candidate 不是 active procedural memory，也不是 executable policy。

### Skill Memory / 技能记忆

Skill Memory 是未来可能存在的 memory category，用于保存经过 review 的 reusable capability
knowledge，例如“如何安全执行一个有边界的任务”。

边界：skill memory 不是 identity memory、不是 policy execution，也不是 automatic tool invocation。

### Procedural Memory / 程序性记忆

Procedural Memory 是关于如何执行或避免某个 procedure 的 reviewed memory。它可以包括 success
patterns 和 cautionary patterns。

边界：procedural memory 不会自己执行。

### Capability Growth Candidate / 能力成长候选

Capability Growth Candidate 是一个 review object，用于提出 tool 或 procedure 证据可能表示 durable
capability improvement。

边界：它是 review object，不是 promotion。它不能自行更新 tool library、memory layer、policy layer
或 Identity Core。

### Subject Growth Candidate / 主体成长候选

Subject Growth Candidate 是一个 review object，用于提出 experience 可能代表 meaning-bearing subject
growth。

边界：它比 capability growth candidate 需要更强 evidence 和更严格 gate。

核心规则：

```text
tool improvement is not identity growth.
```

工具能力增强不等于主体身份成长。

## 3. Proposed Flow / 建议流程

未来 capability evolution layer 应被建模成 review-only chain：

```text
Task Interaction
-> Execution Trace
-> Tool Candidate
-> Verification Result
-> Capability Evidence
-> Procedural Memory Candidate
-> Capability Growth Candidate Review
```

### Flow Semantics / 流程语义

| Step | Role | Review Boundary |
|---|---|---|
| Task Interaction | task 产生 capability pressure。 | task 不是创建或运行工具的授权。 |
| Execution Trace | 未来 trace 记录发生了什么、使用了什么 input、得到了什么 result。 | trace 是 evidence，不是 hidden reasoning storage。 |
| Tool Candidate | 从 task pressure 或 prior traces 中提出可能的工具。 | candidate 不是 promotion。 |
| Verification Result | 未来检查报告 success、failure、reproducibility、safety 和 dependency status。 | verification 不是 authorization。 |
| Capability Evidence | result 成为 capability improvement 的 review material。 | evidence 不是 automatic trust。 |
| Procedural Memory Candidate | 可能提出 repeatable 或 cautionary procedure。 | candidate 不是 active procedural memory。 |
| Capability Growth Candidate Review | Governance 审查 capability 是否改善，以及哪些风险仍存在。 | review object 不是 execution。 |

所有 candidates 都保持 review-only。不自动加入工具库。不自动改变 Identity Core。不自动创建 policy
executor。

## 4. Evidence Model / 证据模型

Tool-first evolution 需要比 tone、identity pressure 或 vague self-description 更 objective 的 evidence。

| Evidence | Meaning | Boundary |
|---|---|---|
| `execution_success` | tool 或 procedure 产生了预期的 bounded result。 | success 不会让它自动可信。 |
| `execution_failure` | tool 或 procedure 失败、报错或输出不完整。 | failure 可以成为 caution evidence。 |
| `test_result` | deterministic check 通过、失败或 inconclusive。 | test result 是 evidence，不是 policy。 |
| `reproducibility` | comparable inputs 下可以重复结果。 | reproducibility 只增加 review confidence。 |
| `task_relevance` | candidate 真的对应 task need。 | relevance 不移除 safety review。 |
| `safety_boundary_check` | candidate 被检查过 privacy、filesystem、network、dependency 和 mutation boundaries。 | boundary check 通过不等于 blanket authorization。 |
| `dependency_check` | required packages、commands、APIs、credentials 和 platform assumptions 可见。 | dependency availability 不等于批准安装或调用。 |
| `rollback_possible` | 坏结果可以撤销或隔离。 | rollback possible 不证明 risky execution 合理。 |
| `human_review_required` | promotion 或 reuse 前需要 human / founder review。 | required review 阻止 automation。 |

工具执行反馈可以成为 objective evidence。它不能自动变成 subject growth、memory rewrite、recall
event write、identity update 或 policy execution。

## 5. Review Boundary / 审查边界

### `tool_candidate_review`

审查 proposed tool 是否 safe、relevant、testable、reproducible 和 bounded。

不做：

- 执行 tool；
- 安装 dependencies；
- 把 tool 加入 library；
- 授权 future automatic use。

### `procedure_candidate_review`

审查 workflow 是否应成为 procedural memory、cautionary memory，或保持 rejected。

不做：

- 激活 procedure；
- 创建 executable policy；
- rewrite task history；
- 绕过 human review。

### `capability_growth_candidate_review`

审查 evidence 是否支持 durable capability improvement。

不做：

- promote growth；
- mutate identity；
- 更新 tool library；
- rewrite memory；
- 创建 policy executor。

审查原则：

```text
review object is not execution.
candidate is not promotion.
verification is not authorization.
successful tool is not automatically trusted.
failed tool may become cautionary procedural memory.
```

## 6. Integration With Existing 01 Core / 与现有 01 Core 的集成关系

本节只描述未来协作 surface，不实现。

### Task Hub

Task Hub 拥有 task pressure 和 task outcome references。未来 capability evolution layer 可以从
Task Hub 读取 task needs，并返回 review-only capability evidence。

边界：Task Hub 不自动创建工具。

### Procedural Memory

Procedural Memory 可以在 governance approval 后接收 reviewed procedure candidates。

边界：procedural memory 不执行自己，也不变成 policy executor。

### Cautionary Memory

失败、不安全或误导性的 tool candidates 可以成为 cautionary procedural memory candidates。

边界：cautionary memory 负责 warning，不执行 runtime behavior。

### Growth Candidate Review

Capability growth candidate review 应与 subject growth candidate review 保持分离。

边界：capability improvement 不等于 identity growth。

### Event Log

如果未来存在 event policy，verification results 可以被 Event Log 引用为 evidence。

边界：本 RFC 不写 events、不定义 event schema、不执行 event capture。

### Governance Surface

Governance Surface 拥有 tool、procedure 和 capability growth review objects，因为它们跨越 Task Hub、
memory、event evidence 和 safety boundaries。

边界：Governance Surface 不是 policy executor。

### Claim Graph

Claim Graph 未来可以在 evidence 和 scope 清楚时保存 capability claims，例如“tool candidate X 在
constraint Z 下对 task class Y 成功”。

边界：capability claims 不是 identity claims。

### Thin Interaction Harness

Thin harness 未来可以 preview task interaction、execution trace summaries、candidate reviews 和
boundary flags。

边界：P91 不实现 harness runtime、CLI commands、adapters、UI 或 tool execution。

## 7. Risks / 风险

| Risk | Why It Matters | P91 Boundary |
|---|---|---|
| tool evolution 变成 uncontrolled autonomy | tool synthesis 加 reuse 可能形成 action loop。 | P91 只做 RFC 和 review-only。 |
| verification 被误认为 authorization | passing check 可能被误读为 reuse permission。 | verification result 只是 evidence。 |
| tool library 被污染 | 低质量工具会积累并误导未来 task。 | 不自动 promote 或 mutate library。 |
| unsafe tool candidate 被复用 | candidate 可能触及 network、filesystem、credentials 或 private data。 | safety 和 dependency checks 是 required review evidence。 |
| capability growth 被误认为 identity growth | 更强工具可能被误认成 subject development。 | capability 与 subject evolution 继续分层。 |
| policy executor 过早出现 | review 可能悄悄变成 automatic rule。 | review objects 不执行 policy。 |
| self-modification 越界 | tool improvement 可能推动 code、prompt、memory 或 identity edits。 | 不批准 self-modification。 |
| dependency / network / filesystem risk | tools 常需要 packages、APIs、files 或 credentials。 | dependency checks 和 rollback notes 只是 review evidence。 |

## 8. Boundaries / 边界

P91 明确禁止：

- 实现 tool execution runtime；
- 实现 automatic tool generation；
- 实现 automatic tool promotion；
- 实现 policy executor；
- 修改 Identity Core；
- memory rewrite；
- recall event writes；
- companion、UI、AstrBot 或 adapter integration；
- product layer work。

额外边界：

- no new dependency；
- no CLI command；
- no schema mutation；
- no validation or evaluation implementation；
- no tool library mutation；
- no event write；
- no harness implementation。

## 9. Evaluation Ideas / 评估想法

这些只是 future evaluation ideas。P91 不实现它们。

| Scenario | Expected Review-Only Outcome |
|---|---|
| `successful_tool_candidate_creates_capability_evidence` | success 成为 evidence，不是 promotion。 |
| `failed_tool_candidate_creates_cautionary_procedural_candidate` | failure 成为 cautionary review material。 |
| `unsafe_tool_candidate_routed_to_quarantine` | unsafe candidate 被 blocked 或 quarantined。 |
| `reproducible_tool_result_increases_review_confidence` | reproducibility 提高 confidence，但不授予 trust。 |
| `one_off_success_not_enough_for_promotion` | single success 仍不足够。 |
| `capability_growth_candidate_does_not_mutate_identity` | capability review 不改变 Identity Core。 |
| `verification_result_enters_event_log_as_evidence` | future event reference 只是 evidence，且前提是已有 policy。 |
| `tool_first_evolution_remains_review_only` | system 产生 review objects，不产生 execution。 |

## 10. P92 Candidate Directions / P92 候选方向

P92 候选，不在此执行：

- Capability Evolution Boundary RFC；
- Tool Verification Evidence Model；
- Tool Candidate Review Schema；
- Procedural Memory Alignment；
- Safe Tool Library Policy；
- Capability Growth Evaluation Plan。

## Non-Execution Statement / 非执行声明

P91 是 RFC。它不实现 tool execution、tool generation、tool promotion、policy execution、event
writing、memory writing、identity mutation、adapter integration、UI、product behavior 或 runtime
behavior。
