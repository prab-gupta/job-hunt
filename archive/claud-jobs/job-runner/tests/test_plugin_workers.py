import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from plugin_workers import CommandResult, PluginError, PluginWorkers, SOURCES


class FakeRunner:
    def __init__(self, responses):
        self.responses = list(responses)
        self.calls = []

    def __call__(self, command, cwd, timeout):
        self.calls.append((list(command), cwd, timeout))
        return self.responses.pop(0)


class PluginWorkersTests(unittest.TestCase):
    def worker(self, responses, cooldowns=None):
        runner = FakeRunner(responses)
        return PluginWorkers("/skills", runner=runner, cooldowns=cooldowns), runner

    def test_source_commands_are_bounded_and_use_documented_flags(self):
        worker, _ = self.worker([])
        expectations = {
            "freehire": ("--query", "--limit"),
            "linkedin": ("--query", "--limit"),
            "jobnet": ("--search-string", "--per-page"),
            "jobindex": ("--query", "--limit"),
            "jobdanmark": ("--text", "--limit"),
            "jobbank": ("--key", "--limit"),
        }
        for source, flags in expectations.items():
            command = worker.search_command(source, "developer", "Italy", 999)
            self.assertIn(flags[0], command)
            self.assertIn(flags[1], command)
            self.assertEqual(str(SOURCES[source].result_limit), command[command.index(flags[1]) + 1])
        linkedin = worker.search_command("linkedin", "developer", "Italy", 999)
        self.assertEqual("1", linkedin[linkedin.index("--page") + 1])
        self.assertEqual("10", linkedin[linkedin.index("--limit") + 1])
        self.assertEqual("14", linkedin[linkedin.index("--jobage") + 1])
        self.assertIn("--no-description", worker.search_command("freehire", "developer"))
        freehire = worker.search_command("freehire", "developer")
        self.assertEqual("eu,none", freehire[freehire.index("--region") + 1])
        self.assertEqual("14", freehire[freehire.index("--jobage") + 1])

    def test_search_parses_and_normalizes_json(self):
        body = {"results": [{
            "id": "abc", "title": "Engineer", "company": "Acme",
            "location": "Milan", "url": "https://acme.test/job", "date": "2026-09-01",
        }]}
        worker, runner = self.worker([CommandResult(0, json.dumps(body))])
        rows = worker.search("freehire", "engineer", now=100)
        self.assertEqual("abc", rows[0]["source_id"])
        self.assertEqual("Engineer", rows[0]["role"])
        self.assertEqual("https://acme.test/job", rows[0]["direct_url"])
        self.assertEqual("json", runner.calls[0][0][-1])

    def test_cooldown_blocks_a_second_call(self):
        worker, runner = self.worker([CommandResult(0, '{"results": []}')])
        worker.search("linkedin", "engineer", "Italy", now=100)
        with self.assertRaisesRegex(PluginError, "cooldown active"):
            worker.search("linkedin", "engineer", "Italy", now=101)
        self.assertEqual(1, len(runner.calls))

    def test_failed_source_is_isolated_and_gets_cooldown(self):
        worker, _ = self.worker([
            CommandResult(1, "", '{"error":"rate limited"}'),
            CommandResult(0, '{"results": [{"id":"ok","title":"Developer"}]}'),
        ])
        result = worker.sweep([
            {"source": "linkedin", "query": "developer", "location": "Italy", "now": 100},
            {"source": "freehire", "query": "developer", "now": 100},
        ])
        self.assertFalse(result["linkedin"]["ok"])
        self.assertTrue(result["freehire"]["ok"])
        self.assertGreater(worker.cooldowns["linkedin"], 100)

    def test_health_requires_search_and_detail(self):
        worker, runner = self.worker([
            CommandResult(0, '{"results": [{"jobAdId":"uuid-1","title":"Developer"}]}'),
            CommandResult(0, '{"jobAdId":"uuid-1","description":"Full"}'),
        ])
        result = worker.health("jobnet", "udvikler")
        self.assertTrue(result["healthy"])
        self.assertIn("detail", runner.calls[1][0])
        self.assertIn("uuid-1", runner.calls[1][0])

    def test_invalid_json_fails_closed(self):
        worker, _ = self.worker([CommandResult(0, "not-json")])
        with self.assertRaisesRegex(PluginError, "invalid JSON"):
            worker.search("freehire", "developer", now=10)

    def test_unknown_source_is_isolated(self):
        worker, _ = self.worker([])
        result = worker.sweep([{"source": "missing", "query": "developer"}])
        self.assertFalse(result["missing"]["ok"])


if __name__ == "__main__":
    unittest.main()
