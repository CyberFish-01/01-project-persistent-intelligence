import tempfile
import unittest
from pathlib import Path

from one_core.state import StateStore
from one_core.validation import validate_state


class StateValidationTests(unittest.TestCase):
    def test_initialized_state_passes_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "passed")
            self.assertEqual(report["issue_count"], 0)

    def test_missing_continuity_anchor_fails_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["working_state"]["context_anchors"].pop("who_am_i")
            report = validate_state(state, store.list_episodes())
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn("working_state.context_anchors.who_am_i", paths)

    def test_adapter_event_index_must_point_to_episode(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            state["adapter_event_index"] = {
                "local_generic_adapter": {
                    "event-1": {
                        "adapter_id": "local_generic_adapter",
                        "event_id": "event-1",
                        "episode_id": "missing_episode",
                        "recorded_at": state["created_at"],
                        "channel": "local",
                    }
                }
            }
            report = validate_state(state, [{"id": "episode_present"}])
            self.assertEqual(report["status"], "failed")
            paths = {issue["path"] for issue in report["issues"]}
            self.assertIn(
                "adapter_event_index.local_generic_adapter.event-1.episode_id",
                paths,
            )


if __name__ == "__main__":
    unittest.main()
