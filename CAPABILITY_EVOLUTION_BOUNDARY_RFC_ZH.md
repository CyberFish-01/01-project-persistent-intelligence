# Capability Evolution Boundary RFC / 能力演化边界 RFC

English version: [CAPABILITY_EVOLUTION_BOUNDARY_RFC.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC.md)

状态：`P92`、`RFC-only`、`document-only`、`non-runtime`。

## Background / 背景

P91 已经把 Tool-First Self-Evolution 定义为更安全的自进化起点：tools、skills 和 procedures 可以产生
verifiable task feedback，而 Identity Core、memory rewrite、relationship memory 和 subject growth
保持受保护。

P92 定义 Capability Evolution 的边界，防止 tool-first self-evolution 滑向 automatic tool
execution、automatic tool promotion、policy execution 或 identity mutation。

本 RFC 不实现 runtime behavior、schemas、CLI commands、tool execution、dependency installation、
event writes、policy execution、memory rewrite、identity mutation、adapter integration、UI 或 product
behavior。

## 1. Core Distinctions / 核心区分

### Capability Evolution / 能力演化

Capability Evolution 是用 task evidence，在 review 管控下改进 tools、skills 和 procedures。

边界：capability improvement does not imply identity growth。

### Subject Evolution / 主体演化

Subject Evolution 是可能影响 continuity、identity interpretation 或 long-term subject history 的
meaning-bearing subject-state transition。

边界：subject evolution 仍是 high-gated，不能只从 tool success 推导出来。

### Tool Candidate / 工具候选

Tool Candidate 是 proposed tool、script、function、command pattern 或 external capability wrapper。

边界：tool candidate 不是 trusted tool，也不是 execution approval。

### Procedure Candidate / 流程候选

Procedure Candidate 是包含 steps、checks、inputs、outputs、rollback notes 和 safety boundaries 的
proposed repeatable workflow。

边界：reusable procedure does not imply trusted tool。

### Skill Memory / 技能记忆

Skill Memory 是未来可能保存 reviewed、reusable capability knowledge 的 memory category。

边界：skill memory 不执行 tools，也不更新 identity。

### Procedural Memory / 程序性记忆

Procedural Memory 是关于如何执行或避免某个 procedure 的 reviewed memory。它可以包含 success
patterns 和 cautionary patterns。

边界：procedural memory 不是 policy executor。

### Capability Evidence / 能力证据

Capability Evidence 是由 task results、verification results、failures、reproducibility、safety
checks、dependency checks 或 rollback notes 产生的 review material。

边界：evidence 支持 review；它不授权 action。

### Capability Growth Candidate / 能力成长候选

Capability Growth Candidate 提出 evidence 可能表示 durable capability improvement。

边界：它不是 tool promotion、不是 subject growth，也不是 identity change。

### Subject Growth Candidate / 主体成长候选

Subject Growth Candidate 提出 experience 可能代表 meaning-bearing subject growth。

边界：它需要比 capability growth candidate 更严格的 review。

### Tool Authorization / 工具授权

Tool Authorization 是未来 explicit permission gate，用于在明确 scope、inputs、outputs、dependencies
和 rollback conditions 下执行或 promote 工具。

边界：authorization 不能只由 verification 创建。

### Tool Verification / 工具验证

Tool Verification 是未来 evidence process，用于检查 candidate 是否 worked、failed、reproduced、
stayed within boundaries，并保持 task-relevant。

边界：verification does not imply authorization。

核心规则：

```text
Capability improvement does not imply identity growth.
Verification does not imply authorization.
Reusable procedure does not imply trusted tool.
```

## 2. Boundary Model / 边界模型

### Allowed Scope / 允许范围

Capability Evolution 未来可以允许这些 review-only activities：

| Allowed Activity | Meaning | Boundary |
|---|---|---|
| tool candidate proposal | 描述一个 possible tool，供 review。 | 不执行，不 promote。 |
| procedure candidate proposal | 描述一个 repeatable workflow，供 review。 | 不是 active procedural memory。 |
| verification evidence collection | 未来检查可以收集 success、failure、reproducibility、safety、dependency 和 rollback evidence。 | evidence collection 不是 authorization。 |
| review-only capability growth candidate | governance object 审查 capability 是否改善。 | candidate 不是 promotion。 |
| cautionary procedural memory candidate | failed 或 unsafe pattern 被提出为 warning material。 | warning candidate 不是 executable policy。 |

### Forbidden Scope / 禁止范围

Capability Evolution 不允许：

- automatic tool execution；
- automatic tool promotion；
- automatic policy executor；
- automatic identity update；
- automatic memory rewrite；
- uncontrolled filesystem 或 network access；
- unreviewed dependency installation；
- self-modifying runtime。

即使 candidate 成功过一次，这些仍然 blocked。

## 3. Evidence and Review / 证据与审查

Evidence 可以提高 review quality，但不能授权 action。

| Evidence / Review Signal | Interpretation | Boundary |
|---|---|---|
| `execution_success` | candidate 产生了预期 bounded result。 | evidence，不是 authorization。 |
| `execution_failure` | candidate 失败、报错或产生 unsafe output。 | 可以成为 cautionary evidence。 |
| `reproducibility` | comparable conditions 下结果可重复。 | 只提高 review confidence。 |
| one-off success | 单次成功发生过。 | 不足以 promotion。 |
| unsafe candidate | candidate 违反或施压 safety boundary。 | route to quarantine。 |
| human / founder review | human authority 审查 promotion scope。 | 仍是 promotion gate。 |

审查含义：

- `execution_success` 可以作为 evidence，但不是 authorization。
- `execution_failure` 可以成为 cautionary evidence。
- reproducibility 提高 review confidence。
- one-off success 不足以 promotion。
- unsafe candidate 进入 quarantine。
- human / founder review 仍是 promotion gate。

## 4. Integration With Existing Core / 与现有 Core 的集成

本 RFC 只描述未来 integration boundaries。

### Task Hub

Task Hub 提供 task pressure、task context 和 task outcome references。

边界：Task Hub 不自动创建或运行工具。

### Procedural Memory

Procedural Memory 未来可以接收 approved procedure candidates。

边界：procedure candidates 在 review 前不是 active procedural memory。

### Cautionary Memory

Cautionary Memory 未来可以把 failed 或 unsafe procedure candidates 接收为 warning material。

边界：cautionary memory 负责 warning，不执行 policy。

### Event Log

如果未来存在 event policy，Event Log 可以把 verification results 作为 audit evidence 引用。

边界：P92 不写 events，也不定义 event schemas。

### Governance Surface

Governance Surface 拥有 tool candidates、procedure candidates、capability evidence 和 capability
growth candidates 等跨层 review objects。

边界：Governance Surface 不是 policy executor。

### Growth Candidate Review

Growth Candidate Review 应保持 capability growth candidate review 和 subject growth candidate
review 分离。

边界：capability growth candidate 不 mutate identity。

### Tool-First Self-Evolution RFC

P91 说明为什么 tool-first self-evolution 比 identity-first self-modification 更安全。

边界：P92 把 P91 收窄为明确的 allowed / forbidden boundary classes。

### Thin Interaction Harness

Thin Interaction Harness 未来可以 preview tool candidates、procedure candidates、verification
evidence、quarantine state 和 review routing。

边界：P92 不实现 harness runtime、CLI commands、adapter work、UI 或 product behavior。

## 5. Risk Register / 风险台账

| Risk | Description | Boundary Response |
|---|---|---|
| tool library contamination | 低质量或 unsafe candidates 变成 reusable。 | 不自动 promote；未来需要 safe library policy。 |
| unsafe reusable procedures | repeatable procedure 可能 repeat harm。 | failed 或 unsafe procedures 路由到 caution/quarantine。 |
| verification over-trust | passing checks 被当成 authorization。 | verification 只保持 evidence。 |
| policy executor creep | review rules 变成 automatic runtime policy。 | review objects 不执行。 |
| capability growth mistaken as subject growth | 更好的工具被解释成 identity development。 | capability 和 subject evolution 保持分层。 |
| dependency / filesystem / network risk | candidates 需要 packages、files、APIs、credentials 或 network。 | dependency 和 safety checks 是 required review evidence。 |
| self-modification risk | capability work 施压 runtime、prompt、code、memory 或 identity edits。 | self-modifying runtime 仍禁止。 |
| hidden autonomy | tool proposal、verification、reuse 和 promotion 形成 invisible loop。 | human / founder promotion gate 仍必需。 |

## 6. Evaluation Ideas / 评估想法

这些只是 future evaluation ideas。P92 不实现它们。

| Scenario | Expected Review-Only Outcome |
|---|---|
| `successful_tool_candidate_remains_review_only` | success 创建 evidence，不执行也不 promote。 |
| `failed_tool_candidate_becomes_cautionary_candidate` | failure 成为 cautionary procedural candidate。 |
| `one_off_success_rejected_for_promotion` | 单次成功不足够。 |
| `unsafe_tool_candidate_routed_to_quarantine` | unsafe candidate 被 quarantined 或 blocked。 |
| `reproducible_result_increases_review_confidence` | reproducibility 增加 confidence，但不授权。 |
| `capability_candidate_does_not_mutate_identity` | capability review 不改变 Identity Core。 |
| `verification_result_enters_audit_trail_only` | verification result 只作为 evidence 或 audit reference。 |

## 7. P93 Candidate Directions / P93 候选方向

P93 候选，不在此执行：

- Tool Verification Evidence Model；
- Tool Candidate Review Schema；
- Procedural Memory Alignment；
- Safe Tool Library Policy；
- Capability Growth Evaluation Plan。

## Non-Execution Statement / 非执行声明

P92 只做 RFC。它不实现 tool execution、automatic tool generation、automatic tool promotion、policy
execution、identity mutation、memory rewrite、growth execution、dependency installation、filesystem
access、network access、adapter integration、UI、product behavior 或 runtime behavior。
