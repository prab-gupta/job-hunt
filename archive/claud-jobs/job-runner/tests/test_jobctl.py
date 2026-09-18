import csv
import os
import sqlite3
import subprocess
import tempfile
import time
import unittest
from pathlib import Path
from unittest.mock import patch

import jobctl


class JobctlTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.db_path = self.root / "test.db"
        self.db = jobctl.connect(self.db_path)
        self.addCleanup(self.db.close)
        jobctl.init_db(self.db, Path(jobctl.__file__).with_name("schema.sql"))

    def write_csv(self):
        path = self.root / "applications.csv"
        with path.open("w", newline="", encoding="utf-8") as handle:
            writer = csv.writer(handle)
            writer.writerow(jobctl.FIELDS)
            writer.writerow(["2026-08-01", "Acme", "Engineer", "Greenhouse",
                             "https://example.com/job?utm_source=x", "LEAD", "", "", "", "line 1\nline 2"])
            writer.writerow(["2026-08-02", "Acme", "Engineer", "Greenhouse",
                             "https://example.com/job", "SUBMITTED", "Success", "", "no", "done"])
            writer.writerow(["", "No URL", "QA", "", "", "BLOCKED", "", "", "", ""])
        return path

    def test_idempotent_import_dedup_and_round_trip(self):
        source = self.write_csv()
        first = jobctl.import_csv(self.db, source)
        second = jobctl.import_csv(self.db, source)
        self.assertEqual(first["source_rows_read"], 3)
        self.assertEqual(first["canonical_opportunities"], 2)
        self.assertEqual(second["created"], 0)
        self.assertEqual(jobctl.status(self.db)["source_rows"], 3)
        output = self.root / "export.csv"
        self.assertEqual(jobctl.export_csv(self.db, output)["exported_rows"], 3)
        with output.open(newline="", encoding="utf-8") as handle:
            rows = list(csv.DictReader(handle))
        self.assertEqual(rows[0]["notes"], "line 1\nline 2")

    def test_transition_guards(self):
        source = self.write_csv()
        jobctl.import_csv(self.db, source)
        opportunity_id = self.db.execute(
            "SELECT id FROM opportunities WHERE company='No URL'"
        ).fetchone()[0]
        with self.assertRaises(ValueError):
            jobctl.transition(self.db, opportunity_id, "SUBMITTING")
        self.db.execute("UPDATE opportunities SET state='CONFIRMED' WHERE id=?", (opportunity_id,))
        with self.assertRaises(sqlite3.IntegrityError):
            jobctl.transition(self.db, opportunity_id, "SUBMITTING")

    def test_confirmed_submission_requires_batch_and_evidence(self):
        cursor = self.db.execute(
            """INSERT INTO opportunities
               (company, role, employer_role_key) VALUES ('Test Co', 'Tester', 'test-co-tester')"""
        )
        opportunity_id = cursor.lastrowid
        for state in ("PREFLIGHTING", "READY", "AWAITING_CONFIRMATION", "CONFIRMED"):
            jobctl.transition(self.db, opportunity_id, state)
        with self.assertRaises(sqlite3.IntegrityError):
            jobctl.transition(self.db, opportunity_id, "SUBMITTING")
        self.db.execute(
            "INSERT INTO confirmation_batches (id, confirmation_text, confirmed_at) VALUES ('batch-1', 'confirm Test Co', '2026-09-01')"
        )
        self.db.execute(
            "INSERT INTO confirmation_batch_items VALUES ('batch-1', ?, 'Test Co', 'Tester')",
            (opportunity_id,),
        )
        jobctl.transition(self.db, opportunity_id, "SUBMITTING")
        with self.assertRaises(sqlite3.IntegrityError):
            jobctl.transition(self.db, opportunity_id, "SUBMITTED")
        self.db.execute(
            """INSERT INTO applications
               (opportunity_id, batch_id, final_state, confirmation_evidence)
               VALUES (?, 'batch-1', 'SUBMITTED', 'Application received')""",
            (opportunity_id,),
        )
        jobctl.transition(self.db, opportunity_id, "SUBMITTED")
        state = self.db.execute(
            "SELECT state FROM opportunities WHERE id=?", (opportunity_id,)
        ).fetchone()[0]
        self.assertEqual(state, "SUBMITTED")

    def insert_ready(self, company="Exact Co", role="Engineer", url="https://jobs.example.test/1"):
        cursor = self.db.execute(
            """INSERT INTO opportunities
               (company, role, direct_url, normalized_direct_url, employer_role_key, state)
               VALUES (?, ?, ?, ?, ?, 'READY')""",
            (company, role, url, url, jobctl.employer_role_key(company, role)),
        )
        return cursor.lastrowid

    def test_discovery_urls_wait_for_direct_ats_resolution(self):
        result = jobctl.store_candidates(self.db, [
            {"company": "From LinkedIn", "role": "QA", "direct_url": "https://www.linkedin.com/jobs/view/1", "source": "linkedin"},
            {"company": "Direct Co", "role": "QA", "direct_url": "https://jobs.example.test/2", "source": "direct-greenhouse"},
        ])
        self.assertEqual(2, result["created"])
        linked = self.db.execute("SELECT discovery_url,direct_url FROM opportunities WHERE company='From LinkedIn'").fetchone()
        self.assertTrue(linked["discovery_url"])
        self.assertEqual("", linked["direct_url"])
        queue = jobctl.preflight_queue(self.db, 10)
        self.assertEqual(["Direct Co"], [item["company"] for item in queue["opportunities"]])

    def test_exact_confirmation_and_manifest_release(self):
        opportunity_id = self.insert_ready()
        fourth = self.insert_ready("Fourth Co", "Other", "https://jobs.example.test/4")
        batch = jobctl.build_confirmation_batch(self.db, [opportunity_id])
        with self.assertRaises(ValueError):
            jobctl.confirm_batch(self.db, "missing", "confirm Exact Co")
        with self.assertRaises(ValueError):
            jobctl.confirm_batch(self.db, batch["batch_id"], "confirm Exact Co — Engineer")
        jobctl.confirm_batch(self.db, batch["batch_id"], batch["confirmation_text"])
        self.assertEqual("READY", self.db.execute("SELECT state FROM opportunities WHERE id=?", (fourth,)).fetchone()[0])
        cv = self.root / "Prabhavit_CV.pdf"
        cv.write_bytes(b"unchanged")
        released = jobctl.release_manifests(self.db, batch["batch_id"], cv, self.root / "manifests")
        manifest = __import__("json").loads(Path(released["manifests"][0]).read_text())
        self.assertEqual({"company": "Exact Co", "role": "Engineer"}, manifest["confirmed_item"])
        self.assertTrue(manifest["released"])

    def test_dry_run_does_not_change_confirmed_state(self):
        opportunity_id = self.insert_ready()
        batch = jobctl.build_confirmation_batch(self.db, [opportunity_id])
        jobctl.confirm_batch(self.db, batch["batch_id"], batch["confirmation_text"])
        cv = self.root / "Prabhavit_CV.pdf"; cv.write_bytes(b"unchanged")
        profile = self.root / "profile.json"; profile.write_text('{"first_name":"P"}')
        with patch.object(jobctl, "_run_browser_container", return_value={"state": "DRY_RUN", "evidence": "filled"}):
            result = jobctl.submit_batch(self.db, batch["batch_id"], cv, profile, self.root / "evidence", "image", True)
        self.assertEqual("DRY_RUN", result["results"][0]["state"])
        self.assertEqual("CONFIRMED", self.db.execute("SELECT state FROM opportunities WHERE id=?", (opportunity_id,)).fetchone()[0])

    def test_uncertain_post_click_outcome_never_resubmits(self):
        opportunity_id = self.insert_ready()
        batch = jobctl.build_confirmation_batch(self.db, [opportunity_id])
        jobctl.confirm_batch(self.db, batch["batch_id"], batch["confirmation_text"])
        cv = self.root / "Prabhavit_CV.pdf"; cv.write_bytes(b"unchanged")
        profile = self.root / "profile.json"; profile.write_text('{"first_name":"P"}')
        with patch.object(jobctl, "_run_browser_container", return_value={"state": "NEEDS_REVIEW", "error": "clicked; no evidence"}):
            jobctl.submit_batch(self.db, batch["batch_id"], cv, profile, self.root / "evidence", "image", False)
        self.assertEqual("NEEDS_REVIEW", self.db.execute("SELECT state FROM opportunities WHERE id=?", (opportunity_id,)).fetchone()[0])
        with self.assertRaises(ValueError):
            jobctl.submit_batch(self.db, batch["batch_id"], cv, profile, self.root / "evidence", "image", False)

    def test_browser_command_keeps_security_option_and_uses_minimal_environment(self):
        completed = type("Completed", (), {"stdout": '{"state":"DRY_RUN"}\n', "stderr": "", "returncode": 0})()
        with patch.object(jobctl.subprocess, "run", return_value=completed) as run:
            jobctl._run_browser_container(
                self.root / "manifest.json", self.root / "profile.json",
                self.root / "cv.pdf", self.root / "evidence",
                "localhost/job-runner-browser:1", True, True,
            )
        command = run.call_args.args[0]
        security = command.index("--security-opt")
        self.assertEqual("label=disable", command[security + 1])
        self.assertIn("host.containers.internal:host-gateway", command)
        self.assertEqual({"HOME", "PATH", "XDG_RUNTIME_DIR"}, set(run.call_args.kwargs["env"]))

    def test_browser_launch_failures_never_become_retryable(self):
        for failure in (
            subprocess.TimeoutExpired(["podman"], 180),
            OSError("podman unavailable"),
        ):
            with self.subTest(failure=type(failure).__name__), patch.object(
                jobctl.subprocess, "run", side_effect=failure
            ):
                outcome = jobctl._run_browser_container(
                    self.root / "manifest.json", self.root / "profile.json",
                    self.root / "cv.pdf", self.root / "evidence",
                    "localhost/job-runner-browser:1", True, True,
                )
                self.assertEqual("NEEDS_REVIEW", outcome["state"])

        completed = type("Completed", (), {"stdout": "", "stderr": "failed", "returncode": 125})()
        with patch.object(jobctl.subprocess, "run", return_value=completed):
            outcome = jobctl._run_browser_container(
                self.root / "manifest.json", self.root / "profile.json",
                self.root / "cv.pdf", self.root / "evidence",
                "localhost/job-runner-browser:1", True, True,
            )
        self.assertEqual("NEEDS_REVIEW", outcome["state"])

    def test_production_browser_image_is_allowlisted(self):
        with self.assertRaises(ValueError):
            jobctl._run_browser_container(
                self.root / "manifest.json", self.root / "profile.json",
                self.root / "cv.pdf", self.root / "evidence",
                "attacker.example/browser:latest", False, False,
            )

    def test_submitted_requires_fresh_evidence_inside_root(self):
        opportunity_id = self.insert_ready()
        batch = jobctl.build_confirmation_batch(self.db, [opportunity_id])
        jobctl.confirm_batch(self.db, batch["batch_id"], batch["confirmation_text"])
        cv = self.root / "Prabhavit_CV.pdf"; cv.write_bytes(b"unchanged")
        profile = self.root / "profile.json"; profile.write_text('{"first_name":"P"}')
        evidence_root = self.root / "evidence"
        evidence_root.mkdir()
        stale = evidence_root / "stale.png"
        stale.write_bytes(b"old")
        os.utime(stale, (1, 1))
        forged = {"state": "SUBMITTED", "evidence": "Application received", "evidence_path": str(stale)}
        with patch.object(jobctl, "_run_browser_container", return_value=forged):
            result = jobctl.submit_batch(
                self.db, batch["batch_id"], cv, profile, evidence_root,
                "localhost/job-runner-browser:1", False,
            )
        self.assertEqual("NEEDS_REVIEW", result["results"][0]["state"])
        self.assertEqual("NEEDS_REVIEW", self.db.execute(
            "SELECT state FROM opportunities WHERE id=?", (opportunity_id,)
        ).fetchone()[0])

    def test_partial_batch_resume_releases_only_remaining_confirmed_member(self):
        first = self.insert_ready("First Co", "Engineer", "https://jobs.example.test/first")
        second = self.insert_ready("Second Co", "Engineer", "https://jobs.example.test/second")
        batch = jobctl.build_confirmation_batch(self.db, [first, second])
        jobctl.confirm_batch(self.db, batch["batch_id"], batch["confirmation_text"])
        self.db.execute("UPDATE opportunities SET state='NEEDS_REVIEW' WHERE id=?", (first,))
        cv = self.root / "Prabhavit_CV.pdf"; cv.write_bytes(b"unchanged")
        released = jobctl.release_manifests(self.db, batch["batch_id"], cv, self.root / "manifests")
        self.assertEqual(1, len(released["manifests"]))
        manifest = __import__("json").loads(Path(released["manifests"][0]).read_text())
        self.assertEqual(second, manifest["opportunity_id"])
        self.assertEqual({"company": "Second Co", "role": "Engineer"}, manifest["confirmed_item"])

    def test_agent_sweep_output_is_validated_and_ingested(self):
        survivor = {
            "opportunity_id": "agent-1", "company": "Agent Co", "role": "QA",
            "direct_url": "https://jobs.example.test/agent-1", "location": "Italy",
            "source_plugin": "direct_greenhouse", "fit": "high",
            "possible_blockers": [], "verified_at": "2026-09-02T00:00:00Z",
        }
        result = jobctl.record_sweep_output(self.db, {"survivors": [survivor]}, "italy_direct")
        self.assertEqual(1, result["created"])
        row = self.db.execute("SELECT source,fit,state FROM opportunities WHERE company='Agent Co'").fetchone()
        self.assertEqual(("direct_greenhouse", "high", "NEW"), tuple(row))
        bad = dict(survivor)
        bad["fit"] = "perfect"
        with self.assertRaises(ValueError):
            jobctl.record_sweep_output(self.db, {"survivors": [bad]}, "italy_direct")


if __name__ == "__main__":
    unittest.main()
