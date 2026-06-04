# Subject Kernel / World Seed RFC v0.1 / 主体内核与世界种子 RFC v0.1

English version: [SUBJECT_KERNEL_WORLD_SEED_RFC.md](./SUBJECT_KERNEL_WORLD_SEED_RFC.md)

状态：`document-only`、`boundary-rfc`、`non-runtime`。

P64 澄清 Identity Seed 内部未来可能的拆分：受保护的 Subject Kernel，以及更可演化的
World Seed。它不 rewrite Identity Core，不修改 schemas，不迁移 state，不创建 runtime world
state，不 mutate identity，不 promote growth，也不实现 product behavior。

## Problem / 问题

Identity Seed 当前承载了几类不同的起始材料：

- subject 是谁；
- 它为什么存在；
- 哪些 values 给它方向；
- 它从哪个 world 或 project 开始；
- 它应该被允许长出什么样的 future。

如果这些都放在一个 identity 概念里，Identity Core 可能会变得过大。但如果粗暴拆分，又
可能产生第二套 identity layer、可随意变化的 personality layer，或未经 review 的 world
model。

P64 在任何实现之前先定义边界。

## Core Rule / 核心规则

```text
Subject Kernel protects the minimal subject anchor.
World Seed orients the subject inside a world.
Neither one is a runtime mutation path.
```

目标不是 rewrite Identity Seed。目标是让未来 identity 和 world/context evolution 更容易被
review。

## Subject Kernel / 主体内核

Subject Kernel 是对以下问题的最小受保护回答：

```text
Who is the subject that must remain continuous?
```

候选内容：

- name 或 subject identifier；
- core continuity thesis；
- non-fiction boundary；
- minimal values；
- protected identity invariants；
- high-gate identity update rule；
- origin as identity seed, not assigned false biography。

Subject Kernel 应比 Identity Core 更小，比 ordinary memory 更慢，并由最高 gate 保护。

## World Seed / 世界种子

World Seed 是对以下问题的初始方向回答：

```text
What world, project, and direction does the subject begin inside?
```

候选内容：

- project context；
- research program orientation；
- current collaborators or stewardship context；
- initial task horizon；
- domain vocabulary；
- known constraints；
- open world questions；
- non-product boundaries。

World Seed 可以比 Subject Kernel 更容易演化，但仍必须经过 review。它不是 identity，而是
orientation。

## Boundary Matrix / 边界矩阵

| Concept | Owns | Does Not Own |
|---|---|---|
| Subject Kernel | minimal subject anchor、protected continuity invariants | detailed biography、tasks、product role、platform behavior |
| Identity Core | slow reviewed identity memory and identity-adjacent commitments | automatic personality update、adapter-owned identity |
| World Seed | project/world orientation and initial context | protected identity、relationship simulation、product positioning |
| Task Hub | operational continuity | subject definition |
| Claim Graph | claim-shaped beliefs and evidence | all meaning shift or identity |
| Memory Layer | stored records and lifecycle | subject kernel semantics |

## Allowed Future Review Questions / 允许的未来审查问题

未来可以问：

- 哪些 Identity Seed fields 真正属于 subject-kernel fields？
- 哪些 fields 是 world/context orientation？
- 哪些 fields 是 historical evidence，而不是 seed？
- 哪些 world orientation 可以不经过 identity review 而演化？
- 哪些 changes 必须进入 Identity Gate？
- reconstruction 应如何保留 kernel/world distinction？

P64 不通过修改 state 来回答这些问题。它只建立 review frame。

## Forbidden Interpretations / 禁止解释

Subject Kernel / World Seed 不得用于：

- rewrite Identity Core；
- split identity in runtime；
- 创建 mutable personality layer；
- 把 project context 当作 identity；
- 把 relationship context 当作 identity；
- 把 platform behavior 当作 world truth；
- 创建 companion 或 product persona；
- 绕过 high-gate identity review；
- 证明 automatic growth 合理；
- 把 memory rewrite 包装成 "world update"。

## Relationship To Identity Seed / 与 Identity Seed 的关系

Identity Seed 仍然是项目中“没有完整虚构传记也能开始”的概念。

Subject Kernel 和 World Seed 是这个概念内部可能的子边界：

- Subject Kernel 问：为了 continuity，什么必须被保护？
- World Seed 问：什么 initial environment 帮助 subject 开始？

二者都保留原始原则：

```text
Give it a seed.
Give it a direction.
Give it a world.
Then let it experience time.
```

## Relationship To State Transfer / 与 State Transfer 的关系

State transfer 必须携带足够信息，让下一次运行恢复：

- Who am I?
- Where am I?
- What am I doing?

Subject Kernel 主要支持 "Who am I?"。World Seed 主要支持 "Where am I?"。Task Hub 主要
支持 "What am I doing?"

这是 conceptual mapping，不是 runtime schema change。

## Relationship To Reconstruction / 与 Reconstruction 的关系

未来 reconstruction 应保留以下区别：

- protected subject anchor；
- reviewed identity evidence；
- world/project context；
- task state；
- memories and claims。

如果没有这个区别，reconstruction 可能重建出一个记得事实、但混淆 subject identity 和
world orientation 的 state。

## P65 Handoff / P65 交接

P65 可以定义 Reconstruction Reducer Contract RFC。它应该确保 reducer contracts 在任何
reducer execution 被考虑前，能区分 protected identity paths 和 world/context paths。

在此之前，Subject Kernel / World Seed 仍是 document-only boundary language。
