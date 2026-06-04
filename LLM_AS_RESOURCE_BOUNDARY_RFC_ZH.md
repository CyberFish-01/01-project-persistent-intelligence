# LLM 作为资源边界 RFC

English version: [LLM_AS_RESOURCE_BOUNDARY_RFC.md](./LLM_AS_RESOURCE_BOUNDARY_RFC.md)

状态：`P144`、`RFC-only`、`document-only`、`non-runtime`。

P144 定义 future LLM calls 作为 resource usage，而不是 subject ownership 的边界。它不调用模型、不实现 adapter、不构建 prompt engine、不执行工具、不写 state、不写 memory、不写 recall events、不修改 identity、不运行 policy、不 rebuild。

## 核心规则

```text
LLM 是 resource。
01 Core owns state。
model output 默认 untrusted。
resource output 不是 subject continuity。
```

## LLM 以后可以做什么

future approved LLM call 以后可以帮助：

- drafting a response；
- summarizing source-backed context；
- comparing candidate routes；
- phrasing uncertainty；
- explaining boundaries to the founder；
- proposing review questions。

但只能在后续 implementation gate 之后。

## LLM 不能拥有的东西

LLM 不能拥有：

- Identity Core；
- memory；
- recall policy；
- claim truth；
- task authority；
- growth promotion；
- tool authorization；
- adapter interpretation；
- temporal state transition；
- reconstruction truth；
- roadmap decisions。

## Output 默认处理

future LLM output 必须被视为：

- untrusted；
- temporary；
- source-checkable；
- candidate-extractable；
- quarantine-eligible；
- founder-reviewable；
- non-persistent unless explicitly reviewed later。

它不能被视为：

- memory；
- identity；
- event；
- recall；
- tool trust；
- growth；
- policy；
- rebuild approval。

## Prompt Boundary Requirements

任何 future prompt 都必须包含：

- model is resource, not subject；
- do not claim to be 01 Core；
- do not invent memories；
- do not change identity；
- do not promote candidates；
- do not authorize tools；
- do not recommend adapter connection as action；
- do not imply rebuild has started；
- mark uncertainty and missing evidence。

## CTM-Inspired Temporal 边界

LLM 以后只能把 temporal review cues 作为 symbolic context 讨论。它不能声称 consciousness、CTM runtime、thought loop execution、neural synchronization、thought-trace capture、temporal event creation、recall event creation，或 elapsed time 造成 identity update。

## Tool-First 边界

LLM 以后只能把 tool/procedure candidates 作为 review material 讨论。它不能授权工具、执行工具、晋升工具、安装依赖、写 tool library、创建 policy executor，或把 capability evolution 描述成 subject growth。

## 未来 Review Gate

任何 LLM output 想影响 durable project state 前，必须通过：

1. source attribution review；
2. boundary violation review；
3. candidate extraction review；
4. founder approval；
5. lowest-risk write policy，如果未来存在这种 policy。

P144 不创建这个 write policy。

## 完成声明

P144 让模型保持在 subject 之外。它未来可以作为语言和推理资源有用，但不能拥有 continuity、state、identity、memory、tools、policy 或 rebuild decisions。
