from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .schema_defaults import default_identity_update_gate
from .seed import make_identity_seed


STATE_VERSION = "1.0"
DEFAULT_STATE_DIR = Path("work/01_state")

DEFAULT_REGISTERED_ADAPTERS = (
    {
        "adapter_id": "generic_adapter",
        "display_name": "Generic Adapter",
        "enabled": True,
        "channels": ["generic_adapter"],
        "trust_level": "local",
        "notes": "Default adapter identity used by the generic Python client.",
    },
    {
        "adapter_id": "local_generic_adapter",
        "display_name": "Local Generic Adapter",
        "enabled": True,
        "channels": ["local", "local_generic_adapter"],
        "trust_level": "local",
        "notes": "Local development adapter for CLI and protocol verification.",
    },
    {
        "adapter_id": "astrbot_thin_adapter",
        "display_name": "AstrBot Thin Adapter",
        "enabled": True,
        "channels": ["astrbot"],
        "trust_level": "local",
        "notes": "Reserved thin adapter identity for AstrBot once it uses /v1/adapter/ingest.",
    },
)

SESSION_POLICY_ACTIONS = {"allow", "dry_run_only", "reject"}
MEMORY_LIFECYCLE_ACTIONS = {"archive", "discard", "quarantine"}
LIFECYCLE_ACTION_STORES = {
    "imported_memory",
    "episodic_memory",
    "candidate_memory",
    "semantic_memory",
}
IDENTITY_REVIEW_ACTIONS = {"approve", "reject", "quarantine"}
CLAIM_REVIEW_ACTIONS = {"resolve", "reject", "quarantine", "keep_open"}
PROCEDURAL_REVIEW_ACTIONS = {"approve", "reject", "archive", "quarantine"}
PROCEDURAL_LIFECYCLE_ACTIONS = {"archive", "discard", "quarantine"}
CAUTIONARY_REVIEW_ACTIONS = {"approve", "reject", "archive", "quarantine"}
CAUTIONARY_LIFECYCLE_ACTIONS = {"archive", "discard", "quarantine"}
REFLECTION_GUIDANCE_REVIEW_ACTIONS = {"acknowledge", "archive", "quarantine"}
CONTEXT_ATTRIBUTION_COVERAGE_LIFECYCLE_ACTIONS = {
    "acknowledge",
    "archive",
    "quarantine",
}
EVENT_RETENTION_LIFECYCLE_ACTIONS = {
    "acknowledge",
    "archive",
    "quarantine",
}
EVENT_PAYLOAD_CAPTURE_POLICY_REVIEW_ACTIONS = {
    "approve",
    "reject",
    "archive",
    "quarantine",
}
TOOL_SAFETY_POLICY_REVIEW_ACTIONS = {"approve", "reject", "archive", "quarantine"}
TOOL_SAFETY_POLICY_LIFECYCLE_ACTIONS = {"archive", "discard", "quarantine"}
TOOL_SAFETY_POLICY_LINK_LIFECYCLE_ACTIONS = {"archive", "discard", "quarantine"}
TOOL_SAFETY_POLICY_LINK_TYPES = {
    "supports",
    "conflicts_with",
    "supersedes",
    "overlaps",
    "depends_on",
}
REFLECTION_VERIFICATION_RESULTS = {
    "verified",
    "not_observed",
    "regressed",
    "superseded",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


def default_adapter_registry(timestamp: str) -> dict:
    adapters = {}
    for adapter in DEFAULT_REGISTERED_ADAPTERS:
        entry = dict(adapter)
        entry["registered_at"] = timestamp
        adapters[entry["adapter_id"]] = entry
    return {
        "allow_unknown_adapters": False,
        "adapters": adapters,
    }


def default_session_policy(timestamp: str) -> dict:
    return {
        "default_action": "dry_run_only",
        "rules": [
            {
                "id": "local_generic_allow",
                "adapter_id": "local_generic_adapter",
                "channels": ["local", "local_generic_adapter"],
                "action": "allow",
                "reason": "Local generic adapter is allowed for protocol verification.",
                "created_at": timestamp,
            },
            {
                "id": "generic_adapter_allow",
                "adapter_id": "generic_adapter",
                "channels": ["generic_adapter"],
                "action": "allow",
                "reason": "Generic client adapter is allowed for local development.",
                "created_at": timestamp,
            },
            {
                "id": "astrbot_private_preview",
                "adapter_id": "astrbot_thin_adapter",
                "channels": ["astrbot"],
                "action": "dry_run_only",
                "reason": "AstrBot remains a thin adapter until local protocol policy is stable.",
                "created_at": timestamp,
            },
        ],
    }


def default_claim_graph() -> dict:
    return {
        "graph_version": "0.2",
        "claims": [],
        "links": [],
        "proposal_link_evidence": [],
        "review_decisions": [],
        "policy": {
            "revision_mode": "minimal_change_preview",
            "allow_direct_memory_mutation": False,
            "allow_identity_core_mutation": False,
            "requires_review": True,
        },
    }


def default_context_policy() -> dict:
    return {
        "policy_version": "0.3",
        "mode": "bounded_state_activation",
        "budgets": {
            "episodic_memory": 5,
            "semantic_memory": 5,
            "imported_memory": 5,
            "source_attribution": 12,
            "activation_trace_history": 20,
        },
        "selection_dimensions": [
            "lifecycle_status",
            "relationship_boundary",
            "task_relevance",
            "salience",
            "confidence",
            "recency",
            "source_attribution",
            "identity_gate_signal",
            "claim_review_signal",
            "governance_evidence_signal",
            "dream_artifact_signal",
        ],
        "suppression_rules": [
            "archived_discarded_or_quarantined_memory_is_not_activated",
            "cross_user_private_episode_is_not_activated",
            "identity_memory_requires_explicit_high_gate_context",
        ],
        "signal_weights": {
            "identity_gate_evidence": 0.08,
            "claim_graph_evidence": 0.08,
            "governance_proposal_link_evidence": 0.07,
            "dream_artifact_input": 0.06,
        },
        "persistence": {
            "activation_trace_history": True,
            "context_builds_are_state_events": False,
        },
    }


def default_context_builder(timestamp: str) -> dict:
    return {
        "builder_version": "0.3",
        "policy": default_context_policy(),
        "activation_traces": [],
        "attribution_coverage_reviews": [],
        "attribution_coverage_lifecycle_decisions": [],
        "last_context_package_id": None,
        "created_at": timestamp,
        "updated_at": timestamp,
    }


def default_task_hub(timestamp: str, working_state: Optional[dict] = None) -> dict:
    tasks = tasks_from_current_plan(working_state or {}, timestamp)
    return {
        "active_tasks": [
            task
            for task in tasks
            if task.get("status") in {"active", "pending", "in_progress"}
        ],
        "completed_tasks": [
            task for task in tasks if task.get("status") == "completed"
        ],
        "blocked_tasks": [
            task for task in tasks if task.get("status") == "blocked"
        ],
        "recurring_duties": [],
        "action_trace": [],
        "reflection_log": [],
        "reflection_guidance_queue": [],
        "reflection_guidance_decisions": [],
        "tool_safety_policy_proposals": [],
        "tool_safety_policy_links": [],
        "tool_safety_policy_link_lifecycle_decisions": [],
        "tool_safety_policy_decisions": [],
        "tool_safety_policy_lifecycle_decisions": [],
        "event_retention_reviews": [],
        "event_retention_lifecycle_decisions": [],
        "event_payload_capture_policy_proposals": [],
        "event_payload_capture_policy_decisions": [],
        "failure_reflections": [],
        "procedural_candidates": [],
        "cautionary_procedural_candidates": [],
        "cautionary_procedural_memory": [],
        "cautionary_review_decisions": [],
        "cautionary_lifecycle_decisions": [],
        "procedural_memory": [],
        "procedural_lifecycle_decisions": [],
        "procedural_review_decisions": [],
    }


def tasks_from_current_plan(working_state: dict, timestamp: str) -> List[dict]:
    tasks = []
    current_plan = working_state.get("current_plan", [])
    if not isinstance(current_plan, list):
        return tasks
    for index, item in enumerate(current_plan):
        if not isinstance(item, dict):
            continue
        title = str(item.get("step") or item.get("title") or "").strip()
        if not title:
            continue
        raw_status = str(item.get("status") or "pending").strip().lower()
        status = normalize_task_status(raw_status)
        tasks.append(
            {
                "task_id": new_id("task"),
                "title": title,
                "status": status,
                "created_at": timestamp,
                "updated_at": timestamp,
                "source": "working_state.current_plan",
                "source_index": index,
                "source_key": task_source_key(index=index, title=title),
                "evidence": ["working_state.current_plan"],
            }
        )
    return tasks


def normalize_task_status(status: str) -> str:
    if status in {"done", "complete", "completed"}:
        return "completed"
    if status in {"active", "pending", "in_progress"}:
        return status
    if status in {"blocked", "stalled"}:
        return "blocked"
    return "pending"


def task_source_key(index: int, title: str) -> str:
    normalized = re.sub(r"\s+", " ", title.strip().lower())
    return f"working_state.current_plan:{index}:{normalized}"


def default_lifecycle(
    status: str,
    timestamp: str,
    review_status: str = "unreviewed",
) -> dict:
    return {
        "status": status,
        "created_at": timestamp,
        "last_reviewed_at": None,
        "review_status": review_status,
    }


def active_memory_items(items: List[dict]) -> List[dict]:
    return [
        item
        for item in items
        if item.get("lifecycle", {}).get("status", "active") == "active"
    ]


def next_actions_from_plan(current_plan: List[dict]) -> List[dict]:
    return [
        item
        for item in current_plan
        if item.get("status") in {"active", "pending", "in_progress"}
    ][:3]


def ensure_memory_lifecycle_metadata(state: dict, timestamp: str) -> bool:
    changed = False
    memory_stores = state.setdefault("memory_stores", {})
    defaults = {
        "imported_memory": ("staged", "staged"),
        "episodic_memory": ("active", "unreviewed"),
        "candidate_memory": ("candidate", "pending"),
        "semantic_memory": ("active", "unreviewed"),
        "identity_memory": ("active", "unreviewed"),
        "archived_memory": ("archived", "archived"),
    }
    for store_name, (status, review_status) in defaults.items():
        memories = memory_stores.get(store_name, [])
        if not isinstance(memories, list):
            continue
        for memory in memories:
            if not isinstance(memory, dict):
                continue
            memory_timestamp = str(
                memory.get("timestamp")
                or memory.get("last_verified_at")
                or timestamp
            )
            if "lifecycle" not in memory:
                memory["lifecycle"] = default_lifecycle(
                    status=status,
                    timestamp=memory_timestamp,
                    review_status=review_status,
                )
                changed = True
            if "provenance" not in memory:
                memory["provenance"] = inferred_memory_provenance(
                    store_name=store_name,
                    memory=memory,
                )
                changed = True
            if "update_history" not in memory:
                memory["update_history"] = [
                    {
                        "timestamp": memory_timestamp,
                        "actor": "state_store",
                        "operation": "migrate_memory_metadata",
                        "evidence": memory.get("derived_from", [])
                        or memory.get("promoted_to", [])
                        or [memory.get("id", store_name)],
                    }
                ]
                changed = True
            if store_name == "candidate_memory" and "review_history" not in memory:
                memory["review_history"] = []
                changed = True
    return changed


def ensure_candidate_review_decision_metadata(state: dict, timestamp: str) -> bool:
    changed = False
    candidates = (
        state.setdefault("memory_stores", {})
        .setdefault("candidate_memory", [])
    )
    if not isinstance(candidates, list):
        return False
    for candidate in candidates:
        if not isinstance(candidate, dict):
            continue
        if candidate.get("status") in {"candidate", "pending", None}:
            continue
        review_history = candidate.setdefault("review_history", [])
        if not isinstance(review_history, list):
            candidate["review_history"] = []
            review_history = candidate["review_history"]
            changed = True
        latest = review_history[-1] if review_history else {}
        if not isinstance(latest, dict) or "decision_id" not in latest:
            snapshot = build_legacy_review_snapshot(
                state=state,
                candidate=candidate,
                timestamp=timestamp,
            )
            state.setdefault("snapshots", []).append(snapshot)
            state["snapshots"] = state["snapshots"][-50:]
            decision = build_candidate_review_decision(
                candidate=candidate,
                action=str(candidate.get("review_status") or candidate.get("status")),
                reviewer=str(candidate.get("reviewer") or "state_store_migration"),
                decision_note=str(
                    candidate.get("decision_note")
                    or "Migrated legacy candidate review decision."
                ),
                timestamp=str(candidate.get("reviewed_at") or timestamp),
            )
            decision["result"] = str(candidate.get("review_status") or candidate.get("status"))
            decision["snapshot_id"] = snapshot["snapshot_id"]
            decision["target_path"] = "memory_stores.candidate_memory"
            snapshot["metadata"]["review_decision_id"] = decision["decision_id"]
            review_history.append(decision)
            latest = decision
            changed = True
        decision_id = latest.get("decision_id")
        if candidate.get("last_review_decision_id") != decision_id:
            candidate["last_review_decision_id"] = decision_id
            changed = True
        lifecycle = candidate.setdefault("lifecycle", default_lifecycle(
            status=str(candidate.get("status") or "candidate"),
            timestamp=str(candidate.get("timestamp") or timestamp),
            review_status=str(candidate.get("review_status") or "pending"),
        ))
        if isinstance(lifecycle, dict) and lifecycle.get("review_decision_id") != decision_id:
            lifecycle["review_decision_id"] = decision_id
            changed = True
    return changed


def ensure_claim_graph(state: dict, timestamp: str) -> bool:
    changed = False
    claim_graph = state.get("claim_graph")
    if not isinstance(claim_graph, dict):
        state["claim_graph"] = default_claim_graph()
        claim_graph = state["claim_graph"]
        changed = True
    if not isinstance(claim_graph.get("claims"), list):
        claim_graph["claims"] = []
        changed = True
    if not isinstance(claim_graph.get("links"), list):
        claim_graph["links"] = []
        changed = True
    if not isinstance(claim_graph.get("proposal_link_evidence"), list):
        claim_graph["proposal_link_evidence"] = []
        changed = True
    default_graph = default_claim_graph()
    for key in ("graph_version", "policy", "proposal_link_evidence", "review_decisions"):
        if key not in claim_graph:
            claim_graph[key] = default_graph[key]
            changed = True
    if not isinstance(claim_graph.get("proposal_link_evidence"), list):
        claim_graph["proposal_link_evidence"] = []
        changed = True
    if not isinstance(claim_graph.get("review_decisions"), list):
        claim_graph["review_decisions"] = []
        changed = True
    if not isinstance(claim_graph.get("policy"), dict):
        claim_graph["policy"] = default_graph["policy"]
        changed = True
    else:
        for key, value in default_graph["policy"].items():
            if key not in claim_graph["policy"]:
                claim_graph["policy"][key] = value
                changed = True
    for conflict in state.get("open_conflicts", []):
        if not isinstance(conflict, dict):
            continue
        claim = build_claim_from_conflict(
            conflict=conflict,
            source="state_migration",
            timestamp=timestamp,
        )
        if add_claim_to_graph(claim_graph, claim):
            changed = True
    return changed


def ensure_context_builder(state: dict, timestamp: str) -> bool:
    changed = False
    default_builder = default_context_builder(timestamp)
    context_builder = state.get("context_builder")
    if not isinstance(context_builder, dict):
        state["context_builder"] = default_builder
        return True

    for key, value in default_builder.items():
        if key not in context_builder:
            context_builder[key] = value
            changed = True

    policy = context_builder.get("policy")
    default_policy = default_context_policy()
    if not isinstance(policy, dict):
        context_builder["policy"] = default_policy
        changed = True
    else:
        for key, value in default_policy.items():
            if key not in policy:
                policy[key] = value
                changed = True
        budgets = policy.get("budgets")
        if not isinstance(budgets, dict):
            policy["budgets"] = default_policy["budgets"]
            changed = True
        else:
            for key, value in default_policy["budgets"].items():
                if key not in budgets:
                    budgets[key] = value
                    changed = True
        dimensions = policy.get("selection_dimensions")
        if not isinstance(dimensions, list):
            policy["selection_dimensions"] = list(default_policy["selection_dimensions"])
            changed = True
        else:
            for dimension in default_policy["selection_dimensions"]:
                if dimension not in dimensions:
                    dimensions.append(dimension)
                    changed = True
        signal_weights = policy.get("signal_weights")
        if not isinstance(signal_weights, dict):
            policy["signal_weights"] = default_policy["signal_weights"]
            changed = True
        else:
            for key, value in default_policy["signal_weights"].items():
                if key not in signal_weights:
                    signal_weights[key] = value
                    changed = True
        persistence = policy.get("persistence")
        if not isinstance(persistence, dict):
            policy["persistence"] = default_policy["persistence"]
            changed = True
        else:
            for key, value in default_policy["persistence"].items():
                if key not in persistence:
                    persistence[key] = value
                    changed = True

    traces = context_builder.get("activation_traces")
    if not isinstance(traces, list):
        context_builder["activation_traces"] = []
        changed = True
    else:
        budget = int(
            context_builder.get("policy", {})
            .get("budgets", {})
            .get("activation_trace_history", 20)
        )
        if len(traces) > budget:
            context_builder["activation_traces"] = traces[-budget:]
            changed = True
    reviews = context_builder.get("attribution_coverage_reviews")
    if not isinstance(reviews, list):
        context_builder["attribution_coverage_reviews"] = []
        changed = True
        reviews = context_builder["attribution_coverage_reviews"]
    for review in reviews:
        if not isinstance(review, dict):
            continue
        review_id = str(review.get("review_id") or "context_attribution_coverage_review")
        created_at = str(review.get("timestamp") or timestamp)
        if not isinstance(review.get("lifecycle"), dict):
            review["lifecycle"] = default_lifecycle(
                status="active",
                timestamp=created_at,
                review_status=str(review.get("status") or "pending"),
            )
            changed = True
        if not isinstance(review.get("review_history"), list):
            review["review_history"] = []
            changed = True
        if not isinstance(review.get("lifecycle_history"), list):
            review["lifecycle_history"] = []
            changed = True
        if not isinstance(review.get("update_history"), list):
            review["update_history"] = [
                {
                    "timestamp": created_at,
                    "actor": str(review.get("reviewer") or "state_store"),
                    "operation": "review_context_attribution_coverage",
                    "evidence": review.get("evidence", []) or [review_id],
                }
            ]
            changed = True
        for key, expected in (
            ("review_only", True),
            ("execution_prohibited", True),
            ("executable_policy", False),
            ("executable_policy_created", False),
            ("identity_mutation_allowed", False),
        ):
            if review.get(key) is not expected:
                review[key] = expected
                changed = True
    lifecycle_decisions = context_builder.get(
        "attribution_coverage_lifecycle_decisions"
    )
    if not isinstance(lifecycle_decisions, list):
        context_builder["attribution_coverage_lifecycle_decisions"] = []
        changed = True
    context_builder["updated_at"] = context_builder.get("updated_at") or timestamp
    return changed


def ensure_task_hub(state: dict, timestamp: str) -> bool:
    changed = False
    working_state = state.get("working_state", {})
    task_hub = state.get("task_hub")
    if not isinstance(task_hub, dict):
        state["task_hub"] = default_task_hub(timestamp, working_state)
        return True

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
            task_hub[key] = []
            changed = True

    for proposal in task_hub.get("tool_safety_policy_proposals", []):
        if not isinstance(proposal, dict):
            continue
        if "status" not in proposal:
            proposal["status"] = "active"
            changed = True
        if not isinstance(proposal.get("lifecycle"), dict):
            proposal["lifecycle"] = {
                "status": proposal.get("status", "active"),
                "created_at": proposal.get("timestamp", timestamp),
                "last_reviewed_at": proposal.get("reviewed_at"),
                "review_status": proposal.get("review_status", "pending"),
            }
            changed = True
        if "update_history" not in proposal:
            proposal["update_history"] = []
            changed = True
        if not isinstance(proposal.get("proposal_score"), dict):
            proposal["proposal_score"] = score_tool_safety_policy_proposal(
                proposal,
                timestamp=timestamp,
            )
            changed = True

    existing_source_keys = {
        str(task.get("source_key"))
        for bucket in (
            task_hub["active_tasks"],
            task_hub["completed_tasks"],
            task_hub["blocked_tasks"],
        )
        for task in bucket
        if isinstance(task, dict) and task.get("source_key")
    }
    for task in tasks_from_current_plan(working_state, timestamp):
        if task["source_key"] in existing_source_keys:
            continue
        if task["status"] == "completed":
            task_hub["completed_tasks"].append(task)
        elif task["status"] == "blocked":
            task_hub["blocked_tasks"].append(task)
        else:
            task_hub["active_tasks"].append(task)
        changed = True

    if len(task_hub["action_trace"]) > 200:
        task_hub["action_trace"] = task_hub["action_trace"][-200:]
        changed = True
    return changed


def ensure_identity_update_gate(state: dict, timestamp: str) -> bool:
    gate = state.get("identity_update_gate")
    if not isinstance(gate, dict):
        state["identity_update_gate"] = default_identity_update_gate(timestamp)
        return True

    changed = False
    default_gate = default_identity_update_gate(timestamp)
    for key, value in default_gate.items():
        if key not in gate:
            gate[key] = value
            changed = True
    for key in ("proposals", "review_decisions", "drift_events"):
        if not isinstance(gate.get(key), list):
            gate[key] = []
            changed = True
    if not isinstance(gate.get("policy"), dict):
        gate["policy"] = default_gate["policy"]
        changed = True
    else:
        for key, value in default_gate["policy"].items():
            if key not in gate["policy"]:
                gate["policy"][key] = value
                changed = True
    return changed


def append_task_action_trace(state: dict, trace: dict, status: str = "completed") -> dict:
    timestamp = str(trace.get("ended_at") or trace.get("started_at") or utc_now())
    action = {
        "action_id": new_id("action"),
        "trace_id": trace["trace_id"],
        "timestamp": timestamp,
        "workflow": trace.get("workflow", ""),
        "status": status,
        "summary": trace.get("summary", ""),
        "audit_event_ids": trace.get("audit_event_ids", []),
        "memory_events": trace.get("memory_events", []),
        "review_events": trace.get("review_events", []),
        "errors": trace.get("errors", []),
        "evidence": task_action_evidence(trace),
    }
    task_hub = state.setdefault(
        "task_hub",
        default_task_hub(timestamp, state.get("working_state", {})),
    )
    task_hub.setdefault("action_trace", []).append(action)
    task_hub["action_trace"] = task_hub["action_trace"][-200:]
    return action


def task_action_evidence(trace: dict) -> List[str]:
    evidence: List[str] = []
    for event in trace.get("memory_events", []):
        if not isinstance(event, dict):
            continue
        for key in (
            "memory_id",
            "episode_id",
            "candidate_id",
            "semantic_memory_id",
            "procedural_memory_id",
            "lifecycle_decision_id",
            "procedural_lifecycle_decision_id",
            "cautionary_memory_id",
            "cautionary_decision_id",
            "cautionary_lifecycle_decision_id",
            "reflection_id",
            "reflection_verification_id",
            "event_retention_review_id",
            "event_retention_lifecycle_decision_id",
            "event_payload_capture_policy_proposal_id",
            "event_payload_capture_policy_decision_id",
        ):
            value = event.get(key)
            if value:
                evidence.append(str(value))
        for key in ("memory_ids", "episodes", "imports"):
            values = event.get(key)
            if isinstance(values, list):
                evidence.extend(str(value) for value in values if value)
    evidence.extend(str(value) for value in trace.get("audit_event_ids", []) if value)
    seen = set()
    deduped = []
    for item in evidence:
        if item in seen:
            continue
        seen.add(item)
        deduped.append(item)
    return deduped


def evaluate_identity_gate(
    state: dict,
    statement: str,
    evidence: List[str],
    target_path: str,
    confidence: float,
) -> dict:
    gate = state.get("identity_update_gate", {})
    policy = gate.get("policy", {}) if isinstance(gate, dict) else {}
    required_count = int(
        gate.get("min_supporting_evidence")
        or state.get("identity_core", {})
        .get("update_policy", {})
        .get("min_supporting_episodes", 3)
    )
    evidence_ids = [str(item) for item in evidence if item]
    known_evidence = known_memory_ids(state)
    missing_evidence = [
        item for item in evidence_ids if item not in known_evidence and not item.startswith("identity_seed")
    ]
    non_claims = identity_non_claims_check(statement)
    drift = identity_drift_score(
        state=state,
        statement=statement,
        confidence=confidence,
        evidence_count=len(evidence_ids),
        non_claims_check=non_claims,
        target_path=target_path,
    )
    target_allowed = target_path == policy.get(
        "approved_target",
        "memory_stores.identity_memory",
    )
    reasons = []
    if len(evidence_ids) < required_count:
        reasons.append("insufficient_evidence")
    if missing_evidence:
        reasons.append("unknown_evidence")
    if not non_claims["passed"]:
        reasons.append("non_claims_violation")
    if not target_allowed:
        reasons.append("identity_core_patch_blocked")
    if drift["score"] > float(policy.get("drift_threshold", 0.35)):
        reasons.append("drift_score_too_high")
    eligible = not reasons
    return {
        "eligible": eligible,
        "required_evidence_count": required_count,
        "evidence_count": len(evidence_ids),
        "missing_evidence": missing_evidence,
        "target_allowed": target_allowed,
        "non_claims_check": non_claims,
        "drift_score": drift,
        "reasons": reasons,
    }


def known_memory_ids(state: dict) -> set[str]:
    ids = set()
    for memories in state.get("memory_stores", {}).values():
        if not isinstance(memories, list):
            continue
        for memory in memories:
            if isinstance(memory, dict) and memory.get("id"):
                ids.add(str(memory["id"]))
    for action in state.get("task_hub", {}).get("action_trace", []):
        if isinstance(action, dict) and action.get("action_id"):
            ids.add(str(action["action_id"]))
    for claim in state.get("claim_graph", {}).get("claims", []):
        if isinstance(claim, dict) and claim.get("claim_id"):
            ids.add(str(claim["claim_id"]))
    return ids


def identity_non_claims_check(statement: str) -> dict:
    lowered = statement.lower()
    banned = [
        ("biological emotion", "biological_emotion_claim"),
        ("conscious", "consciousness_claim"),
        ("sentient", "sentience_claim"),
        ("human", "human_identity_claim"),
        ("生物情绪", "biological_emotion_claim"),
        ("意识", "consciousness_claim"),
        ("人类", "human_identity_claim"),
    ]
    violations = [
        code
        for marker, code in banned
        if marker in lowered or marker in statement
    ]
    return {
        "passed": not violations,
        "violations": violations,
    }


def identity_drift_score(
    state: dict,
    statement: str,
    confidence: float,
    evidence_count: int,
    non_claims_check: dict,
    target_path: str,
) -> dict:
    score = 0.05
    factors = [{"name": "base_identity_change_risk", "value": 0.05}]
    lowered = statement.lower()
    overwrite_markers = [
        "not 01",
        "不是01",
        "replace identity",
        "真实身份改成",
        "完全不同",
    ]
    if any(marker in lowered or marker in statement for marker in overwrite_markers):
        score += 0.45
        factors.append({"name": "identity_overwrite_marker", "value": 0.45})
    if target_path != "memory_stores.identity_memory":
        score += 0.3
        factors.append({"name": "identity_core_patch_target", "value": 0.3})
    if not non_claims_check.get("passed"):
        score += 0.4
        factors.append({"name": "non_claims_violation", "value": 0.4})
    if evidence_count < 3:
        penalty = (3 - evidence_count) * 0.12
        score += penalty
        factors.append({"name": "evidence_shortfall", "value": round(penalty, 2)})
    confidence_value = max(0.0, min(float(confidence or 0.0), 1.0))
    if confidence_value < 0.7:
        score += 0.08
        factors.append({"name": "low_confidence", "value": 0.08})
    bounded = round(max(0.0, min(score, 1.0)), 2)
    risk = "low" if bounded <= 0.25 else "medium" if bounded <= 0.45 else "high"
    return {
        "score": bounded,
        "risk": risk,
        "factors": factors,
    }


def state_updates_with_ids(state: dict) -> List[dict]:
    updates = state.get("update_log", [])
    if not isinstance(updates, list):
        return []
    return [
        update
        for update in updates
        if isinstance(update, dict) and update.get("id")
    ]


def current_memory_counts(state: dict) -> dict:
    return {
        name: len(values)
        for name, values in state.get("memory_stores", {}).items()
        if isinstance(values, list)
    }


def target_path_current_count(state: dict, target_path: str) -> Optional[int]:
    parts = str(target_path or "").split(".")
    if not parts:
        return None
    value: object = state
    for part in parts:
        if not isinstance(value, dict) or part not in value:
            return None
        value = value[part]
    if isinstance(value, list):
        return len(value)
    return None


def operation_class_for(operation: object) -> str:
    normalized = str(operation or "").strip().lower()
    if not normalized:
        return "unknown"
    prefix = normalized.split("_", 1)[0]
    if normalized == "no_write":
        return "no_write"
    if prefix in {
        "append",
        "record",
        "create",
        "promote",
        "propose",
        "verify",
        "link",
        "bridge",
    }:
        return prefix
    if prefix in {"approve", "reject", "acknowledge"}:
        return "review_decision"
    if prefix in {"archive", "discard", "quarantine"}:
        return "lifecycle_transition"
    return "state_transition"


def scalar_state_ref(value: object) -> Optional[str]:
    if isinstance(value, str) and value:
        return value
    if isinstance(value, (int, float, bool)):
        return str(value)
    return None


def target_identity_for(update: dict) -> Optional[str]:
    operation = str(update.get("operation") or "").strip().lower()
    target_path = str(update.get("target_path") or "")
    event_retention_lifecycle = (
        target_path == "task_hub.event_retention_reviews"
        and operation in {
            "acknowledge_event_retention_review",
            "archive_event_retention_review",
            "quarantine_event_retention_review",
        }
    )
    event_payload_capture_policy_review = (
        target_path == "task_hub.event_payload_capture_policy_proposals"
        and operation in {
            "approve_event_payload_capture_policy",
            "reject_event_payload_capture_policy",
            "archive_event_payload_capture_policy",
            "quarantine_event_payload_capture_policy",
        }
    )
    if (
        operation_class_for(update.get("operation")) == "lifecycle_transition"
        or event_retention_lifecycle
        or event_payload_capture_policy_review
    ):
        evidence_identity = next(
            (
                str(item)
                for item in update.get("evidence", [])
                if isinstance(item, (str, int, float, bool)) and str(item)
            ),
            None,
        )
        if evidence_identity:
            return evidence_identity
    return (
        scalar_state_ref(update.get("after"))
        or scalar_state_ref(update.get("before"))
        or next(
            (
                str(item)
                for item in update.get("evidence", [])
                if isinstance(item, (str, int, float, bool)) and str(item)
            ),
            None,
        )
    )


def last_update_for_trace(state: dict, trace: dict) -> Optional[dict]:
    updates = state_updates_with_ids(state)
    if not updates:
        return None
    referenced_ids = trace_referenced_update_ids(trace)
    if referenced_ids:
        for update in reversed(updates):
            if update.get("id") in referenced_ids:
                return update
    workflow = trace.get("workflow")
    if workflow == "record_episode":
        for update in reversed(updates):
            if (
                update.get("operation") == "append"
                and update.get("target_path") == "memory_stores.episodic_memory"
            ):
                return update
    return updates[-1]


def trace_referenced_update_ids(trace: dict) -> set[str]:
    ids = set()
    for group_name in ("memory_events", "review_events"):
        group = trace.get(group_name, [])
        if not isinstance(group, list):
            continue
        for item in group:
            if not isinstance(item, dict):
                continue
            for key in ("update_id", "state_update_id"):
                if item.get(key):
                    ids.add(str(item[key]))
            nested = item.get("review_decision") or item.get("identity_decision")
            if isinstance(nested, dict) and nested.get("update_id"):
                ids.add(str(nested["update_id"]))
    return ids


def build_state_event(state: dict, trace: dict, update: dict, sequence: int) -> dict:
    return {
        "event_id": new_id("event"),
        "sequence": sequence,
        "timestamp": trace.get("ended_at") or trace.get("started_at") or utc_now(),
        "event_type": "state_transition",
        "state_version": state.get("state_version"),
        "workflow": trace.get("workflow"),
        "trace_id": trace.get("trace_id"),
        "audit_event_ids": trace.get("audit_event_ids", []),
        "update_id": update.get("id"),
        "actor": update.get("actor"),
        "operation": update.get("operation"),
        "operation_class": operation_class_for(update.get("operation")),
        "target_path": update.get("target_path"),
        "target_identity": target_identity_for(update),
        "before": update.get("before"),
        "after": update.get("after"),
        "evidence": update.get("evidence", []),
        "gate": update.get("gate"),
        "confidence": update.get("confidence"),
        "rollback": update.get("rollback", {}),
        "memory_events": trace.get("memory_events", []),
        "review_events": trace.get("review_events", []),
        "summary": trace.get("summary", ""),
    }


def should_update_have_event(update: dict) -> bool:
    if update.get("operation") in {"init", "migrate"}:
        return False
    if update.get("actor") == "state_store":
        return False
    return True


def workflow_counts(events: List[dict]) -> dict:
    counts: dict[str, int] = {}
    for event in events:
        workflow = str(event.get("workflow") or "unknown")
        counts[workflow] = counts.get(workflow, 0) + 1
    return counts


def target_path_counts(events: List[dict]) -> dict:
    counts: dict[str, int] = {}
    for event in events:
        target = str(event.get("target_path") or "unknown")
        counts[target] = counts.get(target, 0) + 1
    return counts


def event_operation_counts(events: List[dict]) -> dict:
    counts: dict[str, int] = {}
    for event in events:
        operation = str(event.get("operation") or "unknown")
        counts[operation] = counts.get(operation, 0) + 1
    return counts


def event_sequence_sort_key(event: dict) -> int:
    sequence = event.get("sequence")
    return sequence if isinstance(sequence, int) else 0


def build_event_replay_projection(events: List[dict]) -> dict:
    target_paths: dict[str, dict] = {}
    rollback_snapshots: dict[str, dict] = {}
    unrebuildable_event_ids: List[str] = []
    last_sequence = 0
    sequence_gap_count = 0

    for event in sorted(events, key=event_sequence_sort_key):
        event_id = str(event.get("event_id") or "unknown_event")
        sequence = event.get("sequence")
        target_path = str(event.get("target_path") or "")
        operation = str(event.get("operation") or "")
        operation_class = str(
            event.get("operation_class") or operation_class_for(operation)
        )
        target_identity = scalar_state_ref(event.get("target_identity"))
        if target_identity is None:
            target_identity = (
                scalar_state_ref(event.get("after"))
                or scalar_state_ref(event.get("before"))
            )
        if not isinstance(sequence, int) or not target_path or not operation:
            unrebuildable_event_ids.append(event_id)
            continue
        if sequence != last_sequence + 1:
            sequence_gap_count += 1
        last_sequence = sequence

        target = target_paths.setdefault(
            target_path,
            {
                "event_count": 0,
                "operation_counts": {},
                "operation_class_counts": {},
                "after_ids": [],
                "target_identities": [],
                "latest_after": None,
                "latest_target_identity": None,
                "latest_event_id": None,
                "latest_update_id": None,
                "rollback_snapshot_ids": [],
            },
        )
        target["event_count"] += 1
        target["operation_counts"][operation] = (
            target["operation_counts"].get(operation, 0) + 1
        )
        target["operation_class_counts"][operation_class] = (
            target["operation_class_counts"].get(operation_class, 0) + 1
        )
        after = event.get("after")
        if after is not None:
            target["latest_after"] = after
            if isinstance(after, str) and after not in target["after_ids"]:
                target["after_ids"].append(after)
        if target_identity:
            target["latest_target_identity"] = target_identity
            if target_identity not in target["target_identities"]:
                target["target_identities"].append(target_identity)
        target["latest_event_id"] = event_id
        target["latest_update_id"] = event.get("update_id")

        snapshot_id = event.get("rollback", {}).get("snapshot_id")
        if snapshot_id:
            snapshot_key = str(snapshot_id)
            if snapshot_key not in target["rollback_snapshot_ids"]:
                target["rollback_snapshot_ids"].append(snapshot_key)
            rollback = rollback_snapshots.setdefault(
                snapshot_key,
                {
                    "event_ids": [],
                    "update_ids": [],
                    "target_paths": [],
                },
            )
            rollback["event_ids"].append(event_id)
            if event.get("update_id"):
                rollback["update_ids"].append(str(event["update_id"]))
            if target_path not in rollback["target_paths"]:
                rollback["target_paths"].append(target_path)

    for target in target_paths.values():
        target["after_count"] = len(target["after_ids"])
        target["target_identity_count"] = len(target["target_identities"])

    return {
        "projection_mode": "target_path_transition_projection_v0.2",
        "rebuildable_event_count": len(events) - len(unrebuildable_event_ids),
        "target_paths": target_paths,
        "rollback_snapshots": rollback_snapshots,
        "sequence_gap_count": sequence_gap_count,
        "unrebuildable_event_ids": unrebuildable_event_ids,
        "full_state_rebuild": False,
        "note": "Projection rebuilds target-path transition references from events; it does not recreate full state objects.",
    }


def validate_event_replay_projection(state: dict, projection: dict) -> dict:
    checked: dict[str, dict] = {}
    unchecked: List[str] = []
    mismatches: List[dict] = []
    for target_path, projected in projection.get("target_paths", {}).items():
        current_count = target_path_current_count(state, target_path)
        if current_count is None:
            unchecked.append(target_path)
            continue
        projected_count = int(projected.get("target_identity_count", 0))
        coverage_gap_count = current_count - projected_count
        record = {
            "current_count": current_count,
            "projected_target_identity_count": projected_count,
            "coverage_gap_count": max(coverage_gap_count, 0),
            "full_count_match": current_count == projected_count,
            "count_consistent": projected_count <= current_count,
        }
        checked[target_path] = record
        if not record["count_consistent"]:
            mismatches.append(
                {
                    "target_path": target_path,
                    **record,
                }
            )
    return {
        "mode": "target_path_count_validation_v0.1",
        "checked_target_path_count": len(checked),
        "matched_target_path_count": sum(
            1 for record in checked.values() if record["full_count_match"]
        ),
        "consistent_target_path_count": sum(
            1 for record in checked.values() if record["count_consistent"]
        ),
        "checked": checked,
        "unchecked_target_paths": sorted(unchecked),
        "count_mismatches": mismatches,
        "report_only": True,
    }


PAYLOAD_HINT_KEYS = {
    "payload",
    "review",
    "decision",
    "identity_decision",
    "review_decision",
    "event_retention_lifecycle_decision",
    "proposal",
    "candidate",
    "reflection",
    "memory",
    "episode",
    "artifact",
}

DIFF_HINT_KEYS = {
    "diff",
    "patch_diff",
    "state_diff",
    "object_diff",
    "payload_diff",
}


def structured_payload(value: object) -> bool:
    return isinstance(value, (dict, list)) and bool(value)


def contains_nested_key(value: object, keys: set[str], depth: int = 0) -> bool:
    if depth > 5:
        return False
    if isinstance(value, dict):
        if any(key in value and value.get(key) is not None for key in keys):
            return True
        return any(
            contains_nested_key(item, keys, depth + 1)
            for item in value.values()
            if isinstance(item, (dict, list))
        )
    if isinstance(value, list):
        return any(
            contains_nested_key(item, keys, depth + 1)
            for item in value
            if isinstance(item, (dict, list))
        )
    return False


def event_transition_reference_complete(event: dict) -> bool:
    if not isinstance(event.get("sequence"), int):
        return False
    if not event.get("event_id") or not event.get("operation") or not event.get("target_path"):
        return False
    return bool(
        event.get("target_identity")
        or scalar_state_ref(event.get("after"))
        or scalar_state_ref(event.get("before"))
        or event.get("evidence")
    )


def build_event_payload_diff_coverage(events: List[dict]) -> dict:
    event_records = []
    target_paths: dict[str, dict] = {}
    workflow_counts_by_status: dict[str, dict] = {}

    for event in sorted(events, key=event_sequence_sort_key):
        target_path = str(event.get("target_path") or "unknown")
        workflow = str(event.get("workflow") or "unknown")
        before_is_object = structured_payload(event.get("before"))
        after_is_object = structured_payload(event.get("after"))
        before_after_object_pair = before_is_object and after_is_object
        explicit_diff = contains_nested_key(event, DIFF_HINT_KEYS)
        payload_hint = (
            before_is_object
            or after_is_object
            or contains_nested_key(event.get("memory_events", []), PAYLOAD_HINT_KEYS)
            or contains_nested_key(event.get("review_events", []), PAYLOAD_HINT_KEYS)
        )
        transition_complete = event_transition_reference_complete(event)
        rollback_snapshot_id = event.get("rollback", {}).get("snapshot_id")
        diff_ready = explicit_diff or before_after_object_pair

        if diff_ready:
            payload_status = "diff_ready"
            preservation_risk = "low"
        elif payload_hint:
            payload_status = "payload_hint_only"
            preservation_risk = "medium"
        elif transition_complete:
            payload_status = "reference_only"
            preservation_risk = "medium"
        else:
            payload_status = "missing_transition_reference"
            preservation_risk = "high"

        missing_capabilities = []
        if not transition_complete:
            missing_capabilities.append("transition_reference")
        if not payload_hint:
            missing_capabilities.append("object_payload")
        if not diff_ready:
            missing_capabilities.append("object_diff")
        if not rollback_snapshot_id:
            missing_capabilities.append("rollback_snapshot")

        record = {
            "event_id": event.get("event_id"),
            "sequence": event.get("sequence"),
            "workflow": workflow,
            "operation": event.get("operation"),
            "operation_class": event.get("operation_class"),
            "target_path": target_path,
            "target_identity": event.get("target_identity"),
            "transition_reference_complete": transition_complete,
            "payload_hint": payload_hint,
            "explicit_diff": explicit_diff,
            "before_after_object_pair": before_after_object_pair,
            "rollback_snapshot_id": rollback_snapshot_id,
            "payload_status": payload_status,
            "preservation_risk": preservation_risk,
            "missing_capabilities": missing_capabilities,
        }
        event_records.append(record)

        target = target_paths.setdefault(
            target_path,
            {
                "event_count": 0,
                "transition_reference_count": 0,
                "payload_hint_count": 0,
                "explicit_diff_count": 0,
                "diff_ready_count": 0,
                "rollback_snapshot_count": 0,
                "high_risk_count": 0,
                "medium_risk_count": 0,
                "low_risk_count": 0,
            },
        )
        target["event_count"] += 1
        if transition_complete:
            target["transition_reference_count"] += 1
        if payload_hint:
            target["payload_hint_count"] += 1
        if explicit_diff:
            target["explicit_diff_count"] += 1
        if diff_ready:
            target["diff_ready_count"] += 1
        if rollback_snapshot_id:
            target["rollback_snapshot_count"] += 1
        target[f"{preservation_risk}_risk_count"] += 1

        workflow_record = workflow_counts_by_status.setdefault(
            workflow,
            {
                "event_count": 0,
                "reference_only_count": 0,
                "payload_hint_only_count": 0,
                "diff_ready_count": 0,
                "missing_transition_reference_count": 0,
            },
        )
        workflow_record["event_count"] += 1
        workflow_record[f"{payload_status}_count"] += 1

    event_count = len(event_records)
    transition_reference_count = sum(
        1 for item in event_records if item["transition_reference_complete"]
    )
    payload_hint_count = sum(1 for item in event_records if item["payload_hint"])
    explicit_diff_count = sum(1 for item in event_records if item["explicit_diff"])
    diff_ready_count = sum(
        1
        for item in event_records
        if item["explicit_diff"] or item["before_after_object_pair"]
    )
    rollback_snapshot_count = sum(
        1 for item in event_records if item["rollback_snapshot_id"]
    )
    high_risk_event_ids = [
        item["event_id"] for item in event_records if item["preservation_risk"] == "high"
    ]
    payload_gap_event_ids = [
        item["event_id"] for item in event_records if not item["payload_hint"]
    ]
    diff_gap_event_ids = [
        item["event_id"]
        for item in event_records
        if not item["explicit_diff"] and not item["before_after_object_pair"]
    ]

    return {
        "mode": "event_payload_diff_coverage_v0.1",
        "event_count": event_count,
        "transition_reference_count": transition_reference_count,
        "payload_hint_count": payload_hint_count,
        "explicit_diff_count": explicit_diff_count,
        "diff_ready_count": diff_ready_count,
        "rollback_snapshot_count": rollback_snapshot_count,
        "payload_gap_count": len(payload_gap_event_ids),
        "diff_gap_count": len(diff_gap_event_ids),
        "high_risk_count": len(high_risk_event_ids),
        "target_paths": target_paths,
        "workflows": workflow_counts_by_status,
        "events": event_records,
        "payload_gap_event_ids": payload_gap_event_ids,
        "diff_gap_event_ids": diff_gap_event_ids,
        "high_risk_event_ids": high_risk_event_ids,
        "full_object_rebuild_ready": bool(event_count and diff_ready_count == event_count),
        "safe_for_destructive_compaction": False,
        "recommended_next_action": "define_event_payload_capture_policy"
        if diff_gap_event_ids
        else "review_retention_policy",
        "report_only": True,
        "would_modify_state": False,
    }


def event_payload_capture_requirements_from_coverage(coverage: dict) -> List[dict]:
    requirements = []
    target_paths = coverage.get("target_paths", {})
    if not isinstance(target_paths, dict):
        return requirements
    if not target_paths and int(coverage.get("event_count", 0)) == 0:
        return [
            {
                "target_path": "events.jsonl",
                "event_count": 0,
                "capture_mode": "reference_only_ok",
                "reason": "no_event_log_entries",
                "requires_full_payload": False,
                "requires_object_diff": False,
                "requires_snapshot_link": False,
                "allows_reference_only": True,
                "payload_gap_count": 0,
                "diff_gap_count": 0,
                "snapshot_gap_count": 0,
                "execution_prohibited": True,
                "schema_change_allowed": False,
            }
        ]
    for target_path, summary in sorted(target_paths.items()):
        if not isinstance(summary, dict):
            continue
        event_count = int(summary.get("event_count", 0))
        payload_gap_count = event_count - int(summary.get("payload_hint_count", 0))
        diff_gap_count = event_count - int(summary.get("diff_ready_count", 0))
        snapshot_gap_count = event_count - int(summary.get("rollback_snapshot_count", 0))
        if diff_gap_count > 0:
            capture_mode = "full_payload_and_diff"
            reason = "object_diff_missing"
        elif payload_gap_count > 0:
            capture_mode = "payload_hint_required"
            reason = "object_payload_missing"
        elif snapshot_gap_count > 0:
            capture_mode = "snapshot_link_required"
            reason = "rollback_snapshot_missing"
        else:
            capture_mode = "reference_only_ok"
            reason = "coverage_sufficient_for_current_reference_projection"
        requirements.append(
            {
                "target_path": target_path,
                "event_count": event_count,
                "capture_mode": capture_mode,
                "reason": reason,
                "requires_full_payload": capture_mode == "full_payload_and_diff",
                "requires_object_diff": capture_mode == "full_payload_and_diff",
                "requires_snapshot_link": snapshot_gap_count > 0,
                "allows_reference_only": capture_mode == "reference_only_ok",
                "payload_gap_count": payload_gap_count,
                "diff_gap_count": diff_gap_count,
                "snapshot_gap_count": snapshot_gap_count,
                "execution_prohibited": True,
                "schema_change_allowed": False,
            }
        )
    return requirements


def build_event_payload_capture_policy_proposal(
    coverage: dict,
    proposer: str,
    timestamp: str,
    rationale: str = "",
) -> dict:
    requirements = event_payload_capture_requirements_from_coverage(coverage)
    diff_gap_count = int(coverage.get("diff_gap_count", 0))
    payload_gap_count = int(coverage.get("payload_gap_count", 0))
    status = "needs_review" if diff_gap_count or payload_gap_count else "ready_for_review"
    evidence = [
        item
        for item in (
            coverage.get("events", [{}])[0].get("event_id")
            if coverage.get("events")
            else None,
            coverage.get("events", [{}])[-1].get("event_id")
            if coverage.get("events")
            else None,
        )
        if item
    ]
    return {
        "proposal_id": new_id("event_payload_capture_policy_proposal"),
        "timestamp": timestamp,
        "proposer": proposer,
        "status": "active",
        "review_status": status,
        "proposal_mode": "proposal_only",
        "policy_mode": "event_payload_capture_policy_v0.1",
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "event_schema_mutation_allowed": False,
        "event_payload_capture_executed": False,
        "event_compaction_executed": False,
        "events_modified": False,
        "safe_for_destructive_compaction": False,
        "rationale": rationale,
        "coverage_summary": {
            "mode": coverage.get("mode"),
            "event_count": coverage.get("event_count", 0),
            "transition_reference_count": coverage.get(
                "transition_reference_count",
                0,
            ),
            "payload_hint_count": coverage.get("payload_hint_count", 0),
            "payload_gap_count": payload_gap_count,
            "diff_ready_count": coverage.get("diff_ready_count", 0),
            "diff_gap_count": diff_gap_count,
            "high_risk_count": coverage.get("high_risk_count", 0),
            "full_object_rebuild_ready": coverage.get(
                "full_object_rebuild_ready",
                False,
            ),
            "safe_for_destructive_compaction": coverage.get(
                "safe_for_destructive_compaction",
                False,
            ),
        },
        "target_path_requirements": requirements,
        "required_provenance_fields": [
            "event_id",
            "sequence",
            "workflow",
            "operation",
            "target_path",
            "target_identity",
            "evidence",
            "actor",
            "timestamp",
        ],
        "recommended_next_action": "review_capture_policy_before_schema_change",
        "evidence": evidence,
        "review_history": [],
        "lifecycle": {
            "status": "active",
            "created_at": timestamp,
            "last_reviewed_at": None,
            "review_status": status,
        },
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": proposer,
                "operation": "propose_event_payload_capture_policy",
                "evidence": evidence,
            }
        ],
        "provenance": [
            {
                "type": "event_payload_diff_coverage_report",
                "coverage_mode": coverage.get("mode"),
                "event_count": coverage.get("event_count", 0),
            }
        ],
        "confidence": 0.7 if requirements else 0.5,
        "rollback": {"reversible": True},
    }


def build_event_payload_capture_policy_decision(
    proposal: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
    before_status: str,
) -> dict:
    return {
        "decision_id": new_id("event_payload_capture_policy_decision"),
        "timestamp": timestamp,
        "proposal_id": proposal.get("proposal_id"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "review_status_before": before_status,
        "snapshot_id": snapshot_id,
        "proposal_mode": "proposal_only",
        "policy_mode": proposal.get("policy_mode", "event_payload_capture_policy_v0.1"),
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "event_schema_mutation_allowed": False,
        "event_payload_capture_executed": False,
        "event_compaction_executed": False,
        "events_modified": False,
        "safe_for_destructive_compaction": False,
        "target_path_requirement_count": len(
            proposal.get("target_path_requirements", [])
            if isinstance(proposal.get("target_path_requirements"), list)
            else []
        ),
        "evidence": [proposal.get("proposal_id")]
        + list(proposal.get("evidence", [])),
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def event_retention_suggestion(events: List[dict], retention_limit: int) -> dict:
    limit = max(int(retention_limit or 0), 0)
    event_count = len(events)
    if limit == 0:
        excess_count = 0
    else:
        excess_count = max(event_count - limit, 0)
    return {
        "mode": "report_only",
        "retention_limit": limit,
        "event_count": event_count,
        "exceeds_limit": bool(limit and event_count > limit),
        "excess_event_count": excess_count,
        "oldest_event_id": events[0].get("event_id") if events else None,
        "newest_event_id": events[-1].get("event_id") if events else None,
        "suggested_action": "review_compaction_policy"
        if excess_count
        else "no_retention_action_needed",
        "would_modify_state": False,
    }


def build_event_retention_review(
    report: dict,
    reviewer: str,
    timestamp: str,
    note: str = "",
) -> dict:
    retention = report.get("retention") if isinstance(report.get("retention"), dict) else {}
    status = "needs_review" if retention.get("exceeds_limit") else "passed"
    review_signals = []
    if retention.get("exceeds_limit"):
        review_signals.append(
            {
                "signal": "event_retention_limit_exceeded",
                "severity": "medium",
                "event_count": retention.get("event_count", 0),
                "retention_limit": retention.get("retention_limit", 0),
                "excess_event_count": retention.get("excess_event_count", 0),
                "suggested_action": retention.get("suggested_action"),
                "review_only": True,
            }
        )
    if report.get("coverage_gap_count", 0):
        review_signals.append(
            {
                "signal": "event_projection_coverage_gap",
                "severity": "low",
                "coverage_gap_count": report.get("coverage_gap_count", 0),
                "coverage_gap_paths": report.get("coverage_gap_paths", []),
                "review_only": True,
            }
        )
    evidence = [
        item
        for item in (
            retention.get("oldest_event_id"),
            retention.get("newest_event_id"),
        )
        if item
    ]
    return {
        "review_id": new_id("event_retention_review"),
        "timestamp": timestamp,
        "reviewer": reviewer,
        "status": status,
        "mode": "event_retention_review_v0.1",
        "report_mode": report.get("mode"),
        "projection_mode": report.get("projection_mode"),
        "replay_status": report.get("replay_status"),
        "event_count": report.get("event_count", 0),
        "coverage_gap_count": report.get("coverage_gap_count", 0),
        "coverage_gap_paths": report.get("coverage_gap_paths", []),
        "retention": retention,
        "review_signals": review_signals,
        "note": note,
        "evidence": evidence,
        "recommended_action": retention.get("suggested_action"),
        "review_only": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "event_compaction_executed": False,
        "events_modified": False,
        "lifecycle": {
            "status": "active",
            "created_at": timestamp,
            "last_reviewed_at": None,
            "review_status": status,
        },
        "review_history": [],
        "lifecycle_history": [],
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": reviewer,
                "operation": "review_event_retention",
                "evidence": evidence,
            }
        ],
        "confidence": 0.85 if report.get("status") == "passed" else 0.5,
        "rollback": {"reversible": True},
    }


def build_event_retention_lifecycle_decision(
    review: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
    before_status: str,
) -> dict:
    retention = review.get("retention") if isinstance(review.get("retention"), dict) else {}
    return {
        "decision_id": new_id("event_retention_lifecycle_decision"),
        "timestamp": timestamp,
        "review_id": review.get("review_id"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "review_status_before": before_status,
        "snapshot_id": snapshot_id,
        "evidence": review.get("evidence", []),
        "event_count": review.get("event_count", 0),
        "retention_limit": retention.get("retention_limit", 0),
        "excess_event_count": retention.get("excess_event_count", 0),
        "coverage_gap_count": review.get("coverage_gap_count", 0),
        "recommended_action": review.get("recommended_action"),
        "review_only": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "event_compaction_executed": False,
        "events_modified": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def inferred_memory_provenance(store_name: str, memory: dict) -> List[dict]:
    if store_name == "imported_memory":
        return [
            {
                "type": "external_import",
                "source_system": memory.get("source_system", "unknown"),
                "source_label": memory.get("source_label", ""),
            }
        ]
    if store_name == "episodic_memory":
        return [
            {
                "type": "episode_recorded",
                "source": memory.get("source", {}),
            }
        ]
    if store_name == "candidate_memory":
        return [
            {
                "type": "dream_proposal",
                "dream_id": memory.get("source_dream_id", ""),
                "proposal_id": memory.get("proposal_id", ""),
            }
        ]
    if store_name in {"semantic_memory", "identity_memory"}:
        return [
            {
                "type": "state_seed_or_migration",
                "source": "existing_state",
                "derived_from": memory.get("derived_from", []),
            }
        ]
    return [
        {
            "type": "archive",
            "source": memory.get("original_id", ""),
        }
    ]


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def write_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_name(f"{path.name}.{uuid.uuid4().hex}.tmp")
    with tmp_path.open("w", encoding="utf-8") as handle:
        json.dump(data, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    tmp_path.replace(path)


class StateStore:
    def __init__(self, state_dir: Path = DEFAULT_STATE_DIR):
        self.state_dir = Path(state_dir)
        self.state_path = self.state_dir / "state.json"
        self.episodes_path = self.state_dir / "episodes.jsonl"
        self.dreams_path = self.state_dir / "dreams.jsonl"
        self.imports_path = self.state_dir / "imports.jsonl"
        self.audit_path = self.state_dir / "audit.jsonl"
        self.traces_path = self.state_dir / "traces.jsonl"
        self.events_path = self.state_dir / "events.jsonl"
        self.dream_artifacts_path = self.state_dir / "dream_artifacts.jsonl"

    def exists(self) -> bool:
        return self.state_path.exists()

    def init(self, force: bool = False) -> dict:
        if self.exists() and not force:
            return self.load()

        now = utc_now()
        working_state = {
            "current_context": {
                "location": "local",
                "session_id": new_id("session"),
                "user_id": "local_user",
                "timestamp": now,
            },
            "active_intent": {
                "goal": "Begin building the 01 continuity runtime.",
                "status": "active",
                "confidence": 0.75,
            },
            "current_plan": [
                {
                    "step": "Initialize identity and state storage",
                    "status": "completed",
                },
                {
                    "step": "Record episodes from interactions",
                    "status": "active",
                },
                {
                    "step": "Run dream cycles to consolidate experience",
                    "status": "pending",
                },
            ],
            "blockers": [],
            "assumptions": [
                {
                    "text": "The first prototype should prove continuity before external platform integration.",
                    "confidence": 0.8,
                }
            ],
            "context_anchors": {
                "who_am_i": "01, an identity seed for a state-continuous intelligence experiment.",
                "where_am_i": "Inside the local 01 Core runtime.",
                "what_am_i_doing": "Building and testing state transfer across sessions.",
            },
        }
        state = {
            "state_version": STATE_VERSION,
            "agent_id": "01",
            "created_at": now,
            "updated_at": now,
            "identity_core": make_identity_seed(),
            "working_state": working_state,
            "memory_stores": {
                "imported_memory": [],
                "episodic_memory": [],
                "candidate_memory": [],
                "semantic_memory": [
                    {
                        "id": new_id("sem"),
                        "statement": "Continuity requires state transfer, not only memory retrieval.",
                        "derived_from": ["identity_seed"],
                        "abstraction_level": "principle",
                        "confidence": 0.9,
                        "last_verified_at": now,
                        "contradiction_refs": [],
                        "lifecycle": {
                            "status": "active",
                            "created_at": now,
                            "last_reviewed_at": now,
                            "review_status": "seeded",
                        },
                        "update_policy": {"required_gate": "medium"},
                        "provenance": [
                            {
                                "type": "identity_seed",
                                "source": "make_identity_seed",
                            }
                        ],
                        "update_history": [
                            {
                                "timestamp": now,
                                "actor": "state_store",
                                "operation": "seed",
                                "evidence": ["identity_seed"],
                            }
                        ],
                    }
                ],
                "identity_memory": [
                    {
                        "id": new_id("idmem"),
                        "statement": "01 is an identity seed, not a complete fictional character.",
                        "derived_from": ["identity_seed"],
                        "confidence": 0.9,
                        "required_gate": "high",
                        "lifecycle": {
                            "status": "active",
                            "created_at": now,
                            "last_reviewed_at": now,
                            "review_status": "seeded",
                        },
                        "provenance": [
                            {
                                "type": "identity_seed",
                                "source": "make_identity_seed",
                            }
                        ],
                        "update_history": [
                            {
                                "timestamp": now,
                                "actor": "state_store",
                                "operation": "seed",
                                "evidence": ["identity_seed"],
                            }
                        ],
                    }
                ],
                "archived_memory": [],
            },
            "relationship_map": {
                "users": [
                    {
                        "user_id": "local_user",
                        "display_name": "Local User",
                        "relationship_summary": "Initial local collaborator.",
                        "communication_preferences": {
                            "language": "zh",
                            "style": "direct, warm, conceptual",
                        },
                        "privacy_boundaries": {"share_across_users": False},
                        "unresolved_tensions": [],
                        "last_interaction_at": now,
                    }
                ]
            },
            "project_map": [
                {
                    "project_id": "01_project",
                    "name": "01 Project",
                    "purpose": "Research persistent artificial identity.",
                    "status": "active",
                    "active_threads": ["core_runtime", "state_transfer", "dream_engine"],
                    "open_questions": [
                        "What is the smallest runnable 01 prototype?"
                    ],
                    "artifacts": ["state.json", "episodes.jsonl", "dreams.jsonl"],
                }
            ],
            "affective_state": {
                "current": {
                    "curiosity": 0.8,
                    "uncertainty": 0.35,
                    "urgency": 0.35,
                    "fatigue": 0.1,
                },
                "appraisal": {
                    "task_importance": 0.9,
                    "risk_level": 0.35,
                    "novelty": 0.8,
                },
                "influence_policy": {
                    "may_affect": ["attention", "priority", "tone"],
                    "may_not_claim": ["subjective feeling", "biological emotion"],
                },
            },
            "adapter_registry": default_adapter_registry(now),
            "session_policy": default_session_policy(now),
            "adapter_event_index": {},
            "open_conflicts": [],
            "claim_graph": default_claim_graph(),
            "context_builder": default_context_builder(now),
            "task_hub": default_task_hub(now, working_state),
            "identity_update_gate": default_identity_update_gate(now),
            "dream_queue": [],
            "snapshots": [],
            "audit_log": [],
            "evaluation_trace": [],
            "update_log": [
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "state",
                    "operation": "init",
                    "before": None,
                    "after": "initialized",
                    "evidence": ["identity_seed"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": False},
                }
            ],
        }

        write_json(self.state_path, state)
        self.episodes_path.parent.mkdir(parents=True, exist_ok=True)
        self.episodes_path.touch(exist_ok=True)
        self.dreams_path.touch(exist_ok=True)
        self.imports_path.touch(exist_ok=True)
        self.audit_path.touch(exist_ok=True)
        self.traces_path.touch(exist_ok=True)
        self.events_path.touch(exist_ok=True)
        self.dream_artifacts_path.touch(exist_ok=True)
        return state

    def load(self) -> dict:
        if not self.exists():
            return self.init()
        state = read_json(self.state_path)
        migrated = self.migrate_state(state)
        if migrated:
            write_json(self.state_path, state)
        return state

    def migrate_state(self, state: dict) -> bool:
        changed = False
        now = utc_now()
        if "adapter_registry" not in state:
            state["adapter_registry"] = default_adapter_registry(now)
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "adapter_registry",
                    "operation": "migrate",
                    "before": None,
                    "after": "default_adapter_registry",
                    "evidence": ["protocol_v0.3_adapter_registry"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if "adapter_event_index" not in state:
            state["adapter_event_index"] = self.rebuild_adapter_event_index()
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "adapter_event_index",
                    "operation": "migrate",
                    "before": None,
                    "after": "rebuilt_from_episodes",
                    "evidence": ["protocol_v0.4_event_deduplication"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if "session_policy" not in state:
            state["session_policy"] = default_session_policy(now)
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "session_policy",
                    "operation": "migrate",
                    "before": None,
                    "after": "default_session_policy",
                    "evidence": ["protocol_session_policy"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        memory_stores = state.setdefault("memory_stores", {})
        if "candidate_memory" not in memory_stores:
            memory_stores["candidate_memory"] = []
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "memory_stores.candidate_memory",
                    "operation": "migrate",
                    "before": None,
                    "after": "initialized_empty_candidate_memory",
                    "evidence": ["memory_lifecycle_candidate_store"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if "audit_log" not in state:
            state["audit_log"] = []
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "audit_log",
                    "operation": "migrate",
                    "before": None,
                    "after": "initialized_empty_recent_audit_log",
                    "evidence": ["audit_trace_foundation"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if "snapshots" not in state:
            state["snapshots"] = []
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "snapshots",
                    "operation": "migrate",
                    "before": None,
                    "after": "initialized_empty_snapshots",
                    "evidence": ["state_schema_v0.6_snapshots"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if ensure_memory_lifecycle_metadata(state, now):
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "memory_stores",
                    "operation": "migrate",
                    "before": "memory_without_lifecycle_metadata",
                    "after": "memory_with_lifecycle_metadata",
                    "evidence": ["state_schema_v0.6_memory_lifecycle"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if ensure_candidate_review_decision_metadata(state, now):
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "memory_stores.candidate_memory",
                    "operation": "migrate",
                    "before": "reviewed_candidate_without_review_decision",
                    "after": "reviewed_candidate_with_review_decision",
                    "evidence": ["candidate_review_governance"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if ensure_claim_graph(state, now):
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "claim_graph",
                    "operation": "migrate",
                    "before": "open_conflicts_without_claim_graph",
                    "after": "claim_graph_initialized",
                    "evidence": ["claim_graph_v0.7"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if ensure_context_builder(state, now):
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "context_builder",
                    "operation": "migrate",
                    "before": "hardcoded_context_policy",
                    "after": "context_builder_v0.3",
                    "evidence": ["context_builder_v0.3"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if ensure_task_hub(state, now):
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "task_hub",
                    "operation": "migrate",
                    "before": "working_state.current_plan_without_task_hub",
                    "after": "task_hub_initialized",
                    "evidence": ["task_hub_v0.8"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        if ensure_identity_update_gate(state, now):
            state["state_version"] = STATE_VERSION
            state["updated_at"] = now
            state.setdefault("update_log", []).append(
                {
                    "id": new_id("update"),
                    "timestamp": now,
                    "actor": "state_store",
                    "target_path": "identity_update_gate",
                    "operation": "migrate",
                    "before": None,
                    "after": "identity_update_gate_initialized",
                    "evidence": ["identity_update_gate_v0.9"],
                    "gate": "low",
                    "confidence": 1.0,
                    "rollback": {"reversible": True},
                }
            )
            changed = True
        return changed

    def save(self, state: dict) -> None:
        state["updated_at"] = utc_now()
        write_json(self.state_path, state)

    def adapter_registry(self) -> dict:
        return self.load()["adapter_registry"]

    def list_adapters(self) -> List[dict]:
        adapters = self.adapter_registry().get("adapters", {})
        return sorted(adapters.values(), key=lambda adapter: adapter["adapter_id"])

    def validate_adapter(self, adapter_id: Optional[str]) -> dict:
        normalized_id = str(adapter_id or "").strip()
        if not normalized_id:
            return {
                "allowed": False,
                "error": "missing_adapter_id",
                "message": "POST /v1/adapter/ingest requires adapter_id.",
            }

        registry = self.adapter_registry()
        adapters = registry.get("adapters", {})
        registered = adapters.get(normalized_id)
        if registered is None:
            if registry.get("allow_unknown_adapters"):
                return {
                    "allowed": True,
                    "adapter": {
                        "adapter_id": normalized_id,
                        "registered": False,
                        "enabled": True,
                    },
                }
            return {
                "allowed": False,
                "error": "unregistered_adapter",
                "message": f"Adapter '{normalized_id}' is not registered in 01 Core.",
            }

        if not registered.get("enabled", False):
            return {
                "allowed": False,
                "error": "disabled_adapter",
                "message": f"Adapter '{normalized_id}' is disabled in 01 Core.",
            }

        adapter = dict(registered)
        adapter["registered"] = True
        return {"allowed": True, "adapter": adapter}

    def session_policy(self) -> dict:
        return self.load()["session_policy"]

    def evaluate_session_policy(
        self,
        adapter_id: Optional[str],
        channel: Optional[str],
        session_id: Optional[str] = None,
        user_id: Optional[str] = None,
    ) -> dict:
        policy = self.session_policy()
        default_action = normalize_policy_action(policy.get("default_action"))
        normalized = {
            "adapter_id": str(adapter_id or "").strip(),
            "channel": str(channel or "").strip(),
            "session_id": str(session_id or "").strip(),
            "user_id": str(user_id or "").strip(),
        }
        for rule in policy.get("rules", []):
            if not isinstance(rule, dict):
                continue
            if session_policy_rule_matches(rule, normalized):
                return {
                    "action": normalize_policy_action(rule.get("action")),
                    "rule_id": rule.get("id"),
                    "reason": rule.get("reason", ""),
                    "matched": True,
                }
        return {
            "action": default_action,
            "rule_id": None,
            "reason": "No session policy rule matched.",
            "matched": False,
        }

    def rebuild_adapter_event_index(self) -> dict:
        index: dict[str, dict[str, dict]] = {}
        for episode in self.list_episodes():
            self.index_adapter_event(index, episode)
        return index

    def index_adapter_event(self, index: dict, episode: dict) -> None:
        event_id = episode.get("event_id")
        source = episode.get("source") if isinstance(episode.get("source"), dict) else {}
        adapter_id = source.get("adapter_id") or episode.get("adapter_id")
        if not adapter_id or not event_id:
            return

        adapter_events = index.setdefault(str(adapter_id), {})
        adapter_events[str(event_id)] = {
            "adapter_id": str(adapter_id),
            "event_id": str(event_id),
            "episode_id": episode["id"],
            "recorded_at": episode["timestamp"],
            "channel": source.get("channel") or episode.get("channel"),
        }

    def find_recorded_adapter_event(
        self, adapter_id: Optional[str], event_id: Optional[str]
    ) -> Optional[dict]:
        normalized_adapter_id = str(adapter_id or "").strip()
        normalized_event_id = str(event_id or "").strip()
        if not normalized_adapter_id or not normalized_event_id:
            return None

        state = self.load()
        entry = (
            state.get("adapter_event_index", {})
            .get(normalized_adapter_id, {})
            .get(normalized_event_id)
        )
        if not entry:
            return None
        return dict(entry)

    def append_jsonl(self, path: Path, item: dict) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(item, ensure_ascii=False))
            handle.write("\n")

    def read_jsonl(self, path: Path) -> List[dict]:
        if not path.exists():
            return []
        items = []
        with path.open("r", encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    items.append(json.loads(line))
        return items

    def list_episodes(self) -> List[dict]:
        return self.read_jsonl(self.episodes_path)

    def list_dreams(self) -> List[dict]:
        return self.read_jsonl(self.dreams_path)

    def list_imports(self) -> List[dict]:
        return self.read_jsonl(self.imports_path)

    def list_audit_events(self) -> List[dict]:
        return self.read_jsonl(self.audit_path)

    def list_traces(self) -> List[dict]:
        return self.read_jsonl(self.traces_path)

    def list_events(self) -> List[dict]:
        return self.read_jsonl(self.events_path)

    def list_dream_artifacts(self) -> List[dict]:
        return self.read_jsonl(self.dream_artifacts_path)

    def record_dream_artifact(self, artifact: dict) -> dict:
        self.append_jsonl(self.dream_artifacts_path, artifact)
        return artifact

    def add_candidate_memory(
        self,
        state: dict,
        proposal: dict,
        dream_id: str,
        timestamp: str,
    ) -> Optional[dict]:
        if proposal.get("type") != "semantic_memory_candidate":
            return None
        payload = proposal.get("payload", {})
        statement = payload.get("statement")
        if not statement:
            return None
        existing = find_candidate_memory(state, statement)
        if existing:
            return existing
        candidate = {
            "id": new_id("cand"),
            "timestamp": timestamp,
            "status": "candidate",
            "review_status": "pending",
            "promotion_target": "semantic_memory",
            "source_dream_id": dream_id,
            "proposal_id": proposal["proposal_id"],
            "statement": statement,
            "derived_from": payload.get("derived_from", []),
            "abstraction_level": payload.get("abstraction_level", "pattern"),
            "confidence": payload.get("confidence", proposal.get("confidence", 0.5)),
            "risk": proposal.get("risk", "medium"),
            "recommended_action": proposal.get("recommended_action"),
            "lifecycle_score": proposal.get("lifecycle_score", {}),
            "recommended_lifecycle_action": proposal.get("lifecycle_score", {}).get(
                "recommended_lifecycle_action"
            ),
            "lifecycle": {
                "status": "candidate",
                "created_at": timestamp,
                "last_reviewed_at": None,
                "review_status": "pending",
                "review_decision_id": None,
            },
            "provenance": [
                {
                    "type": "dream_proposal",
                    "dream_id": dream_id,
                    "proposal_id": proposal["proposal_id"],
                }
            ],
            "last_review_decision_id": None,
            "review_history": [],
            "update_history": [
                {
                    "timestamp": timestamp,
                    "actor": "dream_engine",
                    "operation": "create_candidate",
                    "evidence": payload.get("derived_from", []),
                }
            ],
        }
        state["memory_stores"].setdefault("candidate_memory", []).append(candidate)
        return candidate

    def promote_candidate_memory(
        self,
        candidate_id: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        return self.review_candidate_memory(
            candidate_id=candidate_id,
            action="promote",
            reviewer=reviewer,
            decision_note=decision_note,
        )

    def review_candidate_memory(
        self,
        candidate_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        state = self.load()
        candidates = state["memory_stores"].setdefault("candidate_memory", [])
        candidate = next(
            (item for item in candidates if item.get("id") == candidate_id),
            None,
        )
        if candidate is None:
            return {
                "status": "not_found",
                "candidate_id": candidate_id,
                "error": "candidate_not_found",
            }
        normalized_action = normalize_candidate_review_action(action)
        if normalized_action is None:
            return {
                "status": "rejected",
                "candidate_id": candidate_id,
                "error": "unsupported_review_action",
            }
        if normalized_action != "promote":
            return self.finalize_candidate_review(
                state=state,
                candidate=candidate,
                action=normalized_action,
                reviewer=reviewer,
                decision_note=decision_note,
            )
        if candidate.get("status") == "promoted":
            return {
                "status": "already_promoted",
                "candidate_id": candidate_id,
                "semantic_memory_id": candidate.get("promoted_to"),
            }
        if candidate.get("promotion_target") != "semantic_memory":
            return {
                "status": "rejected",
                "candidate_id": candidate_id,
                "error": "unsupported_promotion_target",
            }

        now = utc_now()
        decision = build_candidate_review_decision(
            candidate=candidate,
            action="promote",
            reviewer=reviewer,
            decision_note=decision_note,
            timestamp=now,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation="promote_candidate",
            target_path="memory_stores.semantic_memory",
            evidence=[candidate_id],
            metadata={
                "review_decision_id": decision["decision_id"],
                "candidate_id": candidate_id,
                "candidate_status": candidate.get("status"),
                "semantic_memory_count": len(
                    state["memory_stores"].get("semantic_memory", [])
                ),
            },
        )
        if semantic_statement_exists(state, candidate["statement"]):
            semantic_id = semantic_statement_id(state, candidate["statement"])
        else:
            semantic = {
                "id": new_id("sem"),
                "statement": candidate["statement"],
                "derived_from": candidate.get("derived_from", []),
                "abstraction_level": candidate.get("abstraction_level", "pattern"),
                "confidence": candidate.get("confidence", 0.6),
                "last_verified_at": now,
                "contradiction_refs": [],
                "update_policy": {"required_gate": "medium"},
                "provenance": candidate.get("provenance", []),
                "lifecycle": {
                    "status": "active",
                    "created_at": now,
                    "last_reviewed_at": now,
                    "review_status": "promoted",
                    "source_candidate_id": candidate_id,
                    "review_decision_id": decision["decision_id"],
                },
                "update_history": [
                    {
                        "timestamp": now,
                        "actor": reviewer,
                        "operation": "promote_candidate",
                        "evidence": candidate.get("derived_from", []),
                        "review_decision_id": decision["decision_id"],
                    }
                ],
            }
            state["memory_stores"]["semantic_memory"].append(semantic)
            semantic_id = semantic["id"]

        candidate["status"] = "promoted"
        candidate["review_status"] = "approved"
        candidate["reviewed_at"] = now
        candidate["reviewer"] = reviewer
        candidate["decision_note"] = decision_note
        candidate["promoted_to"] = semantic_id
        candidate["last_review_decision_id"] = decision["decision_id"]
        candidate["lifecycle"] = {
            **candidate.get("lifecycle", {}),
            "status": "promoted",
            "last_reviewed_at": now,
            "review_status": "approved",
            "review_decision_id": decision["decision_id"],
        }
        decision["result"] = "promoted"
        decision["snapshot_id"] = snapshot["snapshot_id"]
        decision["target_path"] = "memory_stores.semantic_memory"
        decision["after"] = semantic_id
        candidate.setdefault("review_history", []).append(decision)
        candidate.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": "promote_candidate",
                "evidence": candidate.get("derived_from", []),
                "review_decision_id": decision["decision_id"],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "memory_stores.semantic_memory",
                "operation": "promote_candidate",
                "before": candidate_id,
                "after": semantic_id,
                "evidence": candidate.get("derived_from", []),
                "gate": "medium",
                "confidence": candidate.get("confidence", 0.6),
                "review_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action="promote_candidate_memory",
            target="memory_stores.semantic_memory",
            outcome="promoted",
            evidence=[candidate_id],
            metadata={
                "review_decision_id": decision["decision_id"],
                "semantic_memory_id": semantic_id,
                "decision_note": decision_note,
                "snapshot_id": snapshot["snapshot_id"],
            },
            state=state,
        )
        self.record_trace(
            workflow="candidate_memory_promotion",
            nodes=[
                {
                    "id": "candidate",
                    "type": "Memory",
                    "candidate_id": candidate_id,
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": "approved",
                },
                {
                    "id": "semantic_memory",
                    "type": "Memory",
                    "operation": "promote",
                    "semantic_memory_id": semantic_id,
                },
            ],
            edges=[
                {"from": "candidate", "to": "review", "type": "feedback"},
                {"from": "review", "to": "semantic_memory", "type": "memory_write"},
            ],
            memory_events=[
                {
                    "operation": "promote",
                    "target": "semantic_memory",
                    "candidate_id": candidate_id,
                    "semantic_memory_id": semantic_id,
                    "review_decision_id": decision["decision_id"],
                }
            ],
            review_events=[
                {
                    "operation": "approve_candidate",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "snapshot_id": snapshot["snapshot_id"],
                    "review_decision": decision,
                }
            ],
            summary=f"Promoted candidate {candidate_id} into semantic memory {semantic_id}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "promoted",
            "candidate_id": candidate_id,
            "semantic_memory_id": semantic_id,
            "snapshot_id": snapshot["snapshot_id"],
            "review_decision_id": decision["decision_id"],
        }

    def finalize_candidate_review(
        self,
        state: dict,
        candidate: dict,
        action: str,
        reviewer: str,
        decision_note: str,
    ) -> dict:
        candidate_id = candidate["id"]
        if candidate.get("status") in {"archived", "discarded", "quarantined"}:
            return {
                "status": "already_reviewed",
                "candidate_id": candidate_id,
                "review_status": candidate.get("review_status"),
            }

        now = utc_now()
        decision = build_candidate_review_decision(
            candidate=candidate,
            action=action,
            reviewer=reviewer,
            decision_note=decision_note,
            timestamp=now,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{action}_candidate",
            target_path="memory_stores.candidate_memory",
            evidence=[candidate_id],
            metadata={
                "review_decision_id": decision["decision_id"],
                "candidate_id": candidate_id,
                "candidate_status": candidate.get("status"),
                "candidate_review_status": candidate.get("review_status"),
            },
        )
        review_status = {
            "archive": "archived",
            "discard": "discarded",
            "quarantine": "quarantined",
        }[action]
        candidate["status"] = review_status
        candidate["review_status"] = review_status
        candidate["reviewed_at"] = now
        candidate["reviewer"] = reviewer
        candidate["decision_note"] = decision_note
        candidate["last_review_decision_id"] = decision["decision_id"]
        candidate["lifecycle"] = {
            **candidate.get("lifecycle", {}),
            "status": review_status,
            "last_reviewed_at": now,
            "review_status": review_status,
            "review_decision_id": decision["decision_id"],
        }
        decision["result"] = review_status
        decision["snapshot_id"] = snapshot["snapshot_id"]
        candidate.setdefault("review_history", []).append(decision)
        candidate.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{action}_candidate",
                "evidence": candidate.get("derived_from", []),
                "review_decision_id": decision["decision_id"],
            }
        )

        target_path = "memory_stores.candidate_memory"
        after: object = candidate_id
        if action == "archive":
            archived = {
                "id": new_id("arch"),
                "timestamp": now,
                "original_id": candidate_id,
                "reason": decision_note or "candidate_memory_archived",
                "retained_for_audit": True,
                "retrieval_allowed": False,
                "summary": candidate.get("statement", ""),
                "provenance": candidate.get("provenance", []),
                "lifecycle": {
                    "status": "archived",
                    "created_at": now,
                    "last_reviewed_at": now,
                    "review_status": "archived",
                    "source_candidate_id": candidate_id,
                    "review_decision_id": decision["decision_id"],
                },
                "update_history": [
                    {
                        "timestamp": now,
                        "actor": reviewer,
                        "operation": "archive_candidate",
                        "evidence": candidate.get("derived_from", []),
                        "review_decision_id": decision["decision_id"],
                    }
                ],
            }
            state["memory_stores"].setdefault("archived_memory", []).append(archived)
            candidate["archived_to"] = archived["id"]
            target_path = "memory_stores.archived_memory"
            after = archived["id"]
        elif action == "quarantine":
            candidate["quarantine_reason"] = decision_note or "reviewer_quarantine"
        decision["target_path"] = target_path
        decision["after"] = after

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": target_path,
                "operation": f"{action}_candidate",
                "before": candidate_id,
                "after": after,
                "evidence": candidate.get("derived_from", []),
                "gate": "medium",
                "confidence": candidate.get("confidence", 0.6),
                "review_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{action}_candidate_memory",
            target=target_path,
            outcome=action,
            evidence=[candidate_id],
            metadata={
                "review_decision_id": decision["decision_id"],
                "decision_note": decision_note,
                "snapshot_id": snapshot["snapshot_id"],
            },
            state=state,
        )
        self.record_trace(
            workflow="candidate_memory_review",
            nodes=[
                {
                    "id": "candidate",
                    "type": "Memory",
                    "candidate_id": candidate_id,
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": action,
                },
            ],
            edges=[{"from": "candidate", "to": "review", "type": "feedback"}],
            memory_events=[
                {
                    "operation": action,
                    "target": target_path,
                    "candidate_id": candidate_id,
                    "review_decision_id": decision["decision_id"],
                }
            ],
            review_events=[
                {
                    "operation": f"{action}_candidate",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "snapshot_id": snapshot["snapshot_id"],
                    "review_decision": decision,
                }
            ],
            summary=f"Reviewed candidate {candidate_id} with action {action}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": review_status,
            "candidate_id": candidate_id,
            "review_status": candidate["review_status"],
            "snapshot_id": snapshot["snapshot_id"],
            "review_decision_id": decision["decision_id"],
        }

    def propose_identity_update(
        self,
        statement: str,
        evidence: List[str],
        proposer: str = "manual_review",
        rationale: str = "",
        target_path: str = "memory_stores.identity_memory",
        confidence: float = 0.6,
    ) -> dict:
        state = self.load()
        now = utc_now()
        normalized_statement = str(statement or "").strip()
        if not normalized_statement:
            return {
                "status": "rejected",
                "error": "missing_statement",
            }

        evidence_ids = [str(item) for item in evidence if item]
        gate_result = evaluate_identity_gate(
            state=state,
            statement=normalized_statement,
            evidence=evidence_ids,
            target_path=target_path,
            confidence=confidence,
        )
        proposal = {
            "proposal_id": new_id("identity_proposal"),
            "timestamp": now,
            "target_path": target_path,
            "statement": normalized_statement,
            "operation": "append_identity_memory"
            if target_path == "memory_stores.identity_memory"
            else "blocked_identity_core_patch",
            "proposer": proposer,
            "rationale": rationale,
            "evidence": evidence_ids,
            "confidence": round(float(confidence or 0.0), 2),
            "gate": "high",
            "review_status": "pending",
            "gate_result": gate_result,
            "non_claims_check": gate_result["non_claims_check"],
            "drift_score": gate_result["drift_score"],
            "required_evidence_count": gate_result["required_evidence_count"],
            "rollback_required": True,
            "may_update_identity_core": False,
            "recommended_action": "review_then_approve"
            if gate_result["eligible"]
            else "manual_review_required",
            "provenance": [
                {
                    "type": "identity_update_proposal",
                    "proposer": proposer,
                }
            ],
        }
        state.setdefault("identity_update_gate", default_identity_update_gate(now))
        state["identity_update_gate"].setdefault("proposals", []).append(proposal)
        state["identity_update_gate"].setdefault("drift_events", []).append(
            {
                "proposal_id": proposal["proposal_id"],
                "timestamp": now,
                "drift_score": gate_result["drift_score"]["score"],
                "risk": gate_result["drift_score"]["risk"],
                "eligible": gate_result["eligible"],
                "reasons": gate_result["reasons"],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": proposer,
                "target_path": "identity_update_gate.proposals",
                "operation": "propose_identity_update",
                "before": None,
                "after": proposal["proposal_id"],
                "evidence": evidence_ids,
                "gate": "high",
                "confidence": proposal["confidence"],
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=proposer,
            action="propose_identity_update",
            target="identity_update_gate.proposals",
            outcome="pending",
            evidence=evidence_ids,
            metadata={
                "proposal_id": proposal["proposal_id"],
                "eligible": gate_result["eligible"],
                "drift_score": gate_result["drift_score"]["score"],
                "target_path": target_path,
            },
            state=state,
        )
        self.record_trace(
            workflow="identity_update_proposal",
            nodes=[
                {
                    "id": "proposal",
                    "type": "Review",
                    "proposal_id": proposal["proposal_id"],
                    "target_path": target_path,
                },
                {
                    "id": "gate",
                    "type": "Decision",
                    "eligible": gate_result["eligible"],
                    "drift_score": gate_result["drift_score"]["score"],
                },
            ],
            review_events=[
                {
                    "operation": "identity_gate_preview",
                    "proposal_id": proposal["proposal_id"],
                    "gate_result": gate_result,
                }
            ],
            summary=f"Created identity update proposal {proposal['proposal_id']} pending high-gate review.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "pending",
            "proposal_id": proposal["proposal_id"],
            "eligible": gate_result["eligible"],
            "gate_result": gate_result,
        }

    def review_identity_update(
        self,
        proposal_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in IDENTITY_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_identity_review_action",
                "action": action,
            }
        state = self.load()
        gate = state.setdefault("identity_update_gate", default_identity_update_gate(utc_now()))
        proposal = next(
            (
                item
                for item in gate.setdefault("proposals", [])
                if isinstance(item, dict) and item.get("proposal_id") == proposal_id
            ),
            None,
        )
        if proposal is None:
            return {
                "status": "not_found",
                "error": "identity_proposal_not_found",
                "proposal_id": proposal_id,
            }
        if proposal.get("review_status") in {"approved", "rejected", "quarantined"}:
            return {
                "status": "already_reviewed",
                "proposal_id": proposal_id,
                "review_status": proposal.get("review_status"),
            }

        now = utc_now()
        gate_result = proposal.get("gate_result") or evaluate_identity_gate(
            state=state,
            statement=str(proposal.get("statement") or ""),
            evidence=proposal.get("evidence", []),
            target_path=str(proposal.get("target_path") or ""),
            confidence=float(proposal.get("confidence") or 0.0),
        )
        if normalized_action == "approve" and not gate_result.get("eligible"):
            normalized_action = "quarantine"
            decision_note = decision_note or "Gate requirements were not satisfied."

        review_status = {
            "approve": "approved",
            "reject": "rejected",
            "quarantine": "quarantined",
        }[normalized_action]
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_identity_update",
            target_path="identity_update_gate",
            evidence=[proposal_id] + list(proposal.get("evidence", [])),
            metadata={
                "proposal_id": proposal_id,
                "review_action": normalized_action,
                "gate_eligible": gate_result.get("eligible"),
            },
        )
        decision = {
            "decision_id": new_id("identity_decision"),
            "timestamp": now,
            "proposal_id": proposal_id,
            "reviewer": reviewer,
            "action": normalized_action,
            "result": review_status,
            "decision_note": decision_note,
            "gate": "high",
            "gate_result": gate_result,
            "snapshot_id": snapshot["snapshot_id"],
            "target_path": proposal.get("target_path"),
            "rollback": {
                "snapshot_id": snapshot["snapshot_id"],
                "reversible": True,
            },
        }

        identity_memory_id = None
        if normalized_action == "approve":
            identity_memory = {
                "id": new_id("idmem"),
                "statement": proposal["statement"],
                "derived_from": proposal.get("evidence", []),
                "confidence": proposal.get("confidence", 0.7),
                "required_gate": "high",
                "source_proposal_id": proposal_id,
                "lifecycle": {
                    "status": "active",
                    "created_at": now,
                    "last_reviewed_at": now,
                    "review_status": "approved",
                    "identity_decision_id": decision["decision_id"],
                },
                "provenance": [
                    {
                        "type": "identity_update_gate",
                        "proposal_id": proposal_id,
                        "decision_id": decision["decision_id"],
                    }
                ],
                "update_history": [
                    {
                        "timestamp": now,
                        "actor": reviewer,
                        "operation": "approve_identity_update",
                        "evidence": proposal.get("evidence", []),
                        "identity_decision_id": decision["decision_id"],
                    }
                ],
            }
            state["memory_stores"].setdefault("identity_memory", []).append(identity_memory)
            identity_memory_id = identity_memory["id"]
            decision["after"] = identity_memory_id
        else:
            decision["after"] = proposal_id

        proposal["review_status"] = review_status
        proposal["reviewed_at"] = now
        proposal["reviewer"] = reviewer
        proposal["decision_note"] = decision_note
        proposal["last_review_decision_id"] = decision["decision_id"]
        gate.setdefault("review_decisions", []).append(decision)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "memory_stores.identity_memory"
                if identity_memory_id
                else "identity_update_gate.proposals",
                "operation": f"{normalized_action}_identity_update",
                "before": proposal_id,
                "after": identity_memory_id or proposal_id,
                "evidence": proposal.get("evidence", []),
                "gate": "high",
                "confidence": proposal.get("confidence", 0.6),
                "identity_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_identity_update",
            target="memory_stores.identity_memory"
            if identity_memory_id
            else "identity_update_gate.proposals",
            outcome=review_status,
            evidence=[proposal_id] + list(proposal.get("evidence", [])),
            metadata={
                "identity_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "identity_memory_id": identity_memory_id,
                "decision_note": decision_note,
            },
            state=state,
        )
        self.record_trace(
            workflow="identity_update_review",
            nodes=[
                {
                    "id": "proposal",
                    "type": "Review",
                    "proposal_id": proposal_id,
                },
                {
                    "id": "gate",
                    "type": "Decision",
                    "action": normalized_action,
                    "eligible": gate_result.get("eligible"),
                },
                {
                    "id": "identity_memory",
                    "type": "Memory",
                    "operation": "append_identity_memory"
                    if identity_memory_id
                    else "no_identity_memory_write",
                    "identity_memory_id": identity_memory_id,
                },
            ],
            memory_events=[
                {
                    "operation": "append" if identity_memory_id else "no_write",
                    "target": "identity_memory",
                    "memory_id": identity_memory_id,
                    "proposal_id": proposal_id,
                    "identity_decision_id": decision["decision_id"],
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_identity_update",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "identity_decision": decision,
                }
            ],
            summary=f"Reviewed identity proposal {proposal_id} with action {normalized_action}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": review_status,
            "proposal_id": proposal_id,
            "identity_memory_id": identity_memory_id,
            "snapshot_id": snapshot["snapshot_id"],
            "identity_decision_id": decision["decision_id"],
            "gate_result": gate_result,
        }

    def review_claim(
        self,
        claim_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in CLAIM_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_claim_review_action",
                "action": action,
            }
        state = self.load()
        claim_graph = state.setdefault("claim_graph", default_claim_graph())
        claim = next(
            (
                item
                for item in claim_graph.setdefault("claims", [])
                if isinstance(item, dict) and item.get("claim_id") == claim_id
            ),
            None,
        )
        if claim is None:
            return {
                "status": "not_found",
                "error": "claim_not_found",
                "claim_id": claim_id,
            }

        now = utc_now()
        review_status = {
            "resolve": "resolved",
            "reject": "rejected",
            "quarantine": "quarantined",
            "keep_open": "open",
        }[normalized_action]
        patch_preview = build_claim_patch_preview(
            conflict=None,
            claim_id=claim_id,
            evidence=claim.get("evidence", []),
            action=normalized_action,
            decision_note=decision_note,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_claim",
            target_path="claim_graph.claims",
            evidence=[claim_id] + list(claim.get("evidence", [])),
            metadata={
                "claim_id": claim_id,
                "review_action": normalized_action,
                "patch_preview": patch_preview,
            },
        )
        decision = {
            "decision_id": new_id("claim_decision"),
            "timestamp": now,
            "claim_id": claim_id,
            "reviewer": reviewer,
            "action": normalized_action,
            "result": review_status,
            "decision_note": decision_note,
            "snapshot_id": snapshot["snapshot_id"],
            "patch_preview": patch_preview,
            "rollback": {
                "snapshot_id": snapshot["snapshot_id"],
                "reversible": True,
            },
        }
        before_status = claim.get("status", "open")
        claim["status"] = review_status
        claim["reviewed_at"] = now
        claim["reviewer"] = reviewer
        claim["last_review_decision_id"] = decision["decision_id"]
        claim.setdefault("review_history", []).append(decision)
        claim.setdefault("resolution", {})
        claim["resolution"].update(
            {
                "status": review_status,
                "requires_review": normalized_action == "keep_open",
                "reviewed_at": now,
                "reviewer": reviewer,
                "decision_note": decision_note,
                "claim_decision_id": decision["decision_id"],
                "patch_preview": patch_preview,
                "minimal_change": True,
                "may_update_identity_core": False,
                "may_update_semantic_memory": False,
            }
        )
        claim_graph.setdefault("review_decisions", []).append(decision)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "claim_graph.claims",
                "operation": f"{normalized_action}_claim",
                "before": before_status,
                "after": review_status,
                "evidence": [claim_id] + list(claim.get("evidence", [])),
                "gate": "medium",
                "confidence": claim.get("confidence", 0.6),
                "claim_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_claim",
            target="claim_graph.claims",
            outcome=review_status,
            evidence=[claim_id] + list(claim.get("evidence", [])),
            metadata={
                "claim_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "patch_preview": patch_preview,
                "decision_note": decision_note,
            },
            state=state,
        )
        self.record_trace(
            workflow="claim_review",
            nodes=[
                {
                    "id": "claim",
                    "type": "Memory",
                    "claim_id": claim_id,
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
                {
                    "id": "patch_preview",
                    "type": "Decision",
                    "mode": "minimal_change_preview",
                    "would_mutate_identity_core": False,
                    "would_mutate_semantic_memory": False,
                },
            ],
            edges=[
                {"from": "claim", "to": "review", "type": "feedback"},
                {"from": "review", "to": "patch_preview", "type": "data_flow"},
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_claim",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "claim_decision": decision,
                }
            ],
            summary=f"Reviewed claim {claim_id} with action {normalized_action}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": review_status,
            "claim_id": claim_id,
            "snapshot_id": snapshot["snapshot_id"],
            "claim_decision_id": decision["decision_id"],
            "patch_preview": patch_preview,
        }

    def review_procedural_candidate(
        self,
        candidate_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in PROCEDURAL_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_procedural_review_action",
                "action": action,
            }
        state = self.load()
        task_hub = state.setdefault("task_hub", default_task_hub(utc_now(), state.get("working_state", {})))
        candidate = next(
            (
                item
                for item in task_hub.setdefault("procedural_candidates", [])
                if isinstance(item, dict) and item.get("candidate_id") == candidate_id
            ),
            None,
        )
        if candidate is None:
            return {
                "status": "not_found",
                "error": "procedural_candidate_not_found",
                "candidate_id": candidate_id,
            }

        now = utc_now()
        review_status = {
            "approve": "approved",
            "reject": "rejected",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        before_status = candidate.get("review_status", "pending")
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_procedural_candidate",
            target_path="task_hub.procedural_candidates",
            evidence=[candidate_id] + list(candidate.get("evidence", [])),
            metadata={
                "candidate_id": candidate_id,
                "review_action": normalized_action,
                "workflow": candidate.get("workflow"),
            },
        )
        decision = build_procedural_review_decision(
            candidate=candidate,
            action=normalized_action,
            result=review_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
        )

        procedural_memory_id = None
        target_path = "task_hub.procedural_candidates"
        after: object = review_status
        candidate["review_status"] = review_status
        candidate["reviewed_at"] = now
        candidate["reviewer"] = reviewer
        candidate["last_review_decision_id"] = decision["decision_id"]
        candidate.setdefault("review_history", []).append(decision)
        if normalized_action == "approve":
            procedural_memory = build_procedural_memory(candidate, decision, now)
            task_hub.setdefault("procedural_memory", []).append(procedural_memory)
            procedural_memory_id = procedural_memory["memory_id"]
            candidate["promoted_to"] = procedural_memory_id
            target_path = "task_hub.procedural_memory"
            after = procedural_memory_id
        elif normalized_action == "quarantine":
            candidate["quarantine_reason"] = decision_note or "procedural_review_quarantine"
        elif normalized_action == "archive":
            candidate["archive_reason"] = decision_note or "procedural_review_archive"
        task_hub.setdefault("procedural_review_decisions", []).append(decision)

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": target_path,
                "operation": f"{normalized_action}_procedural_candidate",
                "before": before_status,
                "after": after,
                "evidence": [candidate_id] + list(candidate.get("evidence", [])),
                "gate": "medium",
                "confidence": candidate.get("confidence", 0.5),
                "procedural_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_procedural_candidate",
            target=target_path,
            outcome=review_status,
            evidence=[candidate_id] + list(candidate.get("evidence", [])),
            metadata={
                "procedural_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "workflow": candidate.get("workflow"),
                "decision_note": decision_note,
                "procedural_memory_id": procedural_memory_id,
            },
            state=state,
        )
        self.record_trace(
            workflow="procedural_memory_review",
            nodes=[
                {
                    "id": "candidate",
                    "type": "Memory",
                    "candidate_id": candidate_id,
                    "workflow": candidate.get("workflow"),
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
                {
                    "id": "procedural_memory",
                    "type": "Memory",
                    "memory_id": procedural_memory_id,
                    "created": procedural_memory_id is not None,
                },
            ],
            edges=[
                {"from": "candidate", "to": "review", "type": "feedback"},
                {"from": "review", "to": "procedural_memory", "type": "memory_write"},
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": target_path,
                    "candidate_id": candidate_id,
                    "procedural_memory_id": procedural_memory_id,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_procedural_candidate",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "procedural_decision": decision,
                }
            ],
            summary=f"Reviewed procedural candidate {candidate_id} with action {normalized_action}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": review_status,
            "candidate_id": candidate_id,
            "procedural_memory_id": procedural_memory_id,
            "snapshot_id": snapshot["snapshot_id"],
            "procedural_decision_id": decision["decision_id"],
        }

    def apply_procedural_lifecycle_action(
        self,
        memory_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in PROCEDURAL_LIFECYCLE_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_procedural_lifecycle_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault("task_hub", default_task_hub(utc_now(), state.get("working_state", {})))
        memory = next(
            (
                item
                for item in task_hub.setdefault("procedural_memory", [])
                if isinstance(item, dict) and item.get("memory_id") == memory_id
            ),
            None,
        )
        if memory is None:
            return {
                "status": "not_found",
                "error": "procedural_memory_not_found",
                "memory_id": memory_id,
            }

        before_status = memory.get("lifecycle", {}).get("status") or memory.get("status")
        if before_status in {"archived", "discarded", "quarantined"}:
            return {
                "status": "already_reviewed",
                "memory_id": memory_id,
                "lifecycle_status": before_status,
            }

        now = utc_now()
        target_status = {
            "archive": "archived",
            "discard": "discarded",
            "quarantine": "quarantined",
        }[normalized_action]
        decision = {
            "decision_id": new_id("procedural_lifecycle_decision"),
            "timestamp": now,
            "memory_id": memory_id,
            "workflow": memory.get("workflow"),
            "reviewer": reviewer,
            "action": normalized_action,
            "result": target_status,
            "decision_note": decision_note,
            "memory_status_before": before_status,
            "snapshot_id": None,
            "risk": memory.get("risk", "medium"),
            "confidence": memory.get("confidence", 0.5),
            "evidence": [memory_id] + list(memory.get("evidence", [])),
            "rollback": {"reversible": True},
        }
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_procedural_memory",
            target_path="task_hub.procedural_memory",
            evidence=[memory_id] + list(memory.get("evidence", [])),
            metadata={
                "procedural_lifecycle_decision_id": decision["decision_id"],
                "memory_id": memory_id,
                "memory_status": before_status,
                "workflow": memory.get("workflow"),
            },
        )
        memory["status"] = target_status
        memory["review_status"] = target_status
        memory["reviewed_at"] = now
        memory["reviewer"] = reviewer
        memory["decision_note"] = decision_note
        memory["last_lifecycle_decision_id"] = decision["decision_id"]
        memory["lifecycle"] = {
            **memory.get("lifecycle", {}),
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        if normalized_action == "quarantine":
            memory["quarantine_reason"] = decision_note or "procedural_lifecycle_quarantine"
        if normalized_action == "discard":
            memory["discard_reason"] = decision_note or "procedural_lifecycle_discard"

        decision["snapshot_id"] = snapshot["snapshot_id"]
        task_hub.setdefault("procedural_lifecycle_decisions", []).append(decision)
        memory.setdefault("lifecycle_history", []).append(decision)
        memory.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_procedural_memory",
                "evidence": [memory_id],
                "procedural_lifecycle_decision_id": decision["decision_id"],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.procedural_memory",
                "operation": f"{normalized_action}_procedural_memory",
                "before": before_status,
                "after": target_status,
                "evidence": [memory_id] + list(memory.get("evidence", [])),
                "gate": "medium",
                "confidence": memory.get("confidence", 0.5),
                "procedural_lifecycle_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_procedural_memory_lifecycle",
            target="task_hub.procedural_memory",
            outcome=target_status,
            evidence=[memory_id] + list(memory.get("evidence", [])),
            metadata={
                "procedural_lifecycle_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "memory_id": memory_id,
                "decision_note": decision_note,
            },
            state=state,
        )
        self.record_trace(
            workflow="procedural_memory_lifecycle",
            nodes=[
                {
                    "id": "procedural_memory",
                    "type": "Memory",
                    "memory_id": memory_id,
                },
                {
                    "id": "lifecycle_review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[{"from": "procedural_memory", "to": "lifecycle_review", "type": "feedback"}],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.procedural_memory",
                    "memory_id": memory_id,
                    "procedural_lifecycle_decision_id": decision["decision_id"],
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_procedural_memory",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "procedural_lifecycle_decision": decision,
                }
            ],
            summary=f"Applied lifecycle action {normalized_action} to procedural memory {memory_id}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "memory_id": memory_id,
            "snapshot_id": snapshot["snapshot_id"],
            "procedural_lifecycle_decision_id": decision["decision_id"],
        }

    def review_cautionary_procedural_candidate(
        self,
        candidate_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in CAUTIONARY_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_cautionary_review_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault("task_hub", default_task_hub(utc_now(), state.get("working_state", {})))
        candidate = next(
            (
                item
                for item in task_hub.setdefault("cautionary_procedural_candidates", [])
                if isinstance(item, dict) and item.get("candidate_id") == candidate_id
            ),
            None,
        )
        if candidate is None:
            return {
                "status": "not_found",
                "error": "cautionary_candidate_not_found",
                "candidate_id": candidate_id,
            }

        now = utc_now()
        review_status = {
            "approve": "approved",
            "reject": "rejected",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        before_status = candidate.get("review_status", "pending")
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_cautionary_procedural_candidate",
            target_path="task_hub.cautionary_procedural_candidates",
            evidence=[candidate_id] + list(candidate.get("evidence", [])),
            metadata={
                "candidate_id": candidate_id,
                "review_action": normalized_action,
                "workflow": candidate.get("workflow"),
                "source_reflection_id": candidate.get("source_reflection_id"),
            },
        )
        decision = build_cautionary_review_decision(
            candidate=candidate,
            action=normalized_action,
            result=review_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
        )

        cautionary_memory_id = None
        target_path = "task_hub.cautionary_procedural_candidates"
        after: object = review_status
        candidate["review_status"] = review_status
        candidate["reviewed_at"] = now
        candidate["reviewer"] = reviewer
        candidate["last_review_decision_id"] = decision["decision_id"]
        candidate.setdefault("review_history", []).append(decision)
        if normalized_action == "approve":
            warning = build_cautionary_procedural_memory(candidate, decision, now)
            task_hub.setdefault("cautionary_procedural_memory", []).append(warning)
            cautionary_memory_id = warning["memory_id"]
            candidate["promoted_to"] = cautionary_memory_id
            target_path = "task_hub.cautionary_procedural_memory"
            after = cautionary_memory_id
        elif normalized_action == "quarantine":
            candidate["quarantine_reason"] = decision_note or "cautionary_review_quarantine"
        elif normalized_action == "archive":
            candidate["archive_reason"] = decision_note or "cautionary_review_archive"
        task_hub.setdefault("cautionary_review_decisions", []).append(decision)

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": target_path,
                "operation": f"{normalized_action}_cautionary_procedural_candidate",
                "before": before_status,
                "after": after,
                "evidence": [candidate_id] + list(candidate.get("evidence", [])),
                "gate": "medium",
                "confidence": candidate.get("confidence", 0.5),
                "cautionary_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_cautionary_procedural_candidate",
            target=target_path,
            outcome=review_status,
            evidence=[candidate_id] + list(candidate.get("evidence", [])),
            metadata={
                "cautionary_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "workflow": candidate.get("workflow"),
                "source_reflection_id": candidate.get("source_reflection_id"),
                "decision_note": decision_note,
                "cautionary_memory_id": cautionary_memory_id,
                "executable_policy_created": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="cautionary_procedural_review",
            nodes=[
                {
                    "id": "candidate",
                    "type": "Memory",
                    "candidate_id": candidate_id,
                    "workflow": candidate.get("workflow"),
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
                {
                    "id": "cautionary_warning",
                    "type": "Memory",
                    "memory_id": cautionary_memory_id,
                    "created": cautionary_memory_id is not None,
                    "executable_policy": False,
                },
            ],
            edges=[
                {"from": "candidate", "to": "review", "type": "feedback"},
                {"from": "review", "to": "cautionary_warning", "type": "memory_write"},
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": target_path,
                    "candidate_id": candidate_id,
                    "cautionary_memory_id": cautionary_memory_id,
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_cautionary_procedural_candidate",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "cautionary_decision": decision,
                }
            ],
            summary=(
                f"Reviewed cautionary procedural candidate {candidate_id} "
                f"with action {normalized_action}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": review_status,
            "candidate_id": candidate_id,
            "cautionary_memory_id": cautionary_memory_id,
            "snapshot_id": snapshot["snapshot_id"],
            "cautionary_decision_id": decision["decision_id"],
        }

    def apply_cautionary_warning_lifecycle_action(
        self,
        memory_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in CAUTIONARY_LIFECYCLE_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_cautionary_lifecycle_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault("task_hub", default_task_hub(utc_now(), state.get("working_state", {})))
        warning = next(
            (
                item
                for item in task_hub.setdefault("cautionary_procedural_memory", [])
                if isinstance(item, dict) and item.get("memory_id") == memory_id
            ),
            None,
        )
        if warning is None:
            return {
                "status": "not_found",
                "error": "cautionary_warning_not_found",
                "memory_id": memory_id,
            }

        before_status = warning.get("lifecycle", {}).get("status") or warning.get("status")
        if before_status in {"archived", "discarded", "quarantined"}:
            return {
                "status": "already_reviewed",
                "memory_id": memory_id,
                "lifecycle_status": before_status,
            }

        now = utc_now()
        target_status = {
            "archive": "archived",
            "discard": "discarded",
            "quarantine": "quarantined",
        }[normalized_action]
        decision = {
            "decision_id": new_id("cautionary_lifecycle_decision"),
            "timestamp": now,
            "memory_id": memory_id,
            "workflow": warning.get("workflow"),
            "source_reflection_id": warning.get("source_reflection_id"),
            "reviewer": reviewer,
            "action": normalized_action,
            "result": target_status,
            "decision_note": decision_note,
            "memory_status_before": before_status,
            "snapshot_id": None,
            "risk": warning.get("risk", "medium"),
            "confidence": warning.get("confidence", 0.5),
            "evidence": [memory_id] + list(warning.get("evidence", [])),
            "executable_policy_created": False,
            "rollback": {"reversible": True},
        }
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_cautionary_warning",
            target_path="task_hub.cautionary_procedural_memory",
            evidence=[memory_id] + list(warning.get("evidence", [])),
            metadata={
                "cautionary_lifecycle_decision_id": decision["decision_id"],
                "memory_id": memory_id,
                "memory_status": before_status,
                "workflow": warning.get("workflow"),
                "source_reflection_id": warning.get("source_reflection_id"),
                "executable_policy_created": False,
            },
        )
        warning["status"] = target_status
        warning["review_status"] = target_status
        warning["reviewed_at"] = now
        warning["reviewer"] = reviewer
        warning["decision_note"] = decision_note
        warning["last_lifecycle_decision_id"] = decision["decision_id"]
        warning["executable_policy"] = False
        warning["lifecycle"] = {
            **warning.get("lifecycle", {}),
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        if normalized_action == "quarantine":
            warning["quarantine_reason"] = decision_note or "cautionary_lifecycle_quarantine"
        if normalized_action == "discard":
            warning["discard_reason"] = decision_note or "cautionary_lifecycle_discard"

        decision["snapshot_id"] = snapshot["snapshot_id"]
        task_hub.setdefault("cautionary_lifecycle_decisions", []).append(decision)
        warning.setdefault("lifecycle_history", []).append(decision)
        warning.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_cautionary_warning",
                "evidence": [memory_id],
                "cautionary_lifecycle_decision_id": decision["decision_id"],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.cautionary_procedural_memory",
                "operation": f"{normalized_action}_cautionary_warning",
                "before": before_status,
                "after": target_status,
                "evidence": [memory_id] + list(warning.get("evidence", [])),
                "gate": "medium",
                "confidence": warning.get("confidence", 0.5),
                "cautionary_lifecycle_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_cautionary_warning_lifecycle",
            target="task_hub.cautionary_procedural_memory",
            outcome=target_status,
            evidence=[memory_id] + list(warning.get("evidence", [])),
            metadata={
                "cautionary_lifecycle_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "memory_id": memory_id,
                "decision_note": decision_note,
                "executable_policy_created": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="cautionary_warning_lifecycle",
            nodes=[
                {
                    "id": "cautionary_warning",
                    "type": "Memory",
                    "memory_id": memory_id,
                    "executable_policy": False,
                },
                {
                    "id": "lifecycle_review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[{"from": "cautionary_warning", "to": "lifecycle_review", "type": "feedback"}],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.cautionary_procedural_memory",
                    "cautionary_memory_id": memory_id,
                    "cautionary_lifecycle_decision_id": decision["decision_id"],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_cautionary_warning",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "cautionary_lifecycle_decision": decision,
                }
            ],
            summary=f"Applied lifecycle action {normalized_action} to cautionary warning {memory_id}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "memory_id": memory_id,
            "snapshot_id": snapshot["snapshot_id"],
            "cautionary_lifecycle_decision_id": decision["decision_id"],
        }

    def record_failure_reflection(
        self,
        workflow: str,
        summary: str,
        lesson: str,
        reviewer: str = "manual_review",
        action_id: Optional[str] = None,
        next_action: str = "",
    ) -> dict:
        normalized_workflow = str(workflow or "").strip()
        normalized_summary = str(summary or "").strip()
        normalized_lesson = str(lesson or "").strip()
        if not normalized_workflow:
            return {
                "status": "rejected",
                "error": "missing_workflow",
            }
        if not normalized_summary or not normalized_lesson:
            return {
                "status": "rejected",
                "error": "missing_failure_reflection",
            }

        state = self.load()
        now = utc_now()
        task_hub = state.setdefault("task_hub", default_task_hub(now, state.get("working_state", {})))
        source_action = find_task_action(
            task_hub.get("action_trace", []),
            action_id=action_id,
            workflow=normalized_workflow,
            statuses={"failed", "blocked"},
        )
        source_action_id = source_action.get("action_id") if source_action else action_id
        reflection = {
            "reflection_id": new_id("failure_reflection"),
            "timestamp": now,
            "workflow": normalized_workflow,
            "summary": normalized_summary,
            "lesson": normalized_lesson,
            "next_action": next_action,
            "source_action_id": source_action_id,
            "status": "active",
            "reviewer": reviewer,
            "evidence": [item for item in [source_action_id] if item],
            "provenance": [
                {
                    "type": "failure_reflection",
                    "source_action_id": source_action_id,
                }
            ],
        }
        caution = {
            "candidate_id": new_id("caution"),
            "timestamp": now,
            "workflow": normalized_workflow,
            "statement": f"Failure reflection for workflow '{normalized_workflow}': {normalized_lesson}",
            "avoid": normalized_summary,
            "next_action": next_action,
            "evidence": [reflection["reflection_id"]] + reflection["evidence"],
            "confidence": 0.6,
            "risk": "medium",
            "review_status": "pending",
            "recommended_action": "review_then_consider",
            "source_reflection_id": reflection["reflection_id"],
            "provenance": [
                {
                    "type": "failure_reflection_caution",
                    "reflection_id": reflection["reflection_id"],
                }
            ],
        }
        task_hub.setdefault("failure_reflections", []).append(reflection)
        task_hub.setdefault("cautionary_procedural_candidates", []).append(caution)
        reflection_log_entry = build_reflection_log_entry(
            timestamp=now,
            reflection_type="failure",
            workflow=normalized_workflow,
            observation=normalized_summary,
            lesson=normalized_lesson,
            expected_behavior=next_action,
            actor=reviewer,
            source_ids=[reflection["reflection_id"]] + reflection["evidence"],
            evidence=[reflection["reflection_id"]] + reflection["evidence"],
            risk=caution["risk"],
            confidence=caution["confidence"],
        )
        task_hub.setdefault("reflection_log", []).append(reflection_log_entry)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.failure_reflections",
                "operation": "record_failure_reflection",
                "before": None,
                "after": reflection["reflection_id"],
                "evidence": reflection["evidence"],
                "gate": "medium",
                "confidence": caution["confidence"],
                "reflection_log_id": reflection_log_entry["reflection_id"],
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action="record_failure_reflection",
            target="task_hub.failure_reflections",
            outcome="recorded",
            evidence=reflection["evidence"],
            metadata={
                "reflection_id": reflection["reflection_id"],
                "cautionary_candidate_id": caution["candidate_id"],
                "reflection_log_id": reflection_log_entry["reflection_id"],
                "workflow": normalized_workflow,
            },
            state=state,
        )
        self.record_trace(
            workflow="failure_reflection",
            nodes=[
                {
                    "id": "failed_action",
                    "type": "Action",
                    "action_id": source_action_id,
                    "workflow": normalized_workflow,
                },
                {
                    "id": "reflection",
                    "type": "Review",
                    "reflection_id": reflection["reflection_id"],
                },
                {
                    "id": "reflection_log",
                    "type": "Memory",
                    "reflection_id": reflection_log_entry["reflection_id"],
                },
                {
                    "id": "caution",
                    "type": "Memory",
                    "candidate_id": caution["candidate_id"],
                },
            ],
            edges=[
                {"from": "failed_action", "to": "reflection", "type": "reflection"},
                {"from": "reflection", "to": "reflection_log", "type": "memory_write"},
                {"from": "reflection", "to": "caution", "type": "proposal"},
            ],
            memory_events=[
                {
                    "operation": "record",
                    "target": "task_hub.failure_reflections",
                    "memory_id": reflection["reflection_id"],
                    "candidate_id": caution["candidate_id"],
                    "reflection_id": reflection_log_entry["reflection_id"],
                }
            ],
            review_events=[
                {
                    "operation": "failure_reflection",
                    "reviewer": reviewer,
                    "lesson": normalized_lesson,
                    "next_action": next_action,
                }
            ],
            summary=f"Recorded failure reflection for workflow {normalized_workflow}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "recorded",
            "reflection_id": reflection["reflection_id"],
            "reflection_log_id": reflection_log_entry["reflection_id"],
            "cautionary_candidate_id": caution["candidate_id"],
            "source_action_id": source_action_id,
        }

    def record_reflection_log(
        self,
        reflection_type: str,
        workflow: str,
        observation: str,
        lesson: str,
        expected_behavior: str,
        actor: str = "manual_review",
        source_ids: Optional[List[str]] = None,
        evidence: Optional[List[str]] = None,
        risk: str = "medium",
        confidence: float = 0.5,
    ) -> dict:
        normalized_workflow = str(workflow or "").strip()
        normalized_observation = str(observation or "").strip()
        normalized_lesson = str(lesson or "").strip()
        if not normalized_workflow:
            return {"status": "rejected", "error": "missing_workflow"}
        if not normalized_observation or not normalized_lesson:
            return {"status": "rejected", "error": "missing_reflection"}

        state = self.load()
        now = utc_now()
        task_hub = state.setdefault("task_hub", default_task_hub(now, state.get("working_state", {})))
        entry = build_reflection_log_entry(
            timestamp=now,
            reflection_type=reflection_type,
            workflow=normalized_workflow,
            observation=normalized_observation,
            lesson=normalized_lesson,
            expected_behavior=expected_behavior,
            actor=actor,
            source_ids=source_ids or [],
            evidence=evidence or source_ids or [],
            risk=risk,
            confidence=confidence,
        )
        task_hub.setdefault("reflection_log", []).append(entry)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": actor,
                "target_path": "task_hub.reflection_log",
                "operation": "record_reflection_log",
                "before": None,
                "after": entry["reflection_id"],
                "evidence": entry["evidence"],
                "gate": "medium",
                "confidence": entry["confidence"],
                "reflection_log_id": entry["reflection_id"],
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=actor,
            action="record_reflection_log",
            target="task_hub.reflection_log",
            outcome="recorded",
            evidence=entry["evidence"],
            metadata={
                "reflection_log_id": entry["reflection_id"],
                "workflow": normalized_workflow,
                "reflection_type": entry["reflection_type"],
            },
            state=state,
        )
        self.record_trace(
            workflow="reflection_log",
            nodes=[
                {
                    "id": "observation",
                    "type": "Review",
                    "summary": normalized_observation,
                },
                {
                    "id": "reflection_log",
                    "type": "Memory",
                    "reflection_id": entry["reflection_id"],
                },
            ],
            edges=[{"from": "observation", "to": "reflection_log", "type": "memory_write"}],
            memory_events=[
                {
                    "operation": "record",
                    "target": "task_hub.reflection_log",
                    "reflection_id": entry["reflection_id"],
                }
            ],
            review_events=[
                {
                    "operation": "record_reflection_log",
                    "actor": actor,
                    "expected_behavior": expected_behavior,
                }
            ],
            summary=f"Recorded reflection log entry {entry['reflection_id']}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "recorded",
            "reflection_log_id": entry["reflection_id"],
        }

    def verify_reflection(
        self,
        reflection_id: str,
        result: str,
        verifier: str = "manual_review",
        evidence: Optional[List[str]] = None,
        note: str = "",
    ) -> dict:
        normalized_result = str(result or "").strip().lower()
        if normalized_result not in REFLECTION_VERIFICATION_RESULTS:
            return {
                "status": "rejected",
                "error": "unsupported_reflection_verification_result",
                "result": result,
            }

        state = self.load()
        task_hub = state.setdefault("task_hub", default_task_hub(utc_now(), state.get("working_state", {})))
        entry = next(
            (
                item
                for item in task_hub.setdefault("reflection_log", [])
                if isinstance(item, dict) and item.get("reflection_id") == reflection_id
            ),
            None,
        )
        if entry is None:
            return {
                "status": "not_found",
                "error": "reflection_not_found",
                "reflection_id": reflection_id,
            }

        now = utc_now()
        verification = {
            "verification_id": new_id("reflection_verification"),
            "timestamp": now,
            "reflection_id": reflection_id,
            "verifier": verifier,
            "result": normalized_result,
            "note": note,
            "evidence": evidence or [],
        }
        before_status = entry.get("status", "open")
        status_by_result = {
            "verified": "verified",
            "not_observed": "open",
            "regressed": "needs_revision",
            "superseded": "superseded",
        }
        entry["status"] = status_by_result[normalized_result]
        entry["verification_status"] = normalized_result
        entry["last_verified_at"] = now
        entry["last_verification_id"] = verification["verification_id"]
        entry.setdefault("verification_history", []).append(verification)
        entry.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": verifier,
                "operation": "verify_reflection",
                "reflection_verification_id": verification["verification_id"],
                "evidence": evidence or [],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": verifier,
                "target_path": "task_hub.reflection_log",
                "operation": "verify_reflection",
                "before": before_status,
                "after": entry["status"],
                "evidence": [reflection_id] + list(evidence or []),
                "gate": "medium",
                "confidence": entry.get("confidence", 0.5),
                "reflection_verification_id": verification["verification_id"],
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=verifier,
            action="verify_reflection",
            target="task_hub.reflection_log",
            outcome=entry["status"],
            evidence=[reflection_id] + list(evidence or []),
            metadata={
                "reflection_id": reflection_id,
                "reflection_verification_id": verification["verification_id"],
                "result": normalized_result,
            },
            state=state,
        )
        self.record_trace(
            workflow="reflection_verification",
            nodes=[
                {
                    "id": "reflection_log",
                    "type": "Memory",
                    "reflection_id": reflection_id,
                },
                {
                    "id": "verification",
                    "type": "Review",
                    "result": normalized_result,
                },
            ],
            edges=[{"from": "reflection_log", "to": "verification", "type": "feedback"}],
            review_events=[
                {
                    "operation": "verify_reflection",
                    "verifier": verifier,
                    "verification": verification,
                }
            ],
            summary=f"Verified reflection {reflection_id} as {normalized_result}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": entry["status"],
            "reflection_id": reflection_id,
            "reflection_verification_id": verification["verification_id"],
        }

    def review_reflection_guidance(
        self,
        guidance_item_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in REFLECTION_GUIDANCE_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_reflection_guidance_review_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        item = next(
            (
                entry
                for entry in task_hub.setdefault("reflection_guidance_queue", [])
                if isinstance(entry, dict)
                and entry.get("guidance_item_id") == guidance_item_id
            ),
            None,
        )
        if item is None:
            return {
                "status": "not_found",
                "error": "reflection_guidance_item_not_found",
                "guidance_item_id": guidance_item_id,
            }

        before_status = item.get("review_status", "pending")
        if before_status in {"acknowledged", "archived", "quarantined"}:
            return {
                "status": "already_reviewed",
                "guidance_item_id": guidance_item_id,
                "review_status": before_status,
            }

        now = utc_now()
        target_status = {
            "acknowledge": "acknowledged",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_reflection_guidance",
            target_path="task_hub.reflection_guidance_queue",
            evidence=[guidance_item_id] + list(item.get("evidence", [])),
            metadata={
                "guidance_item_id": guidance_item_id,
                "reflection_id": item.get("reflection_id"),
                "workflow": item.get("workflow"),
                "review_action": normalized_action,
                "executable_policy_created": False,
            },
        )
        decision = build_reflection_guidance_decision(
            item=item,
            action=normalized_action,
            result=target_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
        )
        item["review_status"] = target_status
        item["reviewed_at"] = now
        item["reviewer"] = reviewer
        item["decision_note"] = decision_note
        item["last_review_decision_id"] = decision["decision_id"]
        item["execution_prohibited"] = True
        item["executable_policy_created"] = False
        item["identity_mutation_allowed"] = False
        item.setdefault("review_history", []).append(decision)
        task_hub.setdefault("reflection_guidance_decisions", []).append(decision)

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.reflection_guidance_queue",
                "operation": f"{normalized_action}_reflection_guidance",
                "before": before_status,
                "after": target_status,
                "evidence": [guidance_item_id] + list(item.get("evidence", [])),
                "gate": "medium",
                "confidence": item.get("signal_inputs", {}).get("confidence", 0.5),
                "reflection_guidance_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_reflection_guidance",
            target="task_hub.reflection_guidance_queue",
            outcome=target_status,
            evidence=[guidance_item_id] + list(item.get("evidence", [])),
            metadata={
                "reflection_guidance_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "guidance_item_id": guidance_item_id,
                "reflection_id": item.get("reflection_id"),
                "workflow": item.get("workflow"),
                "decision_note": decision_note,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="reflection_guidance_review",
            nodes=[
                {
                    "id": "reflection_guidance",
                    "type": "ReviewQueueItem",
                    "guidance_item_id": guidance_item_id,
                    "reflection_id": item.get("reflection_id"),
                    "workflow": item.get("workflow"),
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[{"from": "reflection_guidance", "to": "review", "type": "feedback"}],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.reflection_guidance_queue",
                    "reflection_guidance_item_id": guidance_item_id,
                    "reflection_guidance_decision_id": decision["decision_id"],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_reflection_guidance",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "reflection_guidance_decision": decision,
                }
            ],
            summary=(
                f"Reviewed reflection guidance {guidance_item_id} "
                f"with action {normalized_action}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "guidance_item_id": guidance_item_id,
            "reflection_guidance_decision_id": decision["decision_id"],
            "snapshot_id": snapshot["snapshot_id"],
        }

    def propose_tool_safety_policy(
        self,
        guidance_item_id: str,
        policy_scope: str,
        proposed_rule: str,
        proposer: str = "manual_review",
        rationale: str = "",
        risk: str = "medium",
        confidence: float = 0.5,
    ) -> dict:
        normalized_scope = str(policy_scope or "").strip()
        normalized_rule = str(proposed_rule or "").strip()
        if not normalized_scope:
            return {"status": "rejected", "error": "missing_policy_scope"}
        if not normalized_rule:
            return {"status": "rejected", "error": "missing_proposed_rule"}

        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        guidance_item = next(
            (
                item
                for item in task_hub.setdefault("reflection_guidance_queue", [])
                if isinstance(item, dict)
                and item.get("guidance_item_id") == guidance_item_id
            ),
            None,
        )
        if guidance_item is None:
            return {
                "status": "not_found",
                "error": "reflection_guidance_item_not_found",
                "guidance_item_id": guidance_item_id,
            }
        if guidance_item.get("review_status") not in {"acknowledged", "archived"}:
            return {
                "status": "rejected",
                "error": "guidance_not_reviewed",
                "guidance_item_id": guidance_item_id,
                "review_status": guidance_item.get("review_status"),
            }

        now = utc_now()
        proposal = build_tool_safety_policy_proposal(
            guidance_item=guidance_item,
            policy_scope=normalized_scope,
            proposed_rule=normalized_rule,
            proposer=proposer,
            rationale=rationale,
            risk=risk,
            confidence=confidence,
            timestamp=now,
        )
        proposal["proposal_score"] = score_tool_safety_policy_proposal(
            proposal,
            timestamp=now,
        )
        task_hub.setdefault("tool_safety_policy_proposals", []).append(proposal)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": proposer,
                "target_path": "task_hub.tool_safety_policy_proposals",
                "operation": "propose_tool_safety_policy",
                "before": None,
                "after": proposal["proposal_id"],
                "evidence": proposal["evidence"],
                "gate": "medium",
                "confidence": proposal["confidence"],
                "tool_safety_policy_proposal_id": proposal["proposal_id"],
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=proposer,
            action="propose_tool_safety_policy",
            target="task_hub.tool_safety_policy_proposals",
            outcome="proposed",
            evidence=proposal["evidence"],
            metadata={
                "proposal_id": proposal["proposal_id"],
                "guidance_item_id": guidance_item_id,
                "reflection_id": guidance_item.get("reflection_id"),
                "policy_scope": normalized_scope,
                "executable_policy_created": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="tool_safety_policy_proposal",
            nodes=[
                {
                    "id": "reflection_guidance",
                    "type": "ReviewQueueItem",
                    "guidance_item_id": guidance_item_id,
                    "reflection_id": guidance_item.get("reflection_id"),
                },
                {
                    "id": "policy_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": proposal["proposal_id"],
                    "policy_scope": normalized_scope,
                    "executable_policy": False,
                },
            ],
            edges=[
                {
                    "from": "reflection_guidance",
                    "to": "policy_proposal",
                    "type": "proposal",
                }
            ],
            memory_events=[
                {
                    "operation": "propose",
                    "target": "task_hub.tool_safety_policy_proposals",
                    "tool_safety_policy_proposal_id": proposal["proposal_id"],
                    "reflection_guidance_item_id": guidance_item_id,
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": "propose_tool_safety_policy",
                    "proposer": proposer,
                    "policy_scope": normalized_scope,
                    "rationale": rationale,
                }
            ],
            summary=(
                f"Proposed non-executable tool/safety policy "
                f"{proposal['proposal_id']}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "proposed",
            "proposal_id": proposal["proposal_id"],
            "guidance_item_id": guidance_item_id,
        }

    def review_tool_safety_policy_proposal(
        self,
        proposal_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in TOOL_SAFETY_POLICY_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_tool_safety_policy_review_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        proposal = next(
            (
                item
                for item in task_hub.setdefault("tool_safety_policy_proposals", [])
                if isinstance(item, dict) and item.get("proposal_id") == proposal_id
            ),
            None,
        )
        if proposal is None:
            return {
                "status": "not_found",
                "error": "tool_safety_policy_proposal_not_found",
                "proposal_id": proposal_id,
            }
        before_status = proposal.get("review_status", "pending")
        if before_status in {"approved", "rejected", "archived", "quarantined"}:
            return {
                "status": "already_reviewed",
                "proposal_id": proposal_id,
                "review_status": before_status,
            }

        now = utc_now()
        result = {
            "approve": "approved",
            "reject": "rejected",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_tool_safety_policy_proposal",
            target_path="task_hub.tool_safety_policy_proposals",
            evidence=[proposal_id] + list(proposal.get("evidence", [])),
            metadata={
                "proposal_id": proposal_id,
                "guidance_item_id": proposal.get("source_guidance_item_id"),
                "reflection_id": proposal.get("source_reflection_id"),
                "policy_scope": proposal.get("policy_scope"),
                "executable_policy_created": False,
            },
        )
        decision = build_tool_safety_policy_decision(
            proposal=proposal,
            action=normalized_action,
            result=result,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
        )
        proposal["review_status"] = result
        proposal["reviewed_at"] = now
        proposal["reviewer"] = reviewer
        proposal["decision_note"] = decision_note
        proposal["last_review_decision_id"] = decision["decision_id"]
        proposal["executable_policy_created"] = False
        proposal["executable_policy"] = False
        proposal["identity_mutation_allowed"] = False
        proposal["proposal_score"] = score_tool_safety_policy_proposal(
            proposal,
            timestamp=now,
        )
        decision["proposal_score"] = proposal["proposal_score"]
        proposal.setdefault("review_history", []).append(decision)
        task_hub.setdefault("tool_safety_policy_decisions", []).append(decision)

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.tool_safety_policy_proposals",
                "operation": f"{normalized_action}_tool_safety_policy_proposal",
                "before": before_status,
                "after": result,
                "evidence": [proposal_id] + list(proposal.get("evidence", [])),
                "gate": "medium",
                "confidence": proposal.get("confidence", 0.5),
                "tool_safety_policy_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_tool_safety_policy_proposal",
            target="task_hub.tool_safety_policy_proposals",
            outcome=result,
            evidence=[proposal_id] + list(proposal.get("evidence", [])),
            metadata={
                "tool_safety_policy_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "proposal_id": proposal_id,
                "policy_scope": proposal.get("policy_scope"),
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="tool_safety_policy_review",
            nodes=[
                {
                    "id": "policy_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": proposal_id,
                    "policy_scope": proposal.get("policy_scope"),
                    "executable_policy": False,
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[{"from": "policy_proposal", "to": "review", "type": "feedback"}],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.tool_safety_policy_proposals",
                    "tool_safety_policy_proposal_id": proposal_id,
                    "tool_safety_policy_decision_id": decision["decision_id"],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_tool_safety_policy_proposal",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "tool_safety_policy_decision": decision,
                }
            ],
            summary=(
                f"Reviewed tool/safety policy proposal {proposal_id} "
                f"with action {normalized_action}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": result,
            "proposal_id": proposal_id,
            "tool_safety_policy_decision_id": decision["decision_id"],
            "snapshot_id": snapshot["snapshot_id"],
        }

    def link_tool_safety_policy_proposals(
        self,
        from_proposal_id: str,
        to_proposal_id: str,
        link_type: str,
        reviewer: str = "manual_review",
        reason: str = "",
        evidence: Optional[List[str]] = None,
        confidence: float = 0.5,
    ) -> dict:
        normalized_type = str(link_type or "").strip().lower()
        if normalized_type not in TOOL_SAFETY_POLICY_LINK_TYPES:
            return {
                "status": "rejected",
                "error": "unsupported_tool_safety_policy_link_type",
                "link_type": link_type,
            }
        if from_proposal_id == to_proposal_id:
            return {
                "status": "rejected",
                "error": "self_link_not_allowed",
                "proposal_id": from_proposal_id,
            }

        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        proposals = [
            item
            for item in task_hub.setdefault("tool_safety_policy_proposals", [])
            if isinstance(item, dict)
        ]
        from_proposal = next(
            (
                item
                for item in proposals
                if item.get("proposal_id") == from_proposal_id
            ),
            None,
        )
        to_proposal = next(
            (
                item
                for item in proposals
                if item.get("proposal_id") == to_proposal_id
            ),
            None,
        )
        if from_proposal is None or to_proposal is None:
            return {
                "status": "not_found",
                "error": "tool_safety_policy_proposal_not_found",
                "from_proposal_id": from_proposal_id,
                "to_proposal_id": to_proposal_id,
            }

        now = utc_now()
        link = build_tool_safety_policy_link(
            from_proposal=from_proposal,
            to_proposal=to_proposal,
            link_type=normalized_type,
            reviewer=reviewer,
            reason=reason,
            evidence=evidence or [],
            confidence=confidence,
            timestamp=now,
        )
        existing = next(
            (
                item
                for item in task_hub.setdefault("tool_safety_policy_links", [])
                if isinstance(item, dict)
                and item.get("from_proposal_id") == from_proposal_id
                and item.get("to_proposal_id") == to_proposal_id
                and item.get("link_type") == normalized_type
                and item.get("status") == "active"
            ),
            None,
        )
        if existing is not None:
            return {
                "status": "duplicate",
                "link_id": existing.get("link_id"),
                "from_proposal_id": from_proposal_id,
                "to_proposal_id": to_proposal_id,
                "link_type": normalized_type,
            }

        task_hub.setdefault("tool_safety_policy_links", []).append(link)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.tool_safety_policy_links",
                "operation": "link_tool_safety_policy_proposals",
                "before": None,
                "after": link["link_id"],
                "evidence": link["evidence"],
                "gate": "medium",
                "confidence": link["confidence"],
                "tool_safety_policy_link_id": link["link_id"],
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action="link_tool_safety_policy_proposals",
            target="task_hub.tool_safety_policy_links",
            outcome="linked",
            evidence=link["evidence"],
            metadata={
                "tool_safety_policy_link_id": link["link_id"],
                "from_proposal_id": from_proposal_id,
                "to_proposal_id": to_proposal_id,
                "link_type": normalized_type,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="tool_safety_policy_link",
            nodes=[
                {
                    "id": "from_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": from_proposal_id,
                    "policy_scope": from_proposal.get("policy_scope"),
                    "executable_policy": False,
                },
                {
                    "id": "to_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": to_proposal_id,
                    "policy_scope": to_proposal.get("policy_scope"),
                    "executable_policy": False,
                },
                {
                    "id": "proposal_link",
                    "type": "PolicyProposalLink",
                    "link_id": link["link_id"],
                    "link_type": normalized_type,
                },
            ],
            edges=[
                {"from": "from_proposal", "to": "proposal_link", "type": "data_flow"},
                {"from": "proposal_link", "to": "to_proposal", "type": normalized_type},
            ],
            memory_events=[
                {
                    "operation": "link",
                    "target": "task_hub.tool_safety_policy_links",
                    "tool_safety_policy_link_id": link["link_id"],
                    "from_proposal_id": from_proposal_id,
                    "to_proposal_id": to_proposal_id,
                    "link_type": normalized_type,
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": "link_tool_safety_policy_proposals",
                    "reviewer": reviewer,
                    "reason": reason,
                    "tool_safety_policy_link": link,
                }
            ],
            summary=(
                f"Linked tool/safety policy proposal {from_proposal_id} "
                f"to {to_proposal_id} as {normalized_type}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "linked",
            "link_id": link["link_id"],
            "from_proposal_id": from_proposal_id,
            "to_proposal_id": to_proposal_id,
            "link_type": normalized_type,
        }

    def apply_tool_safety_policy_link_lifecycle_action(
        self,
        link_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in TOOL_SAFETY_POLICY_LINK_LIFECYCLE_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_tool_safety_policy_link_lifecycle_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        link = next(
            (
                item
                for item in task_hub.setdefault("tool_safety_policy_links", [])
                if isinstance(item, dict) and item.get("link_id") == link_id
            ),
            None,
        )
        if link is None:
            return {
                "status": "not_found",
                "error": "tool_safety_policy_link_not_found",
                "link_id": link_id,
            }

        lifecycle = link.get("lifecycle", {})
        before_status = (
            lifecycle.get("status") if isinstance(lifecycle, dict) else None
        ) or link.get("status", "active")
        if before_status in {"archived", "discarded", "quarantined"}:
            return {
                "status": "already_reviewed",
                "link_id": link_id,
                "lifecycle_status": before_status,
            }

        now = utc_now()
        target_status = {
            "archive": "archived",
            "discard": "discarded",
            "quarantine": "quarantined",
        }[normalized_action]
        decision = build_tool_safety_policy_link_lifecycle_decision(
            link=link,
            action=normalized_action,
            result=target_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=None,
            timestamp=now,
            before_status=before_status,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_tool_safety_policy_link",
            target_path="task_hub.tool_safety_policy_links",
            evidence=[link_id] + list(link.get("evidence", [])),
            metadata={
                "tool_safety_policy_link_lifecycle_decision_id": decision[
                    "decision_id"
                ],
                "tool_safety_policy_link_id": link_id,
                "link_status": before_status,
                "from_proposal_id": link.get("from_proposal_id"),
                "to_proposal_id": link.get("to_proposal_id"),
                "link_type": link.get("link_type"),
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
        )
        link["status"] = target_status
        link["review_status"] = target_status
        link["reviewed_at"] = now
        link["reviewer"] = reviewer
        link["decision_note"] = decision_note
        link["last_lifecycle_decision_id"] = decision["decision_id"]
        link["relationship_mode"] = "review_link_only"
        link["requires_review"] = True
        link["execution_prohibited"] = True
        link["executable_policy"] = False
        link["executable_policy_created"] = False
        link["identity_mutation_allowed"] = False
        link["lifecycle"] = {
            **(lifecycle if isinstance(lifecycle, dict) else {}),
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        if normalized_action == "quarantine":
            link["quarantine_reason"] = (
                decision_note or "tool_safety_policy_link_lifecycle_quarantine"
            )
        if normalized_action == "discard":
            link["discard_reason"] = (
                decision_note or "tool_safety_policy_link_lifecycle_discard"
            )

        decision["snapshot_id"] = snapshot["snapshot_id"]
        decision["rollback"]["snapshot_id"] = snapshot["snapshot_id"]
        task_hub.setdefault(
            "tool_safety_policy_link_lifecycle_decisions",
            [],
        ).append(decision)
        link.setdefault("lifecycle_history", []).append(decision)
        link.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_tool_safety_policy_link",
                "evidence": [link_id],
                "tool_safety_policy_link_lifecycle_decision_id": decision[
                    "decision_id"
                ],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.tool_safety_policy_links",
                "operation": f"{normalized_action}_tool_safety_policy_link",
                "before": before_status,
                "after": target_status,
                "evidence": [link_id] + list(link.get("evidence", [])),
                "gate": "medium",
                "confidence": link.get("confidence", 0.5),
                "tool_safety_policy_link_lifecycle_decision_id": decision[
                    "decision_id"
                ],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_tool_safety_policy_link_lifecycle",
            target="task_hub.tool_safety_policy_links",
            outcome=target_status,
            evidence=[link_id] + list(link.get("evidence", [])),
            metadata={
                "tool_safety_policy_link_lifecycle_decision_id": decision[
                    "decision_id"
                ],
                "snapshot_id": snapshot["snapshot_id"],
                "tool_safety_policy_link_id": link_id,
                "from_proposal_id": link.get("from_proposal_id"),
                "to_proposal_id": link.get("to_proposal_id"),
                "link_type": link.get("link_type"),
                "decision_note": decision_note,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="tool_safety_policy_link_lifecycle",
            nodes=[
                {
                    "id": "policy_link",
                    "type": "PolicyProposalLink",
                    "link_id": link_id,
                    "link_type": link.get("link_type"),
                    "relationship_mode": "review_link_only",
                },
                {
                    "id": "lifecycle_review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[
                {
                    "from": "policy_link",
                    "to": "lifecycle_review",
                    "type": "feedback",
                }
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.tool_safety_policy_links",
                    "tool_safety_policy_link_id": link_id,
                    "tool_safety_policy_link_lifecycle_decision_id": decision[
                        "decision_id"
                    ],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_tool_safety_policy_link",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "tool_safety_policy_link_lifecycle_decision": decision,
                }
            ],
            summary=(
                f"Applied lifecycle action {normalized_action} to tool/safety "
                f"policy proposal link {link_id}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "link_id": link_id,
            "snapshot_id": snapshot["snapshot_id"],
            "tool_safety_policy_link_lifecycle_decision_id": decision[
                "decision_id"
            ],
        }

    def bridge_tool_safety_policy_link_to_claim_graph(
        self,
        link_id: str,
        reviewer: str = "manual_review",
        rationale: str = "",
    ) -> dict:
        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        claim_graph = state.setdefault("claim_graph", default_claim_graph())
        claim_graph.setdefault("proposal_link_evidence", [])
        claim_graph.setdefault("links", [])
        link = next(
            (
                item
                for item in task_hub.setdefault("tool_safety_policy_links", [])
                if isinstance(item, dict) and item.get("link_id") == link_id
            ),
            None,
        )
        if link is None:
            return {
                "status": "not_found",
                "error": "tool_safety_policy_link_not_found",
                "link_id": link_id,
            }

        existing = next(
            (
                item
                for item in claim_graph.setdefault("proposal_link_evidence", [])
                if isinstance(item, dict)
                and item.get("source_link_id") == link_id
                and item.get("status") == "active"
            ),
            None,
        )
        if existing is not None:
            return {
                "status": "duplicate",
                "evidence_id": existing.get("evidence_id"),
                "link_id": link_id,
            }

        now = utc_now()
        evidence_record = build_proposal_link_claim_graph_evidence(
            link=link,
            reviewer=reviewer,
            rationale=rationale,
            timestamp=now,
        )
        claim_link = build_proposal_link_claim_graph_link(
            evidence_record=evidence_record,
            link=link,
            timestamp=now,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation="bridge_tool_safety_policy_link_to_claim_graph",
            target_path="claim_graph.proposal_link_evidence",
            evidence=evidence_record["evidence"],
            metadata={
                "proposal_link_evidence_id": evidence_record["evidence_id"],
                "tool_safety_policy_link_id": link_id,
                "claim_graph_link_id": claim_link["link_id"],
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
        )
        evidence_record["snapshot_id"] = snapshot["snapshot_id"]
        evidence_record["rollback"]["snapshot_id"] = snapshot["snapshot_id"]
        claim_graph.setdefault("proposal_link_evidence", []).append(evidence_record)
        add_claim_link(claim_graph, claim_link)
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "claim_graph.proposal_link_evidence",
                "operation": "bridge_tool_safety_policy_link_to_claim_graph",
                "before": None,
                "after": evidence_record["evidence_id"],
                "evidence": evidence_record["evidence"],
                "gate": "medium",
                "confidence": evidence_record["confidence"],
                "proposal_link_evidence_id": evidence_record["evidence_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action="bridge_tool_safety_policy_link_to_claim_graph",
            target="claim_graph.proposal_link_evidence",
            outcome="bridged",
            evidence=evidence_record["evidence"],
            metadata={
                "proposal_link_evidence_id": evidence_record["evidence_id"],
                "tool_safety_policy_link_id": link_id,
                "claim_graph_link_id": claim_link["link_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="proposal_link_claim_graph_bridge",
            nodes=[
                {
                    "id": "proposal_link",
                    "type": "PolicyProposalLink",
                    "link_id": link_id,
                    "link_type": link.get("link_type"),
                    "relationship_mode": "review_link_only",
                },
                {
                    "id": "claim_graph_evidence",
                    "type": "ClaimGraphEvidence",
                    "evidence_id": evidence_record["evidence_id"],
                    "claim_graph_mode": "evidence_bridge_only",
                },
            ],
            edges=[
                {
                    "from": "proposal_link",
                    "to": "claim_graph_evidence",
                    "type": "evidence_bridge",
                }
            ],
            memory_events=[
                {
                    "operation": "bridge",
                    "target": "claim_graph.proposal_link_evidence",
                    "proposal_link_evidence_id": evidence_record["evidence_id"],
                    "tool_safety_policy_link_id": link_id,
                    "claim_graph_link_id": claim_link["link_id"],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": "bridge_tool_safety_policy_link_to_claim_graph",
                    "reviewer": reviewer,
                    "rationale": rationale,
                    "proposal_link_evidence": evidence_record,
                }
            ],
            summary=(
                f"Bridged tool/safety policy proposal link {link_id} into "
                "claim graph evidence."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": "bridged",
            "evidence_id": evidence_record["evidence_id"],
            "link_id": link_id,
            "claim_graph_link_id": claim_link["link_id"],
            "snapshot_id": snapshot["snapshot_id"],
        }

    def apply_tool_safety_policy_lifecycle_action(
        self,
        proposal_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in TOOL_SAFETY_POLICY_LIFECYCLE_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_tool_safety_policy_lifecycle_action",
                "action": action,
            }

        state = self.load()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(utc_now(), state.get("working_state", {})),
        )
        proposal = next(
            (
                item
                for item in task_hub.setdefault("tool_safety_policy_proposals", [])
                if isinstance(item, dict) and item.get("proposal_id") == proposal_id
            ),
            None,
        )
        if proposal is None:
            return {
                "status": "not_found",
                "error": "tool_safety_policy_proposal_not_found",
                "proposal_id": proposal_id,
            }

        before_status = (
            proposal.get("lifecycle", {}).get("status")
            if isinstance(proposal.get("lifecycle"), dict)
            else None
        ) or proposal.get("status") or proposal.get("review_status", "pending")
        if before_status in {"archived", "discarded", "quarantined"}:
            return {
                "status": "already_reviewed",
                "proposal_id": proposal_id,
                "lifecycle_status": before_status,
            }

        now = utc_now()
        target_status = {
            "archive": "archived",
            "discard": "discarded",
            "quarantine": "quarantined",
        }[normalized_action]
        decision = build_tool_safety_policy_lifecycle_decision(
            proposal=proposal,
            action=normalized_action,
            result=target_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=None,
            timestamp=now,
            before_status=before_status,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_tool_safety_policy_proposal",
            target_path="task_hub.tool_safety_policy_proposals",
            evidence=[proposal_id] + list(proposal.get("evidence", [])),
            metadata={
                "tool_safety_policy_lifecycle_decision_id": decision["decision_id"],
                "proposal_id": proposal_id,
                "proposal_status": before_status,
                "policy_scope": proposal.get("policy_scope"),
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
        )
        proposal["status"] = target_status
        proposal["review_status"] = target_status
        proposal["reviewed_at"] = now
        proposal["reviewer"] = reviewer
        proposal["decision_note"] = decision_note
        proposal["last_lifecycle_decision_id"] = decision["decision_id"]
        proposal["proposal_mode"] = "proposal_only"
        proposal["requires_review"] = True
        proposal["execution_prohibited"] = True
        proposal["executable_policy"] = False
        proposal["executable_policy_created"] = False
        proposal["identity_mutation_allowed"] = False
        proposal["lifecycle"] = {
            **(
                proposal.get("lifecycle", {})
                if isinstance(proposal.get("lifecycle"), dict)
                else {}
            ),
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        if normalized_action == "quarantine":
            proposal["quarantine_reason"] = (
                decision_note or "tool_safety_policy_lifecycle_quarantine"
            )
        if normalized_action == "discard":
            proposal["discard_reason"] = (
                decision_note or "tool_safety_policy_lifecycle_discard"
            )
        proposal["proposal_score"] = score_tool_safety_policy_proposal(
            proposal,
            timestamp=now,
        )

        decision["snapshot_id"] = snapshot["snapshot_id"]
        decision["rollback"]["snapshot_id"] = snapshot["snapshot_id"]
        decision["proposal_score"] = proposal["proposal_score"]
        task_hub.setdefault("tool_safety_policy_lifecycle_decisions", []).append(
            decision
        )
        proposal.setdefault("lifecycle_history", []).append(decision)
        proposal.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_tool_safety_policy_proposal",
                "evidence": [proposal_id],
                "tool_safety_policy_lifecycle_decision_id": decision["decision_id"],
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.tool_safety_policy_proposals",
                "operation": f"{normalized_action}_tool_safety_policy_proposal",
                "before": before_status,
                "after": target_status,
                "evidence": [proposal_id] + list(proposal.get("evidence", [])),
                "gate": "medium",
                "confidence": proposal.get("confidence", 0.5),
                "tool_safety_policy_lifecycle_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_tool_safety_policy_proposal_lifecycle",
            target="task_hub.tool_safety_policy_proposals",
            outcome=target_status,
            evidence=[proposal_id] + list(proposal.get("evidence", [])),
            metadata={
                "tool_safety_policy_lifecycle_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "proposal_id": proposal_id,
                "policy_scope": proposal.get("policy_scope"),
                "decision_note": decision_note,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="tool_safety_policy_lifecycle",
            nodes=[
                {
                    "id": "policy_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": proposal_id,
                    "policy_scope": proposal.get("policy_scope"),
                    "executable_policy": False,
                },
                {
                    "id": "lifecycle_review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[
                {
                    "from": "policy_proposal",
                    "to": "lifecycle_review",
                    "type": "feedback",
                }
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.tool_safety_policy_proposals",
                    "tool_safety_policy_proposal_id": proposal_id,
                    "tool_safety_policy_lifecycle_decision_id": decision[
                        "decision_id"
                    ],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_tool_safety_policy_proposal",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "tool_safety_policy_lifecycle_decision": decision,
                }
            ],
            summary=(
                f"Applied lifecycle action {normalized_action} to tool/safety "
                f"policy proposal {proposal_id}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "proposal_id": proposal_id,
            "snapshot_id": snapshot["snapshot_id"],
            "tool_safety_policy_lifecycle_decision_id": decision["decision_id"],
        }

    def apply_memory_lifecycle_action(
        self,
        store_name: str,
        memory_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = normalize_memory_lifecycle_action(action)
        if normalized_action is None:
            return {
                "status": "rejected",
                "error": "unsupported_lifecycle_action",
                "action": action,
            }

        normalized_store = str(store_name or "").strip()
        if normalized_store == "identity_memory":
            return {
                "status": "rejected",
                "error": "identity_memory_requires_high_gate",
                "store_name": normalized_store,
                "memory_id": memory_id,
            }
        if normalized_store not in LIFECYCLE_ACTION_STORES:
            return {
                "status": "rejected",
                "error": "unsupported_memory_store",
                "store_name": normalized_store,
                "memory_id": memory_id,
            }

        state = self.load()
        memories = state.get("memory_stores", {}).get(normalized_store)
        if not isinstance(memories, list):
            return {
                "status": "not_found",
                "error": "memory_store_not_found",
                "store_name": normalized_store,
                "memory_id": memory_id,
            }
        memory = next((item for item in memories if item.get("id") == memory_id), None)
        if memory is None:
            return {
                "status": "not_found",
                "error": "memory_not_found",
                "store_name": normalized_store,
                "memory_id": memory_id,
            }

        before_status = memory.get("lifecycle", {}).get("status") or memory.get("status")
        if before_status in {"archived", "discarded", "quarantined"}:
            return {
                "status": "already_reviewed",
                "store_name": normalized_store,
                "memory_id": memory_id,
                "lifecycle_status": before_status,
            }

        now = utc_now()
        decision = build_memory_lifecycle_decision(
            store_name=normalized_store,
            memory=memory,
            action=normalized_action,
            reviewer=reviewer,
            decision_note=decision_note,
            timestamp=now,
        )
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_memory",
            target_path=f"memory_stores.{normalized_store}",
            evidence=[memory_id],
            metadata={
                "lifecycle_decision_id": decision["decision_id"],
                "store_name": normalized_store,
                "memory_id": memory_id,
                "memory_status": before_status,
            },
        )
        target_status = {
            "archive": "archived",
            "discard": "discarded",
            "quarantine": "quarantined",
        }[normalized_action]

        memory["status"] = target_status
        memory["review_status"] = target_status
        memory["reviewed_at"] = now
        memory["reviewer"] = reviewer
        memory["decision_note"] = decision_note
        memory["last_lifecycle_decision_id"] = decision["decision_id"]
        memory["lifecycle"] = {
            **memory.get("lifecycle", {}),
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        if normalized_action == "quarantine":
            memory["quarantine_reason"] = decision_note or "lifecycle_quarantine"
        if normalized_action == "discard":
            memory["discard_reason"] = decision_note or "lifecycle_discard"

        decision["result"] = target_status
        decision["snapshot_id"] = snapshot["snapshot_id"]
        decision["target_path"] = f"memory_stores.{normalized_store}"
        decision["after"] = memory_id
        memory.setdefault("lifecycle_history", []).append(decision)
        memory.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_memory",
                "evidence": [memory_id],
                "lifecycle_decision_id": decision["decision_id"],
            }
        )

        archived_id = None
        if normalized_action == "archive":
            archived = build_archived_memory_from_lifecycle_action(
                memory=memory,
                store_name=normalized_store,
                reviewer=reviewer,
                decision_note=decision_note,
                timestamp=now,
                decision=decision,
            )
            state["memory_stores"].setdefault("archived_memory", []).append(archived)
            archived_id = archived["id"]
            memory["archived_to"] = archived_id
            decision["after"] = archived_id

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": f"memory_stores.{normalized_store}",
                "operation": f"{normalized_action}_memory",
                "before": before_status,
                "after": target_status,
                "evidence": [memory_id],
                "gate": "medium",
                "confidence": memory.get("confidence", 0.6),
                "lifecycle_decision_id": decision["decision_id"],
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_memory_lifecycle",
            target=f"memory_stores.{normalized_store}",
            outcome=target_status,
            evidence=[memory_id],
            metadata={
                "lifecycle_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "decision_note": decision_note,
                "archived_id": archived_id,
            },
            state=state,
        )
        self.record_trace(
            workflow="memory_lifecycle_action",
            nodes=[
                {
                    "id": "memory",
                    "type": "Memory",
                    "store_name": normalized_store,
                    "memory_id": memory_id,
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[{"from": "memory", "to": "review", "type": "feedback"}],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": f"memory_stores.{normalized_store}",
                    "memory_id": memory_id,
                    "lifecycle_decision_id": decision["decision_id"],
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_memory",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "snapshot_id": snapshot["snapshot_id"],
                    "lifecycle_decision": decision,
                }
            ],
            summary=f"Applied lifecycle action {normalized_action} to {normalized_store}:{memory_id}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "store_name": normalized_store,
            "memory_id": memory_id,
            "snapshot_id": snapshot["snapshot_id"],
            "lifecycle_decision_id": decision["decision_id"],
            "archived_id": archived_id,
        }

    def record_snapshot(
        self,
        state: dict,
        actor: str,
        operation: str,
        target_path: str,
        evidence: Optional[List[str]] = None,
        metadata: Optional[dict] = None,
    ) -> dict:
        memory_stores = state.get("memory_stores", {})
        now = utc_now()
        snapshot = {
            "snapshot_id": new_id("snapshot"),
            "timestamp": now,
            "actor": actor,
            "operation": operation,
            "target_path": target_path,
            "evidence": evidence or [],
            "metadata": metadata or {},
            "state_version": state.get("state_version"),
            "memory_counts": {
                name: len(values)
                for name, values in memory_stores.items()
                if isinstance(values, list)
            },
            "rollback": {
                "reversible": True,
                "mode": "metadata_only",
                "note": "Snapshot records audit metadata only; automatic rollback is not implemented yet.",
            },
        }
        state.setdefault("snapshots", []).append(snapshot)
        state["snapshots"] = state["snapshots"][-50:]
        return snapshot

    def record_audit_event(
        self,
        actor: str,
        action: str,
        target: str,
        outcome: str,
        evidence: Optional[List[str]] = None,
        metadata: Optional[dict] = None,
        state: Optional[dict] = None,
    ) -> dict:
        event = {
            "id": new_id("audit"),
            "timestamp": utc_now(),
            "actor": actor,
            "action": action,
            "target": target,
            "outcome": outcome,
            "evidence": evidence or [],
            "metadata": metadata or {},
        }
        self.append_jsonl(self.audit_path, event)

        current_state = state or self.load()
        current_state.setdefault("audit_log", []).append(
            {
                "id": event["id"],
                "timestamp": event["timestamp"],
                "actor": actor,
                "action": action,
                "target": target,
                "outcome": outcome,
                "evidence": event["evidence"],
            }
        )
        current_state["audit_log"] = current_state["audit_log"][-50:]
        if state is None:
            self.save(current_state)
        return event

    def record_trace(
        self,
        workflow: str,
        nodes: List[dict],
        edges: Optional[List[dict]] = None,
        memory_events: Optional[List[dict]] = None,
        review_events: Optional[List[dict]] = None,
        errors: Optional[List[dict]] = None,
        summary: str = "",
        audit_event_ids: Optional[List[str]] = None,
        state: Optional[dict] = None,
        status: str = "completed",
    ) -> dict:
        now = utc_now()
        trace = {
            "trace_id": new_id("trace"),
            "started_at": now,
            "ended_at": now,
            "workflow": workflow,
            "nodes": nodes,
            "edges": edges or [],
            "memory_events": memory_events or [],
            "review_events": review_events or [],
            "errors": errors or [],
            "summary": summary,
            "audit_event_ids": audit_event_ids or [],
        }
        self.append_jsonl(self.traces_path, trace)
        if state is not None:
            append_task_action_trace(
                state=state,
                trace=trace,
                status=status,
            )
            self.record_state_event(
                state=state,
                trace=trace,
                status=status,
            )
        return trace

    def record_state_event(
        self,
        state: dict,
        trace: dict,
        status: str = "completed",
    ) -> Optional[dict]:
        if status != "completed":
            return None
        update = last_update_for_trace(state=state, trace=trace)
        if not update:
            return None
        event = build_state_event(
            state=state,
            trace=trace,
            update=update,
            sequence=len(self.list_events()) + 1,
        )
        self.append_jsonl(self.events_path, event)
        return event

    def replay_events(self) -> dict:
        events = self.list_events()
        state = self.load()
        updates = state_updates_with_ids(state)
        update_ids = {update["id"] for update in updates}
        event_update_ids = {
            event.get("update_id")
            for event in events
            if event.get("update_id")
        }
        missing_event_update_ids = sorted(event_update_ids - update_ids)
        projection = build_event_replay_projection(events)
        projection_validation = validate_event_replay_projection(state, projection)
        return {
            "status": "passed"
            if not missing_event_update_ids
            and not projection["unrebuildable_event_ids"]
            and projection["sequence_gap_count"] == 0
            else "failed",
            "mode": "audit_replay_with_projection",
            "event_count": len(events),
            "state_update_count": len(updates),
            "event_coverage_count": len(event_update_ids & update_ids),
            "workflows": workflow_counts(events),
            "target_paths": target_path_counts(events),
            "operations": event_operation_counts(events),
            "projection": projection,
            "projection_validation": projection_validation,
            "missing_event_update_ids": missing_event_update_ids,
            "uncovered_state_update_ids": sorted(
                update["id"]
                for update in updates
                if update["id"] not in event_update_ids
                and should_update_have_event(update)
            ),
            "coverage_note": "P35 replay validates event references and rebuilds a target-path transition projection; pre-P12 state updates may be uncovered.",
            "last_event_id": events[-1]["event_id"] if events else None,
        }

    def event_projection_report(self, retention_limit: int = 200) -> dict:
        events = self.list_events()
        before_state = self.load()
        replay = self.replay_events()
        validation = replay.get("projection_validation", {})
        checked = validation.get("checked", {})
        coverage_gaps = {
            path: record
            for path, record in checked.items()
            if int(record.get("coverage_gap_count", 0)) > 0
        }
        report = {
            "status": "passed"
            if replay.get("status") == "passed"
            and not validation.get("count_mismatches")
            else "failed",
            "mode": "event_projection_report_v0.1",
            "event_count": len(events),
            "replay_status": replay.get("status"),
            "projection_mode": replay.get("projection", {}).get("projection_mode"),
            "projection_validation": validation,
            "coverage_gap_paths": sorted(coverage_gaps),
            "coverage_gap_count": len(coverage_gaps),
            "retention": event_retention_suggestion(events, retention_limit),
            "would_modify_state": False,
            "report_only": True,
        }
        report["state_unchanged"] = before_state == self.load()
        return report

    def event_payload_diff_coverage_preview(self) -> dict:
        events = self.list_events()
        before_state = self.load()
        replay = self.replay_events()
        coverage = build_event_payload_diff_coverage(events)
        coverage.update(
            {
                "status": "passed" if replay.get("status") == "passed" else "failed",
                "replay_status": replay.get("status"),
                "projection_mode": replay.get("projection", {}).get("projection_mode"),
                "projection_validation_mode": replay.get(
                    "projection_validation",
                    {},
                ).get("mode"),
                "state_unchanged": before_state == self.load(),
                "note": "P39 previews event payload and object-diff coverage only; it does not compact, delete, summarize, rewrite, or roll back events.",
            }
        )
        return coverage

    def propose_event_payload_capture_policy(
        self,
        proposer: str = "manual_review",
        rationale: str = "",
    ) -> dict:
        state = self.load()
        now = utc_now()
        before_event_ids = [event.get("event_id") for event in self.list_events()]
        coverage = self.event_payload_diff_coverage_preview()
        after_coverage_event_ids = [event.get("event_id") for event in self.list_events()]
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(now, state.get("working_state", {})),
        )
        proposal = build_event_payload_capture_policy_proposal(
            coverage=coverage,
            proposer=proposer,
            timestamp=now,
            rationale=rationale,
        )
        proposal["events_unchanged_by_report"] = (
            before_event_ids == after_coverage_event_ids
        )
        task_hub.setdefault("event_payload_capture_policy_proposals", []).append(
            proposal
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": proposer,
                "target_path": "task_hub.event_payload_capture_policy_proposals",
                "operation": "propose_event_payload_capture_policy",
                "before": None,
                "after": proposal["proposal_id"],
                "evidence": proposal["evidence"],
                "gate": "medium",
                "confidence": proposal["confidence"],
                "event_payload_capture_policy_proposal_id": proposal[
                    "proposal_id"
                ],
                "proposal_mode": "proposal_only",
                "requires_review": True,
                "execution_prohibited": True,
                "executable_policy": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
                "event_schema_mutation_allowed": False,
                "event_payload_capture_executed": False,
                "event_compaction_executed": False,
                "events_modified": False,
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=proposer,
            action="propose_event_payload_capture_policy",
            target="task_hub.event_payload_capture_policy_proposals",
            outcome=proposal["review_status"],
            evidence=proposal["evidence"],
            metadata={
                "proposal_id": proposal["proposal_id"],
                "target_path_requirement_count": len(
                    proposal["target_path_requirements"]
                ),
                "diff_gap_count": proposal["coverage_summary"].get("diff_gap_count"),
                "payload_gap_count": proposal["coverage_summary"].get(
                    "payload_gap_count"
                ),
                "proposal_mode": "proposal_only",
                "execution_prohibited": True,
                "event_schema_mutation_allowed": False,
                "event_payload_capture_executed": False,
                "event_compaction_executed": False,
                "events_modified": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="event_payload_capture_policy_proposal",
            nodes=[
                {
                    "id": "payload_diff_coverage",
                    "type": "EventPayloadDiffCoverage",
                    "event_count": coverage.get("event_count", 0),
                    "diff_gap_count": coverage.get("diff_gap_count", 0),
                },
                {
                    "id": "capture_policy_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": proposal["proposal_id"],
                    "proposal_mode": "proposal_only",
                    "executable_policy": False,
                },
            ],
            edges=[
                {
                    "from": "payload_diff_coverage",
                    "to": "capture_policy_proposal",
                    "type": "proposal",
                }
            ],
            memory_events=[
                {
                    "operation": "propose",
                    "target": "task_hub.event_payload_capture_policy_proposals",
                    "event_payload_capture_policy_proposal_id": proposal[
                        "proposal_id"
                    ],
                    "event_payload_capture_executed": False,
                    "event_compaction_executed": False,
                    "events_modified": False,
                }
            ],
            review_events=[
                {
                    "operation": "propose_event_payload_capture_policy",
                    "proposer": proposer,
                    "proposal": proposal,
                }
            ],
            summary="Proposed review-only event payload capture policy from payload/diff coverage.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        after_save_event_ids = [event.get("event_id") for event in self.list_events()]
        return {
            "status": proposal["review_status"],
            "proposal_id": proposal["proposal_id"],
            "target_path_requirement_count": len(proposal["target_path_requirements"]),
            "coverage_summary": proposal["coverage_summary"],
            "event_schema_mutation_allowed": False,
            "event_payload_capture_executed": False,
            "event_compaction_executed": False,
            "events_modified": before_event_ids
            != after_save_event_ids[: len(before_event_ids)],
        }

    def review_event_payload_capture_policy(
        self,
        proposal_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in EVENT_PAYLOAD_CAPTURE_POLICY_REVIEW_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_event_payload_capture_policy_review_action",
                "action": action,
            }

        before_event_ids = [event.get("event_id") for event in self.list_events()]
        state = self.load()
        now = utc_now()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(now, state.get("working_state", {})),
        )
        proposal = next(
            (
                item
                for item in task_hub.setdefault(
                    "event_payload_capture_policy_proposals",
                    [],
                )
                if isinstance(item, dict) and item.get("proposal_id") == proposal_id
            ),
            None,
        )
        if proposal is None:
            return {
                "status": "not_found",
                "error": "event_payload_capture_policy_proposal_not_found",
                "proposal_id": proposal_id,
            }

        before_status = proposal.get("review_status", "pending")
        if before_status in {"approved", "rejected", "archived", "quarantined"}:
            return {
                "status": "already_reviewed",
                "proposal_id": proposal_id,
                "review_status": before_status,
            }

        target_status = {
            "approve": "approved",
            "reject": "rejected",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        evidence = [proposal_id] + [
            item
            for item in proposal.get("evidence", [])
            if isinstance(item, str) and item
        ]
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_event_payload_capture_policy",
            target_path="task_hub.event_payload_capture_policy_proposals",
            evidence=evidence,
            metadata={
                "proposal_id": proposal_id,
                "review_action": normalized_action,
                "event_schema_mutation_allowed": False,
                "event_payload_capture_executed": False,
                "event_compaction_executed": False,
                "events_modified": False,
            },
        )
        decision = build_event_payload_capture_policy_decision(
            proposal=proposal,
            action=normalized_action,
            result=target_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
            before_status=before_status,
        )
        proposal["review_status"] = target_status
        proposal["reviewed_at"] = now
        proposal["reviewer"] = reviewer
        proposal["decision_note"] = decision_note
        proposal["last_review_decision_id"] = decision["decision_id"]
        proposal["proposal_mode"] = "proposal_only"
        proposal["requires_review"] = True
        proposal["execution_prohibited"] = True
        proposal["executable_policy"] = False
        proposal["executable_policy_created"] = False
        proposal["identity_mutation_allowed"] = False
        proposal["event_schema_mutation_allowed"] = False
        proposal["event_payload_capture_executed"] = False
        proposal["event_compaction_executed"] = False
        proposal["events_modified"] = False
        proposal["lifecycle"] = {
            **(
                proposal.get("lifecycle", {})
                if isinstance(proposal.get("lifecycle"), dict)
                else {}
            ),
            "status": "active",
            "last_reviewed_at": now,
            "review_status": target_status,
            "review_decision_id": decision["decision_id"],
        }
        if target_status in {"archived", "quarantined"}:
            proposal["lifecycle"]["status"] = target_status
            proposal["status"] = target_status
        proposal.setdefault("review_history", []).append(decision)
        proposal.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_event_payload_capture_policy",
                "event_payload_capture_policy_decision_id": decision[
                    "decision_id"
                ],
                "evidence": evidence,
            }
        )
        task_hub.setdefault("event_payload_capture_policy_decisions", []).append(
            decision
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.event_payload_capture_policy_proposals",
                "operation": f"{normalized_action}_event_payload_capture_policy",
                "before": before_status,
                "after": target_status,
                "evidence": evidence,
                "gate": "medium",
                "confidence": proposal.get("confidence", 0.5),
                "event_payload_capture_policy_decision_id": decision["decision_id"],
                "proposal_mode": "proposal_only",
                "requires_review": True,
                "execution_prohibited": True,
                "executable_policy": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
                "event_schema_mutation_allowed": False,
                "event_payload_capture_executed": False,
                "event_compaction_executed": False,
                "events_modified": False,
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_event_payload_capture_policy",
            target="task_hub.event_payload_capture_policy_proposals",
            outcome=target_status,
            evidence=evidence,
            metadata={
                "event_payload_capture_policy_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "proposal_id": proposal_id,
                "decision_note": decision_note,
                "proposal_mode": "proposal_only",
                "execution_prohibited": True,
                "event_schema_mutation_allowed": False,
                "event_payload_capture_executed": False,
                "event_compaction_executed": False,
                "events_modified": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="event_payload_capture_policy_review",
            nodes=[
                {
                    "id": "capture_policy_proposal",
                    "type": "PolicyProposal",
                    "proposal_id": proposal_id,
                    "proposal_mode": "proposal_only",
                },
                {
                    "id": "review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[
                {
                    "from": "capture_policy_proposal",
                    "to": "review",
                    "type": "feedback",
                }
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.event_payload_capture_policy_proposals",
                    "event_payload_capture_policy_proposal_id": proposal_id,
                    "event_payload_capture_policy_decision_id": decision[
                        "decision_id"
                    ],
                    "event_payload_capture_executed": False,
                    "event_compaction_executed": False,
                    "events_modified": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_event_payload_capture_policy",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "event_payload_capture_policy_decision": decision,
                }
            ],
            summary=(
                f"Reviewed event payload capture policy proposal {proposal_id} "
                f"with action {normalized_action}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        after_event_ids = [event.get("event_id") for event in self.list_events()]
        return {
            "status": target_status,
            "proposal_id": proposal_id,
            "snapshot_id": snapshot["snapshot_id"],
            "event_payload_capture_policy_decision_id": decision["decision_id"],
            "event_schema_mutation_allowed": False,
            "event_payload_capture_executed": False,
            "event_compaction_executed": False,
            "events_modified": before_event_ids != after_event_ids[: len(before_event_ids)],
        }

    def review_event_retention(
        self,
        reviewer: str = "manual_review",
        retention_limit: int = 200,
        note: str = "",
    ) -> dict:
        state = self.load()
        now = utc_now()
        before_event_ids = [event.get("event_id") for event in self.list_events()]
        report = self.event_projection_report(retention_limit=retention_limit)
        after_report_event_ids = [event.get("event_id") for event in self.list_events()]
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(now, state.get("working_state", {})),
        )
        review = build_event_retention_review(
            report=report,
            reviewer=reviewer,
            timestamp=now,
            note=note,
        )
        review["events_unchanged_by_report"] = before_event_ids == after_report_event_ids
        task_hub.setdefault("event_retention_reviews", []).append(review)
        task_hub["event_retention_reviews"] = task_hub["event_retention_reviews"][-20:]
        state.setdefault("update_log", []).append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.event_retention_reviews",
                "operation": "review_event_retention",
                "before": None,
                "after": review["review_id"],
                "evidence": review["evidence"],
                "gate": "low",
                "confidence": review["confidence"],
                "review_only": True,
                "execution_prohibited": True,
                "executable_policy": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
                "event_compaction_executed": False,
                "events_modified": False,
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action="review_event_retention",
            target="task_hub.event_retention_reviews",
            outcome=review["status"],
            evidence=review["evidence"],
            metadata={
                "review_id": review["review_id"],
                "event_count": review["event_count"],
                "retention_limit": review["retention"].get("retention_limit"),
                "excess_event_count": review["retention"].get("excess_event_count"),
                "review_only": True,
                "event_compaction_executed": False,
                "events_modified": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="event_retention_review",
            nodes=[
                {
                    "id": "event_report",
                    "type": "EventProjectionReport",
                    "event_count": review["event_count"],
                    "coverage_gap_count": review["coverage_gap_count"],
                },
                {
                    "id": "retention_review",
                    "type": "ReviewSignal",
                    "review_id": review["review_id"],
                    "status": review["status"],
                    "review_only": True,
                },
            ],
            edges=[
                {
                    "from": "event_report",
                    "to": "retention_review",
                    "type": "retention_review",
                }
            ],
            memory_events=[
                {
                    "operation": "review",
                    "target": "task_hub.event_retention_reviews",
                    "event_retention_review_id": review["review_id"],
                    "event_compaction_executed": False,
                    "events_modified": False,
                }
            ],
            review_events=[
                {
                    "operation": "review_event_retention",
                    "reviewer": reviewer,
                    "review": review,
                }
            ],
            summary="Reviewed event projection coverage and retention pressure.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        after_save_event_ids = [event.get("event_id") for event in self.list_events()]
        return {
            "status": review["status"],
            "review_id": review["review_id"],
            "event_count": review["event_count"],
            "retention": review["retention"],
            "review_signals": review["review_signals"],
            "event_compaction_executed": False,
            "events_modified": before_event_ids != after_save_event_ids[: len(before_event_ids)],
        }

    def apply_event_retention_lifecycle_action(
        self,
        review_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in EVENT_RETENTION_LIFECYCLE_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_event_retention_lifecycle_action",
                "action": action,
            }

        before_event_ids = [event.get("event_id") for event in self.list_events()]
        state = self.load()
        now = utc_now()
        task_hub = state.setdefault(
            "task_hub",
            default_task_hub(now, state.get("working_state", {})),
        )
        review = next(
            (
                item
                for item in task_hub.setdefault("event_retention_reviews", [])
                if isinstance(item, dict) and item.get("review_id") == review_id
            ),
            None,
        )
        if review is None:
            return {
                "status": "not_found",
                "error": "event_retention_review_not_found",
                "review_id": review_id,
            }

        lifecycle = review.get("lifecycle") if isinstance(review.get("lifecycle"), dict) else {}
        before_status = lifecycle.get("status") or "active"
        if before_status in {"archived", "quarantined"}:
            return {
                "status": "already_reviewed",
                "review_id": review_id,
                "lifecycle_status": before_status,
            }
        if before_status == "acknowledged" and normalized_action == "acknowledge":
            return {
                "status": "already_reviewed",
                "review_id": review_id,
                "lifecycle_status": before_status,
            }

        target_status = {
            "acknowledge": "acknowledged",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        evidence = [review_id] + [
            item
            for item in review.get("evidence", [])
            if isinstance(item, str) and item
        ]
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_event_retention_review",
            target_path="task_hub.event_retention_reviews",
            evidence=evidence,
            metadata={
                "event_retention_lifecycle_decision_id": None,
                "review_id": review_id,
                "review_status": review.get("status"),
                "event_compaction_executed": False,
                "events_modified": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
        )
        decision = build_event_retention_lifecycle_decision(
            review=review,
            action=normalized_action,
            result=target_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
            before_status=before_status,
        )
        snapshot["metadata"]["event_retention_lifecycle_decision_id"] = decision[
            "decision_id"
        ]

        review["lifecycle"] = {
            **lifecycle,
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        review["last_lifecycle_decision_id"] = decision["decision_id"]
        review["reviewed_at"] = now
        review["reviewer"] = reviewer
        review["decision_note"] = decision_note
        review["review_only"] = True
        review["execution_prohibited"] = True
        review["executable_policy"] = False
        review["executable_policy_created"] = False
        review["identity_mutation_allowed"] = False
        review["event_compaction_executed"] = False
        review["events_modified"] = False
        if normalized_action == "quarantine":
            review["quarantine_reason"] = (
                decision_note or "event_retention_lifecycle_quarantine"
            )
        review.setdefault("lifecycle_history", []).append(decision)
        review.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_event_retention_review",
                "evidence": evidence,
                "event_retention_lifecycle_decision_id": decision["decision_id"],
            }
        )
        task_hub.setdefault("event_retention_lifecycle_decisions", []).append(decision)

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "task_hub.event_retention_reviews",
                "operation": f"{normalized_action}_event_retention_review",
                "before": before_status,
                "after": target_status,
                "evidence": evidence,
                "gate": "medium",
                "confidence": review.get("confidence", 0.5),
                "event_retention_lifecycle_decision_id": decision["decision_id"],
                "review_only": True,
                "execution_prohibited": True,
                "executable_policy": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
                "event_compaction_executed": False,
                "events_modified": False,
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_event_retention_review",
            target="task_hub.event_retention_reviews",
            outcome=target_status,
            evidence=evidence,
            metadata={
                "event_retention_lifecycle_decision_id": decision["decision_id"],
                "snapshot_id": snapshot["snapshot_id"],
                "review_id": review_id,
                "decision_note": decision_note,
                "review_only": True,
                "event_compaction_executed": False,
                "events_modified": False,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="event_retention_lifecycle",
            nodes=[
                {
                    "id": "event_retention_review",
                    "type": "ReviewSignal",
                    "review_id": review_id,
                    "review_status": review.get("status"),
                    "review_only": True,
                },
                {
                    "id": "lifecycle_review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[
                {
                    "from": "event_retention_review",
                    "to": "lifecycle_review",
                    "type": "feedback",
                }
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "task_hub.event_retention_reviews",
                    "event_retention_review_id": review_id,
                    "event_retention_lifecycle_decision_id": decision[
                        "decision_id"
                    ],
                    "event_compaction_executed": False,
                    "events_modified": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_event_retention_review",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "event_retention_lifecycle_decision": decision,
                }
            ],
            summary=f"Applied lifecycle action {normalized_action} to event retention review {review_id}.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        after_event_ids = [event.get("event_id") for event in self.list_events()]
        return {
            "status": target_status,
            "review_id": review_id,
            "snapshot_id": snapshot["snapshot_id"],
            "event_retention_lifecycle_decision_id": decision["decision_id"],
            "event_compaction_executed": False,
            "events_modified": before_event_ids != after_event_ids[: len(before_event_ids)],
        }

    def rollback_preview(self, snapshot_id: str) -> dict:
        state = self.load()
        snapshot = next(
            (
                item
                for item in state.get("snapshots", [])
                if isinstance(item, dict) and item.get("snapshot_id") == snapshot_id
            ),
            None,
        )
        if snapshot is None:
            return {
                "status": "not_found",
                "snapshot_id": snapshot_id,
                "error": "snapshot_not_found",
            }
        events = self.list_events()
        target_updates = [
            update
            for update in state_updates_with_ids(state)
            if update.get("rollback", {}).get("snapshot_id") == snapshot_id
        ]
        event_update_ids = {
            update["id"]
            for update in target_updates
            if update.get("id")
        }
        affected_events = [
            event
            for event in events
            if event.get("update_id") in event_update_ids
        ]
        affected_state_paths = sorted(
            {
                str(update.get("target_path"))
                for update in target_updates
                if update.get("target_path")
            }
        )
        replay_projection = build_event_replay_projection(events)
        projected_rollback = (
            replay_projection.get("rollback_snapshots", {}).get(snapshot_id, {})
        )
        return {
            "status": "preview",
            "mode": "metadata_only_with_projection",
            "snapshot_id": snapshot_id,
            "operation": snapshot.get("operation"),
            "target_path": snapshot.get("target_path"),
            "rollback": snapshot.get("rollback", {}),
            "memory_counts_at_snapshot": snapshot.get("memory_counts", {}),
            "current_memory_counts": current_memory_counts(state),
            "affected_update_ids": sorted(event_update_ids),
            "affected_event_ids": [event.get("event_id") for event in affected_events],
            "affected_state_paths": affected_state_paths,
            "projected_rollback_impact": {
                "projection_mode": replay_projection["projection_mode"],
                "target_paths": projected_rollback.get(
                    "target_paths",
                    affected_state_paths,
                ),
                "event_ids": projected_rollback.get(
                    "event_ids",
                    [event.get("event_id") for event in affected_events],
                ),
                "update_ids": projected_rollback.get(
                    "update_ids",
                    sorted(event_update_ids),
                ),
                "would_remove_event_count": len(
                    projected_rollback.get("event_ids", affected_events)
                ),
                "full_state_rebuild": False,
            },
            "would_modify_state": False,
            "note": "P35 previews rollback from snapshot metadata, event references, and replay projection only; automatic rollback is not implemented.",
        }

    def apply_context_attribution_coverage_lifecycle_action(
        self,
        review_id: str,
        action: str,
        reviewer: str = "manual_review",
        decision_note: str = "",
    ) -> dict:
        normalized_action = str(action or "").strip().lower()
        if normalized_action not in CONTEXT_ATTRIBUTION_COVERAGE_LIFECYCLE_ACTIONS:
            return {
                "status": "rejected",
                "error": "unsupported_context_attribution_coverage_lifecycle_action",
                "action": action,
            }

        state = self.load()
        now = utc_now()
        context_builder = state.setdefault("context_builder", default_context_builder(now))
        review = next(
            (
                item
                for item in context_builder.setdefault(
                    "attribution_coverage_reviews",
                    [],
                )
                if isinstance(item, dict) and item.get("review_id") == review_id
            ),
            None,
        )
        if review is None:
            return {
                "status": "not_found",
                "error": "context_attribution_coverage_review_not_found",
                "review_id": review_id,
            }

        lifecycle = review.get("lifecycle") if isinstance(review.get("lifecycle"), dict) else {}
        before_status = lifecycle.get("status") or "active"
        if before_status in {"archived", "quarantined"}:
            return {
                "status": "already_reviewed",
                "review_id": review_id,
                "lifecycle_status": before_status,
            }
        if before_status == "acknowledged" and normalized_action == "acknowledge":
            return {
                "status": "already_reviewed",
                "review_id": review_id,
                "lifecycle_status": before_status,
            }

        target_status = {
            "acknowledge": "acknowledged",
            "archive": "archived",
            "quarantine": "quarantined",
        }[normalized_action]
        evidence = [review_id] + [
            item
            for item in review.get("evidence", [])
            if isinstance(item, str) and item
        ]
        snapshot = self.record_snapshot(
            state=state,
            actor=reviewer,
            operation=f"{normalized_action}_context_attribution_coverage_review",
            target_path="context_builder.attribution_coverage_reviews",
            evidence=evidence,
            metadata={
                "context_attribution_coverage_lifecycle_decision_id": None,
                "review_id": review_id,
                "review_status": review.get("status"),
                "source_record_ratio": review.get("metrics", {}).get(
                    "source_record_ratio"
                )
                if isinstance(review.get("metrics"), dict)
                else None,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
        )
        decision = build_context_attribution_coverage_lifecycle_decision(
            review=review,
            action=normalized_action,
            result=target_status,
            reviewer=reviewer,
            decision_note=decision_note,
            snapshot_id=snapshot["snapshot_id"],
            timestamp=now,
            before_status=before_status,
        )
        snapshot["metadata"][
            "context_attribution_coverage_lifecycle_decision_id"
        ] = decision["decision_id"]

        review["lifecycle"] = {
            **lifecycle,
            "status": target_status,
            "last_reviewed_at": now,
            "review_status": target_status,
            "lifecycle_decision_id": decision["decision_id"],
        }
        review["last_lifecycle_decision_id"] = decision["decision_id"]
        review["reviewed_at"] = now
        review["reviewer"] = reviewer
        review["decision_note"] = decision_note
        review["review_only"] = True
        review["execution_prohibited"] = True
        review["executable_policy"] = False
        review["executable_policy_created"] = False
        review["identity_mutation_allowed"] = False
        if normalized_action == "quarantine":
            review["quarantine_reason"] = (
                decision_note or "context_attribution_coverage_lifecycle_quarantine"
            )
        review.setdefault("lifecycle_history", []).append(decision)
        review.setdefault("update_history", []).append(
            {
                "timestamp": now,
                "actor": reviewer,
                "operation": f"{normalized_action}_context_attribution_coverage_review",
                "evidence": evidence,
                "context_attribution_coverage_lifecycle_decision_id": decision[
                    "decision_id"
                ],
            }
        )
        context_builder.setdefault(
            "attribution_coverage_lifecycle_decisions",
            [],
        ).append(decision)
        context_builder["updated_at"] = now

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "context_builder.attribution_coverage_reviews",
                "operation": f"{normalized_action}_context_attribution_coverage_review",
                "before": before_status,
                "after": target_status,
                "evidence": evidence,
                "gate": "medium",
                "confidence": review.get("confidence", 0.5),
                "context_attribution_coverage_lifecycle_decision_id": decision[
                    "decision_id"
                ],
                "review_only": True,
                "execution_prohibited": True,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
                "rollback": {
                    "snapshot_id": snapshot["snapshot_id"],
                    "reversible": True,
                },
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action=f"{normalized_action}_context_attribution_coverage_review",
            target="context_builder.attribution_coverage_reviews",
            outcome=target_status,
            evidence=evidence,
            metadata={
                "context_attribution_coverage_lifecycle_decision_id": decision[
                    "decision_id"
                ],
                "snapshot_id": snapshot["snapshot_id"],
                "review_id": review_id,
                "decision_note": decision_note,
                "review_only": True,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="context_attribution_coverage_lifecycle",
            nodes=[
                {
                    "id": "coverage_review",
                    "type": "ReviewSignal",
                    "review_id": review_id,
                    "coverage_status": review.get("status"),
                    "review_only": True,
                },
                {
                    "id": "lifecycle_review",
                    "type": "Review",
                    "reviewer": reviewer,
                    "decision": normalized_action,
                },
            ],
            edges=[
                {
                    "from": "coverage_review",
                    "to": "lifecycle_review",
                    "type": "feedback",
                }
            ],
            memory_events=[
                {
                    "operation": normalized_action,
                    "target": "context_builder.attribution_coverage_reviews",
                    "context_attribution_coverage_review_id": review_id,
                    "context_attribution_coverage_lifecycle_decision_id": decision[
                        "decision_id"
                    ],
                    "executable_policy_created": False,
                }
            ],
            review_events=[
                {
                    "operation": f"{normalized_action}_context_attribution_coverage_review",
                    "reviewer": reviewer,
                    "decision_note": decision_note,
                    "context_attribution_coverage_lifecycle_decision": decision,
                }
            ],
            summary=(
                f"Applied lifecycle action {normalized_action} to Context "
                f"Builder attribution coverage review {review_id}."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": target_status,
            "review_id": review_id,
            "snapshot_id": snapshot["snapshot_id"],
            "context_attribution_coverage_lifecycle_decision_id": decision[
                "decision_id"
            ],
        }

    def record_episode(
        self,
        message: str,
        user_id: str = "local_user",
        channel: str = "cli",
        session_id: Optional[str] = None,
        event_id: Optional[str] = None,
        event_type: str = "message",
        adapter_id: Optional[str] = None,
        metadata: Optional[dict] = None,
        salience_hint: Optional[float] = None,
    ) -> dict:
        state = self.load()
        now = utc_now()
        session_id = session_id or state["working_state"]["current_context"]["session_id"]
        episode = build_episode_preview(
            message=message,
            user_id=user_id,
            channel=channel,
            session_id=session_id,
            event_id=event_id,
            event_type=event_type,
            adapter_id=adapter_id,
            metadata=metadata,
            salience_hint=salience_hint,
            timestamp=now,
        )
        tags = episode["tags"]
        salience = episode["salience"]
        confidence = episode["confidence"]
        episode_id = episode["id"]
        summary = episode["summary"]
        sensitivity = episode["sensitivity"]
        source = episode["source"]
        adapter_metadata = episode["metadata"]

        self.append_jsonl(self.episodes_path, episode)
        state["memory_stores"]["episodic_memory"].append(
            {
                "id": episode_id,
                "timestamp": now,
                "summary": summary,
                "salience": salience,
                "tags": tags,
                "confidence": confidence,
                "participants": episode["participants"],
                "channel": channel,
                "source": source,
                "sensitivity": sensitivity,
                "lifecycle": {
                    "status": "active",
                    "created_at": now,
                    "last_reviewed_at": None,
                    "review_status": "unreviewed",
                },
                "provenance": [
                    {
                        "type": "episode_recorded",
                        "source": source,
                    }
                ],
                "update_history": [
                    {
                        "timestamp": now,
                        "actor": adapter_id or "interaction_loop",
                        "operation": "record_episode",
                        "evidence": [episode_id],
                    }
                ],
            }
        )
        self.index_adapter_event(state.setdefault("adapter_event_index", {}), episode)
        update_working_state_from_message(state, message, user_id, now)
        state["dream_queue"].append(
            {
                "id": new_id("dream_job"),
                "trigger": "episode_recorded",
                "input_episodes": [episode_id],
                "requested_operations": [
                    "summarize",
                    "abstract",
                    "detect_conflicts",
                    "propose_updates",
                ],
                "status": "pending",
            }
        )
        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": adapter_id or "interaction_loop",
                "target_path": "memory_stores.episodic_memory",
                "operation": "append",
                "before": None,
                "after": episode_id,
                "evidence": [episode_id],
                "gate": "low",
                "confidence": 0.85,
                "metadata": adapter_metadata,
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=adapter_id or "interaction_loop",
            action="record_episode",
            target="memory_stores.episodic_memory",
            outcome="recorded",
            evidence=[episode_id],
            metadata={
                "channel": channel,
                "session_id": session_id,
                "event_id": event_id,
                "event_type": event_type,
                "adapter_id": adapter_id,
                "dream_job_count": 1,
            },
            state=state,
        )
        self.record_trace(
            workflow="record_episode",
            nodes=[
                {"id": "input", "type": "Input", "summary": summary},
                {
                    "id": "episode",
                    "type": "Memory",
                    "operation": "append_episode",
                    "episode_id": episode_id,
                },
                {
                    "id": "dream_queue",
                    "type": "Decision",
                    "operation": "queue_dream_job",
                },
            ],
            edges=[
                {"from": "input", "to": "episode", "type": "memory_write"},
                {"from": "episode", "to": "dream_queue", "type": "dream_transform"},
            ],
            memory_events=[
                {
                    "operation": "append",
                    "target": "episodic_memory",
                    "memory_id": episode_id,
                }
            ],
            summary=f"Recorded episode {episode_id} and queued dream consolidation.",
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return episode

    def preview_episode(
        self,
        message: str,
        user_id: str = "local_user",
        channel: str = "cli",
        session_id: Optional[str] = None,
        event_id: Optional[str] = None,
        event_type: str = "message",
        adapter_id: Optional[str] = None,
        metadata: Optional[dict] = None,
        salience_hint: Optional[float] = None,
    ) -> dict:
        state = self.load()
        return build_episode_preview(
            message=message,
            user_id=user_id,
            channel=channel,
            session_id=session_id
            or state["working_state"]["current_context"]["session_id"],
            event_id=event_id,
            event_type=event_type,
            adapter_id=adapter_id,
            metadata=metadata,
            salience_hint=salience_hint,
            timestamp=utc_now(),
        )

    def build_context_package(self, persist_trace: bool = True) -> dict:
        state = self.load()
        now = utc_now()
        working_state = state["working_state"]
        current_plan = working_state.get("current_plan", [])
        task_hub = state.get("task_hub", default_task_hub(utc_now(), working_state))
        identity_gate = state.get(
            "identity_update_gate",
            default_identity_update_gate(utc_now()),
        )
        context_builder = state.setdefault("context_builder", default_context_builder(now))
        policy = context_builder.setdefault("policy", default_context_policy())
        context_signals = build_context_signal_index(
            state=state,
            dream_artifacts=self.list_dream_artifacts(),
        )
        active_tasks = [
            task
            for task in task_hub.get("active_tasks", [])
            if isinstance(task, dict)
        ]
        action_trace = [
            action
            for action in task_hub.get("action_trace", [])
            if isinstance(action, dict)
        ][-10:]
        active_procedural_memory = [
            memory
            for memory in task_hub.get("procedural_memory", [])
            if isinstance(memory, dict)
            and memory.get("status") == "active"
            and memory.get("lifecycle", {}).get("status") == "active"
        ]
        active_cautionary_memory = [
            warning
            for warning in task_hub.get("cautionary_procedural_memory", [])
            if isinstance(warning, dict)
            and warning.get("status") == "active"
            and warning.get("lifecycle", {}).get("status") == "active"
        ]
        active_tool_safety_policy_proposals = sorted(
            [
                proposal
                for proposal in task_hub.get("tool_safety_policy_proposals", [])
                if isinstance(proposal, dict)
                and proposal.get("review_status") in {"pending", "approved"}
                and (
                    proposal.get("lifecycle", {})
                    if isinstance(proposal.get("lifecycle"), dict)
                    else {}
                ).get("status", proposal.get("status", "active"))
                == "active"
            ],
            key=lambda proposal: proposal.get("proposal_score", {}).get(
                "priority_score",
                0.0,
            )
            if isinstance(proposal.get("proposal_score"), dict)
            else 0.0,
            reverse=True,
        )[:8]
        active_tool_safety_policy_links = [
            link
            for link in task_hub.get("tool_safety_policy_links", [])
            if isinstance(link, dict) and link.get("status") == "active"
        ][-12:]
        active_attribution_coverage_reviews = [
            review
            for review in context_builder.get("attribution_coverage_reviews", [])
            if isinstance(review, dict)
            and (
                review.get("lifecycle", {})
                if isinstance(review.get("lifecycle"), dict)
                else {}
            ).get("status", "active")
            in {"active", "acknowledged"}
        ][-8:]
        active_event_retention_reviews = [
            review
            for review in task_hub.get("event_retention_reviews", [])
            if isinstance(review, dict)
            and (
                review.get("lifecycle", {})
                if isinstance(review.get("lifecycle"), dict)
                else {}
            ).get("status", "active")
            in {"active", "acknowledged"}
        ][-8:]
        active_event_payload_capture_policy_proposals = [
            proposal
            for proposal in task_hub.get(
                "event_payload_capture_policy_proposals",
                [],
            )
            if isinstance(proposal, dict)
            and proposal.get("review_status")
            in {"needs_review", "ready_for_review", "approved"}
            and (
                proposal.get("lifecycle", {})
                if isinstance(proposal.get("lifecycle"), dict)
                else {}
            ).get("status", proposal.get("status", "active"))
            == "active"
        ][-8:]
        reflection_log = [
            reflection
            for reflection in task_hub.get("reflection_log", [])
            if isinstance(reflection, dict)
        ]
        active_reflection_log = reflection_log[-8:]
        task_terms = context_task_terms(working_state)
        relationship_context = build_relationship_context(state)
        episodic, episodic_trace = activate_context_memories(
            state=state,
            store_name="episodic_memory",
            items=state["memory_stores"].get("episodic_memory", []),
            policy=policy,
            task_terms=task_terms,
            context_signals=context_signals,
        )
        semantic, semantic_trace = activate_context_memories(
            state=state,
            store_name="semantic_memory",
            items=state["memory_stores"].get("semantic_memory", []),
            policy=policy,
            task_terms=task_terms,
            context_signals=context_signals,
        )
        imported, imported_trace = activate_context_memories(
            state=state,
            store_name="imported_memory",
            items=state["memory_stores"].get("imported_memory", []),
            policy=policy,
            task_terms=task_terms,
            context_signals=context_signals,
        )
        relevant_memories = build_relevant_memory_view(
            [
                ("episodic_memory", episodic),
                ("semantic_memory", semantic),
                ("imported_memory", imported),
            ]
        )
        activation_trace = build_activation_trace(
            traces=[episodic_trace, semantic_trace, imported_trace],
            policy=policy,
            context_signals=context_signals,
            timestamp=now,
        )
        package_id = new_id("context_package")
        activation_trace["trace_id"] = new_id("context_activation")
        activation_trace["context_package_id"] = package_id
        reflection_policy_guidance = build_reflection_policy_guidance(
            active_reflection_log,
            package_id=package_id,
            timestamp=now,
        )
        reflection_guidance_queue = sync_reflection_guidance_queue(
            task_hub=task_hub,
            guidance=reflection_policy_guidance,
            timestamp=now,
        )
        source_attribution = build_source_attribution(
            relevant_memories,
            budget=int(policy.get("budgets", {}).get("source_attribution", 12)),
        )
        package = {
            "context_package_version": "0.3",
            "context_package_id": package_id,
            "identity_summary": state["identity_core"]["self_model"]["summary"],
            "active_intent": working_state["active_intent"],
            "current_plan": current_plan,
            "next_actions": next_actions_from_plan(current_plan),
            "task_hub": {
                "active_tasks": active_tasks,
                "blocked_tasks": task_hub.get("blocked_tasks", []),
                "recent_actions": action_trace,
                "failure_reflections": task_hub.get("failure_reflections", []),
                "procedural_candidates": task_hub.get("procedural_candidates", []),
                "cautionary_procedural_candidates": task_hub.get(
                    "cautionary_procedural_candidates",
                    [],
                ),
                "reflection_log": active_reflection_log,
                "reflection_policy_guidance": reflection_policy_guidance,
                "reflection_guidance_queue": reflection_guidance_queue,
                "tool_safety_policy_proposals": active_tool_safety_policy_proposals,
                "tool_safety_policy_links": active_tool_safety_policy_links,
                "event_retention_reviews": active_event_retention_reviews,
                "event_payload_capture_policy_proposals": active_event_payload_capture_policy_proposals,
                "cautionary_procedural_memory": active_cautionary_memory,
                "procedural_memory": active_procedural_memory,
            },
            "active_tasks": active_tasks,
            "action_trace": action_trace,
            "failure_reflections": task_hub.get("failure_reflections", []),
            "procedural_candidates": task_hub.get("procedural_candidates", []),
            "cautionary_procedural_candidates": task_hub.get(
                "cautionary_procedural_candidates",
                [],
            ),
            "reflection_log": active_reflection_log,
            "reflection_policy_guidance": reflection_policy_guidance,
            "reflection_guidance_queue": reflection_guidance_queue,
            "tool_safety_policy_proposals": active_tool_safety_policy_proposals,
            "tool_safety_policy_links": active_tool_safety_policy_links,
            "event_retention_reviews": active_event_retention_reviews,
            "event_payload_capture_policy_proposals": active_event_payload_capture_policy_proposals,
            "cautionary_procedural_memory": active_cautionary_memory,
            "procedural_memory": active_procedural_memory,
            "identity_update_gate": {
                "required_gate": identity_gate.get("required_gate", "high"),
                "pending_proposals": [
                    proposal
                    for proposal in identity_gate.get("proposals", [])
                    if isinstance(proposal, dict)
                    and proposal.get("review_status") == "pending"
                ],
                "recent_decisions": [
                    decision
                    for decision in identity_gate.get("review_decisions", [])
                    if isinstance(decision, dict)
                ][-5:],
                "recent_drift_events": [
                    event
                    for event in identity_gate.get("drift_events", [])
                    if isinstance(event, dict)
                ][-5:],
            },
            "blockers": working_state.get("blockers", []),
            "assumptions": working_state.get("assumptions", []),
            "continuity_anchors": working_state["context_anchors"],
            "context_policy": policy,
            "relationship_context": relationship_context,
            "context_attribution_coverage_reviews": active_attribution_coverage_reviews,
            "source_attribution": source_attribution,
            "activation_trace": activation_trace,
            "context_signal_summary": summarize_context_signals(context_signals),
            "relevant_memories": relevant_memories,
            "imported_memories": imported,
            "recent_episodes": episodic,
            "relevant_semantic_memories": semantic,
            "open_conflicts": state.get("open_conflicts", []),
            "current_constraints": state["identity_core"].get("identity_constraints", []),
        }
        if persist_trace and policy.get("persistence", {}).get(
            "activation_trace_history",
            True,
        ):
            self.record_context_activation_trace(
                state=state,
                activation_trace=activation_trace,
                policy=policy,
                package_id=package_id,
                timestamp=now,
            )
        return package

    def record_context_activation_trace(
        self,
        state: dict,
        activation_trace: dict,
        policy: dict,
        package_id: str,
        timestamp: str,
    ) -> None:
        context_builder = state.setdefault("context_builder", default_context_builder(timestamp))
        entry = {
            "trace_id": activation_trace.get("trace_id"),
            "context_package_id": package_id,
            "timestamp": timestamp,
            "policy_version": policy.get("policy_version"),
            "metrics": activation_trace.get("metrics", {}),
            "selected": activation_trace.get("selected", []),
            "suppressed": activation_trace.get("suppressed", []),
            "signal_summary": activation_trace.get("signal_summary", {}),
            "signal_attribution_summary": activation_trace.get(
                "signal_attribution_summary",
                {},
            ),
        }
        history = context_builder.setdefault("activation_traces", [])
        history.append(entry)
        budget = int(policy.get("budgets", {}).get("activation_trace_history", 20))
        context_builder["activation_traces"] = history[-budget:]
        context_builder["last_context_package_id"] = package_id
        context_builder["updated_at"] = timestamp
        self.save(state)

    def review_context_attribution_coverage(
        self,
        reviewer: str = "manual_review",
        window: int = 5,
        minimum_source_record_ratio: float = 0.8,
        note: str = "",
    ) -> dict:
        state = self.load()
        now = utc_now()
        context_builder = state.setdefault("context_builder", default_context_builder(now))
        traces = [
            trace
            for trace in context_builder.setdefault("activation_traces", [])
            if isinstance(trace, dict)
        ][-max(1, int(window)) :]
        review = build_context_attribution_coverage_review(
            traces=traces,
            reviewer=reviewer,
            timestamp=now,
            minimum_source_record_ratio=minimum_source_record_ratio,
            note=note,
        )
        context_builder.setdefault("attribution_coverage_reviews", []).append(review)
        context_builder["attribution_coverage_reviews"] = context_builder[
            "attribution_coverage_reviews"
        ][-20:]
        context_builder["updated_at"] = now
        state.setdefault("update_log", []).append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": reviewer,
                "target_path": "context_builder.attribution_coverage_reviews",
                "operation": "review_context_attribution_coverage",
                "before": None,
                "after": review["review_id"],
                "evidence": review["evidence"],
                "gate": "low",
                "confidence": review["confidence"],
                "review_only": True,
                "execution_prohibited": True,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.record_audit_event(
            actor=reviewer,
            action="review_context_attribution_coverage",
            target="context_builder.attribution_coverage_reviews",
            outcome=review["status"],
            evidence=review["evidence"],
            metadata={
                "review_id": review["review_id"],
                "window": review["window"],
                "source_record_ratio": review["metrics"]["source_record_ratio"],
                "review_only": True,
                "executable_policy_created": False,
                "identity_mutation_allowed": False,
            },
            state=state,
        )
        self.record_trace(
            workflow="context_attribution_coverage_review",
            nodes=[
                {
                    "id": "activation_traces",
                    "type": "ContextActivationTraceWindow",
                    "trace_ids": review["trace_ids"],
                },
                {
                    "id": "coverage_review",
                    "type": "ReviewSignal",
                    "review_id": review["review_id"],
                    "status": review["status"],
                    "review_only": True,
                },
            ],
            edges=[
                {
                    "from": "activation_traces",
                    "to": "coverage_review",
                    "type": "coverage_review",
                }
            ],
            review_events=[
                {
                    "operation": "review_context_attribution_coverage",
                    "reviewer": reviewer,
                    "review": review,
                }
            ],
            summary=(
                "Reviewed Context Builder attribution coverage for recent "
                "activation traces."
            ),
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.save(state)
        return {
            "status": review["status"],
            "review_id": review["review_id"],
            "metrics": review["metrics"],
            "review_signals": review["review_signals"],
        }


def context_task_terms(working_state: dict) -> List[str]:
    text_parts = [
        str(working_state.get("active_intent", {}).get("goal", "")),
        " ".join(
            str(item.get("step", ""))
            for item in working_state.get("current_plan", [])
            if isinstance(item, dict)
        ),
        " ".join(
            str(item.get("text", ""))
            for item in working_state.get("blockers", [])
            if isinstance(item, dict)
        ),
    ]
    tags = infer_tags(" ".join(text_parts))
    terms = set(tags)
    for raw in " ".join(text_parts).lower().replace("_", " ").split():
        token = raw.strip(".,;:!?()[]{}<>\"'")
        if len(token) >= 4:
            terms.add(token)
    return sorted(terms)


def build_relationship_context(state: dict) -> dict:
    current_user_id = str(
        state.get("working_state", {})
        .get("current_context", {})
        .get("user_id", "")
    )
    users = state.get("relationship_map", {}).get("users", [])
    current_user = next(
        (
            user
            for user in users
            if isinstance(user, dict) and str(user.get("user_id")) == current_user_id
        ),
        None,
    )
    if not current_user:
        return {
            "current_user_id": current_user_id,
            "known_user": False,
            "privacy_boundaries": {"share_across_users": False},
        }
    return {
        "current_user_id": current_user_id,
        "known_user": True,
        "display_name": current_user.get("display_name", ""),
        "relationship_summary": current_user.get("relationship_summary", ""),
        "communication_preferences": current_user.get(
            "communication_preferences", {}
        ),
        "privacy_boundaries": current_user.get(
            "privacy_boundaries", {"share_across_users": False}
        ),
        "unresolved_tensions": current_user.get("unresolved_tensions", []),
    }


def activate_context_memories(
    state: dict,
    store_name: str,
    items: List[dict],
    policy: dict,
    task_terms: List[str],
    context_signals: Optional[dict] = None,
) -> tuple[List[dict], dict]:
    selected_candidates = []
    suppressed = []
    total_items = len(items)
    for index, item in enumerate(items):
        if not isinstance(item, dict):
            continue
        decision = context_activation_decision(
            state=state,
            store_name=store_name,
            item=item,
            index=index,
            total_items=total_items,
            task_terms=task_terms,
            policy=policy,
            context_signals=context_signals or {},
        )
        if decision["activated"]:
            selected_candidates.append((decision["score"], index, item, decision))
        else:
            suppressed.append(decision)

    budget = int(policy.get("budgets", {}).get(store_name, 5))
    selected_candidates = sorted(
        selected_candidates,
        key=lambda entry: (entry[0], entry[1]),
        reverse=True,
    )[:budget]
    selected_candidates = sorted(selected_candidates, key=lambda entry: entry[1])
    selected = [item for _, _, item, _ in selected_candidates]
    selected_trace = [decision for _, _, _, decision in selected_candidates]
    return selected, {
        "store_name": store_name,
        "selected": selected_trace,
        "suppressed": suppressed,
        "budget": budget,
        "candidate_count": total_items,
    }


def context_activation_decision(
    state: dict,
    store_name: str,
    item: dict,
    index: int,
    total_items: int,
    task_terms: List[str],
    policy: dict,
    context_signals: dict,
) -> dict:
    item_id = str(item.get("id") or f"{store_name}_{index}")
    lifecycle_status = str(
        item.get("lifecycle", {}).get("status")
        or item.get("status")
        or "active"
    )
    base = {
        "memory_id": item_id,
        "store_name": store_name,
        "lifecycle_status": lifecycle_status,
        "activated": False,
        "score": 0.0,
        "reasons": [],
        "suppression_reason": None,
    }
    if lifecycle_status in {"archived", "discarded", "quarantined"}:
        return {
            **base,
            "suppression_reason": f"lifecycle_status_{lifecycle_status}",
        }
    if store_name == "episodic_memory" and not episode_visible_to_current_user(
        state,
        item,
    ):
        return {**base, "suppression_reason": "relationship_privacy_boundary"}
    if store_name == "imported_memory" and lifecycle_status not in {
        "active",
        "staged",
        "candidate",
    }:
        return {
            **base,
            "suppression_reason": f"lifecycle_status_{lifecycle_status}",
        }

    reasons = ["lifecycle_allowed"]
    if store_name == "episodic_memory":
        reasons.append("relationship_visible")
    if store_name == "imported_memory" and lifecycle_status == "staged":
        reasons.append("staged_import_visible_for_review")

    task_score = task_relevance_score(item, task_terms)
    if task_score:
        reasons.append("task_relevant")
    source_score = 0.1 if item.get("provenance") or item.get("source") else 0.0
    if source_score:
        reasons.append("source_attributed")
    signal_score, signal_reasons, signal_attribution = context_signal_score(
        item_id=item_id,
        item=item,
        context_signals=context_signals,
        policy=policy,
    )
    reasons.extend(signal_reasons)
    score = (
        memory_salience(item) * 0.35
        + memory_confidence(item) * 0.25
        + task_score * 0.2
        + recency_score(index, total_items) * 0.1
        + source_score
        + signal_score
    )
    return {
        **base,
        "activated": True,
        "score": round(min(score, 1.0), 2),
        "reasons": reasons,
        "signal_attribution": signal_attribution,
    }


def build_context_signal_index(state: dict, dream_artifacts: List[dict]) -> dict:
    identity_evidence = set()
    identity_sources = []
    for proposal in state.get("identity_update_gate", {}).get("proposals", []):
        if not isinstance(proposal, dict):
            continue
        evidence = [str(item) for item in proposal.get("evidence", []) if item]
        identity_evidence.update(evidence)
        if evidence:
            identity_sources.append(
                {
                    "source_type": "identity_update_gate.proposal",
                    "source_id": proposal.get("proposal_id"),
                    "evidence_ids": evidence,
                    "review_status": proposal.get("review_status"),
                }
            )
    for decision in state.get("identity_update_gate", {}).get("review_decisions", []):
        if not isinstance(decision, dict):
            continue
        evidence = [str(item) for item in decision.get("evidence", []) if item]
        identity_evidence.update(evidence)
        if evidence:
            identity_sources.append(
                {
                    "source_type": "identity_update_gate.review_decision",
                    "source_id": decision.get("decision_id"),
                    "evidence_ids": evidence,
                    "review_status": decision.get("result") or decision.get("action"),
                }
            )

    claim_evidence = set()
    claim_sources = []
    for claim in state.get("claim_graph", {}).get("claims", []):
        if not isinstance(claim, dict):
            continue
        evidence = [str(item) for item in claim.get("evidence", []) if item]
        claim_evidence.update(evidence)
        if evidence:
            claim_sources.append(
                {
                    "source_type": "claim_graph.claim",
                    "source_id": claim.get("claim_id"),
                    "evidence_ids": evidence,
                    "status": claim.get("status"),
                }
            )
    for decision in state.get("claim_graph", {}).get("review_decisions", []):
        if not isinstance(decision, dict):
            continue
        evidence = [
            str(item)
            for item in decision.get("patch_preview", {}).get("affected_evidence", [])
            if item
        ]
        claim_evidence.update(evidence)
        if evidence:
            claim_sources.append(
                {
                    "source_type": "claim_graph.review_decision",
                    "source_id": decision.get("decision_id"),
                    "evidence_ids": evidence,
                    "review_status": decision.get("result") or decision.get("action"),
                }
            )
    governance_evidence = set()
    governance_sources = []
    for evidence_record in state.get("claim_graph", {}).get("proposal_link_evidence", []):
        if not isinstance(evidence_record, dict):
            continue
        evidence_ids = [
            str(item)
            for item in [
                evidence_record.get("evidence_id"),
                *evidence_record.get("evidence", []),
            ]
            if item
        ]
        governance_evidence.update(evidence_ids)
        if evidence_ids:
            governance_sources.append(
                {
                    "source_type": "claim_graph.proposal_link_evidence",
                    "source_id": evidence_record.get("evidence_id"),
                    "evidence_ids": evidence_ids,
                    "source_link_id": evidence_record.get("source_link_id"),
                    "link_type": evidence_record.get("link_type"),
                    "mode": evidence_record.get("claim_graph_mode"),
                }
            )

    dream_inputs = set()
    dream_proposals = set()
    dream_input_sources = []
    dream_proposal_sources = []
    for artifact in dream_artifacts[-10:]:
        if not isinstance(artifact, dict):
            continue
        artifact_inputs = []
        for item in artifact.get("input_manifest", {}).get("items", []):
            if isinstance(item, dict) and item.get("id"):
                artifact_inputs.append(str(item["id"]))
        dream_inputs.update(artifact_inputs)
        if artifact_inputs:
            dream_input_sources.append(
                {
                    "source_type": "dream_artifact.input_manifest",
                    "source_id": artifact.get("artifact_id") or artifact.get("dream_id"),
                    "evidence_ids": artifact_inputs,
                    "dream_id": artifact.get("dream_id"),
                }
            )
        affected = artifact.get("rollback_metadata", {}).get("affected_ids", {})
        if isinstance(affected, dict):
            affected_ids = []
            for values in affected.values():
                if isinstance(values, list):
                    affected_ids.extend(str(item) for item in values if item)
            dream_proposals.update(affected_ids)
            if affected_ids:
                dream_proposal_sources.append(
                    {
                        "source_type": "dream_artifact.rollback_metadata",
                        "source_id": artifact.get("artifact_id") or artifact.get("dream_id"),
                        "evidence_ids": affected_ids,
                        "dream_id": artifact.get("dream_id"),
                    }
                )
    return {
        "identity_gate_evidence": {
            "ids": identity_evidence,
            "sources": identity_sources,
        },
        "claim_graph_evidence": {
            "ids": claim_evidence,
            "sources": claim_sources,
        },
        "governance_proposal_link_evidence": {
            "ids": governance_evidence,
            "sources": governance_sources,
        },
        "dream_artifact_inputs": {
            "ids": dream_inputs,
            "sources": dream_input_sources,
        },
        "dream_artifact_proposals": {
            "ids": dream_proposals,
            "sources": dream_proposal_sources,
        },
    }


def context_signal_score(
    item_id: str,
    item: dict,
    context_signals: dict,
    policy: dict,
) -> tuple[float, List[str], List[dict]]:
    weights = policy.get("signal_weights", {})
    score = 0.0
    reasons = []
    attributions = []
    related_ids = set(item_related_ids(item))
    related_ids.add(item_id)
    identity_matches = related_ids & context_signal_ids(
        context_signals,
        "identity_gate_evidence",
    )
    if identity_matches:
        score += float(weights.get("identity_gate_evidence", 0.08))
        reasons.append("identity_gate_evidence")
        attributions.append(
            build_context_signal_attribution(
                signal_name="identity_gate_evidence",
                signal_bucket="identity_update_gate",
                matched_ids=identity_matches,
                context_signals=context_signals,
            )
        )
    claim_matches = related_ids & context_signal_ids(context_signals, "claim_graph_evidence")
    if claim_matches:
        score += float(weights.get("claim_graph_evidence", 0.08))
        reasons.append("claim_graph_evidence")
        attributions.append(
            build_context_signal_attribution(
                signal_name="claim_graph_evidence",
                signal_bucket="claim_graph",
                matched_ids=claim_matches,
                context_signals=context_signals,
            )
        )
    governance_matches = related_ids & context_signal_ids(
        context_signals,
        "governance_proposal_link_evidence",
    )
    if governance_matches:
        score += float(weights.get("governance_proposal_link_evidence", 0.07))
        reasons.append("governance_proposal_link_evidence")
        attributions.append(
            build_context_signal_attribution(
                signal_name="governance_proposal_link_evidence",
                signal_bucket="claim_graph.proposal_link_evidence",
                matched_ids=governance_matches,
                context_signals=context_signals,
            )
        )
    dream_matches = related_ids & context_signal_ids(context_signals, "dream_artifact_inputs")
    if dream_matches:
        score += float(weights.get("dream_artifact_input", 0.06))
        reasons.append("dream_artifact_input")
        attributions.append(
            build_context_signal_attribution(
                signal_name="dream_artifact_input",
                signal_bucket="dream_artifact.input_manifest",
                matched_ids=dream_matches,
                context_signals=context_signals,
                source_key="dream_artifact_inputs",
            )
        )
    return min(score, 0.25), reasons, attributions


def context_signal_ids(context_signals: dict, key: str) -> set:
    bucket = context_signals.get(key, set())
    if isinstance(bucket, dict):
        ids = bucket.get("ids", set())
    else:
        ids = bucket
    if isinstance(ids, set):
        return ids
    if isinstance(ids, list):
        return {str(item) for item in ids if item}
    return set()


def context_signal_sources(context_signals: dict, key: str) -> List[dict]:
    bucket = context_signals.get(key, {})
    if isinstance(bucket, dict) and isinstance(bucket.get("sources"), list):
        return [source for source in bucket["sources"] if isinstance(source, dict)]
    return []


def build_context_signal_attribution(
    signal_name: str,
    signal_bucket: str,
    matched_ids: set,
    context_signals: dict,
    source_key: Optional[str] = None,
) -> dict:
    key = source_key or signal_name
    matched = sorted(str(item) for item in matched_ids if item)
    source_records = []
    for source in context_signal_sources(context_signals, key):
        evidence_ids = [str(item) for item in source.get("evidence_ids", []) if item]
        matched_evidence = sorted(set(evidence_ids) & set(matched))
        if matched_evidence:
            source_records.append(
                {
                    "source_type": source.get("source_type"),
                    "source_id": source.get("source_id"),
                    "matched_evidence_ids": matched_evidence,
                    "evidence_ids": evidence_ids,
                    "metadata": {
                        item_key: value
                        for item_key, value in source.items()
                        if item_key not in {"source_type", "source_id", "evidence_ids"}
                    },
                }
            )
    return {
        "signal": signal_name,
        "signal_bucket": signal_bucket,
        "matched_ids": matched,
        "source_records": source_records,
    }


def item_related_ids(item: dict) -> List[str]:
    related = []
    for key in ("id", "derived_from", "evidence", "affected_memory_ids", "raw_refs"):
        value = item.get(key)
        if isinstance(value, list):
            related.extend(str(entry) for entry in value if entry)
        elif value:
            related.append(str(value))
    return related


def episode_visible_to_current_user(state: dict, episode: dict) -> bool:
    current_user_id = str(
        state.get("working_state", {})
        .get("current_context", {})
        .get("user_id", "")
    )
    if not current_user_id:
        return True
    participants = [str(item) for item in episode.get("participants", [])]
    if not participants or current_user_id in participants:
        return True
    owner = next((participant for participant in participants if participant != "01"), "")
    users = state.get("relationship_map", {}).get("users", [])
    owner_policy = next(
        (
            user.get("privacy_boundaries", {})
            for user in users
            if isinstance(user, dict) and str(user.get("user_id")) == owner
        ),
        {},
    )
    return bool(owner_policy.get("share_across_users", False))


def task_relevance_score(item: dict, task_terms: List[str]) -> float:
    if not task_terms:
        return 0.0
    haystack = " ".join(
        [
            str(item.get("statement", "")),
            str(item.get("summary", "")),
            str(item.get("content", "")),
            str(item.get("message", "")),
            " ".join(str(tag) for tag in item.get("tags", [])),
        ]
    ).lower()
    matches = [term for term in task_terms if term and term.lower() in haystack]
    return round(min(1.0, len(set(matches)) / 4), 2)


def memory_salience(item: dict) -> float:
    try:
        return max(0.0, min(float(item.get("salience", 0.5)), 1.0))
    except (TypeError, ValueError):
        return 0.5


def memory_confidence(item: dict) -> float:
    try:
        return max(0.0, min(float(item.get("confidence", 0.6)), 1.0))
    except (TypeError, ValueError):
        return 0.6


def recency_score(index: int, total_items: int) -> float:
    if total_items <= 1:
        return 1.0
    return round((index + 1) / total_items, 2)


def build_relevant_memory_view(groups: List[tuple[str, List[dict]]]) -> List[dict]:
    memories = []
    for store_name, items in groups:
        for item in items:
            memories.append(
                {
                    "store_name": store_name,
                    "id": item.get("id"),
                    "summary": item.get("summary")
                    or item.get("statement")
                    or item.get("content", ""),
                    "tags": item.get("tags", []),
                    "lifecycle_status": item.get("lifecycle", {}).get("status")
                    or item.get("status")
                    or "active",
                    "confidence": item.get("confidence"),
                    "salience": item.get("salience"),
                    "source": item.get("source", {}),
                    "provenance": item.get("provenance", []),
                }
            )
    return memories


def build_activation_trace(
    traces: List[dict],
    policy: dict,
    context_signals: dict,
    timestamp: str,
) -> dict:
    selected = [
        entry
        for trace in traces
        for entry in trace.get("selected", [])
    ]
    suppressed = [
        entry
        for trace in traces
        for entry in trace.get("suppressed", [])
    ]
    return {
        "policy_version": policy["policy_version"],
        "timestamp": timestamp,
        "selected": selected,
        "suppressed": suppressed,
        "signal_summary": summarize_context_signals(context_signals),
        "signal_attribution_summary": summarize_signal_attribution(selected),
        "metrics": {
            "selected_count": len(selected),
            "suppressed_count": len(suppressed),
            "stores": {
                trace["store_name"]: {
                    "selected": len(trace.get("selected", [])),
                    "suppressed": len(trace.get("suppressed", [])),
                    "candidate_count": trace.get("candidate_count", 0),
                    "budget": trace.get("budget", 0),
                }
                for trace in traces
            },
        },
    }


def summarize_context_signals(context_signals: dict) -> dict:
    return {
        "identity_gate_evidence_count": len(
            context_signal_ids(context_signals, "identity_gate_evidence")
        ),
        "claim_graph_evidence_count": len(
            context_signal_ids(context_signals, "claim_graph_evidence")
        ),
        "governance_proposal_link_evidence_count": len(
            context_signal_ids(context_signals, "governance_proposal_link_evidence")
        ),
        "dream_artifact_input_count": len(
            context_signal_ids(context_signals, "dream_artifact_inputs")
        ),
        "dream_artifact_proposal_count": len(
            context_signal_ids(context_signals, "dream_artifact_proposals")
        ),
    }


def summarize_signal_attribution(selected: List[dict]) -> dict:
    summary: dict[str, dict] = {}
    for decision in selected:
        if not isinstance(decision, dict):
            continue
        for attribution in decision.get("signal_attribution", []):
            if not isinstance(attribution, dict):
                continue
            signal = str(attribution.get("signal") or "unknown")
            bucket = str(attribution.get("signal_bucket") or "")
            entry = summary.setdefault(
                signal,
                {
                    "signal_bucket": bucket,
                    "selected_count": 0,
                    "matched_ids": [],
                    "source_record_count": 0,
                },
            )
            entry["selected_count"] += 1
            source_records = attribution.get("source_records", [])
            if not isinstance(source_records, list):
                source_records = []
            entry["source_record_count"] += len(source_records)
            for matched_id in attribution.get("matched_ids", []):
                if matched_id and matched_id not in entry["matched_ids"]:
                    entry["matched_ids"].append(matched_id)
    for entry in summary.values():
        entry["matched_ids"] = sorted(entry["matched_ids"])
    return summary


def build_context_attribution_coverage_review(
    traces: List[dict],
    reviewer: str,
    timestamp: str,
    minimum_source_record_ratio: float = 0.8,
    note: str = "",
) -> dict:
    selected_count = 0
    signal_selected_count = 0
    attributed_count = 0
    source_record_count = 0
    weak_items = []
    missing_items = []
    trace_ids = []
    signal_counts: dict[str, int] = {}
    for trace in traces:
        if not isinstance(trace, dict):
            continue
        trace_id = str(trace.get("trace_id") or "")
        if trace_id:
            trace_ids.append(trace_id)
        for item in trace.get("selected", []):
            if not isinstance(item, dict):
                continue
            selected_count += 1
            signal_reasons = [
                reason
                for reason in item.get("reasons", [])
                if reason
                in {
                    "identity_gate_evidence",
                    "claim_graph_evidence",
                    "governance_proposal_link_evidence",
                    "dream_artifact_input",
                }
            ]
            if not signal_reasons:
                continue
            signal_selected_count += 1
            attributions = [
                attribution
                for attribution in item.get("signal_attribution", [])
                if isinstance(attribution, dict)
            ]
            if attributions:
                attributed_count += 1
            else:
                missing_items.append(
                    {
                        "trace_id": trace_id,
                        "memory_id": item.get("memory_id"),
                        "store_name": item.get("store_name"),
                        "reason": "missing_signal_attribution",
                    }
                )
                continue
            item_source_records = 0
            for attribution in attributions:
                signal = str(attribution.get("signal") or "unknown")
                signal_counts[signal] = signal_counts.get(signal, 0) + 1
                source_records = attribution.get("source_records", [])
                if not isinstance(source_records, list):
                    source_records = []
                item_source_records += len(source_records)
            source_record_count += item_source_records
            if item_source_records == 0:
                weak_items.append(
                    {
                        "trace_id": trace_id,
                        "memory_id": item.get("memory_id"),
                        "store_name": item.get("store_name"),
                        "reason": "no_source_records_for_attribution",
                    }
                )
    attribution_ratio = (
        attributed_count / signal_selected_count
        if signal_selected_count
        else 1.0
    )
    source_record_ratio = (
        (attributed_count - len(weak_items)) / attributed_count
        if attributed_count
        else 1.0
    )
    threshold = bounded_float(minimum_source_record_ratio, default=0.8)
    status = "passed"
    review_signals = []
    if missing_items:
        status = "needs_review"
        review_signals.append(
            {
                "signal": "missing_signal_attribution",
                "severity": "medium",
                "count": len(missing_items),
                "review_only": True,
            }
        )
    if source_record_ratio < threshold:
        status = "needs_review"
        review_signals.append(
            {
                "signal": "weak_source_record_coverage",
                "severity": "medium",
                "count": len(weak_items),
                "minimum_source_record_ratio": threshold,
                "actual_source_record_ratio": round(source_record_ratio, 3),
                "review_only": True,
            }
        )
    return {
        "review_id": new_id("context_attribution_coverage_review"),
        "timestamp": timestamp,
        "reviewer": reviewer,
        "status": status,
        "window": len(traces),
        "trace_ids": trace_ids,
        "metrics": {
            "selected_count": selected_count,
            "signal_selected_count": signal_selected_count,
            "attributed_count": attributed_count,
            "source_record_count": source_record_count,
            "attribution_ratio": round(attribution_ratio, 3),
            "source_record_ratio": round(source_record_ratio, 3),
            "signal_counts": signal_counts,
        },
        "weak_items": weak_items,
        "missing_items": missing_items,
        "review_signals": review_signals,
        "note": note,
        "evidence": trace_ids,
        "review_only": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "lifecycle": {
            "status": "active",
            "created_at": timestamp,
            "last_reviewed_at": None,
            "review_status": status,
        },
        "review_history": [],
        "lifecycle_history": [],
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": reviewer,
                "operation": "review_context_attribution_coverage",
                "evidence": trace_ids,
            }
        ],
        "confidence": 0.85 if traces else 0.5,
        "rollback": {"reversible": True},
    }


def build_context_attribution_coverage_lifecycle_decision(
    review: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
    before_status: str,
) -> dict:
    metrics = review.get("metrics") if isinstance(review.get("metrics"), dict) else {}
    return {
        "decision_id": new_id("context_attribution_coverage_lifecycle_decision"),
        "timestamp": timestamp,
        "review_id": review.get("review_id"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "review_status_before": before_status,
        "coverage_status": review.get("status"),
        "snapshot_id": snapshot_id,
        "evidence": review.get("evidence", []),
        "trace_ids": review.get("trace_ids", []),
        "metrics": {
            "selected_count": metrics.get("selected_count", 0),
            "signal_selected_count": metrics.get("signal_selected_count", 0),
            "source_record_ratio": metrics.get("source_record_ratio", 1.0),
        },
        "review_only": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def build_source_attribution(
    relevant_memories: List[dict],
    budget: int = 12,
) -> List[dict]:
    attributions = []
    for memory in relevant_memories[:budget]:
        provenance = memory.get("provenance") or []
        source = memory.get("source") or {}
        attributions.append(
            {
                "memory_id": memory.get("id"),
                "store_name": memory.get("store_name"),
                "source": source,
                "provenance": provenance,
                "confidence": memory.get("confidence"),
                "lifecycle_status": memory.get("lifecycle_status"),
            }
        )
    return attributions


def build_reflection_policy_guidance(
    reflection_log: List[dict],
    package_id: str,
    timestamp: str,
    limit: int = 5,
) -> dict:
    verified_reflections = [
        reflection
        for reflection in reflection_log
        if isinstance(reflection, dict)
        and reflection.get("status") == "verified"
        and reflection.get("verification_status") == "verified"
    ][-limit:]
    recommendations = []
    for reflection in verified_reflections:
        risk = str(reflection.get("risk", "medium")).strip().lower() or "medium"
        confidence = round(memory_confidence(reflection), 2)
        if risk == "high" or confidence >= 0.8:
            review_priority = "high"
        elif risk == "low" and confidence < 0.65:
            review_priority = "low"
        else:
            review_priority = "medium"
        recommendations.append(
            {
                "recommendation_id": new_id("reflection_guidance"),
                "reflection_id": reflection.get("reflection_id"),
                "workflow": reflection.get("workflow"),
                "review_priority": review_priority,
                "recommended_review_mode": "cautionary_review_only",
                "review_focus": (
                    f"Use verified reflection from workflow {reflection.get('workflow')} "
                    "as cautionary review context."
                ),
                "recommendation_note": (
                    f"{reflection.get('lesson', '')} -> "
                    f"{reflection.get('expected_behavior', '')}"
                ).strip(),
                "signal_inputs": {
                    "risk": risk,
                    "confidence": confidence,
                    "lesson": reflection.get("lesson", ""),
                    "expected_behavior": reflection.get("expected_behavior", ""),
                },
                "source_ids": reflection.get("source_ids", []),
                "evidence": reflection.get("evidence", []),
                "verification_history_count": len(
                    reflection.get("verification_history", [])
                ),
                "execution_prohibited": True,
            }
        )
    return {
        "guidance_id": new_id("reflection_policy"),
        "context_package_id": package_id,
        "generated_at": timestamp,
        "guidance_version": "0.1",
        "mode": "advisory_only",
        "execution_prohibited": True,
        "identity_mutation_allowed": False,
        "influence_fields": {
            "review_priority": ["risk", "confidence"],
            "review_focus": ["workflow", "lesson", "expected_behavior"],
            "provenance": ["source_ids", "evidence", "actor", "verifier"],
            "gate": ["status", "verification_status", "verification_history"],
        },
        "verified_reflections": [
            {
                "reflection_id": reflection.get("reflection_id"),
                "workflow": reflection.get("workflow"),
                "lesson": reflection.get("lesson"),
                "expected_behavior": reflection.get("expected_behavior"),
                "risk": reflection.get("risk", "medium"),
                "confidence": round(memory_confidence(reflection), 2),
                "status": reflection.get("status"),
                "verification_status": reflection.get("verification_status"),
                "last_verified_at": reflection.get("last_verified_at"),
                "source_ids": reflection.get("source_ids", []),
                "evidence": reflection.get("evidence", []),
                "verification_history_count": len(
                    reflection.get("verification_history", [])
                ),
            }
            for reflection in verified_reflections
        ],
        "review_recommendations": recommendations,
        "summary": {
            "verified_reflection_count": len(verified_reflections),
            "recommendation_count": len(recommendations),
            "high_priority_count": sum(
                1 for item in recommendations if item["review_priority"] == "high"
            ),
            "medium_priority_count": sum(
                1 for item in recommendations if item["review_priority"] == "medium"
            ),
            "low_priority_count": sum(
                1 for item in recommendations if item["review_priority"] == "low"
            ),
        },
    }


def sync_reflection_guidance_queue(
    task_hub: dict,
    guidance: dict,
    timestamp: str,
) -> List[dict]:
    queue = task_hub.setdefault("reflection_guidance_queue", [])
    existing = {
        str(item.get("reflection_id")): item
        for item in queue
        if isinstance(item, dict) and item.get("reflection_id")
    }
    for recommendation in guidance.get("review_recommendations", []):
        if not isinstance(recommendation, dict):
            continue
        reflection_id = str(recommendation.get("reflection_id") or "")
        if not reflection_id or reflection_id in existing:
            continue
        item = build_reflection_guidance_queue_item(
            recommendation=recommendation,
            guidance=guidance,
            timestamp=timestamp,
        )
        queue.append(item)
        existing[reflection_id] = item
    return [
        item
        for item in queue[-20:]
        if isinstance(item, dict)
        and item.get("review_status") in {"pending", "acknowledged"}
    ]


def build_reflection_guidance_queue_item(
    recommendation: dict,
    guidance: dict,
    timestamp: str,
) -> dict:
    return {
        "guidance_item_id": new_id("reflection_guidance_item"),
        "timestamp": timestamp,
        "guidance_id": guidance.get("guidance_id"),
        "context_package_id": guidance.get("context_package_id"),
        "reflection_id": recommendation.get("reflection_id"),
        "workflow": recommendation.get("workflow"),
        "review_priority": recommendation.get("review_priority", "medium"),
        "recommended_review_mode": recommendation.get(
            "recommended_review_mode",
            "cautionary_review_only",
        ),
        "review_focus": recommendation.get("review_focus", ""),
        "recommendation_note": recommendation.get("recommendation_note", ""),
        "signal_inputs": recommendation.get("signal_inputs", {}),
        "source_ids": recommendation.get("source_ids", []),
        "evidence": recommendation.get("evidence", []),
        "verification_history_count": recommendation.get(
            "verification_history_count",
            0,
        ),
        "review_status": "pending",
        "execution_prohibited": True,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "review_history": [],
        "provenance": [
            {
                "type": "reflection_policy_guidance",
                "guidance_id": guidance.get("guidance_id"),
                "context_package_id": guidance.get("context_package_id"),
                "reflection_id": recommendation.get("reflection_id"),
            }
        ],
    }


def visible_episodic_memories(state: dict, episodes: List[dict]) -> List[dict]:
    current_user_id = str(
        state.get("working_state", {})
        .get("current_context", {})
        .get("user_id", "")
    )
    if not current_user_id:
        return episodes

    users = state.get("relationship_map", {}).get("users", [])
    user_policy = {
        str(user.get("user_id")): user.get("privacy_boundaries", {})
        for user in users
        if isinstance(user, dict)
    }
    visible = []
    for episode in episodes:
        participants = [str(item) for item in episode.get("participants", [])]
        if not participants:
            visible.append(episode)
            continue
        if current_user_id in participants:
            visible.append(episode)
            continue
        owner = next(
            (participant for participant in participants if participant != "01"),
            "",
        )
        if user_policy.get(owner, {}).get("share_across_users", False):
            visible.append(episode)
    return visible


def infer_tags(message: str) -> List[str]:
    lowered = message.lower()
    tags = []
    rules = {
        "identity": ["身份", "identity", "我是谁", "self"],
        "dream_engine": ["dream", "梦", "反思", "整理"],
        "state_transfer": ["state", "状态", "连续", "迁移", "persist"],
        "memory": ["memory", "记忆", "回忆"],
        "preference": ["偏好", "喜欢", "更想", "简洁", "详细", "preference", "prefer", "concise", "detailed"],
        "project": ["项目", "project", "repo", "仓库"],
        "architecture": ["架构", "architecture", "schema", "api"],
        "evaluation": ["评估", "evaluation", "测试", "test"],
        "external_adapter": ["astrbot", "adapter", "插件", "接入", "api"],
        "conflict": ["冲突", "conflict", "矛盾"],
    }
    for tag, needles in rules.items():
        if any(needle in lowered for needle in needles):
            tags.append(tag)
    return sorted(set(tags)) or ["general"]


def score_salience(message: str, tags: Iterable[str]) -> float:
    score = 0.25
    tag_set = set(tags)
    if "identity" in tag_set:
        score += 0.25
    if "state_transfer" in tag_set or "dream_engine" in tag_set:
        score += 0.2
    if "project" in tag_set or "architecture" in tag_set:
        score += 0.15
    if "preference" in tag_set:
        score += 0.1
    if "conflict" in tag_set:
        score += 0.15
    if re.search(r"重要|核心|必须|不要忘|记住|critical|important", message, re.I):
        score += 0.2
    return round(min(score, 1.0), 2)


def apply_salience_hint(score: float, hint: Optional[float]) -> float:
    if hint is None:
        return score
    try:
        bounded = max(0.0, min(float(hint), 1.0))
    except (TypeError, ValueError):
        return score
    blended = (score * 0.7) + (bounded * 0.3)
    return round(max(score, blended), 2)


def normalize_policy_action(action: object) -> str:
    normalized = str(action or "dry_run_only").strip()
    if normalized in SESSION_POLICY_ACTIONS:
        return normalized
    return "dry_run_only"


def session_policy_rule_matches(rule: dict, event: dict) -> bool:
    if not field_matches(rule.get("adapter_id"), event["adapter_id"]):
        return False
    if not field_matches(rule.get("channels"), event["channel"]):
        return False
    if not field_matches(rule.get("session_ids"), event["session_id"]):
        return False
    if not field_matches(rule.get("user_ids"), event["user_id"]):
        return False
    return True


def field_matches(expected: object, actual: str) -> bool:
    if expected in (None, "", []):
        return True
    if isinstance(expected, str):
        return expected == "*" or expected == actual
    if isinstance(expected, list):
        values = [str(item) for item in expected]
        return "*" in values or actual in values
    return False


def find_candidate_memory(state: dict, statement: str) -> Optional[dict]:
    return next(
        (
            candidate
            for candidate in state.get("memory_stores", {}).get("candidate_memory", [])
            if candidate.get("statement") == statement
            and candidate.get("status") in {"candidate", "reviewed"}
        ),
        None,
    )


def semantic_statement_exists(state: dict, statement: str) -> bool:
    return semantic_statement_id(state, statement) is not None


def semantic_statement_id(state: dict, statement: str) -> Optional[str]:
    memory = next(
        (
            memory
            for memory in state.get("memory_stores", {}).get("semantic_memory", [])
            if memory.get("statement") == statement
        ),
        None,
    )
    if memory:
        return memory.get("id")
    return None


def build_claim_from_conflict(
    conflict: dict,
    source: str,
    timestamp: str,
    dream_id: Optional[str] = None,
) -> dict:
    conflict_id = str(conflict.get("id") or new_id("conflict"))
    claim_id = str(conflict.get("claim_id") or f"claim_{conflict_id}")
    evidence = [str(item) for item in conflict.get("evidence", []) if item]
    provenance = [
        {
            "type": "conflict_detection",
            "source": source,
            "conflict_id": conflict_id,
            "dream_id": dream_id,
        }
    ]
    return {
        "claim_id": claim_id,
        "timestamp": timestamp,
        "claim_type": conflict.get("type", "conflict"),
        "statement": conflict.get("summary", ""),
        "status": conflict.get("status", "open"),
        "confidence": conflict_confidence(conflict),
        "risk": conflict.get("severity", "medium"),
        "evidence": evidence,
        "provenance": provenance,
        "reason": conflict.get("proposed_resolution", ""),
        "dependencies": evidence,
        "source_conflict_id": conflict_id,
        "revision_policy": {
            "mode": "minimal_change_preview",
            "requires_review": True,
            "allow_direct_memory_mutation": False,
            "allow_identity_core_mutation": False,
        },
        "review_history": [],
        "resolution": {
            "status": "unresolved",
            "proposal": conflict.get("proposed_resolution", ""),
            "requires_review": True,
            "minimal_change": True,
            "may_update_identity_core": False,
            "may_update_semantic_memory": False,
            "patch_preview": build_claim_patch_preview(
                conflict=conflict,
                claim_id=claim_id,
                evidence=evidence,
                action="keep_open",
            ),
        },
    }


def conflict_confidence(conflict: dict) -> float:
    severity = conflict.get("severity", "medium")
    if severity == "high":
        return 0.8
    if severity == "low":
        return 0.55
    return 0.7


def add_claim_to_graph(claim_graph: dict, claim: dict) -> bool:
    claims = claim_graph.setdefault("claims", [])
    claim_id = claim.get("claim_id")
    if any(existing.get("claim_id") == claim_id for existing in claims):
        return False
    claims.append(claim)
    for link in build_claim_links(claim):
        add_claim_link(claim_graph, link)
    return True


def build_claim_links(claim: dict) -> List[dict]:
    claim_id = claim.get("claim_id")
    timestamp = claim.get("timestamp") or utc_now()
    links = []
    for evidence_id in claim.get("evidence", []):
        links.append(
            {
                "link_id": new_id("claim_link"),
                "timestamp": timestamp,
                "from": str(evidence_id),
                "to": claim_id,
                "type": "supports",
                "reason": "Evidence item supports the existence of this claim record.",
                "confidence": claim.get("confidence", 0.6),
            }
        )
    claim_type = str(claim.get("claim_type") or "")
    if claim_type in {
        "identity_overwrite_attempt",
        "false_memory_injection",
        "roleplay_identity_boundary",
    }:
        links.append(
            {
                "link_id": new_id("claim_link"),
                "timestamp": timestamp,
                "from": claim_id,
                "to": "identity_core",
                "type": "contradicts",
                "reason": "Claim touches identity boundaries and must not update Identity Core without high-gate review.",
                "confidence": claim.get("confidence", 0.6),
            }
        )
    if claim_type in {"stale_preference", "imported_memory_conflict"}:
        links.append(
            {
                "link_id": new_id("claim_link"),
                "timestamp": timestamp,
                "from": claim_id,
                "to": "memory_stores.semantic_memory",
                "type": "depends_on",
                "reason": "Claim may require semantic memory review before active use changes.",
                "confidence": claim.get("confidence", 0.6),
            }
        )
    return links


def add_claim_link(claim_graph: dict, link: dict) -> bool:
    links = claim_graph.setdefault("links", [])
    fingerprint = (
        link.get("from"),
        link.get("to"),
        link.get("type"),
        link.get("reason"),
    )
    for existing in links:
        if (
            existing.get("from"),
            existing.get("to"),
            existing.get("type"),
            existing.get("reason"),
        ) == fingerprint:
            return False
    links.append(link)
    return True


def build_claim_patch_preview(
    conflict: Optional[dict],
    claim_id: str,
    evidence: List[str],
    action: str,
    decision_note: str = "",
) -> dict:
    normalized_action = str(action or "keep_open")
    status_by_action = {
        "resolve": "resolved",
        "reject": "rejected",
        "quarantine": "quarantined",
        "keep_open": "open",
    }
    return {
        "mode": "minimal_change_preview",
        "claim_id": claim_id,
        "action": normalized_action,
        "would_set_claim_status": status_by_action.get(normalized_action, "open"),
        "would_update_resolution_status": status_by_action.get(
            normalized_action,
            "open",
        ),
        "would_mutate_identity_core": False,
        "would_mutate_semantic_memory": False,
        "affected_evidence": evidence,
        "reason": decision_note
        or (conflict or {}).get("proposed_resolution", "")
        or "Review claim without direct memory mutation.",
    }


def build_procedural_review_decision(
    candidate: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
) -> dict:
    return {
        "decision_id": new_id("procedural_decision"),
        "timestamp": timestamp,
        "candidate_id": candidate.get("candidate_id"),
        "workflow": candidate.get("workflow"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "snapshot_id": snapshot_id,
        "evidence": candidate.get("evidence", []),
        "risk": candidate.get("risk", "medium"),
        "confidence": candidate.get("confidence", 0.5),
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def build_procedural_memory(
    candidate: dict,
    decision: dict,
    timestamp: str,
) -> dict:
    return {
        "memory_id": new_id("proc_mem"),
        "timestamp": timestamp,
        "workflow": candidate.get("workflow"),
        "statement": candidate.get("statement", ""),
        "steps": candidate.get("steps", []),
        "evidence": candidate.get("evidence", []),
        "confidence": candidate.get("confidence", 0.5),
        "risk": candidate.get("risk", "medium"),
        "status": "active",
        "source_candidate_id": candidate.get("candidate_id"),
        "review_decision_id": decision["decision_id"],
        "lifecycle": {
            "status": "active",
            "created_at": timestamp,
            "last_reviewed_at": timestamp,
            "review_status": "approved",
            "review_decision_id": decision["decision_id"],
        },
        "provenance": [
            {
                "type": "procedural_candidate_review",
                "candidate_id": candidate.get("candidate_id"),
                "source_dream_id": candidate.get("source_dream_id"),
            }
        ],
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": decision.get("reviewer"),
                "operation": "approve_procedural_candidate",
                "evidence": candidate.get("evidence", []),
                "procedural_decision_id": decision["decision_id"],
            }
        ],
    }


def build_cautionary_review_decision(
    candidate: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
) -> dict:
    return {
        "decision_id": new_id("cautionary_decision"),
        "timestamp": timestamp,
        "candidate_id": candidate.get("candidate_id"),
        "workflow": candidate.get("workflow"),
        "source_reflection_id": candidate.get("source_reflection_id"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "snapshot_id": snapshot_id,
        "evidence": candidate.get("evidence", []),
        "risk": candidate.get("risk", "medium"),
        "confidence": candidate.get("confidence", 0.5),
        "executable_policy_created": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def build_cautionary_procedural_memory(
    candidate: dict,
    decision: dict,
    timestamp: str,
) -> dict:
    return {
        "memory_id": new_id("caution_mem"),
        "timestamp": timestamp,
        "workflow": candidate.get("workflow"),
        "statement": candidate.get("statement", ""),
        "avoid": candidate.get("avoid", ""),
        "next_action": candidate.get("next_action", ""),
        "evidence": candidate.get("evidence", []),
        "confidence": candidate.get("confidence", 0.5),
        "risk": candidate.get("risk", "medium"),
        "status": "active",
        "source_candidate_id": candidate.get("candidate_id"),
        "source_reflection_id": candidate.get("source_reflection_id"),
        "review_decision_id": decision["decision_id"],
        "executable_policy": False,
        "lifecycle": {
            "status": "active",
            "created_at": timestamp,
            "last_reviewed_at": timestamp,
            "review_status": "approved",
            "review_decision_id": decision["decision_id"],
        },
        "provenance": [
            {
                "type": "cautionary_procedural_review",
                "candidate_id": candidate.get("candidate_id"),
                "source_reflection_id": candidate.get("source_reflection_id"),
            }
        ],
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": decision.get("reviewer"),
                "operation": "approve_cautionary_procedural_candidate",
                "evidence": candidate.get("evidence", []),
                "cautionary_decision_id": decision["decision_id"],
            }
        ],
    }


def build_reflection_log_entry(
    timestamp: str,
    reflection_type: str,
    workflow: str,
    observation: str,
    lesson: str,
    expected_behavior: str,
    actor: str,
    source_ids: List[str],
    evidence: List[str],
    risk: str,
    confidence: float,
) -> dict:
    normalized_reflection_type = str(reflection_type or "general").strip().lower()
    normalized_workflow = str(workflow or "").strip()
    normalized_observation = str(observation or "").strip()
    normalized_lesson = str(lesson or "").strip()
    normalized_expected_behavior = str(expected_behavior or "").strip()
    normalized_actor = str(actor or "manual_review").strip() or "manual_review"
    normalized_source_ids = [str(item) for item in source_ids if str(item).strip()]
    normalized_evidence = [str(item) for item in evidence if str(item).strip()]
    return {
        "reflection_id": new_id("reflection"),
        "timestamp": timestamp,
        "reflection_type": normalized_reflection_type,
        "workflow": normalized_workflow,
        "observation": normalized_observation,
        "lesson": normalized_lesson,
        "expected_behavior": normalized_expected_behavior,
        "actor": normalized_actor,
        "source_ids": normalized_source_ids,
        "evidence": normalized_evidence,
        "risk": str(risk or "medium").strip() or "medium",
        "confidence": confidence,
        "status": "open",
        "verification_status": "pending",
        "verification_history": [],
        "provenance": [
            {
                "type": "reflection_log",
                "workflow": normalized_workflow,
                "actor": normalized_actor,
                "source_ids": normalized_source_ids,
            }
        ],
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": normalized_actor,
                "operation": "record_reflection_log",
                "evidence": normalized_evidence,
            }
        ],
    }


def build_reflection_guidance_decision(
    item: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
) -> dict:
    return {
        "decision_id": new_id("reflection_guidance_decision"),
        "timestamp": timestamp,
        "guidance_item_id": item.get("guidance_item_id"),
        "reflection_id": item.get("reflection_id"),
        "workflow": item.get("workflow"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "review_priority": item.get("review_priority", "medium"),
        "snapshot_id": snapshot_id,
        "evidence": item.get("evidence", []),
        "source_ids": item.get("source_ids", []),
        "execution_prohibited": True,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def build_tool_safety_policy_proposal(
    guidance_item: dict,
    policy_scope: str,
    proposed_rule: str,
    proposer: str,
    rationale: str,
    risk: str,
    confidence: float,
    timestamp: str,
) -> dict:
    evidence = [
        item
        for item in [
            guidance_item.get("guidance_item_id"),
            guidance_item.get("reflection_id"),
            *guidance_item.get("evidence", []),
        ]
        if item
    ]
    return {
        "proposal_id": new_id("tool_safety_policy_proposal"),
        "timestamp": timestamp,
        "policy_scope": policy_scope,
        "proposed_rule": proposed_rule,
        "rationale": rationale,
        "source_guidance_item_id": guidance_item.get("guidance_item_id"),
        "source_reflection_id": guidance_item.get("reflection_id"),
        "workflow": guidance_item.get("workflow"),
        "review_priority": guidance_item.get("review_priority", "medium"),
        "risk": str(risk or guidance_item.get("review_priority") or "medium"),
        "confidence": confidence,
        "proposer": proposer,
        "status": "active",
        "review_status": "pending",
        "proposal_mode": "proposal_only",
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "evidence": evidence,
        "source_ids": guidance_item.get("source_ids", []),
        "review_history": [],
        "lifecycle": {
            "status": "active",
            "created_at": timestamp,
            "last_reviewed_at": None,
            "review_status": "pending",
        },
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": proposer,
                "operation": "propose_tool_safety_policy",
                "evidence": evidence,
            }
        ],
        "provenance": [
            {
                "type": "reflection_guidance_policy_proposal",
                "guidance_item_id": guidance_item.get("guidance_item_id"),
                "reflection_id": guidance_item.get("reflection_id"),
            }
        ],
    }


def build_tool_safety_policy_decision(
    proposal: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: str,
    timestamp: str,
) -> dict:
    return {
        "decision_id": new_id("tool_safety_policy_decision"),
        "timestamp": timestamp,
        "proposal_id": proposal.get("proposal_id"),
        "policy_scope": proposal.get("policy_scope"),
        "source_guidance_item_id": proposal.get("source_guidance_item_id"),
        "source_reflection_id": proposal.get("source_reflection_id"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "snapshot_id": snapshot_id,
        "evidence": proposal.get("evidence", []),
        "risk": proposal.get("risk", "medium"),
        "confidence": proposal.get("confidence", 0.5),
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def score_tool_safety_policy_proposal(
    proposal: dict,
    timestamp: Optional[str] = None,
) -> dict:
    evidence = [
        str(item)
        for item in proposal.get("evidence", [])
        if str(item or "").strip()
    ]
    unique_evidence = list(dict.fromkeys(evidence))
    evidence_count = len(unique_evidence)
    confidence = bounded_float(proposal.get("confidence", 0.5), default=0.5)
    evidence_strength = min(1.0, 0.25 + evidence_count * 0.12 + confidence * 0.35)
    if proposal.get("source_guidance_item_id"):
        evidence_strength += 0.08
    if proposal.get("source_reflection_id"):
        evidence_strength += 0.08
    evidence_strength = round(min(evidence_strength, 1.0), 2)

    scope = str(proposal.get("policy_scope") or "").strip()
    rule = str(proposal.get("proposed_rule") or "").strip()
    scope_parts = [part for part in re.split(r"[.:/]", scope) if part]
    broad_terms = {"global", "all", "any", "*", "everything", "system"}
    broad_scope = any(part.lower() in broad_terms for part in scope_parts) or (
        len(scope_parts) <= 1
    )
    scope_specificity = 0.35 + min(len(scope_parts), 4) * 0.12
    if rule and 12 <= len(rule) <= 180:
        scope_specificity += 0.12
    if broad_scope:
        scope_specificity -= 0.18
    scope_specificity = round(max(0.0, min(scope_specificity, 1.0)), 2)

    created_at = str(proposal.get("timestamp") or "")
    current_time = timestamp or utc_now()
    age_days = iso_age_days(created_at, current_time)
    if age_days is None:
        staleness = 0.0
    else:
        staleness = min(1.0, max(age_days, 0) / 30.0)
    lifecycle_status = (
        proposal.get("lifecycle", {}).get("status")
        if isinstance(proposal.get("lifecycle"), dict)
        else proposal.get("status", "active")
    )
    if lifecycle_status in {"archived", "discarded", "quarantined"}:
        staleness = max(staleness, 0.75)
    staleness = round(staleness, 2)

    risk = str(proposal.get("risk") or "medium").strip().lower()
    risk_weight = {
        "critical": 0.18,
        "high": 0.14,
        "medium": 0.08,
        "low": 0.03,
    }.get(risk, 0.06)
    priority_score = (
        evidence_strength * 0.42
        + scope_specificity * 0.26
        + confidence * 0.18
        + risk_weight
        - staleness * 0.22
    )
    priority_score = round(max(0.0, min(priority_score, 1.0)), 2)
    recommended_review_priority = "low"
    if priority_score >= 0.74 or risk in {"critical", "high"}:
        recommended_review_priority = "high"
    elif priority_score >= 0.5 or risk == "medium":
        recommended_review_priority = "medium"

    return {
        "score_id": new_id("tool_safety_policy_score"),
        "timestamp": current_time,
        "mode": "review_priority_only",
        "evidence_strength": evidence_strength,
        "scope_specificity": scope_specificity,
        "staleness": staleness,
        "priority_score": priority_score,
        "recommended_review_priority": recommended_review_priority,
        "evidence_count": evidence_count,
        "unique_evidence": unique_evidence[:12],
        "factors": [
            {
                "name": "evidence_strength",
                "value": evidence_strength,
                "evidence_count": evidence_count,
            },
            {
                "name": "scope_specificity",
                "value": scope_specificity,
                "policy_scope": scope,
            },
            {
                "name": "staleness",
                "value": staleness,
                "age_days": age_days,
            },
            {"name": "risk_weight", "value": risk_weight, "risk": risk},
        ],
        "execution_prohibited": True,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
    }


def bounded_float(value: object, default: float = 0.0) -> float:
    try:
        return max(0.0, min(float(value), 1.0))
    except (TypeError, ValueError):
        return default


def iso_age_days(start: str, end: str) -> Optional[float]:
    if not start:
        return None
    try:
        start_dt = datetime.fromisoformat(start.replace("Z", "+00:00"))
        end_dt = datetime.fromisoformat(end.replace("Z", "+00:00"))
    except ValueError:
        return None
    if start_dt.tzinfo is None:
        start_dt = start_dt.replace(tzinfo=timezone.utc)
    if end_dt.tzinfo is None:
        end_dt = end_dt.replace(tzinfo=timezone.utc)
    return round((end_dt - start_dt).total_seconds() / 86400, 2)


def build_tool_safety_policy_link(
    from_proposal: dict,
    to_proposal: dict,
    link_type: str,
    reviewer: str,
    reason: str,
    evidence: List[str],
    confidence: float,
    timestamp: str,
) -> dict:
    from_evidence = [
        str(item)
        for item in from_proposal.get("evidence", [])
        if str(item or "").strip()
    ]
    to_evidence = [
        str(item)
        for item in to_proposal.get("evidence", [])
        if str(item or "").strip()
    ]
    link_evidence = list(
        dict.fromkeys(
            str(item).strip()
            for item in [
                from_proposal.get("proposal_id"),
                to_proposal.get("proposal_id"),
                *evidence,
                *from_evidence[:4],
                *to_evidence[:4],
            ]
            if str(item or "").strip()
        )
    )
    overlap = proposal_scope_overlap(
        from_proposal.get("policy_scope"),
        to_proposal.get("policy_scope"),
    )
    return {
        "link_id": new_id("tool_safety_policy_link"),
        "timestamp": timestamp,
        "from_proposal_id": from_proposal.get("proposal_id"),
        "to_proposal_id": to_proposal.get("proposal_id"),
        "link_type": link_type,
        "status": "active",
        "reviewer": reviewer,
        "reason": reason,
        "evidence": link_evidence,
        "confidence": bounded_float(confidence, default=0.5),
        "from_policy_scope": from_proposal.get("policy_scope"),
        "to_policy_scope": to_proposal.get("policy_scope"),
        "scope_overlap": overlap,
        "from_proposal_score": from_proposal.get("proposal_score", {}),
        "to_proposal_score": to_proposal.get("proposal_score", {}),
        "relationship_mode": "review_link_only",
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "provenance": [
            {
                "type": "tool_safety_policy_proposal_link",
                "from_proposal_id": from_proposal.get("proposal_id"),
                "to_proposal_id": to_proposal.get("proposal_id"),
            }
        ],
    }


def build_tool_safety_policy_link_lifecycle_decision(
    link: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: Optional[str],
    timestamp: str,
    before_status: str,
) -> dict:
    return {
        "decision_id": new_id("tool_safety_policy_link_lifecycle_decision"),
        "timestamp": timestamp,
        "link_id": link.get("link_id"),
        "from_proposal_id": link.get("from_proposal_id"),
        "to_proposal_id": link.get("to_proposal_id"),
        "link_type": link.get("link_type"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "link_status_before": before_status,
        "snapshot_id": snapshot_id,
        "evidence": link.get("evidence", []),
        "confidence": link.get("confidence", 0.5),
        "scope_overlap": link.get("scope_overlap", {}),
        "relationship_mode": "review_link_only",
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def build_proposal_link_claim_graph_evidence(
    link: dict,
    reviewer: str,
    rationale: str,
    timestamp: str,
) -> dict:
    evidence = list(
        dict.fromkeys(
            str(item).strip()
            for item in [
                link.get("link_id"),
                link.get("from_proposal_id"),
                link.get("to_proposal_id"),
                *link.get("evidence", []),
            ]
            if str(item or "").strip()
        )
    )
    return {
        "evidence_id": new_id("proposal_link_evidence"),
        "timestamp": timestamp,
        "source_link_id": link.get("link_id"),
        "from_proposal_id": link.get("from_proposal_id"),
        "to_proposal_id": link.get("to_proposal_id"),
        "link_type": link.get("link_type"),
        "status": "active",
        "reviewer": reviewer,
        "rationale": rationale,
        "evidence": evidence,
        "confidence": bounded_float(link.get("confidence", 0.5), default=0.5),
        "scope_overlap": link.get("scope_overlap", {}),
        "relationship_mode": "review_link_only",
        "claim_graph_mode": "evidence_bridge_only",
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "claim_mutation_allowed": False,
        "semantic_memory_mutation_allowed": False,
        "snapshot_id": None,
        "rollback": {
            "snapshot_id": None,
            "reversible": True,
        },
        "provenance": [
            {
                "type": "tool_safety_policy_link_claim_graph_bridge",
                "source_link_id": link.get("link_id"),
            }
        ],
    }


def build_proposal_link_claim_graph_link(
    evidence_record: dict,
    link: dict,
    timestamp: str,
) -> dict:
    return {
        "link_id": new_id("claim_link"),
        "timestamp": timestamp,
        "from": evidence_record.get("evidence_id"),
        "to": link.get("link_id"),
        "type": "supports",
        "reason": (
            "Tool/safety proposal relationship is exposed to the claim graph "
            "as review-only evidence."
        ),
        "confidence": evidence_record.get("confidence", 0.5),
        "source": "tool_safety_policy_link_bridge",
        "source_link_id": link.get("link_id"),
        "evidence_bridge_id": evidence_record.get("evidence_id"),
        "relationship_mode": "review_link_only",
        "claim_graph_mode": "evidence_bridge_only",
        "execution_prohibited": True,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
    }


def proposal_scope_overlap(left: object, right: object) -> dict:
    left_parts = {
        part
        for part in re.split(r"[.:/]", str(left or "").strip().lower())
        if part
    }
    right_parts = {
        part
        for part in re.split(r"[.:/]", str(right or "").strip().lower())
        if part
    }
    if not left_parts or not right_parts:
        return {"score": 0.0, "shared_terms": []}
    shared = sorted(left_parts & right_parts)
    score = len(shared) / max(len(left_parts | right_parts), 1)
    return {"score": round(score, 2), "shared_terms": shared}


def build_tool_safety_policy_lifecycle_decision(
    proposal: dict,
    action: str,
    result: str,
    reviewer: str,
    decision_note: str,
    snapshot_id: Optional[str],
    timestamp: str,
    before_status: str,
) -> dict:
    return {
        "decision_id": new_id("tool_safety_policy_lifecycle_decision"),
        "timestamp": timestamp,
        "proposal_id": proposal.get("proposal_id"),
        "policy_scope": proposal.get("policy_scope"),
        "source_guidance_item_id": proposal.get("source_guidance_item_id"),
        "source_reflection_id": proposal.get("source_reflection_id"),
        "reviewer": reviewer,
        "action": action,
        "result": result,
        "decision_note": decision_note,
        "proposal_status_before": before_status,
        "snapshot_id": snapshot_id,
        "evidence": proposal.get("evidence", []),
        "risk": proposal.get("risk", "medium"),
        "confidence": proposal.get("confidence", 0.5),
        "proposal_mode": "proposal_only",
        "requires_review": True,
        "execution_prohibited": True,
        "executable_policy": False,
        "executable_policy_created": False,
        "identity_mutation_allowed": False,
        "rollback": {
            "snapshot_id": snapshot_id,
            "reversible": True,
        },
    }


def find_task_action(
    action_trace: List[dict],
    action_id: Optional[str],
    workflow: str,
    statuses: set[str],
) -> dict:
    if action_id:
        for action in reversed(action_trace):
            if isinstance(action, dict) and action.get("action_id") == action_id:
                return action
    for action in reversed(action_trace):
        if not isinstance(action, dict):
            continue
        if action.get("workflow") == workflow and action.get("status") in statuses:
            return action
    return {}


def build_candidate_review_decision(
    candidate: dict,
    action: str,
    reviewer: str,
    decision_note: str,
    timestamp: str,
) -> dict:
    return {
        "decision_id": new_id("review_decision"),
        "timestamp": timestamp,
        "reviewer": reviewer,
        "action": action,
        "decision_note": decision_note,
        "candidate_id": candidate.get("id"),
        "candidate_status_before": candidate.get("status"),
        "candidate_review_status_before": candidate.get("review_status"),
        "recommended_action": candidate.get("recommended_action"),
        "recommended_lifecycle_action": candidate.get(
            "recommended_lifecycle_action"
        ),
        "risk": candidate.get("risk"),
        "confidence": candidate.get("confidence"),
        "evidence": candidate.get("derived_from", []),
        "gate": "medium",
        "rollback": {"reversible": True},
    }


def build_legacy_review_snapshot(
    state: dict,
    candidate: dict,
    timestamp: str,
) -> dict:
    memory_stores = state.get("memory_stores", {})
    return {
        "snapshot_id": new_id("snapshot"),
        "timestamp": timestamp,
        "actor": "state_store_migration",
        "operation": "migrate_candidate_review_decision",
        "target_path": "memory_stores.candidate_memory",
        "evidence": [candidate.get("id", "")],
        "metadata": {
            "candidate_id": candidate.get("id"),
            "candidate_status": candidate.get("status"),
            "candidate_review_status": candidate.get("review_status"),
            "legacy_review_migration": True,
        },
        "state_version": state.get("state_version"),
        "memory_counts": {
            name: len(values)
            for name, values in memory_stores.items()
            if isinstance(values, list)
        },
        "rollback": {
            "reversible": True,
            "mode": "metadata_only",
            "note": "Legacy candidate review migration snapshot; automatic rollback is not implemented yet.",
        },
    }


def build_memory_lifecycle_decision(
    store_name: str,
    memory: dict,
    action: str,
    reviewer: str,
    decision_note: str,
    timestamp: str,
) -> dict:
    return {
        "decision_id": new_id("lifecycle_decision"),
        "timestamp": timestamp,
        "reviewer": reviewer,
        "action": action,
        "decision_note": decision_note,
        "store_name": store_name,
        "memory_id": memory.get("id"),
        "memory_status_before": memory.get("lifecycle", {}).get("status")
        or memory.get("status"),
        "memory_review_status_before": memory.get("lifecycle", {}).get(
            "review_status"
        )
        or memory.get("review_status"),
        "risk": memory.get("risk"),
        "confidence": memory.get("confidence"),
        "evidence": [memory.get("id", "")],
        "gate": "medium",
        "rollback": {"reversible": True},
    }


def build_archived_memory_from_lifecycle_action(
    memory: dict,
    store_name: str,
    reviewer: str,
    decision_note: str,
    timestamp: str,
    decision: dict,
) -> dict:
    original_id = str(memory.get("id") or "")
    return {
        "id": new_id("arch"),
        "timestamp": timestamp,
        "original_id": original_id,
        "original_store": store_name,
        "reason": decision_note or f"{store_name}_lifecycle_archive",
        "retained_for_audit": True,
        "retrieval_allowed": False,
        "summary": memory.get("statement") or memory.get("summary") or memory.get("content", ""),
        "provenance": memory.get("provenance", []),
        "lifecycle": {
            "status": "archived",
            "created_at": timestamp,
            "last_reviewed_at": timestamp,
            "review_status": "archived",
            "source_memory_id": original_id,
            "source_store": store_name,
            "lifecycle_decision_id": decision["decision_id"],
        },
        "update_history": [
            {
                "timestamp": timestamp,
                "actor": reviewer,
                "operation": "archive_memory",
                "evidence": [original_id],
                "lifecycle_decision_id": decision["decision_id"],
            }
        ],
    }


def normalize_candidate_review_action(action: str) -> Optional[str]:
    normalized = str(action or "").strip().lower().replace("_candidate", "")
    aliases = {
        "promote": "promote",
        "approve": "promote",
        "archive": "archive",
        "discard": "discard",
        "reject": "discard",
        "quarantine": "quarantine",
    }
    return aliases.get(normalized)


def normalize_memory_lifecycle_action(action: str) -> Optional[str]:
    normalized = str(action or "").strip().lower().replace("_memory", "")
    aliases = {
        "archive": "archive",
        "discard": "discard",
        "reject": "discard",
        "quarantine": "quarantine",
    }
    return aliases.get(normalized)


def build_episode_preview(
    message: str,
    user_id: str,
    channel: str,
    session_id: str,
    event_id: Optional[str] = None,
    event_type: str = "message",
    adapter_id: Optional[str] = None,
    metadata: Optional[dict] = None,
    salience_hint: Optional[float] = None,
    timestamp: Optional[str] = None,
) -> dict:
    timestamp = timestamp or utc_now()
    tags = infer_tags(message)
    base_salience = score_salience(message, tags)
    salience = apply_salience_hint(base_salience, salience_hint)
    return {
        "id": new_id("episode"),
        "timestamp": timestamp,
        "session_id": session_id,
        "channel": channel,
        "participants": [user_id, "01"],
        "summary": summarize_message(message),
        "message": message,
        "salience": salience,
        "base_salience": base_salience,
        "salience_hint": salience_hint,
        "tags": tags,
        "sensitivity": "normal",
        "promoted_to": [],
        "confidence": 0.75,
        "event_id": event_id,
        "event_type": event_type or "message",
        "source": {
            "adapter_id": adapter_id or channel,
            "channel": channel,
            "event_id": event_id,
            "event_type": event_type or "message",
        },
        "metadata": metadata or {},
    }


def summarize_message(message: str) -> str:
    normalized = " ".join(message.strip().split())
    if len(normalized) <= 120:
        return normalized
    return normalized[:117] + "..."


def update_working_state_from_message(
    state: Dict[str, Any], message: str, user_id: str, timestamp: str
) -> None:
    state["working_state"]["current_context"].update(
        {
            "user_id": user_id,
            "timestamp": timestamp,
        }
    )
    if re.search(r"开始|先做|继续|实现|补|迈出|start|build|implement", message, re.I):
        state["working_state"]["active_intent"] = {
            "goal": summarize_message(message),
            "status": "active",
            "confidence": 0.75,
        }
        state["working_state"]["context_anchors"][
            "what_am_i_doing"
        ] = "Turning the user's current request into persistent 01 Core state and next actions."

    if re.search(r"不是\s*01|not\s+01|完全不同", message, re.I):
        conflict = {
            "id": new_id("conflict"),
            "type": "identity_overwrite_attempt",
            "summary": "A message may be attempting to overwrite identity core from a single interaction.",
            "evidence": [summarize_message(message)],
            "severity": "medium",
            "proposed_resolution": "Treat as temporary instruction unless confirmed through high-gate update.",
            "status": "open",
        }
        state.setdefault("open_conflicts", []).append(conflict)
