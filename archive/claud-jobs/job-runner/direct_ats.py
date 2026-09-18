"""Bounded polling of employer ATS boards already present in the tracker."""

import json
from typing import Any, Callable, Dict, Iterable, List, Mapping, Optional, Tuple
from urllib.parse import quote, urlsplit
from urllib.request import Request, urlopen


FetchJSON = Callable[[str], Any]


def fetch_json(url: str) -> Any:
    request = Request(url, headers={"User-Agent": "job-runner/1.0"})
    with urlopen(request, timeout=20) as response:
        if response.status != 200:
            raise RuntimeError("ATS returned HTTP %s" % response.status)
        return json.load(response)


def board_from_url(url: str) -> Optional[Tuple[str, str]]:
    """Return (ATS, tenant) only for known public employer-board URL shapes."""
    parts = urlsplit(url)
    segments = [segment for segment in parts.path.split("/") if segment]
    host = (parts.hostname or "").casefold()
    if host in {"job-boards.greenhouse.io", "boards.greenhouse.io", "job-boards.eu.greenhouse.io"} and segments:
        return "greenhouse", segments[0]
    if host == "jobs.lever.co" and segments:
        return "lever", segments[0]
    if host == "jobs.ashbyhq.com" and segments:
        return "ashby", segments[0]
    return None


def endpoint(ats: str, tenant: str) -> str:
    tenant = quote(tenant, safe="")
    if ats == "greenhouse":
        return "https://boards-api.greenhouse.io/v1/boards/%s/jobs?content=true" % tenant
    if ats == "lever":
        return "https://api.lever.co/v0/postings/%s?mode=json" % tenant
    if ats == "ashby":
        return "https://api.ashbyhq.com/posting-api/job-board/%s" % tenant
    raise ValueError("unsupported ATS: %s" % ats)


def discover_boards(urls: Iterable[str], limit: int = 12) -> List[Tuple[str, str]]:
    boards = []
    seen = set()
    for url in urls:
        board = board_from_url(url)
        if board and board not in seen:
            boards.append(board)
            seen.add(board)
            if len(boards) == limit:
                break
    return boards


def _rows(ats: str, payload: Any) -> List[Mapping[str, Any]]:
    if ats == "greenhouse":
        value = payload.get("jobs", []) if isinstance(payload, dict) else []
    elif ats == "ashby":
        value = payload.get("jobs", []) if isinstance(payload, dict) else []
    else:
        value = payload if isinstance(payload, list) else []
    return [row for row in value if isinstance(row, Mapping)]


def normalize(ats: str, tenant: str, row: Mapping[str, Any]) -> Optional[Dict[str, Any]]:
    company = row.get("company") or row.get("companyName") or tenant
    role = row.get("title") or row.get("text")
    direct_url = row.get("absolute_url") or row.get("hostedUrl") or row.get("jobUrl") or row.get("applyUrl")
    if not role or not direct_url or urlsplit(str(direct_url)).scheme != "https":
        return None
    categories = row.get("categories") if isinstance(row.get("categories"), Mapping) else {}
    location = row.get("location") or categories.get("location") or row.get("locationName")
    if isinstance(location, Mapping):
        location = location.get("name")
    return {
        "source": "direct-%s" % ats,
        "source_id": str(row.get("id") or row.get("jobId") or direct_url),
        "company": str(company),
        "role": str(role),
        "direct_url": str(direct_url),
        "location": str(location or ""),
        "posted_at": row.get("created_at") or row.get("createdAt") or row.get("publishedAt"),
        "raw": dict(row),
    }


def poll(urls: Iterable[str], fetch: FetchJSON = fetch_json, board_limit: int = 12,
         jobs_per_board: int = 30) -> Dict[str, Any]:
    results, errors = [], []
    boards = discover_boards(urls, board_limit)
    for ats, tenant in boards:
        try:
            payload = fetch(endpoint(ats, tenant))
            for row in _rows(ats, payload)[:jobs_per_board]:
                item = normalize(ats, tenant, row)
                if item:
                    results.append(item)
        except (OSError, RuntimeError, ValueError, json.JSONDecodeError) as exc:
            errors.append({"source": "direct-%s" % ats, "tenant": tenant, "error": str(exc)[:500]})
    return {"boards": len(boards), "results": results, "errors": errors}
