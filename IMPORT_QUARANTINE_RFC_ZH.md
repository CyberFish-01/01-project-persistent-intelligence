# Import Quarantine RFC / 导入隔离 RFC

English version: [IMPORT_QUARANTINE_RFC.md](./IMPORT_QUARANTINE_RFC.md)

状态：`P122`、`RFC-only`、`document-only`、`non-runtime`。

P122 定义未来任何来自旧 01、历史日志、memory dumps、模型输出、外部文件或 adapter exports 的 import，在人工审查前必须如何保持 sandbox。它不实现 import runtime、file loading、quarantine storage、memory writes、event writes、identity mutation、adapter integration、model calls 或 rebuild。

## 问题

项目已有历史 memory import 参考。在本地重构 01 前，危险不只是“能导入什么”。危险是“导入内容会被误当成什么”。

导入内容可能因为旧、情绪显著、或格式像 memory，而显得权威。但这不意味着它是 trusted state。

## Quarantine 命题

```text
import is not adoption.
old memory is not current identity.
log evidence is not subject authority.
model output is not life history.
external files are not trusted state.
```

未来每个 import 都必须先成为 import quarantine object、sandbox preview 或 review candidate。任何导入内容都不能自动进入正式 identity、memory、event、recall、growth 或 tool trust。

## 导入来源类别

| Source Class | Examples | Initial Trust | Required First Route |
|---|---|---|---|
| `old_01_export` | 旧本地 01 state、notes、summaries | unverified | `import_sandbox` |
| `chat_log_export` | chat transcripts、pasted logs、platform history | unverified | `privacy_review_quarantine` |
| `memory_dump` | Angel Memory、AstrBot memory、JSONL memory exports | unverified | `memory_claim_quarantine` |
| `model_output_export` | model summaries、自传式 claims、“I remember” text | untrusted | `model_claim_quarantine` |
| `adapter_export` | platform session metadata、channel context、bot state | untrusted platform metadata | `adapter_artifact_quarantine` |
| `tool_result_export` | tool verification logs、procedure results、generated scripts | unverified evidence | `capability_evidence_quarantine` |
| `external_file` | approved whitelist 外部的 txt/json/csv/sqlite/db/pdf/md | unverified | `external_file_quarantine` |

## Quarantine Object Preview

未来 quarantine object 可以包含：

- `quarantine_id`；
- `source_class`；
- `source_label`；
- `source_path_ref` 或 redacted source reference；
- `privacy_scope`；
- `content_hash`；
- `size_hint`；
- `imported_at`；
- `review_reason`；
- `risk_flags`；
- `candidate_routes`；
- `allowed_preview_only: true`；
- `promoted: false`；
- `persisted_to_memory: false`；
- `identity_update_allowed: false`。

P122 不创建该 object 或 storage。

## Candidate Routes

未来 imports 可以 preview 成：

- `memory_claim_candidate`；
- `identity_claim_candidate`；
- `claim_graph_candidate`；
- `task_context_candidate`；
- `growth_candidate_review`；
- `adapter_context_artifact`；
- `prompt_contamination_candidate`；
- `unverified_capability_claim`；
- `cautionary_procedural_memory_candidate`。

Candidate routing 不是 promotion。Quarantine 不是 memory。Review 不是 adoption。

## 必要审查门

未来任何 adoption 被考虑前，imported content 都需要对应 gate：

| Gate | Handles | Still Forbidden |
|---|---|---|
| `privacy_review` | personal logs、platform transcripts、sensitive files | direct memory write |
| `identity_high_gate` | identity claims、self-history claims、subject boundary claims | Identity Core mutation |
| `memory_review` | possible memory candidates | automatic memory promotion |
| `claim_review` | factual 或 interpretive claims | claim mutation without evidence |
| `adapter_boundary_review` | platform metadata 和 adapter context | platform-owned identity |
| `capability_review` | tool/procedure evidence | tool authorization |
| `contamination_review` | prompt 或 model contamination | instruction authority |

## CTM-Inspired Temporal Dynamics 边界

Imported logs 经常包含 timestamps、gaps 和 resume context。这些可以成为 temporal review questions，但不能成为 temporal state transition。

P122 阻止：

- 从 imported timestamps 写 temporal event；
- elapsed-time salience mutation；
- 从旧日志直接 promotion delayed realization；
- 从 imported reasoning text 存 thought trace；
- CTM runtime 或 thought loop execution。

允许的未来 preview：

- 把 timestamp gaps 标记为 `temporal_review_candidate`；
- 通过 source ID 引用 Temporal Awareness 或 CTM RFC；
- 询问未来 manual review 是否应考虑 elapsed time。

## Tool-First In-Situ Self-Evolution 边界

Imported tool logs 或 procedure notes 可以是 evidence，不是 trusted tools。

P122 阻止：

- 从 imported scripts 执行 tool；
- 从 success logs 自动 tool promotion；
- dependency installation；
- filesystem 或 network access；
- capability evidence 变成 subject growth。

允许的未来 preview：

- `tool_candidate`；
- `procedure_candidate`；
- `verification_evidence_candidate`；
- `cautionary_procedural_memory_candidate`；
- `capability_growth_candidate_review`。

## 与 P121 的关系

P121 冻结 core boundary。P122 把这种冻结应用到 imports。

如果 P121 说 external content is not core state，那么 P122 说 imported content 是最危险的 external-content 路径之一，必须先隔离。

## Future No-Write Checks

未来 no-write validator 可以检查：

- 每个 import 都有 `source_class`；
- 每个 import 先路由到 quarantine 或 sandbox；
- 没有 imported content 出现 `promoted: true`；
- 没有 imported content 写 memory、identity、recall 或 events；
- 没有在 approved import sandbox 外读取 external file path；
- model memory claims 与 memory evidence 分离；
- adapter artifacts 与 identity 分离。

P122 不实现这些 checks。

## P123 候选方向

推荐 P123：**Shadow Adapter Mode RFC**。

它应定义未来 adapter 如何作为 shadow input 被观察，同时不拥有 identity、不写 memory、不创建 live integration。
