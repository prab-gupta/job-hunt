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


if __name__ == "__main__":
    unittest.main()
