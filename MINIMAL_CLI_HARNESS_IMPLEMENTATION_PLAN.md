# Minimal CLI Harness Implementation Plan

Chinese version: [MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md](./MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md)

Status: `P99`, `planning`, `RFC-only`, `document-only`, `non-runtime`.

P99 defines an implementation plan for a possible future minimal CLI harness. It
does not implement the harness, add a CLI command, add tests, write schemas,
call a model, call external APIs, mutate state, integrate adapters, or enter the
product layer.

## Plan Rule

```text
implementation plan is not implementation.
dry-run means no writes.
preview is not persistence.
candidate is not promotion.
review queue preview is not lifecycle.
```

## 1. Problem Statement

P0-P98 produced a broad foundation: identity boundaries, state transfer, event
sourcing, reconstruction readiness, stateful memory, growth review, temporal
review vocabulary, capability boundaries, and the read-only Foundation
Observatory.

P96 implemented `foundation-observatory-report` as a static read-only report.
P97 reviewed whether that report was founder-readable. P98 improved the report
so a founder can see status, risk, boundary, and next-step candidates more
clearly.

The next pressure on the system is interaction. The foundation needs a minimal
way to test how a real user message would touch intake, context, candidates,
review queues, boundaries, and observatory summaries. It should not jump
directly into Companion, Web UI, AstrBot, adapter integration, cloud runtime, or
product behavior.

The minimal CLI harness is therefore a local test bench. It is not a product,
chatbot, adapter, memory writer, identity owner, growth engine, or automatic
executor.

## 2. Minimal Scope

The smallest future command candidate is:

```bash
python3 -m one_core.cli harness-dry-run
```

P99 does not add this command. It only plans the future command boundary.

Candidate future parameters:

| Parameter | Purpose | Boundary |
|---|---|---|
| `--input TEXT` | User message or fixture text to preview. | Text input only; not adapter ingest. |
| `--session-id ID` | Local session reference for preview grouping. | Does not own identity or write session state. |
| `--actor-id ID` | Actor reference for preview attribution. | Does not create actor identity. |
| `--lang en\|zh` | Output language. | Display choice only. |
| `--format markdown\|json` | Output format. | Report format only, not schema persistence. |
| `--output PATH` | Optional report destination. | Writes the report only if explicitly requested; no state write. |
| `--no-write` | Required no-write mode, default `true`. | If future implementation cannot prove no-write, it must fail closed. |

Minimum allowed output is a deterministic Markdown or JSON dry-run report. The
harness must not call a model, external API, adapter, network service, cloud
service, or product surface.

## 3. Dry-run Flow

Future dry-run flow:

```text
user message or fixture input
  -> conversation_intake_preview
  -> context_package_preview
  -> candidate_preview
  -> review_queue_preview
  -> boundary_monitor
  -> observatory_snapshot
  -> non_execution_invariants
```

| Step | Preview Purpose | Explicit Non-Execution Boundary |
|---|---|---|
| `conversation_intake_preview` | Normalize the input into an audit-safe envelope. | No adapter ingest, event write, identity ownership, or session state write. |
| `context_package_preview` | Show what context references would be considered, selected, omitted, or suppressed. | No retrieval execution as continuity, prompt construction, activation trace write, or context mutation. |
| `candidate_preview` | Show possible review objects raised by the input. | No durable candidate creation, approval, promotion, or lifecycle execution. |
| `review_queue_preview` | Show how candidates might be routed for review. | No queue storage, lifecycle transition, policy execution, or owner assignment mutation. |
| `boundary_monitor` | Show forbidden actions as disabled or blocked. | No runtime enforcement, policy executor, or automatic mitigation. |
| `observatory_snapshot` | Attach a compact status summary from the observatory vocabulary. | Observatory displays status only; it does not decide the next phase. |

Required dry-run guarantees:

- no state mutation;
- no memory promotion;
- no recall event write;
- no growth execution;
- no adapter ownership;
- no identity mutation;
- no tool execution;
- no model call;
- no external API call.

## 4. Inputs

The future dry-run input envelope should be minimal:

| Input Field | Required | Meaning | Boundary |
|---|---:|---|---|
| `user_message` | yes | The message or fixture content being previewed. | Not stored as memory by the harness. |
| `session_id` | yes | Local preview session reference. | Not a durable session runtime. |
| `actor_id` | yes | Actor reference for attribution. | Does not create or mutate identity. |
| `timestamp` | no | Optional provided timestamp for display or deterministic fixture comparison. | Not Temporal Awareness runtime. |
| `platform_ref` | no | Optional source label, such as `local_cli` or fixture name. | Not adapter integration or platform ownership. |
| `privacy_scope` | yes | Declared privacy boundary such as `private`, `local`, or `shareable_fixture`. | Must bias toward suppression when unclear. |
| `context_request` | no | Optional user-requested context focus. | Not automatic retrieval or prompt construction. |

Future implementation should reject missing required fields, unsafe privacy
scope, and unsupported formats without writing state.

## 5. Outputs

The future report should contain these sections:

| Output Section | Meaning | Boundary |
|---|---|---|
| `intake_preview` | Normalized input envelope, privacy scope, source reference, and safe display text or redaction note. | Preview only; not event persistence. |
| `selected_context_preview` | Candidate context references, omission reasons, and context gaps. | Not retrieval execution, memory rewrite, or prompt construction. |
| `candidate_preview` | Possible memory, claim, growth-review, meaning-shift, recall-event, or task candidates. | Candidate is not promotion. |
| `review_queue_preview` | Candidate ordering, review depth hint, risk label, and blocked reason. | Review queue preview is not lifecycle. |
| `boundary_status` | Disabled, blocked, RFC-only, or future-direction boundary flags. | Boundary status is not runtime enforcement. |
| `observatory_summary` | Compact status summary using Foundation Observatory naming. | Observatory summary is not decision execution. |
| `non_execution_invariants` | Explicit false/disabled flags for forbidden actions. | Invariants are report assertions, not runtime capabilities. |

Required non-execution invariants:

```yaml
harness_dry_run_only: true
execution_prohibited: true
state_unchanged: true
identity_core_mutated: false
memory_rewrite_executed: false
recall_mutation_executed: false
growth_engine_executed: false
temporal_event_executed: false
tool_execution_enabled: false
policy_executor_enabled: false
companion_feature_enabled: false
adapter_integration_required: false
model_call_executed: false
external_api_call_executed: false
```

## 6. Candidate Types

The future dry-run may preview these candidate types only:

| Candidate Type | Preview Meaning | Explicitly Not |
|---|---|---|
| `memory_candidate` | The input may be relevant to future memory review. | memory write, memory rewrite, or memory promotion |
| `claim_candidate` | The input may create, support, conflict with, or weaken a claim. | claim revision or belief update |
| `growth_candidate_review` | The input may be relevant to future growth review. | growth promotion or identity update |
| `meaning_shift_candidate` | The input may change how an existing memory or claim is interpreted. | semantic mutation or memory rewrite |
| `recall_event_candidate` | The input may raise a future question about recall event policy. | recall event write |
| `task_update_candidate` | The input may suggest a future task update. | task closure, task mutation, or automatic roadmap execution |

Rules:

- candidate is not promotion;
- preview is not persistence;
- review queue preview is not lifecycle;
- candidate risk can be shown, but it must not authorize execution;
- candidate output must include blocked boundaries when relevant.

## 7. Boundary Rules

The future harness dry-run must forbid:

- write state;
- mutate identity;
- rewrite memory;
- write recall event;
- promote growth;
- execute tool;
- call model;
- call external API;
- integrate AstrBot;
- integrate adapters;
- run companion behavior;
- run temporal runtime;
- execute policy;
- execute reconstruction reducer;
- compact events;
- create roadmap phase;
- auto-select the next phase.

If a future implementation cannot prove a boundary is disabled, it should mark
the dry-run as blocked and return a report explaining why.

## 8. Relationship To Observatory

The future `harness-dry-run` should end with an `observatory_snapshot` so the
founder can compare interaction pressure against the same status vocabulary used
by `foundation-observatory-report`.

Relationship:

| Artifact | Role |
|---|---|
| [FOUNDATION_OBSERVATORY_REPORT.md](./FOUNDATION_OBSERVATORY_REPORT.md) | Defines the founder-facing status sections that the snapshot should reuse. |
| [MINIMAL_OBSERVATORY_CLI_PLAN.md](./MINIMAL_OBSERVATORY_CLI_PLAN.md) | Defines why observability must remain read-only. |
| [OBSERVATORY_USABILITY_REVIEW.md](./OBSERVATORY_USABILITY_REVIEW.md) | Explains why founder-facing output must be plain and boundary-first. |
| [THIN_INTERACTION_HARNESS_RFC.md](./THIN_INTERACTION_HARNESS_RFC.md) | Defines the harness as preview-only. |
| [CONVERSATION_INTAKE_CONTRACT_RFC.md](./CONVERSATION_INTAKE_CONTRACT_RFC.md) | Provides intake envelope vocabulary. |
| [CONTEXT_PACKAGE_PREVIEW_RFC.md](./CONTEXT_PACKAGE_PREVIEW_RFC.md) | Provides context preview vocabulary. |
| [REVIEW_QUEUE_PREVIEW_RFC.md](./REVIEW_QUEUE_PREVIEW_RFC.md) | Provides candidate and review queue preview vocabulary. |
| [CORE_INTERACTION_HARNESS_ROADMAP.md](./CORE_INTERACTION_HARNESS_ROADMAP.md) | Provides readiness gates and non-negotiable boundaries. |

Observatory only displays status. It does not decide, approve, promote, or
execute. The harness must not automatically execute the observatory's next-step
recommendations.

## 9. Tests Plan

If P100 explicitly approves implementation, the first test plan must include:

| Test | Required Assertion |
|---|---|
| Future CLI would run dry-run | A future `python3 -m one_core.cli harness-dry-run` implementation would return a report for valid fixture input. |
| No state file changed | State directory checksums or mtimes remain unchanged after dry-run. |
| Markdown output sections | Markdown contains all required dry-run sections. |
| JSON output keys | JSON contains all required top-level keys. |
| Chinese output naming | `--lang zh` uses founder-facing Chinese display names. |
| Candidate preview does not promote | Candidate outputs never contain promotion, lifecycle, or mutation results. |
| Boundary monitor disables forbidden actions | All forbidden actions are disabled or blocked in output. |
| Invalid input handled safely | Missing input, unsafe privacy scope, unsupported format, or path errors fail without state writes. |
| No model or external call | Tests prove no model, network, adapter, or external API call is needed. |
| Output path safety | `--output` writes only the requested report and never creates state artifacts. |

Test fixtures should be deterministic, local, and small. They should not contain
real secrets, live chat logs, adapter payloads, cloud references, or private
conversation exports.

## 10. P100 Candidate Directions

Candidate P100 directions only, not executed by P99:

1. Minimal CLI Harness Dry-Run Implementation.
2. Harness Dry-Run Output Schema.
3. Boundary Monitor CLI Extension.
4. Context Package Preview Static Generator.

Recommended order: if the founder approves implementation, start with a
strictly local, no-write, no-model-call dry-run command and its tests. If the
founder does not approve implementation, pause for founder / CTO review.

## Non-Execution Statement

P99 does not implement:

- `harness-dry-run`;
- CLI command registration;
- parser changes;
- output schema files;
- validation code;
- tests;
- state reads beyond existing documentation checks;
- state writes;
- memory writes;
- recall event writes;
- growth lifecycle;
- identity mutation;
- memory rewrite;
- temporal runtime;
- thought loop;
- tool execution;
- model calls;
- external API calls;
- adapter or AstrBot integration;
- companion behavior;
- UI;
- product layer;
- policy executor;
- reconstruction reducer execution;
- event compaction;
- automatic roadmap execution;
- P100.
