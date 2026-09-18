# Job-search folder audit

Created: 2026-08-28

## Outcome

The folder contains a mature application system, but its operating knowledge was split across multiple files and `applications.csv` contains malformed rows. ATS-specific runbooks now live in [`ats-guides/`](ats-guides/README.md).

## Confirmed observations

- `applications.csv` has 10 columns and 2,386 parsed data rows.
- Exactly 26 physical CSV records have fewer than the required 10 fields. The first is physical record 826 and the last is 2,369. Values such as dates, URLs, ATS names, and long notes consequently appear under the wrong headers. Raw status totals are therefore unreliable.
- Affected physical records: 826, 827, 828, 829, 831, 832, 833, 834, 836, 840, 842, 843, 857, 859, 860, 861, 862, 2,350, 2,351, 2,352, 2,353, 2,354, 2,355, 2,356, 2,357, and 2,369.
- The Rithum second Spain requisition is already `SUBMITTED` with confirmation: “Thank you for applying for a role at Rithum! Your application has been received.”
- The first Rithum requisition is `CLOSED`.
- Existing ATS knowledge was split between `form-quirks.md` and `apply-bot/PATTERNS.md`.
- The repository already had substantial uncommitted application history and generated material before this audit. Those files were preserved.

## Safe next cleanup

1. Create a timestamped copy of `applications.csv`.
2. Identify every physical CSV record whose field count differs from 10.
3. Reconstruct each malformed record from nearby rows, job folders, confirmation screenshots, and prior backups.
4. Produce a proposed repaired CSV plus a row-by-row change report.
5. Replace the live tracker only after manual review.

Automatic repair was intentionally not performed because column shifts can change application history silently.
