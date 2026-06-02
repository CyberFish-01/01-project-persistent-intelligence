from __future__ import annotations

import json
import re
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .seed import make_identity_seed


STATE_VERSION = "0.3"
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
            "adapter_registry": default_adapter_registry(now),
            "adapter_event_index": {},
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
