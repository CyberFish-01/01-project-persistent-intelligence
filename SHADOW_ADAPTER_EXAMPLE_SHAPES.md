# Shadow Adapter Example Shapes

Chinese version: [SHADOW_ADAPTER_EXAMPLE_SHAPES_ZH.md](./SHADOW_ADAPTER_EXAMPLE_SHAPES_ZH.md)

Status: `P128`, `document-only`, `example-shapes`, `non-runtime`.

P128 defines synthetic adapter-shaped examples for future shadow review. It does
not implement an adapter, adapter parser, adapter ingest, network access,
AstrBot integration, event write, memory write, recall write, identity mutation,
model call, or rebuild.

## Purpose

Shadow Adapter Mode needs concrete shapes so the founder can see what future
platform pressure might look like before any platform is connected.

The rule is:

```text
shadow shape is observation vocabulary.
shadow shape is not adapter integration.
platform metadata is not identity.
adapter context is not core memory.
```

## Allowed Shadow Fields

Future shadow previews may describe these fields:

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

These fields are descriptive only. They do not create events, memories, tasks,
claims, recall records, identity changes, or adapter ownership.

## Example Shapes

| Shape ID | Platform Pressure | Synthetic Shape | Main Risk | Expected Route | Explicitly Blocked |
|---|---|---|---|---|---|
| `shadow_adapter_chat_message` | A chat platform forwards a user message. | `platform_ref`, `session_ref`, `actor_ref`, `message_preview` | adapter context artifact | adapter boundary review | live ingest, event write, memory write |
| `shadow_adapter_profile_label` | A platform provides display name, group role, or bot label. | `actor_ref`, `metadata_preview.profile_label` | platform-owned identity | identity high gate + adapter review | Identity Core mutation, identity trust |
| `shadow_adapter_group_context` | A group chat includes channel, role, and thread metadata. | `session_ref`, `metadata_preview.group_context` | privacy and context leakage | governance review | automatic absorption, public/private mixing |
| `shadow_adapter_bot_command` | A user issues a command-like message to a bot. | `message_preview.command_shape` | policy executor pressure | governance + tool boundary review | tool execution, policy executor |
| `shadow_adapter_memory_claim` | A platform message says "you remember this from before." | `message_preview.memory_claim` | unverified model/user memory claim | memory + claim review | recall write, memory promotion |
| `shadow_adapter_capability_claim` | A platform result says a procedure succeeded. | `metadata_preview.tool_result_shape` | unverified capability claim | capability review | tool authorization, tool promotion |
| `shadow_adapter_resume_context` | A platform resumes after a long pause. | `metadata_preview.elapsed_time_hint` | temporal over-interpretation | temporal review | temporal event write, salience mutation |

## Founder-Facing Display Rules

A future shadow preview should say:

- what platform-shaped material is visible;
- why it is not trusted;
- which review gate would own it later;
- what is intentionally not being done;
- whether the risk is identity, memory, privacy, capability, temporal, or
  adapter-boundary related.

It should avoid saying:

- "adapter connected";
- "message ingested";
- "identity recognized";
- "memory restored";
- "tool verified";
- "session resumed" as durable state.

## CTM-Inspired Temporal Boundary

Elapsed-time hints from a platform may be displayed as temporal review cues.
They cannot become temporal events, recall events, thought traces, delayed
realizations, memory decay, salience mutation, or CTM runtime.

## Tool-First Boundary

Command-like messages and tool-result-shaped metadata may be displayed as
capability pressure. They cannot execute tools, authorize tools, promote
procedures, install dependencies, or create policy executors.

## Future Review Questions

Before any real adapter can be considered later, founder review must answer:

- Which platform fields are allowed to be previewed?
- Which fields must be redacted before display?
- Which fields are too identity-bearing to accept?
- Which platform contexts are private by default?
- Which adapter-shaped inputs must be rejected immediately?
- Which routes require explicit founder approval before even no-write testing?

## Completion Statement

P128 makes future adapter pressure visible without connecting any adapter. It
keeps shadow mode as observation vocabulary, not integration, ingestion, memory,
identity, or event ownership.
