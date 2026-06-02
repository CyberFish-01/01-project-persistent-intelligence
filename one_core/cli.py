from __future__ import annotations

import argparse
import json
from pathlib import Path

from .dream import DreamEngine
from .importer import import_text_file
from .state import DEFAULT_STATE_DIR, StateStore


def main() -> None:
    parser = argparse.ArgumentParser(prog="01-core")
    parser.add_argument(
        "--state-dir",
        default=str(DEFAULT_STATE_DIR),
        help="Directory for state.json, episodes.jsonl, and dreams.jsonl.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="Initialize local 01 state.")
    init_parser.add_argument("--force", action="store_true", help="Reinitialize state.")

    subparsers.add_parser("status", help="Print continuity anchors and state summary.")

    interact_parser = subparsers.add_parser("interact", help="Record an interaction.")
    interact_parser.add_argument("message", help="User message to record as an episode.")
    interact_parser.add_argument("--user-id", default="local_user")
    interact_parser.add_argument("--channel", default="cli")

    import_parser = subparsers.add_parser(
        "import-text", help="Import external memories from a plain text file."
    )
    import_parser.add_argument("path", help="Text file containing memories.")
    import_parser.add_argument("--source-label", default="external_memory")
    import_parser.add_argument("--source-system", default="generic_text")
    import_parser.add_argument("--confidence", type=float, default=0.55)

    dream_parser = subparsers.add_parser("dream", help="Run a dream consolidation cycle.")
    dream_parser.add_argument("--limit", type=int, default=20)

    subparsers.add_parser("context", help="Print the current state transfer package.")

    args = parser.parse_args()
    store = StateStore(Path(args.state_dir))

    if args.command == "init":
        state = store.init(force=args.force)
        print_json(
            {
                "status": "initialized",
                "state_dir": str(store.state_dir),
                "agent_id": state["agent_id"],
                "anchors": state["working_state"]["context_anchors"],
            }
        )
    elif args.command == "status":
        state = store.load()
        print_json(
            {
                "agent_id": state["agent_id"],
                "updated_at": state["updated_at"],
                "identity": state["identity_core"]["self_model"]["summary"],
                "active_intent": state["working_state"]["active_intent"],
                "anchors": state["working_state"]["context_anchors"],
                "imported_memories": len(
                    state["memory_stores"].get("imported_memory", [])
                ),
                "episodes": len(state["memory_stores"]["episodic_memory"]),
                "semantic_memories": len(state["memory_stores"]["semantic_memory"]),
                "open_conflicts": len(state.get("open_conflicts", [])),
                "pending_dream_jobs": len(
                    [
                        job
                        for job in state.get("dream_queue", [])
                        if job.get("status") == "pending"
                    ]
                ),
            }
        )
    elif args.command == "interact":
        episode = store.record_episode(
            args.message, user_id=args.user_id, channel=args.channel
        )
        package = store.build_context_package()
        print_json(
            {
                "episode_id": episode["id"],
                "summary": episode["summary"],
                "tags": episode["tags"],
                "salience": episode["salience"],
                "reply": build_local_reply(package),
                "anchors": package["continuity_anchors"],
            }
        )
    elif args.command == "import-text":
        report = import_text_file(
            store,
            Path(args.path),
            source_label=args.source_label,
            source_system=args.source_system,
            confidence=args.confidence,
        )
        print_json(report)
    elif args.command == "dream":
        report = DreamEngine(store).run(limit=args.limit)
        print_json(report)
    elif args.command == "context":
        print_json(store.build_context_package())


def build_local_reply(package: dict) -> str:
    active_goal = package["active_intent"]["goal"]
    anchors = package["continuity_anchors"]
    return (
        "01 Core 已记录这次经历。"
        f" 我是谁：{anchors['who_am_i']}"
        f" 我在哪：{anchors['where_am_i']}"
        f" 我在做什么：{active_goal}"
    )


def print_json(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
