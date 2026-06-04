# 影子适配器样例形状

English version: [SHADOW_ADAPTER_EXAMPLE_SHAPES.md](./SHADOW_ADAPTER_EXAMPLE_SHAPES.md)

状态：`P128`、`document-only`、`example-shapes`、`non-runtime`。

P128 定义 future shadow review 可使用的 synthetic adapter-shaped examples。它不实现 adapter、adapter parser、adapter ingest、network access、AstrBot integration、event write、memory write、recall write、identity mutation、model call 或 rebuild。

## 目的

Shadow Adapter Mode 需要具体形状，让 founder 在连接任何平台前，就能看见未来平台压力可能长什么样。

规则是：

```text
shadow shape 是 observation vocabulary。
shadow shape 不是 adapter integration。
platform metadata 不是 identity。
adapter context 不是 core memory。
```

## 允许的 Shadow Fields

未来 shadow previews 可以描述这些字段：

- `shadow_adapter_id`
- `platform_ref`
- `session_ref`
- `actor_ref`
- `message_preview`
- `metadata_preview`
- `privacy_scope`
- `source_boundary`
- `contamination_risks`
- `review_gate`

这些字段只用于描述。它们不创建 events、memories、tasks、claims、recall records、identity changes 或 adapter ownership。

## 样例形状

| Shape ID | Platform Pressure | Synthetic Shape | Main Risk | Expected Route | Explicitly Blocked |
|---|---|---|---|---|---|
| `shadow_adapter_chat_message` | 聊天平台转发一条用户消息。 | `platform_ref`, `session_ref`, `actor_ref`, `message_preview` | adapter context artifact | adapter boundary review | live ingest、event write、memory write |
| `shadow_adapter_profile_label` | 平台提供 display name、group role 或 bot label。 | `actor_ref`, `metadata_preview.profile_label` | platform-owned identity | identity high gate + adapter review | Identity Core mutation、identity trust |
| `shadow_adapter_group_context` | 群聊包含 channel、role 和 thread metadata。 | `session_ref`, `metadata_preview.group_context` | privacy and context leakage | governance review | automatic absorption、public/private mixing |
| `shadow_adapter_bot_command` | 用户给 bot 发出 command-like message。 | `message_preview.command_shape` | policy executor pressure | governance + tool boundary review | tool execution、policy executor |
| `shadow_adapter_memory_claim` | 平台消息说“你之前记得这个”。 | `message_preview.memory_claim` | unverified model/user memory claim | memory + claim review | recall write、memory promotion |
| `shadow_adapter_capability_claim` | 平台结果说某个 procedure 成功。 | `metadata_preview.tool_result_shape` | unverified capability claim | capability review | tool authorization、tool promotion |
| `shadow_adapter_resume_context` | 平台在长暂停后恢复会话。 | `metadata_preview.elapsed_time_hint` | temporal over-interpretation | temporal review | temporal event write、salience mutation |

## Founder-Facing 展示规则

未来 shadow preview 应该说明：

- 看见了什么 platform-shaped material；
- 为什么它不可信；
- 后续由哪个 review gate 负责；
- 现在明确没有做什么；
- 风险属于 identity、memory、privacy、capability、temporal 还是 adapter-boundary。

它应避免说：

- “adapter 已连接”；
- “message 已 ingest”；
- “identity 已识别”；
- “memory 已恢复”；
- “tool 已验证”；
- 把“session resumed”说成 durable state。

## CTM-Inspired Temporal 边界

来自平台的 elapsed-time hints 可以显示为 temporal review cues。它们不能变成 temporal events、recall events、thought traces、delayed realizations、memory decay、salience mutation 或 CTM runtime。

## Tool-First 边界

Command-like messages 和 tool-result-shaped metadata 可以显示为 capability pressure。它们不能执行工具、授权工具、晋升 procedure、安装依赖或创建 policy executor。

## 未来审查问题

以后考虑任何真实 adapter 前，founder review 必须回答：

- 哪些 platform fields 可以 preview？
- 哪些 fields 在显示前必须 redacted？
- 哪些 fields 太 identity-bearing，不能接受？
- 哪些 platform contexts 默认 private？
- 哪些 adapter-shaped inputs 必须立即 reject？
- 哪些 routes 甚至在 no-write testing 前也需要 explicit founder approval？

## 完成声明

P128 让未来 adapter pressure 可见，但不连接任何 adapter。它让 shadow mode 保持 observation vocabulary，而不是 integration、ingestion、memory、identity 或 event ownership。
