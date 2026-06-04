# 回应编排预览 RFC

English version: [RESPONSE_ORCHESTRATION_PREVIEW_RFC.md](./RESPONSE_ORCHESTRATION_PREVIEW_RFC.md)

状态：`P143`、`RFC-only`、`document-only`、`non-runtime`。

P143 定义 future response orchestration preview path。它不实现 orchestration、prompt building、model calls、response generation、post-response extraction、state writes、memory writes、recall writes、identity mutation、adapter integration、tool execution、policy executor 或 rebuild。

## 核心规则

```text
orchestration preview 不是 orchestration。
model output 不是 core state。
response plan 不是 response execution。
```

## 未来预览流程

future response orchestration preview 可以显示：

1. conversation intake preview；
2. input pressure classification；
3. context package preview；
4. boundary injection preview；
5. model-as-resource response strategy；
6. expected post-response candidate extraction surfaces；
7. manual review gates；
8. non-execution invariants。

P143 不执行这个流程。

## Response Strategy Preview

preview 可以描述未来模型应如何被指示：

- 作为 resource 回答；
- 不声称自己是 01 Core；
- 不创建 identity claims；
- 除非 source backing，否则不声称 memory；
- 让 candidates 保持 candidates；
- 标记 uncertainty 和 missing evidence；
- 保持 CTM temporal boundaries；
- 保持 Tool-First capability boundaries；
- action-like next steps 前请求 founder review。

## 输出预览 Sections

未来 preview output 可以包含：

- `response_orchestration_preview_only`
- `intake_summary`
- `context_package_summary`
- `boundary_summary`
- `model_resource_strategy`
- `candidate_extraction_plan`
- `manual_review_gates`
- `blocked_actions`
- `non_execution_invariants`

## CTM-Inspired Temporal 边界

preview 可以提到 temporal review cues 和 review depth。它不能执行 deliberation ticks、thought loops、temporal runtime、CTM runtime、thought-trace storage、temporal event writes、recall event writes、memory salience mutation 或 identity updates。

## Tool-First 边界

preview 可以提到 tool candidates、procedure candidates、verification evidence 和 capability review gates。它不能执行工具、授权工具、晋升工具、安装依赖、修改工具库，或把 capability evolution 变成 subject growth。

## Post-Response 边界

未来 model output 默认必须被视为 untrusted。

它只能成为：

- candidate extraction input；
- quarantine candidate；
- founder review material；
- temporary report evidence。

它不能直接成为：

- memory；
- identity；
- recall event；
- event log entry；
- task update；
- claim truth；
- tool authorization；
- growth promotion。

## 未来测试预期

如果后续实现，tests 应验证：

- preview runs without model calls；
- preview includes context package and boundary summaries；
- response strategy says model is resource, not subject；
- post-response output is candidate-only；
- all forbidden capabilities remain false；
- no state or memory files change。

## 完成声明

P143 把 response orchestration path 定义为先可预览、后才可能执行的东西。它让 future model 保持在 subject ownership 之外，并把 response planning 与 response generation 分开。
