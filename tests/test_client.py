from __future__ import annotations

import json
import unittest
from unittest.mock import patch

from one_core.client import (
    AdapterEvent,
    OneCoreClient,
    format_adapters,
    format_context,
    format_status,
)


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
            {
                "adapter_id": "generic_adapter",
                "event": {
                    "text": "hello",
                    "user": {"id": "u1"},
                    "source": {
                        "adapter_id": "generic_adapter",
                        "channel": "test",
                        "session_id": None,
                    },
                    "event_type": "message",
                },
            },
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
        self.assertEqual(captured["url"], "http://localhost:9999/v1/adapter/ingest")
        self.assertEqual(captured["method"], "POST")
        self.assertEqual(captured["timeout"], 3)
        self.assertEqual(
            captured["body"],
            {
                "adapter_id": "generic_adapter",
                "event": {
                    "text": "hello",
                    "user": {"id": "u1"},
                    "source": {
                        "adapter_id": "generic_adapter",
                        "channel": "local",
                        "session_id": "s1",
                    },
                    "event_type": "message",
                    "session_id": "s1",
                },
            },
        )

    def test_client_can_dry_run_interaction(self) -> None:
        captured = {}

        def fake_urlopen(request, timeout):
            captured["body"] = json.loads(request.data.decode("utf-8"))
            return FakeResponse({"status": "preview"})

        with patch("urllib.request.urlopen", fake_urlopen):
            result = OneCoreClient("http://localhost:9999").interact(
                AdapterEvent("hello"),
                dry_run=True,
            )

        self.assertEqual(result, {"status": "preview"})
        self.assertTrue(captured["body"]["dry_run"])

    def test_client_fetches_adapters(self) -> None:
        captured = {}

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["method"] = request.get_method()
            return FakeResponse({"adapters": []})

        with patch("urllib.request.urlopen", fake_urlopen):
            result = OneCoreClient("http://localhost:9999").adapters()

        self.assertEqual(result, {"adapters": []})
        self.assertEqual(captured["url"], "http://localhost:9999/v1/adapters")
        self.assertEqual(captured["method"], "GET")

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
                "registered_adapters": 6,
                "indexed_adapter_events": 7,
                "pending_dream_jobs": 6,
            }
        )
        self.assertIn("01 Core 状态", status)
        self.assertIn("persist", status)
        self.assertIn("已注册适配器：6", status)
        self.assertIn("已索引事件：7", status)

        context = format_context(
            {
                "continuity_anchors": {
                    "who_am_i": "01",
                    "where_am_i": "local",
                },
                "active_intent": {"goal": "test adapters"},
                "context_package_version": "0.2",
                "activation_trace": {
                    "metrics": {"selected_count": 3, "suppressed_count": 1}
                },
                "recent_episodes": [{}],
                "relevant_semantic_memories": [{}, {}],
                "imported_memories": [],
                "open_conflicts": [],
            }
        )
        self.assertIn("01 Core 上下文包", context)
        self.assertIn("test adapters", context)
        self.assertIn("版本：0.2", context)
        self.assertIn("激活记忆：3", context)
        self.assertIn("压制记忆：1", context)

        adapters = format_adapters(
            {
                "adapters": [
                    {
                        "adapter_id": "generic_adapter",
                        "enabled": True,
                        "channels": ["generic_adapter"],
                    }
                ]
            }
        )
        self.assertIn("01 Core 适配器注册表", adapters)
        self.assertIn("generic_adapter", adapters)


if __name__ == "__main__":
    unittest.main()
