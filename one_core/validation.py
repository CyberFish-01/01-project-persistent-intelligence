from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable


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


@dataclass(frozen=True)
class ValidationIssue:
    path: str
    message: str
    severity: str = "error"


def validate_state(state: dict[str, Any], episodes: Iterable[dict] | None = None) -> dict:
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
    issues.extend(validate_snapshots(state))
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
    issues: list[ValidationIssue] = []
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

    for index, link in enumerate(links):
        path = f"claim_graph.links[{index}]"
        if not isinstance(link, dict):
            issues.append(ValidationIssue(path, "Claim graph link must be an object."))
            continue
        for key in ("from", "to", "type"):
            if key not in link:
                issues.append(ValidationIssue(path + f".{key}", "Claim graph link key is missing."))
    return issues


def issue_to_dict(issue: ValidationIssue) -> dict:
    return {
        "path": issue.path,
        "message": issue.message,
        "severity": issue.severity,
    }
