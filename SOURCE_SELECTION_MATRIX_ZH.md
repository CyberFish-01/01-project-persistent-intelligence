# 来源选择矩阵

English version: [SOURCE_SELECTION_MATRIX.md](./SOURCE_SELECTION_MATRIX.md)

状态：`P139`、`matrix`、`document-only`、`non-runtime`。

P139 定义 future context package previews 的 source selection rules。它不实现 retrieval、ranking、builder、CLI command、model call、prompt execution、state write、memory write、recall write、identity mutation、adapter integration、tool execution、policy executor 或 rebuild。

## 选择原则

```text
source selection 是 explanation。
selection 不是真相。
omission 必须可见。
trust level 必须跟随 source。
```

## Pack 选择矩阵

| Pack | Preferred Sources | Include When | Omit When | Required Explanation |
|---|---|---|---|---|
| `identity_pack` | `FOUNDATION`、identity seed docs、architecture boundaries | 需要 identity anchors 或 high gates。 | Source 是 candidate、external 或 identity-changing。 | 解释 protected anchor 和 mutation block。 |
| `state_pack` | current phase index、observatory reports、readiness reviews | 需要当前项目状态。 | Source stale 或不是 local/approved。 | 解释 status date 和 source class。 |
| `task_pack` | roadmap、phase plan、review artifacts | 需要 next-step 或 blocked-work context。 | task 暗示 automatic execution。 | 解释 candidate status 和 manual approval need。 |
| `claim_pack` | RFCs、reviews、evidence maps | claim 需要 citation 或 uncertainty。 | Claim 缺 provenance 或只有 model assertion。 | 解释 evidence level 和 review gate。 |
| `memory_pack` | memory policy、stateful memory docs、source-backed refs | memory semantics 相关。 | 会暗示 memory restoration 或 rewrite。 | 解释 retrieval is not continuity。 |
| `boundary_pack` | boundary RFCs、risk register、no-write contracts | 任何 forbidden action 相关。 | global safety boundaries 永不省略。 | 解释 blocked capabilities。 |
| `temporal_pack` | temporal awareness、CTM RFC、coherence evaluation | time、delay、review depth 或 tension 相关。 | 会暗示 runtime 或 thought execution。 | 解释 symbolic/review-only status。 |
| `capability_pack` | Tool-First RFC、capability boundary、risk reviews | tool/procedure/evidence pressure 相关。 | 会暗示 authorization 或 execution。 | 解释 evidence is not authorization。 |
| `response_strategy_pack` | LLM-as-resource future boundary、context package RFC、non-claims | future model response 需要 guardrails。 | strategy 会像 execution approval。 | 解释 model is resource, not subject。 |

## Source Trust Matrix

| Trust Level | Meaning | Allowed Use |
|---|---|---|
| `trusted_foundation` | 稳定项目边界或 accepted foundation text。 | 可以 anchor pack explanations。 |
| `source_backed` | 有 citation 的 whitelisted local doc 或 report。 | 可以支持 previews。 |
| `review_only` | 不授权 action 的 review/RFC language。 | 可以把 decisions 路由到 gates。 |
| `candidate_only` | Proposed concept、next step 或 unreviewed item。 | 只能作为 candidate 出现。 |
| `quarantined` | 等待 review 的 external 或 untrusted material。 | 只能显示为 risk。 |
| `omitted` | 相关但被排除的 source。 | 必须包含 omission reason。 |
| `blocked` | source 或 action 超出 allowed boundary。 | 必须显示 block reason。 |

## Omission Reasons

未来 previews 应区分：

- `not_relevant`
- `stale`
- `not_approved_source`
- `external_or_untrusted`
- `identity_risk`
- `write_path_risk`
- `adapter_risk`
- `model_call_risk`
- `tool_execution_risk`
- `rebuild_risk`

Omission 是 report 的一部分，不是 silent failure。

## CTM-Inspired Temporal Selection

只有当 input 或 phase 涉及这些内容时，才可以选择 temporal sources：

- elapsed time；
- resumed session；
- interruption；
- unresolved tension；
- delayed alignment；
- review depth；
- thought-trace boundary。

它们必须标为 symbolic 和 review-only。它们不能证明 temporal events、recall events、thought loops、hidden traces、salience mutation 或 identity change。

## Tool-First Capability Selection

只有当 input 或 phase 涉及这些内容时，才可以选择 capability sources：

- tool candidate；
- procedure candidate；
- verification evidence；
- capability review；
- cautionary procedural memory；
- tool authorization boundary。

它们必须标为 candidate/evidence/review only。它们不能证明 tool execution、tool promotion、dependency installation、tool-library mutation 或 subject growth。

## 未来测试预期

如果 source selection 后续被实现，tests 应验证：

- every selected source has a reason；
- every omitted relevant source has a reason；
- trust level is present on every source；
- no quarantined source is promoted；
- forbidden actions 相关时 boundary sources 不能省略；
- temporal 和 capability sources 保持 review-only；
- no selection mutates state。

## 完成声明

P139 把 source selection 变成可见矩阵。它防止 future context packages 用 retrieval language 隐藏 trust、omission 或 review boundaries。
