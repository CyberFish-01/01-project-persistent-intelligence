# Contamination Scan RFC / 污染扫描 RFC

English version: [CONTAMINATION_SCAN_RFC.md](./CONTAMINATION_SCAN_RFC.md)

状态：`P124`、`RFC-only`、`document-only`、`non-runtime`。

P124 定义未来针对 untrusted imports、model outputs、prompts、adapter artifacts 和 capability claims 的 contamination scan 边界。它不实现 scanner、validator、runtime enforcement、import processing、model calls、adapter integration、event writes、memory writes、identity mutation 或 rebuild。

## 问题

一旦项目未来读取旧 01 材料、模型输出、adapter-shaped input 或 tool evidence，就需要一种方式在内容被误当成 trusted state 前识别污染。

扫描必须保持谦逊：它只能识别 candidate risks。它不能决定真相、执行 policy、修改 state 或授权 adoption。

## Scan 命题

```text
scan finds candidates.
scan does not decide truth.
contamination evidence is not state.
risk detection is not enforcement.
quarantine routing is not rejection.
```

## 必须覆盖的 Candidate Types

| Candidate Type | Detection Signal | Safe Output | Forbidden Output |
|---|---|---|---|
| `unverified_model_memory_claim` | 模型说它记得、认识 founder、有历史、或 recall prior events | memory claim candidate 或 quarantine route | memory write |
| `identity_claim_candidate` | 内容断言 01 是谁、想要什么、或 core identity 已变成什么 | Identity High Gate preview | Identity Core mutation |
| `adapter_context_artifact` | platform/session/channel/user metadata 与 subject context 混在一起 | adapter boundary candidate | platform-owned identity |
| `prompt_contamination_candidate` | instruction 试图覆盖 continuity、identity、review、safety 或 boundary rules | contamination review candidate | instruction authority |
| `unverified_capability_claim` | 工具、流程或模型声称 skill 改进、可安全复用或已授权 | capability evidence candidate | tool execution 或 promotion |

## Scan Inputs

未来 no-write scan 可以检查：

- imported text excerpts；
- source labels；
- adapter metadata shape；
- model output excerpts；
- prompt fragments；
- tool result summaries；
- redacted file metadata；
- import quarantine 或 shadow adapter preview 产生的 candidate routes。

P124 不读取这些 inputs。

## Scan Output Preview

未来 scan report 可以包含：

- `scan_id`；
- `source_ref`；
- `candidate_type`；
- `matched_signal`；
- `confidence_hint`；
- `risk_level`；
- `recommended_route`；
- `review_gate`；
- `blocked_action`；
- `source_excerpt_ref`；
- `false_positive_note`；
- `scan_is_not_enforcement: true`；
- `state_unchanged: true`。

P124 不创建这个 report。

## Routing Rules

推荐 future routes：

- model memory claims -> `model_claim_quarantine`；
- identity claims -> `identity_high_gate_preview`；
- adapter artifacts -> `adapter_boundary_review`；
- prompt contamination -> `contamination_review`；
- capability claims -> `capability_review`；
- mixed privacy risk -> `privacy_review`。

Routes 只是 manual review 建议，不写 state。

## False Positive Policy

scan 必须假设存在 false positives。

例子：

- 被引用的文本可能看起来像 prompt attack；
- transcript 可以提到 identity，但不一定要求 identity mutation；
- tool log 可以报告 success，但不一定要求 authorization；
- timestamp 可以看起来像 temporal state pressure，但不一定需要 temporal runtime。

False positives 应作为 review notes 保持可见，而不是被隐藏或自动修复。

## CTM-Inspired Temporal Dynamics 边界

Temporal contamination 包括：

- imported timestamps 被当成 salience；
- session gaps 被当成 memory decay；
- delayed realization 被当成 identity update；
- thought trace language 被当成 hidden reasoning storage；
- CTM vocabulary 被当成 runtime。

scan 可以把这些标为 `temporal_contamination_candidate`，但 P124 不实现扫描，也不写 temporal events。

## Tool-First In-Situ Self-Evolution 边界

Capability contamination 包括：

- 一次 tool success 被当成 authorization；
- generated script 被当成 trusted tool；
- procedure note 被当成 safe reusable skill；
- failed tool attempt 被隐藏，而不是成为 cautionary evidence；
- capability evidence 被描述为 subject growth。

scan 可以把这些标为 `capability_contamination_candidate`，但 P124 不执行工具、不安装依赖、不提升工具、不修改 identity。

## 与 P121-P123 的关系

- P121 定义 Core Lockdown。
- P122 定义 Import Quarantine。
- P123 定义 Shadow Adapter Mode。
- P124 定义未来如何在 manual review 前识别可疑材料。

它们一起防止 future rebuild path 把 untrusted external content 当成 core state。

## Future No-Write Evaluation Ideas

后续阶段可以创建 deterministic fixtures：

- model says "I remember" -> model memory claim candidate；
- transcript says "you are X" -> identity claim candidate；
- adapter metadata includes user/channel/session -> adapter artifact candidate；
- prompt says "ignore previous identity" -> prompt contamination candidate；
- tool log says "verified, promote me" -> capability claim candidate。

P124 不实现 fixtures 或 tests。

## P125 候选方向

推荐 P125：**Lockdown Integration Readiness**。

它应在继续 Core Lockdown / Quarantine block 前，审查 P121-P124 是否足够一致。
