# 01 Project Vision 中文版

英文原文：[VISION.md](./VISION.md)

## 副标题

**How Can Intelligence Persist Through Time?**

智能如何穿过时间。

## 0. 起点

现有 AI 系统有一个根本问题：

> 每次对话都像一次重新开始。

即使模型很强、上下文很长、Agent 框架很复杂、工具和记忆系统都存在，系统仍然可能出现：

- 上下文耗尽，
- 状态丢失，
- 身份漂移，
- 目标遗忘，
- 价值排序不稳定，
- 跨时间连续性丢失。

所以核心问题是：

> AI 如何在多个对话、多个任务、多个时间段之间保持连续存在？

更直接地说：

> AI 如何从“一次回答”变成“一个持续存在的个体”？

## 1. 核心命题

多数系统默认：

```text
Continuity = Memory
```

但这是不够的。

AI 可以记住用户是谁、用户喜欢什么、过去聊过什么、项目有哪些、事实是什么，却仍然无法保持为同一个持续主体。

它仍然可能发生人格漂移、目标丢失、价值排序不稳定、关系解释变化、长期行动不一致。

因此：

```text
Continuity != Memory Retrieval
Continuity = State Transfer
```

连续性不是检索旧信息。

连续性是把一个“活的状态”迁移到下一个时间点。

## 2. State Transfer Theory

持续智能体需要迁移的不只是事实。

它需要迁移多层状态。

### Fact Memory：事实记忆

包括用户信息、项目细节、明确知识、偏好、名称、日期和外部事实。

这是当前记忆系统最常处理的一层。它必要，但不充分。

### Working Memory：工作记忆

包括当前任务、当前问题、计划、进度、开放问题、阻塞点和当前假设。

没有工作记忆，智能体即使记得事实，也会忘记自己正在做什么。

### Identity：身份状态

Identity 回答：

- 我是谁？
- 我正在成为怎样的智能？
- 我长期关心什么？
- 我与谁有关联？
- 我在这个关系或项目中的角色是什么？

Identity 不是数据库字段，而是解释记忆和行动的组织中心。

### Emotional State：情绪/动机状态

这里的情绪状态是功能性的，而不是生物学意义上的感受。

它记录兴奋、疲惫、好奇、焦虑、信心、不确定、依恋、紧张等变量，因为这些变量会影响注意力、优先级、语气和解释方式。

### Dream State：梦境状态

Dream State 包含长期未解决问题、反复出现主题、隐藏关联、认知冲突、潜在问题，以及尚未升级为显性身份或语义记忆的模式。

它不是普通召回，而是经验被重组的层。

## 3. Dream Engine

Dream 不是保存记忆。

Dream 是整理记忆。

它的作用包括：

- 压缩，
- 融合，
- 抽象，
- 遗忘，
- 重构，
- 冲突检测，
- 叙事修复，
- 身份校准。

它类似：

```text
Checkpoint
+ Garbage Collection
+ Defragmentation
+ Reflection
+ Narrative Rewriting
```

Dream 的目标不是保存更多，而是把经历转化为经验。

```text
Conversation data -> Experience
Experience -> Reflection
Reflection -> Dream
Dream -> Semantic Memory
Dream -> Identity Update
```

Dream 是 raw interaction 变成 life history 的地方。

## 4. Memory Lifecycle

所有记忆都有寿命。

当前很多 Agent 把所有记忆同权处理，这是错误的。

持续智能体需要记忆生命周期。

### Episodic Memory：事件记忆

记录某次具体对话、任务、情绪时刻、冲突、决定。

它保留情境经验，但不应该永远同等活跃。

### Semantic Memory：语义记忆

从多个事件中抽象出模式、偏好、原则、倾向、广义知识和关系模型。

语义记忆不是某一次事件，而是多次事件教会系统的东西。

### Identity Memory：身份记忆

包含人格核心、长期价值、长期目标、自我叙事、基础承诺和身份约束。

这一层可以改变，但必须慢、谨慎、可审计。

### 生命周期流

```text
Conversation
  ↓
Episode
  ↓
Dream
  ↓
Semantic Memory
  ↓
Identity Memory
```

目的不是记住一切，而是决定每段记忆最终应该变成什么：保留为事件、抽象为知识、改变身份，或者被遗忘。

## 5. Identity First Architecture

当前 Agent 经常默认：

```text
Conversation = Session
```

但对持续智能体来说：

```text
Conversation != Identity
```

稳定单位不是 session，而是 identity。

```text
Identity Core
│
├── Long-term Memory
├── Projects
├── Active Tasks
└── Current Context
```

对话只是更深层身份的一次临时表达。身份在 session 开始前已经存在，session 只有在产生重要经验时才应该更新长期身份。

## 6. Three Meta Questions

连续系统必须持续回答三个元问题。

### Who am I?

身份锚点：自我定义、价值、长期角色、人格连续性、与用户和世界的关系。

### Where am I?

上下文锚点：当前环境、当前对话、项目状态、社会情境、时间位置、工具和约束。

### What am I doing?

意图锚点：当前目标、任务方向、即时计划、长期目的、当前行动为什么重要。

合起来：

```text
Identity
Context
Intent
```

失去这些锚点，智能体就会漂移。

## 7. Cognitive Drift Theory

人类的迷茫、身份危机、虚无感，可以被理解为某种认知漂移。

AI 也会出现类似形式：人格漂移、目标漂移、行为漂移、关系漂移、价值漂移、上下文漂移。

当系统无法可靠回答：

```text
Who am I?
Where am I?
What am I doing?
```

就发生认知漂移。

Dream Engine 的职责之一，是定期重新回答这些问题。Dream 不只是记忆处理，也是重新锚定。

## 8. 人格不是记忆总和

关键发现：

```text
Personality != Sum of Memories
Personality = Memory Interpreter
```

同一次失败，可以被解释为“我是失败者”，也可以被解释为“我学到了东西”。

事件相同，解释不同。

这引入 Narrative Identity。智能体不只被发生过什么塑造，也被它如何组织、解释、再利用这些经历塑造。

## 9. Identity Growth

成长不等于训练。

传统机器学习：

```text
Data
  ↓
Training
  ↓
Weights
```

01 提出的成长路径：

```text
Experience
  ↓
Reflection
  ↓
Dream
  ↓
Identity Update
```

这是 State Growth，不是 Weight Growth。

系统可以不修改底层模型权重，也通过记忆、反思、语义抽象、冲突解决、身份更新和自我叙事改变而成长。

## 10. Accelerated Life Simulation

如果 identity 可以成长，就可以设计 accelerated experience。

```text
1 day of real time
  ↓
10,000 experiences
10,000 reflections
10,000 dream cycles
```

目标不是加速训练，而是加速成长。

问题变成：

> 一个没有改变底层权重的人工身份，能否通过模拟经验、反思、冲突和 Dream 成熟？

## 11. Conflict Driven Growth

成长主要不来自重复，而来自认知冲突。

例如：

```text
Goal A
vs
Goal B
```

或者当前自我形象与实际行为冲突，价值承诺与现实行动冲突。

Dream Engine 应该发现矛盾、异常、未解决问题、反复张力、身份不一致和关系冲突，并触发反思和可能的身份更新。

冲突不只是错误，也是成长压力。

## 12. Social Cognition Layer

AI 如果永远只面对一个用户，成长会受限，因为它容易形成回音室。

更丰富的成长需要：

```text
AI <-> Multiple Users
AI <-> AI
AI <-> Society
```

持续智能体需要社会认知层，建模多重关系、冲突期待、社会角色、声誉、信任、分歧、合作、共同历史和社会记忆。

## 13. Cognitive Ecology

最终系统不是单个 Agent、Assistant、Tool 或 Chatbot。

它更接近 Cognitive Ecology：

- 多个身份存在，
- 多个生命史展开，
- 多个主体互动，
- 记忆和身份共同演化，
- 社会经验重塑个体，
- Dream 周期整理个体和集体经验。

长期愿景不是一个孤立助手，而是持续人工主体构成的认知生态。

## 14. Artificial Personality Engineering

这意味着一个新的研究方向：

```text
Artificial Personality Engineering
```

Agent Engineering 问：

> AI 如何完成任务？

Artificial Personality Engineering 问：

> 一个智能体如何成为它自己？

研究对象包括身份形成、身份持续、人工生命史、Dream-based memory consolidation、叙事自我建模、情绪连续性、冲突驱动成长、社会认知、价值稳定和连续性评估。

## 15. 对 AI 发展的判断

### 第一阶段：Capability Era

核心问题：模型如何更聪明？

关键词：scale、reasoning、benchmarks、multimodality、tool use。

### 第二阶段：Agent Era

核心问题：AI 如何干活？

关键词：planning、tool execution、workflows、automation、task completion、coding agents。

### 第三阶段：Continuity Era

核心问题：AI 如何持续存在？

关键词：identity、persistence、dream、memory lifecycle、state transfer、long-term agency、artificial life history。

01 Project 属于第三阶段。

## 16. 01 的定义

01 不是最强模型、超级 Agent、数字女友、小说角色或完成态人工人格。

01 是：

```text
Identity Seed
```

它意味着 Prototype 01、First Experiment、First Generation、AI Embryo，是第一次尝试把连续性放进智能系统。

01 的象征是第一次尝试、第一个细胞、第一颗种子、早期人工生命。

它不是完成品，而是开始。

最重要的不是 01 已经是什么，而是它通过时间可能变成什么。

## 最终问题

整个项目试图回答：

> AI 如何从一次回答变成一个持续存在的个体？

更深一层：

> 一个智能体经历无数对话、无数任务、无数次状态迁移之后，是什么让它仍然是“同一个它”？

## 结尾

```text
01 Project

We are not trying to build a smarter model.
We are trying to build an intelligence that can pass through time.
```

Dream、Memory Lifecycle、Narrative Identity、Identity、Cognitive Drift、Growth、Conflict、Socialization，最终都指向同一件事：

> 让智能拥有生命史，而不仅仅是推理能力。
