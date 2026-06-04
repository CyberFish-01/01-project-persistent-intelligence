# Post-Harness Founder Review

Chinese version: [POST_HARNESS_FOUNDER_REVIEW_ZH.md](./POST_HARNESS_FOUNDER_REVIEW_ZH.md)

Status: `P111`, `review-only`, `planning`, `document-only`, `non-runtime`.

P111 reviews whether P102-P110 actually solved the P101 usability problem and
whether the project is ready to consider a State-Backed Read-Only Harness. It
does not change harness runtime, CLI behavior, state, memory, recall policy,
identity, tools, adapters, UI, or product surfaces.

## 1. What Was The P101 Problem?

P101 found that the first `harness-dry-run` was safe but too static.

The command already proved the most important boundary: no state write, no
memory write, no recall write, no identity mutation, no model call, no adapter,
and no tool execution. But it did not yet help the founder understand the
specific pressure created by an input.

Main P101 issues:

- very different inputs received nearly the same candidate table;
- `context_package_preview` was mostly a generic foundation reference list;
- growth, AstrBot, product-layer, and tool-library questions were not routed
  differently enough;
- boundary flags were visible but not always loud for the current input;
- founder-facing readability scored **6.5 / 10**;
- the harness prevented bad action, but did not yet guide what to review next.

## 2. What Did P102-P110 Solve?

| Phase | What It Solved | Remaining Boundary |
|---|---|---|
| P102 | Added deterministic pressure routing for observability, growth, adapter, product, capability, temporal, reconstruction, and unknown inputs. | Classification remains rule-based, not understanding. |
| P103 | Added founder summary, human-readable risks, next step, and do-not-do list. | Summary is report text, not decision execution. |
| P104 | Added Scenario Profile Test Matrix so pressure profiles have expected outputs. | Matrix is documentation, not runtime policy. |
| P105 | Hardened boundary monitor with structured disabled capabilities and active violation list. | Monitor is audit output, not enforcement. |
| P106 | Specialized candidate previews by pressure, including intent, selection reason, blocked promotion, and manual review target. | Candidate remains preview-only. |
| P107 | Specialized review queue previews with queue intent, gate reason, blocked lifecycle, and manual-review-only action. | Review routing is not lifecycle. |
| P108 | Re-ran usability review across eight input types and measured improvement. | Review is evidence, not authorization. |
| P109 | Added roadmap for what the harness can see and cannot see. | Roadmap is not implementation approval. |
| P110 | Closed the overnight cycle with commits, tests, boundary audit, and stop condition. | Summary is not P111/P112 execution. |

## 3. Did P108 Readability Improve?

Yes.

P101 founder-facing readability: **6.5 / 10**.

P108 founder-facing readability: **8.0 / 10**.

The improvement is credible because it maps directly to the original P101
complaints:

- inputs no longer share one generic candidate table;
- pressure type and matched signals appear at the top;
- candidates explain why they were selected and why they cannot be promoted;
- review gates explain why no lifecycle is created;
- boundary monitor highlights the most relevant blocked capabilities;
- each profile gives a concrete manual next step and do-not-do list.

The score is not higher because the harness still does not inspect real state.

## 4. Which Pressure Types Work Best?

Strongest pressure types:

- `adapter_boundary_pressure`: clear founder value because AstrBot/platform
  pressure is immediately routed to adapter boundary review, with integration
  blocked.
- `capability_evolution_pressure`: clearly encodes the key P92 principle:
  verification is not authorization.
- `growth_review_pressure`: correctly makes growth review primary while keeping
  identity mutation and growth execution blocked.
- `product_layer_pressure`: clearly prevents "project unclear, so build UI" as
  an accidental jump.
- `reconstruction_pressure`: useful because payload/diff, replay, reducers, and
  compaction are easy to confuse; the report separates them.

## 5. Which Pressure Types Still Feel Like Templates?

Still more templated:

- `observability_pressure`: it correctly routes confusion to observatory
  readability, but it does not yet answer the founder's confusion with a compact
  "what this project has built" summary.
- `temporal_pressure`: the boundaries are right, but the concepts still lean on
  RFC terms such as elapsed time, recall write, temporal event, and delayed
  interpretation.
- `unknown_pressure`: safely conservative, but it can feel unhelpful for normal
  note-like inputs because writing remains blocked.

These are acceptable for a dry-run harness, but they show where a read-only
state-backed view could help.

## 6. Is `candidate_preview` More Specific?

Yes.

P101 candidate preview was safe but generic. P106 made candidates pressure
specific:

- adapter input now shows adapter boundary, task update, and governance boundary
  candidates;
- growth input now shows growth review, meaning shift, and identity high gate;
- tool-library input now shows capability growth, tool authorization, and
  cautionary procedural memory;
- temporal input now shows temporal review, recall-write, and delayed
  interpretation;
- reconstruction input now shows reconstruction evidence, payload/diff gap, and
  replay check.

Each row now states:

- candidate intent;
- why it was selected;
- why it cannot be promoted;
- which manual review gate would be required later;
- `preview_only`, `promoted: false`, and `persisted: false`.

This solves the "same static candidate table" problem.

## 7. Is `review_queue_preview` Clearer?

Yes.

P107 made review gates explain:

- queue intent;
- why the candidate routes to that gate;
- why lifecycle creation is blocked;
- manual review is required;
- the next allowed action is `manual_review_only`;
- lifecycle creation and execution remain false.

This addresses the P101 concern that the review queue was safe but too thin. It
now communicates "this is where a human would look later" instead of implying a
live workflow.

## 8. Is `boundary_monitor` Visible Enough?

Mostly yes.

P105 made the monitor the strongest part of the harness:

- forbidden capabilities are structured as disabled rows;
- unchanged state is explicit;
- active boundary violations are listed and empty;
- all forbidden actions are reported disabled;
- each pressure type highlights the boundaries most relevant to the current
  input.

Remaining issue: in Markdown, the boundary monitor can be long and visually
dense. A future report format could add a compact "top blocked actions" section
above the full table, but this should stay display-only.

## 9. Does `observatory_snapshot` Help Founder Decisions?

Partly.

It helps because it now reflects the selected pressure type and top risks. That
is enough to stop premature moves such as "connect AstrBot now" or "start UI
now".

It is still not enough to answer deeper founder questions because it does not
read actual state, events, memory summaries, task status, or current artifact
coverage. It is a pressure-aligned status hint, not a state-backed project
diagnosis.

## 10. Is It Suitable To Enter State-Backed Read-Only Harness?

Yes, with a narrow definition.

The project is suitable to enter a **State-Backed Read-Only Harness planning or
minimal read-only phase**, but not a runtime, product, adapter, or memory-writing
phase.

The reason is simple: P102-P110 solved the static routing problem. The next
weakness is no longer "the harness cannot distinguish inputs"; it is "the
harness cannot show whether any existing state evidence actually supports the
preview."

That weakness is exactly the next safe frontier, as long as "state-backed" means
read-only inspection and report output only.

## 11. If Suitable, What Should P112 Do?

Recommended P112: **State-Backed Read-Only Harness Plan** or a very small
approved read-only implementation, depending on founder preference.

The safest P112 scope:

- define which existing local state/report files may be read;
- define a read-only state snapshot envelope;
- add `state_refs_preview`, not real retrieval;
- show selected refs, omitted refs, and missing evidence;
- prove no state directory files change before/after the command;
- keep all candidates preview-only;
- keep all review gates manual-review-only;
- keep all forbidden boundary flags disabled/false;
- do not call models, tools, adapters, network, AstrBot, UI, or product code.

P112 should not implement memory search as continuity, claim mutation, task
writes, recall writes, temporal runtime, reducer execution, or policy execution.

## 12. If Not Suitable, What Would Need More Work?

If the founder decides P112 is still too early, the useful review-only work would
be:

- make Chinese display labels less crowded by English internal keys;
- add a compact top-level "what this input means" summary;
- improve temporal and unknown pressure wording;
- split risk explanations into more situation-specific text;
- define a state-backed read-only contract before any code;
- review whether existing state files are safe to read in a dry-run report.

These are refinements, not blockers. The main P101 problem has been solved well
enough to consider the next read-only frontier.

## Founder Judgment

P102-P110 did not make the harness intelligent. It made the harness legible.

That is the right kind of progress for this stage. The project should now avoid
adding more abstract layers and instead decide whether to let the harness read a
small, explicit, local, read-only snapshot of existing state.

## Boundary Statement

P111 is review-only. It does not authorize runtime work, product work, adapter
integration, Companion behavior, model calls, real retrieval, event writes,
memory writes, recall writes, identity mutation, growth execution, temporal
runtime, tool execution, policy execution, reconstruction reducer execution,
event compaction, automatic tool promotion, or automatic roadmap execution.
