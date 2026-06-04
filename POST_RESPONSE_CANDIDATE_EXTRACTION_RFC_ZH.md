# 回应后候选抽取 RFC

English version: [POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md](./POST_RESPONSE_CANDIDATE_EXTRACTION_RFC.md)

状态：`P145`、`RFC-only`、`document-only`、`non-runtime`。

P145 定义 future model output 在 response 之后如何被检查为 candidates。它不实现 extraction、model calls、response generation、candidate storage、review lifecycle、event writes、memory writes、recall writes、identity mutation、tool execution、policy executor、adapter integration 或 rebuild。

## 核心规则

```text
extraction 是 inspection。
inspection 不是 persistence。
candidate 不是 promotion。
model output remains untrusted。
```

## Candidate Types

future extraction 可以识别：

- `memory_candidate`
- `claim_candidate`
- `task_update_candidate`
- `meaning_shift_candidate`
- `growth_candidate_review`
- `recall_event_candidate`
- `identity_claim_candidate`
- `temporal_review_candidate`
- `tool_candidate`
- `procedure_candidate`
- `capability_evidence_candidate`
- `quarantine_candidate`

所有 extracted items 在 manual review 前都必须 preview-only。

## 必需 Candidate Fields

每个 extracted candidate 应包含：

- `candidate_type`
- `source_output_ref`
- `claim_text_or_summary`
- `why_detected`
- `trust_level`
- `risk_flags`
- `review_gate`
- `blocked_promotions`
- `preview_only: true`
- `persisted: false`
- `promoted: false`

## Candidate Routing

| Candidate | Review Gate | Default Outcome |
|---|---|---|
| memory candidate | memory review | preview only |
| claim candidate | claim review | evidence check |
| task update candidate | task review | manual planning |
| meaning shift candidate | growth/meaning review | no promotion |
| recall event candidate | recall write policy review | no write |
| identity claim candidate | identity high gate | reject or quarantine by default |
| temporal review candidate | temporal review | symbolic only |
| tool/procedure candidate | capability review | no execution |
| capability evidence candidate | tool authorization review | evidence only |
| quarantine candidate | quarantine review | containment |

## CTM-Inspired Temporal Extraction

Temporal extraction 可以注意：

- elapsed-time claims；
- delayed realization language；
- unresolved tension；
- coherence break language；
- review depth suggestions。

它不得写 temporal events、recall events、thought traces、salience changes、identity updates 或 CTM runtime state。

## Tool-First Extraction

Capability extraction 可以注意：

- tool suggestions；
- reusable procedures；
- verification evidence；
- failed execution notes；
- capability improvement language。

它不得授权工具、执行工具、晋升工具、安装依赖、写 tool-library entries，或把 capability improvement 当成 subject growth。

## Rejection And Quarantine

Candidate extraction 应支持 rejection 和 quarantine，而不只是 positive routing。

Unsafe 或 low-provenance output 应路由到：

- `quarantine_candidate`
- `reject_as_prompt_contamination`
- `defer_pending_founder_review`
- `false_positive_review`

## 未来测试预期

如果后续实现，tests 应验证：

- extracted candidates remain preview-only；
- no candidate is persisted or promoted；
- identity claims route to high gate；
- temporal candidates remain symbolic；
- capability candidates do not enable tools；
- quarantine candidates do not write storage；
- model output does not mutate state。

## 完成声明

P145 把 post-response extraction 定义为 review surface，而不是 write path。它允许 future model output 被检查，但不能变成 memory、identity、authority、growth、tool trust 或 state。
