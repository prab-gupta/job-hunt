#!/usr/bin/env python3
"""Dedupe, status rules, and three-path sync for the tracker MCP server."""

from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SERVER_PATH = Path(__file__).with_name("server.py")
SPEC = importlib.util.spec_from_file_location("tracker_server", SERVER_PATH)
server = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(server)


def seed(root: Path) -> None:
    header = ",".join(server.tracker.HEADER)
    row = "Acme,AI Engineer,https://example.com/jobs/1/?lang=en,test,needs_you,80,2026-10-02,,,n8n role,login"
    text = header + "\n" + row + "\n"
    for rel in server.CSV_REL:
        path = root / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    (root / "docs").mkdir(parents=True, exist_ok=True)


class TrackerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        seed(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_dedupe_strips_language_query_and_rejects_duplicate(self) -> None:
        left = server.tracker.dedupe_key({"url": "https://Example.com/jobs/1/?language=en"})
        right = server.tracker.dedupe_key({"url": "https://example.com/jobs/1"})
        self.assertEqual(left, right)
        with self.assertRaises(server.TrackerError) as caught:
            server.add_row(
                {
                    "company": "Other",
                    "role": "Other",
                    "url": "https://example.com/jobs/1",
                    "source": "test",
                    "status": "needs_you",
                    "blocker": "login",
                    "date_added": "2026-10-02",
                },
                root=self.root,
            )
        self.assertIn("duplicate", str(caught.exception))
        self.assertEqual(server.stats(self.root)["rows"], 1)

    def test_submitted_requires_auditor_and_gmail_note(self) -> None:
        with self.assertRaises(server.TrackerError):
            server.update_row(
                match_url="https://example.com/jobs/1",
                patch={"status": "submitted", "date_applied": "2026-10-02", "notes": "thanks page"},
                actor="needs-you-drainer",
                root=self.root,
            )
        with self.assertRaises(server.TrackerError):
            server.update_row(
                match_url="https://example.com/jobs/1",
                patch={"status": "submitted", "date_applied": "2026-10-02", "notes": "thanks page"},
                actor="apply-auditor",
                root=self.root,
            )
        result = server.update_row(
            match_url="https://example.com/jobs/1?language=en",
            patch={
                "status": "submitted",
                "date_applied": "2026-10-02",
                "notes": "gmail: Application received @ 2026-10-02T12:00:00Z",
                "blocker": "",
            },
            actor="apply-auditor",
            root=self.root,
        )
        self.assertEqual(result["status"], "submitted")
        with self.assertRaises(server.TrackerError):
            server.update_row(
                match_url="https://example.com/jobs/1",
                patch={"status": "needs_you", "blocker": "login", "notes": "again"},
                actor="needs-you-drainer",
                root=self.root,
            )

    def test_skipped_is_not_reapplied(self) -> None:
        server.update_row(
            match_url="https://example.com/jobs/1",
            patch={"status": "skipped", "blocker": "closed", "notes": "page says closed"},
            actor="tracker-keeper",
            root=self.root,
        )
        with self.assertRaises(server.TrackerError):
            server.update_row(
                match_url="https://example.com/jobs/1",
                patch={"status": "needs_you", "blocker": "login"},
                actor="needs-you-drainer",
                root=self.root,
            )

    def test_sync_paths_hashes_match(self) -> None:
        server.add_row(
            {
                "company": "Beta",
                "role": "PM",
                "url": "https://beta.example/jobs/9",
                "source": "test",
                "status": "needs_you",
                "blocker": "other",
                "date_added": "2026-10-02",
                "notes": "open posting",
            },
            root=self.root,
        )
        hashes = server.sync_paths(self.root)
        self.assertEqual(len(set(hashes["paths"].values())), 1)
        bodies = [(self.root / rel).read_bytes() for rel in server.CSV_REL]
        self.assertEqual(bodies[0], bodies[1])
        self.assertEqual(bodies[0], bodies[2])
        self.assertIn("Beta", bodies[0].decode())

    def test_secret_is_not_written(self) -> None:
        before = (self.root / "applications.csv").read_bytes()
        with self.assertRaises(server.TrackerError):
            server.add_row(
                {
                    "company": "Gamma",
                    "role": "SE",
                    "url": "https://gamma.example/j/1",
                    "status": "needs_you",
                    "blocker": "login",
                    "notes": "pass" + "word=example",
                },
                root=self.root,
            )
        self.assertEqual((self.root / "applications.csv").read_bytes(), before)

    def test_next_needs_you_claims_once(self) -> None:
        first = server.next_needs_you("drainer-a", root=self.root)
        second = server.next_needs_you("drainer-b", root=self.root)
        again = server.next_needs_you("drainer-a", root=self.root)
        self.assertEqual(first["row"]["company"], "Acme")
        self.assertIsNone(second["row"])
        self.assertTrue(again["already_held"])
        self.assertEqual(again["row"]["company"], "Acme")
        server.release_claim("drainer-a", root=self.root)
        released = server.next_needs_you("drainer-b", root=self.root)
        self.assertEqual(released["row"]["company"], "Acme")

    def test_stdio_lists_tools(self) -> None:
        proc = subprocess.Popen(
            [sys.executable, str(SERVER_PATH)],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env={**os.environ, "TRACKER_ROOT": str(self.root)},
        )
        payload = "\n".join(
            [
                json.dumps(
                    {
                        "jsonrpc": "2.0",
                        "id": 1,
                        "method": "initialize",
                        "params": {"protocolVersion": "2024-11-05"},
                    }
                ),
                json.dumps({"jsonrpc": "2.0", "method": "notifications/initialized"}),
                json.dumps({"jsonrpc": "2.0", "id": 2, "method": "tools/list"}),
            ]
        ) + "\n"
        stdout, stderr = proc.communicate(payload, timeout=10)
        self.assertEqual(proc.returncode, 0, stderr)
        lines = [json.loads(line) for line in stdout.splitlines() if line.strip()]
        names = [tool["name"] for tool in lines[1]["result"]["tools"]]
        self.assertIn("sync_paths", names)
        self.assertIn("add_row", names)
        self.assertIn("next_needs_you", names)


def _add(root: Path, company: str, role: str, url: str, blocker: str, notes: str) -> None:
    server.add_row(
        {
            "company": company,
            "role": role,
            "url": url,
            "source": "test",
            "status": "needs_you",
            "blocker": blocker,
            "date_added": "2026-10-04",
            "notes": notes,
        },
        root=root,
    )


class ParkedAndAttemptedTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        seed(self.root)
        # Acme (seeded, login) is claimable. Park a question row ahead of a clean one.
        _add(self.root, "Parky", "AI Eng", "https://parky.example/j/1", "other",
             "parked 2026-10-02: required yes/no question, unanswered, needs user")
        _add(self.root, "Cleanco", "AI Eng", "https://cleanco.example/j/2", "other", "open posting")

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_parked_question_rows_are_not_in_autonomous_queue(self) -> None:
        for note in (
            "parked: required question",
            "needs user: street address",
            "user-only question: anti-AI essay",
            "unanswered criminal-convictions question",
            "missing fact: nationality",
        ):
            self.assertTrue(server.tracker.is_parked({"notes": note}), note)
            self.assertTrue(server.tracker.human_line({"blocker": "other", "notes": note}), note)
        self.assertFalse(server.tracker.is_parked({"notes": "open posting"}))
        seen = []
        for _ in range(5):
            got = server.next_needs_you("agent-q", root=self.root)
            if got["row"] is None:
                break
            seen.append(got["row"]["company"])
            server.release_claim("agent-q", root=self.root)
        self.assertNotIn("Parky", seen)
        self.assertEqual(sorted(seen), ["Acme", "Cleanco"])

    def test_released_row_is_not_reclaimed_in_same_session(self) -> None:
        first = server.next_needs_you("agent-r", root=self.root)
        server.release_claim("agent-r", root=self.root)
        second = server.next_needs_you("agent-r", root=self.root)
        self.assertNotEqual(first["row"]["company"], second["row"]["company"])
        server.release_claim("agent-r", root=self.root)
        third = server.next_needs_you("agent-r", root=self.root)
        server.release_claim("agent-r", root=self.root)
        self.assertNotIn(third["row"] and third["row"]["company"], {first["row"]["company"], second["row"]["company"]})
        self.assertIsNone(third["row"])
        # Another agent is not blocked by agent-r's attempts, and include_attempted overrides.
        other = server.next_needs_you("agent-s", root=self.root)
        self.assertEqual(other["row"]["company"], first["row"]["company"])
        server.release_claim("agent-s", root=self.root)
        again = server.next_needs_you("agent-r", root=self.root, include_attempted=True)
        self.assertEqual(again["row"]["company"], first["row"]["company"])

    def test_view_you_column_flags_parked_row(self) -> None:
        text = (self.root / "docs/needs-you.md").read_text(encoding="utf-8")
        line = next(line for line in text.splitlines() if "Parky" in line)
        self.assertIn("parked question", line)


class StatusContractTests(unittest.TestCase):
    def test_confirmed_label_is_never_submitted(self) -> None:
        plan = server.tracker.plan_change(
            [], {"company": "A", "role": "B", "url": "https://a.example/1", "status": "confirmed"}, "insert"
        )
        self.assertEqual(plan["action"], "insert")
        self.assertEqual(plan["row"]["status"], "needs_you")
        self.assertEqual(plan["row"]["blocker"], "no_confirm")
        self.assertIn("unconfirmed", plan["row"]["notes"])

    def test_fallback_blocker_is_in_vocabulary(self) -> None:
        plan = server.tracker.plan_change(
            [], {"company": "A", "role": "B", "url": "https://a.example/2", "status": "mystery"}, "insert"
        )
        self.assertIn(plan["row"]["blocker"], server.tracker.BLOCKER_TYPES)


class UrlNormalizationTests(unittest.TestCase):
    def key(self, url: str):
        return server.tracker.dedupe_key({"url": url})

    def test_job_identifying_params_are_kept(self) -> None:
        self.assertNotEqual(self.key("https://x.example/jobs?gh_jid=1"), self.key("https://x.example/jobs?gh_jid=2"))
        self.assertNotEqual(self.key("https://x.example/jobs?jid=1"), self.key("https://x.example/jobs?jid=2"))
        self.assertNotEqual(self.key("https://x.example/careers?id=1"), self.key("https://x.example/careers?id=2"))
        self.assertNotEqual(self.key("https://x.example/c?job=1"), self.key("https://x.example/c?job=2"))
        self.assertNotEqual(self.key("https://x.example/c?requisition=1"), self.key("https://x.example/c?requisition=2"))
        self.assertNotEqual(self.key("https://x.example/c?ashby_jid=a"), self.key("https://x.example/c?ashby_jid=b"))
        self.assertNotEqual(self.key("https://it.indeed.com/viewjob?jk=a"), self.key("https://it.indeed.com/viewjob?jk=b"))

    def test_tracking_and_language_params_are_stripped(self) -> None:
        base = self.key("https://x.example/jobs/9")
        for suffix in (
            "?language=en", "?lang=it", "?utm_source=a&utm_medium=b", "?ref=li", "?source=x", "?locale=en_US",
            "?gclid=1&fbclid=2", "/?utm_campaign=z#apply",
        ):
            self.assertEqual(self.key("https://x.example/jobs/9" + suffix), base, suffix)

    def test_mixed_params_keep_only_job_id_and_ignore_order(self) -> None:
        a = self.key("https://x.example/jobs?utm_source=a&gh_jid=7&lang=en")
        b = self.key("https://X.example/jobs/?gh_jid=7&ref=z")
        self.assertEqual(a, b)
        self.assertEqual(a, ("url", "https://x.example/jobs?gh_jid=7"))


if __name__ == "__main__":
    unittest.main()
