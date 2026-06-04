# Founder Console Roadmap

Chinese version: [FOUNDER_CONSOLE_ROADMAP_ZH.md](./FOUNDER_CONSOLE_ROADMAP_ZH.md)

Status: `P136`, `roadmap`, `document-only`, `non-runtime`.

P136 closes the Thin Founder Console planning block. It does not implement a
console, CLI command, Web UI, Companion, adapter integration, model call, tool
execution, write path, policy executor, or rebuild.

## What P131-P136 Established

| Phase | Contribution |
|---|---|
| P131 | Boundary: local, founder-only, no-write visibility, not product behavior. |
| P132 | Flow: see status, preview input path, inspect boundaries, choose manually. |
| P133 | Contract: only explicit report outputs, no formal state or memory writes. |
| P134 | Acceptance criteria: visibility without autonomy. |
| P135 | Risk review: product, Companion, roadmap, write, adapter, model, temporal, and capability creep. |

## Roadmap Position

The founder console is not the next thing to implement by default.

The safer next work is to define **Context Package Builder planning** first,
because a future console should not invent context packaging on the fly. It
should display or preview a well-defined package shape.

## Future Console Milestones

If implementation is approved later, the roadmap should be:

1. Static founder report surface.
2. Read-only source inventory panel.
3. Harness dry-run panel.
4. Boundary monitor panel.
5. Review queue preview panel.
6. Context package preview panel after P137-P142 define the package contract.
7. Pre-rebuild verification panel after P148-P154 define the verification gate.

Each milestone must pass P133 no-write contract and P134 acceptance criteria.

## Do Not Build Yet

Do not build:

- Web UI;
- Companion layer;
- chat product;
- adapter panel;
- live old 01 import view;
- model response view;
- tool execution view;
- temporal runtime view;
- rebuild execution button.

## Bridge To P137-P142

P137-P142 should define how 01 Core prepares context for a future model call
without calling a model.

The founder console should eventually be able to display:

- `identity_pack`
- `state_pack`
- `task_pack`
- `claim_pack`
- `memory_pack`
- `boundary_pack`
- `temporal_pack`
- `capability_pack`
- `response_strategy_pack`

But P136 does not define those packs in detail. It only identifies them as the
next planning block.

## CTM-Inspired Temporal Roadmap

Temporal console content should wait for a `temporal_pack` contract. That pack
may later display elapsed-time cues, review-depth suggestions, unresolved
tension, and delayed alignment signals as symbolic review material only.

No CTM runtime, thought loop, thought trace storage, temporal event write,
recall write, or identity update is allowed.

## Tool-First Roadmap

Capability console content should wait for a `capability_pack` contract. That
pack may later display tool candidates, procedure candidates, verification
evidence, and capability review gates as candidate/evidence/review material
only.

No tool execution, tool promotion, dependency installation, policy executor, or
subject-growth claim is allowed.

## Roadmap Decision

P131-P136 are complete enough to proceed to **Context Package Builder planning**
before any console implementation.

Proceed next to:

- Context Package Builder RFC;
- Context Package Preview CLI Plan;
- Source Selection Matrix;
- Boundary Injection RFC;
- CTM Temporal Context Pack RFC;
- Capability Context Pack RFC.

## Completion Statement

P136 closes the Thin Founder Console block. The project now knows what a founder
console must be and must not be. The next safe frontier is defining context
packages before model orchestration, console implementation, adapter work, or
rebuild.
