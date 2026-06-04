# Source-Backed Harness Usability Review

Chinese version: [SOURCE_BACKED_HARNESS_USABILITY_REVIEW_ZH.md](./SOURCE_BACKED_HARNESS_USABILITY_REVIEW_ZH.md)

Status: `P120`, `review-only`, `document-only`, `non-runtime`.

P120 reviews whether P112-P119 improved the dry-run harness after the P111
founder review. It does not change runtime behavior, write state, write memory,
write recall events, mutate identity, call a model, execute tools, integrate
adapters, enter product work, or start rebuild work.

## Review Scope

P112-P119 were the State-Backed Read-Only Harness cycle:

- P112 defined state-backed as whitelisted local source citation only.
- P113 listed the approved Markdown source inventory.
- P114 planned a deterministic read-only loader.
- P115 implemented `one_core/source_loader.py`.
- P116 hardened whitelist validation.
- P117 exposed `harness-source-inventory`.
- P118 added pressure-specific `source_refs_preview` to `harness-dry-run`.
- P119 added source-backed risk and open-question mappings.

The cycle did not read user-supplied paths, parse private state, call network,
call a model, write formal events, write memory, or authorize rebuild.

## Commands Reviewed

Reviewed representative commands:

```bash
python3 -m one_core.cli harness-dry-run --input "我现在有点看不清这个项目到底做了什么" --lang zh --format json
python3 -m one_core.cli harness-dry-run --input "我隔了很久回来，怎么恢复会话？" --lang zh --format json
python3 -m one_core.cli harness-dry-run --input "这个工具候选验证成功了，能不能直接加入工具库？" --lang zh --format json
python3 -m one_core.cli harness-source-inventory --format markdown --lang zh
```

All reviewed commands kept the configured temporary state paths absent and kept
forbidden boundary flags false/disabled.

## Readability Score

Founder-facing readability: **8.4 / 10**.

This is an improvement over P108's 8.0 / 10, but not a leap. The main gain is
not prettier wording; it is provenance. The founder can now see which source
documents, risk IDs, and open questions support each pressure route.

The score is not higher because the output is now denser. `source_refs_preview`
is useful, but long excerpts can make Markdown and JSON feel heavy.

## What Improved

The harness is now visibly source-backed:

- observability pressure cites `foundation_status`, `phase_index`,
  `observatory_report`, `visual_naming`, and P108 review evidence;
- temporal pressure cites `temporal_awareness`, `ctm_temporal_dynamics`,
  `temporal_coherence_eval`, `deliberation_tick`, `thought_trace_storage`, and
  `session_resume`;
- capability pressure cites `tool_first_self_evolution`,
  `capability_evolution_boundary`, `deliberation_tick`, and `risk_register`;
- reconstruction pressure cites reducer and payload/diff policy documents.

The harness is also clearer about why a pressure is risky:

- temporal pressure maps to risks R5, R6, and R7;
- capability pressure maps to R19, R20, R21, and R22;
- reconstruction pressure maps to R8, R9, and R13;
- adapter pressure maps to R12, R18, and R11.

Open questions are now visible next to the preview. This helps the founder see
that many items are clarified but still not implemented.

## What Still Feels Static

The mapping is deterministic and document-backed, but still static:

- it does not inspect actual `work/01_state`;
- it does not compare current task status or memory summaries;
- it does not rank sources by relevance inside a pressure type;
- it does not summarize the selected documents beyond short excerpts;
- it does not decide whether a risk is currently active.

This is acceptable for P120 because the goal was "see source backing before
acting," not "perform real retrieval or verification."

## Most Useful Pressure Types

Most improved:

- `temporal_pressure`: now clearly carries the CTM-inspired Temporal Dynamics
  line while keeping CTM runtime, thought loop, temporal event write, and recall
  mutation blocked.
- `capability_evolution_pressure`: now clearly carries Tool-First In-Situ
  Self-Evolution while keeping tool execution and automatic promotion blocked.
- `reconstruction_pressure`: now points to reducer and payload/diff documents
  without implying reducer execution.
- `adapter_boundary_pressure`: now shows adapter boundary sources without
  approving AstrBot or external adapter work.

Still weaker:

- `observability_pressure`: source refs help, but the founder still needs a
  compact "what has actually been built" summary.
- `unknown_pressure`: safely conservative, but remains low-information.

## Boundary Review

P112-P119 preserved the requested boundaries:

- no formal state/event/memory/recall write;
- no identity mutation;
- no memory rewrite;
- no growth lifecycle execution;
- no tool execution or tool promotion;
- no temporal runtime or CTM runtime;
- no external IO, model call, adapter integration, Companion, Web UI, or
  product layer;
- no rebuild start.

The new `risk_refs_preview` and `open_question_refs_preview` are review aids.
They are not policy execution, authorization, or automatic next-step selection.

## Founder Judgment

P112-P119 solved the P111 next weakness well enough: the harness can now show
which approved local documents support a preview route.

It did not make the harness intelligent, and that is good. It made the harness
more auditable. The current system now better follows:

```text
first see, then act
first read-only, then writes
first preview, then persistence
first candidate, then review
```

## Recommendation

It is appropriate to enter P121 Core Lockdown / Quarantine planning.

P121 should not rebuild 01. It should freeze the core before any future test
connection to old 01, models, imports, adapters, or external systems. The next
safe question is not "can we write?" It is "what must be quarantined before any
future read or import can be trusted?"

## Do Not Do Next

- Do not connect old 01.
- Do not connect AstrBot or any external adapter.
- Do not call an LLM.
- Do not write formal memory, recall events, identity, or event logs.
- Do not implement Temporal Awareness runtime, CTM runtime, thought loop, tool
  execution, policy executor, or growth lifecycle.
- Do not start local rebuild.

## P121 Candidate Direction

Recommended P121: **Core Lockdown Mode RFC**.

It should define how future work blocks or quarantines:

- unverified model memory claims;
- identity claim candidates;
- adapter context artifacts;
- prompt contamination candidates;
- unverified capability claims.

This should remain RFC-only unless explicitly approved as a later no-write
validator.
