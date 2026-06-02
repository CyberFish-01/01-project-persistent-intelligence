import tempfile
import unittest
from pathlib import Path

from one_core.dream import DreamEngine
from one_core.state import StateStore


class CoreStateTests(unittest.TestCase):
    def test_init_creates_continuity_anchors(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            state = store.init()
            anchors = state["working_state"]["context_anchors"]
            self.assertIn("who_am_i", anchors)
            self.assertIn("where_am_i", anchors)
            self.assertIn("what_am_i_doing", anchors)
            self.assertEqual(state["agent_id"], "01")

    def test_interaction_records_episode_and_updates_intent(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            store.init()
            episode = store.record_episode("我们开始实现 01 Core 的 State Transfer。")
            state = store.load()
            self.assertEqual(len(state["memory_stores"]["episodic_memory"]), 1)
            self.assertIn("state_transfer", episode["tags"])
            self.assertEqual(state["working_state"]["active_intent"]["status"], "active")

    def test_dream_promotes_semantic_memory(self):
        with tempfile.TemporaryDirectory() as tmp:
            store = StateStore(Path(tmp))
            store.init()
            store.record_episode("State Transfer 是 01 的核心。")
            store.record_episode("我们继续做 State Transfer 和 Dream Engine。")
            report = DreamEngine(store).run()
            statements = [
                memory["statement"]
                for memory in store.load()["memory_stores"]["semantic_memory"]
            ]
            self.assertTrue(report["semantic_candidates"])
            self.assertIn(
                "The project repeatedly treats continuity as state transfer rather than memory retrieval.",
                statements,
            )


if __name__ == "__main__":
    unittest.main()
