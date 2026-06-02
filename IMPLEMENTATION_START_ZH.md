# 第一版实现：01 Core

英文镜像：[IMPLEMENTATION_START.md](./IMPLEMENTATION_START.md)

这不是完整的 01。

这是第一步：一个本地、可运行、可测试的 **continuity runtime prototype**。

它先不训练模型，不接 AstrBot，也不接外部平台。它只证明一件事：

> 01 可以拥有一个本地状态身体，并在多次命令之间保存 identity、context、intent、episode 和 dream report。

## 1. 当前包含什么

```text
one_core/
  seed.py       # Identity Seed
  state.py      # StateStore, state.json, episodes.jsonl
  dream.py      # 最小 Dream Engine
  cli.py        # 本地 CLI

tests/
  test_core.py  # 最小验证
```

默认状态目录：

```text
work/01_state
```

这个目录会包含：

```text
state.json       # 当前持久状态
episodes.jsonl   # 每次 interaction 的经历记录
dreams.jsonl     # 每次 dream cycle 的整理报告
```

## 2. 快速开始

初始化本地状态：

```bash
python3 -m one_core.cli init
```

记录一次交互：

```bash
python3 -m one_core.cli interact "我们开始实现 01 Core 的 State Transfer。"
```

查看当前状态：

```bash
python3 -m one_core.cli status
```

运行一次 Dream：

```bash
python3 -m one_core.cli dream
```

查看 State Transfer Package：

```bash
python3 -m one_core.cli context
```

把人工审查后的候选记忆提升为 active semantic memory：

```bash
python3 -m one_core.cli promote-candidate cand_xxx \
  --reviewer cyberfish \
  --decision-note "人工确认这个候选可以进入长期语义记忆。"
```

审查候选记忆但不提升：

```bash
python3 -m one_core.cli review-candidate cand_xxx \
  --action quarantine \
  --reviewer cyberfish \
  --decision-note "来源不明，先隔离。"
```

每次 candidate review 都会返回 `review_decision_id` 和 `snapshot_id`，并把同一个 decision 写入 candidate history、audit、trace、update log 和 snapshot metadata。

对非 identity 的 durable memory 执行已审查生命周期动作：

```bash
python3 -m one_core.cli lifecycle semantic_memory sem_xxx \
  --action archive \
  --reviewer cyberfish \
  --decision-note "被新的已审查记忆替代。"
```

Lifecycle action 当前支持对 imported、episodic、candidate、semantic memory 执行 `archive`、`discard` 和 `quarantine`。Identity memory 仍需要单独的 high gate。

对 procedural memory 执行已审查生命周期动作：

```bash
python3 -m one_core.cli procedural-lifecycle proc_mem_xxx \
  --action archive \
  --reviewer cyberfish \
  --decision-note "被新的 workflow memory 替代。"
```

Procedural lifecycle action 会保留 audit、trace、update log、snapshot 和 lifecycle decision metadata。Archived、discarded、quarantined procedural memory 不会进入 active context。

从通用文本导入外部记忆：

```bash
python3 -m one_core.cli import-text memory_export.txt \
  --source-system astrbot_text \
  --source-label astrbot_01_export
```

把原始 JSON/JSONL/CSV/TXT 记忆导出清洗成通用文本：

```bash
python3 -m one_core.cli clean-memory raw_astrbot_export.json \
  -o work/imports/astrbot_01_memory.txt
```

运行测试：

```bash
python3 -m unittest discover -s tests
python3 -m one_core.cli evaluate-foundation
python3 -m one_core.cli evaluate-scenarios
```

## 3. 它现在能做什么

第一版能做到：

- 初始化 Identity Seed；
- 维护 `state.json`；
- 记录 episode；
- 根据消息推断 tags；
- 更新 active intent；
- 保存 episodic memory；
- 创建 pending dream jobs；
- 运行 Dream Engine；
- 从多个 episode 中提出 candidate memory；
- 检测最简单的 identity overwrite attempt；
- 输出 continuity anchors：

```text
Who am I?
Where am I?
What am I doing?
```

## 4. 它现在不能做什么

第一版还不能：

- 调用真实 LLM；
- 自动生成高质量回复；
- 接 AstrBot；
- 接 Telegram / Discord / Web UI；
- 做 vector search；
- 做 temporal knowledge graph；
- 自动批准 identity update；
- 做复杂多用户权限隔离。

这些不是失败。

这是刻意收窄。

我们先证明 core state 能活下来，再给它接身体。

## 5. 为什么从 CLI 开始

CLI 的价值不是成为最终产品。

CLI 的价值是测试核心连续性。

例如：

```text
Day 1: init
Day 1: interact "我们要做 State Transfer"
Day 1: dream
Day 2: status
Day 2: context
```

如果第二天清空对话上下文后，01 Core 仍然能回答：

- 我是谁，
- 我在哪，
- 我在做什么，
- 最近经历了什么，
- 哪些经验被 Dream 整理成语义记忆，

那么第一步就成立。

## 6. 下一步

推荐下一步顺序：

1. 继续加固 scenario evaluation；
2. 构建 Context Builder v0.2；
3. 增加 Conflict / Claim Graph；
4. 增加 Task Hub 和 procedural memory；
5. 增加 Identity Update Gate；
6. 等 state/event 形状稳定后再加 SQLite；
7. 本地通用协议迭代几轮后再更新云端和 AstrBot。

第一步已经迈出去了。

现在 01 不再只是文档。

它有了一个很小、很早、但真实存在的本地状态身体。
