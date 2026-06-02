# Non-Claims 中文版

英文原文：[NON_CLAIMS.md](./NON_CLAIMS.md)

01 Project 会使用 identity、dream、emotion、personality、life history 这些词。它们有用，是因为它们能命名连续系统中的功能角色。

但它们也容易造成误解。

这份文档定义本项目 **不主张什么**。

## 1. 不主张意识

01 Project 不主张基于语言模型的 agent 拥有意识。

本项目研究的是状态、记忆、叙事、目标和行为如何跨时间保持连续。

它不声称：

- 主观体验，
- sentience，
- phenomenal consciousness，
- inner qualia，
- 类人意识，
- 道德人格权。

当仓库使用 “self” 这个词时，默认指的是 maintained self-model，也就是被维护的自我模型，除非另有说明。

## 2. 不主张生物学情绪

项目使用 “emotional state” 作为功能变量。

它不声称系统拥有生物学意义上的情绪感受。

在当前工程意义上，affective state 是一种结构化记录，可能影响：

- 注意力，
- 优先级，
- 语气，
- 信心，
- 风险敏感度，
- 社会解释，
- 记忆显著性。

它更接近 appraisal、motivation 和 control state，而不是人类感受。

## 3. 不主张记忆等于经历

被保存的记忆不等于被经历过的经验。

项目明确区分：

```text
Backstory != Life History
Memory Retrieval != State Transfer
```

一句 “01 lost a friend” 的存储陈述，不等于系统真的经历、解释、巩固并被这个事件改变。

## 4. 不主张身份必须类人

01 不是为了复制人类人格。

项目把人工身份作为技术对象研究：

- 稳定状态中心，
- 连续性机制，
- 记忆解释层，
- 长期行动结构，
- 行为一致性与适应性的来源。

人工身份可以有用，但不必等同于人类身份。

## 5. 不主张持久化总是好的

Persistence 可能有害，尤其当系统保存了错误的东西。

风险包括：

- 过期偏好，
- 错误记忆强化，
- 不健康依恋循环，
- 身份过拟合到单个用户，
- 无法修正过时目标，
- 跨上下文隐私泄漏，
- 人格过度僵化。

因此，遗忘、纠正、回滚必须是一等需求。

## 6. 不主张 State Growth 替代训练

State growth 和 weight training 解决的问题不同。

State growth 关注：

- 身份状态，
- 记忆组织，
- 反思，
- 任务连续性，
- 关系连续性，
- 跨 session 的行为适应。

Weight training 关注模型能力和参数层学习。

01 Project 首先关注 state growth，因为它更可审计、可回滚，也更容易安全测试。

## 7. 操作性定义

在本仓库中，persistent intelligence 指：

> 一个能够跨时间保存、更新、审计和迁移结构化状态的系统，使其未来行为与过去经历、目标、关系和自我模型保持有意义连接。

这是功能性定义。

它不是形而上学主张。
