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
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Reinitialize state and reset local JSONL logs in the state directory.",
    )

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

    procedural_lifecycle_parser = subparsers.add_parser(
        "procedural-lifecycle",
        help="Apply a reviewed lifecycle action to a procedural memory.",
    )
    procedural_lifecycle_parser.add_argument("memory_id")
    procedural_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["archive", "discard", "quarantine"],
    )
    procedural_lifecycle_parser.add_argument("--reviewer", default="manual_review")
    procedural_lifecycle_parser.add_argument("--decision-note", default="")

    cautionary_lifecycle_parser = subparsers.add_parser(
        "cautionary-warning-lifecycle",
        help="Apply a reviewed lifecycle action to a cautionary warning.",
    )
    cautionary_lifecycle_parser.add_argument("memory_id")
    cautionary_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["archive", "discard", "quarantine"],
    )
    cautionary_lifecycle_parser.add_argument("--reviewer", default="manual_review")
    cautionary_lifecycle_parser.add_argument("--decision-note", default="")

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

    claim_review_parser = subparsers.add_parser(
        "review-claim",
        help="Review a claim graph node with minimal-change patch preview.",
    )
    claim_review_parser.add_argument("claim_id")
    claim_review_parser.add_argument(
        "--action",
        required=True,
        choices=["resolve", "reject", "quarantine", "keep_open"],
    )
    claim_review_parser.add_argument("--reviewer", default="manual_review")
    claim_review_parser.add_argument("--decision-note", default="")

    procedural_review_parser = subparsers.add_parser(
        "review-procedural-candidate",
        help="Review a procedural memory candidate.",
    )
    procedural_review_parser.add_argument("candidate_id")
    procedural_review_parser.add_argument(
        "--action",
        required=True,
        choices=["approve", "reject", "archive", "quarantine"],
    )
    procedural_review_parser.add_argument("--reviewer", default="manual_review")
    procedural_review_parser.add_argument("--decision-note", default="")

    cautionary_review_parser = subparsers.add_parser(
        "review-cautionary-procedural-candidate",
        help="Review a cautionary procedural warning candidate.",
    )
    cautionary_review_parser.add_argument("candidate_id")
    cautionary_review_parser.add_argument(
        "--action",
        required=True,
        choices=["approve", "reject", "archive", "quarantine"],
    )
    cautionary_review_parser.add_argument("--reviewer", default="manual_review")
    cautionary_review_parser.add_argument("--decision-note", default="")

    failure_reflection_parser = subparsers.add_parser(
        "record-failure-reflection",
        help="Record a failure reflection and cautionary procedural candidate.",
    )
    failure_reflection_parser.add_argument("--workflow", required=True)
    failure_reflection_parser.add_argument("--summary", required=True)
    failure_reflection_parser.add_argument("--lesson", required=True)
    failure_reflection_parser.add_argument("--reviewer", default="manual_review")
    failure_reflection_parser.add_argument("--action-id", default=None)
    failure_reflection_parser.add_argument("--next-action", default="")

    reflection_log_parser = subparsers.add_parser(
        "record-reflection",
        help="Record a reflection log entry without requiring a failure reflection.",
    )
    reflection_log_parser.add_argument("--reflection-type", required=True)
    reflection_log_parser.add_argument("--workflow", required=True)
    reflection_log_parser.add_argument("--observation", required=True)
    reflection_log_parser.add_argument("--lesson", required=True)
    reflection_log_parser.add_argument("--expected-behavior", required=True)
    reflection_log_parser.add_argument("--actor", default="manual_review")
    reflection_log_parser.add_argument("--source-id", action="append", default=[])
    reflection_log_parser.add_argument("--evidence", action="append", default=[])
    reflection_log_parser.add_argument("--risk", default="medium")
    reflection_log_parser.add_argument("--confidence", type=float, default=0.5)

    verify_reflection_parser = subparsers.add_parser(
        "verify-reflection",
        help="Verify a reflection log entry and record the outcome.",
    )
    verify_reflection_parser.add_argument("reflection_id")
    verify_reflection_parser.add_argument(
        "--result",
        required=True,
        choices=["verified", "not_observed", "regressed", "superseded"],
    )
    verify_reflection_parser.add_argument("--verifier", default="manual_review")
    verify_reflection_parser.add_argument("--evidence", action="append", default=[])
    verify_reflection_parser.add_argument("--note", default="")

    reflection_guidance_parser = subparsers.add_parser(
        "review-reflection-guidance",
        help="Review a reflection guidance queue item without creating executable policy.",
    )
    reflection_guidance_parser.add_argument("guidance_item_id")
    reflection_guidance_parser.add_argument(
        "--action",
        required=True,
        choices=["acknowledge", "archive", "quarantine"],
    )
    reflection_guidance_parser.add_argument("--reviewer", default="manual_review")
    reflection_guidance_parser.add_argument("--decision-note", default="")

    attribution_coverage_parser = subparsers.add_parser(
        "review-context-attribution-coverage",
        help="Create a review-only coverage report for recent Context Builder attribution traces.",
    )
    attribution_coverage_parser.add_argument("--reviewer", default="manual_review")
    attribution_coverage_parser.add_argument("--window", type=int, default=5)
    attribution_coverage_parser.add_argument(
        "--minimum-source-record-ratio",
        type=float,
        default=0.8,
    )
    attribution_coverage_parser.add_argument("--note", default="")

    attribution_coverage_lifecycle_parser = subparsers.add_parser(
        "context-attribution-coverage-lifecycle",
        help="Apply a reviewed lifecycle action to a Context Builder attribution coverage review.",
    )
    attribution_coverage_lifecycle_parser.add_argument("review_id")
    attribution_coverage_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["acknowledge", "archive", "quarantine"],
    )
    attribution_coverage_lifecycle_parser.add_argument(
        "--reviewer",
        default="manual_review",
    )
    attribution_coverage_lifecycle_parser.add_argument("--decision-note", default="")

    tool_safety_proposal_parser = subparsers.add_parser(
        "propose-tool-safety-policy",
        help="Create a non-executable tool/safety policy proposal from reviewed guidance.",
    )
    tool_safety_proposal_parser.add_argument("guidance_item_id")
    tool_safety_proposal_parser.add_argument("--policy-scope", required=True)
    tool_safety_proposal_parser.add_argument("--proposed-rule", required=True)
    tool_safety_proposal_parser.add_argument("--proposer", default="manual_review")
    tool_safety_proposal_parser.add_argument("--rationale", default="")
    tool_safety_proposal_parser.add_argument("--risk", default="medium")
    tool_safety_proposal_parser.add_argument("--confidence", type=float, default=0.5)

    tool_safety_review_parser = subparsers.add_parser(
        "review-tool-safety-policy-proposal",
        help="Review a non-executable tool/safety policy proposal.",
    )
    tool_safety_review_parser.add_argument("proposal_id")
    tool_safety_review_parser.add_argument(
        "--action",
        required=True,
        choices=["approve", "reject", "archive", "quarantine"],
    )
    tool_safety_review_parser.add_argument("--reviewer", default="manual_review")
    tool_safety_review_parser.add_argument("--decision-note", default="")

    tool_safety_lifecycle_parser = subparsers.add_parser(
        "tool-safety-policy-lifecycle",
        help="Apply a reviewed lifecycle action to a tool/safety policy proposal.",
    )
    tool_safety_lifecycle_parser.add_argument("proposal_id")
    tool_safety_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["archive", "discard", "quarantine"],
    )
    tool_safety_lifecycle_parser.add_argument("--reviewer", default="manual_review")
    tool_safety_lifecycle_parser.add_argument("--decision-note", default="")

    tool_safety_link_parser = subparsers.add_parser(
        "link-tool-safety-policy-proposals",
        help="Create a review-only link between two tool/safety policy proposals.",
    )
    tool_safety_link_parser.add_argument("from_proposal_id")
    tool_safety_link_parser.add_argument("to_proposal_id")
    tool_safety_link_parser.add_argument(
        "--link-type",
        required=True,
        choices=[
            "supports",
            "conflicts_with",
            "supersedes",
            "overlaps",
            "depends_on",
        ],
    )
    tool_safety_link_parser.add_argument("--reviewer", default="manual_review")
    tool_safety_link_parser.add_argument("--reason", default="")
    tool_safety_link_parser.add_argument(
        "--evidence",
        action="append",
        default=[],
        help="Supporting memory/action/proposal id. Repeat for multiple evidence ids.",
    )
    tool_safety_link_parser.add_argument("--confidence", type=float, default=0.5)

    tool_safety_link_lifecycle_parser = subparsers.add_parser(
        "tool-safety-policy-link-lifecycle",
        help="Apply a reviewed lifecycle action to a tool/safety policy proposal link.",
    )
    tool_safety_link_lifecycle_parser.add_argument("link_id")
    tool_safety_link_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["archive", "discard", "quarantine"],
    )
    tool_safety_link_lifecycle_parser.add_argument(
        "--reviewer",
        default="manual_review",
    )
    tool_safety_link_lifecycle_parser.add_argument("--decision-note", default="")

    proposal_link_bridge_parser = subparsers.add_parser(
        "bridge-proposal-link-claim-evidence",
        help="Bridge a proposal link into claim graph evidence without mutating claims.",
    )
    proposal_link_bridge_parser.add_argument("link_id")
    proposal_link_bridge_parser.add_argument("--reviewer", default="manual_review")
    proposal_link_bridge_parser.add_argument("--rationale", default="")

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
    event_report_parser = subparsers.add_parser(
        "event-report",
        help="Report replay projection coverage and retention suggestions without mutating state.",
    )
    event_report_parser.add_argument("--retention-limit", type=int, default=200)
    subparsers.add_parser(
        "event-payload-diff-report",
        help="Preview event payload and object-diff coverage without mutating state.",
    )
    subparsers.add_parser(
        "event-replayability-assessment",
        help="Assess whether events can support future state reconstruction without mutating state.",
    )
    subparsers.add_parser(
        "reconstruction-evidence-schema-report",
        help="Draft report-only evidence schema requirements for future reconstruction.",
    )
    subparsers.add_parser(
        "reconstruction-evidence-coverage-map",
        help="Map current event workflows to reconstruction evidence schema gaps.",
    )
    subparsers.add_parser(
        "reconstruction-evidence-gap-priorities",
        help="Rank reconstruction evidence gaps for review without mutating state.",
    )
    subparsers.add_parser(
        "reconstruction-evidence-schema-review-checklist",
        help="Build a review-only schema checklist from prioritized reconstruction evidence gaps.",
    )
    reconstruction_schema_review_parser = subparsers.add_parser(
        "review-reconstruction-schema-checklist-item",
        help="Record a non-executable review decision for a reconstruction schema checklist item.",
    )
    reconstruction_schema_review_parser.add_argument("checklist_id")
    reconstruction_schema_review_parser.add_argument(
        "--action",
        required=True,
        choices=[
            "approve_for_schema_design",
            "request_more_evidence",
            "reject_as_low_value",
            "defer",
            "quarantine",
        ],
    )
    reconstruction_schema_review_parser.add_argument(
        "--reviewer",
        default="manual_review",
    )
    reconstruction_schema_review_parser.add_argument("--rationale", default="")
    reconstruction_schema_review_parser.add_argument(
        "--requested-evidence",
        action="append",
        default=[],
        help="Evidence request to attach to the review decision; may be repeated.",
    )
    reconstruction_schema_review_parser.add_argument(
        "--approval-scope",
        action="append",
        default=[],
        help="Schema design scope approved for later review; may be repeated.",
    )
    subparsers.add_parser(
        "reconstruction-schema-review-coverage-map",
        help="Map reconstruction schema checklist review decisions to workflow coverage without mutating state.",
    )
    subparsers.add_parser(
        "reconstruction-schema-review-evidence-requests",
        help="Track requested reconstruction schema review evidence without mutating state.",
    )
    subparsers.add_parser(
        "growth-semantics-rfc",
        help="Print the P50 stateful memory and growth semantics RFC without mutating state.",
    )
    subparsers.add_parser(
        "growth-semantics-report",
        help="Report review-only growth semantics signals without mutating state.",
    )
    subparsers.add_parser(
        "growth-candidate-review-rfc",
        help="Print the P51 growth candidate review RFC without mutating state.",
    )
    subparsers.add_parser(
        "growth-candidate-review-report",
        help="Report review-only growth candidate review objects without mutating state.",
    )
    evidence_request_lifecycle_parser = subparsers.add_parser(
        "reconstruction-schema-evidence-request-lifecycle",
        help="Apply a review-only lifecycle action to a reconstruction schema evidence request.",
    )
    evidence_request_lifecycle_parser.add_argument("request_id")
    evidence_request_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["satisfy", "defer", "archive", "quarantine"],
    )
    evidence_request_lifecycle_parser.add_argument(
        "--reviewer",
        default="manual_review",
    )
    evidence_request_lifecycle_parser.add_argument("--decision-note", default="")
    evidence_request_lifecycle_parser.add_argument(
        "--evidence-ref",
        action="append",
        default=[],
        help="Evidence reference used to satisfy or review the request; may be repeated.",
    )
    payload_capture_policy_parser = subparsers.add_parser(
        "propose-event-payload-capture-policy",
        help="Create a review-only event payload capture policy proposal.",
    )
    payload_capture_policy_parser.add_argument("--proposer", default="manual_review")
    payload_capture_policy_parser.add_argument("--rationale", default="")
    payload_capture_policy_review_parser = subparsers.add_parser(
        "review-event-payload-capture-policy",
        help="Review a non-executable event payload capture policy proposal.",
    )
    payload_capture_policy_review_parser.add_argument("proposal_id")
    payload_capture_policy_review_parser.add_argument(
        "--action",
        required=True,
        choices=["approve", "reject", "archive", "quarantine"],
    )
    payload_capture_policy_review_parser.add_argument("--reviewer", default="manual_review")
    payload_capture_policy_review_parser.add_argument("--decision-note", default="")
    event_retention_review_parser = subparsers.add_parser(
        "review-event-retention",
        help="Record a review-only event retention planning record.",
    )
    event_retention_review_parser.add_argument("--retention-limit", type=int, default=200)
    event_retention_review_parser.add_argument("--reviewer", default="manual_review")
    event_retention_review_parser.add_argument("--note", default="")
    event_retention_lifecycle_parser = subparsers.add_parser(
        "event-retention-lifecycle",
        help="Apply a review-only lifecycle action to an event retention review.",
    )
    event_retention_lifecycle_parser.add_argument("review_id")
    event_retention_lifecycle_parser.add_argument(
        "--action",
        required=True,
        choices=["acknowledge", "archive", "quarantine"],
    )
    event_retention_lifecycle_parser.add_argument("--reviewer", default="manual_review")
    event_retention_lifecycle_parser.add_argument("--decision-note", default="")
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
    elif args.command == "procedural-lifecycle":
        print_json(
            store.apply_procedural_lifecycle_action(
                memory_id=args.memory_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "cautionary-warning-lifecycle":
        print_json(
            store.apply_cautionary_warning_lifecycle_action(
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
    elif args.command == "review-claim":
        print_json(
            store.review_claim(
                claim_id=args.claim_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "review-procedural-candidate":
        print_json(
            store.review_procedural_candidate(
                candidate_id=args.candidate_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "review-cautionary-procedural-candidate":
        print_json(
            store.review_cautionary_procedural_candidate(
                candidate_id=args.candidate_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "record-failure-reflection":
        print_json(
            store.record_failure_reflection(
                workflow=args.workflow,
                summary=args.summary,
                lesson=args.lesson,
                reviewer=args.reviewer,
                action_id=args.action_id,
                next_action=args.next_action,
            )
        )
    elif args.command == "record-reflection":
        print_json(
            store.record_reflection_log(
                reflection_type=args.reflection_type,
                workflow=args.workflow,
                observation=args.observation,
                lesson=args.lesson,
                expected_behavior=args.expected_behavior,
                actor=args.actor,
                source_ids=args.source_id,
                evidence=args.evidence,
                risk=args.risk,
                confidence=args.confidence,
            )
        )
    elif args.command == "verify-reflection":
        print_json(
            store.verify_reflection(
                reflection_id=args.reflection_id,
                result=args.result,
                verifier=args.verifier,
                evidence=args.evidence,
                note=args.note,
            )
        )
    elif args.command == "review-reflection-guidance":
        print_json(
            store.review_reflection_guidance(
                guidance_item_id=args.guidance_item_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "review-context-attribution-coverage":
        print_json(
            store.review_context_attribution_coverage(
                reviewer=args.reviewer,
                window=args.window,
                minimum_source_record_ratio=args.minimum_source_record_ratio,
                note=args.note,
            )
        )
    elif args.command == "context-attribution-coverage-lifecycle":
        print_json(
            store.apply_context_attribution_coverage_lifecycle_action(
                review_id=args.review_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "propose-tool-safety-policy":
        print_json(
            store.propose_tool_safety_policy(
                guidance_item_id=args.guidance_item_id,
                policy_scope=args.policy_scope,
                proposed_rule=args.proposed_rule,
                proposer=args.proposer,
                rationale=args.rationale,
                risk=args.risk,
                confidence=args.confidence,
            )
        )
    elif args.command == "review-tool-safety-policy-proposal":
        print_json(
            store.review_tool_safety_policy_proposal(
                proposal_id=args.proposal_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "tool-safety-policy-lifecycle":
        print_json(
            store.apply_tool_safety_policy_lifecycle_action(
                proposal_id=args.proposal_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "link-tool-safety-policy-proposals":
        print_json(
            store.link_tool_safety_policy_proposals(
                from_proposal_id=args.from_proposal_id,
                to_proposal_id=args.to_proposal_id,
                link_type=args.link_type,
                reviewer=args.reviewer,
                reason=args.reason,
                evidence=args.evidence,
                confidence=args.confidence,
            )
        )
    elif args.command == "tool-safety-policy-link-lifecycle":
        print_json(
            store.apply_tool_safety_policy_link_lifecycle_action(
                link_id=args.link_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "bridge-proposal-link-claim-evidence":
        print_json(
            store.bridge_tool_safety_policy_link_to_claim_graph(
                link_id=args.link_id,
                reviewer=args.reviewer,
                rationale=args.rationale,
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
    elif args.command == "event-report":
        print_json(store.event_projection_report(retention_limit=args.retention_limit))
    elif args.command == "event-payload-diff-report":
        print_json(store.event_payload_diff_coverage_preview())
    elif args.command == "event-replayability-assessment":
        print_json(store.event_replayability_assessment())
    elif args.command == "reconstruction-evidence-schema-report":
        print_json(store.reconstruction_evidence_schema_report())
    elif args.command == "reconstruction-evidence-coverage-map":
        print_json(store.reconstruction_evidence_coverage_mapping())
    elif args.command == "reconstruction-evidence-gap-priorities":
        print_json(store.reconstruction_evidence_gap_prioritization())
    elif args.command == "reconstruction-evidence-schema-review-checklist":
        print_json(store.reconstruction_evidence_schema_review_checklist())
    elif args.command == "review-reconstruction-schema-checklist-item":
        print_json(
            store.review_reconstruction_schema_checklist_item(
                checklist_id=args.checklist_id,
                action=args.action,
                reviewer=args.reviewer,
                rationale=args.rationale,
                requested_evidence=args.requested_evidence,
                approval_scope=args.approval_scope,
            )
        )
    elif args.command == "reconstruction-schema-review-coverage-map":
        print_json(store.reconstruction_schema_review_coverage_map())
    elif args.command == "reconstruction-schema-review-evidence-requests":
        print_json(store.reconstruction_schema_review_evidence_request_tracker())
    elif args.command == "growth-semantics-rfc":
        print_json(store.growth_semantics_rfc())
    elif args.command == "growth-semantics-report":
        print_json(store.growth_semantics_report())
    elif args.command == "growth-candidate-review-rfc":
        print_json(store.growth_candidate_review_rfc())
    elif args.command == "growth-candidate-review-report":
        print_json(store.growth_candidate_review_report())
    elif args.command == "reconstruction-schema-evidence-request-lifecycle":
        print_json(
            store.apply_reconstruction_schema_evidence_request_lifecycle_action(
                request_id=args.request_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
                evidence_refs=args.evidence_ref,
            )
        )
    elif args.command == "propose-event-payload-capture-policy":
        print_json(
            store.propose_event_payload_capture_policy(
                proposer=args.proposer,
                rationale=args.rationale,
            )
        )
    elif args.command == "review-event-payload-capture-policy":
        print_json(
            store.review_event_payload_capture_policy(
                proposal_id=args.proposal_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
    elif args.command == "review-event-retention":
        print_json(
            store.review_event_retention(
                reviewer=args.reviewer,
                retention_limit=args.retention_limit,
                note=args.note,
            )
        )
    elif args.command == "event-retention-lifecycle":
        print_json(
            store.apply_event_retention_lifecycle_action(
                review_id=args.review_id,
                action=args.action,
                reviewer=args.reviewer,
                decision_note=args.decision_note,
            )
        )
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
