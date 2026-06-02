from __future__ import annotations

import io
import json
import unittest
from unittest.mock import patch

from one_core.client import AdapterEvent, OneCoreClient, format_context, format_status


class FakeResponse:
    def __init__(self, payload: dict):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False

    def read(self) -> bytes:
        return json.dumps(self.payload).encode("utf-8")


class ClientTest(unittest.TestCase):
    def test_adapter_event_payload_omits_empty_session(self) -> None:
        event = AdapterEvent("hello", user_id="u1", channel="test")
        self.assertEqual(
            event.to_payload(),
            {"message": "hello", "user_id": "u1", "channel": "test"},
        )

    def test_client_posts_interaction_payload(self) -> None:
        captured = {}

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["method"] = request.get_method()
            captured["body"] = json.loads(request.data.decode("utf-8"))
            captured["timeout"] = timeout
            return FakeResponse({"reply": "ok"})

        with patch("urllib.request.urlopen", fake_urlopen):
            result = OneCoreClient("http://localhost:9999", timeout=3).interact(
                AdapterEvent(
                    "hello",
                    user_id="u1",
                    channel="local",
                    session_id="s1",
                )
            )

        self.assertEqual(result, {"reply": "ok"})
        self.assertEqual(captured["url"], "http://localhost:9999/v1/interact")
        self.assertEqual(captured["method"], "POST")
        self.assertEqual(captured["timeout"], 3)
        self.assertEqual(
            captured["body"],
            {
                "message": "hello",
                "user_id": "u1",
                "channel": "local",
                "session_id": "s1",
            },
        )

    def test_formatters_are_human_readable(self) -> None:
        status = format_status(
            {
                "agent_id": "01",
                "identity": "seed",
                "active_intent": {"goal": "persist"},
                "imported_memories": 2,
                "episodes": 3,
                "semantic_memories": 4,
                "open_conflicts": 5,
                "pending_dream_jobs": 6,
            }
        )
        self.assertIn("01 Core 状态", status)
        self.assertIn("persist", status)

        context = format_context(
            {
                "continuity_anchors": {
                    "who_am_i": "01",
                    "where_am_i": "local",
                },
                "active_intent": {"goal": "test adapters"},
                "recent_episodes": [{}],
                "relevant_semantic_memories": [{}, {}],
                "imported_memories": [],
                "open_conflicts": [],
            }
        )
        self.assertIn("01 Core 上下文包", context)
        self.assertIn("test adapters", context)


if __name__ == "__main__":
    unittest.main()
