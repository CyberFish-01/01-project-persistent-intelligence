# 外部记忆导入

英文镜像：[MEMORY_IMPORT.md](./MEMORY_IMPORT.md)

01 Core 可以吸收 AstrBot 上 01 的旧记忆，但不能依赖 AstrBot 或 Angel Memory 的内部格式。

原则是：

```text
外部系统记忆
  ↓
提取为通用文本
  ↓
导入 01 Core imported_memory
  ↓
Dream review
  ↓
必要时提出 semantic memory candidate
  ↓
默认不更新 Identity Core
```

## 1. 为什么用通用文本

AstrBot、Angel Memory、其他 bot 框架或记忆插件都只是外部载体。

01 的连续性不应该绑定在任何一个载体上。

所以导入时只保留：

- 记忆文本本身；
- 来源系统；
- 来源标签；
- 来源路径；
- 导入时间；
- 置信度；
- provenance；
- promotion policy。

不保留外部系统的执行逻辑。

## 2. 文本格式

推荐把旧记忆整理成普通 `.txt`。

可以用空行分段：

```text
01 认为连续性不是记忆检索，而是 State Transfer。

01 和用户正在研究 Dream Engine、Memory Lifecycle、Identity Seed。

AstrBot 只是未来的外部接入层，不应该拥有 01 Core 的核心状态。
```

也可以用项目符号：

```text
- 01 认为连续性不是记忆检索，而是 State Transfer。
- 01 和用户正在研究 Dream Engine、Memory Lifecycle、Identity Seed。
- AstrBot 只是未来的外部接入层，不应该拥有 01 Core 的核心状态。
```

## 3. 导入命令

```bash
python3 -m one_core.cli import-text astrbot_01_memory.txt \
  --source-system astrbot_text \
  --source-label astrbot_01_export
```

如果来自 Angel Memory：

```bash
python3 -m one_core.cli import-text angel_memory_export.txt \
  --source-system angel_memory_text \
  --source-label astrbot_angel_memory_export
```

## 4. 导入后存到哪里

导入内容进入：

```text
state.json -> memory_stores.imported_memory
imports.jsonl
```

它们会被标记为：

```yaml
status: "staged"
promotion_policy:
  default_target: "semantic_memory_candidate"
  requires_dream_review: true
  may_update_identity_core: false
```

也就是说，导入记忆默认只是“外部材料”，不是 01 的身份核心。

## 5. 为什么不直接写入 Identity Core

因为旧记忆可能包含：

- 过期偏好；
- 插件误记；
- roleplay 内容；
- 临时情绪；
- AstrBot 平台状态；
- Angel Memory 的格式噪声；
- 用户当时没有打算永久保存的内容。

这些内容可以作为历史材料，但不能自动改变 “Who am I?”。

Identity Core 的更新必须通过 high gate。

## 6. 推荐流程

1. 从 AstrBot / Angel Memory 导出旧记忆；
2. 人工粗略清理为 `.txt`；
3. 删除明显隐私、噪声和插件内部字段；
4. 用 `import-text` 导入；
5. 查看 `context` 和 `status`；
6. 运行 `dream`；
7. 检查 Dream 是否提出合适的 semantic candidates；
8. 后续再实现人工批准和 identity update gate。

## 7. 当前限制

第一版导入器还不会：

- 自动读取 AstrBot 数据库；
- 自动解析 Angel Memory 专有格式；
- 自动去重；
- 自动判断真假；
- 自动升级为 identity memory。

这是故意的。

导入器现在只负责一件事：

> 把外部记忆安全地带进 01 Core，但不让外部系统支配 01。
