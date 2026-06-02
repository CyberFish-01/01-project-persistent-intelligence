# Architecture 中文版

英文原文：[ARCHITECTURE.md](./ARCHITECTURE.md)

这份文档把 01 Project 的愿景转化为第一版工程架构。

目标不是建造有意识的机器。

目标是建造一个系统，让 identity、memory、task state、reflection 和 update history 能够以可审计方式穿过时间。

## 1. 设计原则

### Identity First

稳定单位不是 conversation。

稳定单位是 identity。

```text
Conversation != Identity
Session != Self
```

Session 是临时交互表面。

Identity 是跨 session 存活的长期状态对象。

### State Before Retrieval

Memory retrieval 只是连续性的一部分。

架构必须迁移：

- facts，
- working state，
- goals，
- unresolved conflicts，
- relationships，
- affective and motivational state，
- identity constraints，
- update history。

### Slow Identity, Fast Context

不同状态层应该以不同速度更新。

```text
Current Context: fast update
Working State: fast update
Episodic Memory: medium update
Semantic Memory: slower update
Identity Core: slowest update
```

这样可以防止单次对话过快重写身份。

### Auditable Growth

每次 identity-level update 都应该可解释。

系统应该记录：

- 改了什么，
- 为什么改，
- 哪些证据支持，
- 置信度是多少，
- 是否可以回滚。

## 2. 高层系统

```text
┌─────────────────────────────────────────────────────┐
│                    Identity Core                    │
│  values, self-model, constraints, long-term purpose  │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                   State Manager                     │
│  loads, validates, merges, snapshots, rolls back     │
└───────┬─────────────┬─────────────┬────────────────┘
        │             │             │
┌───────▼──────┐ ┌────▼─────┐ ┌────▼────────────┐
│ Memory Layer │ │ Task Hub │ │ Relationship Map │
└───────┬──────┘ └────┬─────┘ └────┬────────────┘
        │             │             │
┌───────▼─────────────▼─────────────▼────────────────┐
│                  Current Context                    │
│ prompt state, active task, retrieved memories, tools │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                  Interaction Loop                   │
│ observe -> reason -> act -> log episode              │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                    Dream Engine                     │
│ consolidate, abstract, forget, detect conflict       │
└─────────────────────────┬───────────────────────────┘
                          │
┌─────────────────────────▼───────────────────────────┐
│                    Update Log                       │
│ evidence, deltas, confidence, provenance, rollback   │
└─────────────────────────────────────────────────────┘
```

## 3. 核心模块

### Identity Core

Identity Core 包含慢变化状态：

- 名字和象征性角色，
- 核心价值，
- 稳定特质，
- 长期目的，
- 自我叙事，
- 身份约束，
- 禁止的自我更新，
- 连续性锚点。

它只能通过 gated process 更新。

### State Manager

State Manager 负责 state transfer。

职责包括：

- session 开始时加载持久状态，
- 校验 schema version，
- 选择进入当前上下文的状态，
- 合并 interaction loop 产生的更新，
- 请求 Dream Engine 巩固，
- 写入 snapshot，
- 维护 rollback point。

### Memory Layer

Memory Layer 不是单个数据库。

它包含：

- episodic memory，
- semantic memory，
- identity memory，
- relationship memory，
- project memory，
- conflict memory，
- forgotten or archived memory。

每条 memory 都应该包含来源、时间戳、置信度、敏感等级、衰减策略和更新历史。

### Task Hub

Task Hub 保持跨中断的行动连续性。

它追踪：

- active goals，
- current plan，
- blocked tasks，
- completed tasks，
- recurring duties，
- project state，
- next actions。

它回答：

```text
What am I doing?
```

### Relationship Map

Relationship Map 保存社会状态。

它应该区分：

- user-specific memories，
- cross-user generalizations，
- private information，
- shared project history，
- trust level，
- communication preferences，
- relationship conflicts。

多用户 persistence 很容易造成隐私和边界故障，所以这个模块非常关键。

### Current Context Builder

Context Builder 决定哪些状态被激活进入 session。

输入：

- identity core，
- active task，
- recent episodes，
- relevant semantic memories，
- relationship context，
- current user message，
- tool/environment constraints。

输出：

- 一个 bounded context package。

它必须足够小以适配上下文窗口，也足够丰富以保持连续性。

### Interaction Loop

Interaction Loop 处理实时行为：

```text
observe -> interpret -> retrieve -> plan -> act -> record
```

每次有意义的互动结束后，它输出 episode record。

### Dream Engine

Dream Engine 在即时响应循环之外运行。

它把 episodes 转化为：

- summaries，
- semantic memories，
- conflict records，
- identity update proposals，
- forgetting proposals，
- relationship updates，
- future questions。

它应该提出 identity update，而不是绕过 gate 直接应用。

### Evaluation Harness

Evaluation Harness 测试系统是否真正 persistent。

它应模拟：

- 时间间隔，
- 上下文丢失，
- 用户偏好变化，
- 冲突目标，
- 多 session 项目，
- 噪声或误导性记忆，
- 社会冲突。

## 4. Session Lifecycle

### Session Start

```text
load identity
load relationship context
load active tasks
retrieve relevant memories
build current context
answer Identity / Context / Intent anchors
```

### During Session

```text
observe user input
retrieve relevant state
plan response or action
update working memory
log important events
mark possible conflicts
```

### Session End

```text
write episode
update task status
queue dream cycle
snapshot state
record update log
```

### Dream Cycle

```text
select episodes
cluster themes
extract semantic memories
detect conflicts
propose forgetting
propose identity updates
run safety gates
write approved updates
```

## 5. Update Gates

不是所有更新都同级。

### Low Gate

用于最近任务进展、临时上下文、非敏感事实和用户纠正的细节。

### Medium Gate

用于 semantic memories、preferences、relationship patterns 和 recurring project behavior。

需要多次支持性 episode 或用户明确确认。

### High Gate

用于 identity core、long-term values、self-narrative、relationship commitments 和 safety-relevant beliefs。

需要：

- 多个证据来源，
- conflict check，
- reversibility，
- 明确 update reason，
- audit log。

## 6. First MVP

最小可行 01 系统应该避免 weight training。

它可以由以下部分组成：

- 一个 base model，
- 一个 structured state file，
- 一个 episodic memory log，
- 一个 semantic memory file，
- 一个 identity seed file，
- 一个 dream script，
- 一个简单 evaluation suite。

第一研究目标：

> 一个 stateful agent 能否比 memory-retrieval-only baseline 更好地在中断 session 之间恢复 identity、context 和 intent？

如果可以，State Transfer 就已经具有实验意义。
