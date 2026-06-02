import tempfile
import unittest
from pathlib import Path

from one_core.dream import DreamEngine
from one_core.importer import import_text_file, split_memory_text
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

    def test_import_text_stages_external_memory_without_identity_update(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "astrbot_01_memory.txt"
            source.write_text(
                "- 01 认为连续性是 State Transfer。\n"
                "- AstrBot 只是外部身体，不应该拥有 01 Core 状态。\n",
                encoding="utf-8",
            )
            store = StateStore(root / "state")
            before_identity = store.init()["identity_core"]
            report = import_text_file(
                store,
                source,
                source_label="astrbot_01_export",
                source_system="astrbot_text",
            )
            state = store.load()
            self.assertEqual(report["imported_count"], 2)
            self.assertEqual(len(state["memory_stores"]["imported_memory"]), 2)
            self.assertEqual(state["identity_core"], before_identity)
            self.assertFalse(
                state["memory_stores"]["imported_memory"][0]["promotion_policy"][
                    "may_update_identity_core"
                ]
            )

    def test_dream_reviews_imported_memory(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "memory.txt"
            source.write_text("01 的连续性来自 State Transfer。", encoding="utf-8")
            store = StateStore(root / "state")
            store.init()
            report = import_text_file(
                store,
                source,
                source_label="astrbot_01_export",
                source_system="astrbot_text",
            )
            dream = DreamEngine(store).run()
            self.assertEqual(len(report["memory_ids"]), 1)
            self.assertEqual(dream["input_imports"], report["memory_ids"])
            self.assertTrue(dream["semantic_candidates"])

    def test_split_memory_text_accepts_bullets(self):
        chunks = split_memory_text("- A\n- B\n- C")
        self.assertEqual(chunks, ["A", "B", "C"])


if __name__ == "__main__":
    unittest.main()
