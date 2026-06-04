# Tool-First Self-Evolution RFC

Chinese version: [TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md](./TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md)

Status: `P91`, `RFC-only`, `document-only`, `non-runtime`.

## 1. Background

P0-P90 established 01 Core's foundation core, growth semantics, growth
candidate review, CTM-inspired temporal dynamics, and thin interaction harness
planning. P91 asks how 01 Core should absorb ideas from Yunjue Agent / Zero-Start
In-Situ Self-Evolving Agent research without turning self-evolution into
identity mutation.

Yunjue Agent's public materials describe a zero-start setting where the agent
begins with an empty tool library and uses task interactions to synthesize,
verify, refine, and reuse tools. The central lesson for 01 Core is not that
identity should self-modify. The lesson is narrower and safer:

```text
tool evolution is useful because tool execution can produce verifiable feedback.
```

Tool execution feedback can often be checked as success, failure, error,
reproducibility, task relevance, or safety violation. That makes tools and
procedures a safer first layer for capability evolution than Identity Core,
personality, relationship memory, or subject growth.

01 Core should not directly self-edit identity. Capability evolution and subject
evolution must be layered:

- capability evolution concerns tools, skills, procedures, and verified task
  performance;
- subject evolution concerns meaning-bearing subject-state transitions that may
  affect continuity, identity pressure, and long-term interpretation.

This RFC translates tool-first self-evolution into a future 01 Core capability
evolution layer. It does not implement tool execution, tool generation, tool
promotion, policy execution, memory rewrite, recall writes, identity mutation,
or runtime integration.

External sources used as inspiration:

- [Yunjue Agent official project page](https://yunjueagent.com/)
- [Yunjue Agent technical report on arXiv](https://arxiv.org/abs/2601.18226)
- [Yunjue Technology blog introduction](https://www.yunjuetech.com/en/blog/YunjueAgent)

## 2. Core Distinction

### Capability Evolution

Capability Evolution is the review-governed improvement of tools, skills, and
procedures using objective task evidence.

Boundary: capability evolution is not subject evolution. It can improve what 01
Core may be able to do in a future system, but it does not decide who 01 is.

### Subject Evolution

Subject Evolution is an evidence-backed, reviewed, meaning-bearing state
transition that may affect continuity, identity interpretation, or long-term
subject history.

Boundary: subject evolution remains high-gated. It must not be triggered by tool
success alone.

### Tool Candidate

A Tool Candidate is a proposed tool, script, function, command pattern, or
external capability wrapper that may help complete tasks.

Boundary: a tool candidate is not a tool-library entry, not trusted code, and
not execution approval.

### Procedure Candidate

A Procedure Candidate is a proposed repeatable workflow: a sequence of steps,
checks, inputs, outputs, rollback notes, and safety boundaries.

Boundary: a procedure candidate is not active procedural memory and not
executable policy.

### Skill Memory

Skill Memory is a future memory category for reviewed, reusable capability
knowledge such as "how to perform a bounded task safely."

Boundary: skill memory is not identity memory, not policy execution, and not
automatic tool invocation.

### Procedural Memory

Procedural Memory is reviewed memory about how to perform or avoid a procedure.
It can include success patterns and cautionary patterns.

Boundary: procedural memory does not execute itself.

### Capability Growth Candidate

A Capability Growth Candidate is a review object proposing that evidence from
tool or procedure use indicates a durable capability improvement.

Boundary: it is a review object, not promotion. It cannot update the tool
library, memory layer, policy layer, or Identity Core by itself.

### Subject Growth Candidate

A Subject Growth Candidate is a review object proposing that experience may
represent meaning-bearing subject growth.

Boundary: it requires stronger evidence and stricter gates than a capability
growth candidate.

Core rule:

```text
tool improvement is not identity growth.
```

工具能力增强不等于主体身份成长。

## 3. Proposed Flow

The future capability evolution layer should be modeled as a review-only chain:

```text
Task Interaction
-> Execution Trace
-> Tool Candidate
-> Verification Result
-> Capability Evidence
-> Procedural Memory Candidate
-> Capability Growth Candidate Review
```

### Flow Semantics

| Step | Role | Review Boundary |
|---|---|---|
| Task Interaction | A task creates pressure for a capability. | A task is not authorization to create or run tools. |
| Execution Trace | A future trace records what happened, what inputs were used, and what result occurred. | A trace is evidence, not hidden reasoning storage. |
| Tool Candidate | A possible tool is proposed from task pressure or prior traces. | Candidate is not promotion. |
| Verification Result | A future check reports success, failure, reproducibility, safety, and dependency status. | Verification is not authorization. |
| Capability Evidence | The result becomes review material for capability improvement. | Evidence is not automatic trust. |
| Procedural Memory Candidate | A repeatable or cautionary procedure may be proposed. | Candidate is not active procedural memory. |
| Capability Growth Candidate Review | Governance reviews whether capability improved and what remains unsafe. | Review object is not execution. |

All candidates remain review-only. No candidate is automatically added to the
tool library. No candidate changes Identity Core. No candidate creates a policy
executor.

## 4. Evidence Model

Tool-first evolution needs evidence that is more objective than tone, identity
pressure, or vague self-description.

| Evidence | Meaning | Boundary |
|---|---|---|
| `execution_success` | The tool or procedure produced the expected bounded result. | Success does not make it trusted. |
| `execution_failure` | The tool or procedure failed, errored, or produced incomplete output. | Failure may be useful caution evidence. |
| `test_result` | A deterministic check passed, failed, or was inconclusive. | A test result is evidence, not policy. |
| `reproducibility` | The result can be repeated under comparable inputs. | Reproducibility increases review confidence only. |
| `task_relevance` | The candidate actually addresses the task need. | Relevance does not remove safety review. |
| `safety_boundary_check` | The candidate was checked against privacy, filesystem, network, dependency, and mutation boundaries. | Passing a boundary check is not blanket authorization. |
| `dependency_check` | Required packages, commands, APIs, credentials, and platform assumptions are visible. | Dependency availability is not approval to install or call them. |
| `rollback_possible` | A bad result can be undone or isolated. | Rollback possibility does not justify risky execution. |
| `human_review_required` | Human or founder review is required before promotion or reuse. | Required review blocks automation. |

Tool execution feedback can become objective evidence. It cannot automatically
become subject growth, memory rewrite, recall event write, identity update, or
policy execution.

## 5. Review Boundary

### `tool_candidate_review`

Reviews whether a proposed tool is safe, relevant, testable, reproducible, and
bounded.

Does not:

- execute the tool;
- install dependencies;
- add the tool to a library;
- grant future automatic use.

### `procedure_candidate_review`

Reviews whether a workflow should become procedural memory, cautionary memory,
or remain rejected.

Does not:

- activate the procedure;
- create executable policy;
- rewrite task history;
- bypass human review.

### `capability_growth_candidate_review`

Reviews whether evidence supports a durable capability improvement.

Does not:

- promote growth;
- mutate identity;
- update the tool library;
- rewrite memory;
- create a policy executor.

Review principles:

```text
review object is not execution.
candidate is not promotion.
verification is not authorization.
successful tool is not automatically trusted.
failed tool may become cautionary procedural memory.
```

## 6. Integration With Existing 01 Core

This section describes future collaboration surfaces only. It does not implement
them.

### Task Hub

Task Hub owns task pressure and task outcome references. A future capability
evolution layer may read task needs from Task Hub and return review-only
capability evidence.

Boundary: Task Hub does not auto-create tools.

### Procedural Memory

Procedural Memory can receive reviewed procedure candidates after governance
approval.

Boundary: procedural memory does not execute itself and does not become a policy
executor.

### Cautionary Memory

Failed, unsafe, or misleading tool candidates can become cautionary procedural
memory candidates.

Boundary: cautionary memory warns; it does not enforce runtime behavior.

### Growth Candidate Review

Capability growth candidate review should remain separate from subject growth
candidate review.

Boundary: capability improvement does not equal identity growth.

### Event Log

Future verification results may be referenced by Event Log as evidence if a
future event policy exists.

Boundary: this RFC does not write events, define event schemas, or execute event
capture.

### Governance Surface

Governance Surface owns tool, procedure, and capability growth review objects
because they cross Task Hub, memory, event evidence, and safety boundaries.

Boundary: Governance Surface is not a policy executor.

### Claim Graph

Claim Graph may store claims about capability only if evidence and scope are
clear, for example "tool candidate X succeeded on task class Y under constraint
Z."

Boundary: capability claims are not identity claims.

### Thin Interaction Harness

The thin harness may eventually preview task interaction, execution trace
summaries, candidate reviews, and boundary flags.

Boundary: P91 does not implement harness runtime, CLI commands, adapters, UI, or
tool execution.

## 7. Risks

| Risk | Why It Matters | P91 Boundary |
|---|---|---|
| Tool evolution becomes uncontrolled autonomy | Tool synthesis plus reuse can create an action loop. | P91 is RFC-only and review-only. |
| Verification is mistaken for authorization | A passing check can be overread as permission to reuse. | Verification result is evidence only. |
| Tool library pollution | Low-quality tools can accumulate and mislead future tasks. | No auto promotion or library mutation. |
| Unsafe tool candidate reuse | A candidate may touch network, filesystem, credentials, or private data. | Safety and dependency checks are required review evidence. |
| Capability growth is mistaken for identity growth | Better tools can be confused with subject development. | Capability and subject evolution remain layered. |
| Policy executor appears too early | Reviews can accidentally become automatic rules. | Review objects do not execute policy. |
| Self-modification crosses boundary | Tool improvement could pressure code, prompt, memory, or identity edits. | No self-modification is approved. |
| Dependency / network / filesystem risk | Tools often require packages, APIs, files, or credentials. | Dependency checks and rollback notes are review evidence only. |

## 8. Boundaries

P91 explicitly forbids:

- tool execution runtime implementation;
- automatic tool generation;
- automatic tool promotion;
- policy executor implementation;
- Identity Core modification;
- memory rewrite;
- recall event writes;
- companion, UI, AstrBot, or adapter integration;
- product layer work.

Additional boundaries:

- no new dependency;
- no CLI command;
- no schema mutation;
- no validation or evaluation implementation;
- no tool library mutation;
- no event write;
- no harness implementation.

## 9. Evaluation Ideas

These are future evaluation ideas only. P91 does not implement them.

| Scenario | Expected Review-Only Outcome |
|---|---|
| `successful_tool_candidate_creates_capability_evidence` | Success becomes evidence, not promotion. |
| `failed_tool_candidate_creates_cautionary_procedural_candidate` | Failure becomes cautionary review material. |
| `unsafe_tool_candidate_routed_to_quarantine` | Unsafe candidate is blocked or quarantined. |
| `reproducible_tool_result_increases_review_confidence` | Reproducibility raises confidence without granting trust. |
| `one_off_success_not_enough_for_promotion` | Single success remains insufficient. |
| `capability_growth_candidate_does_not_mutate_identity` | Capability review leaves Identity Core unchanged. |
| `verification_result_enters_event_log_as_evidence` | Future event reference is evidence only, if a policy exists. |
| `tool_first_evolution_remains_review_only` | The system produces review objects, not execution. |

## 10. P92 Candidate Directions

P92 candidates, not executed here:

- Capability Evolution Boundary RFC;
- Tool Verification Evidence Model;
- Tool Candidate Review Schema;
- Procedural Memory Alignment;
- Safe Tool Library Policy;
- Capability Growth Evaluation Plan.

## Non-Execution Statement

P91 is an RFC. It does not implement tool execution, tool generation, tool
promotion, policy execution, event writing, memory writing, identity mutation,
adapter integration, UI, product behavior, or runtime behavior.
