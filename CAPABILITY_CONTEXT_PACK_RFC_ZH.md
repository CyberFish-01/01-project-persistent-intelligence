# 能力上下文包 RFC

English version: [CAPABILITY_CONTEXT_PACK_RFC.md](./CAPABILITY_CONTEXT_PACK_RFC.md)

状态：`P142`、`RFC-only`、`document-only`、`non-runtime`。

P142 使用 Tool-First In-Situ Self-Evolution vocabulary 定义 future context packages 的 `capability_pack`。它不实现 tool execution、tool verification runtime、tool promotion、tool library mutation、dependency installation、policy executor、model calls、adapter integration、state writes、memory writes、identity mutation 或 rebuild。

## 核心规则

```text
capability_pack 是 evidence context。
evidence 不是 authorization。
candidate 不是 tool-library entry。
capability evolution 不是 subject growth。
```

## Pack 目的

future `capability_pack` 帮助 founder 或 model-as-resource 看见 tool/procedure pressure，同时不意外启用工具。

它应让 capability evidence 可审查，而不是可执行。

## 允许字段

pack 可以包含：

- `tool_candidate`
- `procedure_candidate`
- `verification_evidence_preview`
- `execution_failure_note`
- `reproducibility_hint`
- `cautionary_procedural_memory_candidate`
- `capability_growth_candidate_review`
- `tool_authorization_gate`
- `quarantine_route`
- `capability_boundary_reminder`

## 禁止字段

pack 不得包含：

- executable tool handle；
- shell command to run；
- dependency install instruction；
- credential 或 token；
- policy executor rule；
- trusted tool-library entry；
- automatic promotion decision；
- subject growth claim；
- self-modifying runtime instruction。

## Capability Cue Matrix

| Cue | Meaning | Allowed Use | Forbidden Interpretation |
|---|---|---|---|
| tool candidate | 一个 tool-like idea 可能有用。 | 路由到 review。 | tool 已可执行。 |
| procedure candidate | 一个 reusable process 可能存在。 | 描述 review target。 | procedure 已可信。 |
| verification evidence | 一个 result 可能支持 confidence。 | 增加 review confidence。 | authorization granted。 |
| failure note | 一个 failure 可能有警示价值。 | 路由到 cautionary candidate。 | tool 应该全局禁用。 |
| reproducibility hint | repetition 可能重要。 | 请求 future evidence。 | 一次成功就足够。 |
| authorization gate | 需要 human approval。 | 阻止 promotion。 | gate 已批准。 |

## Tool-First Mapping

P142 保持 Tool-First research line：

- tool improvement 是 capability evolution，不是 identity growth；
- procedure reuse 是 candidate，不是 trusted skill；
- verification result 是 evidence，不是 authorization；
- review object 不是 execution；
- unsafe candidate 路由到 quarantine 或 caution。

## Boundary Injection

每个 `capability_pack` 必须包含：

- `tool_execution_allowed: false`
- `tool_promotion_allowed: false`
- `auto_tool_promotion_allowed: false`
- `policy_executor_allowed: false`
- `dependency_install_allowed: false`
- `tool_library_mutation_allowed: false`
- `identity_growth_claim_allowed: false`

这些是 planned contract fields，不是 P142 已实现 runtime flags。

## 与其他 Packs 的关系

`capability_pack` 不应替代：

- `task_pack`：tasks 仍需要 manual planning；
- `boundary_pack`：forbidden capabilities 仍是 global；
- `claim_pack`：capability claims 仍需要 evidence；
- `response_strategy_pack`：future model instructions 仍需要 no-execution wording。

## 未来测试预期

如果后续实现，tests 应验证：

- capability pack 只在 relevant 时出现；
- every capability item is candidate/evidence/review only；
- forbidden tool actions remain false；
- no executable handle is emitted；
- no dependency install is suggested；
- no capability item mutates identity or memory；
- unsafe items route to quarantine or caution。

## 完成声明

P142 给 Tool-First In-Situ Self-Evolution 一个安全位置：在 future context packages 中保持 candidate/evidence/review only，绝不变成 execution、promotion、policy 或 subject growth。
