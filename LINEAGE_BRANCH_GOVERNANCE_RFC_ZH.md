# Lineage and Branch Governance RFC / 谱系与分支治理 RFC

English version: [LINEAGE_BRANCH_GOVERNANCE_RFC.md](./LINEAGE_BRANCH_GOVERNANCE_RFC.md)

状态：`P155`、`governance-only`、`planning`、`non-runtime`、`no-tag-created`、`no-branch-created`。

P155 在任何未来本地 01 重构之前，定义 lineage、branch、tag 和 checkpoint 治理。它不创建 git
tag，不创建 git branch，不 push，不启动 rebuild，不读取 old 01，不导入外部材料，不写 state、
event 或 memory，不修改 Identity Core，不执行 tool，不调用模型，也不连接 adapter。

## 1. Why Lineage Governance / 为什么需要谱系治理

Lineage governance 存在的原因是：初始 01 Core 必须永久可回溯。

项目现在已经有足够多的 foundation、harness、lockdown、context-package、response-boundary 和
pre-rebuild verification 工作，未来 local rebuild 和 01 instances 会变得很有吸引力。这是好事，
但如果没有 lineage boundary，也很危险。

必须承认的事实：

- 初始 01 Core 必须永久可恢复；
- 每个 01 instance 都必须有声明来源；
- 更像 01 不等于更接近 Core；
- instance 可以大胆生长，但不能直接改 Core；
- synthetic history、AstrBot context、adapter payloads 和 LLM self-claims 必须可隔离；
- branch 用于 recovery、comparison、abandonment、quarantine、review 和 selected return。

没有这一层，未来 sandbox instance 可能生成很有说服力的风格、记忆声明、自我描述或工具候选，让它们看起来像
Core 原生历史。P155 防止这种混淆。

## 2. Core Principle / 核心原则

```text
Instance may grow; Core must remain sovereign.
实例可以生长，内核不可僭越。
```

这意味着：

- Core 拥有长期连续性的边界；
- instance 可以探索行为、风格、假设、模拟经历和工具候选；
- instance output 是 evidence 或 candidate material，不是 Core history；
- Core 只接受 reviewed、selected、minimal returns；
- branch 名、tag 名、report 或 model output 都不授权 mutation。

## 3. Branch Types / 分支类型

| Branch Type | Purpose | Allowed Use | Forbidden Use |
|---|---|---|---|
| `core trunk` | 受保护的主连续性线。 | 保存已审查的 Core history 和稳定项目状态。 | direct instance merge、quarantine merge、unreviewed model output、adapter-owned context。 |
| `core baseline` | 可恢复的已知良好 Core reference。 | anchor rollback、comparison 和 rebuild planning。 | 把 baseline 当成 mutable experiment space。 |
| `foundation milestone` | 重大 foundation 阶段的命名点。 | 引用 P-level documents 和只读能力。 | 宣称 milestone 等于 product readiness。 |
| `pre-rebuild checkpoint` | rebuild 前安全门。 | 标记 rebuild 可在 founder approval 后被考虑的 evidence。 | 自动开始 rebuild 或 migration。 |
| `instance sandbox branch` | 受控 01 instance exploration line。 | 探索 style、assumptions、simulation、candidates、本地行为。 | 直接写 Core identity、memory、event 或 tool trust。 |
| `research experiment branch` | 受控 research line。 | 探索 CTM vocabulary、Tool-First ideas、synthetic-history accelerators、evaluation plans。 | 把未审查 output merge 到 Core trunk。 |
| `quarantine branch` | suspicious 或 untrusted material 的 containment area。 | 保存 imported memory、LLM self-claims、adapter context、prompt contamination、synthetic autobiography。 | merge 到 Core trunk。 |
| `release / verification branch` | 临时 verification surface。 | 在人工决定前验证 candidate state。 | 未经审查成为 alternate Core trunk。 |

## 4. Naming Rules / 命名规则

以下名称是示例和建议。P155 不创建它们。

Core names：

```text
core/baseline
```

Instance sandbox names：

```text
instance/01-local-rebuild-trial
instance/01-astrbot-shadow
instance/01-synthetic-history-v1
```

Research names：

```text
research/ctm-temporal-dynamics
research/tool-first-evolution
research/synthetic-history-accelerator
```

Quarantine names：

```text
quarantine/imported-astrbot-memory
quarantine/llm-self-claims
```

Milestone names：

```text
milestone-p100-harness-dry-run
milestone-p154-pre-rebuild-ready
core-v1-pre-rebuild-ready
```

命名约束：

- 尽量使用 lowercase；
- 名称说明 purpose，而不是 personality label；
- `instance/` 用于 sandbox subjects；
- `research/` 用于 concept experiments；
- `quarantine/` 用于 untrusted 或 contaminated material；
- 不要把 branch 命名成新的 Core，除非 founder 已明确批准这个角色。

## 5. Tagging Rules / Tag 规则

P155 只建议 tag semantics，不创建 tag。

| Suggested Tag | Meaning | Suggested Commit Selection Rule |
|---|---|---|
| `core-v0-baseline` | 最早的稳定本地 01 Core baseline。 | 如果 founder 需要这个历史锚点，选择后续治理扩展前代表 minimal local Core 的最后一个 commit。 |
| `core-v0-foundation-baseline` | foundation documents 和 prototype references 足够一致，可作为 research baseline。 | 选择 foundation consolidation artifacts 已存在且 tests pass 之后的 commit。不要在没审 phase index 和 verification state 时猜 commit。 |
| `core-v0-observable-baseline` | 只读 observatory 和 harness visibility 已存在。 | 选择 observatory 和 no-write harness dry-run 已实现并 review 之后的 commit。 |
| `core-v1-pre-rebuild-ready` | pre-rebuild evidence 已足够询问是否可以开始 local rebuild。 | 在 verification 和 branch governance 被接受后，选择 P154 push-readiness commit 或后续 founder-approved checkpoint commit。 |
| `milestone-p100-harness-dry-run` | 第一个 no-write harness dry-run 存在。 | 选择引入 minimal CLI harness dry-run 的 commit。 |
| `milestone-p110-scenario-routing` | P102-P110 harness routing 和 review cycle 已收口。 | 选择 routing、specialization、usability review 之后关闭 overnight harness work summary 的 commit。 |
| `milestone-p154-pre-rebuild-ready` | pre-rebuild completion 和 push readiness 已记录。 | 如果 founder 需要 pre-rebuild-ready reference，选择 P154 audit commit。 |

如果具体 commit 不明显，不要猜。选择流程：

1. 检查 `PHASE_INDEX.md`；
2. 检查 `git log --oneline`；
3. 检查相关 completion 或 review document；
4. 跑 tests 和 forbidden search；
5. 在 future tag-advisor report 中记录 candidate commits；
6. 只有在单独批准的操作中才创建 tag。

## 6. Merge / Return Rules / 合并与回流规则

Branch return 必须明确且保守。

禁止 direct merges：

- instance branch -> core trunk；
- research branch -> core trunk；
- quarantine branch -> core trunk；
- adapter branch -> core trunk；
- synthetic-history branch -> core trunk；
- tool-candidate branch -> core trunk。

允许的回流路径：

```text
candidate -> quarantine -> review -> manual selected return
```

允许回流的材料：

- RFC；
- tests；
- reports；
- safe schema；
- reviewed procedural insight；
- reviewed boundary improvement；
- minimal founder decision note；
- minimal review note。

禁止回流的材料：

- identity mutation；
- automatic memory write；
- unverified model memory claims；
- adapter context artifact；
- synthetic autobiographical memory；
- tool trust update without review；
- prompt contamination residue；
- imported memory treated as native history；
- instance style treated as Core identity。

Manual selected return 表示人类审查识别一个小的、有边界、有来源标注的 change，它可以返回 Core，
但不会把该 branch 的 identity、memory 或 trust assumptions 一起导入。

## 7. Instance Sandbox Rule / Instance 沙盒规则

Instance sandbox 是一个受控 exploration line，用于可能的 01 variants。

instance sandbox 内允许：

- style exploration；
- expression experiments；
- self-hypotheses；
- simulated experiences；
- synthetic history experiments；
- tool candidates；
- procedure candidates；
- local behavior experiments；
- evaluation notes。

必须保持的边界：

- instance outputs 只能进入 candidate、quarantine 或 review surfaces；
- instance output 不写 Core；
- instance memory 不是 Core memory；
- instance identity 不是 Core identity；
- instance tool success 不是 Core tool authorization；
- Core 拥有最终审查权。

看起来最像 01 的 instance 仍然只是 instance。它可以提供 evidence，但不拥有 lineage。

## 8. Recovery Rules / 恢复规则

Recovery rules 定义 future operators 在 branch 变得不清楚、被污染或不安全时该怎么做。

### Return To Baseline / 回到 baseline

回到 baseline：

1. 识别 approved baseline tag 或 commit；
2. 验证它指向预期 Core state；
3. 检查 verification 和 checkpoint documents；
4. 任何 future recovery 都必须经过 explicit founder-approved action；
5. 不要随意覆盖 Core trunk history。

### Abandon A Contaminated Branch / 废弃污染分支

当 branch 包含以下内容时，应考虑废弃：

- unverified identity claims；
- untrusted synthetic autobiography；
- adapter context 与 Core identity 混合；
- model output 被当作 native memory；
- tool trust 未经 review 就被 promotion；
- 无法解释 source lineage。

废弃应该记录在 future report 中，而不是静默隐藏。

### Compare Two Instance Branches / 比较两个 instance branches

比较应检查：

- declared source；
- changed files；
- identity claims；
- memory claims；
- tool candidates；
- review artifacts；
- quarantine material；
- tests 和 reports；
- divergence from baseline；
- forbidden return material。

比较不是决定哪个 instance “更真实”。它只显示 lineage、evidence 和 risk。

### Record Branch Lineage / 记录分支谱系

future lineage record 应包含：

- branch name；
- source commit；
- parent branch；
- purpose；
- allowed scope；
- forbidden scope；
- source material；
- review status；
- quarantine status；
- selected return decisions；
- abandonment decision if any。

### Future Lineage Report / 未来谱系报告

future `lineage-report` 可以总结 branch ancestry、checkpoints、risk status 和 selected returns。
除非未来 founder-approved phase 另行定义，否则它必须保持 report-only。

## 9. Relationship To Existing Roadmap / 与现有路线关系

P155 连接已有 artifacts，但不改变它们的 execution status：

- Core Lockdown：lineage governance 把 lockdown 从内容处理扩展到 branch handling。
- Import Quarantine：untrusted imports 可以进入 quarantine branches，而不是 Core trunk。
- Shadow Adapter：adapter-shaped material 可以在 shadow branches 中被观察，不能作为 Core memory 或 identity 被 merge。
- Synthetic History Accelerator：如果未来探索 synthetic history，它属于 instance 或 research branches，只能以 reviewed theory、tests 或 quarantine evidence 回流。
- CTM Temporal Dynamics：CTM-inspired temporal work 属于 research branches 和 symbolic review artifacts，不是 CTM runtime。
- Tool-First Self-Evolution：tool candidates 和 capability evidence 在 review 前属于 research 或 instance branches；verification 不是 authorization。
- Rebuild Migration Protocol：migration 在任何 local rebuild 开始前，需要 explicit baseline、checkpoint 和 founder approval。

## 10. Future CLI Ideas / 未来 CLI 候选

只列候选；P155 不实现：

- `lineage-report`；
- `branch-checkpoint-plan`；
- `instance-diff`；
- `quarantine-return-preview`；
- `baseline-tag-advisor`。

Future CLI boundaries：

- 默认 read-only；
- 除非单独批准，不创建 tag；
- 除非单独批准，不创建 branch；
- 不 push；
- 不启动 rebuild；
- 不自动 merge；
- 不自动 selected return；
- 不调用模型；
- 不连接 adapter；
- 不修改 state、memory、identity、event、recall、growth、tool、temporal 或 CTM runtime。

## P156 Candidate Directions / P156 候选方向

P155 不进入 P156。只有在 founder 未来明确批准时，候选方向才包括：

- Lineage Report Plan；
- Baseline Tag Advisor Plan；
- Instance Sandbox Contract；
- Quarantine Return Preview RFC；
- Local Rebuild Start Decision Record。

## Non-Execution Statement / 非执行声明

P155 不会：

- 创建 git tag；
- 创建 git branch；
- push 到远端；
- 启动 rebuild；
- 读取 old 01；
- 导入 AstrBot memory；
- 连接 adapter；
- 调用模型；
- 写 formal state；
- 写 events；
- 写 memory；
- 写 recall events；
- 修改 Identity Core；
- rewrite memory；
- 执行 growth；
- 执行 tools；
- 启用 temporal runtime；
- 启用 CTM runtime；
- 执行 policy；
- 创建 automatic roadmap。
