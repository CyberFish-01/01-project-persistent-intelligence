# Founder Console User Flow

Chinese version: [FOUNDER_CONSOLE_USER_FLOW_ZH.md](./FOUNDER_CONSOLE_USER_FLOW_ZH.md)

Status: `P132`, `document-only`, `user-flow`, `non-runtime`.

P132 defines the founder-facing flow for a future Thin Founder Console. It does
not implement a console, CLI command, Web UI, Companion layer, adapter
integration, model call, tool execution, state write, memory write, recall
write, identity mutation, policy executor, or rebuild.

## Flow Goal

The founder should be able to answer one question:

```text
What is the safest next thing to inspect, without accidentally causing the
system to act?
```

The console flow therefore moves from visibility to preview to manual decision.
It never moves from warning to automatic action.

## Primary Flow

| Step | Founder Sees | Founder Can Do | System Must Not Do |
|---|---|---|---|
| 1. Open local status | Current phase, readiness, blocked boundaries. | Read project state summary. | Start runtime or rebuild. |
| 2. Inspect observatory snapshot | Foundation axes, risks, next candidates. | Compare possible directions. | Choose roadmap automatically. |
| 3. Inspect source inventory | Approved Markdown sources and mappings. | See what can be cited. | Read old 01 or external files. |
| 4. Run dry-run preview | How one input would route. | Test an idea as preview. | Write events, memory, recall, identity, or tasks. |
| 5. Inspect boundary monitor | Blocked capabilities and relevant risks. | Confirm what remains disabled. | Execute tools, adapters, models, or policy. |
| 6. Inspect review queue preview | Candidate review gates. | Decide what deserves human review later. | Create lifecycle or promotion. |
| 7. Choose next candidate | Document-only next directions. | Approve or defer a planning phase. | Auto-create next phase or run it. |

## Secondary Flows

### Observability Confusion

Founder asks: "What has this project done?"

Safe flow:

1. show observatory snapshot;
2. show current phase index reference;
3. show highest risks;
4. suggest founder/CTO review as candidate.

Forbidden shortcut: build UI or product layer to make the project feel clearer.

### Adapter Pressure

Founder asks: "Can we connect AstrBot?"

Safe flow:

1. show shadow adapter boundary;
2. show adapter-shaped examples;
3. show quarantine gates;
4. keep integration blocked.

Forbidden shortcut: connect AstrBot, ingest events, or let the platform own
identity.

### Growth Pressure

Founder asks: "Is this growth?"

Safe flow:

1. show growth candidate review boundary;
2. show meaning-shift and identity gate references;
3. show candidate-only route;
4. require manual review.

Forbidden shortcut: promote growth or mutate identity.

### Temporal Pressure

Founder asks: "Does time passing change this?"

Safe flow:

1. show temporal awareness RFC reference;
2. show temporal coherence evaluation plan;
3. show review depth suggestion;
4. keep temporal cues symbolic.

Forbidden shortcut: write temporal events, recall events, salience changes, or
thought traces.

### Capability Pressure

Founder asks: "The tool worked; can it enter the tool library?"

Safe flow:

1. show Tool-First boundary;
2. show capability evidence candidate;
3. show authorization gate;
4. keep promotion blocked.

Forbidden shortcut: execute or promote tools automatically.

## Founder-Facing Labels

Future display should prefer simple labels:

| Internal Key | Founder Label |
|---|---|
| `observatory_snapshot` | current status |
| `source_inventory` | readable sources |
| `harness_dry_run` | input path preview |
| `boundary_monitor` | blocked actions |
| `review_queue_preview` | human review paths |
| `next_step_candidates` | possible next plans |

## No-Write Flow Invariants

Every flow must show:

- `founder_console_report_only: true`
- `execution_prohibited: true`
- `state_unchanged: true`
- `candidate_is_not_promotion: true`
- `review_is_not_lifecycle: true`
- `adapter_integration_blocked: true`
- `model_call_blocked: true`
- `rebuild_blocked: true`

These are display invariants, not runtime implementation in P132.

## Completion Statement

P132 gives the future founder console a clear user flow: see, preview, review,
decide. It preserves the project rule that founder visibility must not become
automatic action.
