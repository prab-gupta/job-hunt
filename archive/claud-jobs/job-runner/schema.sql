PRAGMA journal_mode = WAL;
PRAGMA foreign_keys = ON;
PRAGMA busy_timeout = 5000;

CREATE TABLE IF NOT EXISTS opportunities (
    id INTEGER PRIMARY KEY,
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    ats TEXT NOT NULL DEFAULT '',
    discovery_url TEXT NOT NULL DEFAULT '',
    direct_url TEXT NOT NULL DEFAULT '',
    normalized_direct_url TEXT,
    employer_role_key TEXT NOT NULL,
    source TEXT NOT NULL DEFAULT 'legacy-csv',
    location TEXT NOT NULL DEFAULT '',
    compensation TEXT NOT NULL DEFAULT '',
    fit TEXT CHECK (fit IN ('high', 'medium', 'low') OR fit IS NULL),
    state TEXT NOT NULL DEFAULT 'NEW' CHECK (state IN (
        'NEW', 'PREFLIGHTING', 'READY', 'AWAITING_CONFIRMATION',
        'CONFIRMED', 'SUBMITTING', 'SUBMITTED', 'DROPPED', 'BLOCKED',
        'DEAD', 'NEEDS_REVIEW'
    )),
    legacy_status TEXT NOT NULL DEFAULT '',
    source_id TEXT NOT NULL DEFAULT '',
    description TEXT NOT NULL DEFAULT '',
    verified_at TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX IF NOT EXISTS opportunities_direct_url_uq
ON opportunities(normalized_direct_url)
WHERE normalized_direct_url IS NOT NULL;

CREATE UNIQUE INDEX IF NOT EXISTS opportunities_employer_role_uq
ON opportunities(employer_role_key);

-- The source ledger stays separate so deduplication never destroys historical rows.
CREATE TABLE IF NOT EXISTS source_rows (
    id INTEGER PRIMARY KEY,
    source_file TEXT NOT NULL,
    row_number INTEGER NOT NULL,
    row_fingerprint TEXT NOT NULL,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id),
    date TEXT NOT NULL DEFAULT '',
    company TEXT NOT NULL DEFAULT '',
    role TEXT NOT NULL DEFAULT '',
    ats TEXT NOT NULL DEFAULT '',
    url TEXT NOT NULL DEFAULT '',
    status TEXT NOT NULL DEFAULT '',
    confirmation_text TEXT NOT NULL DEFAULT '',
    salary_stated TEXT NOT NULL DEFAULT '',
    cover_letter_attached TEXT NOT NULL DEFAULT '',
    notes TEXT NOT NULL DEFAULT '',
    imported_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    UNIQUE(source_file, row_number)
);

CREATE TABLE IF NOT EXISTS preflights (
    id INTEGER PRIMARY KEY,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id),
    decision TEXT NOT NULL CHECK (decision IN (
        'READY', 'DEAD', 'DUPLICATE', 'LOCATION', 'WORK_AUTH', 'LANGUAGE',
        'DEGREE', 'EXPERIENCE', 'COMPENSATION', 'ESSAY', 'PORTFOLIO',
        'ASSESSMENT', 'CAPTCHA', 'STAFFING', 'NEEDS_REVIEW'
    )),
    required_fields_json TEXT NOT NULL DEFAULT '[]',
    blockers_json TEXT NOT NULL DEFAULT '[]',
    verified_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS confirmation_batches (
    id TEXT PRIMARY KEY,
    confirmation_text TEXT NOT NULL DEFAULT '',
    confirmed_at TEXT,
    created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS confirmation_batch_items (
    batch_id TEXT NOT NULL REFERENCES confirmation_batches(id),
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id),
    company TEXT NOT NULL,
    role TEXT NOT NULL,
    PRIMARY KEY (batch_id, opportunity_id)
);

CREATE INDEX IF NOT EXISTS confirmation_batch_items_opportunity_idx
ON confirmation_batch_items(opportunity_id, batch_id);

CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY,
    opportunity_id INTEGER NOT NULL REFERENCES opportunities(id),
    batch_id TEXT REFERENCES confirmation_batches(id),
    attempted_at TEXT,
    final_state TEXT NOT NULL CHECK (final_state IN (
        'CONFIRMED', 'SUBMITTING', 'SUBMITTED', 'BLOCKED', 'NEEDS_REVIEW'
    )),
    confirmation_evidence TEXT NOT NULL DEFAULT '',
    evidence_path TEXT NOT NULL DEFAULT '',
    cv_checksum TEXT NOT NULL DEFAULT '',
    UNIQUE(opportunity_id, final_state)
);

CREATE TABLE IF NOT EXISTS runs (
    id INTEGER PRIMARY KEY,
    kind TEXT NOT NULL,
    started_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finished_at TEXT,
    input_count INTEGER NOT NULL DEFAULT 0,
    output_count INTEGER NOT NULL DEFAULT 0,
    error_count INTEGER NOT NULL DEFAULT 0,
    elapsed_ms INTEGER,
    token_count INTEGER,
    details_json TEXT NOT NULL DEFAULT '{}'
);

CREATE TRIGGER IF NOT EXISTS opportunity_submitting_requires_confirmation
BEFORE UPDATE OF state ON opportunities
WHEN NEW.state = 'SUBMITTING'
BEGIN
    SELECT CASE WHEN NOT EXISTS (
        SELECT 1
        FROM confirmation_batch_items i
        JOIN confirmation_batches b ON b.id = i.batch_id
        WHERE i.opportunity_id = NEW.id AND b.confirmed_at IS NOT NULL
    ) THEN RAISE(ABORT, 'SUBMITTING requires confirmed batch membership') END;
END;

CREATE TRIGGER IF NOT EXISTS opportunity_insert_cannot_skip_submission_guards
BEFORE INSERT ON opportunities
WHEN NEW.state IN ('SUBMITTING', 'SUBMITTED')
BEGIN
    SELECT RAISE(ABORT, 'insert opportunity before entering a submission state');
END;

CREATE TRIGGER IF NOT EXISTS opportunity_submitted_requires_evidence
BEFORE UPDATE OF state ON opportunities
WHEN NEW.state = 'SUBMITTED'
BEGIN
    SELECT CASE WHEN NOT EXISTS (
        SELECT 1 FROM applications a
        WHERE a.opportunity_id = NEW.id
          AND a.final_state = 'SUBMITTED'
          AND length(trim(a.confirmation_evidence)) > 0
    ) THEN RAISE(ABORT, 'SUBMITTED requires recorded success evidence') END;
END;

CREATE TRIGGER IF NOT EXISTS application_submitted_requires_evidence
BEFORE INSERT ON applications
WHEN NEW.final_state = 'SUBMITTED' AND length(trim(NEW.confirmation_evidence)) = 0
BEGIN
    SELECT RAISE(ABORT, 'SUBMITTED application requires success evidence');
END;
