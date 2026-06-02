from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


class OneCoreClientError(RuntimeError):
    pass


@dataclass(frozen=True)
class AdapterEvent:
    message: str
    user_id: str = "adapter_user"
    channel: str = "generic_adapter"
    session_id: str | None = None

    def to_payload(self) -> dict[str, Any]:
        payload: dict[str, Any] = {
            "message": self.message,
            "user_id": self.user_id,
            "channel": self.channel,
        }
        if self.session_id:
            payload["session_id"] = self.session_id
        return payload


class OneCoreClient:
    def __init__(self, api_base_url: str = "http://127.0.0.1:8765", timeout: float = 10):
        self.api_base_url = api_base_url.rstrip("/")
        self.timeout = timeout

    def health(self) -> dict[str, Any]:
        return self._request("GET", "/health")

    def status(self) -> dict[str, Any]:
        return self._request("GET", "/v1/status")

    def context(self) -> dict[str, Any]:
        return self._request("GET", "/v1/context")

    def interact(self, event: AdapterEvent) -> dict[str, Any]:
        return self._request("POST", "/v1/interact", event.to_payload())

    def dream(self, limit: int = 20) -> dict[str, Any]:
        return self._request("POST", "/v1/dream", {"limit": limit})

    def _request(
        self, method: str, path: str, payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        data = None
        headers = {"Accept": "application/json"}
        if payload is not None:
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json; charset=utf-8"

        request = urllib.request.Request(
            f"{self.api_base_url}{path}",
            data=data,
            headers=headers,
            method=method,
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                raw = response.read().decode("utf-8")
        except urllib.error.URLError as exc:
            raise OneCoreClientError(
                f"Could not reach 01 Core API at {self.api_base_url}: {exc}"
            ) from exc

        try:
            parsed = json.loads(raw)
        except json.JSONDecodeError as exc:
            raise OneCoreClientError("01 Core API returned invalid JSON.") from exc
        if not isinstance(parsed, dict):
            raise OneCoreClientError("01 Core API returned a non-object JSON payload.")
        return parsed


def format_status(status: dict[str, Any]) -> str:
    return (
        "01 Core 状态\n"
        f"- 人格编号：{status.get('agent_id', 'unknown')}\n"
        f"- 身份：{status.get('identity', 'unknown')}\n"
        f"- 当前目标：{status.get('active_intent', {}).get('goal', 'unknown')}\n"
        f"- 导入记忆：{status.get('imported_memories', 0)}\n"
        f"- 事件记忆：{status.get('episodes', 0)}\n"
        f"- 语义记忆：{status.get('semantic_memories', 0)}\n"
        f"- 开放冲突：{status.get('open_conflicts', 0)}\n"
        f"- 待做梦任务：{status.get('pending_dream_jobs', 0)}"
    )


def format_context(context: dict[str, Any]) -> str:
    anchors = context.get("continuity_anchors", {})
    active_intent = context.get("active_intent", {})
    return (
        "01 Core 上下文包\n"
        f"- 我是谁：{anchors.get('who_am_i', 'unknown')}\n"
        f"- 我在哪：{anchors.get('where_am_i', 'unknown')}\n"
        f"- 我在做什么：{active_intent.get('goal', 'unknown')}\n"
        f"- 最近经历：{len(context.get('recent_episodes', []))}\n"
        f"- 语义记忆：{len(context.get('relevant_semantic_memories', []))}\n"
        f"- 导入记忆：{len(context.get('imported_memories', []))}\n"
        f"- 开放冲突：{len(context.get('open_conflicts', []))}"
    )
