import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import direct_ats


class DirectATSTest(unittest.TestCase):
    def test_discovers_supported_boards_once(self):
        urls = [
            "https://job-boards.greenhouse.io/acme/jobs/1",
            "https://job-boards.greenhouse.io/acme/jobs/2",
            "https://jobs.lever.co/beta/abc",
            "https://example.test/job",
        ]
        self.assertEqual(
            [("greenhouse", "acme"), ("lever", "beta")],
            direct_ats.discover_boards(urls),
        )

    def test_poll_is_bounded_normalized_and_failure_isolated(self):
        urls = [
            "https://job-boards.greenhouse.io/acme/jobs/1",
            "https://jobs.lever.co/beta/abc",
        ]
        def fetch(url):
            if "greenhouse" in url:
                return {"jobs": [{"id": 2, "title": "Engineer", "absolute_url": "https://job-boards.greenhouse.io/acme/jobs/2", "location": {"name": "Italy"}}]}
            raise RuntimeError("blocked")
        result = direct_ats.poll(urls, fetch=fetch, jobs_per_board=1)
        self.assertEqual(2, result["boards"])
        self.assertEqual("direct-greenhouse", result["results"][0]["source"])
        self.assertEqual("Italy", result["results"][0]["location"])
        self.assertEqual(1, len(result["errors"]))


if __name__ == "__main__":
    unittest.main()
