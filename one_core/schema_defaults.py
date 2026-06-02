from __future__ import annotations


def default_identity_update_gate(timestamp: str) -> dict:
    return {
        "gate_version": "0.9",
        "required_gate": "high",
        "min_supporting_evidence": 3,
        "allow_identity_core_patch": False,
        "proposals": [],
        "review_decisions": [],
        "drift_events": [],
        "policy": {
            "non_claims_check_required": True,
            "drift_threshold": 0.35,
            "approved_target": "memory_stores.identity_memory",
            "identity_core_update_mode": "blocked_in_v0.9",
            "created_at": timestamp,
        },
    }
