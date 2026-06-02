import tempfile
import unittest
from pathlib import Path

from one_core.api import OneCoreAPI
from one_core.state import StateStore


class APITests(unittest.TestCase):
    def test_status_interact_and_dream_endpoints(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            status_code, status = api.handle_get("/v1/status")
            self.assertEqual(status_code, 200)
            self.assertEqual(status["agent_id"], "01")
            self.assertEqual(status["episodes"], 0)
            self.assertGreaterEqual(status["registered_adapters"], 1)
            self.assertEqual(status["indexed_adapter_events"], 0)

            status_code, adapters = api.handle_get("/v1/adapters")
            self.assertEqual(status_code, 200)
            adapter_ids = [adapter["adapter_id"] for adapter in adapters["adapters"]]
            self.assertIn("local_generic_adapter", adapter_ids)

            status_code, interact = api.handle_post(
                "/v1/interact",
                {
                    "message": "我们通过 API 接入 AstrBot adapter。",
                    "user_id": "test_user",
                    "channel": "test_api",
                },
            )
            self.assertEqual(status_code, 200)
            self.assertIn("episode_id", interact)
            self.assertIn("external_adapter", interact["tags"])
            self.assertIn("state_transfer_package", interact)

            status_code, dream = api.handle_post("/v1/dream", {"limit": 10})
            self.assertEqual(status_code, 200)
            self.assertIn("summary", dream)

            status_code, status_after = api.handle_get("/v1/status")
            self.assertEqual(status_code, 200)
            self.assertEqual(status_after["episodes"], 1)
            self.assertEqual(status_after["pending_dream_jobs"], 0)

    def test_interact_requires_message(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            status_code, response = api.handle_post("/v1/interact", {})
            self.assertEqual(status_code, 400)
            self.assertEqual(response["error"], "missing_message")

    def test_adapter_ingest_dry_run_does_not_record_episode(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            status_code, preview = api.handle_post(
                "/v1/adapter/ingest",
                {
                    "adapter_id": "local_generic_adapter",
                    "dry_run": True,
                    "event": {
                        "text": "这是一条 dry-run adapter 事件。",
                        "user": {"id": "tester"},
                        "source": {
                            "channel": "local_test",
                            "session_id": "session_1",
                        },
                        "event_type": "message",
                        "salience_hint": 0.9,
                    },
                },
            )
            self.assertEqual(status_code, 200)
            self.assertEqual(preview["status"], "preview")
            self.assertTrue(preview["dry_run"])
            self.assertIn("would_record_episode", preview)
            self.assertGreaterEqual(preview["would_record_episode"]["salience"], 0.25)

            status_code, status = api.handle_get("/v1/status")
            self.assertEqual(status_code, 200)
            self.assertEqual(status["episodes"], 0)
            self.assertEqual(status["indexed_adapter_events"], 0)

    def test_adapter_ingest_ignores_invalid_salience_hint(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            status_code, preview = api.handle_post(
                "/v1/adapter/ingest",
                {
                    "adapter_id": "generic_adapter",
                    "dry_run": True,
                    "event": {
                        "text": "普通消息",
                        "salience_hint": "not-a-number",
                    },
                },
            )
            self.assertEqual(status_code, 200)
            self.assertEqual(preview["would_record_episode"]["salience"], 0.25)

    def test_adapter_ingest_deduplicates_recorded_event_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            payload = {
                "adapter_id": "local_generic_adapter",
                "event": {
                    "event_id": "event-1",
                    "text": "这是一条真实 adapter 事件。",
                    "user": {"id": "tester"},
                    "source": {
                        "channel": "local",
                        "session_id": "session_1",
                    },
                    "event_type": "message",
                },
            }
            status_code, recorded = api.handle_post("/v1/adapter/ingest", payload)
            self.assertEqual(status_code, 200)
            self.assertEqual(recorded["status"], "recorded")

            status_code, duplicate = api.handle_post("/v1/adapter/ingest", payload)
            self.assertEqual(status_code, 409)
            self.assertEqual(duplicate["status"], "duplicate")
            self.assertEqual(duplicate["error"], "duplicate_event")
            self.assertEqual(duplicate["episode_id"], recorded["episode_id"])

            status_code, status = api.handle_get("/v1/status")
            self.assertEqual(status_code, 200)
            self.assertEqual(status["episodes"], 1)
            self.assertEqual(status["indexed_adapter_events"], 1)

    def test_adapter_ingest_without_event_id_is_not_deduplicated(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            payload = {
                "adapter_id": "local_generic_adapter",
                "event": {
                    "text": "没有 event_id 的兼容消息。",
                    "source": {"channel": "local"},
                },
            }
            first_status, first = api.handle_post("/v1/adapter/ingest", payload)
            second_status, second = api.handle_post("/v1/adapter/ingest", payload)
            self.assertEqual(first_status, 200)
            self.assertEqual(second_status, 200)
            self.assertNotEqual(first["episode_id"], second["episode_id"])

            status_code, status = api.handle_get("/v1/status")
            self.assertEqual(status_code, 200)
            self.assertEqual(status["episodes"], 2)
            self.assertEqual(status["indexed_adapter_events"], 0)

    def test_adapter_ingest_rejects_unregistered_adapter(self):
        with tempfile.TemporaryDirectory() as tmp:
            api = OneCoreAPI(StateStore(Path(tmp)))
            status_code, response = api.handle_post(
                "/v1/adapter/ingest",
                {
                    "adapter_id": "unknown_adapter",
                    "dry_run": True,
                    "event": {"text": "未知 adapter 不应写入。"},
                },
            )
            self.assertEqual(status_code, 403)
            self.assertEqual(response["status"], "rejected")
            self.assertEqual(response["error"], "unregistered_adapter")

            status_code, status = api.handle_get("/v1/status")
            self.assertEqual(status_code, 200)
            self.assertEqual(status["episodes"], 0)


if __name__ == "__main__":
    unittest.main()
