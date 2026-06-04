# Founder Console Risk Review

Chinese version: [FOUNDER_CONSOLE_RISK_REVIEW_ZH.md](./FOUNDER_CONSOLE_RISK_REVIEW_ZH.md)

Status: `P135`, `risk-review`, `document-only`, `non-runtime`.

P135 reviews the risks introduced by planning a future Thin Founder Console. It
does not implement a console, command, UI, Companion layer, adapter integration,
model call, tool execution, write path, policy executor, or rebuild.

## Risk Summary

The founder console is safe only if it remains a local visibility surface. Its
main danger is psychological and architectural: because it looks like an
application, it can tempt the project to behave like a product too early.

## Top Risks

| Risk | Why It Matters | Mitigation |
|---|---|---|
| product-layer creep | A readable console can become a user product before core readiness. | Keep founder-only language and no product routes. |
| Companion creep | A console that answers founder questions can start sounding like a social agent. | Keep it report-oriented, not relational. |
| automatic roadmap creep | Next-step candidates can be mistaken for selected actions. | Show candidate status and require explicit founder approval. |
| write-path creep | Output files can become a bridge to formal state writes. | Keep reports outside state stores and mark report-only. |
| adapter creep | Adapter pressure can return through "preview" language. | Keep shadow adapter examples disconnected and no-ingest. |
| model-call creep | A console may seem more useful with an LLM summary. | Keep deterministic local reports until a later boundary exists. |
| policy-executor creep | Boundary warnings can become automatic enforcement. | Keep warnings as display, not execution. |
| founder over-trust | A polished report can look more authoritative than it is. | Show source refs, omissions, and uncertainty. |
| temporal overreach | Temporal cues can be mistaken for thought dynamics. | Keep CTM-inspired content symbolic and review-only. |
| capability overreach | Tool evidence can be mistaken for authorized tools. | Keep Tool-First evidence as candidate/review only. |

## Founder-Facing Warning

The future console should explicitly say:

```text
This is a visibility surface.
It does not decide, write, connect, execute, or rebuild.
```

Without that line, founder-facing clarity can become founder-facing
overconfidence.

## Risky Phrases To Avoid

Avoid labels such as:

- "approved next step";
- "memory restored";
- "identity updated";
- "adapter ready";
- "tool verified";
- "temporal state changed";
- "rebuild ready" unless final verification has actually passed.

Prefer:

- "candidate next step";
- "source-backed preview";
- "manual review required";
- "blocked boundary";
- "report-only";
- "not ready yet".

## CTM-Inspired Temporal Risk

The console may make temporal concepts easier to see. That increases risk of
misreading them as inner thought.

Mitigation:

- use "temporal review cue" rather than "thought state";
- use "review depth suggestion" rather than "deliberation executed";
- use "thought-trace policy reminder" rather than "thought trace captured";
- never claim consciousness or neural equivalence.

## Tool-First Risk

The console may make capability candidates look operational.

Mitigation:

- show "verification evidence is not authorization";
- show "candidate is not tool library entry";
- show unsafe candidates as quarantined or deferred;
- keep tool execution disabled and visible.

## Risk Decision

The founder console block may continue because the risk is manageable at the
document-only planning level.

It should not proceed to implementation unless P134 acceptance criteria remain
visible and a future implementation phase proves:

- local-only operation;
- no external IO;
- no model call;
- no state mutation;
- no adapter connection;
- no automatic next step;
- no rebuild.

## Completion Statement

P135 records the main danger of the founder console: making the project feel
ready before it is ready. The mitigation is to keep the console report-only,
founder-only, local, explicit about blocked actions, and humble about what it
knows.
