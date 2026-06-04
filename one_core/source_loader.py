from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]

LANGUAGES = ("en", "zh")
OUTPUT_FORMATS = ("markdown", "json")

NON_EXECUTION_INVARIANTS = {
    "read_only_source_backing": True,
    "state_unchanged": True,
    "execution_prohibited": True,
    "identity_core_mutated": False,
    "memory_rewrite_executed": False,
    "recall_mutation_executed": False,
    "growth_engine_executed": False,
    "temporal_event_executed": False,
    "tool_execution_enabled": False,
    "auto_tool_promotion_enabled": False,
    "policy_executor_enabled": False,
    "companion_feature_enabled": False,
    "adapter_integration_required": False,
    "harness_write_enabled": False,
    "external_io_enabled": False,
    "model_call_enabled": False,
    "source_loader_write_enabled": False,
    "rebuild_started": False,
}


@dataclass(frozen=True)
class SourceSpec:
    source_id: str
    en_path: str
    zh_path: str
    source_class: str
    pressure_types: tuple[str, ...]
    research_line: str
    why_allowed: str


SOURCE_WHITELIST: tuple[SourceSpec, ...] = (
    SourceSpec("phase_index", "PHASE_INDEX.md", "PHASE_INDEX_ZH.md", "foundation_status", ("all",), "both", "Phase map for current status and provenance."),
    SourceSpec("foundation", "FOUNDATION.md", "FOUNDATION_ZH.md", "foundation_status", ("all",), "both", "Stable project invariants and stage order."),
    SourceSpec("foundation_status", "FOUNDATION_STATUS.md", "FOUNDATION_STATUS_ZH.md", "foundation_status", ("observability_pressure", "product_layer_pressure"), "both", "What exists, what is missing, and what is pushed back."),
    SourceSpec("concept_map", "CONCEPT_MAP.md", "CONCEPT_MAP_ZH.md", "foundation_status", ("all",), "both", "Cross-layer concept relationships."),
    SourceSpec("architecture_boundaries", "ARCHITECTURE_BOUNDARIES.md", "ARCHITECTURE_BOUNDARIES_ZH.md", "governance_boundary", ("growth_review_pressure", "temporal_pressure", "reconstruction_pressure", "product_layer_pressure", "adapter_boundary_pressure"), "both", "Boundary ownership across identity, memory, growth, temporal, reconstruction, governance, and product layers."),
    SourceSpec("glossary", "GLOSSARY.md", "GLOSSARY_ZH.md", "foundation_status", ("all",), "both", "Shared vocabulary and anti-misreading boundaries."),
    SourceSpec("open_questions", "OPEN_QUESTIONS.md", "OPEN_QUESTIONS_ZH.md", "governance_boundary", ("all",), "both", "Active unresolved questions and deferred risks."),
    SourceSpec("risk_register", "RISK_REGISTER.md", "RISK_REGISTER_ZH.md", "governance_boundary", ("all",), "both", "Current risk signals and mitigations."),
    SourceSpec("rfc_index", "RFC_INDEX.md", "RFC_INDEX_ZH.md", "governance_boundary", ("all",), "both", "Navigation for RFC-only artifacts and their non-execution status."),
    SourceSpec("boundary_test_matrix", "BOUNDARY_TEST_MATRIX.md", "BOUNDARY_TEST_MATRIX_ZH.md", "governance_boundary", ("all",), "both", "Boundary expectations for allowed and forbidden outputs."),
    SourceSpec("visual_naming", "VISUAL_NAMING_GUIDE.md", "VISUAL_NAMING_GUIDE_ZH.md", "founder_readability", ("observability_pressure", "product_layer_pressure"), "both", "Founder-facing display names without UI implementation."),
    SourceSpec("observatory_report", "FOUNDATION_OBSERVATORY_REPORT.md", "FOUNDATION_OBSERVATORY_REPORT_ZH.md", "founder_readability", ("observability_pressure",), "both", "Static founder-facing status snapshot."),
    SourceSpec("minimal_cli_harness_plan", "MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN.md", "MINIMAL_CLI_HARNESS_IMPLEMENTATION_PLAN_ZH.md", "harness_boundary", ("all",), "both", "Original no-write dry-run scope."),
    SourceSpec("thin_interaction_harness", "THIN_INTERACTION_HARNESS_RFC.md", "THIN_INTERACTION_HARNESS_RFC_ZH.md", "harness_boundary", ("all",), "both", "Harness preview-only boundary before implementation."),
    SourceSpec("conversation_intake", "CONVERSATION_INTAKE_CONTRACT_RFC.md", "CONVERSATION_INTAKE_CONTRACT_RFC_ZH.md", "harness_boundary", ("all",), "both", "Intake envelope vocabulary without adapter ingest or event writes."),
    SourceSpec("context_preview", "CONTEXT_PACKAGE_PREVIEW_RFC.md", "CONTEXT_PACKAGE_PREVIEW_RFC_ZH.md", "harness_boundary", ("all",), "both", "Context preview vocabulary without retrieval execution."),
    SourceSpec("review_queue_preview", "REVIEW_QUEUE_PREVIEW_RFC.md", "REVIEW_QUEUE_PREVIEW_RFC_ZH.md", "harness_boundary", ("all",), "both", "Review queue preview vocabulary without lifecycle execution."),
    SourceSpec("scenario_profile_matrix", "SCENARIO_PROFILE_TEST_MATRIX.md", "SCENARIO_PROFILE_TEST_MATRIX_ZH.md", "harness_boundary", ("all",), "both", "Expected pressure profiles, candidates, boundaries, and next steps."),
    SourceSpec("harness_usability_p101", "HARNESS_USABILITY_REVIEW.md", "HARNESS_USABILITY_REVIEW_ZH.md", "founder_readability", ("all",), "both", "Baseline 6.5/10 usability problems."),
    SourceSpec("harness_usability_p108", "HARNESS_USABILITY_REVIEW_P108.md", "HARNESS_USABILITY_REVIEW_P108_ZH.md", "founder_readability", ("all",), "both", "Re-review showing 8.0/10 and remaining static source gap."),
    SourceSpec("harness_roadmap", "HARNESS_ROADMAP.md", "HARNESS_ROADMAP_ZH.md", "harness_boundary", ("all",), "both", "What harness can see and cannot see after P109."),
    SourceSpec("post_harness_founder_review", "POST_HARNESS_FOUNDER_REVIEW.md", "POST_HARNESS_FOUNDER_REVIEW_ZH.md", "founder_readability", ("all",), "both", "P111 decision that narrow state-backed read-only is appropriate."),
    SourceSpec("state_backed_read_only_harness", "STATE_BACKED_READ_ONLY_HARNESS_RFC.md", "STATE_BACKED_READ_ONLY_HARNESS_RFC_ZH.md", "harness_boundary", ("all",), "both", "P112 boundary for whitelisted local source citation."),
    SourceSpec("temporal_awareness", "TEMPORAL_AWARENESS_RFC.md", "TEMPORAL_AWARENESS_RFC_ZH.md", "temporal_ctm_boundary", ("temporal_pressure",), "CTM-inspired Temporal Dynamics", "Elapsed time as future review vocabulary, not runtime."),
    SourceSpec("ctm_temporal_dynamics", "CTM_TEMPORAL_DYNAMICS_RFC.md", "CTM_TEMPORAL_DYNAMICS_RFC_ZH.md", "temporal_ctm_boundary", ("temporal_pressure",), "CTM-inspired Temporal Dynamics", "Symbolic CTM-inspired mapping without neural CTM or training."),
    SourceSpec("temporal_coherence_eval", "TEMPORAL_COHERENCE_EVALUATION_PLAN.md", "TEMPORAL_COHERENCE_EVALUATION_PLAN_ZH.md", "temporal_ctm_boundary", ("temporal_pressure",), "CTM-inspired Temporal Dynamics", "Deterministic evaluation plan without temporal runtime."),
    SourceSpec("deliberation_tick", "DELIBERATION_TICK_REVIEW_DEPTH_RFC.md", "DELIBERATION_TICK_REVIEW_DEPTH_RFC_ZH.md", "temporal_ctm_boundary", ("temporal_pressure", "growth_review_pressure", "capability_evolution_pressure"), "CTM-inspired Temporal Dynamics", "Review depth and tick vocabulary without thought loops."),
    SourceSpec("thought_trace_storage", "THOUGHT_TRACE_STORAGE_POLICY_RFC.md", "THOUGHT_TRACE_STORAGE_POLICY_RFC_ZH.md", "temporal_ctm_boundary", ("temporal_pressure",), "CTM-inspired Temporal Dynamics", "Trace storage boundary without hidden chain-of-thought capture."),
    SourceSpec("session_resume", "SESSION_RESUME_SCENARIO_PLAN.md", "SESSION_RESUME_SCENARIO_PLAN_ZH.md", "temporal_ctm_boundary", ("temporal_pressure",), "CTM-inspired Temporal Dynamics", "Resume scenarios without temporal event writes."),
    SourceSpec("tool_first_self_evolution", "TOOL_FIRST_SELF_EVOLUTION_RFC.md", "TOOL_FIRST_SELF_EVOLUTION_RFC_ZH.md", "capability_boundary", ("capability_evolution_pressure",), "Tool-First In-Situ Self-Evolution", "Tool-first capability vocabulary without tool execution."),
    SourceSpec("capability_evolution_boundary", "CAPABILITY_EVOLUTION_BOUNDARY_RFC.md", "CAPABILITY_EVOLUTION_BOUNDARY_RFC_ZH.md", "capability_boundary", ("capability_evolution_pressure",), "Tool-First In-Situ Self-Evolution", "Verification is not authorization; tool candidate is not promotion."),
    SourceSpec("stateful_memory_policy", "STATEFUL_MEMORY_ENCODING_POLICY.md", "STATEFUL_MEMORY_ENCODING_POLICY_ZH.md", "governance_boundary", ("growth_review_pressure", "temporal_pressure"), "both", "Minimal encoding policy before meaning-shift review."),
    SourceSpec("growth_candidate_lifecycle", "GROWTH_CANDIDATE_LIFECYCLE_RFC.md", "GROWTH_CANDIDATE_LIFECYCLE_RFC_ZH.md", "governance_boundary", ("growth_review_pressure",), "both", "Review-object lifecycle vocabulary without growth execution."),
    SourceSpec("productive_drift", "PRODUCTIVE_DRIFT_VS_COLLAPSE.md", "PRODUCTIVE_DRIFT_VS_COLLAPSE_ZH.md", "governance_boundary", ("growth_review_pressure",), "both", "Drift vocabulary without automatic drift classification."),
    SourceSpec("reconstruction_reducer_contract", "RECONSTRUCTION_REDUCER_CONTRACT_RFC.md", "RECONSTRUCTION_REDUCER_CONTRACT_RFC_ZH.md", "reconstruction_boundary", ("reconstruction_pressure",), "both", "Future reducer contract without reducer execution."),
    SourceSpec("payload_diff_policy", "PAYLOAD_DIFF_CAPTURE_POLICY_RFC.md", "PAYLOAD_DIFF_CAPTURE_POLICY_RFC_ZH.md", "reconstruction_boundary", ("reconstruction_pressure",), "both", "Payload/diff vocabulary without capture or compaction."),
)

SOURCE_BY_ID = {spec.source_id: spec for spec in SOURCE_WHITELIST}

PRESSURE_SOURCE_IDS = {
    "observability_pressure": ("foundation_status", "phase_index", "observatory_report", "visual_naming", "harness_usability_p108"),
    "growth_review_pressure": ("growth_candidate_lifecycle", "productive_drift", "stateful_memory_policy", "architecture_boundaries", "deliberation_tick"),
    "adapter_boundary_pressure": ("architecture_boundaries", "thin_interaction_harness", "conversation_intake", "state_backed_read_only_harness"),
    "product_layer_pressure": ("foundation_status", "visual_naming", "architecture_boundaries", "risk_register"),
    "capability_evolution_pressure": ("tool_first_self_evolution", "capability_evolution_boundary", "deliberation_tick", "risk_register"),
    "temporal_pressure": ("temporal_awareness", "ctm_temporal_dynamics", "temporal_coherence_eval", "deliberation_tick", "thought_trace_storage", "session_resume"),
    "reconstruction_pressure": ("reconstruction_reducer_contract", "payload_diff_policy", "boundary_test_matrix", "architecture_boundaries"),
    "unknown_pressure": ("foundation", "open_questions", "risk_register", "boundary_test_matrix"),
}


def load_source_inventory(lang: str = "en") -> list[dict[str, Any]]:
    _validate_lang(lang)
    return [_build_source_record(spec, lang) for spec in SOURCE_WHITELIST]


def load_source_record(source_id: str, lang: str = "en") -> dict[str, Any]:
    _validate_lang(lang)
    if source_id not in SOURCE_BY_ID:
        raise ValueError(f"unknown source_id: {source_id}")
    return _build_source_record(SOURCE_BY_ID[source_id], lang)


def source_refs_for_pressure(pressure_type: str, lang: str = "en") -> list[dict[str, Any]]:
    _validate_lang(lang)
    if pressure_type not in PRESSURE_SOURCE_IDS:
        raise ValueError(f"unknown pressure_type: {pressure_type}")
    return [load_source_record(source_id, lang=lang) for source_id in PRESSURE_SOURCE_IDS[pressure_type]]


def build_source_inventory_report(lang: str = "en") -> dict[str, Any]:
    _validate_lang(lang)
    records = load_source_inventory(lang=lang)
    return {
        "report_id": "harness_source_inventory_v0.1",
        "generated_by": "source_loader",
        "lang": lang,
        "scope": "read_only_whitelisted_markdown",
        "source_count": len(records),
        "sources": records,
        "pressure_mappings": {
            pressure: [record["source_id"] for record in source_refs_for_pressure(pressure, lang=lang)]
            for pressure in PRESSURE_SOURCE_IDS
        },
        "disallowed_sources": [
            "user_supplied_paths",
            "hidden_files",
            "credentials",
            "work_01_state",
            "state_jsonl_logs",
            "imported_memory_dumps",
            "adapter_directories",
            "cloud_deployment_secrets",
            "network_urls",
            "binary_files",
            "generated_caches",
            "outside_repository_root",
        ],
        "non_execution_invariants": dict(NON_EXECUTION_INVARIANTS),
    }


def render_source_inventory_report(report: dict[str, Any], output_format: str) -> str:
    if output_format not in OUTPUT_FORMATS:
        raise ValueError("output_format must be 'markdown' or 'json'")
    if output_format == "json":
        return json.dumps(report, ensure_ascii=False, indent=2)
    zh = report.get("lang") == "zh"
    title = "Harness Source Inventory / 试验台来源清单" if zh else "Harness Source Inventory"
    lines = [
        f"# {title}",
        "",
        f"`report_id`: `{report['report_id']}`",
        f"`scope`: `{report['scope']}`",
        f"`source_count`: `{report['source_count']}`",
        "",
        "## Sources" if not zh else "## Sources / 来源",
        "",
        "| source_id | path | class | research_line | exists | heading |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for source in report["sources"]:
        lines.append(
            "| {source_id} | {path} | {source_class} | {research_line} | {exists} | {heading} |".format(
                source_id=source["source_id"],
                path=source["path"],
                source_class=source["class"],
                research_line=source["research_line"],
                exists=str(source["exists"]).lower(),
                heading=_escape_table(str(source["heading"])),
            )
        )
    lines.extend([
        "",
        "## Pressure Mappings" if not zh else "## Pressure Mappings / 压力映射",
        "",
        "| pressure_type | source_ids |",
        "| --- | --- |",
    ])
    for pressure, source_ids in report["pressure_mappings"].items():
        lines.append(f"| `{pressure}` | {', '.join(source_ids)} |")
    lines.extend([
        "",
        "## Non-Execution Invariants" if not zh else "## Non-Execution Invariants / 非执行边界",
        "",
    ])
    for key, value in report["non_execution_invariants"].items():
        lines.append(f"- {key}: {str(value).lower()}")
    return "\n".join(lines)


def _build_source_record(spec: SourceSpec, lang: str) -> dict[str, Any]:
    path = spec.zh_path if lang == "zh" else spec.en_path
    paired_path = spec.en_path if lang == "zh" else spec.zh_path
    full_path = _safe_repo_markdown_path(path)
    exists = full_path.exists()
    text = full_path.read_text(encoding="utf-8") if exists else ""
    heading = _extract_heading(text)
    return {
        "source_id": spec.source_id,
        "path": path,
        "paired_path": paired_path,
        "lang": lang,
        "class": spec.source_class,
        "pressure_types": list(spec.pressure_types),
        "research_line": spec.research_line,
        "why_allowed": spec.why_allowed,
        "exists": exists,
        "heading": heading,
        "excerpt": _extract_excerpt(text),
        "read_mode": "read_only",
        "source_status": "approved_whitelist",
        "missing_reason": "" if exists else "missing_whitelisted_file",
    }


def _safe_repo_markdown_path(path: str) -> Path:
    candidate = Path(path)
    if candidate.is_absolute() or candidate.suffix != ".md" or len(candidate.parts) != 1:
        raise ValueError(f"unsafe source path in whitelist: {path}")
    if any(part.startswith(".") or part == ".." for part in candidate.parts):
        raise ValueError(f"unsafe source path in whitelist: {path}")
    resolved = (REPO_ROOT / candidate).resolve()
    if resolved.parent != REPO_ROOT:
        raise ValueError(f"source path escapes repository root: {path}")
    return resolved


def _extract_heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return ""


def _extract_excerpt(text: str, max_chars: int = 280) -> str:
    lines = []
    seen_heading = False
    for line in text.splitlines():
        if line.startswith("# "):
            seen_heading = True
            continue
        if not seen_heading:
            continue
        stripped = line.strip()
        if stripped:
            lines.append(stripped)
        if sum(len(item) for item in lines) > max_chars:
            break
    excerpt = " ".join(lines)
    if len(excerpt) > max_chars:
        return excerpt[: max_chars - 3].rstrip() + "..."
    return excerpt


def _validate_lang(lang: str) -> None:
    if lang not in LANGUAGES:
        raise ValueError("lang must be 'en' or 'zh'")


def _escape_table(value: str) -> str:
    return value.replace("|", "\\|")
