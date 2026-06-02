from __future__ import annotations

import argparse
import json
from pathlib import Path

from .api import run_server, state_summary
from .client import (
    AdapterEvent,
    OneCoreClient,
    format_adapters,
    format_context,
    format_status,
)
from .cleaner import clean_memory_files, write_cleaned_text
from .dream import DreamEngine
from .evaluation import run_foundation_evaluation, run_scenario_evaluation
from .importer import import_text_file
from .state import DEFAULT_STATE_DIR, StateStore
from .validation import validate_state


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

    clean_parser = subparsers.add_parser(
        "clean-memory",
        help="Clean raw memory exports into generic text for import-text.",
    )
    clean_parser.add_argument("paths", nargs="+", help="Raw memory export files.")
    clean_parser.add_argument(
        "-o",
        "--output",
        required=True,
        help="Output .txt file in generic bullet format.",
    )
    clean_parser.add_argument("--min-chars", type=int, default=8)

    serve_parser = subparsers.add_parser("serve", help="Run the local 01 Core HTTP API.")
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8765)

    dream_parser = subparsers.add_parser("dream", help="Run a dream consolidation cycle.")
    dream_parser.add_argument("--limit", type=int, default=20)

    promote_parser = subparsers.add_parser(
        "promote-candidate",
        help="Promote a reviewed candidate memory into active semantic memory.",
    )
    promote_parser.add_argument("candidate_id")
    promote_parser.add_argument("--reviewer", default="manual_review")
    promote_parser.add_argument("--decision-note", default="")

    review_parser = subparsers.add_parser(
        "review-candidate",
        help="Review a candidate memory with promote, archive, discard, or quarantine.",
    )
    review_parser.add_argument("candidate_id")
    review_parser.add_argument(
        "--action",
        required=True,
        choices=["promote", "archive", "discard", "quarantine"],
    )
    review_parser.add_argument("--reviewer", default="manual_review")
    review_parser.add_argument("--decision-note", default="")

    lifecycle_parser = subparsers.add_parser(
        "lifecycle",
        help="Apply a reviewed lifecycle action to a durable memory.",
    )
    lifecycle_parser.add_argument(
        "store_name",
        choices=[
            "imported_memory",
            "episodic_memory",
            "candidate_memory",
            "semantic_memory",
        ],
    )
    lifecycle_parser.add_argument("memory_id")
    lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["archive", "discard", "quarantine"],
    )
    lifecycle_parser.add_argument("--reviewer", default="manual_review")
    lifecycle_parser.add_argument("--decision-note", default="")

    identity_propose_parser = subparsers.add_parser(
        "propose-identity-update",
        help="Create a high-gate identity update proposal without applying it.",
    )
    identity_propose_parser.add_argument("statement")
    identity_propose_parser.add_argument(
        "--evidence",
        action="append",
        default=[],
        help="Supporting memory/action/claim id. Repeat for multiple evidence ids.",
    )
    identity_propose_parser.add_argument("--proposer", default="manual_review")
    identity_propose_parser.add_argument("--rationale", default="")
    identity_propose_parser.add_argument(
        "--target-path",
        default="memory_stores.identity_memory",
    )
    identity_propose_parser.add_argument("--confidence", type=float, default=0.7)

    identity_review_parser = subparsers.add_parser(
        "review-identity-update",
        help="Review an identity update proposal through the high gate.",
    )
    identity_review_parser.add_argument("proposal_id")
    identity_review_parser.add_argument(
        "--action",
        required=True,
        choices=["approve", "reject", "quarantine"],
    )
    identity_review_parser.add_argument("--reviewer", default="manual_review")
    identity_review_parser.add_argument("--decision-note", default="")

    subparsers.add_parser("context", help="Print the current state transfer package.")

    subparsers.add_parser(
        "evaluate-foundation",
        help="Run non-destructive foundation invariant checks.",
    )
    subparsers.add_parser(
        "evaluate-scenarios",
        help="Run non-destructive continuity scenario checks.",
    )
    subparsers.add_parser(
        "validate-state",
        help="Validate the current state structure without mutating it.",
    )
    subparsers.add_parser(
        "replay-events",
        help="Check append-only event log consistency against current update_log.",
    )
    rollback_parser = subparsers.add_parser(
        "rollback-preview",
        help="Preview rollback metadata for a snapshot without mutating state.",
    )
    rollback_parser.add_argument("snapshot_id")

    remote_parser = subparsers.add_parser(
        "remote", help="Call a running 01 Core API through the generic adapter protocol."
    )
    remote_parser.add_argument(
        "--api-base-url",
        default="http://127.0.0.1:8765",
        help="01 Core API base URL.",
    )
    remote_subparsers = remote_parser.add_subparsers(
        dest="remote_command", required=True
    )
    remote_subparsers.add_parser("health", help="Call GET /health.")
    remote_subparsers.add_parser("status", help="Call GET /v1/status.")
    remote_subparsers.add_parser("context", help="Call GET /v1/context.")
    remote_subparsers.add_parser("adapters", help="Call GET /v1/adapters.")
    remote_interact = remote_subparsers.add_parser(
        "interact", help="Call POST /v1/interact."
    )
    remote_interact.add_argument("message")
    remote_interact.add_argument("--user-id", default="local_adapter_user")
    remote_interact.add_argument("--channel", default="local_generic_adapter")
    remote_interact.add_argument("--session-id")
    remote_interact.add_argument("--adapter-id", default="local_generic_adapter")
    remote_interact.add_argument("--event-id")
    remote_interact.add_argument("--event-type", default="message")
    remote_interact.add_argument("--salience-hint", type=float)
    remote_interact.add_argument("--dry-run", action="store_true")
    remote_dream = remote_subparsers.add_parser("dream", help="Call POST /v1/dream.")
    remote_dream.add_argument("--limit", type=int, default=20)

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
        print_json(state_summary(store))
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
    elif args.command == "clean-memory":
        memories = clean_memory_files(
            [Path(path) for path in args.paths], min_chars=args.min_chars
        )
        report = write_cleaned_text(memories, Path(args.output))
        print_json(report)
    elif args.command == "serve":
        run_server(host=args.host, port=args.port, state_dir=Path(args.state_dir))
    elif args.command == "dream":
        report = DreamEngine(store).run(limit=args.limit)
        print_json(report)
    elif args.command == "promote-candidate":
        print_json(
            store.promote_candidate_memory(
                args.candidate_id,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "review-candidate":
        print_json(
            store.review_candidate_memory(
                args.candidate_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "lifecycle":
        print_json(
            store.apply_memory_lifecycle_action(
                store_name=args.store_name,
                memory_id=args.memory_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "propose-identity-update":
        print_json(
            store.propose_identity_update(
                statement=args.statement,
                evidence=args.evidence,
                proposer=args.proposer,
                rationale=args.rationale,
                target_path=args.target_path,
                confidence=args.confidence,
            )
        )
    elif args.command == "review-identity-update":
        print_json(
            store.review_identity_update(
                proposal_id=args.proposal_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "context":
        print_json(store.build_context_package())
    elif args.command == "evaluate-foundation":
        print_json(run_foundation_evaluation())
    elif args.command == "evaluate-scenarios":
        print_json(run_scenario_evaluation())
    elif args.command == "validate-state":
        print_json(
            validate_state(
                store.load(),
                store.list_episodes(),
                events=store.list_events(),
                dream_artifacts=store.list_dream_artifacts(),
            )
        )
    elif args.command == "replay-events":
        print_json(store.replay_events())
    elif args.command == "rollback-preview":
        print_json(store.rollback_preview(args.snapshot_id))
    elif args.command == "remote":
        client = OneCoreClient(args.api_base_url)
        if args.remote_command == "health":
            print_json(client.health())
        elif args.remote_command == "status":
            print(format_status(client.status()))
        elif args.remote_command == "context":
            print(format_context(client.context()))
        elif args.remote_command == "adapters":
            print(format_adapters(client.adapters()))
        elif args.remote_command == "interact":
            print_json(
                client.interact(
                    AdapterEvent(
                        message=args.message,
                        user_id=args.user_id,
                        channel=args.channel,
                        session_id=args.session_id,
                        adapter_id=args.adapter_id,
                        event_id=args.event_id,
                        event_type=args.event_type,
                        salience_hint=args.salience_hint,
                    ),
                    dry_run=args.dry_run,
                )
            )
        elif args.remote_command == "dream":
            print_json(client.dream(limit=args.limit))


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
