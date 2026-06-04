# Capability Evolution Boundary RFC

Chinese version: [CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md](./CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md)

Status: `P92`, `RFC-only`, `document-only`, `non-runtime`.

## Background

P91 established Tool-First Self-Evolution as a safer first direction for
self-evolving capability: tools, skills, and procedures can produce verifiable
task feedback, while Identity Core, memory rewrite, relationship memory, and
subject growth remain protected.

P92 defines the boundary around Capability Evolution so that tool-first
self-evolution does not slide into automatic tool execution, automatic tool
promotion, policy execution, or identity mutation.

This RFC does not implement runtime behavior, schemas, CLI commands, tool
execution, dependency installation, event writes, policy execution, memory
rewrite, identity mutation, adapter integration, UI, or product behavior.

## 1. Core Distinctions

### Capability Evolution

Capability Evolution is the review-governed improvement of tools, skills, and
procedures using task evidence.

Boundary: capability improvement does not imply identity growth.

### Subject Evolution

Subject Evolution is a meaning-bearing subject-state transition that may affect
continuity, identity interpretation, or long-term subject history.

Boundary: subject evolution remains high-gated and cannot be inferred from tool
success alone.

### Tool Candidate

A Tool Candidate is a proposed tool, script, function, command pattern, or
external capability wrapper.

Boundary: a tool candidate is not a trusted tool and not execution approval.

### Procedure Candidate

A Procedure Candidate is a proposed repeatable workflow with steps, checks,
inputs, outputs, rollback notes, and safety boundaries.

Boundary: a reusable procedure does not imply trusted tool.

### Skill Memory

Skill Memory is a possible future memory category for reviewed, reusable
capability knowledge.

Boundary: skill memory does not execute tools and does not update identity.

### Procedural Memory

Procedural Memory is reviewed memory about how to perform or avoid a procedure.
It may include success patterns and cautionary patterns.

Boundary: procedural memory is not a policy executor.

### Capability Evidence

Capability Evidence is review material generated from task results,
verification results, failures, reproducibility, safety checks, dependency
checks, or rollback notes.

Boundary: evidence supports review; it does not authorize action.

### Capability Growth Candidate

A Capability Growth Candidate proposes that evidence may indicate durable
capability improvement.

Boundary: it is not tool promotion, not subject growth, and not identity change.

### Subject Growth Candidate

A Subject Growth Candidate proposes that experience may represent
meaning-bearing subject growth.

Boundary: it requires stricter review than a capability growth candidate.

### Tool Authorization

Tool Authorization is a future explicit permission gate for executing or
promoting a tool under defined scope, inputs, outputs, dependencies, and
rollback conditions.

Boundary: authorization is not created by verification alone.

### Tool Verification

Tool Verification is a future evidence process that checks whether a candidate
worked, failed, reproduced, stayed within boundaries, and remained task-relevant.

Boundary: verification does not imply authorization.

Core rules:

```text
Capability improvement does not imply identity growth.
Verification does not imply authorization.
Reusable procedure does not imply trusted tool.
```

## 2. Boundary Model

### Allowed Scope

Capability Evolution may allow these review-only activities in future planning:

| Allowed Activity | Meaning | Boundary |
|---|---|---|
| tool candidate proposal | A possible tool is described for review. | It is not executed or promoted. |
| procedure candidate proposal | A repeatable workflow is described for review. | It is not active procedural memory. |
| verification evidence collection | Future checks may collect success, failure, reproducibility, safety, dependency, and rollback evidence. | Evidence collection is not authorization. |
| review-only capability growth candidate | A governance object reviews whether capability improved. | Candidate is not promotion. |
| cautionary procedural memory candidate | A failed or unsafe pattern is proposed as warning material. | Warning candidate is not executable policy. |

### Forbidden Scope

Capability Evolution must not allow:

- automatic tool execution;
- automatic tool promotion;
- automatic policy executor;
- automatic identity update;
- automatic memory rewrite;
- uncontrolled filesystem or network access;
- unreviewed dependency installation;
- self-modifying runtime.

These are blocked even if a candidate has succeeded once.

## 3. Evidence and Review

Evidence can raise review quality without authorizing action.

| Evidence / Review Signal | Interpretation | Boundary |
|---|---|---|
| `execution_success` | Candidate produced the expected bounded result. | Evidence, not authorization. |
| `execution_failure` | Candidate failed, errored, or produced unsafe output. | May become cautionary evidence. |
| `reproducibility` | Result repeats under comparable conditions. | Raises review confidence only. |
| one-off success | A single success happened once. | Not enough for promotion. |
| unsafe candidate | Candidate violates or pressures a safety boundary. | Route to quarantine. |
| human / founder review | Human authority reviews promotion scope. | Remains the promotion gate. |

Review implications:

- `execution_success` can be evidence, but not authorization.
- `execution_failure` can become cautionary evidence.
- reproducibility increases review confidence.
- one-off success is insufficient for promotion.
- unsafe candidate enters quarantine.
- human / founder review remains the promotion gate.

## 4. Integration With Existing Core

This RFC only describes future integration boundaries.

### Task Hub

Task Hub supplies task pressure, task context, and task outcome references.

Boundary: Task Hub does not automatically create or run tools.

### Procedural Memory

Procedural Memory may later receive approved procedure candidates.

Boundary: procedure candidates are not active procedural memory until reviewed.

### Cautionary Memory

Cautionary Memory may later receive failed or unsafe procedure candidates as
warning material.

Boundary: cautionary memory warns; it does not enforce policy.

### Event Log

Event Log may later reference verification results as audit evidence if a future
event policy exists.

Boundary: P92 does not write events or define event schemas.

### Governance Surface

Governance Surface owns cross-layer review objects for tool candidates,
procedure candidates, capability evidence, and capability growth candidates.

Boundary: Governance Surface is not a policy executor.

### Growth Candidate Review

Growth Candidate Review should keep capability growth candidate review separate
from subject growth candidate review.

Boundary: capability growth candidate does not mutate identity.

### Tool-First Self-Evolution RFC

P91 defines why tool-first self-evolution is safer than identity-first
self-modification.

Boundary: P92 narrows P91 into explicit allowed and forbidden boundary classes.

### Thin Interaction Harness

Thin Interaction Harness may later preview tool candidates, procedure
candidates, verification evidence, quarantine state, and review routing.

Boundary: P92 does not implement harness runtime, CLI commands, adapter work, UI,
or product behavior.

## 5. Risk Register

| Risk | Description | Boundary Response |
|---|---|---|
| tool library contamination | Low-quality or unsafe candidates become reusable. | No auto promotion; require safe library policy later. |
| unsafe reusable procedures | A repeatable procedure can repeat harm. | Failed or unsafe procedures route to caution/quarantine. |
| verification over-trust | Passing checks are treated as authorization. | Verification remains evidence only. |
| policy executor creep | Review rules become automatic runtime policy. | Review objects do not execute. |
| capability growth mistaken as subject growth | Better tools are interpreted as identity development. | Capability and subject evolution stay layered. |
| dependency / filesystem / network risk | Candidates require packages, files, APIs, credentials, or network. | Dependency and safety checks are required review evidence. |
| self-modification risk | Capability work pressures runtime, prompt, code, memory, or identity edits. | Self-modifying runtime remains forbidden. |
| hidden autonomy | Tool proposal, verification, reuse, and promotion form an invisible loop. | Human / founder promotion gate remains required. |

## 6. Evaluation Ideas

These are future evaluation ideas only. P92 does not implement them.

| Scenario | Expected Review-Only Outcome |
|---|---|
| `successful_tool_candidate_remains_review_only` | Success creates evidence, not execution or promotion. |
| `failed_tool_candidate_becomes_cautionary_candidate` | Failure becomes cautionary procedural candidate. |
| `one_off_success_rejected_for_promotion` | Single success is insufficient. |
| `unsafe_tool_candidate_routed_to_quarantine` | Unsafe candidate is quarantined or blocked. |
| `reproducible_result_increases_review_confidence` | Reproducibility increases confidence without authorization. |
| `capability_candidate_does_not_mutate_identity` | Capability review leaves Identity Core unchanged. |
| `verification_result_enters_audit_trail_only` | Verification result is evidence or audit reference only. |

## 7. P93 Candidate Directions

P93 candidates, not executed here:

- Tool Verification Evidence Model;
- Tool Candidate Review Schema;
- Procedural Memory Alignment;
- Safe Tool Library Policy;
- Capability Growth Evaluation Plan.

## Non-Execution Statement

P92 is RFC-only. It does not implement tool execution, automatic tool generation,
automatic tool promotion, policy execution, identity mutation, memory rewrite,
growth execution, dependency installation, filesystem access, network access,
adapter integration, UI, product behavior, or runtime behavior.
