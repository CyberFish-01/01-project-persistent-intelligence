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
        if claim_ids and not any(endpoint in claim_ids for endpoint in endpoints):
            issues.append(
                ValidationIssue(
                    path,
                    "Claim graph link must reference at least one known claim.",
                )
            )
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
    if not isinstance(policy.get("signal_weights"), dict):
        issues.append(
            ValidationIssue(
                "context_builder.policy.signal_weights",
                "Context policy must include signal weights.",
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
