"""Bounded, fail-closed adapters for the installed Bun job-search skills."""

from __future__ import annotations

import json
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Sequence


class PluginError(RuntimeError):
    """A single portal failed; callers should continue with other portals."""


@dataclass(frozen=True)
class SourceConfig:
    name: str
    cli_dir: str
    query_flag: str
    location_flag: Optional[str] = None
    limit_flag: str = "--limit"
    page_flag: Optional[str] = "--page"
    result_limit: int = 10
    cooldown_seconds: int = 6 * 60 * 60
    id_fields: Sequence[str] = ("id",)


SOURCES: Dict[str, SourceConfig] = {
    "freehire": SourceConfig(
        "freehire", "freehire-search", "--query", result_limit=25,
        id_fields=("id", "slug"),
    ),
    "linkedin": SourceConfig(
        "linkedin", "linkedin-search", "--query", "--location",
        result_limit=10, id_fields=("id", "jobId", "job_id"),
    ),
    "jobnet": SourceConfig(
        "jobnet", "jobnet-search", "--search-string",
        limit_flag="--per-page", result_limit=10,
        id_fields=("jobAdId", "id"), cooldown_seconds=7 * 24 * 60 * 60,
    ),
    "jobindex": SourceConfig(
        "jobindex", "jobindex-search", "--query", result_limit=10,
        id_fields=("id",), cooldown_seconds=7 * 24 * 60 * 60,
    ),
    "jobdanmark": SourceConfig(
        "jobdanmark", "jobdanmark-search", "--text", result_limit=10,
        id_fields=("slug", "id"), cooldown_seconds=7 * 24 * 60 * 60,
    ),
    "jobbank": SourceConfig(
        "jobbank", "jobbank-search", "--key", page_flag=None,
        result_limit=10, id_fields=("id",), cooldown_seconds=7 * 24 * 60 * 60,
    ),
}


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str = ""


Runner = Callable[[Sequence[str], str, int], CommandResult]


def subprocess_runner(command: Sequence[str], cwd: str, timeout: int) -> CommandResult:
    """Run one CLI without a shell, with a deadline and a small output ceiling."""
    try:
        result = subprocess.run(
            list(command), cwd=cwd, stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
            timeout=timeout, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise PluginError(str(exc)) from exc
    max_output = 2 * 1024 * 1024
    if len(result.stdout.encode("utf-8")) > max_output or len(result.stderr.encode("utf-8")) > max_output:
        raise PluginError("plugin output exceeded 2 MiB")
    return CommandResult(result.returncode, result.stdout, result.stderr)


class PluginWorkers:
    def __init__(
        self,
        skills_root: str,
        bun: str = "/opt/job-runner/bin/bun",
        runner: Runner = subprocess_runner,
        timeout_seconds: int = 45,
        cooldowns: Optional[Dict[str, float]] = None,
    ) -> None:
        self.skills_root = Path(skills_root)
        self.bun = bun
        self.runner = runner
        self.timeout_seconds = timeout_seconds
        self.cooldowns = cooldowns if cooldowns is not None else {}

    def _cli(self, config: SourceConfig) -> Path:
        return self.skills_root / config.cli_dir / "cli"

    def _run_json(self, config: SourceConfig, args: Sequence[str]) -> Any:
        cwd = self._cli(config)
        command = [self.bun, "run", "src/cli.ts", *args, "--format", "json"]
        result = self.runner(command, str(cwd), self.timeout_seconds)
        if result.returncode:
            message = result.stderr.strip() or result.stdout.strip() or "unknown plugin failure"
            raise PluginError(f"{config.name}: {message[:500]}")
        try:
            return json.loads(result.stdout)
        except (TypeError, json.JSONDecodeError) as exc:
            raise PluginError(f"{config.name}: invalid JSON") from exc

    def search_command(
        self, source: str, query: str, location: Optional[str] = None,
        limit: Optional[int] = None,
    ) -> List[str]:
        config = SOURCES[source]
        safe_limit = min(max(1, limit or config.result_limit), config.result_limit)
        args = ["search", config.query_flag, query]
        if config.location_flag:
            if not location:
                raise ValueError(f"{source} requires location")
            args.extend([config.location_flag, location])
        if config.page_flag:
            args.extend([config.page_flag, "1"])
        args.extend([config.limit_flag, str(safe_limit)])
        if source == "freehire":
            args.extend(["--no-description", "--region", "eu,none", "--jobage", "14"])
        if source == "linkedin":
            args.extend(["--jobage", "14"])
        if source == "jobindex":
            args.extend(["--jobage", "7", "--sort", "date"])
        return args

    def search(
        self, source: str, query: str, location: Optional[str] = None,
        limit: Optional[int] = None, now: Optional[float] = None,
        force: bool = False,
    ) -> List[Dict[str, Any]]:
        config = SOURCES[source]
        timestamp = time.time() if now is None else now
        if not force and timestamp < self.cooldowns.get(source, 0):
            raise PluginError(f"{source}: cooldown active")
        try:
            payload = self._run_json(config, self.search_command(source, query, location, limit))
        finally:
            self.cooldowns[source] = timestamp + config.cooldown_seconds
        rows = payload.get("results", []) if isinstance(payload, dict) else payload
        if not isinstance(rows, list):
            raise PluginError(f"{source}: JSON results must be a list")
        maximum = min(limit or config.result_limit, config.result_limit)
        return [self._normalize(source, row) for row in rows[:maximum] if isinstance(row, dict)]

    def detail(self, source: str, identifier: str) -> Mapping[str, Any]:
        config = SOURCES[source]
        payload = self._run_json(config, ["detail", str(identifier)])
        if not isinstance(payload, dict):
            raise PluginError(f"{source}: detail JSON must be an object")
        return payload

    def health(self, source: str, query: str, location: Optional[str] = None) -> Dict[str, Any]:
        """One sentinel search plus one detail fetch; never disguises a partial pass."""
        results = self.search(source, query, location, limit=1, force=True)
        if not results or not results[0]["source_id"]:
            raise PluginError(f"{source}: sentinel search returned no detail identifier")
        detail = self.detail(source, results[0]["source_id"])
        return {"source": source, "healthy": True, "search_count": len(results), "detail": detail}

    def sweep(self, requests: Iterable[Mapping[str, Any]]) -> Dict[str, Dict[str, Any]]:
        """Isolate portal failures so one outage cannot abort the sweep."""
        outcome: Dict[str, Dict[str, Any]] = {}
        for request in requests:
            source = str(request.get("source", "unknown"))
            try:
                rows = self.search(
                    source, str(request["query"]), request.get("location"),
                    request.get("limit"), request.get("now"),
                )
                outcome[source] = {"ok": True, "results": rows}
            except (KeyError, ValueError, PluginError) as exc:
                outcome[source] = {"ok": False, "error": str(exc), "results": []}
        return outcome

    @staticmethod
    def _normalize(source: str, row: Mapping[str, Any]) -> Dict[str, Any]:
        config = SOURCES[source]
        identifier = next((row.get(field) for field in config.id_fields if row.get(field)), None)
        company = row.get("company") or row.get("companyName") or row.get("employer") or row.get("hiringOrganization")
        if isinstance(company, dict):
            company = company.get("name")
        location = row.get("location") or row.get("jobLocation") or row.get("city")
        if isinstance(location, dict):
            location = location.get("name") or location.get("address")
        return {
            "source": source,
            "source_id": str(identifier) if identifier is not None else None,
            "company": company,
            "role": row.get("title") or row.get("jobTitle") or row.get("position"),
            "direct_url": row.get("applyUrl") or row.get("applicationUrl") or row.get("url") or row.get("link"),
            "location": location,
            "posted_at": row.get("date") or row.get("postedAt") or row.get("datePosted"),
            "raw": dict(row),
        }
