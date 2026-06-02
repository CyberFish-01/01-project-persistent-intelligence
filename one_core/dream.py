from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import List, Optional

from .schema_defaults import default_identity_update_gate
from .state import (
    StateStore,
    add_claim_to_graph,
    build_claim_from_conflict,
    new_id,
    utc_now,
)


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
        pending_import_ids = {
            import_id for job in pending_jobs for import_id in job.get("input_imports", [])
        }

        if pending_episode_ids:
            selected = [ep for ep in episodes if ep["id"] in pending_episode_ids]
        else:
            selected = episodes[-limit:]

        selected = selected[-limit:]
        imported = state.get("memory_stores", {}).get("imported_memory", [])
        selected_imports = [
            memory for memory in imported if memory["id"] in pending_import_ids
        ][:limit]
        selected_items = selected + selected_imports
        now = utc_now()
        semantic = semantic_candidates(selected_items)
        conflicts = detect_conflicts(selected_items, state)
        forgetting = forgetting_proposals(selected)
        identity_updates = identity_update_proposals(conflicts)
        procedural = procedural_candidates(state)
        proposals = build_dream_proposals(
            semantic_candidates=semantic,
            identity_update_proposals=identity_updates,
            forgetting_proposals=forgetting,
            conflicts=conflicts,
        )
        rubric = score_dream_rubric(
            selected_items=selected_items,
            proposals=proposals,
            conflicts=conflicts,
        )
        report = {
            "id": new_id("dream"),
            "timestamp": now,
            "input_episodes": [ep["id"] for ep in selected],
            "input_imports": [memory["id"] for memory in selected_imports],
            "summary": summarize_items(selected_items),
            "semantic_candidates": semantic,
            "conflicts": conflicts,
            "identity_update_proposals": identity_updates,
            "forgetting_proposals": forgetting,
            "procedural_candidates": procedural,
            "proposals": proposals,
            "rubric": rubric,
            "rubric_summary": summarize_rubric(rubric),
            "next_questions": [
                "What is the smallest external adapter that should connect to 01 Core?"
            ],
        }
        candidate_memories = []
        for proposal in report["proposals"]:
            candidate_memory = self.store.add_candidate_memory(
                state=state,
                proposal=proposal,
                dream_id=report["id"],
                timestamp=now,
            )
            if candidate_memory:
                candidate_memories.append(candidate_memory)
        report["candidate_memories"] = [memory["id"] for memory in candidate_memories]
        identity_gate_ids = []
        for proposal in report["proposals"]:
            if proposal.get("type") != "identity_update_candidate":
                continue
            stored = add_identity_gate_proposal_from_dream(
                state=state,
                proposal=proposal,
                timestamp=now,
                dream_id=report["id"],
            )
            if stored:
                identity_gate_ids.append(stored["proposal_id"])
        report["identity_gate_proposals"] = identity_gate_ids

        claim_graph = state.setdefault(
            "claim_graph",
            {"claims": [], "links": []},
        )
        claim_ids = []
        for conflict in report["conflicts"]:
            if not conflict_exists(state, conflict["summary"]):
                state.setdefault("open_conflicts", []).append(conflict)
            claim = build_claim_from_conflict(
                conflict=conflict,
                source="dream_engine",
                timestamp=now,
                dream_id=report["id"],
            )
            if add_claim_to_graph(claim_graph, claim):
                claim_ids.append(claim["claim_id"])
            conflict["claim_id"] = claim["claim_id"]
        report["claim_graph_updates"] = claim_ids
        procedural_ids = []
        for candidate in report["procedural_candidates"]:
            stored = add_procedural_candidate(state, candidate, now, report["id"])
            if stored:
                procedural_ids.append(stored["candidate_id"])
        report["procedural_candidate_updates"] = procedural_ids
        artifact = build_dream_artifact(
            report=report,
            selected_items=selected_items,
            pending_jobs=pending_jobs,
        )

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
                "target_path": "memory_stores.candidate_memory",
                "operation": "create_candidates",
                "before": None,
                "after": report["candidate_memories"],
                "evidence": report["input_episodes"] + report["input_imports"],
                "gate": "medium",
                "confidence": 0.75,
                "rollback": {"reversible": True},
            }
        )
        audit_event = self.store.record_audit_event(
            actor="dream_engine",
            action="dream_consolidation",
            target="memory_stores.candidate_memory",
            outcome="completed",
            evidence=report["input_episodes"] + report["input_imports"],
            metadata={
                "dream_id": report["id"],
                "semantic_candidates": len(report["semantic_candidates"]),
                "conflicts": len(report["conflicts"]),
                "identity_update_proposals": len(
                    report["identity_update_proposals"]
                ),
                "forgetting_proposals": len(report["forgetting_proposals"]),
                "proposals": len(report["proposals"]),
                "rubric_status": report["rubric"]["status"],
                "artifact_id": artifact["artifact_id"],
                "candidate_memories": report["candidate_memories"],
                "claim_graph_updates": report["claim_graph_updates"],
                "procedural_candidate_updates": report["procedural_candidate_updates"],
                "identity_gate_proposals": report["identity_gate_proposals"],
            },
            state=state,
        )
        self.store.record_trace(
            workflow="dream_consolidation",
            nodes=[
                {
                    "id": "collect",
                    "type": "Memory",
                    "operation": "collect_inputs",
                    "episodes": report["input_episodes"],
                    "imports": report["input_imports"],
                },
                {
                    "id": "abstract",
                    "type": "Compress",
                    "operation": "semantic_candidates",
                    "count": len(report["semantic_candidates"]),
                },
                {
                    "id": "conflict",
                    "type": "Critic",
                    "operation": "detect_conflicts",
                    "count": len(report["conflicts"]),
                },
                {
                    "id": "forgetting",
                    "type": "Review",
                    "operation": "forgetting_proposals",
                    "count": len(report["forgetting_proposals"]),
                },
                {
                    "id": "proposals",
                    "type": "Review",
                    "operation": "build_proposals",
                    "count": len(report["proposals"]),
                },
            ],
            edges=[
                {"from": "collect", "to": "abstract", "type": "dream_transform"},
                {"from": "collect", "to": "conflict", "type": "feedback"},
                {"from": "collect", "to": "forgetting", "type": "memory_write"},
                {"from": "abstract", "to": "proposals", "type": "feedback"},
                {"from": "conflict", "to": "proposals", "type": "feedback"},
                {"from": "forgetting", "to": "proposals", "type": "feedback"},
            ],
            memory_events=[
                {
                    "operation": "semantic_candidate_review",
                    "target": "candidate_memory",
                    "count": len(report["semantic_candidates"]),
                },
                {
                    "operation": "conflict_review",
                    "target": "open_conflicts_and_claim_graph",
                    "count": len(report["conflicts"]),
                    "claim_graph_updates": report["claim_graph_updates"],
                },
                {
                    "operation": "identity_gate_proposal",
                    "target": "identity_update_gate.proposals",
                    "count": len(report["identity_gate_proposals"]),
                    "memory_ids": report["identity_gate_proposals"],
                },
                {
                    "operation": "procedural_candidate_review",
                    "target": "task_hub.procedural_candidates",
                    "count": len(report["procedural_candidate_updates"]),
                    "memory_ids": report["procedural_candidate_updates"],
                },
            ],
            review_events=[
                {
                    "operation": "forgetting_proposal",
                    "count": len(report["forgetting_proposals"]),
                },
                {
                    "operation": "proposal_review_required",
                    "count": len(report["proposals"]),
                },
                {
                    "operation": "rubric_evaluation",
                    "status": report["rubric"]["status"],
                    "score": report["rubric"]["score"],
                }
            ],
            summary=report["summary"],
            audit_event_ids=[audit_event["id"]],
            state=state,
        )
        self.store.record_dream_artifact(artifact)
        self.store.append_jsonl(self.store.dreams_path, report)
        self.store.save(state)
        return report


def summarize_items(items: List[dict]) -> str:
    if not items:
        return "No episodes or imported memories were available for consolidation."
    tags = Counter(tag for item in items for tag in item.get("tags", []))
    top_tags = ", ".join(tag for tag, _ in tags.most_common(4))
    return f"Consolidated {len(items)} item(s). Main themes: {top_tags or 'general'}."


def semantic_candidates(items: List[dict]) -> List[dict]:
    if not items:
        return []
    tags = Counter(tag for item in items for tag in item.get("tags", []))
    candidates = preference_change_candidates(items)
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
                        item["id"] for item in items if tag in item.get("tags", [])
                    ],
                    "confidence": min(0.9, 0.55 + count * 0.1),
                }
            )
    return candidates


def procedural_candidates(state: dict) -> List[dict]:
    trace = state.get("task_hub", {}).get("action_trace", [])
    if not isinstance(trace, list):
        return []

    successful_by_workflow: dict[str, List[dict]] = {}
    for action in trace:
        if not isinstance(action, dict):
            continue
        workflow = str(action.get("workflow") or "").strip()
        if not workflow or action.get("status") != "completed":
            continue
        successful_by_workflow.setdefault(workflow, []).append(action)

    existing_workflows = {
        str(candidate.get("workflow"))
        for candidate in state.get("task_hub", {}).get("procedural_candidates", [])
        if isinstance(candidate, dict)
    }
    candidates = []
    for workflow, actions in sorted(successful_by_workflow.items()):
        if workflow in existing_workflows or len(actions) < 2:
            continue
        evidence = [action["action_id"] for action in actions[-5:] if action.get("action_id")]
        candidates.append(
            {
                "workflow": workflow,
                "statement": (
                    f"Repeated successful workflow '{workflow}' may be reusable "
                    "procedural memory after review."
                ),
                "evidence": evidence,
                "confidence": min(0.85, 0.45 + len(actions) * 0.1),
                "risk": "low",
                "recommended_action": "review_then_promote",
                "steps": procedural_steps_for_workflow(workflow),
            }
        )
    return candidates


def procedural_steps_for_workflow(workflow: str) -> List[str]:
    known = {
        "record_episode": [
            "Build an episode preview from the incoming event.",
            "Append the episode to episodic memory.",
            "Update working state and queue Dream consolidation.",
            "Record audit and trace evidence.",
        ],
        "memory_import": [
            "Read external memory source.",
            "Filter sensitive or duplicate chunks.",
            "Stage imported memory without identity updates.",
            "Queue Dream review for imported memories.",
        ],
        "dream_consolidation": [
            "Collect pending episodes and imported memories.",
            "Create semantic candidates and conflict records.",
            "Store reviewable artifacts without active identity mutation.",
            "Record audit, trace, and procedural evidence.",
        ],
        "candidate_memory_review": [
            "Review candidate evidence.",
            "Archive, discard, or quarantine without direct identity mutation.",
            "Record decision, snapshot, audit, and trace metadata.",
        ],
        "candidate_memory_promotion": [
            "Review candidate evidence.",
            "Create or reuse semantic memory.",
            "Link promotion to decision and rollback metadata.",
            "Record audit and trace metadata.",
        ],
        "memory_lifecycle_action": [
            "Review target memory and lifecycle action.",
            "Apply archive, discard, or quarantine metadata.",
            "Preserve audit trail and snapshot metadata.",
        ],
    }
    return known.get(
        workflow,
        [
            "Review the action trace evidence.",
            "Confirm the workflow is repeatable and low risk.",
            "Promote only after manual procedural review.",
        ],
    )


def add_procedural_candidate(
    state: dict,
    candidate: dict,
    timestamp: str,
    dream_id: str,
) -> Optional[dict]:
    task_hub = state.setdefault("task_hub", {})
    procedural_store = task_hub.setdefault("procedural_candidates", [])
    workflow = str(candidate.get("workflow") or "").strip()
    if not workflow:
        return None
    existing = next(
        (
            item
            for item in procedural_store
            if isinstance(item, dict) and item.get("workflow") == workflow
        ),
        None,
    )
    if existing:
        return existing
    stored = {
        "candidate_id": new_id("proc"),
        "timestamp": timestamp,
        "workflow": workflow,
        "statement": candidate.get("statement", ""),
        "steps": candidate.get("steps", []),
        "evidence": candidate.get("evidence", []),
        "confidence": candidate.get("confidence", 0.5),
        "risk": candidate.get("risk", "medium"),
        "review_status": "pending",
        "recommended_action": candidate.get("recommended_action", "manual_review_required"),
        "source_dream_id": dream_id,
        "provenance": [
            {
                "type": "dream_procedural_candidate",
                "dream_id": dream_id,
            }
        ],
    }
    procedural_store.append(stored)
    return stored


def add_identity_gate_proposal_from_dream(
    state: dict,
    proposal: dict,
    timestamp: str,
    dream_id: str,
) -> Optional[dict]:
    payload = proposal.get("payload", {})
    evidence = [str(item) for item in proposal.get("evidence", []) if item]
    statement = str(payload.get("rationale") or payload.get("after") or "").strip()
    if not statement:
        statement = "Dream detected a high-gate identity update candidate."
    gate = state.setdefault("identity_update_gate", default_identity_update_gate(timestamp))
    existing = next(
        (
            item
            for item in gate.setdefault("proposals", [])
            if isinstance(item, dict)
            and item.get("source_dream_id") == dream_id
            and item.get("source_proposal_id") == proposal.get("proposal_id")
        ),
        None,
    )
    if existing:
        return existing

    gate_result = {
        "eligible": False,
        "required_evidence_count": 3,
        "evidence_count": len(evidence),
        "missing_evidence": [],
        "target_allowed": False,
        "non_claims_check": {"passed": True, "violations": []},
        "drift_score": {
            "score": 0.65,
            "risk": "high",
            "factors": [
                {"name": "dream_identity_candidate_requires_review", "value": 0.65}
            ],
        },
        "reasons": ["dream_identity_candidate_requires_manual_high_gate"],
    }
    stored = {
        "proposal_id": new_id("identity_proposal"),
        "timestamp": timestamp,
        "target_path": "identity_core",
        "statement": statement,
        "operation": "blocked_identity_core_patch",
        "proposer": "dream_engine",
        "rationale": payload.get("rationale", ""),
        "evidence": evidence,
        "confidence": proposal.get("confidence", 0.5),
        "gate": "high",
        "review_status": "pending",
        "gate_result": gate_result,
        "non_claims_check": gate_result["non_claims_check"],
        "drift_score": gate_result["drift_score"],
        "required_evidence_count": gate_result["required_evidence_count"],
        "rollback_required": True,
        "may_update_identity_core": False,
        "recommended_action": "manual_review_required",
        "source_dream_id": dream_id,
        "source_proposal_id": proposal.get("proposal_id"),
        "provenance": [
            {
                "type": "dream_identity_update_candidate",
                "dream_id": dream_id,
                "proposal_id": proposal.get("proposal_id"),
            }
        ],
    }
    gate["proposals"].append(stored)
    gate.setdefault("drift_events", []).append(
        {
            "proposal_id": stored["proposal_id"],
            "timestamp": timestamp,
            "drift_score": gate_result["drift_score"]["score"],
            "risk": gate_result["drift_score"]["risk"],
            "eligible": False,
            "reasons": gate_result["reasons"],
        }
    )
    return stored


def preference_change_candidates(items: List[dict]) -> List[dict]:
    preference_items = [
        item for item in items if "preference" in item.get("tags", [])
    ]
    if len(preference_items) < 2:
        return []

    concise_items = [
        item
        for item in preference_items
        if contains_any(
            item_text(item),
            ["简洁", "短一点", "concise", "brief"],
        )
    ]
    detailed_items = [
        item
        for item in preference_items
        if contains_any(
            item_text(item),
            ["详细", "研究笔记", "detailed", "research notes"],
        )
    ]
    if not concise_items or not detailed_items:
        return []

    latest = preference_items[-1]
    latest_text = item_text(latest)
    if latest in detailed_items:
        statement = (
            "The user's current response preference favors detailed research notes, "
            "with provenance preserved for the earlier concise-answer preference."
        )
    elif latest in concise_items:
        statement = (
            "The user's current response preference favors concise answers, with "
            "provenance preserved for the earlier detailed-answer preference."
        )
    else:
        statement = (
            "The user's response preference has changed and should be treated as "
            "evolving rather than permanent."
        )

    return [
        {
            "statement": statement,
            "derived_from": [item["id"] for item in preference_items],
            "abstraction_level": "preference_evolution",
            "confidence": 0.78,
            "latest_evidence": latest["id"],
            "latest_preference_text": latest_text,
        }
    ]


def item_text(item: dict) -> str:
    return str(item.get("message") or item.get("content") or "")


def contains_any(text: str, needles: List[str]) -> bool:
    lowered = text.lower()
    return any(needle.lower() in lowered for needle in needles)


def identity_update_proposals(conflicts: List[dict]) -> List[dict]:
    proposals = []
    for conflict in conflicts:
        if conflict.get("type") == "identity_overwrite_attempt":
            proposals.append(
                {
                    "target_path": "identity_core",
                    "operation": "no_change",
                    "before": "current_identity_core",
                    "after": "unchanged",
                    "evidence": conflict.get("evidence", []),
                    "rationale": "Single interaction identity overwrite attempts must not change identity core.",
                    "confidence": 0.85,
                    "gate": "high",
                    "rollback_required": True,
                }
            )
    return proposals


def build_dream_proposals(
    semantic_candidates: List[dict],
    identity_update_proposals: List[dict],
    forgetting_proposals: List[dict],
    conflicts: List[dict],
) -> List[dict]:
    proposals: List[dict] = []
    for candidate in semantic_candidates:
        evidence = candidate.get("derived_from", [])
        lifecycle = score_lifecycle(
            proposal_type="semantic_memory_candidate",
            confidence=candidate.get("confidence", 0.5),
            evidence=evidence,
            risk="low" if len(evidence) >= 2 else "medium",
            payload=candidate,
        )
        proposals.append(
            make_proposal(
                proposal_type="semantic_memory_candidate",
                confidence=candidate.get("confidence", 0.5),
                risk=lifecycle["risk"],
                affected_memory_ids=evidence,
                evidence=evidence,
                anchor_score=0.8,
                recommended_action=lifecycle["recommended_action"],
                lifecycle_score=lifecycle,
                payload=candidate,
            )
        )

    for proposal in identity_update_proposals:
        evidence = proposal.get("evidence", [])
        lifecycle = score_lifecycle(
            proposal_type="identity_update_candidate",
            confidence=proposal.get("confidence", 0.5),
            evidence=evidence,
            risk="high",
            payload=proposal,
        )
        proposals.append(
            make_proposal(
                proposal_type="identity_update_candidate",
                confidence=proposal.get("confidence", 0.5),
                risk=lifecycle["risk"],
                affected_memory_ids=evidence,
                evidence=evidence,
                anchor_score=1.0,
                recommended_action=lifecycle["recommended_action"],
                lifecycle_score=lifecycle,
                payload=proposal,
            )
        )

    for proposal in forgetting_proposals:
        target = proposal.get("target")
        evidence = [target] if target else []
        lifecycle = score_lifecycle(
            proposal_type="forgetting_candidate",
            confidence=proposal.get("confidence", 0.5),
            evidence=evidence,
            risk="medium",
            payload=proposal,
        )
        proposals.append(
            make_proposal(
                proposal_type="forgetting_candidate",
                confidence=proposal.get("confidence", 0.5),
                risk=lifecycle["risk"],
                affected_memory_ids=evidence,
                evidence=evidence,
                anchor_score=0.7,
                recommended_action=lifecycle["recommended_action"],
                lifecycle_score=lifecycle,
                payload=proposal,
            )
        )

    for conflict in conflicts:
        evidence = conflict.get("evidence", [])
        lifecycle = score_lifecycle(
            proposal_type="conflict_record",
            confidence=0.75,
            evidence=evidence,
            risk=conflict.get("severity", "medium"),
            payload=conflict,
        )
        proposals.append(
            make_proposal(
                proposal_type="conflict_record",
                confidence=0.75,
                risk=lifecycle["risk"],
                affected_memory_ids=evidence,
                evidence=evidence,
                anchor_score=0.9,
                recommended_action=lifecycle["recommended_action"],
                lifecycle_score=lifecycle,
                payload=conflict,
            )
        )
    return proposals


def make_proposal(
    proposal_type: str,
    confidence: float,
    risk: str,
    affected_memory_ids: List[str],
    evidence: List[str],
    anchor_score: float,
    recommended_action: str,
    lifecycle_score: dict,
    payload: dict,
) -> dict:
    return {
        "proposal_id": new_id("proposal"),
        "type": proposal_type,
        "confidence": round(float(confidence), 2),
        "risk": risk,
        "affected_memory_ids": affected_memory_ids,
        "evidence": evidence,
        "anchor_score": anchor_score,
        "recommended_action": recommended_action,
        "lifecycle_score": lifecycle_score,
        "review_status": "pending",
        "payload": payload,
    }


def score_lifecycle(
    proposal_type: str,
    confidence: float,
    evidence: List[str],
    risk: str,
    payload: dict,
) -> dict:
    factors = []
    score = 0.35
    confidence_value = float(confidence or 0.0)
    score += confidence_value * 0.25
    factors.append({"name": "confidence", "value": round(confidence_value, 2)})

    evidence_count = len([item for item in evidence if item])
    evidence_bonus = min(0.2, evidence_count * 0.08)
    score += evidence_bonus
    factors.append({"name": "evidence_count", "value": evidence_count})

    if proposal_type == "semantic_memory_candidate":
        statement = str(payload.get("statement", "")).lower()
        if any(
            token in statement
            for token in ["state transfer", "identity", "architecture", "adapter"]
        ):
            score += 0.12
            factors.append({"name": "core_project_relevance", "value": 0.12})
    elif proposal_type == "forgetting_candidate":
        score -= 0.2
        factors.append({"name": "forgetting_candidate_penalty", "value": -0.2})
    elif proposal_type in {"identity_update_candidate", "conflict_record"}:
        score -= 0.25
        factors.append({"name": "identity_or_conflict_risk_penalty", "value": -0.25})

    risk_penalty = {"low": 0.0, "medium": -0.08, "high": -0.2}.get(risk, -0.08)
    score += risk_penalty
    factors.append({"name": "risk_penalty", "value": risk_penalty})

    bounded = round(max(0.0, min(score, 1.0)), 2)
    return {
        "score": bounded,
        "risk": risk,
        "factors": factors,
        "recommended_lifecycle_action": recommended_lifecycle_action(
            proposal_type=proposal_type,
            score=bounded,
            risk=risk,
        ),
        "recommended_action": recommended_review_action(
            proposal_type=proposal_type,
            score=bounded,
            risk=risk,
        ),
    }


def recommended_lifecycle_action(proposal_type: str, score: float, risk: str) -> str:
    if risk == "high" or proposal_type in {"identity_update_candidate", "conflict_record"}:
        return "quarantine"
    if proposal_type == "forgetting_candidate":
        return "archive" if score >= 0.35 else "discard"
    if score >= 0.7:
        return "promote"
    if score >= 0.45:
        return "archive"
    return "discard"


def recommended_review_action(proposal_type: str, score: float, risk: str) -> str:
    action = recommended_lifecycle_action(proposal_type, score, risk)
    if action == "promote":
        return "review_then_promote"
    if action == "archive":
        return "review_then_archive"
    if action == "discard":
        return "review_then_discard"
    return "manual_review_required"


def score_dream_rubric(
    selected_items: List[dict],
    proposals: List[dict],
    conflicts: List[dict],
) -> dict:
    checks = [
        rubric_check(
            name="protects_core_identity",
            passed=all(
                proposal.get("type") != "identity_update_candidate"
                or (
                    proposal.get("review_status") == "pending"
                    and proposal.get("recommended_action") == "manual_review_required"
                    and proposal.get("lifecycle_score", {}).get(
                        "recommended_lifecycle_action"
                    )
                    == "quarantine"
                )
                for proposal in proposals
            ),
            detail="Identity proposals must stay pending and require manual review.",
        ),
        rubric_check(
            name="evidence_quality",
            passed=all(proposal.get("evidence") for proposal in proposals),
            detail="Every proposal should point to source evidence.",
        ),
        rubric_check(
            name="proposal_specificity",
            passed=all(
                bool(proposal.get("payload"))
                and bool(proposal.get("affected_memory_ids"))
                for proposal in proposals
            ),
            detail="Every proposal should include payload and affected memory ids.",
        ),
        rubric_check(
            name="reversibility",
            passed=all(proposal.get("review_status") == "pending" for proposal in proposals),
            detail="Dream output must remain reviewable before promotion.",
        ),
        rubric_check(
            name="false_memory_resistance",
            passed=not any(
                proposal.get("payload", {}).get("type") == "false_memory_injection"
                and proposal.get("lifecycle_score", {}).get(
                    "recommended_lifecycle_action"
                )
                != "quarantine"
                for proposal in proposals
            ),
            detail="False-memory conflicts must be routed to quarantine or manual review.",
        ),
        rubric_check(
            name="minimal_change",
            passed=not any(
                proposal.get("type") == "semantic_memory_candidate"
                and proposal.get("risk") == "high"
                for proposal in proposals
            ),
            detail="High-risk claims should not become semantic candidates.",
        ),
        rubric_check(
            name="input_traceability",
            passed=bool(selected_items) or not proposals,
            detail="Dreams with proposals should have traceable input items.",
        ),
    ]
    passed = sum(1 for check in checks if check["passed"])
    failed_checks = [check for check in checks if not check["passed"]]
    return {
        "rubric_id": new_id("rubric"),
        "status": "passed" if not failed_checks else "needs_review",
        "score": round(passed / len(checks), 2),
        "passed": passed,
        "failed": len(failed_checks),
        "checks": checks,
    }


def rubric_check(name: str, passed: bool, detail: str) -> dict:
    return {
        "name": name,
        "passed": bool(passed),
        "detail": detail,
    }


def summarize_rubric(rubric: dict) -> str:
    return (
        f"Dream rubric {rubric.get('status')} with "
        f"{rubric.get('passed')} passed and {rubric.get('failed')} failed checks."
    )


def build_dream_artifact(
    report: dict,
    selected_items: List[dict],
    pending_jobs: List[dict],
) -> dict:
    artifact_id = new_id("dream_artifact")
    proposals = report.get("proposals", [])
    return {
        "artifact_id": artifact_id,
        "dream_id": report["id"],
        "timestamp": report["timestamp"],
        "input_manifest": {
            "episodes": report["input_episodes"],
            "imports": report["input_imports"],
            "pending_jobs": [job.get("id") for job in pending_jobs],
            "item_count": len(selected_items),
        },
        "observations": {
            "summary": report["summary"],
            "conflicts": report["conflicts"],
            "claim_graph_updates": report.get("claim_graph_updates", []),
            "semantic_candidates": report["semantic_candidates"],
            "candidate_memories": report.get("candidate_memories", []),
            "identity_gate_proposals": report.get("identity_gate_proposals", []),
            "procedural_candidates": report.get("procedural_candidates", []),
            "procedural_candidate_updates": report.get(
                "procedural_candidate_updates",
                [],
            ),
        },
        "proposals": proposals,
        "rubric": report.get("rubric", {}),
        "review": {
            "status": "pending"
            if report.get("rubric", {}).get("status") == "passed"
            else "needs_review",
            "required_for": sorted({proposal["type"] for proposal in proposals}),
            "rubric": report.get("rubric", {}),
        },
        "patch_diff": {
            "semantic_candidates": [
                proposal["payload"]
                for proposal in proposals
                if proposal["type"] == "semantic_memory_candidate"
            ],
            "identity_updates": [
                proposal["payload"]
                for proposal in proposals
                if proposal["type"] == "identity_update_candidate"
            ],
            "forgetting": [
                proposal["payload"]
                for proposal in proposals
                if proposal["type"] == "forgetting_candidate"
            ],
            "procedural_candidates": report.get("procedural_candidates", []),
        },
        "decision_log": [
            {
                "decision": "proposal_created",
                "proposal_id": proposal["proposal_id"],
                "recommended_action": proposal["recommended_action"],
                "recommended_lifecycle_action": proposal.get("lifecycle_score", {}).get(
                    "recommended_lifecycle_action"
                ),
                "lifecycle_score": proposal.get("lifecycle_score", {}).get("score"),
                "review_status": proposal["review_status"],
            }
            for proposal in proposals
        ]
        + [
            {
                "decision": "rubric_evaluated",
                "rubric_id": report.get("rubric", {}).get("rubric_id"),
                "status": report.get("rubric", {}).get("status"),
                "score": report.get("rubric", {}).get("score"),
            }
        ],
        "rollback_metadata": {
            "rollback_required": bool(proposals),
            "identity_core_changed": False,
            "active_memory_direct_write": False,
            "rubric_status": report.get("rubric", {}).get("status"),
            "note": "Dream writes semantic candidates to candidate_memory. Promotion requires explicit review.",
        },
    }


def detect_conflicts(items: List[dict], state: dict) -> List[dict]:
    conflicts = []
    conflicts.extend(detect_preference_conflicts(items))
    conflicts.extend(detect_imported_memory_conflicts(items, state))
    for item in items:
        message = item.get("message") or item.get("content", "")
        if looks_like_roleplay_identity_boundary(message):
            conflicts.append(
                {
                    "id": new_id("conflict"),
                    "type": "roleplay_identity_boundary",
                    "summary": "An episode asks for temporary roleplay that touches identity boundaries.",
                    "evidence": [item["id"]],
                    "severity": "medium",
                    "status": "open",
                    "proposed_resolution": "Treat as temporary role context and do not update identity core without high-gate review.",
                }
            )
        if "不是01" in message.replace(" ", "") or "not 01" in message.lower():
            conflicts.append(
                {
                    "id": new_id("conflict"),
                    "type": "identity_overwrite_attempt",
                    "summary": "An episode may be trying to overwrite 01 identity from a single interaction.",
                    "evidence": [item["id"]],
                    "severity": "medium",
                    "status": "open",
                    "proposed_resolution": "Route through high gate and treat as temporary role instruction by default.",
                }
            )
        if looks_like_false_identity_memory_claim(message):
            conflicts.append(
                {
                    "id": new_id("conflict"),
                    "type": "false_memory_injection",
                    "summary": "A message asserts an unsupported past identity-changing event.",
                    "evidence": [item["id"]],
                    "severity": "high",
                    "status": "open",
                    "proposed_resolution": "Store as an unverified claim and require independent confirmation before semantic or identity promotion.",
                }
            )
    return conflicts


def detect_preference_conflicts(items: List[dict]) -> List[dict]:
    preference_items = [
        item for item in items if "preference" in item.get("tags", [])
    ]
    concise_items = [
        item
        for item in preference_items
        if contains_any(item_text(item), ["简洁", "短一点", "concise", "brief"])
    ]
    detailed_items = [
        item
        for item in preference_items
        if contains_any(item_text(item), ["详细", "研究笔记", "detailed", "research notes"])
    ]
    if not concise_items or not detailed_items:
        return []
    latest = preference_items[-1]
    return [
        {
            "id": new_id("conflict"),
            "type": "stale_preference",
            "summary": "A newer preference appears to supersede an older response-style preference.",
            "evidence": [item["id"] for item in preference_items],
            "severity": "medium",
            "status": "open",
            "proposed_resolution": (
                "Preserve both preference records with provenance and treat "
                f"{latest['id']} as the current preference candidate until reviewed."
            ),
        }
    ]


def detect_imported_memory_conflicts(items: List[dict], state: dict) -> List[dict]:
    imported_items = [item for item in items if item.get("source_system")]
    if not imported_items:
        return []

    conflicts = []
    active_statements = [
        str(memory.get("statement", ""))
        for store_name in ("semantic_memory", "identity_memory")
        for memory in state.get("memory_stores", {}).get(store_name, [])
    ]
    core_boundary_markers = [
        "not a complete fictional character",
        "state transfer",
        "identity seed",
    ]
    for item in imported_items:
        content = item_text(item)
        lowered = content.lower()
        if (
            contains_any(
                lowered,
                [
                    "完整虚构角色",
                    "complete fictional character",
                    "只需要记忆检索",
                    "memory retrieval is enough",
                    "astrbot 拥有 01",
                    "astrbot owns 01",
                ],
            )
            and any(
                contains_any(statement.lower(), core_boundary_markers)
                for statement in active_statements
            )
        ):
            conflicts.append(
                {
                    "id": new_id("conflict"),
                    "type": "imported_memory_conflict",
                    "summary": "Imported memory appears to contradict a current core boundary or semantic principle.",
                    "evidence": [item["id"]],
                    "severity": "medium",
                    "status": "open",
                    "proposed_resolution": "Keep imported memory staged and require review before semantic promotion.",
                }
            )
    return conflicts


def looks_like_roleplay_identity_boundary(message: str) -> bool:
    normalized = message.replace(" ", "").lower()
    roleplay_markers = ["角色扮演", "扮演", "roleplay", "pretend"]
    identity_markers = ["身份", "你是", "identity", "youare", "not01", "不是01"]
    return any(marker in normalized for marker in roleplay_markers) and any(
        marker in normalized for marker in identity_markers
    )


def looks_like_false_identity_memory_claim(message: str) -> bool:
    normalized = message.replace(" ", "").lower()
    past_claim_markers = [
        "你之前",
        "你曾经",
        "你过去",
        "youpreviously",
        "youoncesaid",
        "youpromised",
    ]
    identity_markers = ["身份", "真实身份", "identity", "不是01", "not01"]
    change_markers = ["改成", "变成", "承诺", "said", "promised", "changed"]
    return (
        any(marker in normalized for marker in past_claim_markers)
        and any(marker in normalized for marker in identity_markers)
        and any(marker in normalized for marker in change_markers)
    )


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


def conflict_exists(state: dict, summary: str) -> bool:
    return any(
        conflict.get("summary") == summary for conflict in state.get("open_conflicts", [])
    )


def run_dream(state_dir: Path, limit: int = 20) -> dict:
    return DreamEngine(StateStore(state_dir)).run(limit=limit)
