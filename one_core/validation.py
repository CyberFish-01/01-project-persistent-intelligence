from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable
import uuid


REQUIRED_TOP_LEVEL_KEYS = [
    "state_version",
    "agent_id",
    "created_at",
    "updated_at",
    "identity_core",
    "working_state",
    "memory_stores",
    "relationship_map",
    "project_map",
    "affective_state",
    "adapter_registry",
    "session_policy",
    "adapter_event_index",
    "open_conflicts",
    "claim_graph",
    "context_builder",
    "task_hub",
    "identity_update_gate",
    "dream_queue",
    "snapshots",
    "audit_log",
    "evaluation_trace",
    "update_log",
]

REQUIRED_MEMORY_STORES = [
    "imported_memory",
    "episodic_memory",
    "candidate_memory",
    "semantic_memory",
    "identity_memory",
    "archived_memory",
]


def stable_validation_id(prefix: str, *parts: object) -> str:
    normalized = "|".join(str(part or "").strip().lower() for part in parts)
    return f"{prefix}_{uuid.uuid5(uuid.NAMESPACE_URL, normalized).hex[:12]}"

REQUIRED_ANCHORS = ["who_am_i", "where_am_i", "what_am_i_doing"]
VALID_SESSION_POLICY_ACTIONS = {"allow", "dry_run_only", "reject"}
MEMORY_STORES_REQUIRING_METADATA = [
    "imported_memory",
    "episodic_memory",
    "candidate_memory",
    "semantic_memory",
    "identity_memory",
    "archived_memory",
]

GROWTH_SEMANTICS_REQUIRED_INVARIANTS = {
    "review_only": True,
    "execution_prohibited": True,
    "automatic_identity_mutation_allowed": False,
    "automatic_memory_promotion_allowed": False,
    "memory_rewrite_executed": False,
    "recall_mutation_executed": False,
    "growth_engine_executed": False,
}


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str
    severity: str = "error"


def validate_state(
    state: dict[str, Any],
    episodes: Iterable[dict] | None = None,
    events: Iterable[dict] | None = None,
    dream_artifacts: Iterable[dict] | None = None,
) -> dict:
    issues: list[ValidationIssue] = []
    issues.extend(validate_top_level(state))
    issues.extend(validate_identity_core(state))
    issues.extend(validate_working_state(state))
    issues.extend(validate_memory_stores(state))
    issues.extend(validate_audit_log(state))
    issues.extend(validate_update_log(state))
    issues.extend(validate_adapter_registry(state))
    issues.extend(validate_session_policy(state))
    issues.extend(validate_adapter_event_index(state, episodes or []))
    issues.extend(validate_claim_graph(state))
    issues.extend(validate_context_builder(state))
    issues.extend(validate_task_hub(state))
    issues.extend(validate_identity_update_gate(state))
    issues.extend(validate_snapshots(state))
    if events is not None:
        issues.extend(validate_event_log(state, events))
    if dream_artifacts is not None:
        issues.extend(validate_dream_artifacts(dream_artifacts))
    return {
        "status": "passed" if not issues else "failed",
        "issues": [issue_to_dict(issue) for issue in issues],
        "issue_count": len(issues),
    }


def validate_growth_semantics_artifact(artifact: dict[str, Any]) -> dict:
    issues: list[ValidationIssue] = []
    path = "growth_semantics_artifact"
    if artifact.get("mode") not in {
        "stateful_memory_rfc_v0.1",
        "growth_semantics_report_v0.1",
    }:
        issues.append(
            ValidationIssue(
                path + ".mode",
                "Growth semantics artifact mode is invalid.",
            )
        )
    for key, expected in GROWTH_SEMANTICS_REQUIRED_INVARIANTS.items():
        if artifact.get(key) is not expected:
            issues.append(
                ValidationIssue(
                    path + f".{key}",
                    "Growth semantics artifact must preserve review-only invariants.",
                )
            )
    if artifact.get("mode") == "growth_semantics_report_v0.1":
        for bucket_key in (
            "growth_candidates",
            "mutation_only_changes",
            "insufficient_context_changes",
            "identity_review_required_changes",
            "record_only_changes",
        ):
            if not isinstance(artifact.get(bucket_key), list):
                issues.append(
                    ValidationIssue(
                        path + f".{bucket_key}",
                        "Growth semantics report buckets must be lists.",
                    )
                )
        for index, item in enumerate(artifact.get("interpreted_changes", [])):
            if not isinstance(item, dict):
                issues.append(
                    ValidationIssue(
                        path + f".interpreted_changes[{index}]",
                        "Growth semantics interpreted change must be an object.",
                    )
                )
                continue
            for key, expected in (
                ("automatic_identity_mutation_allowed", False),
                ("automatic_memory_promotion_allowed", False),
                ("memory_rewrite_executed", False),
                ("recall_mutation_executed", False),
                ("growth_engine_executed", False),
            ):
                if item.get(key) is not expected:
                    issues.append(
                        ValidationIssue(
                            path + f".interpreted_changes[{index}].{key}",
                            "Growth semantics interpreted changes must not execute mutations.",
                        )
                    )
            if item.get("classification") == "growth_candidate" and item.get(
                "review_required"
            ) is not True:
                issues.append(
                    ValidationIssue(
                        path + f".interpreted_changes[{index}].review_required",
                        "Growth candidates must require review.",
                    )
                )
    return {
        "status": "passed" if not issues else "failed",
        "issues": [issue_to_dict(issue) for issue in issues],
        "issue_count": len(issues),
    }


def validate_top_level(state: dict[str, Any]) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for key in REQUIRED_TOP_LEVEL_KEYS:
        if key not in state:
            issues.append(ValidationIssue(key, "Required top-level state key is missing."))
    if state.get("agent_id") != "01":
        issues.append(ValidationIssue("agent_id", "State agent_id must be 01."))
    if not state.get("state_version"):
        issues.append(ValidationIssue("state_version", "State version is required."))
    return issues


def validate_identity_core(state: dict[str, Any]) -> list[ValidationIssue]:
    identity = state.get("identity_core")
    if not isinstance(identity, dict):
        return [ValidationIssue("identity_core", "Identity core must be an object.")]

    issues: list[ValidationIssue] = []
    self_model = identity.get("self_model")
    if not isinstance(self_model, dict) or not self_model.get("summary"):
        issues.append(
            ValidationIssue(
                "identity_core.self_model.summary",
                "Identity core requires a self-model summary.",
            )
        )
    constraints = identity.get("identity_constraints")
    if not isinstance(constraints, list) or not constraints:
        issues.append(
            ValidationIssue(
                "identity_core.identity_constraints",
                "Identity core requires identity constraints.",
            )
        )
    return issues


def validate_tool_safety_policy_score(path: str, score: Any) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    if not isinstance(score, dict):
        return [ValidationIssue(path, "Tool/safety policy proposal_score must be an object.")]
    for key in (
        "score_id",
        "timestamp",
        "mode",
        "evidence_strength",
        "scope_specificity",
        "staleness",
        "priority_score",
        "recommended_review_priority",
        "factors",
        "execution_prohibited",
        "executable_policy_created",
        "identity_mutation_allowed",
    ):
        if key not in score:
            issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy score key is missing."))
    if score.get("mode") != "review_priority_only":
        issues.append(ValidationIssue(path + ".mode", "Tool/safety policy score must remain review_priority_only."))
    if score.get("recommended_review_priority") not in {"low", "medium", "high"}:
        issues.append(ValidationIssue(path + ".recommended_review_priority", "Tool/safety policy score must have a valid review priority."))
    for key in ("evidence_strength", "scope_specificity", "staleness", "priority_score"):
        value = score.get(key)
        if not isinstance(value, (int, float)) or not 0.0 <= float(value) <= 1.0:
            issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy score value must be between 0 and 1."))
    if score.get("execution_prohibited") is not True:
        issues.append(ValidationIssue(path + ".execution_prohibited", "Tool/safety policy score must prohibit execution."))
    if score.get("executable_policy_created") is not False:
        issues.append(ValidationIssue(path + ".executable_policy_created", "Tool/safety policy score must not create executable policy."))
    if score.get("identity_mutation_allowed") is not False:
        issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Tool/safety policy score must not allow Identity Core mutation."))
    if not isinstance(score.get("factors"), list) or not score.get("factors"):
        issues.append(ValidationIssue(path + ".factors", "Tool/safety policy score requires factors."))
    return issues


def validate_working_state(state: dict[str, Any]) -> list[ValidationIssue]:
    working_state = state.get("working_state")
    if not isinstance(working_state, dict):
        return [ValidationIssue("working_state", "Working state must be an object.")]

    issues: list[ValidationIssue] = []
    anchors = working_state.get("context_anchors")
    if not isinstance(anchors, dict):
        return [
            ValidationIssue(
                "working_state.context_anchors",
                "Working state requires context anchors.",
            )
        ]
    for anchor in REQUIRED_ANCHORS:
        if not anchors.get(anchor):
            issues.append(
                ValidationIssue(
                    f"working_state.context_anchors.{anchor}",
                    "Continuity anchor is missing.",
                )
            )
    active_intent = working_state.get("active_intent")
    if not isinstance(active_intent, dict) or not active_intent.get("goal"):
        issues.append(
            ValidationIssue(
                "working_state.active_intent.goal",
                "Working state requires an active intent goal.",
            )
        )
    return issues


def validate_memory_stores(state: dict[str, Any]) -> list[ValidationIssue]:
    memory_stores = state.get("memory_stores")
    if not isinstance(memory_stores, dict):
        return [ValidationIssue("memory_stores", "Memory stores must be an object.")]

    issues: list[ValidationIssue] = []
    for key in REQUIRED_MEMORY_STORES:
        if not isinstance(memory_stores.get(key), list):
            issues.append(
                ValidationIssue(
                    f"memory_stores.{key}",
                    "Memory store must exist and be a list.",
                )
            )
    issues.extend(validate_durable_memory_metadata(memory_stores))
    issues.extend(validate_candidate_memory(memory_stores))
    return issues


def validate_durable_memory_metadata(
    memory_stores: dict[str, Any]
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for store_name in MEMORY_STORES_REQUIRING_METADATA:
        memories = memory_stores.get(store_name, [])
        if not isinstance(memories, list):
            continue
        for index, memory in enumerate(memories):
            path = f"memory_stores.{store_name}[{index}]"
            if not isinstance(memory, dict):
                continue
            provenance = memory.get("provenance")
            if not isinstance(provenance, list) or not provenance:
                issues.append(
                    ValidationIssue(
                        path + ".provenance",
                        "Durable memory requires non-empty provenance.",
                    )
                )
            lifecycle = memory.get("lifecycle")
            if not isinstance(lifecycle, dict):
                issues.append(
                    ValidationIssue(
                        path + ".lifecycle",
                        "Durable memory requires lifecycle metadata.",
                    )
                )
            else:
                for key in ("status", "created_at", "review_status"):
                    if key not in lifecycle:
                        issues.append(
                            ValidationIssue(
                                path + f".lifecycle.{key}",
                                "Memory lifecycle key is missing.",
                            )
                        )
            update_history = memory.get("update_history")
            if not isinstance(update_history, list) or not update_history:
                issues.append(
                    ValidationIssue(
                        path + ".update_history",
                        "Durable memory requires update history.",
                    )
                )
            issues.extend(validate_lifecycle_action_metadata(path, memory))
    return issues


def validate_lifecycle_action_metadata(
    path: str,
    memory: dict[str, Any],
) -> list[ValidationIssue]:
    lifecycle = memory.get("lifecycle") if isinstance(memory.get("lifecycle"), dict) else {}
    status = lifecycle.get("status") or memory.get("status")
    if status not in {"archived", "discarded", "quarantined"}:
        return []
    decision_id = lifecycle.get("lifecycle_decision_id")
    if not decision_id:
        return []

    issues: list[ValidationIssue] = []
    history = memory.get("lifecycle_history")
    if not isinstance(history, list) or not history:
        issues.append(
            ValidationIssue(
                path + ".lifecycle_history",
                "Lifecycle-reviewed memory requires lifecycle history.",
            )
        )
        return issues
    latest = history[-1]
    if not isinstance(latest, dict):
        issues.append(
            ValidationIssue(
                path + ".lifecycle_history[-1]",
                "Lifecycle decision entry must be an object.",
            )
        )
        return issues
    for key in (
        "decision_id",
        "timestamp",
        "reviewer",
        "action",
        "result",
        "snapshot_id",
    ):
        if key not in latest:
            issues.append(
                ValidationIssue(
                    path + f".lifecycle_history[-1].{key}",
                    "Lifecycle decision key is missing.",
                )
            )
    if memory.get("last_lifecycle_decision_id") != latest.get("decision_id"):
        issues.append(
            ValidationIssue(
                path + ".last_lifecycle_decision_id",
                "Memory last_lifecycle_decision_id must match latest lifecycle decision.",
            )
        )
    if decision_id != latest.get("decision_id"):
        issues.append(
            ValidationIssue(
                path + ".lifecycle.lifecycle_decision_id",
                "Memory lifecycle must reference latest lifecycle decision.",
            )
        )
    return issues


def validate_candidate_memory(memory_stores: dict[str, Any]) -> list[ValidationIssue]:
    candidates = memory_stores.get("candidate_memory", [])
    if not isinstance(candidates, list):
        return []
    issues: list[ValidationIssue] = []
    for index, candidate in enumerate(candidates):
        path = f"memory_stores.candidate_memory[{index}]"
        if not isinstance(candidate, dict):
            issues.append(ValidationIssue(path, "Candidate memory must be an object."))
            continue
        for key in (
            "id",
            "status",
            "review_status",
            "promotion_target",
            "statement",
            "provenance",
            "review_history",
        ):
            if key not in candidate:
                issues.append(
                    ValidationIssue(path + f".{key}", "Candidate memory key is missing.")
                )
        lifecycle_score = candidate.get("lifecycle_score")
        if lifecycle_score is not None and not isinstance(lifecycle_score, dict):
            issues.append(
                ValidationIssue(
                    path + ".lifecycle_score",
                    "Candidate lifecycle score must be an object when present.",
                )
            )
        issues.extend(validate_candidate_review_governance(path, candidate))
    return issues


def validate_candidate_review_governance(
    path: str,
    candidate: dict[str, Any],
) -> list[ValidationIssue]:
    status = candidate.get("status")
    if status in {"candidate", "pending", None}:
        return []

    issues: list[ValidationIssue] = []
    review_history = candidate.get("review_history")
    if not isinstance(review_history, list) or not review_history:
        issues.append(
            ValidationIssue(
                path + ".review_history",
                "Reviewed candidate requires review decision history.",
            )
        )
        return issues

    latest = review_history[-1]
    if not isinstance(latest, dict):
        issues.append(
            ValidationIssue(
                path + ".review_history[-1]",
                "Review decision entry must be an object.",
            )
        )
        return issues
    for key in (
        "decision_id",
        "timestamp",
        "reviewer",
        "action",
        "result",
        "snapshot_id",
    ):
        if key not in latest:
            issues.append(
                ValidationIssue(
                    path + f".review_history[-1].{key}",
                    "Review decision key is missing.",
                )
            )
    if candidate.get("last_review_decision_id") != latest.get("decision_id"):
        issues.append(
            ValidationIssue(
                path + ".last_review_decision_id",
                "Candidate last_review_decision_id must match latest review decision.",
            )
        )
    lifecycle = candidate.get("lifecycle") if isinstance(candidate.get("lifecycle"), dict) else {}
    if lifecycle.get("review_decision_id") != latest.get("decision_id"):
        issues.append(
            ValidationIssue(
                path + ".lifecycle.review_decision_id",
                "Reviewed candidate lifecycle must reference the review decision.",
            )
        )
    return issues


def validate_audit_log(state: dict[str, Any]) -> list[ValidationIssue]:
    audit_log = state.get("audit_log")
    if not isinstance(audit_log, list):
        return [ValidationIssue("audit_log", "Audit log must be a list.")]

    issues: list[ValidationIssue] = []
    for index, entry in enumerate(audit_log):
        path = f"audit_log[{index}]"
        if not isinstance(entry, dict):
            issues.append(ValidationIssue(path, "Audit log entry must be an object."))
            continue
        for key in ("id", "timestamp", "actor", "action", "target", "outcome", "evidence"):
            if key not in entry:
                issues.append(
                    ValidationIssue(path + f".{key}", "Audit log entry key is missing.")
                )
    return issues


def validate_snapshots(state: dict[str, Any]) -> list[ValidationIssue]:
    snapshots = state.get("snapshots")
    if not isinstance(snapshots, list):
        return [ValidationIssue("snapshots", "Snapshots must be a list.")]

    issues: list[ValidationIssue] = []
    for index, snapshot in enumerate(snapshots):
        path = f"snapshots[{index}]"
        if not isinstance(snapshot, dict):
            issues.append(ValidationIssue(path, "Snapshot must be an object."))
            continue
        for key in (
            "snapshot_id",
            "timestamp",
            "actor",
            "operation",
            "target_path",
            "state_version",
            "rollback",
        ):
            if key not in snapshot:
                issues.append(
                    ValidationIssue(path + f".{key}", "Snapshot key is missing.")
                )
        rollback = snapshot.get("rollback")
        if isinstance(rollback, dict) and "reversible" not in rollback:
            issues.append(
                ValidationIssue(
                    path + ".rollback.reversible",
                    "Snapshot rollback metadata must declare reversibility.",
                )
            )
    return issues


def validate_update_log(state: dict[str, Any]) -> list[ValidationIssue]:
    update_log = state.get("update_log")
    if not isinstance(update_log, list) or not update_log:
        return [ValidationIssue("update_log", "Update log must be a non-empty list.")]

    issues: list[ValidationIssue] = []
    for index, entry in enumerate(update_log):
        path = f"update_log[{index}]"
        if not isinstance(entry, dict):
            issues.append(ValidationIssue(path, "Update log entry must be an object."))
            continue
        for key in ("id", "timestamp", "actor", "operation", "evidence", "rollback"):
            if key not in entry:
                issues.append(
                    ValidationIssue(path + f".{key}", "Update log entry key is missing.")
                )
    return issues


def validate_event_log(
    state: dict[str, Any],
    events: Iterable[dict],
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    update_ids = {
        str(update["id"])
        for update in state.get("update_log", [])
        if isinstance(update, dict) and update.get("id")
    }
    last_sequence = 0
    for index, event in enumerate(events):
        path = f"events[{index}]"
        if not isinstance(event, dict):
            issues.append(ValidationIssue(path, "Event log entry must be an object."))
            continue
        for key in (
            "event_id",
            "sequence",
            "timestamp",
            "event_type",
            "workflow",
            "trace_id",
            "update_id",
            "operation",
            "target_path",
        ):
            if key not in event:
                issues.append(ValidationIssue(path + f".{key}", "Event key is missing."))
        sequence = event.get("sequence")
        if not isinstance(sequence, int) or sequence <= last_sequence:
            issues.append(
                ValidationIssue(
                    path + ".sequence",
                    "Event sequence must increase monotonically.",
                )
            )
        elif isinstance(sequence, int):
            last_sequence = sequence
        update_id = event.get("update_id")
        if update_id and str(update_id) not in update_ids:
            issues.append(
                ValidationIssue(
                    path + ".update_id",
                    "Event update_id must reference state update_log.",
                )
            )
    return issues


def validate_dream_artifacts(
    dream_artifacts: Iterable[dict],
) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    for index, artifact in enumerate(dream_artifacts):
        path = f"dream_artifacts[{index}]"
        if not isinstance(artifact, dict):
            issues.append(ValidationIssue(path, "Dream artifact must be an object."))
            continue
        for key in (
            "artifact_id",
            "artifact_version",
            "dream_id",
            "input_manifest",
            "provenance",
            "observations",
            "proposals",
            "proposal_index",
            "review",
            "patch_diff",
            "decision_log",
            "rollback_metadata",
            "package_completeness",
        ):
            if key not in artifact:
                issues.append(ValidationIssue(path + f".{key}", "Dream artifact key is missing."))
        manifest = artifact.get("input_manifest")
        if isinstance(manifest, dict):
            if not isinstance(manifest.get("items"), list):
                issues.append(
                    ValidationIssue(
                        path + ".input_manifest.items",
                        "Dream artifact input manifest must list source items.",
                    )
                )
        review = artifact.get("review")
        if isinstance(review, dict):
            if not isinstance(review.get("queue"), list):
                issues.append(
                    ValidationIssue(
                        path + ".review.queue",
                        "Dream artifact review must include a queue.",
                    )
                )
        decision_log = artifact.get("decision_log")
        if not isinstance(decision_log, list) or not decision_log:
            issues.append(
                ValidationIssue(
                    path + ".decision_log",
                    "Dream artifact decision log must be non-empty.",
                )
            )
        rollback = artifact.get("rollback_metadata")
        if isinstance(rollback, dict):
            if "affected_ids" not in rollback:
                issues.append(
                    ValidationIssue(
                        path + ".rollback_metadata.affected_ids",
                        "Dream artifact rollback metadata must include affected ids.",
                    )
                )
        completeness = artifact.get("package_completeness")
        if isinstance(completeness, dict):
            missing = [
                key
                for key, value in completeness.items()
                if key.startswith("has_") and value is not True
            ]
            for key in missing:
                issues.append(
                    ValidationIssue(
                        path + f".package_completeness.{key}",
                        "Dream artifact package completeness flag must be true.",
                    )
                )
    return issues


def validate_adapter_registry(state: dict[str, Any]) -> list[ValidationIssue]:
    registry = state.get("adapter_registry")
    if not isinstance(registry, dict):
        return [ValidationIssue("adapter_registry", "Adapter registry must be an object.")]

    adapters = registry.get("adapters")
    if not isinstance(adapters, dict) or not adapters:
        return [
            ValidationIssue(
                "adapter_registry.adapters",
                "Adapter registry requires registered adapters.",
            )
        ]

    issues: list[ValidationIssue] = []
    for adapter_id, adapter in adapters.items():
        path = f"adapter_registry.adapters.{adapter_id}"
        if not isinstance(adapter, dict):
            issues.append(ValidationIssue(path, "Adapter entry must be an object."))
            continue
        if adapter.get("adapter_id") != adapter_id:
            issues.append(
                ValidationIssue(path + ".adapter_id", "Adapter id must match registry key.")
            )
        if "enabled" not in adapter:
            issues.append(
                ValidationIssue(path + ".enabled", "Adapter entry must declare enabled.")
            )
    return issues


def validate_session_policy(state: dict[str, Any]) -> list[ValidationIssue]:
    policy = state.get("session_policy")
    if not isinstance(policy, dict):
        return [ValidationIssue("session_policy", "Session policy must be an object.")]

    issues: list[ValidationIssue] = []
    default_action = policy.get("default_action")
    if default_action not in VALID_SESSION_POLICY_ACTIONS:
        issues.append(
            ValidationIssue(
                "session_policy.default_action",
                "Session policy default action must be allow, dry_run_only, or reject.",
            )
        )
    rules = policy.get("rules")
    if not isinstance(rules, list):
        return issues + [
            ValidationIssue("session_policy.rules", "Session policy rules must be a list.")
        ]
    for index, rule in enumerate(rules):
        path = f"session_policy.rules[{index}]"
        if not isinstance(rule, dict):
            issues.append(ValidationIssue(path, "Session policy rule must be an object."))
            continue
        if not rule.get("id"):
            issues.append(ValidationIssue(path + ".id", "Session policy rule needs an id."))
        if rule.get("action") not in VALID_SESSION_POLICY_ACTIONS:
            issues.append(
                ValidationIssue(
                    path + ".action",
                    "Session policy rule action must be allow, dry_run_only, or reject.",
                )
            )
    return issues


def validate_adapter_event_index(
    state: dict[str, Any], episodes: Iterable[dict]
) -> list[ValidationIssue]:
    index = state.get("adapter_event_index")
    if not isinstance(index, dict):
        return [
            ValidationIssue(
                "adapter_event_index", "Adapter event index must be an object."
            )
        ]

    episode_ids = {
        episode.get("id")
        for episode in episodes
        if isinstance(episode, dict) and episode.get("id")
    }
    issues: list[ValidationIssue] = []
    for adapter_id, events in index.items():
        if not isinstance(events, dict):
            issues.append(
                ValidationIssue(
                    f"adapter_event_index.{adapter_id}",
                    "Adapter event bucket must be an object.",
                )
            )
            continue
        for event_id, entry in events.items():
            path = f"adapter_event_index.{adapter_id}.{event_id}"
            if not isinstance(entry, dict):
                issues.append(ValidationIssue(path, "Event index entry must be an object."))
                continue
            if entry.get("adapter_id") != adapter_id:
                issues.append(
                    ValidationIssue(path + ".adapter_id", "Indexed adapter id mismatch.")
                )
            if entry.get("event_id") != event_id:
                issues.append(
                    ValidationIssue(path + ".event_id", "Indexed event id mismatch.")
                )
            episode_id = entry.get("episode_id")
            if episode_ids and episode_id not in episode_ids:
                issues.append(
                    ValidationIssue(
                        path + ".episode_id",
                        "Indexed event points to a missing episode.",
                    )
                )
    return issues


def validate_claim_graph(state: dict[str, Any]) -> list[ValidationIssue]:
    claim_graph = state.get("claim_graph")
    if not isinstance(claim_graph, dict):
        return [ValidationIssue("claim_graph", "Claim graph must be an object.")]

    claims = claim_graph.get("claims")
    links = claim_graph.get("links")
    proposal_link_evidence = claim_graph.get("proposal_link_evidence")
    issues: list[ValidationIssue] = []
    if claim_graph.get("graph_version") != "0.2":
        issues.append(
            ValidationIssue(
                "claim_graph.graph_version",
                "Claim graph must declare graph_version 0.2.",
            )
        )
    if not isinstance(claim_graph.get("policy"), dict):
        issues.append(
            ValidationIssue(
                "claim_graph.policy",
                "Claim graph must include revision policy.",
            )
        )
    if not isinstance(claim_graph.get("review_decisions"), list):
        issues.append(
            ValidationIssue(
                "claim_graph.review_decisions",
                "Claim graph review decisions must be a list.",
            )
        )
    if not isinstance(proposal_link_evidence, list):
        issues.append(
            ValidationIssue(
                "claim_graph.proposal_link_evidence",
                "Claim graph proposal link evidence must be a list.",
            )
        )
        proposal_link_evidence = []
    if not isinstance(claims, list):
        issues.append(ValidationIssue("claim_graph.claims", "Claim graph claims must be a list."))
        claims = []
    if not isinstance(links, list):
        issues.append(ValidationIssue("claim_graph.links", "Claim graph links must be a list."))
        links = []

    claim_ids: set[str] = set()
    for index, claim in enumerate(claims):
        path = f"claim_graph.claims[{index}]"
        if not isinstance(claim, dict):
            issues.append(ValidationIssue(path, "Claim must be an object."))
            continue
        for key in (
            "claim_id",
            "timestamp",
            "claim_type",
            "statement",
            "status",
            "evidence",
            "provenance",
            "dependencies",
            "revision_policy",
            "review_history",
            "resolution",
        ):
            if key not in claim:
                issues.append(ValidationIssue(path + f".{key}", "Claim key is missing."))
        claim_id = claim.get("claim_id")
        if claim_id in claim_ids:
            issues.append(ValidationIssue(path + ".claim_id", "Claim id must be unique."))
        if isinstance(claim_id, str):
            claim_ids.add(claim_id)
        if not isinstance(claim.get("evidence"), list) or not claim.get("evidence"):
            issues.append(
                ValidationIssue(
                    path + ".evidence",
                    "Claim requires non-empty evidence.",
                )
            )
        if not isinstance(claim.get("provenance"), list) or not claim.get("provenance"):
            issues.append(
                ValidationIssue(
                    path + ".provenance",
                    "Claim requires non-empty provenance.",
                )
            )
        resolution = claim.get("resolution")
        if not isinstance(resolution, dict):
            issues.append(ValidationIssue(path + ".resolution", "Claim resolution must be an object."))
        elif "status" not in resolution or "requires_review" not in resolution:
            issues.append(
                ValidationIssue(
                    path + ".resolution",
                    "Claim resolution must include status and requires_review.",
                )
            )
        elif "patch_preview" not in resolution:
            issues.append(
                ValidationIssue(
                    path + ".resolution.patch_preview",
                    "Claim resolution must include a minimal-change patch preview.",
                )
            )
        if claim.get("status") in {"resolved", "rejected", "quarantined"}:
            history = claim.get("review_history")
            if not isinstance(history, list) or not history:
                issues.append(
                    ValidationIssue(
                        path + ".review_history",
                        "Reviewed claim requires review history.",
                    )
                )
            elif history[-1].get("decision_id") != claim.get("last_review_decision_id"):
                issues.append(
                    ValidationIssue(
                        path + ".last_review_decision_id",
                        "Claim last_review_decision_id must match latest review decision.",
                    )
                )

    for index, link in enumerate(links):
        path = f"claim_graph.links[{index}]"
        if not isinstance(link, dict):
            issues.append(ValidationIssue(path, "Claim graph link must be an object."))
            continue
        for key in ("link_id", "timestamp", "from", "to", "type", "reason"):
            if key not in link:
                issues.append(ValidationIssue(path + f".{key}", "Claim graph link key is missing."))
        if link.get("type") not in {"contradicts", "supports", "supersedes", "depends_on"}:
            issues.append(
                ValidationIssue(
                    path + ".type",
                    "Claim graph link type is not supported.",
                )
            )
        endpoints = {str(link.get("from")), str(link.get("to"))}
        evidence_bridge_id = str(link.get("evidence_bridge_id") or "")
        is_evidence_bridge = (
            link.get("claim_graph_mode") == "evidence_bridge_only"
            and bool(evidence_bridge_id)
        )
        if claim_ids and not is_evidence_bridge and not any(endpoint in claim_ids for endpoint in endpoints):
            issues.append(
                ValidationIssue(
                    path,
                    "Claim graph link must reference at least one known claim.",
                )
            )
        if is_evidence_bridge:
            if link.get("relationship_mode") != "review_link_only":
                issues.append(ValidationIssue(path + ".relationship_mode", "Claim graph evidence bridge link must remain review_link_only."))
            if link.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Claim graph evidence bridge link must prohibit execution."))
            if link.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Claim graph evidence bridge link must not create executable policy."))
            if link.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Claim graph evidence bridge link must not mutate Identity Core."))
    for index, evidence in enumerate(proposal_link_evidence):
        path = f"claim_graph.proposal_link_evidence[{index}]"
        if not isinstance(evidence, dict):
            issues.append(ValidationIssue(path, "Proposal link evidence must be an object."))
            continue
        for key in (
            "evidence_id",
            "timestamp",
            "source_link_id",
            "from_proposal_id",
            "to_proposal_id",
            "link_type",
            "status",
            "reviewer",
            "evidence",
            "relationship_mode",
            "claim_graph_mode",
            "requires_review",
            "execution_prohibited",
            "executable_policy",
            "executable_policy_created",
            "identity_mutation_allowed",
            "claim_mutation_allowed",
            "semantic_memory_mutation_allowed",
            "provenance",
            "rollback",
        ):
            if key not in evidence:
                issues.append(ValidationIssue(path + f".{key}", "Proposal link evidence key is missing."))
        if evidence.get("status") not in {"active", "archived", "discarded", "quarantined"}:
            issues.append(ValidationIssue(path + ".status", "Proposal link evidence status is invalid."))
        if evidence.get("link_type") not in {"supports", "conflicts_with", "supersedes", "overlaps", "depends_on"}:
            issues.append(ValidationIssue(path + ".link_type", "Proposal link evidence link type is invalid."))
        if not isinstance(evidence.get("evidence"), list) or not evidence.get("evidence"):
            issues.append(ValidationIssue(path + ".evidence", "Proposal link evidence requires evidence."))
        if evidence.get("relationship_mode") != "review_link_only":
            issues.append(ValidationIssue(path + ".relationship_mode", "Proposal link evidence must remain review_link_only."))
        if evidence.get("claim_graph_mode") != "evidence_bridge_only":
            issues.append(ValidationIssue(path + ".claim_graph_mode", "Proposal link evidence must remain evidence_bridge_only."))
        if evidence.get("requires_review") is not True:
            issues.append(ValidationIssue(path + ".requires_review", "Proposal link evidence must require review."))
        if evidence.get("execution_prohibited") is not True:
            issues.append(ValidationIssue(path + ".execution_prohibited", "Proposal link evidence must prohibit execution."))
        if evidence.get("executable_policy") is not False:
            issues.append(ValidationIssue(path + ".executable_policy", "Proposal link evidence must not be executable policy."))
        if evidence.get("executable_policy_created") is not False:
            issues.append(ValidationIssue(path + ".executable_policy_created", "Proposal link evidence must not create executable policy."))
        if evidence.get("identity_mutation_allowed") is not False:
            issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Proposal link evidence must not mutate Identity Core."))
        if evidence.get("claim_mutation_allowed") is not False:
            issues.append(ValidationIssue(path + ".claim_mutation_allowed", "Proposal link evidence must not mutate claims."))
        if evidence.get("semantic_memory_mutation_allowed") is not False:
            issues.append(ValidationIssue(path + ".semantic_memory_mutation_allowed", "Proposal link evidence must not mutate semantic memory."))
    return issues


def validate_context_builder(state: dict[str, Any]) -> list[ValidationIssue]:
    context_builder = state.get("context_builder")
    if not isinstance(context_builder, dict):
        return [ValidationIssue("context_builder", "Context builder must be an object.")]

    issues: list[ValidationIssue] = []
    if context_builder.get("builder_version") != "0.3":
        issues.append(
            ValidationIssue(
                "context_builder.builder_version",
                "Context builder must declare builder_version 0.3.",
            )
        )
    policy = context_builder.get("policy")
    if not isinstance(policy, dict):
        issues.append(
            ValidationIssue(
                "context_builder.policy",
                "Context builder must include a policy object.",
            )
        )
        policy = {}
    if policy.get("policy_version") != "0.3":
        issues.append(
            ValidationIssue(
                "context_builder.policy.policy_version",
                "Context policy must declare policy_version 0.3.",
            )
        )
    dimensions = policy.get("selection_dimensions")
    if not isinstance(dimensions, list):
        issues.append(
            ValidationIssue(
                "context_builder.policy.selection_dimensions",
                "Context policy must include selection dimensions.",
            )
        )
        dimensions = []
    for dimension in (
        "identity_gate_signal",
        "claim_review_signal",
        "governance_evidence_signal",
        "dream_artifact_signal",
    ):
        if dimension not in dimensions:
            issues.append(
                ValidationIssue(
                    f"context_builder.policy.selection_dimensions.{dimension}",
                    "Context policy selection dimension is missing.",
                )
            )
    budgets = policy.get("budgets")
    if not isinstance(budgets, dict):
        issues.append(
            ValidationIssue(
                "context_builder.policy.budgets",
                "Context policy must include budgets.",
            )
        )
        budgets = {}
    for key in (
        "episodic_memory",
        "semantic_memory",
        "imported_memory",
        "source_attribution",
        "activation_trace_history",
    ):
        if key not in budgets:
            issues.append(
                ValidationIssue(
                    f"context_builder.policy.budgets.{key}",
                    "Context policy budget is missing.",
                )
            )
    signal_weights = policy.get("signal_weights")
    if not isinstance(signal_weights, dict):
        issues.append(
            ValidationIssue(
                "context_builder.policy.signal_weights",
                "Context policy must include signal weights.",
            )
        )
        signal_weights = {}
    for key in (
        "identity_gate_evidence",
        "claim_graph_evidence",
        "governance_proposal_link_evidence",
        "dream_artifact_input",
    ):
        if key not in signal_weights:
            issues.append(
                ValidationIssue(
                    f"context_builder.policy.signal_weights.{key}",
                    "Context policy signal weight is missing.",
                )
            )
    if not isinstance(policy.get("persistence"), dict):
        issues.append(
            ValidationIssue(
                "context_builder.policy.persistence",
                "Context policy must include persistence settings.",
            )
        )
    traces = context_builder.get("activation_traces")
    if not isinstance(traces, list):
        issues.append(
            ValidationIssue(
                "context_builder.activation_traces",
                "Context activation traces must be a list.",
            )
        )
        traces = []
    for index, trace in enumerate(traces):
        path = f"context_builder.activation_traces[{index}]"
        if not isinstance(trace, dict):
            issues.append(ValidationIssue(path, "Context activation trace must be an object."))
            continue
        for key in ("trace_id", "context_package_id", "timestamp", "policy_version", "metrics"):
            if key not in trace:
                issues.append(
                    ValidationIssue(
                        path + f".{key}",
                        "Context activation trace key is missing.",
                    )
                )
        if "signal_attribution_summary" in trace and not isinstance(
            trace.get("signal_attribution_summary"),
            dict,
        ):
            issues.append(
                ValidationIssue(
                    path + ".signal_attribution_summary",
                    "Context activation trace signal attribution summary must be an object.",
                )
            )
        selected = trace.get("selected", [])
        if isinstance(selected, list):
            for item_index, item in enumerate(selected):
                if not isinstance(item, dict):
                    continue
                if "signal_attribution" in item and not isinstance(
                    item.get("signal_attribution"),
                    list,
                ):
                    issues.append(
                        ValidationIssue(
                            path + f".selected[{item_index}].signal_attribution",
                            "Selected context signal attribution must be a list.",
                        )
                    )
    coverage_reviews = context_builder.get("attribution_coverage_reviews")
    if not isinstance(coverage_reviews, list):
        issues.append(
            ValidationIssue(
                "context_builder.attribution_coverage_reviews",
                "Context attribution coverage reviews must be a list.",
            )
        )
        coverage_reviews = []
    for index, review in enumerate(coverage_reviews):
        path = f"context_builder.attribution_coverage_reviews[{index}]"
        if not isinstance(review, dict):
            issues.append(
                ValidationIssue(path, "Context attribution coverage review must be an object.")
            )
            continue
        for key in (
            "review_id",
            "timestamp",
            "status",
            "metrics",
            "review_signals",
            "lifecycle",
            "update_history",
        ):
            if key not in review:
                issues.append(
                    ValidationIssue(
                        path + f".{key}",
                        "Context attribution coverage review key is missing.",
                    )
                )
        if not isinstance(review.get("metrics", {}), dict):
            issues.append(
                ValidationIssue(
                    path + ".metrics",
                    "Context attribution coverage review metrics must be an object.",
                )
            )
        if not isinstance(review.get("review_signals", []), list):
            issues.append(
                ValidationIssue(
                    path + ".review_signals",
                    "Context attribution coverage review signals must be a list.",
                )
            )
        if review.get("review_only") is not True:
            issues.append(
                ValidationIssue(
                    path + ".review_only",
                    "Context attribution coverage review must remain review-only.",
                )
            )
        for flag in (
            "execution_prohibited",
            "executable_policy",
            "executable_policy_created",
            "identity_mutation_allowed",
        ):
            expected = False if flag != "execution_prohibited" else True
            if review.get(flag) is not expected:
                issues.append(
                    ValidationIssue(
                        path + f".{flag}",
                        "Context attribution coverage review must remain review-only.",
                    )
                )
        lifecycle = review.get("lifecycle") if isinstance(review.get("lifecycle"), dict) else {}
        lifecycle_status = lifecycle.get("status")
        if lifecycle_status not in {"active", "acknowledged", "archived", "quarantined"}:
            issues.append(
                ValidationIssue(
                    path + ".lifecycle.status",
                    "Context attribution coverage review must have a valid lifecycle status.",
                )
            )
        if not isinstance(review.get("update_history"), list):
            issues.append(
                ValidationIssue(
                    path + ".update_history",
                    "Context attribution coverage review update history must be a list.",
                )
            )
        if lifecycle_status in {"acknowledged", "archived", "quarantined"}:
            decision_id = lifecycle.get("lifecycle_decision_id")
            if not decision_id:
                issues.append(
                    ValidationIssue(
                        path + ".lifecycle.lifecycle_decision_id",
                        "Context attribution coverage lifecycle must reference a decision.",
                    )
                )
            elif decision_id != review.get("last_lifecycle_decision_id"):
                issues.append(
                    ValidationIssue(
                        path + ".last_lifecycle_decision_id",
                        "Context attribution coverage last_lifecycle_decision_id must match lifecycle decision.",
                    )
                )
            lifecycle_history = review.get("lifecycle_history")
            if not isinstance(lifecycle_history, list) or not lifecycle_history:
                issues.append(
                    ValidationIssue(
                        path + ".lifecycle_history",
                        "Context attribution coverage lifecycle action requires lifecycle history.",
                    )
                )
            elif lifecycle_history[-1].get("decision_id") != review.get(
                "last_lifecycle_decision_id"
            ):
                issues.append(
                    ValidationIssue(
                        path + ".lifecycle_history",
                        "Context attribution coverage lifecycle history must reference latest decision.",
                    )
                )
    coverage_review_ids = {
        review.get("review_id")
        for review in coverage_reviews
        if isinstance(review, dict)
    }
    lifecycle_decisions = context_builder.get(
        "attribution_coverage_lifecycle_decisions"
    )
    if not isinstance(lifecycle_decisions, list):
        issues.append(
            ValidationIssue(
                "context_builder.attribution_coverage_lifecycle_decisions",
                "Context attribution coverage lifecycle decisions must be a list.",
            )
        )
        lifecycle_decisions = []
    for index, decision in enumerate(lifecycle_decisions):
        path = f"context_builder.attribution_coverage_lifecycle_decisions[{index}]"
        if not isinstance(decision, dict):
            issues.append(
                ValidationIssue(
                    path,
                    "Context attribution coverage lifecycle decision must be an object.",
                )
            )
            continue
        for key in (
            "decision_id",
            "timestamp",
            "review_id",
            "reviewer",
            "action",
            "result",
            "snapshot_id",
            "evidence",
            "review_only",
            "execution_prohibited",
            "executable_policy",
            "executable_policy_created",
            "identity_mutation_allowed",
        ):
            if key not in decision:
                issues.append(
                    ValidationIssue(
                        path + f".{key}",
                        "Context attribution coverage lifecycle decision key is missing.",
                    )
                )
        if decision.get("result") not in {"acknowledged", "archived", "quarantined"}:
            issues.append(
                ValidationIssue(
                    path + ".result",
                    "Context attribution coverage lifecycle decision must have a valid result.",
                )
            )
        if decision.get("action") not in {"acknowledge", "archive", "quarantine"}:
            issues.append(
                ValidationIssue(
                    path + ".action",
                    "Context attribution coverage lifecycle decision must have a valid action.",
                )
            )
        if decision.get("review_id") not in coverage_review_ids:
            issues.append(
                ValidationIssue(
                    path + ".review_id",
                    "Context attribution coverage lifecycle decision must reference an existing review.",
                )
            )
        if decision.get("review_only") is not True:
            issues.append(
                ValidationIssue(
                    path + ".review_only",
                    "Context attribution coverage lifecycle decision must remain review-only.",
                )
            )
        for flag in (
            "execution_prohibited",
            "executable_policy",
            "executable_policy_created",
            "identity_mutation_allowed",
        ):
            expected = False if flag != "execution_prohibited" else True
            if decision.get(flag) is not expected:
                issues.append(
                    ValidationIssue(
                        path + f".{flag}",
                        "Context attribution coverage lifecycle decision must remain review-only.",
                    )
                )
    return issues


def validate_task_hub(state: dict[str, Any]) -> list[ValidationIssue]:
    task_hub = state.get("task_hub")
    if not isinstance(task_hub, dict):
        return [ValidationIssue("task_hub", "Task hub must be an object.")]

    issues: list[ValidationIssue] = []
    for key in (
        "active_tasks",
        "completed_tasks",
        "blocked_tasks",
        "recurring_duties",
        "action_trace",
        "reflection_log",
        "reflection_guidance_queue",
        "reflection_guidance_decisions",
        "tool_safety_policy_proposals",
        "tool_safety_policy_links",
        "tool_safety_policy_link_lifecycle_decisions",
        "tool_safety_policy_decisions",
        "tool_safety_policy_lifecycle_decisions",
        "event_retention_reviews",
        "event_retention_lifecycle_decisions",
        "event_payload_capture_policy_proposals",
        "event_payload_capture_policy_decisions",
        "reconstruction_schema_review_decisions",
        "reconstruction_schema_evidence_request_lifecycle_decisions",
        "failure_reflections",
        "procedural_candidates",
        "cautionary_procedural_candidates",
        "cautionary_procedural_memory",
        "cautionary_review_decisions",
        "cautionary_lifecycle_decisions",
        "procedural_memory",
        "procedural_lifecycle_decisions",
        "procedural_review_decisions",
    ):
        if not isinstance(task_hub.get(key), list):
            issues.append(ValidationIssue(f"task_hub.{key}", "Task hub key must be a list."))

    for bucket_name in ("active_tasks", "completed_tasks", "blocked_tasks"):
        tasks = task_hub.get(bucket_name, [])
        if not isinstance(tasks, list):
            continue
        for index, task in enumerate(tasks):
            path = f"task_hub.{bucket_name}[{index}]"
            if not isinstance(task, dict):
                issues.append(ValidationIssue(path, "Task must be an object."))
                continue
            for key in ("task_id", "title", "status", "created_at"):
                if not task.get(key):
                    issues.append(ValidationIssue(path + f".{key}", "Task key is missing."))

    action_trace = task_hub.get("action_trace", [])
    if isinstance(action_trace, list):
        for index, action in enumerate(action_trace):
            path = f"task_hub.action_trace[{index}]"
            if not isinstance(action, dict):
                issues.append(ValidationIssue(path, "Action trace entry must be an object."))
                continue
            for key in ("action_id", "trace_id", "timestamp", "workflow", "status"):
                if not action.get(key):
                    issues.append(ValidationIssue(path + f".{key}", "Action trace key is missing."))

    candidates = task_hub.get("procedural_candidates", [])
    if isinstance(candidates, list):
        for index, candidate in enumerate(candidates):
            path = f"task_hub.procedural_candidates[{index}]"
            if not isinstance(candidate, dict):
                issues.append(ValidationIssue(path, "Procedural candidate must be an object."))
                continue
            for key in ("candidate_id", "workflow", "evidence", "review_status"):
                if key not in candidate:
                    issues.append(ValidationIssue(path + f".{key}", "Procedural candidate key is missing."))
            if not isinstance(candidate.get("evidence"), list) or not candidate.get("evidence"):
                issues.append(
                    ValidationIssue(
                        path + ".evidence",
                        "Procedural candidate requires non-empty evidence.",
                    )
                )
            if candidate.get("review_status") in {"approved", "rejected", "archived", "quarantined"}:
                history = candidate.get("review_history")
                if not isinstance(history, list) or not history:
                    issues.append(
                        ValidationIssue(
                            path + ".review_history",
                            "Reviewed procedural candidate requires review history.",
                        )
                    )
                elif history[-1].get("decision_id") != candidate.get("last_review_decision_id"):
                    issues.append(
                        ValidationIssue(
                            path + ".last_review_decision_id",
                            "Procedural candidate last_review_decision_id must match latest decision.",
                        )
                    )
    reflections = task_hub.get("failure_reflections", [])
    if isinstance(reflections, list):
        for index, reflection in enumerate(reflections):
            path = f"task_hub.failure_reflections[{index}]"
            if not isinstance(reflection, dict):
                issues.append(ValidationIssue(path, "Failure reflection must be an object."))
                continue
            for key in ("reflection_id", "timestamp", "workflow", "summary", "lesson", "status", "evidence", "provenance"):
                if key not in reflection:
                    issues.append(ValidationIssue(path + f".{key}", "Failure reflection key is missing."))
    reflection_log = task_hub.get("reflection_log", [])
    if isinstance(reflection_log, list):
        for index, reflection in enumerate(reflection_log):
            path = f"task_hub.reflection_log[{index}]"
            if not isinstance(reflection, dict):
                issues.append(ValidationIssue(path, "Reflection log entry must be an object."))
                continue
            for key in (
                "reflection_id",
                "timestamp",
                "reflection_type",
                "workflow",
                "observation",
                "lesson",
                "expected_behavior",
                "actor",
                "source_ids",
                "evidence",
                "status",
                "verification_status",
                "verification_history",
                "provenance",
                "update_history",
            ):
                if key not in reflection:
                    issues.append(ValidationIssue(path + f".{key}", "Reflection log key is missing."))
            if not isinstance(reflection.get("source_ids"), list):
                issues.append(ValidationIssue(path + ".source_ids", "Reflection log source_ids must be a list."))
            if not isinstance(reflection.get("evidence"), list) or not reflection.get("evidence"):
                issues.append(ValidationIssue(path + ".evidence", "Reflection log requires non-empty evidence."))
            if reflection.get("status") not in {"open", "verified", "needs_revision", "superseded"}:
                issues.append(ValidationIssue(path + ".status", "Reflection log must have a valid status."))
            if reflection.get("verification_status") not in {"pending", "verified", "not_observed", "regressed", "superseded"}:
                issues.append(ValidationIssue(path + ".verification_status", "Reflection log must have a valid verification status."))
            if reflection.get("verification_status") != "pending":
                history = reflection.get("verification_history")
                if not isinstance(history, list) or not history:
                    issues.append(ValidationIssue(path + ".verification_history", "Verified reflection log entry requires verification history."))
                if not reflection.get("last_verification_id"):
                    issues.append(ValidationIssue(path + ".last_verification_id", "Verified reflection log entry requires last_verification_id."))
    reflection_guidance_queue = task_hub.get("reflection_guidance_queue", [])
    if isinstance(reflection_guidance_queue, list):
        for index, item in enumerate(reflection_guidance_queue):
            path = f"task_hub.reflection_guidance_queue[{index}]"
            if not isinstance(item, dict):
                issues.append(ValidationIssue(path, "Reflection guidance queue item must be an object."))
                continue
            for key in (
                "guidance_item_id",
                "reflection_id",
                "workflow",
                "review_priority",
                "recommended_review_mode",
                "evidence",
                "review_status",
                "execution_prohibited",
                "executable_policy_created",
                "identity_mutation_allowed",
                "review_history",
                "provenance",
            ):
                if key not in item:
                    issues.append(ValidationIssue(path + f".{key}", "Reflection guidance queue key is missing."))
            if item.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Reflection guidance must prohibit execution."))
            if item.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Reflection guidance must not create executable policy."))
            if item.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Reflection guidance must not allow Identity Core mutation."))
            if item.get("review_status") not in {"pending", "acknowledged", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".review_status", "Reflection guidance must have a valid review status."))
            if item.get("review_status") in {"acknowledged", "archived", "quarantined"}:
                history = item.get("review_history")
                if not isinstance(history, list) or not history:
                    issues.append(ValidationIssue(path + ".review_history", "Reviewed reflection guidance requires review history."))
                elif history[-1].get("decision_id") != item.get("last_review_decision_id"):
                    issues.append(ValidationIssue(path + ".last_review_decision_id", "Reflection guidance last_review_decision_id must match latest decision."))
    reflection_guidance_decisions = task_hub.get("reflection_guidance_decisions", [])
    if isinstance(reflection_guidance_decisions, list):
        for index, decision in enumerate(reflection_guidance_decisions):
            path = f"task_hub.reflection_guidance_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Reflection guidance decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "guidance_item_id",
                "reflection_id",
                "workflow",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "execution_prohibited",
                "executable_policy_created",
                "identity_mutation_allowed",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Reflection guidance decision key is missing."))
            if decision.get("result") not in {"acknowledged", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".result", "Reflection guidance decision must have a valid result."))
            if decision.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Reflection guidance decision must prohibit execution."))
            if decision.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Reflection guidance decision must not create executable policy."))
            if decision.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Reflection guidance decision must not allow Identity Core mutation."))
    policy_proposals = task_hub.get("tool_safety_policy_proposals", [])
    if isinstance(policy_proposals, list):
        for index, proposal in enumerate(policy_proposals):
            path = f"task_hub.tool_safety_policy_proposals[{index}]"
            if not isinstance(proposal, dict):
                issues.append(ValidationIssue(path, "Tool/safety policy proposal must be an object."))
                continue
            for key in (
                "proposal_id",
                "timestamp",
                "policy_scope",
                "proposed_rule",
                "source_guidance_item_id",
                "source_reflection_id",
                "status",
                "review_status",
                "proposal_mode",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "evidence",
                "review_history",
                "lifecycle",
                "update_history",
                "proposal_score",
                "provenance",
            ):
                if key not in proposal:
                    issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy proposal key is missing."))
            issues.extend(validate_tool_safety_policy_score(path + ".proposal_score", proposal.get("proposal_score")))
            if proposal.get("status") not in {"active", "archived", "discarded", "quarantined"}:
                issues.append(ValidationIssue(path + ".status", "Tool/safety policy proposal must have a valid lifecycle status."))
            if proposal.get("proposal_mode") != "proposal_only":
                issues.append(ValidationIssue(path + ".proposal_mode", "Tool/safety policy must remain proposal_only."))
            if proposal.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Tool/safety policy proposal requires review."))
            if proposal.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Tool/safety policy proposal must prohibit execution."))
            if proposal.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Tool/safety policy proposal must not be executable policy."))
            if proposal.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Tool/safety policy proposal must not create executable policy."))
            if proposal.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Tool/safety policy proposal must not allow Identity Core mutation."))
            if proposal.get("review_status") not in {"pending", "approved", "rejected", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".review_status", "Tool/safety policy proposal must have a valid review status."))
            if proposal.get("review_status") in {"approved", "rejected", "archived", "quarantined"}:
                history = proposal.get("review_history")
                if proposal.get("status") in {"archived", "discarded", "quarantined"}:
                    history = [] if not isinstance(history, list) else history
                elif not isinstance(history, list) or not history:
                    issues.append(ValidationIssue(path + ".review_history", "Reviewed tool/safety policy proposal requires review history."))
                elif history[-1].get("decision_id") != proposal.get("last_review_decision_id"):
                    issues.append(ValidationIssue(path + ".last_review_decision_id", "Tool/safety policy proposal last_review_decision_id must match latest decision."))
            if proposal.get("status") in {"archived", "discarded", "quarantined"}:
                lifecycle = proposal.get("lifecycle") if isinstance(proposal.get("lifecycle"), dict) else {}
                decision_id = lifecycle.get("lifecycle_decision_id")
                if not decision_id:
                    issues.append(ValidationIssue(path + ".lifecycle.lifecycle_decision_id", "Tool/safety policy lifecycle must reference a decision."))
                elif decision_id != proposal.get("last_lifecycle_decision_id"):
                    issues.append(ValidationIssue(path + ".last_lifecycle_decision_id", "Tool/safety policy last_lifecycle_decision_id must match lifecycle decision."))
                lifecycle_history = proposal.get("lifecycle_history")
                if not isinstance(lifecycle_history, list) or not lifecycle_history:
                    issues.append(ValidationIssue(path + ".lifecycle_history", "Tool/safety policy lifecycle action requires lifecycle history."))
                elif lifecycle_history[-1].get("decision_id") != proposal.get("last_lifecycle_decision_id"):
                    issues.append(ValidationIssue(path + ".lifecycle_history", "Tool/safety policy lifecycle history must reference latest decision."))
    proposal_links = task_hub.get("tool_safety_policy_links", [])
    if isinstance(proposal_links, list):
        proposal_ids = {
            proposal.get("proposal_id")
            for proposal in policy_proposals
            if isinstance(proposal, dict)
        }
        for index, link in enumerate(proposal_links):
            path = f"task_hub.tool_safety_policy_links[{index}]"
            if not isinstance(link, dict):
                issues.append(ValidationIssue(path, "Tool/safety policy link must be an object."))
                continue
            for key in (
                "link_id",
                "timestamp",
                "from_proposal_id",
                "to_proposal_id",
                "link_type",
                "status",
                "reviewer",
                "reason",
                "evidence",
                "confidence",
                "scope_overlap",
                "relationship_mode",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "provenance",
            ):
                if key not in link:
                    issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy link key is missing."))
            if link.get("from_proposal_id") not in proposal_ids:
                issues.append(ValidationIssue(path + ".from_proposal_id", "Tool/safety policy link must reference an existing from proposal."))
            if link.get("to_proposal_id") not in proposal_ids:
                issues.append(ValidationIssue(path + ".to_proposal_id", "Tool/safety policy link must reference an existing to proposal."))
            if link.get("from_proposal_id") == link.get("to_proposal_id"):
                issues.append(ValidationIssue(path, "Tool/safety policy self-link is not allowed."))
            if link.get("link_type") not in {"supports", "conflicts_with", "supersedes", "overlaps", "depends_on"}:
                issues.append(ValidationIssue(path + ".link_type", "Tool/safety policy link type is invalid."))
            if link.get("status") not in {"active", "archived", "discarded", "quarantined"}:
                issues.append(ValidationIssue(path + ".status", "Tool/safety policy link status is invalid."))
            if not isinstance(link.get("evidence"), list) or not link.get("evidence"):
                issues.append(ValidationIssue(path + ".evidence", "Tool/safety policy link requires evidence."))
            if link.get("relationship_mode") != "review_link_only":
                issues.append(ValidationIssue(path + ".relationship_mode", "Tool/safety policy link must remain review_link_only."))
            if link.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Tool/safety policy link must require review."))
            if link.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Tool/safety policy link must prohibit execution."))
            if link.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Tool/safety policy link must not be executable policy."))
            if link.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Tool/safety policy link must not create executable policy."))
            if link.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Tool/safety policy link must not allow Identity Core mutation."))
            if link.get("status") in {"archived", "discarded", "quarantined"}:
                lifecycle = link.get("lifecycle")
                if not isinstance(lifecycle, dict):
                    issues.append(ValidationIssue(path + ".lifecycle", "Tool/safety policy link lifecycle action requires lifecycle metadata."))
                else:
                    decision_id = lifecycle.get("lifecycle_decision_id")
                    if not decision_id:
                        issues.append(ValidationIssue(path + ".lifecycle.lifecycle_decision_id", "Tool/safety policy link lifecycle must reference a decision."))
                    elif decision_id != link.get("last_lifecycle_decision_id"):
                        issues.append(ValidationIssue(path + ".last_lifecycle_decision_id", "Tool/safety policy link last_lifecycle_decision_id must match lifecycle decision."))
                lifecycle_history = link.get("lifecycle_history")
                if not isinstance(lifecycle_history, list) or not lifecycle_history:
                    issues.append(ValidationIssue(path + ".lifecycle_history", "Tool/safety policy link lifecycle action requires lifecycle history."))
                elif lifecycle_history[-1].get("decision_id") != link.get("last_lifecycle_decision_id"):
                    issues.append(ValidationIssue(path + ".lifecycle_history", "Tool/safety policy link lifecycle history must reference latest decision."))
    link_lifecycle_decisions = task_hub.get("tool_safety_policy_link_lifecycle_decisions", [])
    if isinstance(link_lifecycle_decisions, list):
        link_ids = {
            link.get("link_id")
            for link in proposal_links
            if isinstance(link, dict)
        }
        for index, decision in enumerate(link_lifecycle_decisions):
            path = f"task_hub.tool_safety_policy_link_lifecycle_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Tool/safety policy link lifecycle decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "link_id",
                "from_proposal_id",
                "to_proposal_id",
                "link_type",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "evidence",
                "relationship_mode",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "rollback",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy link lifecycle decision key is missing."))
            if decision.get("link_id") not in link_ids:
                issues.append(ValidationIssue(path + ".link_id", "Tool/safety policy link lifecycle decision must reference an existing link."))
            if decision.get("action") not in {"archive", "discard", "quarantine"}:
                issues.append(ValidationIssue(path + ".action", "Tool/safety policy link lifecycle action is invalid."))
            if decision.get("result") not in {"archived", "discarded", "quarantined"}:
                issues.append(ValidationIssue(path + ".result", "Tool/safety policy link lifecycle result is invalid."))
            if not isinstance(decision.get("evidence"), list) or not decision.get("evidence"):
                issues.append(ValidationIssue(path + ".evidence", "Tool/safety policy link lifecycle decision requires evidence."))
            if decision.get("relationship_mode") != "review_link_only":
                issues.append(ValidationIssue(path + ".relationship_mode", "Tool/safety policy link lifecycle decision must remain review_link_only."))
            if decision.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Tool/safety policy link lifecycle decision must require review."))
            if decision.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Tool/safety policy link lifecycle decision must prohibit execution."))
            if decision.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Tool/safety policy link lifecycle decision must not be executable policy."))
            if decision.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Tool/safety policy link lifecycle decision must not create executable policy."))
            if decision.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Tool/safety policy link lifecycle decision must not allow Identity Core mutation."))
    policy_decisions = task_hub.get("tool_safety_policy_decisions", [])
    if isinstance(policy_decisions, list):
        for index, decision in enumerate(policy_decisions):
            path = f"task_hub.tool_safety_policy_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Tool/safety policy decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "proposal_id",
                "policy_scope",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy decision key is missing."))
            if decision.get("result") not in {"approved", "rejected", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".result", "Tool/safety policy decision must have a valid result."))
            if decision.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Tool/safety policy decision must require review."))
            if decision.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Tool/safety policy decision must prohibit execution."))
            if decision.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Tool/safety policy decision must not be executable policy."))
            if decision.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Tool/safety policy decision must not create executable policy."))
            if decision.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Tool/safety policy decision must not allow Identity Core mutation."))
            if "proposal_score" in decision:
                issues.extend(validate_tool_safety_policy_score(path + ".proposal_score", decision.get("proposal_score")))
    policy_lifecycle_decisions = task_hub.get("tool_safety_policy_lifecycle_decisions", [])
    if isinstance(policy_lifecycle_decisions, list):
        for index, decision in enumerate(policy_lifecycle_decisions):
            path = f"task_hub.tool_safety_policy_lifecycle_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Tool/safety policy lifecycle decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "proposal_id",
                "policy_scope",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "proposal_mode",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Tool/safety policy lifecycle decision key is missing."))
            if decision.get("result") not in {"archived", "discarded", "quarantined"}:
                issues.append(ValidationIssue(path + ".result", "Tool/safety policy lifecycle decision must resolve to archived, discarded, or quarantined."))
            if decision.get("proposal_mode") != "proposal_only":
                issues.append(ValidationIssue(path + ".proposal_mode", "Tool/safety policy lifecycle must remain proposal_only."))
            if decision.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Tool/safety policy lifecycle decision must require review."))
            if decision.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Tool/safety policy lifecycle decision must prohibit execution."))
            if decision.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Tool/safety policy lifecycle decision must not be executable policy."))
            if decision.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Tool/safety policy lifecycle decision must not create executable policy."))
            if decision.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Tool/safety policy lifecycle decision must not allow Identity Core mutation."))
            if "proposal_score" in decision:
                issues.extend(validate_tool_safety_policy_score(path + ".proposal_score", decision.get("proposal_score")))
    event_payload_capture_policy_proposals = task_hub.get(
        "event_payload_capture_policy_proposals",
        [],
    )
    event_payload_capture_policy_proposal_ids = {
        item.get("proposal_id")
        for item in event_payload_capture_policy_proposals
        if isinstance(item, dict) and item.get("proposal_id")
    }
    if isinstance(event_payload_capture_policy_proposals, list):
        for index, proposal in enumerate(event_payload_capture_policy_proposals):
            path = f"task_hub.event_payload_capture_policy_proposals[{index}]"
            if not isinstance(proposal, dict):
                issues.append(
                    ValidationIssue(
                        path,
                        "Event payload capture policy proposal must be an object.",
                    )
                )
                continue
            for key in (
                "proposal_id",
                "timestamp",
                "proposer",
                "status",
                "review_status",
                "proposal_mode",
                "policy_mode",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "event_schema_mutation_allowed",
                "event_payload_capture_executed",
                "event_compaction_executed",
                "events_modified",
                "safe_for_destructive_compaction",
                "coverage_summary",
                "target_path_requirements",
                "required_provenance_fields",
                "evidence",
                "review_history",
                "lifecycle",
                "update_history",
                "provenance",
            ):
                if key not in proposal:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Event payload capture policy proposal key is missing.",
                        )
                    )
            if proposal.get("proposal_mode") != "proposal_only":
                issues.append(ValidationIssue(path + ".proposal_mode", "Event payload capture policy proposal must remain proposal_only."))
            if proposal.get("policy_mode") != "event_payload_capture_policy_v0.1":
                issues.append(ValidationIssue(path + ".policy_mode", "Event payload capture policy mode is invalid."))
            if proposal.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Event payload capture policy proposal must require review."))
            if proposal.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Event payload capture policy proposal must prohibit execution."))
            if proposal.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Event payload capture policy proposal must not be executable policy."))
            if proposal.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Event payload capture policy proposal must not create executable policy."))
            if proposal.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Event payload capture policy proposal must not allow Identity Core mutation."))
            if proposal.get("event_schema_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".event_schema_mutation_allowed", "Event payload capture policy proposal must not allow event schema mutation."))
            if proposal.get("event_payload_capture_executed") is not False:
                issues.append(ValidationIssue(path + ".event_payload_capture_executed", "Event payload capture policy proposal must not execute payload capture."))
            if proposal.get("event_compaction_executed") is not False:
                issues.append(ValidationIssue(path + ".event_compaction_executed", "Event payload capture policy proposal must not execute compaction."))
            if proposal.get("events_modified") is not False:
                issues.append(ValidationIssue(path + ".events_modified", "Event payload capture policy proposal must not modify events."))
            if proposal.get("safe_for_destructive_compaction") is not False:
                issues.append(ValidationIssue(path + ".safe_for_destructive_compaction", "Event payload capture policy proposal must not mark destructive compaction safe."))
            if proposal.get("review_status") not in {"needs_review", "ready_for_review", "approved", "rejected", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".review_status", "Event payload capture policy proposal review status is invalid."))
            if proposal.get("status") not in {"active", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".status", "Event payload capture policy proposal status is invalid."))
            requirements = proposal.get("target_path_requirements")
            if not isinstance(requirements, list) or not requirements:
                issues.append(ValidationIssue(path + ".target_path_requirements", "Event payload capture policy proposal requires target path requirements."))
            elif all(isinstance(item, dict) for item in requirements):
                for requirement_index, requirement in enumerate(requirements):
                    req_path = path + f".target_path_requirements[{requirement_index}]"
                    if requirement.get("capture_mode") not in {"full_payload_and_diff", "payload_hint_required", "snapshot_link_required", "reference_only_ok"}:
                        issues.append(ValidationIssue(req_path + ".capture_mode", "Event payload capture requirement mode is invalid."))
                    if requirement.get("execution_prohibited") is not True:
                        issues.append(ValidationIssue(req_path + ".execution_prohibited", "Event payload capture requirement must prohibit execution."))
                    if requirement.get("schema_change_allowed") is not False:
                        issues.append(ValidationIssue(req_path + ".schema_change_allowed", "Event payload capture requirement must not allow schema changes."))
            else:
                issues.append(ValidationIssue(path + ".target_path_requirements", "Event payload capture policy requirements must be objects."))
            if proposal.get("review_status") in {"approved", "rejected", "archived", "quarantined"}:
                history = proposal.get("review_history")
                if not isinstance(history, list) or not history:
                    issues.append(ValidationIssue(path + ".review_history", "Reviewed event payload capture policy proposal requires review history."))
                elif history[-1].get("decision_id") != proposal.get("last_review_decision_id"):
                    issues.append(ValidationIssue(path + ".last_review_decision_id", "Event payload capture policy last review decision id must match history."))

    event_payload_capture_policy_decisions = task_hub.get(
        "event_payload_capture_policy_decisions",
        [],
    )
    if isinstance(event_payload_capture_policy_decisions, list):
        for index, decision in enumerate(event_payload_capture_policy_decisions):
            path = f"task_hub.event_payload_capture_policy_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(
                    ValidationIssue(
                        path,
                        "Event payload capture policy decision must be an object.",
                    )
                )
                continue
            for key in (
                "decision_id",
                "timestamp",
                "proposal_id",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "proposal_mode",
                "policy_mode",
                "requires_review",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "event_schema_mutation_allowed",
                "event_payload_capture_executed",
                "event_compaction_executed",
                "events_modified",
                "safe_for_destructive_compaction",
                "evidence",
                "rollback",
            ):
                if key not in decision:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Event payload capture policy decision key is missing.",
                        )
                    )
            if decision.get("proposal_id") not in event_payload_capture_policy_proposal_ids:
                issues.append(ValidationIssue(path + ".proposal_id", "Event payload capture policy decision must reference an existing proposal."))
            if decision.get("action") not in {"approve", "reject", "archive", "quarantine"}:
                issues.append(ValidationIssue(path + ".action", "Event payload capture policy review action is invalid."))
            if decision.get("result") not in {"approved", "rejected", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".result", "Event payload capture policy decision result is invalid."))
            if decision.get("proposal_mode") != "proposal_only":
                issues.append(ValidationIssue(path + ".proposal_mode", "Event payload capture policy decision must remain proposal_only."))
            if decision.get("policy_mode") != "event_payload_capture_policy_v0.1":
                issues.append(ValidationIssue(path + ".policy_mode", "Event payload capture policy decision mode is invalid."))
            if decision.get("requires_review") is not True:
                issues.append(ValidationIssue(path + ".requires_review", "Event payload capture policy decision must require review."))
            if decision.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Event payload capture policy decision must prohibit execution."))
            if decision.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Event payload capture policy decision must not be executable policy."))
            if decision.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Event payload capture policy decision must not create executable policy."))
            if decision.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Event payload capture policy decision must not allow Identity Core mutation."))
            if decision.get("event_schema_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".event_schema_mutation_allowed", "Event payload capture policy decision must not allow event schema mutation."))
            if decision.get("event_payload_capture_executed") is not False:
                issues.append(ValidationIssue(path + ".event_payload_capture_executed", "Event payload capture policy decision must not execute payload capture."))
            if decision.get("event_compaction_executed") is not False:
                issues.append(ValidationIssue(path + ".event_compaction_executed", "Event payload capture policy decision must not execute compaction."))
            if decision.get("events_modified") is not False:
                issues.append(ValidationIssue(path + ".events_modified", "Event payload capture policy decision must not modify events."))
            if decision.get("safe_for_destructive_compaction") is not False:
                issues.append(ValidationIssue(path + ".safe_for_destructive_compaction", "Event payload capture policy decision must not mark destructive compaction safe."))

    reconstruction_schema_review_decisions = task_hub.get(
        "reconstruction_schema_review_decisions",
        [],
    )
    if isinstance(reconstruction_schema_review_decisions, list):
        for index, decision in enumerate(reconstruction_schema_review_decisions):
            path = f"task_hub.reconstruction_schema_review_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(
                    ValidationIssue(
                        path,
                        "Reconstruction schema review decision must be an object.",
                    )
                )
                continue
            for key in (
                "decision_id",
                "timestamp",
                "checklist_id",
                "workflow",
                "reviewer",
                "action",
                "result",
                "rationale",
                "requested_evidence",
                "approval_scope",
                "snapshot_id",
                "review_mode",
                "checklist_mode",
                "checklist_item",
                "review_questions",
                "acceptance_criteria",
                "required_evidence",
                "source_evidence",
                "requires_review",
                "review_only",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "schema_change_approved",
                "schema_change_allowed",
                "identity_mutation_allowed",
                "event_schema_mutation_allowed",
                "event_payload_capture_executed",
                "reconstruction_executed",
                "event_compaction_executed",
                "automatic_rollback_executed",
                "events_modified",
                "rollback",
            ):
                if key not in decision:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Reconstruction schema review decision key is missing.",
                        )
                    )
            if decision.get("action") not in {
                "approve_for_schema_design",
                "request_more_evidence",
                "reject_as_low_value",
                "defer",
                "quarantine",
            }:
                issues.append(
                    ValidationIssue(
                        path + ".action",
                        "Reconstruction schema review action is invalid.",
                    )
                )
            if decision.get("result") not in {
                "approved_for_schema_design",
                "more_evidence_requested",
                "rejected_as_low_value",
                "deferred",
                "quarantined",
            }:
                issues.append(
                    ValidationIssue(
                        path + ".result",
                        "Reconstruction schema review result is invalid.",
                    )
                )
            if decision.get("review_mode") != "reconstruction_schema_review_v0.1":
                issues.append(
                    ValidationIssue(
                        path + ".review_mode",
                        "Reconstruction schema review mode is invalid.",
                    )
                )
            if (
                decision.get("checklist_mode")
                != "reconstruction_evidence_schema_review_checklist_v0.1"
            ):
                issues.append(
                    ValidationIssue(
                        path + ".checklist_mode",
                        "Reconstruction schema review checklist mode is invalid.",
                    )
                )
            if not isinstance(decision.get("requested_evidence"), list):
                issues.append(
                    ValidationIssue(
                        path + ".requested_evidence",
                        "Reconstruction schema review requested_evidence must be a list.",
                    )
                )
            if not isinstance(decision.get("approval_scope"), list):
                issues.append(
                    ValidationIssue(
                        path + ".approval_scope",
                        "Reconstruction schema review approval_scope must be a list.",
                    )
                )
            for key in (
                "requires_review",
                "review_only",
                "execution_prohibited",
            ):
                if decision.get(key) is not True:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Reconstruction schema review decision must remain review-only.",
                        )
                    )
            for key in (
                "executable_policy",
                "executable_policy_created",
                "schema_change_approved",
                "schema_change_allowed",
                "identity_mutation_allowed",
                "event_schema_mutation_allowed",
                "event_payload_capture_executed",
                "reconstruction_executed",
                "event_compaction_executed",
                "automatic_rollback_executed",
                "events_modified",
            ):
                if decision.get(key) is not False:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Reconstruction schema review decision must not execute changes.",
                        )
                    )

    valid_schema_evidence_request_ids = set()
    for decision in reconstruction_schema_review_decisions:
        if not isinstance(decision, dict):
            continue
        for requested in decision.get("requested_evidence", []):
            requested_label = str(requested).strip()
            if not requested_label:
                continue
            valid_schema_evidence_request_ids.add(
                stable_validation_id(
                    "reconstruction_schema_evidence_request",
                    decision.get("decision_id"),
                    requested_label,
                )
            )

    schema_evidence_request_lifecycle_decisions = task_hub.get(
        "reconstruction_schema_evidence_request_lifecycle_decisions",
        [],
    )
    if isinstance(schema_evidence_request_lifecycle_decisions, list):
        for index, decision in enumerate(
            schema_evidence_request_lifecycle_decisions
        ):
            path = (
                "task_hub.reconstruction_schema_evidence_request_lifecycle_decisions"
                f"[{index}]"
            )
            if not isinstance(decision, dict):
                issues.append(
                    ValidationIssue(
                        path,
                        "Reconstruction schema evidence request lifecycle decision must be an object.",
                    )
                )
                continue
            for key in (
                "decision_id",
                "timestamp",
                "request_id",
                "source_decision_id",
                "checklist_id",
                "workflow",
                "requested_evidence",
                "reviewer",
                "action",
                "result",
                "decision_note",
                "evidence_refs",
                "snapshot_id",
                "lifecycle_mode",
                "request_mode",
                "before_status",
                "after_status",
                "satisfied",
                "satisfied_by",
                "requires_review",
                "review_only",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "schema_change_approved",
                "schema_change_allowed",
                "identity_mutation_allowed",
                "event_schema_mutation_allowed",
                "event_payload_capture_executed",
                "reconstruction_executed",
                "event_compaction_executed",
                "automatic_rollback_executed",
                "events_modified",
                "rollback",
            ):
                if key not in decision:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Reconstruction schema evidence request lifecycle decision key is missing.",
                        )
                    )
            if decision.get("request_id") not in valid_schema_evidence_request_ids:
                issues.append(
                    ValidationIssue(
                        path + ".request_id",
                        "Reconstruction schema evidence request lifecycle decision must reference a derived evidence request.",
                    )
                )
            if decision.get("action") not in {
                "satisfy",
                "defer",
                "archive",
                "quarantine",
            }:
                issues.append(
                    ValidationIssue(
                        path + ".action",
                        "Reconstruction schema evidence request lifecycle action is invalid.",
                    )
                )
            if decision.get("result") not in {
                "satisfied",
                "deferred",
                "archived",
                "quarantined",
            }:
                issues.append(
                    ValidationIssue(
                        path + ".result",
                        "Reconstruction schema evidence request lifecycle result is invalid.",
                    )
                )
            if (
                decision.get("lifecycle_mode")
                != "reconstruction_schema_evidence_request_lifecycle_v0.1"
            ):
                issues.append(
                    ValidationIssue(
                        path + ".lifecycle_mode",
                        "Reconstruction schema evidence request lifecycle mode is invalid.",
                    )
                )
            if (
                decision.get("request_mode")
                != "reconstruction_schema_review_evidence_request_v0.1"
            ):
                issues.append(
                    ValidationIssue(
                        path + ".request_mode",
                        "Reconstruction schema evidence request mode is invalid.",
                    )
                )
            if not isinstance(decision.get("evidence_refs"), list):
                issues.append(
                    ValidationIssue(
                        path + ".evidence_refs",
                        "Reconstruction schema evidence request lifecycle evidence_refs must be a list.",
                    )
                )
            if not isinstance(decision.get("satisfied_by"), list):
                issues.append(
                    ValidationIssue(
                        path + ".satisfied_by",
                        "Reconstruction schema evidence request lifecycle satisfied_by must be a list.",
                    )
                )
            if decision.get("result") == "satisfied":
                if decision.get("satisfied") is not True:
                    issues.append(
                        ValidationIssue(
                            path + ".satisfied",
                            "Satisfied evidence request lifecycle decisions must mark satisfied true.",
                        )
                    )
                if not decision.get("satisfied_by"):
                    issues.append(
                        ValidationIssue(
                            path + ".satisfied_by",
                            "Satisfied evidence request lifecycle decisions must reference satisfying evidence.",
                        )
                    )
            elif decision.get("satisfied") is not False:
                issues.append(
                    ValidationIssue(
                        path + ".satisfied",
                        "Non-satisfied evidence request lifecycle decisions must not mark satisfied true.",
                    )
                )
            for key in (
                "requires_review",
                "review_only",
                "execution_prohibited",
            ):
                if decision.get(key) is not True:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Reconstruction schema evidence request lifecycle decision must remain review-only.",
                        )
                    )
            for key in (
                "executable_policy",
                "executable_policy_created",
                "schema_change_approved",
                "schema_change_allowed",
                "identity_mutation_allowed",
                "event_schema_mutation_allowed",
                "event_payload_capture_executed",
                "reconstruction_executed",
                "event_compaction_executed",
                "automatic_rollback_executed",
                "events_modified",
            ):
                if decision.get(key) is not False:
                    issues.append(
                        ValidationIssue(
                            path + f".{key}",
                            "Reconstruction schema evidence request lifecycle decision must not execute changes.",
                        )
                    )

    raw_event_retention_reviews = task_hub.get("event_retention_reviews", [])
    event_retention_reviews = (
        raw_event_retention_reviews
        if isinstance(raw_event_retention_reviews, list)
        else []
    )
    event_retention_review_ids = {
        item.get("review_id")
        for item in event_retention_reviews
        if isinstance(item, dict) and item.get("review_id")
    }
    if isinstance(raw_event_retention_reviews, list):
        for index, review in enumerate(event_retention_reviews):
            path = f"task_hub.event_retention_reviews[{index}]"
            if not isinstance(review, dict):
                issues.append(ValidationIssue(path, "Event retention review must be an object."))
                continue
            for key in (
                "review_id",
                "timestamp",
                "reviewer",
                "status",
                "mode",
                "event_count",
                "retention",
                "review_only",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "event_compaction_executed",
                "events_modified",
                "lifecycle",
                "update_history",
            ):
                if key not in review:
                    issues.append(ValidationIssue(path + f".{key}", "Event retention review key is missing."))
            if review.get("status") not in {"passed", "needs_review"}:
                issues.append(ValidationIssue(path + ".status", "Event retention review status is invalid."))
            if review.get("mode") != "event_retention_review_v0.1":
                issues.append(ValidationIssue(path + ".mode", "Event retention review mode is invalid."))
            if review.get("review_only") is not True:
                issues.append(ValidationIssue(path + ".review_only", "Event retention review must remain review-only."))
            if review.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Event retention review must prohibit execution."))
            if review.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Event retention review must not be executable policy."))
            if review.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Event retention review must not create executable policy."))
            if review.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Event retention review must not allow Identity Core mutation."))
            if review.get("event_compaction_executed") is not False:
                issues.append(ValidationIssue(path + ".event_compaction_executed", "Event retention review must not execute compaction."))
            if review.get("events_modified") is not False:
                issues.append(ValidationIssue(path + ".events_modified", "Event retention review must not modify events."))
            lifecycle = review.get("lifecycle") if isinstance(review.get("lifecycle"), dict) else {}
            lifecycle_status = lifecycle.get("status", "active")
            if lifecycle_status not in {"active", "acknowledged", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".lifecycle.status", "Event retention review lifecycle status is invalid."))
            if lifecycle_status in {"acknowledged", "archived", "quarantined"}:
                decision_id = lifecycle.get("lifecycle_decision_id")
                if not decision_id:
                    issues.append(ValidationIssue(path + ".lifecycle.lifecycle_decision_id", "Event retention review lifecycle must reference a decision."))
                elif decision_id != review.get("last_lifecycle_decision_id"):
                    issues.append(ValidationIssue(path + ".last_lifecycle_decision_id", "Event retention review last lifecycle decision id must match lifecycle."))
                history = review.get("lifecycle_history")
                if not isinstance(history, list) or not history:
                    issues.append(ValidationIssue(path + ".lifecycle_history", "Event retention review lifecycle action requires history."))
                elif history[-1].get("decision_id") != review.get("last_lifecycle_decision_id"):
                    issues.append(ValidationIssue(path + ".lifecycle_history", "Event retention review lifecycle history must reference latest decision."))
    event_retention_lifecycle_decisions = task_hub.get("event_retention_lifecycle_decisions", [])
    if isinstance(event_retention_lifecycle_decisions, list):
        for index, decision in enumerate(event_retention_lifecycle_decisions):
            path = f"task_hub.event_retention_lifecycle_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Event retention lifecycle decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "review_id",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "review_only",
                "execution_prohibited",
                "executable_policy",
                "executable_policy_created",
                "identity_mutation_allowed",
                "event_compaction_executed",
                "events_modified",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Event retention lifecycle decision key is missing."))
            if decision.get("review_id") not in event_retention_review_ids:
                issues.append(ValidationIssue(path + ".review_id", "Event retention lifecycle decision must reference an existing review."))
            if decision.get("action") not in {"acknowledge", "archive", "quarantine"}:
                issues.append(ValidationIssue(path + ".action", "Event retention lifecycle action is invalid."))
            if decision.get("result") not in {"acknowledged", "archived", "quarantined"}:
                issues.append(ValidationIssue(path + ".result", "Event retention lifecycle result is invalid."))
            if decision.get("review_only") is not True:
                issues.append(ValidationIssue(path + ".review_only", "Event retention lifecycle decision must remain review-only."))
            if decision.get("execution_prohibited") is not True:
                issues.append(ValidationIssue(path + ".execution_prohibited", "Event retention lifecycle decision must prohibit execution."))
            if decision.get("executable_policy") is not False:
                issues.append(ValidationIssue(path + ".executable_policy", "Event retention lifecycle decision must not be executable policy."))
            if decision.get("executable_policy_created") is not False:
                issues.append(ValidationIssue(path + ".executable_policy_created", "Event retention lifecycle decision must not create executable policy."))
            if decision.get("identity_mutation_allowed") is not False:
                issues.append(ValidationIssue(path + ".identity_mutation_allowed", "Event retention lifecycle decision must not allow Identity Core mutation."))
            if decision.get("event_compaction_executed") is not False:
                issues.append(ValidationIssue(path + ".event_compaction_executed", "Event retention lifecycle decision must not execute compaction."))
            if decision.get("events_modified") is not False:
                issues.append(ValidationIssue(path + ".events_modified", "Event retention lifecycle decision must not modify events."))
    cautions = task_hub.get("cautionary_procedural_candidates", [])
    if isinstance(cautions, list):
        for index, caution in enumerate(cautions):
            path = f"task_hub.cautionary_procedural_candidates[{index}]"
            if not isinstance(caution, dict):
                issues.append(ValidationIssue(path, "Cautionary procedural candidate must be an object."))
                continue
            for key in ("candidate_id", "workflow", "statement", "avoid", "evidence", "review_status", "source_reflection_id"):
                if key not in caution:
                    issues.append(ValidationIssue(path + f".{key}", "Cautionary procedural candidate key is missing."))
            if not isinstance(caution.get("evidence"), list) or not caution.get("evidence"):
                issues.append(
                    ValidationIssue(
                        path + ".evidence",
                        "Cautionary procedural candidate requires non-empty evidence.",
                    )
                )
            if caution.get("review_status") in {"approved", "rejected", "archived", "quarantined"}:
                history = caution.get("review_history")
                if not isinstance(history, list) or not history:
                    issues.append(
                        ValidationIssue(
                            path + ".review_history",
                            "Reviewed cautionary procedural candidate requires review history.",
                        )
                    )
                elif history[-1].get("decision_id") != caution.get("last_review_decision_id"):
                    issues.append(
                        ValidationIssue(
                            path + ".last_review_decision_id",
                            "Cautionary candidate last_review_decision_id must match latest decision.",
                        )
                    )
            elif caution.get("review_status") != "pending":
                issues.append(
                    ValidationIssue(
                        path + ".review_status",
                        "Cautionary procedural candidate must be pending or reviewed.",
                    )
                )
    cautionary_memory = task_hub.get("cautionary_procedural_memory", [])
    if isinstance(cautionary_memory, list):
        for index, memory in enumerate(cautionary_memory):
            path = f"task_hub.cautionary_procedural_memory[{index}]"
            if not isinstance(memory, dict):
                issues.append(ValidationIssue(path, "Cautionary procedural memory must be an object."))
                continue
            for key in (
                "memory_id",
                "workflow",
                "statement",
                "avoid",
                "evidence",
                "status",
                "review_decision_id",
                "source_candidate_id",
                "source_reflection_id",
                "provenance",
                "lifecycle",
                "update_history",
                "executable_policy",
            ):
                if key not in memory:
                    issues.append(ValidationIssue(path + f".{key}", "Cautionary procedural memory key is missing."))
            if memory.get("executable_policy") is not False:
                issues.append(
                    ValidationIssue(
                        path + ".executable_policy",
                        "Cautionary procedural memory must not be executable policy.",
                    )
                )
            if memory.get("status") not in {
                "active",
                "archived",
                "discarded",
                "quarantined",
            }:
                issues.append(
                    ValidationIssue(
                        path + ".status",
                        "Cautionary procedural memory must have a valid lifecycle status.",
                    )
                )
            if memory.get("status") in {"archived", "discarded", "quarantined"}:
                lifecycle = memory.get("lifecycle") if isinstance(memory.get("lifecycle"), dict) else {}
                decision_id = lifecycle.get("lifecycle_decision_id")
                if not decision_id:
                    issues.append(
                        ValidationIssue(
                            path + ".lifecycle.lifecycle_decision_id",
                            "Cautionary warning lifecycle must reference a decision.",
                        )
                    )
                elif decision_id != memory.get("last_lifecycle_decision_id"):
                    issues.append(
                        ValidationIssue(
                            path + ".last_lifecycle_decision_id",
                            "Cautionary warning last_lifecycle_decision_id must match lifecycle decision.",
                        )
                    )
                history = memory.get("lifecycle_history")
                if not isinstance(history, list) or not history:
                    issues.append(
                        ValidationIssue(
                            path + ".lifecycle_history",
                            "Cautionary warning lifecycle action requires lifecycle history.",
                        )
                    )
                elif history[-1].get("decision_id") != memory.get("last_lifecycle_decision_id"):
                    issues.append(
                        ValidationIssue(
                            path + ".lifecycle_history",
                            "Cautionary warning lifecycle history must reference latest decision.",
                        )
                    )
    procedural_memory = task_hub.get("procedural_memory", [])
    if isinstance(procedural_memory, list):
        for index, memory in enumerate(procedural_memory):
            path = f"task_hub.procedural_memory[{index}]"
            if not isinstance(memory, dict):
                issues.append(ValidationIssue(path, "Procedural memory must be an object."))
                continue
            for key in (
                "memory_id",
                "workflow",
                "steps",
                "evidence",
                "status",
                "review_decision_id",
                "provenance",
                "lifecycle",
                "update_history",
            ):
                if key not in memory:
                    issues.append(ValidationIssue(path + f".{key}", "Procedural memory key is missing."))
            if memory.get("status") not in {
                "active",
                "archived",
                "discarded",
                "quarantined",
            }:
                issues.append(
                    ValidationIssue(
                        path + ".status",
                        "Procedural memory must have a valid lifecycle status.",
                    )
                )
    lifecycle_decisions = task_hub.get("procedural_lifecycle_decisions", [])
    if isinstance(lifecycle_decisions, list):
        for index, decision in enumerate(lifecycle_decisions):
            path = f"task_hub.procedural_lifecycle_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Procedural lifecycle decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "memory_id",
                "workflow",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Procedural lifecycle decision key is missing."))
            if decision.get("result") not in {"archived", "discarded", "quarantined"}:
                issues.append(
                    ValidationIssue(
                        path + ".result",
                        "Procedural lifecycle decision must resolve to an archived, discarded, or quarantined state.",
                    )
                )
    decisions = task_hub.get("procedural_review_decisions", [])
    if isinstance(decisions, list):
        for index, decision in enumerate(decisions):
            path = f"task_hub.procedural_review_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Procedural review decision must be an object."))
                continue
            for key in ("decision_id", "timestamp", "candidate_id", "workflow", "reviewer", "action", "result", "snapshot_id"):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Procedural review decision key is missing."))
    cautionary_decisions = task_hub.get("cautionary_review_decisions", [])
    if isinstance(cautionary_decisions, list):
        for index, decision in enumerate(cautionary_decisions):
            path = f"task_hub.cautionary_review_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Cautionary review decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "candidate_id",
                "workflow",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "executable_policy_created",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Cautionary review decision key is missing."))
            if decision.get("executable_policy_created") is not False:
                issues.append(
                    ValidationIssue(
                        path + ".executable_policy_created",
                        "Cautionary review must not create executable policy.",
                    )
                )
    cautionary_lifecycle_decisions = task_hub.get("cautionary_lifecycle_decisions", [])
    if isinstance(cautionary_lifecycle_decisions, list):
        for index, decision in enumerate(cautionary_lifecycle_decisions):
            path = f"task_hub.cautionary_lifecycle_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Cautionary lifecycle decision must be an object."))
                continue
            for key in (
                "decision_id",
                "timestamp",
                "memory_id",
                "workflow",
                "reviewer",
                "action",
                "result",
                "snapshot_id",
                "executable_policy_created",
            ):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Cautionary lifecycle decision key is missing."))
            if decision.get("result") not in {"archived", "discarded", "quarantined"}:
                issues.append(
                    ValidationIssue(
                        path + ".result",
                        "Cautionary lifecycle decision must resolve to archived, discarded, or quarantined.",
                    )
                )
            if decision.get("executable_policy_created") is not False:
                issues.append(
                    ValidationIssue(
                        path + ".executable_policy_created",
                        "Cautionary lifecycle must not create executable policy.",
                    )
                )
    return issues


def validate_identity_update_gate(state: dict[str, Any]) -> list[ValidationIssue]:
    gate = state.get("identity_update_gate")
    if not isinstance(gate, dict):
        return [ValidationIssue("identity_update_gate", "Identity update gate must be an object.")]

    issues: list[ValidationIssue] = []
    for key in ("proposals", "review_decisions", "drift_events"):
        if not isinstance(gate.get(key), list):
            issues.append(ValidationIssue(f"identity_update_gate.{key}", "Identity update gate key must be a list."))
    if gate.get("required_gate") != "high":
        issues.append(
            ValidationIssue(
                "identity_update_gate.required_gate",
                "Identity update gate must require high gate.",
            )
        )

    proposals = gate.get("proposals", [])
    if isinstance(proposals, list):
        for index, proposal in enumerate(proposals):
            path = f"identity_update_gate.proposals[{index}]"
            if not isinstance(proposal, dict):
                issues.append(ValidationIssue(path, "Identity proposal must be an object."))
                continue
            for key in (
                "proposal_id",
                "statement",
                "target_path",
                "evidence",
                "review_status",
                "gate_result",
                "drift_score",
                "non_claims_check",
            ):
                if key not in proposal:
                    issues.append(ValidationIssue(path + f".{key}", "Identity proposal key is missing."))
            if not isinstance(proposal.get("evidence"), list):
                issues.append(ValidationIssue(path + ".evidence", "Identity proposal evidence must be a list."))
            if proposal.get("may_update_identity_core") is not False:
                issues.append(
                    ValidationIssue(
                        path + ".may_update_identity_core",
                        "P11 proposals must not directly update Identity Core.",
                    )
                )

    decisions = gate.get("review_decisions", [])
    if isinstance(decisions, list):
        for index, decision in enumerate(decisions):
            path = f"identity_update_gate.review_decisions[{index}]"
            if not isinstance(decision, dict):
                issues.append(ValidationIssue(path, "Identity review decision must be an object."))
                continue
            for key in ("decision_id", "proposal_id", "action", "result", "snapshot_id", "gate_result"):
                if key not in decision:
                    issues.append(ValidationIssue(path + f".{key}", "Identity review decision key is missing."))
    return issues


def issue_to_dict(issue: ValidationIssue) -> dict:
    return {
        "path": issue.path,
        "message": issue.message,
        "severity": issue.severity,
    }
