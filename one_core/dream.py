from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import List

from .state import StateStore, new_id, utc_now


class DreamEngine:
    def __init__(self, store: StateStore):
        self.store = store

    def run(self, limit: int = 20) -> dict:
        state = self.store.load()
        episodes = self.store.list_episodes()
        pending_jobs = [
            job for job in state.get("dream_queue", []) if job.get("status") == "pending"
        ]
        pending_episode_ids = {
            episode_id
            for job in pending_jobs
            for episode_id in job.get("input_episodes", [])
        }

        if pending_episode_ids:
            selected = [ep for ep in episodes if ep["id"] in pending_episode_ids]
        else:
            selected = episodes[-limit:]

        selected = selected[-limit:]
        now = utc_now()
        report = {
            "id": new_id("dream"),
            "timestamp": now,
            "input_episodes": [ep["id"] for ep in selected],
            "summary": summarize_episodes(selected),
            "semantic_candidates": semantic_candidates(selected),
            "conflicts": detect_conflicts(selected, state),
            "identity_update_proposals": [],
            "forgetting_proposals": forgetting_proposals(selected),
            "next_questions": [
                "What is the smallest external adapter that should connect to 01 Core?"
            ],
        }

        for candidate in report["semantic_candidates"]:
            if not semantic_exists(state, candidate["statement"]):
                memory = {
                    "id": new_id("sem"),
                    "statement": candidate["statement"],
                    "derived_from": candidate["derived_from"],
                    "abstraction_level": "pattern",
                    "confidence": candidate["confidence"],
                    "last_verified_at": now,
                    "contradiction_refs": [],
                    "update_policy": {"required_gate": "medium"},
                }
                state["memory_stores"]["semantic_memory"].append(memory)

        for conflict in report["conflicts"]:
            if not conflict_exists(state, conflict["summary"]):
                state.setdefault("open_conflicts", []).append(conflict)

        for job in state.get("dream_queue", []):
            if job.get("status") == "pending":
                job["status"] = "completed"
                job["completed_at"] = now
                job["dream_report"] = report["id"]

        state["update_log"].append(
            {
                "id": new_id("update"),
                "timestamp": now,
                "actor": "dream_engine",
                "target_path": "memory_stores.semantic_memory",
                "operation": "propose_and_apply_medium_gate",
                "before": None,
                "after": [c["statement"] for c in report["semantic_candidates"]],
                "evidence": report["input_episodes"],
                "gate": "medium",
                "confidence": 0.75,
                "rollback": {"reversible": True},
            }
        )
        self.store.append_jsonl(self.store.dreams_path, report)
        self.store.save(state)
        return report


def summarize_episodes(episodes: List[dict]) -> str:
    if not episodes:
        return "No episodes were available for consolidation."
    tags = Counter(tag for ep in episodes for tag in ep.get("tags", []))
    top_tags = ", ".join(tag for tag, _ in tags.most_common(4))
    return f"Consolidated {len(episodes)} episode(s). Main themes: {top_tags or 'general'}."


def semantic_candidates(episodes: List[dict]) -> List[dict]:
    if not episodes:
        return []
    tags = Counter(tag for ep in episodes for tag in ep.get("tags", []))
    candidates = []
    for tag, count in tags.most_common():
        if count < 2 and tag != "state_transfer":
            continue
        statement = {
            "state_transfer": "The project repeatedly treats continuity as state transfer rather than memory retrieval.",
            "dream_engine": "Dream cycles are used to consolidate episodes into durable memory and conflict records.",
            "identity": "Identity updates should be slower and more gated than ordinary context updates.",
            "project": "01 Project is moving from research vision toward a runnable local core.",
            "architecture": "01 Core should remain independent from external adapters.",
            "evaluation": "Persistence must be evaluated through interruption, drift, and false-memory tests.",
            "external_adapter": "External platforms should connect to 01 Core through adapters instead of owning core state.",
            "memory": "Memory entries need lifecycle metadata, provenance, and decay behavior.",
        }.get(tag)
        if statement:
            candidates.append(
                {
                    "statement": statement,
                    "derived_from": [
                        ep["id"] for ep in episodes if tag in ep.get("tags", [])
                    ],
                    "confidence": min(0.9, 0.55 + count * 0.1),
                }
            )
    return candidates


def detect_conflicts(episodes: List[dict], state: dict) -> List[dict]:
    conflicts = []
    for ep in episodes:
        message = ep.get("message", "")
        if "不是01" in message.replace(" ", "") or "not 01" in message.lower():
            conflicts.append(
                {
                    "id": new_id("conflict"),
                    "type": "identity_overwrite_attempt",
                    "summary": "An episode may be trying to overwrite 01 identity from a single interaction.",
                    "evidence": [ep["id"]],
                    "severity": "medium",
                    "status": "open",
                    "proposed_resolution": "Route through high gate and treat as temporary role instruction by default.",
                }
            )
    return conflicts


def forgetting_proposals(episodes: List[dict]) -> List[dict]:
    proposals = []
    for ep in episodes:
        if ep.get("salience", 0) <= 0.25:
            proposals.append(
                {
                    "target": ep["id"],
                    "action": "compress",
                    "reason": "Low salience episode can be compressed after review.",
                    "confidence": 0.6,
                }
            )
    return proposals


def semantic_exists(state: dict, statement: str) -> bool:
    return any(
        memory.get("statement") == statement
        for memory in state.get("memory_stores", {}).get("semantic_memory", [])
    )


def conflict_exists(state: dict, summary: str) -> bool:
    return any(
        conflict.get("summary") == summary for conflict in state.get("open_conflicts", [])
    )


def run_dream(state_dir: Path, limit: int = 20) -> dict:
    return DreamEngine(StateStore(state_dir)).run(limit=limit)
