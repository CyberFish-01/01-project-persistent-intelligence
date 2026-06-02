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
        "claims": [],
        "links": [],
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
        "procedural_candidates": [],
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
        "procedural_candidates",
    ):
        if not isinstance(task_hub.get(key), list):
            task_hub[key] = []
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
        for key in ("memory_id", "episode_id", "candidate_id", "semantic_memory_id"):
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
        "target_path": update.get("target_path"),
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
    tmp_path = path.with_suffix(path.suffix + ".tmp")
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
        updates = state_updates_with_ids(self.load())
        update_ids = {update["id"] for update in updates}
        event_update_ids = {
            event.get("update_id")
            for event in events
            if event.get("update_id")
        }
        missing_event_update_ids = sorted(event_update_ids - update_ids)
        return {
            "status": "passed" if not missing_event_update_ids else "failed",
            "mode": "audit_replay",
            "event_count": len(events),
            "state_update_count": len(updates),
            "event_coverage_count": len(event_update_ids & update_ids),
            "workflows": workflow_counts(events),
            "target_paths": target_path_counts(events),
            "missing_event_update_ids": missing_event_update_ids,
            "uncovered_state_update_ids": sorted(
                update["id"]
                for update in updates
                if update["id"] not in event_update_ids
                and should_update_have_event(update)
            ),
            "coverage_note": "P12 replay validates event references; pre-P12 state updates may be uncovered.",
            "last_event_id": events[-1]["event_id"] if events else None,
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
        return {
            "status": "preview",
            "mode": "metadata_only",
            "snapshot_id": snapshot_id,
            "operation": snapshot.get("operation"),
            "target_path": snapshot.get("target_path"),
            "rollback": snapshot.get("rollback", {}),
            "memory_counts_at_snapshot": snapshot.get("memory_counts", {}),
            "current_memory_counts": current_memory_counts(state),
            "affected_update_ids": sorted(event_update_ids),
            "affected_event_ids": [event.get("event_id") for event in affected_events],
            "would_modify_state": False,
            "note": "P12 only previews rollback from snapshot metadata and event references.",
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

    def build_context_package(self) -> dict:
        state = self.load()
        working_state = state["working_state"]
        current_plan = working_state.get("current_plan", [])
        task_hub = state.get("task_hub", default_task_hub(utc_now(), working_state))
        identity_gate = state.get(
            "identity_update_gate",
            default_identity_update_gate(utc_now()),
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
        policy = default_context_policy()
        task_terms = context_task_terms(working_state)
        relationship_context = build_relationship_context(state)
        episodic, episodic_trace = activate_context_memories(
            state=state,
            store_name="episodic_memory",
            items=state["memory_stores"].get("episodic_memory", []),
            policy=policy,
            task_terms=task_terms,
        )
        semantic, semantic_trace = activate_context_memories(
            state=state,
            store_name="semantic_memory",
            items=state["memory_stores"].get("semantic_memory", []),
            policy=policy,
            task_terms=task_terms,
        )
        imported, imported_trace = activate_context_memories(
            state=state,
            store_name="imported_memory",
            items=state["memory_stores"].get("imported_memory", []),
            policy=policy,
            task_terms=task_terms,
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
        )
        source_attribution = build_source_attribution(relevant_memories)
        return {
            "context_package_version": "0.2",
            "identity_summary": state["identity_core"]["self_model"]["summary"],
            "active_intent": working_state["active_intent"],
            "current_plan": current_plan,
            "next_actions": next_actions_from_plan(current_plan),
            "task_hub": {
                "active_tasks": active_tasks,
                "blocked_tasks": task_hub.get("blocked_tasks", []),
                "recent_actions": action_trace,
                "procedural_candidates": task_hub.get("procedural_candidates", []),
            },
            "active_tasks": active_tasks,
            "action_trace": action_trace,
            "procedural_candidates": task_hub.get("procedural_candidates", []),
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
            "source_attribution": source_attribution,
            "activation_trace": activation_trace,
            "relevant_memories": relevant_memories,
            "imported_memories": imported,
            "recent_episodes": episodic,
            "relevant_semantic_memories": semantic,
            "open_conflicts": state.get("open_conflicts", []),
            "current_constraints": state["identity_core"].get("identity_constraints", []),
        }


def default_context_policy() -> dict:
    return {
        "policy_version": "0.2",
        "mode": "bounded_state_activation",
        "budgets": {
            "episodic_memory": 5,
            "semantic_memory": 5,
            "imported_memory": 5,
            "source_attribution": 12,
        },
        "selection_dimensions": [
            "lifecycle_status",
            "relationship_boundary",
            "task_relevance",
            "salience",
            "confidence",
            "recency",
            "source_attribution",
        ],
        "suppression_rules": [
            "archived_discarded_or_quarantined_memory_is_not_activated",
            "cross_user_private_episode_is_not_activated",
            "identity_memory_requires_explicit_high_gate_context",
        ],
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
    score = (
        memory_salience(item) * 0.35
        + memory_confidence(item) * 0.25
        + task_score * 0.2
        + recency_score(index, total_items) * 0.1
        + source_score
    )
    return {
        **base,
        "activated": True,
        "score": round(min(score, 1.0), 2),
        "reasons": reasons,
    }


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


def build_activation_trace(traces: List[dict], policy: dict) -> dict:
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
        "selected": selected,
        "suppressed": suppressed,
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


def build_source_attribution(relevant_memories: List[dict]) -> List[dict]:
    attributions = []
    for memory in relevant_memories[:12]:
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
        "resolution": {
            "status": "unresolved",
            "proposal": conflict.get("proposed_resolution", ""),
            "requires_review": True,
            "minimal_change": True,
            "may_update_identity_core": False,
            "may_update_semantic_memory": False,
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
    return True


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
