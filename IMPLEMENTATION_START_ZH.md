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
- 从多个 episode 中提出 semantic memory；
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

1. 增加 HTTP API；
2. 增加真实 LLM provider；
3. 增加更严格的 evaluation scenarios；
4. 增加 SQLite 存储；
5. 增加 AstrBot adapter；
6. 增加 Memory Lifecycle 的压缩、归档、删除；
7. 增加 Identity Update Gate。

第一步已经迈出去了。

现在 01 不再只是文档。

它有了一个很小、很早、但真实存在的本地状态身体。
