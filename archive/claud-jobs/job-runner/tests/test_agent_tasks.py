import json
import sys
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import agent_tasks as tasks


class AgentTaskTests(unittest.TestCase):
    def test_three_lanes_are_bounded_and_non_overlapping(self):
        packets = [tasks.build_sweep_task(lane, "run-1", {"roles": ["developer"]}) for lane in tasks.LANES]
        self.assertEqual({p["agent"]["lane"] for p in packets}, set(tasks.LANES))
        self.assertTrue(all(p["agent"]["fork_turns"] == "none" for p in packets))
        self.assertTrue(all(p["limits"]["max_survivors"] == 10 for p in packets))
        self.assertTrue(all(p["limits"]["max_requests"] == 20 for p in packets))
        self.assertEqual(len({p["scope"]["geography"] for p in packets}), 3)

    def test_full_thread_and_csv_payloads_are_rejected(self):
        for forbidden in ("thread_history", "applications_csv", "csv_rows"):
            with self.assertRaises(tasks.ValidationError):
                tasks.build_sweep_task("italy_direct", "run", {forbidden: "large secret payload"})

    def test_task_and_output_caps_are_enforced(self):
        with self.assertRaises(tasks.ValidationError):
            tasks.build_sweep_task("italy_direct", "run", {}, request_budget=21)
        survivor = {
            "opportunity_id": "id", "company": "Company", "role": "Role",
            "direct_url": "https://example.test/job", "location": "Italy",
            "source_plugin": "freehire-search", "fit": "medium",
            "possible_blockers": [], "verified_at": "2026-09-01T00:00:00Z",
        }
        tasks.validate_sweep_output({"survivors": [dict(survivor, opportunity_id=str(i)) for i in range(10)]})
        with self.assertRaises(tasks.ValidationError):
            tasks.validate_sweep_output({"survivors": [dict(survivor, opportunity_id=str(i)) for i in range(11)]})

    def test_safety_flags_are_required_and_cannot_be_enabled(self):
        packet = tasks.build_sweep_task("italy_direct", "run-safe", {"skills": ["python"]})
        for flag in ("open_application_forms", "submit_applications"):
            unsafe = json.loads(json.dumps(packet))
            unsafe["limits"][flag] = True
            with self.assertRaises(tasks.ValidationError):
                tasks.validate_task_packet(unsafe)
            missing = json.loads(json.dumps(packet))
            del missing["limits"][flag]
            with self.assertRaises(tasks.ValidationError):
                tasks.validate_task_packet(missing)

    def test_preflight_enum_and_needs_review_escalation(self):
        result = {
            "opportunity_id": "opp-1", "decision": "NEEDS_REVIEW",
            "required_fields": ["cv"], "blockers": ["ambiguous work authorization"],
            "verified_at": "2026-09-01T00:00:00Z", "reason": "legal wording is unclear",
        }
        tasks.validate_preflight_result(result)
        escalation = tasks.build_review_escalation("run-2", result)
        self.assertEqual(escalation["task_type"], "needs_review")
        self.assertFalse(escalation["limits"]["may_release_submission"])
        with self.assertRaises(tasks.ValidationError):
            tasks.validate_preflight_result(dict(result, decision="MAYBE"))
        with self.assertRaises(tasks.ValidationError):
            tasks.build_review_escalation("run-2", dict(result, decision="READY"))

    def test_preflight_packet_is_small_and_contains_no_personal_data_action(self):
        packet = tasks.build_preflight_task("run-3", [{"opportunity_id": "opp-1", "direct_url": "https://example.test/job"}])
        self.assertLess(len(json.dumps(packet).encode()), tasks.MAX_TASK_BYTES)
        self.assertFalse(packet["limits"]["enter_personal_data"])
        self.assertEqual(packet["agent"]["fork_turns"], "none")

    def test_metrics_envelope_records_elapsed_and_token_totals(self):
        metrics = tasks.metrics_envelope("run-4", "sweep", time.time() - 0.01, 120, 30)
        self.assertGreaterEqual(metrics["elapsed_ms"], 1)
        self.assertEqual(metrics["tokens"]["total"], 150)


if __name__ == "__main__":
    unittest.main()
