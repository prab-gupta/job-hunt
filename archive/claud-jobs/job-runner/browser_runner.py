#!/usr/bin/env python3
"""Deterministic, fail-closed browser executor for confirmed basic-form jobs.

Playwright is deliberately imported only by ``run_with_playwright`` so this
module and its policy checks can run on hosts where the browser runtime is not
installed.
"""

import argparse
import hashlib
import ipaddress
import json
import os
import re
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Mapping, Optional
from urllib.parse import urlsplit


class RunnerRejected(ValueError):
    """The manifest or form is outside the approved deterministic policy."""


@dataclass(frozen=True)
class Outcome:
    state: str
    evidence: str = ""
    evidence_path: str = ""
    error: str = ""

    def as_dict(self) -> Dict[str, str]:
        return {
            "state": self.state,
            "evidence": self.evidence,
            "evidence_path": self.evidence_path,
            "error": self.error,
        }


SAFE_PROFILE_KEYS = {
    "first_name", "last_name", "full_name", "email", "phone", "location",
    "city", "country", "linkedin_url", "website", "work_authorized",
    "requires_sponsorship",
}
UNSAFE_FIELD_WORDS = {
    "cover letter", "cover_letter", "essay", "portfolio", "assessment",
    "writing sample", "github", "personal statement", "motivation",
    "why do you", "why are you", "password", "login",
}
OPTIONAL_DEMOGRAPHIC_WORDS = {
    "gender", "race", "ethnicity", "veteran", "disability", "pronoun",
    "sexual orientation", "demographic",
}


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _origin(parts: Any) -> tuple:
    default_port = 443 if parts.scheme == "https" else None
    return parts.scheme, (parts.hostname or "").casefold(), parts.port or default_port


def _is_private_host(hostname: str) -> bool:
    host = hostname.casefold().rstrip(".")
    if host == "localhost" or host.endswith(".localhost"):
        return True
    try:
        address = ipaddress.ip_address(host)
    except ValueError:
        return False
    return not address.is_global


def validate_navigation(requested_url: str, final_url: str, local_test: bool = False) -> None:
    requested = urlsplit(requested_url)
    final = urlsplit(final_url)
    if final.scheme != "https" or not final.hostname or final.username or final.password:
        raise RunnerRejected("navigation ended at an invalid HTTPS URL")
    if _origin(final) != _origin(requested):
        raise RunnerRejected("navigation redirected outside the confirmed HTTPS origin")
    if _is_private_host(final.hostname) and not local_test:
        raise RunnerRejected("navigation to a private host is not allowed")
    if local_test and final.hostname.casefold().rstrip(".") not in {
        "localhost", "127.0.0.1", "host.containers.internal",
    }:
        raise RunnerRejected("local test navigation left the local test host")


def validate_release(manifest: Mapping[str, Any], cv_path: Path, local_test: bool = False) -> None:
    required = ("opportunity_id", "batch_id", "company", "role", "direct_url", "cv_checksum")
    missing = [key for key in required if not _clean(manifest.get(key))]
    if missing:
        raise RunnerRejected("released manifest missing: " + ", ".join(missing))
    if manifest.get("released") is not True or manifest.get("state") != "CONFIRMED":
        raise RunnerRejected("manifest was not DB-released in CONFIRMED state")
    exact = manifest.get("confirmed_item")
    if not isinstance(exact, Mapping):
        raise RunnerRejected("manifest lacks exact confirmed item")
    if _clean(exact.get("company")) != _clean(manifest["company"]):
        raise RunnerRejected("company differs from confirmed batch membership")
    if _clean(exact.get("role")) != _clean(manifest["role"]):
        raise RunnerRejected("role differs from confirmed batch membership")
    parts = urlsplit(str(manifest["direct_url"]))
    if parts.scheme != "https" or not parts.hostname or parts.username or parts.password:
        raise RunnerRejected("direct_url must be an uncredentialed HTTPS URL")
    if local_test and parts.hostname not in {"localhost", "127.0.0.1", "host.containers.internal"}:
        raise RunnerRejected("local test mode is restricted to the local test host")
    if _is_private_host(parts.hostname) and not local_test:
        raise RunnerRejected("direct_url must not target a private host")
    if not cv_path.is_file() or cv_path.suffix.casefold() != ".pdf":
        raise RunnerRejected("CV must be an existing PDF")
    if file_sha256(cv_path).casefold() != _clean(manifest["cv_checksum"]).casefold():
        raise RunnerRejected("CV checksum differs from released manifest")


def validate_profile(profile: Mapping[str, Any]) -> None:
    unknown = sorted(set(profile) - SAFE_PROFILE_KEYS)
    if unknown:
        raise RunnerRejected("profile contains unsupported fields: " + ", ".join(unknown))
    for key in ("first_name", "last_name", "email"):
        if not _clean(profile.get(key)):
            raise RunnerRejected("profile missing required value: " + key)


def classify_fields(fields: List[Mapping[str, Any]]) -> None:
    """Reject risky or unknown required fields; demographics stay untouched."""
    known = SAFE_PROFILE_KEYS | {"resume", "cv", "consent", "privacy", "terms"}
    known_labels = {token.replace("_", " ") for token in known}
    for field in fields:
        label = _clean(field.get("label") or field.get("name") or field.get("id")).casefold()
        kind = _clean(field.get("type")).casefold()
        required = bool(field.get("required"))
        if kind in {"password"} or any(word in label for word in UNSAFE_FIELD_WORDS):
            raise RunnerRejected("unsupported form field: " + (label or kind))
        if any(word in label for word in OPTIONAL_DEMOGRAPHIC_WORDS):
            if required:
                raise RunnerRejected("required demographic field: " + label)
            continue
        if required and not any(token in label for token in known_labels):
            raise RunnerRejected("unknown required field: " + (label or kind or "unnamed"))


FIELD_SELECTORS = {
    # These names cover the stable basic fields used by Greenhouse, Lever,
    # Ashby and Workable; no DOM-position or guessed-answer selectors are used.
    "first_name": ["input[name='first_name']", "input[name='firstName']", "input[name='firstname']", "#first_name"],
    "last_name": ["input[name='last_name']", "input[name='lastName']", "input[name='lastname']", "#last_name"],
    "full_name": ["input[name='name']", "input[name='full_name']", "input[name='_systemfield_name']"],
    "email": ["input[type='email']", "input[name='email']"],
    "phone": ["input[type='tel']", "input[name='phone']", "input[name='phone_number']"],
    "location": ["input[name='location']", "input[name='city']"],
    "linkedin_url": ["input[name*='linkedin' i]"],
}
UPLOAD_SELECTORS = ["input[type='file'][name*='resume' i]", "input[type='file'][name*='cv' i]", "input[type='file']"]
SUBMIT_SELECTORS = ["button[type='submit']", "input[type='submit']"]
SUCCESS_SELECTORS = ["[data-qa='application-success']", ".application-confirmation", ".thank-you", "text=/thank you|application (was )?submitted|application received/i"]


def _first_visible(page: Any, selectors: List[str]) -> Optional[Any]:
    for selector in selectors:
        locator = page.locator(selector).first
        if locator.count() and locator.is_visible():
            return locator
    return None


def _success_evidence(page: Any) -> set:
    evidence = set()
    for selector in SUCCESS_SELECTORS:
        locator = page.locator(selector).first
        if locator.count() and locator.is_visible():
            text = _clean(locator.inner_text())
            if text:
                evidence.add((selector, text))
    return evidence


def inspect_form(page: Any) -> List[Mapping[str, Any]]:
    if page.locator("iframe[src*='captcha' i], [class*='captcha' i], [id*='captcha' i]").count():
        raise RunnerRejected("CAPTCHA detected")
    return page.evaluate("""() => [...document.querySelectorAll('input,textarea,select')].map(el => ({
      name: el.name || '', id: el.id || '', type: el.type || el.tagName.toLowerCase(),
      required: !!el.required, label: (el.labels && el.labels[0] && el.labels[0].innerText) || el.getAttribute('aria-label') || el.name || el.id || ''
    }))""")


def execute_page(page: Any, manifest: Mapping[str, Any], profile: Mapping[str, Any],
                 cv_path: Path, evidence_dir: Path, dry_run: bool = False,
                 local_test: bool = False) -> Outcome:
    """Execute one already-validated page. Unknown outcomes never auto-retry."""
    clicked = False
    evidence_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(evidence_dir, 0o700)
    try:
        page.goto(manifest["direct_url"], wait_until="domcontentloaded")
        validate_navigation(manifest["direct_url"], page.url, local_test)
        classify_fields(inspect_form(page))
        for key, selectors in FIELD_SELECTORS.items():
            value = _clean(profile.get(key))
            if value:
                target = _first_visible(page, selectors)
                if target is not None:
                    target.fill(value)
        upload = _first_visible(page, UPLOAD_SELECTORS)
        if upload is None:
            raise RunnerRejected("no deterministic CV upload field")
        upload.set_input_files(str(cv_path))
        submit = _first_visible(page, SUBMIT_SELECTORS)
        if submit is None:
            raise RunnerRejected("no deterministic submit control")
        if dry_run:
            return Outcome("DRY_RUN", evidence="validated and filled; submit not clicked")
        success_before = _success_evidence(page)
        clicked = True
        submit.click()
        if hasattr(page, "wait_for_timeout"):
            page.wait_for_timeout(1000)
        new_evidence = _success_evidence(page) - success_before
        if not new_evidence:
            return Outcome("NEEDS_REVIEW", error="submit clicked but success evidence absent")
        evidence = sorted(new_evidence)[0][1]
        evidence_path = evidence_dir / (str(manifest["opportunity_id"]) + "-submitted.png")
        page.screenshot(path=str(evidence_path), full_page=True)
        os.chmod(evidence_path, 0o600)
        return Outcome("SUBMITTED", evidence=evidence, evidence_path=str(evidence_path))
    except RunnerRejected:
        raise
    except Exception as exc:  # browser/network failures need phase-aware recovery
        state = "NEEDS_REVIEW" if clicked else "RETRYABLE"
        return Outcome(state, error=str(exc))


def run_with_playwright(manifest: Mapping[str, Any], profile: Mapping[str, Any], cv_path: Path,
                        evidence_dir: Path, dry_run: bool = False, local_test: bool = False) -> Outcome:
    validate_release(manifest, cv_path, local_test)
    validate_profile(profile)
    from playwright.sync_api import sync_playwright  # imported only at execution time

    with tempfile.TemporaryDirectory(prefix="jobrunner-profile-") as profile_dir:
        with sync_playwright() as playwright:
            context = playwright.chromium.launch_persistent_context(
                profile_dir, headless=True, accept_downloads=False,
                ignore_https_errors=local_test,
            )
            try:
                page = context.pages[0] if context.pages else context.new_page()
                return execute_page(page, manifest, profile, cv_path, evidence_dir, dry_run, local_test)
            finally:
                context.close()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--profile", required=True)
    parser.add_argument("--cv", required=True)
    parser.add_argument("--evidence-dir", required=True)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--local-test", action="store_true")
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    profile = json.loads(Path(args.profile).read_text(encoding="utf-8"))
    outcome = run_with_playwright(manifest, profile, Path(args.cv), Path(args.evidence_dir), args.dry_run, args.local_test)
    print(json.dumps(outcome.as_dict(), sort_keys=True))
    return 0 if outcome.state in {"SUBMITTED", "DRY_RUN"} else 2


if __name__ == "__main__":
    raise SystemExit(main())
