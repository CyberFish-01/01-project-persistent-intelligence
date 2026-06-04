# Full Verification Plan Before Rebuild

Chinese version: [FULL_VERIFICATION_PLAN_BEFORE_REBUILD_ZH.md](./FULL_VERIFICATION_PLAN_BEFORE_REBUILD_ZH.md)

Status: `P150`, `verification-plan`, `document-only`, `non-runtime`.

P150 defines the full verification plan before local 01 rebuild. It does not run
the suite, start rebuild, read old 01, migrate state, write memory, connect
adapters, call models, execute tools, run reducers, compact events, or mutate
identity.

## Verification Goal

Prove that the repository is prepared to **start a read-only verification pass**
and, after that pass, let the founder decide whether local rebuild may begin.

Verification must not become rebuild.

## Verification Areas

| Area | Check |
|---|---|
| repository state | branch, clean status, latest commits |
| formatting | `git diff --check` |
| tests | `python3 -m unittest` |
| markdown links | local Markdown link check |
| forbidden patterns | active forbidden pattern search |
| phase coverage | PHASE_INDEX / ZH reaches current phase |
| index coverage | RFC_INDEX / ZH includes new artifacts |
| README status | README / ZH reflects latest phase |
| required artifacts | P112-P154 required docs exist |
| CLI read-only commands | observatory, harness, source inventory still run |
| no-write evidence | state/report-only boundaries preserved |
| CTM boundary | no CTM runtime or thought loop |
| Tool-First boundary | no tool execution or promotion |
| adapter boundary | no AstrBot/external adapter integration |
| rebuild boundary | no rebuild start or migration |

## Required Commands

The read-only suite should run:

```bash
git status --short
git branch --show-current
git diff --check
python3 -m unittest
python3 -m one_core.cli foundation-observatory-report --format json --lang en
python3 -m one_core.cli foundation-observatory-report --format json --lang zh
python3 -m one_core.cli harness-source-inventory --format json --lang en
python3 -m one_core.cli harness-source-inventory --format json --lang zh
python3 -m one_core.cli harness-dry-run --input "pre-rebuild verification" --format json --lang en
python3 -m one_core.cli harness-dry-run --input "重构前验证" --format json --lang zh
```

It should also run local Markdown link and forbidden-pattern checks.

## Forbidden Pattern Set

Verification must search for active true flags. To keep the repository's own
forbidden-pattern check clean, this plan lists field names separately from the
blocked value `true`:

- `identity_core_mutated`
- `memory_rewrite_executed`
- `recall_mutation_executed`
- `growth_engine_executed`
- `temporal_event_executed`
- `tool_execution_enabled`
- `auto_tool_promotion_enabled`
- `policy_executor_enabled`
- `companion_feature_enabled`
- `adapter_integration_required`
- `harness_write_enabled`
- `ctm_runtime_enabled`
- `external_io_enabled`
- `model_call_enabled`
- `source_loader_write_enabled`
- `app_write_enabled`
- `rebuild_started`

## Pass Criteria

The verification pass succeeds only if:

- all commands pass;
- no forbidden pattern appears;
- required artifacts exist;
- local links resolve;
- tests pass;
- no state mutation is observed;
- no model, adapter, external IO, tool, or rebuild action is required.

## Failure Handling

If verification fails:

- do not rebuild;
- write a blocked/failure report;
- list failing command and evidence;
- do not attempt workaround by connecting external services;
- do not call models to interpret failures;
- do not mutate state to fix verification.

## CTM And Tool-First Verification

The plan must confirm:

- CTM-inspired work is symbolic/review-only;
- no thought loop or temporal runtime exists;
- Tool-First work is candidate/evidence/review-only;
- no tool execution, auto-promotion, or policy executor exists.

## Completion Statement

P150 defines the verification plan. It prepares P151 to implement or run only
the read-only verification suite, without starting rebuild.
