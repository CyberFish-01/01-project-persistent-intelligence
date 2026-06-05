# Lineage and Branch Governance RFC

Chinese version: [LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md](./LINEAGE_BRANCH_GOVERNANCE_RFC_ZH.md)

Status: `P155`, `governance-only`, `planning`, `non-runtime`, `no-tag-created`, `no-branch-created`.

P155 defines lineage, branch, tag, and checkpoint governance before any future
local 01 rebuild. It does not create a git tag, create a git branch, push,
start rebuild, read old 01, import external material, write state, write
events, write memory, mutate Identity Core, execute tools, call a model, or
connect adapters.

## 1. Why Lineage Governance

Lineage governance exists because the first 01 Core must remain permanently
traceable.

The project now has enough foundation, harness, lockdown, context-package,
response-boundary, and pre-rebuild verification work that future local rebuilds
and 01 instances can become attractive. That is useful, but dangerous without a
lineage boundary.

Required observations:

- the initial 01 Core must remain permanently recoverable;
- every 01 instance must have a declared source;
- looking more like 01 does not mean being closer to Core;
- an instance may grow boldly, but it must not directly modify Core;
- synthetic history, AstrBot context, adapter payloads, and LLM self-claims must
  stay isolatable;
- branches exist for recovery, comparison, abandonment, quarantine, review, and
  selected return.

Without this layer, a future sandbox instance could produce a compelling style,
memory claim, self-description, or tool candidate and make it feel native to
Core. P155 prevents that confusion.

## 2. Core Principle

```text
Instance may grow; Core must remain sovereign.
实例可以生长，内核不可僭越。
```

This principle means:

- Core owns the long-lived continuity boundary.
- Instances may explore behavior, style, hypotheses, simulated experience, and
  tool candidates.
- Instance output is evidence or candidate material, not Core history.
- Core accepts only reviewed, selected, minimal returns.
- A branch name, tag name, report, or model output never authorizes mutation.

## 3. Branch Types

| Branch Type | Purpose | Allowed Use | Forbidden Use |
|---|---|---|---|
| `core trunk` | The protected main continuity line. | Holds reviewed Core history and stable project state. | Direct instance merge, quarantine merge, unreviewed model output, adapter-owned context. |
| `core baseline` | A recoverable known-good Core reference. | Anchor rollback, comparison, and rebuild planning. | Treating baseline as mutable experiment space. |
| `foundation milestone` | A named point for a major foundation stage. | Reference P-level documents and read-only capabilities. | Claiming milestone means product readiness. |
| `pre-rebuild checkpoint` | A pre-rebuild safety gate. | Mark evidence that rebuild can be considered after founder approval. | Starting rebuild or migration automatically. |
| `instance sandbox branch` | A contained 01 instance exploration line. | Explore style, assumptions, simulation, candidates, local behavior. | Writing Core identity, memory, event, or tool trust directly. |
| `research experiment branch` | A contained research line. | Explore CTM vocabulary, Tool-First ideas, synthetic-history accelerators, evaluation plans. | Merging unreviewed outputs into Core trunk. |
| `quarantine branch` | A containment area for suspicious or untrusted material. | Hold imported memory, LLM self-claims, adapter context, prompt contamination, synthetic autobiography. | Merge into Core trunk. |
| `release / verification branch` | A temporary verification surface. | Validate a candidate state before human decision. | Becoming an alternate Core trunk without review. |

## 4. Naming Rules

The names below are examples and recommendations. P155 does not create them.

Core names:

```text
core/baseline
```

Instance sandbox names:

```text
instance/01-local-rebuild-trial
instance/01-astrbot-shadow
instance/01-synthetic-history-v1
```

Research names:

```text
research/ctm-temporal-dynamics
research/tool-first-evolution
research/synthetic-history-accelerator
```

Quarantine names:

```text
quarantine/imported-astrbot-memory
quarantine/llm-self-claims
```

Milestone names:

```text
milestone-p100-harness-dry-run
milestone-p154-pre-rebuild-ready
core-v1-pre-rebuild-ready
```

Naming constraints:

- use lowercase where possible;
- include the purpose, not a personality label;
- use `instance/` for sandbox subjects;
- use `research/` for concept experiments;
- use `quarantine/` for untrusted or contaminated material;
- do not name a branch as if it were the new Core unless the founder has
  explicitly approved that role.

## 5. Tagging Rules

P155 recommends tag semantics but does not create tags.

| Suggested Tag | Meaning | Suggested Commit Selection Rule |
|---|---|---|
| `core-v0-baseline` | Earliest stable local 01 Core baseline. | Choose the last commit that represents the minimal local Core before later governance expansion, if the founder wants that historical anchor. |
| `core-v0-foundation-baseline` | Foundation documents and prototype references are coherent enough to serve as a research baseline. | Choose a commit after foundation consolidation artifacts are present and tests pass. Do not guess a commit without reviewing the phase index and verification state. |
| `core-v0-observable-baseline` | Read-only observatory and harness visibility exist. | Choose a commit after the observatory and no-write harness dry-run are implemented and reviewed. |
| `core-v1-pre-rebuild-ready` | Pre-rebuild evidence is complete enough to ask whether local rebuild may begin. | Choose the P154 push-readiness commit or a later founder-approved checkpoint commit only after verification and branch governance are accepted. |
| `milestone-p100-harness-dry-run` | The first no-write harness dry-run exists. | Choose the commit that introduced the minimal CLI harness dry-run. |
| `milestone-p110-scenario-routing` | The P102-P110 harness routing and review cycle is closed. | Choose the commit that closed overnight harness work summary after routing, specialization, and usability review. |
| `milestone-p154-pre-rebuild-ready` | Pre-rebuild completion and push readiness are recorded. | Choose the P154 audit commit if the founder wants a pre-rebuild-ready reference. |

If the exact commit is not obvious, do not guess. Use this selection process:

1. inspect `PHASE_INDEX.md`;
2. inspect `git log --oneline`;
3. inspect the relevant completion or review document;
4. run tests and forbidden search;
5. record candidate commits in a future tag-advisor report;
6. create the tag only in a separately approved operation.

## 6. Merge / Return Rules

Branch return must be explicit and conservative.

Forbidden direct merges:

- instance branch -> core trunk;
- research branch -> core trunk;
- quarantine branch -> core trunk;
- adapter branch -> core trunk;
- synthetic-history branch -> core trunk;
- tool-candidate branch -> core trunk.

Allowed return path:

```text
candidate -> quarantine -> review -> manual selected return
```

Allowed return materials:

- RFC;
- tests;
- reports;
- safe schema;
- reviewed procedural insight;
- reviewed boundary improvement;
- minimal founder decision note;
- minimal review note.

Forbidden return materials:

- identity mutation;
- automatic memory write;
- unverified model memory claims;
- adapter context artifact;
- synthetic autobiographical memory;
- tool trust update without review;
- prompt contamination residue;
- imported memory treated as native history;
- instance style treated as Core identity.

Manual selected return means a human review identifies a small, bounded,
source-attributed change that can return to Core without importing the branch's
identity, memory, or trust assumptions.

## 7. Instance Sandbox Rule

An instance sandbox is a contained exploration line for possible 01 variants.

Allowed inside an instance sandbox:

- style exploration;
- expression experiments;
- self-hypotheses;
- simulated experiences;
- synthetic history experiments;
- tool candidates;
- procedure candidates;
- local behavior experiments;
- evaluation notes.

Required boundaries:

- instance outputs enter only candidate, quarantine, or review surfaces;
- instance output does not write Core;
- instance memory is not Core memory;
- instance identity is not Core identity;
- instance tool success is not Core tool authorization;
- Core has final review authority.

The strongest-looking instance is still only an instance. It may provide
evidence, but it does not own the lineage.

## 8. Recovery Rules

Recovery rules define what future operators should do when a branch becomes
unclear, contaminated, or unsafe.

### Return To Baseline

To return to baseline:

1. identify the approved baseline tag or commit;
2. verify it points to the intended Core state;
3. inspect verification and checkpoint documents;
4. start any future recovery only through an explicit founder-approved action;
5. do not overwrite Core trunk history casually.

### Abandon A Contaminated Branch

A contaminated branch should be abandoned when:

- it contains unverified identity claims;
- it contains untrusted synthetic autobiography;
- it mixes adapter context with Core identity;
- it treats model output as native memory;
- it promotes tool trust without review;
- it cannot explain its source lineage.

Abandonment should be recorded in a future report, not silently hidden.

### Compare Two Instance Branches

Comparison should inspect:

- declared source;
- changed files;
- identity claims;
- memory claims;
- tool candidates;
- review artifacts;
- quarantine material;
- tests and reports;
- divergence from baseline;
- forbidden return material.

Comparison does not decide which instance is "more real." It only shows
lineage, evidence, and risk.

### Record Branch Lineage

A future lineage record should include:

- branch name;
- source commit;
- parent branch;
- purpose;
- allowed scope;
- forbidden scope;
- source material;
- review status;
- quarantine status;
- selected return decisions;
- abandonment decision if any.

### Future Lineage Report

A future `lineage-report` may summarize branch ancestry, checkpoints, risk
status, and selected returns. It must remain report-only unless a later
founder-approved phase defines otherwise.

## 9. Relationship To Existing Roadmap

P155 connects to existing artifacts without changing their execution status:

- Core Lockdown: lineage governance extends lockdown from content handling to
  branch handling.
- Import Quarantine: untrusted imports may live in quarantine branches, not Core
  trunk.
- Shadow Adapter: adapter-shaped material may be observed in shadow branches,
  not merged as Core memory or identity.
- Synthetic History Accelerator: synthetic history, if explored later, belongs
  in instance or research branches and returns only as reviewed theory, tests,
  or quarantine evidence.
- CTM Temporal Dynamics: CTM-inspired temporal work belongs in research branches
  and symbolic review artifacts, not CTM runtime.
- Tool-First Self-Evolution: tool candidates and capability evidence belong in
  research or instance branches until reviewed; verification is not
  authorization.
- Rebuild Migration Protocol: migration needs explicit baseline, checkpoint,
  and founder approval before any local rebuild begins.

## 10. Future CLI Ideas

Candidate future commands only; P155 does not implement them:

- `lineage-report`;
- `branch-checkpoint-plan`;
- `instance-diff`;
- `quarantine-return-preview`;
- `baseline-tag-advisor`.

Future CLI boundaries:

- read-only by default;
- no tag creation unless separately approved;
- no branch creation unless separately approved;
- no push;
- no rebuild start;
- no automatic merge;
- no automatic selected return;
- no model call;
- no adapter connection;
- no state, memory, identity, event, recall, growth, tool, temporal, or CTM
  runtime mutation.

## P156 Candidate Directions

P155 does not enter P156. Candidate directions, only if the founder explicitly
approves later:

- Lineage Report Plan;
- Baseline Tag Advisor Plan;
- Instance Sandbox Contract;
- Quarantine Return Preview RFC;
- Local Rebuild Start Decision Record.

## Non-Execution Statement

P155 does not:

- create a git tag;
- create a git branch;
- push to a remote;
- start rebuild;
- read old 01;
- import AstrBot memory;
- connect adapters;
- call a model;
- write formal state;
- write events;
- write memory;
- write recall events;
- mutate Identity Core;
- rewrite memory;
- execute growth;
- execute tools;
- enable temporal runtime;
- enable CTM runtime;
- execute a policy;
- create an automatic roadmap.
