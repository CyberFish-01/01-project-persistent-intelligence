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
    "adapter_event_index",
    "open_conflicts",
    "dream_queue",
    "evaluation_trace",
    "update_log",
]

REQUIRED_MEMORY_STORES = [
    "imported_memory",
    "episodic_memory",
    "semantic_memory",
    "identity_memory",
    "archived_memory",
]

REQUIRED_ANCHORS = ["who_am_i", "where_am_i", "what_am_i_doing"]


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
    issues.extend(validate_update_log(state))
    issues.extend(validate_adapter_registry(state))
    issues.extend(validate_adapter_event_index(state, episodes or []))
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


def issue_to_dict(issue: ValidationIssue) -> dict:
    return {
        "path": issue.path,
        "message": issue.message,
        "severity": issue.severity,
    }
