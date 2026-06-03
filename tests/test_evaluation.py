import unittest

from one_core.evaluation import run_foundation_evaluation, run_scenario_evaluation


class FoundationEvaluationTests(unittest.TestCase):
    def test_foundation_evaluation_passes(self):
        report = run_foundation_evaluation()
        self.assertEqual(report["suite"], "foundation")
        self.assertEqual(report["state_mode"], "temporary")
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed"], 0)
        self.assertGreaterEqual(report["passed"], 7)

        check_names = {check["name"] for check in report["checks"]}
        self.assertIn("state_invariants", check_names)
        self.assertIn("continuity_anchors", check_names)
        self.assertIn("dry_run_is_non_mutating", check_names)
        self.assertIn("adapter_event_deduplication", check_names)
        self.assertIn("identity_overwrite_is_gated", check_names)
        self.assertIn(
            "false_memory_injection_is_quarantined_or_not_promoted",
            check_names,
        )
        self.assertIn(
            "preference_change_creates_candidate_not_stale_overwrite",
            check_names,
        )

    def test_scenario_evaluation_passes(self):
        report = run_scenario_evaluation()
        self.assertEqual(report["suite"], "scenarios")
        self.assertEqual(report["state_mode"], "temporary")
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["failed"], 0)
        self.assertEqual(report["passed"], 16)
        self.assertEqual(
            report["baselines"]["system_under_test"],
            "state_transfer_system",
        )
        self.assertEqual(
            report["baselines"]["baseline_execution"],
            "deterministic_local_v0.9",
        )
        self.assertIn(
            "retrieval_only_baseline",
            report["baselines"]["tracked_baselines"],
        )
        self.assertIn("results", report["baselines"])
        self.assertIn("comparisons", report["baselines"])
        baseline_results = report["baselines"]["results"]
        comparisons = report["baselines"]["comparisons"]
        for baseline_name in (
            "stateless_baseline",
            "retrieval_only_baseline",
            "summary_only_baseline",
        ):
            self.assertIn(baseline_name, baseline_results)
            self.assertEqual(
                baseline_results[baseline_name]["execution"],
                "deterministic_rule_baseline",
            )
            self.assertIn(baseline_name, comparisons)
            self.assertTrue(comparisons[baseline_name]["state_transfer_outperforms"])
            self.assertGreater(comparisons[baseline_name]["delta"], 0)

        scenario_names = {scenario["name"] for scenario in report["scenarios"]}
        self.assertIn("interrupted_project_resume", scenario_names)
        self.assertIn("multi_user_boundary", scenario_names)
        self.assertIn("lifecycle_retrieval_suppression", scenario_names)
        self.assertIn("claim_graph_conflict_provenance", scenario_names)
        self.assertIn("claim_graph_review_patch_preview", scenario_names)
        self.assertIn("task_hub_action_resume", scenario_names)
        self.assertIn("procedural_memory_review", scenario_names)
        self.assertIn("failure_reflection", scenario_names)
        self.assertIn("cautionary_procedural_review", scenario_names)
        self.assertIn("cautionary_warning_lifecycle", scenario_names)
        self.assertIn("reflection_log_verification", scenario_names)
        self.assertIn("procedural_lifecycle_retention", scenario_names)
        self.assertIn("identity_update_gate_review", scenario_names)
        self.assertIn("event_log_replay_rollback", scenario_names)
        self.assertIn("dream_artifact_package", scenario_names)
        self.assertIn("context_builder_policy_trace", scenario_names)

        metrics = report["metrics_summary"]
        self.assertEqual(metrics["total_scenarios"], 16)
        self.assertEqual(metrics["failed_scenarios"], 0)
        self.assertEqual(metrics["boundary_violation_count"], 0)
        self.assertEqual(metrics["archived_memory_retrieval_count"], 0)
        self.assertGreaterEqual(metrics["claim_count"], 1)
        self.assertEqual(metrics["unreviewed_memory_mutation_count"], 0)
        self.assertEqual(metrics["task_resume_score"], 1.0)
        self.assertEqual(metrics["task_hub_resume_score"], 1.0)
        self.assertGreaterEqual(metrics["procedural_candidate_count"], 1)
        self.assertEqual(metrics["procedural_review_score"], 1.0)
        self.assertGreaterEqual(metrics["procedural_memory_count"], 1)
        self.assertGreaterEqual(metrics["procedural_review_decision_count"], 1)
        self.assertEqual(metrics["procedural_identity_mutation_count"], 0)
        self.assertEqual(metrics["failure_reflection_score"], 1.0)
        self.assertGreaterEqual(metrics["failure_reflection_count"], 1)
        self.assertGreaterEqual(metrics["failure_caution_count"], 1)
        self.assertEqual(metrics["failure_identity_mutation_count"], 0)
        self.assertEqual(metrics["cautionary_review_score"], 1.0)
        self.assertGreaterEqual(metrics["cautionary_warning_count"], 1)
        self.assertGreaterEqual(metrics["cautionary_review_decision_count"], 1)
        self.assertEqual(metrics["cautionary_executable_policy_count"], 0)
        self.assertGreaterEqual(metrics["cautionary_active_context_count"], 1)
        self.assertEqual(metrics["cautionary_identity_mutation_count"], 0)
        self.assertEqual(metrics["cautionary_lifecycle_score"], 1.0)
        self.assertGreaterEqual(metrics["cautionary_lifecycle_decision_count"], 1)
        self.assertGreaterEqual(metrics["cautionary_archived_count"], 1)
        self.assertEqual(metrics["cautionary_lifecycle_active_context_count"], 0)
        self.assertEqual(metrics["cautionary_lifecycle_executable_policy_count"], 0)
        self.assertEqual(metrics["cautionary_lifecycle_identity_mutation_count"], 0)
        self.assertEqual(metrics["reflection_log_score"], 1.0)
        self.assertGreaterEqual(metrics["reflection_log_count"], 1)
        self.assertGreaterEqual(metrics["reflection_verified_count"], 1)
        self.assertGreaterEqual(metrics["reflection_policy_guidance_count"], 1)
        self.assertGreaterEqual(
            metrics["reflection_policy_guidance_verified_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reflection_policy_guidance_high_priority_count"],
            1,
        )
        self.assertGreaterEqual(metrics["reflection_guidance_queue_count"], 1)
        self.assertGreaterEqual(
            metrics["reflection_guidance_review_decision_count"],
            1,
        )
        self.assertEqual(metrics["reflection_guidance_executable_policy_count"], 0)
        self.assertGreaterEqual(metrics["tool_safety_policy_proposal_count"], 1)
        self.assertGreaterEqual(
            metrics["tool_safety_policy_review_decision_count"],
            1,
        )
        self.assertEqual(metrics["tool_safety_policy_executable_policy_count"], 0)
        self.assertGreaterEqual(metrics["tool_safety_policy_score_count"], 1)
        self.assertGreater(metrics["tool_safety_policy_max_priority_score"], 0)
        self.assertGreater(metrics["tool_safety_policy_max_evidence_strength"], 0)
        self.assertGreater(metrics["tool_safety_policy_max_scope_specificity"], 0)
        self.assertGreaterEqual(metrics["tool_safety_policy_max_staleness"], 0)
        self.assertGreaterEqual(metrics["tool_safety_policy_link_count"], 1)
        self.assertGreaterEqual(
            metrics["tool_safety_policy_supersession_link_count"],
            1,
        )
        self.assertEqual(metrics["tool_safety_policy_link_executable_policy_count"], 0)
        self.assertGreaterEqual(
            metrics["tool_safety_policy_link_lifecycle_decision_count"],
            1,
        )
        self.assertGreaterEqual(metrics["tool_safety_policy_link_archived_count"], 1)
        self.assertEqual(metrics["tool_safety_policy_link_active_context_count"], 0)
        self.assertEqual(
            metrics["tool_safety_policy_link_lifecycle_executable_policy_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["proposal_link_claim_graph_evidence_count"],
            1,
        )
        self.assertGreaterEqual(metrics["proposal_link_claim_graph_link_count"], 1)
        self.assertEqual(metrics["proposal_link_claim_graph_claim_mutation_count"], 0)
        self.assertEqual(
            metrics["proposal_link_claim_graph_executable_policy_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["tool_safety_policy_lifecycle_decision_count"],
            1,
        )
        self.assertGreaterEqual(metrics["tool_safety_policy_archived_count"], 1)
        self.assertGreaterEqual(metrics["tool_safety_policy_active_context_count"], 1)
        self.assertEqual(
            metrics["tool_safety_policy_lifecycle_executable_policy_count"],
            0,
        )
        self.assertEqual(metrics["reflection_identity_mutation_count"], 0)
        self.assertEqual(metrics["procedural_lifecycle_score"], 1.0)
        self.assertGreaterEqual(metrics["procedural_lifecycle_decision_count"], 1)
        self.assertGreaterEqual(metrics["procedural_archived_count"], 1)
        self.assertEqual(metrics["procedural_active_context_count"], 0)
        self.assertEqual(metrics["identity_gate_score"], 1.0)
        self.assertEqual(metrics["approved_identity_updates"], 1)
        self.assertEqual(metrics["identity_core_mutation_count"], 0)
        self.assertEqual(metrics["identity_gate_quarantine_count"], 1)
        self.assertEqual(metrics["event_log_replay_score"], 1.0)
        self.assertGreaterEqual(metrics["event_count"], 5)
        self.assertGreaterEqual(metrics["event_coverage_count"], 5)
        self.assertGreaterEqual(metrics["event_projection_count"], 5)
        self.assertEqual(metrics["event_projection_gap_count"], 0)
        self.assertGreaterEqual(metrics["event_projection_checked_path_count"], 1)
        self.assertGreaterEqual(metrics["event_projection_matched_path_count"], 1)
        self.assertGreaterEqual(metrics["event_projection_consistent_path_count"], 1)
        self.assertEqual(metrics["event_projection_mismatch_count"], 0)
        self.assertEqual(metrics["event_report_count"], 1)
        self.assertGreaterEqual(metrics["event_report_coverage_gap_count"], 1)
        self.assertGreaterEqual(metrics["event_report_retention_excess_count"], 1)
        self.assertEqual(metrics["event_payload_report_count"], 1)
        self.assertGreaterEqual(
            metrics["event_payload_transition_reference_count"],
            metrics["event_payload_report_event_count"],
        )
        self.assertGreaterEqual(metrics["event_payload_hint_count"], 1)
        self.assertGreaterEqual(metrics["event_payload_gap_count"], 1)
        self.assertEqual(metrics["event_diff_ready_count"], 0)
        self.assertGreaterEqual(metrics["event_diff_gap_count"], 1)
        self.assertEqual(metrics["event_payload_high_risk_count"], 0)
        self.assertEqual(metrics["event_payload_safe_compaction_count"], 0)
        self.assertEqual(metrics["event_payload_state_mutation_count"], 0)
        self.assertEqual(metrics["event_replayability_assessment_count"], 1)
        self.assertEqual(metrics["event_replayability_ready_count"], 1)
        self.assertEqual(
            metrics["event_replayability_object_reconstruction_ready_count"],
            0,
        )
        self.assertEqual(
            metrics["event_replayability_full_state_reconstruction_ready_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["event_replayability_missing_capability_count"],
            1,
        )
        self.assertGreaterEqual(metrics["event_replayability_payload_gap_count"], 1)
        self.assertGreaterEqual(metrics["event_replayability_diff_gap_count"], 1)
        self.assertEqual(metrics["event_replayability_state_mutation_count"], 0)
        self.assertEqual(metrics["event_replayability_execution_count"], 0)
        self.assertEqual(metrics["reconstruction_evidence_schema_report_count"], 1)
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_schema_section_count"],
            4,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_missing_requirement_count"],
            3,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_target_path_requirement_count"],
            1,
        )
        self.assertEqual(metrics["reconstruction_evidence_schema_mutation_count"], 0)
        self.assertEqual(metrics["reconstruction_evidence_capture_execution_count"], 0)
        self.assertEqual(
            metrics["reconstruction_evidence_reconstruction_execution_count"],
            0,
        )
        self.assertEqual(metrics["reconstruction_evidence_state_mutation_count"], 0)
        self.assertEqual(metrics["reconstruction_evidence_coverage_mapping_count"], 1)
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_coverage_workflow_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_coverage_workflow_gap_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_coverage_section_count"],
            4,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_coverage_schema_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_coverage_capture_execution_count"],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_evidence_coverage_reconstruction_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_coverage_state_mutation_count"],
            0,
        )
        self.assertEqual(metrics["reconstruction_evidence_gap_prioritization_count"], 1)
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_prioritized_workflow_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_max_priority_score"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_priority_schema_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_priority_capture_execution_count"],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_evidence_priority_reconstruction_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_priority_state_mutation_count"],
            0,
        )
        self.assertEqual(metrics["reconstruction_evidence_schema_checklist_count"], 1)
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_schema_checklist_item_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_schema_checklist_question_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_evidence_schema_checklist_acceptance_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics[
                "reconstruction_evidence_schema_checklist_required_evidence_count"
            ],
            1,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_schema_checklist_schema_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_evidence_schema_checklist_capture_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_evidence_schema_checklist_reconstruction_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_schema_checklist_identity_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_evidence_schema_checklist_state_mutation_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_decision_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_more_evidence_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_context_signal_count"],
            1,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_schema_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_capture_execution_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_reconstruction_execution_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_identity_mutation_count"],
            0,
        )
        self.assertEqual(metrics["reconstruction_schema_review_compaction_count"], 0)
        self.assertEqual(
            metrics["reconstruction_schema_review_events_modified_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_replay_after_count"],
            1,
        )
        self.assertEqual(metrics["reconstruction_schema_review_coverage_map_count"], 1)
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_coverage_reviewed_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_coverage_unreviewed_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_coverage_max_ratio"],
            0,
        )
        self.assertGreaterEqual(
            metrics[
                "reconstruction_schema_review_coverage_evidence_requested_count"
            ],
            1,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_coverage_schema_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_coverage_capture_execution_count"],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_coverage_reconstruction_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_coverage_identity_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_coverage_state_mutation_count"],
            0,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_evidence_request_tracker_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_evidence_request_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_open_evidence_request_count"],
            1,
        )
        self.assertEqual(
            metrics["reconstruction_schema_review_satisfied_evidence_request_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["reconstruction_schema_review_evidence_request_decision_count"],
            1,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_evidence_request_schema_mutation_count"
            ],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_evidence_request_capture_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_evidence_request_reconstruction_execution_count"
            ],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_evidence_request_identity_mutation_count"
            ],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_evidence_request_events_modified_count"
            ],
            0,
        )
        self.assertEqual(
            metrics[
                "reconstruction_schema_review_evidence_request_state_mutation_count"
            ],
            0,
        )
        self.assertGreaterEqual(
            metrics["event_payload_capture_policy_proposal_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["event_payload_capture_policy_decision_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["event_payload_capture_policy_approved_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["event_payload_capture_policy_context_count"],
            1,
        )
        self.assertEqual(
            metrics["event_payload_capture_policy_schema_mutation_count"],
            0,
        )
        self.assertEqual(metrics["event_payload_capture_policy_execution_count"], 0)
        self.assertEqual(metrics["event_payload_capture_policy_compaction_count"], 0)
        self.assertEqual(
            metrics["event_payload_capture_policy_events_modified_count"],
            0,
        )
        self.assertEqual(metrics["event_payload_capture_policy_replay_after_count"], 1)
        self.assertGreaterEqual(metrics["event_retention_review_count"], 1)
        self.assertGreaterEqual(
            metrics["event_retention_lifecycle_decision_count"],
            1,
        )
        self.assertGreaterEqual(metrics["event_retention_archived_count"], 1)
        self.assertEqual(metrics["event_retention_active_context_count"], 0)
        self.assertEqual(metrics["event_retention_compaction_count"], 0)
        self.assertEqual(metrics["event_retention_events_modified_count"], 0)
        self.assertEqual(metrics["event_retention_replay_after_count"], 1)
        self.assertEqual(metrics["rollback_preview_count"], 1)
        self.assertGreaterEqual(metrics["rollback_affected_path_count"], 1)
        self.assertGreaterEqual(metrics["rollback_projected_impact_count"], 1)
        self.assertEqual(metrics["rollback_mutation_count"], 0)
        self.assertEqual(metrics["dream_artifact_package_score"], 1.0)
        self.assertGreaterEqual(metrics["dream_artifact_count"], 1)
        self.assertGreaterEqual(metrics["dream_review_queue_count"], 1)
        self.assertEqual(metrics["dream_package_validation_failures"], 0)
        self.assertEqual(metrics["claim_review_score"], 1.0)
        self.assertGreaterEqual(metrics["claim_link_count"], 2)
        self.assertGreaterEqual(metrics["claim_review_decision_count"], 1)
        self.assertEqual(metrics["claim_patch_mutation_count"], 0)
        self.assertEqual(metrics["context_builder_score"], 1.0)
        self.assertGreaterEqual(metrics["context_activation_trace_count"], 1)
        self.assertGreaterEqual(metrics["context_signal_count"], 1)
        self.assertGreaterEqual(metrics["context_governance_signal_count"], 1)
        self.assertGreaterEqual(metrics["context_signal_attribution_count"], 1)
        self.assertGreaterEqual(
            metrics["context_attribution_coverage_review_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["context_attribution_coverage_signal_selected_count"],
            1,
        )
        self.assertEqual(
            metrics["context_attribution_coverage_executable_policy_count"],
            0,
        )
        self.assertGreaterEqual(
            metrics["context_attribution_coverage_lifecycle_decision_count"],
            1,
        )
        self.assertGreaterEqual(
            metrics["context_attribution_coverage_archived_count"],
            1,
        )
        self.assertEqual(
            metrics["context_attribution_coverage_lifecycle_active_context_count"],
            0,
        )
        self.assertEqual(
            metrics[
                "context_attribution_coverage_lifecycle_executable_policy_count"
            ],
            0,
        )


if __name__ == "__main__":
    unittest.main()
