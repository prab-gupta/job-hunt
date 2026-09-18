#!/usr/bin/env python3
"""Deterministic Personio adapter for an exact, confirmed application manifest."""

import argparse
import json
import re
from pathlib import Path

from playwright.sync_api import sync_playwright


parser = argparse.ArgumentParser()
parser.add_argument("--manifest", required=True)
parser.add_argument("--profile", required=True)
parser.add_argument("--cv", required=True)
parser.add_argument("--letter", required=True)
parser.add_argument("--evidence-dir", required=True)
parser.add_argument("--submit", action="store_true")
args = parser.parse_args()

manifest = json.loads(Path(args.manifest).read_text())
profile = json.loads(Path(args.profile).read_text())
evidence_dir = Path(args.evidence_dir)
evidence_dir.mkdir(parents=True, exist_ok=True)
expected = manifest.get("confirmed_item", {})
if not manifest.get("released") or manifest.get("state") != "CONFIRMED":
    raise SystemExit("manifest is not released from a confirmed batch")
if expected != {"company": manifest["company"], "role": manifest["role"]}:
    raise SystemExit("manifest identity mismatch")

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=True)
    page = browser.new_page()
    application_url = manifest["direct_url"].replace("?language=", "/apply?language=")
    if application_url == manifest["direct_url"]:
        raise SystemExit("unsupported Personio URL")
    page.goto(application_url, wait_until="domcontentloaded")
    page.get_by_role("textbox", name="First", exact=True).fill(profile["first_name"])
    page.get_by_role("textbox", name="Last", exact=True).fill(profile["last_name"])
    page.get_by_role("textbox", name="Email (required)", exact=True).fill(profile["email"])
    phone = page.get_by_role("textbox", name="Phone", exact=True)
    if phone.count():
        phone.fill(profile["phone"])
    linkedin = page.get_by_role("textbox", name="LinkedIn", exact=True)
    if linkedin.count():
        linkedin.fill(profile["linkedin_url"])
    available = page.get_by_role("textbox", name="Available from (required)", exact=True)
    if available.count():
        available.fill("Immediately")
    page.get_by_role("textbox", name="Expected salary (required)", exact=True).fill(
        "EUR 30,000-40,000, negotiable"
    )
    consent = page.get_by_role("combobox", name=re.compile("talent pool", re.I))
    if consent.count():
        consent.select_option(label="No")
    page.locator("#doc-input-cv").set_input_files(args.cv)
    page.locator("#doc-input-other").set_input_files(args.letter)
    if not page.get_by_text(Path(args.cv).name, exact=False).count():
        raise SystemExit("CV filename not visible after upload")
    if not page.get_by_text(Path(args.letter).name, exact=False).count():
        raise SystemExit("cover-letter filename not visible after upload")
    if not args.submit:
        print(json.dumps({"state": "DRY_RUN", "opportunity_id": manifest["opportunity_id"]}))
    else:
        page.get_by_role("button", name="Submit Application", exact=True).click()
        page.wait_for_timeout(2000)
        body = page.locator("body").inner_text()
        success = next(
            (line.strip() for line in body.splitlines()
             if "thank" in line.lower() or "application" in line.lower() and "received" in line.lower()),
            "",
        )
        if not success:
            raise SystemExit("submit clicked but confirmation evidence absent")
        screenshot = evidence_dir / (str(manifest["opportunity_id"]) + "-personio-submitted.png")
        page.screenshot(path=str(screenshot), full_page=True)
        screenshot.chmod(0o600)
        print(json.dumps({"state": "SUBMITTED", "opportunity_id": manifest["opportunity_id"],
                          "evidence": success, "evidence_path": str(screenshot)}))
    browser.close()
