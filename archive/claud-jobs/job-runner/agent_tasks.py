#!/usr/bin/env python3
"""Compact, deterministic task packets exchanged between the VPS and Codex.

This module deliberately contains no model client.  It only builds and validates
small JSON documents so the VPS cannot submit applications or run an AI agent.
"""

import json
import time
from typing import Any, Dict, Iterable, List, Mapping, Optional


MAX_SURVIVORS = 10
MAX_TASK_BYTES = 24_000
MAX_REQUESTS = 20

PREFLIGHT_DECISIONS = (
    "READY", "DEAD", "DUPLICATE", "LOCATION", "WORK_AUTH", "LANGUAGE",
    "DEGREE", "EXPERIENCE", "COMPENSATION", "ESSAY", "PORTFOLIO",
    "ASSESSMENT", "CAPTCHA", "STAFFING", "NEEDS_REVIEW",
)

LANES = {
    "italy_direct": {
        "priority": 1,
        "geography": "Italy",
        "sources": ["linkedin-search", "freehire-search", "direct-employer-ats"],
        "exclude": ["EU-remote-only", "EU-relocation"],
    },
    "eu_remote": {
        "priority": 2,
        "geography": "EU roles explicitly remote from Italy",
        "sources": ["freehire-search", "linkedin-search", "greenhouse", "ashby", "lever", "workable"],
        "exclude": ["Italy-onsite-or-hybrid", "relocation-required"],
    },
    "eu_relocation": {
        "priority": 3,
        "geography": "EU roles requiring or supporting relocation outside Italy",
        "sources": ["direct-employer-ats", "jobnet-search", "jobindex-search", "jobdanmark-search", "jobbank-search"],
        "exclude": ["Italy", "remote-from-Italy"],
    },
}

FORBIDDEN_PAYLOAD_KEYS = {
    "conversation", "full_conversation", "thread", "thread_history",
    "full_thread", "csv", "csv_rows", "applications_csv", "historical_rows",
}


class ValidationError(ValueError):
    """Raised when an orchestration packet violates the compact contract."""


def _compact_size(value: Mapping[str, Any]) -> int:
    return len(json.dumps(value, separators=(",", ":"), ensure_ascii=False).encode("utf-8"))


def _reject_forbidden_payload(value: Any, path: str = "$") -> None:
    if isinstance(value, Mapping):
        for key, child in value.items():
            if str(key).lower() in FORBIDDEN_PAYLOAD_KEYS:
                raise ValidationError("forbidden full-history payload key at %s.%s" % (path, key))
            _reject_forbidden_payload(child, "%s.%s" % (path, key))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            _reject_forbidden_payload(child, "%s[%d]" % (path, index))


def build_sweep_task(
    lane: str,
    run_id: str,
    profile_summary: Mapping[str, Any],
    known_opportunity_ids: Iterable[str] = (),
    request_budget: int = MAX_REQUESTS,
) -> Dict[str, Any]:
    """Return one bounded, non-overlapping search-lane task for Codex."""
    if lane not in LANES:
        raise ValidationError("unknown lane: %s" % lane)
    if not 1 <= request_budget <= MAX_REQUESTS:
        raise ValidationError("request_budget must be between 1 and %d" % MAX_REQUESTS)
    known_ids = list(known_opportunity_ids)
    if len(known_ids) > 200:
        raise ValidationError("known_opportunity_ids is capped at 200")
    packet = {
        "schema_version": 1,
        "task_type": "sweep",
        "run_id": run_id,
        "agent": {"lane": lane, "fork_turns": "none"},
        "scope": dict(LANES[lane]),
        "profile_summary": dict(profile_summary),
        "known_opportunity_ids": known_ids,
        "limits": {
            "max_survivors": MAX_SURVIVORS,
            "max_requests": request_budget,
            "max_output_tokens": 2000,
            "open_application_forms": False,
            "submit_applications": False,
        },
        "output": {"format": "json", "schema": "sweep-output.schema.json"},
    }
    validate_task_packet(packet)
    return packet


def build_preflight_task(run_id: str, opportunities: Iterable[Mapping[str, Any]]) -> Dict[str, Any]:
    items = [dict(item) for item in opportunities]
    if not 1 <= len(items) <= 10:
        raise ValidationError("preflight batch must contain 1 to 10 opportunities")
    packet = {
        "schema_version": 1,
        "task_type": "preflight",
        "run_id": run_id,
        "agent": {"role": "preflight_reviewer", "fork_turns": "none"},
        "opportunities": items,
        "checks": [
            "posting_live", "location_eligibility", "work_authorization",
            "language", "degree", "experience", "compensation",
            "required_fields", "cv_basic_only",
        ],
        "limits": {"max_requests": MAX_REQUESTS, "max_output_tokens": 2000, "enter_personal_data": False},
        "output": {"format": "json", "schema": "preflight-output.schema.json"},
    }
    validate_task_packet(packet)
    return packet


def build_review_escalation(run_id: str, preflight: Mapping[str, Any]) -> Dict[str, Any]:
    validate_preflight_result(preflight)
    if preflight["decision"] != "NEEDS_REVIEW":
        raise ValidationError("only NEEDS_REVIEW decisions may be escalated")
    packet = {
        "schema_version": 1,
        "task_type": "needs_review",
        "run_id": run_id,
        "agent": {"role": "coordinator", "fork_turns": "none"},
        "opportunity_id": preflight["opportunity_id"],
        "ambiguity": preflight.get("reason", ""),
        "possible_blockers": preflight.get("blockers", []),
        "limits": {"max_requests": 3, "max_output_tokens": 1000, "may_release_submission": False},
        "output": {"format": "json", "schema": "preflight-output.schema.json"},
    }
    validate_task_packet(packet)
    return packet


def validate_task_packet(packet: Mapping[str, Any]) -> None:
    _reject_forbidden_payload(packet)
    task_type = packet.get("task_type")
    required_flags = {
        "sweep": {"open_application_forms": False, "submit_applications": False},
        "preflight": {"enter_personal_data": False},
        "needs_review": {"may_release_submission": False},
    }
    if task_type not in required_flags:
        raise ValidationError("unknown task_type")
    if packet.get("schema_version") != 1 or not str(packet.get("run_id", "")).strip():
        raise ValidationError("task packet requires schema_version=1 and run_id")
    if packet.get("agent", {}).get("fork_turns") != "none":
        raise ValidationError("all agent packets require fork_turns=none")
    limits = packet.get("limits", {})
    if not isinstance(limits, Mapping):
        raise ValidationError("limits must be an object")
    for flag, safe_value in required_flags[task_type].items():
        if limits.get(flag) is not safe_value:
            raise ValidationError("unsafe or missing task limit: %s" % flag)
    if limits.get("max_requests", 0) > MAX_REQUESTS:
        raise ValidationError("request budget exceeds maximum")
    if limits.get("max_output_tokens", 0) > 2000:
        raise ValidationError("output token cap exceeds 2000")
    if _compact_size(packet) > MAX_TASK_BYTES:
        raise ValidationError("task packet exceeds compact payload limit")


def validate_sweep_output(output: Mapping[str, Any]) -> None:
    allowed_fit = {"high", "medium", "low"}
    required = {"opportunity_id", "company", "role", "direct_url", "location", "source_plugin", "fit", "possible_blockers", "verified_at"}
    survivors = output.get("survivors")
    if not isinstance(survivors, list):
        raise ValidationError("survivors must be a list")
    if len(survivors) > MAX_SURVIVORS:
        raise ValidationError("sweep output exceeds survivor cap")
    for index, item in enumerate(survivors):
        if not isinstance(item, Mapping) or set(item) != required:
            raise ValidationError("survivor %d does not match the output schema" % index)
        for key in required - {"possible_blockers"}:
            if not isinstance(item[key], str) or not item[key].strip():
                raise ValidationError("survivor %d has invalid %s" % (index, key))
        if item["fit"] not in allowed_fit:
            raise ValidationError("survivor %d has invalid fit" % index)
        if not isinstance(item["possible_blockers"], list) or not all(isinstance(v, str) for v in item["possible_blockers"]):
            raise ValidationError("survivor %d has invalid blockers" % index)


def validate_preflight_result(result: Mapping[str, Any]) -> None:
    required = {"opportunity_id", "decision", "required_fields", "blockers", "verified_at"}
    if not required.issubset(result):
        raise ValidationError("preflight result is missing required fields")
    if result["decision"] not in PREFLIGHT_DECISIONS:
        raise ValidationError("invalid preflight decision")
    if not isinstance(result["required_fields"], list) or not isinstance(result["blockers"], list):
        raise ValidationError("required_fields and blockers must be lists")


def metrics_envelope(run_id: str, task_type: str, started_at: float, input_tokens: int, output_tokens: int, status: str = "completed") -> Dict[str, Any]:
    """Create the small metrics record stored in the runs table by jobctl."""
    return {
        "schema_version": 1,
        "run_id": run_id,
        "task_type": task_type,
        "status": status,
        "elapsed_ms": max(0, round((time.time() - started_at) * 1000)),
        "tokens": {"input": max(0, input_tokens), "output": max(0, output_tokens), "total": max(0, input_tokens) + max(0, output_tokens)},
    }
