#!/usr/bin/env python3
"""Exercise confirmation and the real browser container against a local HTTPS form."""

import argparse
import json
from pathlib import Path

import jobctl


parser = argparse.ArgumentParser()
parser.add_argument("--db", required=True)
parser.add_argument("--cv", required=True)
parser.add_argument("--profile", required=True)
parser.add_argument("--evidence-dir", required=True)
args = parser.parse_args()

db_path = Path(args.db)
if db_path.exists():
    db_path.unlink()
db = jobctl.connect(db_path)
try:
    jobctl.init_db(db, Path(jobctl.__file__).with_name("schema.sql"))
    target = db.execute(
        """INSERT INTO opportunities
           (company, role, direct_url, normalized_direct_url, employer_role_key, state)
           VALUES (?, ?, ?, ?, ?, 'READY')""",
        ("Controlled Test Co", "CV Upload Test",
         "https://host.containers.internal:9443/local-form.html",
         "https://host.containers.internal:9443/local-form.html",
         jobctl.employer_role_key("Controlled Test Co", "CV Upload Test")),
    ).lastrowid
    unconfirmed = db.execute(
        """INSERT INTO opportunities
           (company, role, direct_url, normalized_direct_url, employer_role_key, state)
           VALUES (?, ?, ?, ?, ?, 'READY')""",
        ("Unconfirmed Fourth Co", "Must Stay Ready", "https://jobs.example.test/fourth",
         "https://jobs.example.test/fourth",
         jobctl.employer_role_key("Unconfirmed Fourth Co", "Must Stay Ready")),
    ).lastrowid
    batch = jobctl.build_confirmation_batch(db, [target])
    jobctl.confirm_batch(db, batch["batch_id"], batch["confirmation_text"])
    before = db.execute(
        "SELECT state FROM opportunities WHERE id=?", (unconfirmed,)
    ).fetchone()[0]
    result = jobctl.submit_batch(
        db, batch["batch_id"], args.cv, args.profile, args.evidence_dir,
        "localhost/job-runner-browser:1", local_test=True,
    )
    after = db.execute(
        "SELECT state FROM opportunities WHERE id=?", (target,)
    ).fetchone()[0]
    retry_blocked = False
    try:
        jobctl.submit_batch(
            db, batch["batch_id"], args.cv, args.profile, args.evidence_dir,
            "localhost/job-runner-browser:1", local_test=True,
        )
    except ValueError:
        retry_blocked = True
    print(json.dumps({
        "batch_id": batch["batch_id"],
        "target_state": after,
        "unconfirmed_state": before,
        "retry_blocked": retry_blocked,
        "result": result,
    }, indent=2, sort_keys=True))
finally:
    db.close()
