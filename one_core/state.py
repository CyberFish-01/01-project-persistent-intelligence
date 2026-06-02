from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .seed import make_identity_seed


STATE_VERSION = "0.1"
DEFAULT_STATE_DIR = Path("work/01_state")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def new_id(prefix: str) -> str:
    return f"{prefix}_{uuid.uuid4().hex[:12]}"


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

    def exists(self) -> bool:
        return self.state_path.exists()

    def init(self, force: bool = False) -> dict:
        if self.exists() and not force:
            return self.load()

        now = utc_now()
        state = {
            "state_version": STATE_VERSION,
            "agent_id": "01",
            "created_at": now,
            "updated_at": now,
            "identity_core": make_identity_seed(),
            "working_state": {
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
            },
            "memory_stores": {
                "imported_memory": [],
                "episodic_memory": [],
                "semantic_memory": [
                    {
                        "id": new_id("sem"),
                        "statement": "Continuity requires state transfer, not only memory retrieval.",
                        "derived_from": ["identity_seed"],
                        "abstraction_level": "principle",
                        "confidence": 0.9,
                        "last_verified_at": now,
                        "contradiction_refs": [],
                        "update_policy": {"required_gate": "medium"},
                    }
                ],
                "identity_memory": [
                    {
                        "id": new_id("idmem"),
                        "statement": "01 is an identity seed, not a complete fictional character.",
                        "derived_from": ["identity_seed"],
                        "confidence": 0.9,
                        "required_gate": "high",
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
            "open_conflicts": [],
            "dream_queue": [],
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
        return state

    def load(self) -> dict:
        if not self.exists():
            return self.init()
        return read_json(self.state_path)

    def save(self, state: dict) -> None:
        state["updated_at"] = utc_now()
        write_json(self.state_path, state)

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
                "channel": channel,
                "source": source,
                "sensitivity": sensitivity,
            }
        )
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
        semantic = state["memory_stores"].get("semantic_memory", [])[-5:]
        episodic = state["memory_stores"].get("episodic_memory", [])[-5:]
        return {
            "identity_summary": state["identity_core"]["self_model"]["summary"],
            "active_intent": state["working_state"]["active_intent"],
            "continuity_anchors": state["working_state"]["context_anchors"],
            "imported_memories": state["memory_stores"].get("imported_memory", [])[-5:],
            "recent_episodes": episodic,
            "relevant_semantic_memories": semantic,
            "open_conflicts": state.get("open_conflicts", []),
            "current_constraints": state["identity_core"].get("identity_constraints", []),
        }


def infer_tags(message: str) -> List[str]:
    lowered = message.lower()
    tags = []
    rules = {
        "identity": ["身份", "identity", "我是谁", "self"],
        "dream_engine": ["dream", "梦", "反思", "整理"],
        "state_transfer": ["state", "状态", "连续", "迁移", "persist"],
        "memory": ["memory", "记忆", "回忆"],
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
