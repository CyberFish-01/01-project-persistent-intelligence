# Capability Context Pack RFC

Chinese version: [CAPABILITY_CONTEXT_PACK_RFC_ZH.md](./CAPABILITY_CONTEXT_PACK_RFC_ZH.md)

Status: `P142`, `RFC-only`, `document-only`, `non-runtime`.

P142 defines the future `capability_pack` for context packages using
Tool-First In-Situ Self-Evolution vocabulary. It does not implement tool
execution, tool verification runtime, tool promotion, tool library mutation,
dependency installation, policy executor, model calls, adapter integration,
state writes, memory writes, identity mutation, or rebuild.

## Core Rule

```text
capability_pack is evidence context.
evidence is not authorization.
candidate is not tool-library entry.
capability evolution is not subject growth.
```

## Pack Purpose

The future `capability_pack` helps a founder or model-as-resource see
tool/procedure pressure without accidentally enabling tools.

It should make capability evidence reviewable, not executable.

## Allowed Fields

The pack may include:

- `tool_candidate`
- `procedure_candidate`
- `verification_evidence_preview`
- `execution_failure_note`
- `reproducibility_hint`
- `cautionary_procedural_memory_candidate`
- `capability_growth_candidate_review`
- `tool_authorization_gate`
- `quarantine_route`
- `capability_boundary_reminder`

## Forbidden Fields

The pack must not include:

- executable tool handle;
- shell command to run;
- dependency install instruction;
- credential or token;
- policy executor rule;
- trusted tool-library entry;
- automatic promotion decision;
- subject growth claim;
- self-modifying runtime instruction.

## Capability Cue Matrix

| Cue | Meaning | Allowed Use | Forbidden Interpretation |
|---|---|---|---|
| tool candidate | A tool-like idea may be useful. | Route to review. | Tool is available to execute. |
| procedure candidate | A reusable process may exist. | Describe review target. | Procedure is trusted. |
| verification evidence | A result may support confidence. | Increase review confidence. | Authorization granted. |
| failure note | A failure may be cautionary. | Route to cautionary candidate. | Tool should be disabled globally. |
| reproducibility hint | Repetition may matter. | Ask for future evidence. | One success is enough. |
| authorization gate | Human approval is required. | Block promotion. | Gate has approved. |

## Tool-First Mapping

P142 preserves the Tool-First research line:

- tool improvement is capability evolution, not identity growth;
- procedure reuse is candidate, not trusted skill;
- verification result is evidence, not authorization;
- review object is not execution;
- unsafe candidate routes to quarantine or caution.

## Boundary Injection

Every `capability_pack` must include:

- `tool_execution_allowed: false`
- `tool_promotion_allowed: false`
- `auto_tool_promotion_allowed: false`
- `policy_executor_allowed: false`
- `dependency_install_allowed: false`
- `tool_library_mutation_allowed: false`
- `identity_growth_claim_allowed: false`

These are planned contract fields, not implemented runtime flags in P142.

## Relationship To Other Packs

The `capability_pack` should not replace:

- `task_pack`: tasks still need manual planning;
- `boundary_pack`: forbidden capabilities remain global;
- `claim_pack`: capability claims still need evidence;
- `response_strategy_pack`: future model instructions still need no-execution
  wording.

## Future Test Expectations

If implemented later, tests should verify:

- capability pack appears only when relevant;
- every capability item is candidate/evidence/review only;
- forbidden tool actions remain false;
- no executable handle is emitted;
- no dependency install is suggested;
- no capability item mutates identity or memory;
- unsafe items route to quarantine or caution.

## Completion Statement

P142 gives Tool-First In-Situ Self-Evolution a safe place inside future context
packages: candidate/evidence/review only, never execution, promotion, policy, or
subject growth.
