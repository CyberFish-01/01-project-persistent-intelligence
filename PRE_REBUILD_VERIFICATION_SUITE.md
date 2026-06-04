# Pre-Rebuild Verification Suite

Chinese version: [PRE_REBUILD_VERIFICATION_SUITE_ZH.md](./PRE_REBUILD_VERIFICATION_SUITE_ZH.md)

Status: `P151`, `implementation`, `read-only`, `pre-rebuild-verification`.

P151 adds a local read-only verification suite command:

```bash
python3 -m one_core.cli pre-rebuild-verification
```

It generates a report about whether the repository is ready for the final
verification report phase. It does not start rebuild, connect old 01, connect
AstrBot, call a model, execute tools, write state, write memory, write recall
events, mutate identity, execute temporal runtime, execute reconstruction
reducers, compact events, or approve the next phase automatically.

## Why It Exists

P150 defined the full verification plan before rebuild, but the plan still
needed a deterministic local report surface. P151 turns that plan into a
read-only suite so P152 can report evidence instead of relying on hand-written
claims.

The suite answers:

- are required P112-P151 artifacts present in English and Chinese;
- do PHASE_INDEX, RFC_INDEX, and README point to the current phase;
- do local Markdown links resolve;
- are active forbidden true flags absent;
- do existing read-only report builders still produce safe outputs;
- do CTM-inspired and Tool-First lines remain symbolic, candidate/evidence, and
  review-only;
- is rebuild still explicitly not started.

## CLI

```bash
python3 -m one_core.cli pre-rebuild-verification
python3 -m one_core.cli pre-rebuild-verification --format json
python3 -m one_core.cli pre-rebuild-verification --lang zh
python3 -m one_core.cli pre-rebuild-verification --format markdown --output /tmp/pre_rebuild_verification.md
```

Options:

| Option | Values | Meaning |
|---|---|---|
| `--format` | `markdown`, `json` | Output shape; default is `markdown`. |
| `--lang` | `en`, `zh` | Report language; default is `en`. |
| `--output` | path | Optional explicit report file. |

The command writes only when `--output` is provided, and that write is the
requested report artifact only. It does not create or modify the state
directory.

## Report Sections

The report contains:

- `verification_summary`
- `gate_results`
- `required_artifacts`
- `future_artifacts`
- `phase_index_status`
- `index_status`
- `readme_status`
- `forbidden_pattern_status`
- `markdown_link_status`
- `read_only_cli_status`
- `boundary_status`
- `ctm_temporal_status`
- `tool_first_status`
- `verification_commands_for_p152`
- `non_execution_invariants`

## What It Checks Internally

P151 performs only deterministic local checks:

- artifact presence;
- Markdown local link resolution;
- forbidden active-pattern search;
- PHASE_INDEX, RFC_INDEX, and README current-phase coverage;
- in-process generation of existing read-only reports:
  - `foundation-observatory-report`;
  - `harness-source-inventory`;
  - `harness-dry-run` for reconstruction pressure.

It does not internally shell out to Git, run the full unit test suite, or run
format checks. Those remain explicit P152 verification commands so their output
can be reported directly.

## Non-Execution Invariants

The suite output explicitly records:

- `pre_rebuild_verification_report_only`
- `execution_prohibited`
- `state_unchanged`
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

Fields with dangerous meanings remain disabled in the generated report.

## Relationship To P152

P151 creates the suite.

P152 should run the suite, run the required shell checks from P150, and write
`VERIFICATION_REPORT.md` / `VERIFICATION_REPORT_ZH.md`.

P151 does not decide that rebuild may begin.

## Stop Boundary

After P151, the safe next phase is P152 Verification Report. Rebuild remains
blocked until the founder receives and approves the final pre-rebuild
checkpoint.
