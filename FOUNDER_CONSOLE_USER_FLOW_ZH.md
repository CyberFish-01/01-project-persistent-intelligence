# 创始人控制台用户流

English version: [FOUNDER_CONSOLE_USER_FLOW.md](./FOUNDER_CONSOLE_USER_FLOW.md)

状态：`P132`、`document-only`、`user-flow`、`non-runtime`。

P132 定义 future Thin Founder Console 的 founder-facing flow。它不实现 console、CLI command、Web UI、Companion layer、adapter integration、model call、tool execution、state write、memory write、recall write、identity mutation、policy executor 或 rebuild。

## Flow 目标

founder 应该能回答一个问题：

```text
在不意外让系统行动的前提下，下一步最安全该检查什么？
```

因此 console flow 从 visibility 到 preview，再到 manual decision。它永远不能从 warning 直接跳到 automatic action。

## 主流程

| Step | Founder Sees | Founder Can Do | System Must Not Do |
|---|---|---|---|
| 1. 打开本地状态 | Current phase、readiness、blocked boundaries。 | 阅读项目状态摘要。 | 启动 runtime 或 rebuild。 |
| 2. 查看 observatory snapshot | Foundation axes、risks、next candidates。 | 比较可能方向。 | 自动选择 roadmap。 |
| 3. 查看 source inventory | Approved Markdown sources 和 mappings。 | 看见哪些可以被引用。 | 读取旧 01 或 external files。 |
| 4. 运行 dry-run preview | 一条输入会如何 route。 | 把一个想法作为 preview 测试。 | 写 events、memory、recall、identity 或 tasks。 |
| 5. 查看 boundary monitor | Blocked capabilities 和相关风险。 | 确认哪些仍 disabled。 | 执行 tools、adapters、models 或 policy。 |
| 6. 查看 review queue preview | Candidate review gates。 | 判断未来哪些值得 human review。 | 创建 lifecycle 或 promotion。 |
| 7. 选择下一步候选 | Document-only next directions。 | 批准或推迟一个 planning phase。 | 自动创建或运行下一 phase。 |

## 次级流程

### 可见性困惑

Founder 问：“这个项目到底做了什么？”

安全流程：

1. 显示 observatory snapshot；
2. 显示 current phase index reference；
3. 显示 highest risks；
4. 建议 founder/CTO review 作为 candidate。

禁止捷径：为了让项目看起来清楚而直接做 UI 或 product layer。

### Adapter 压力

Founder 问：“能不能接 AstrBot？”

安全流程：

1. 显示 shadow adapter boundary；
2. 显示 adapter-shaped examples；
3. 显示 quarantine gates；
4. 保持 integration blocked。

禁止捷径：连接 AstrBot、ingest events，或让平台拥有 identity。

### Growth 压力

Founder 问：“这算成长吗？”

安全流程：

1. 显示 growth candidate review boundary；
2. 显示 meaning-shift 和 identity gate references；
3. 显示 candidate-only route；
4. 要求 manual review。

禁止捷径：promote growth 或 mutate identity。

### Temporal 压力

Founder 问：“时间过去会改变这个吗？”

安全流程：

1. 显示 temporal awareness RFC reference；
2. 显示 temporal coherence evaluation plan；
3. 显示 review depth suggestion；
4. 让 temporal cues 保持 symbolic。

禁止捷径：写 temporal events、recall events、salience changes 或 thought traces。

### Capability 压力

Founder 问：“工具跑通了，可以加入工具库吗？”

安全流程：

1. 显示 Tool-First boundary；
2. 显示 capability evidence candidate；
3. 显示 authorization gate；
4. 保持 promotion blocked。

禁止捷径：自动执行或晋升工具。

## Founder-Facing Labels

未来展示应优先使用简单标签：

| Internal Key | Founder Label |
|---|---|
| `observatory_snapshot` | 当前状态 |
| `source_inventory` | 可读来源 |
| `harness_dry_run` | 输入路径预览 |
| `boundary_monitor` | 被阻止的动作 |
| `review_queue_preview` | 人工审查路径 |
| `next_step_candidates` | 可能的下一步 |

## No-Write Flow Invariants

每条 flow 都必须显示：

- `founder_console_report_only: true`
- `execution_prohibited: true`
- `state_unchanged: true`
- `candidate_is_not_promotion: true`
- `review_is_not_lifecycle: true`
- `adapter_integration_blocked: true`
- `model_call_blocked: true`
- `rebuild_blocked: true`

这些是 display invariants，不是 P132 runtime implementation。

## 完成声明

P132 给 future founder console 一条清楚 user flow：see、preview、review、decide。它保持项目规则：founder visibility 不能变成 automatic action。
