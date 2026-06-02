from __future__ import annotations

import asyncio
import json
import urllib.error
import urllib.request
from typing import Any

from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register


@register(
    "astrbot_plugin_01_core",
    "CyberFish-01",
    "01 Core adapter for AstrBot. AstrBot is the entrance; 01 Core owns continuity state.",
    "0.1.0",
    "https://github.com/CyberFish-01/01-project-persistent-intelligence",
)
class OneCoreAstrBotAdapter(Star):
    def __init__(self, context: Context, config: dict | None = None):
        super().__init__(context)
        self.config = config or {}
        self.api_base_url = str(
            self.config.get("api_base_url", "http://127.0.0.1:8765")
            or "http://127.0.0.1:8765"
        ).rstrip("/")
        self.timeout_seconds = float(self.config.get("timeout_seconds", 10) or 10)
        self.default_user_id = str(self.config.get("default_user_id", "astrbot_user"))
        self.channel_label = str(self.config.get("channel_label", "astrbot"))
        logger.info("01 Core AstrBot adapter loaded.")

    @filter.command_group("01")
    def one(self):
        """01 Core commands."""
        pass

    @one.command("ping")
    async def ping(self, event: AstrMessageEvent):
        """Check 01 Core API health."""
        try:
            result = await self._request("GET", "/health")
        except Exception as exc:
            yield event.plain_result(self._format_error(exc))
            return

        yield event.plain_result(
            "01 Core API 在线\n"
            f"- 状态：{result.get('status', 'unknown')}\n"
            f"- 人格编号：{result.get('agent_id', 'unknown')}"
        )

    @one.command("status")
    async def status(self, event: AstrMessageEvent):
        """Show current 01 Core continuity status."""
        try:
            result = await self._request("GET", "/v1/status")
        except Exception as exc:
            yield event.plain_result(self._format_error(exc))
            return

        yield event.plain_result(self._format_status(result))

    @one.command("context")
    async def context(self, event: AstrMessageEvent):
        """Show a compact State Transfer Package summary."""
        try:
            result = await self._request("GET", "/v1/context")
        except Exception as exc:
            yield event.plain_result(self._format_error(exc))
            return

        anchors = result.get("continuity_anchors", {})
        active_intent = result.get("active_intent", {})
        yield event.plain_result(
            "01 Core 上下文包\n"
            f"- 我是谁：{anchors.get('who_am_i', 'unknown')}\n"
            f"- 我在哪：{anchors.get('where_am_i', 'unknown')}\n"
            f"- 我在做什么：{active_intent.get('goal', 'unknown')}\n"
            f"- 最近经历：{len(result.get('recent_episodes', []))}\n"
            f"- 语义记忆：{len(result.get('relevant_semantic_memories', []))}\n"
            f"- 导入记忆：{len(result.get('imported_memories', []))}\n"
            f"- 开放冲突：{len(result.get('open_conflicts', []))}"
        )

    @one.command("chat")
    async def chat(self, event: AstrMessageEvent):
        """Record one AstrBot message as an 01 Core interaction."""
        message = self._extract_tail(event, "/01 chat").strip()
        if not message:
            yield event.plain_result("请在 /01 chat 后面加上要写入 01 Core 的内容。")
            return

        payload = {
            "message": message,
            "user_id": self._event_user_id(event),
            "channel": self.channel_label,
            "session_id": getattr(event, "unified_msg_origin", None),
        }
        try:
            result = await self._request("POST", "/v1/interact", payload)
        except Exception as exc:
            yield event.plain_result(self._format_error(exc))
            return

        yield event.plain_result(
            f"{result.get('reply', '01 Core 已记录这次经历。')}\n"
            f"- Episode：{result.get('episode_id', 'unknown')}\n"
            f"- Tags：{', '.join(result.get('tags', [])) or 'none'}\n"
            f"- Salience：{result.get('salience', 'unknown')}"
        )

    @one.command("dream")
    async def dream(self, event: AstrMessageEvent):
        """Run one 01 Core dream consolidation cycle."""
        raw_limit = self._extract_tail(event, "/01 dream").strip()
        limit = 20
        if raw_limit:
            try:
                limit = max(1, min(1000, int(raw_limit.split()[0])))
            except ValueError:
                yield event.plain_result("limit 需要是数字，例如：/01 dream 50")
                return

        try:
            result = await self._request("POST", "/v1/dream", {"limit": limit})
        except Exception as exc:
            yield event.plain_result(self._format_error(exc))
            return

        yield event.plain_result(
            "01 Core Dream 完成\n"
            f"- 处理上限：{limit}\n"
            f"- 新语义候选：{len(result.get('semantic_candidates', []))}\n"
            f"- 冲突：{len(result.get('conflicts', []))}\n"
            f"- 身份更新提案：{len(result.get('identity_update_proposals', []))}\n"
            f"- 遗忘提案：{len(result.get('forgetting_proposals', []))}"
        )

    async def _request(
        self, method: str, path: str, payload: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        return await asyncio.to_thread(self._request_sync, method, path, payload)

    def _request_sync(
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
        with urllib.request.urlopen(request, timeout=self.timeout_seconds) as response:
            raw = response.read().decode("utf-8")
        parsed = json.loads(raw)
        if not isinstance(parsed, dict):
            raise RuntimeError("01 Core API returned a non-object JSON payload.")
        return parsed

    def _format_status(self, result: dict[str, Any]) -> str:
        return (
            "01 Core 状态\n"
            f"- 人格编号：{result.get('agent_id', 'unknown')}\n"
            f"- 身份：{result.get('identity', 'unknown')}\n"
            f"- 当前目标：{result.get('active_intent', {}).get('goal', 'unknown')}\n"
            f"- 导入记忆：{result.get('imported_memories', 0)}\n"
            f"- 事件记忆：{result.get('episodes', 0)}\n"
            f"- 语义记忆：{result.get('semantic_memories', 0)}\n"
            f"- 开放冲突：{result.get('open_conflicts', 0)}\n"
            f"- 待做梦任务：{result.get('pending_dream_jobs', 0)}\n"
            f"- 更新时间：{result.get('updated_at', 'unknown')}"
        )

    def _format_error(self, exc: Exception) -> str:
        if isinstance(exc, urllib.error.URLError):
            return (
                "无法连接 01 Core API。\n"
                f"- 地址：{self.api_base_url}\n"
                "- 请先运行：python3 -m one_core.cli serve"
            )
        return f"01 Core adapter error: {exc}"

    def _extract_tail(self, event: AstrMessageEvent, command: str) -> str:
        text = str(getattr(event, "message_str", "") or "")
        if not text and hasattr(event, "get_message_str"):
            text = str(event.get_message_str() or "")
        stripped = text.strip()
        if stripped.startswith(command):
            return stripped[len(command) :]
        return stripped

    def _event_user_id(self, event: AstrMessageEvent) -> str:
        for attr in ("get_sender_id", "get_user_id"):
            getter = getattr(event, attr, None)
            if callable(getter):
                try:
                    value = getter()
                    if value:
                        return str(value)
                except Exception:
                    pass
        return self.default_user_id
