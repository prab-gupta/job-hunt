# Application statistics: 24 July to 5 October 2026

Like a Bubble repeating group filtered by application date, this audit counts each distinct application once, then checks which records have a matching rejection.

**1,286 recorded applications, 345 matched rejected applications, and a 26.8% observed rejection rate.**

Period: 24 July 2026 through 5 October 2026, inclusive, using Europe/Rome dates. Snapshot generated 5 October 2026 at 10:53 CEST.

| Metric | Count or rate |
|---|---:|
| Distinct dated applications recorded as sent | 1,286 |
| Applications supported by submission evidence or a matching rejection | 1,050 |
| Additional records reported as sent, without independent supporting evidence | 236 |
| Distinct applications with a matched rejection | 345 |
| Observed rejection rate across all recorded applications | 26.8% |
| Observed rejection rate within the supported subset | 32.9% |
| Dated applications without a matched rejection | 941 |

Calculation: 345 / 1,286 × 100 = 26.83%. Within the supported subset, 345 / 1,050 × 100 = 32.86%.

## Applications grouped by submission month

Rejections below belong to applications submitted in that month. They are counted regardless of which later month the rejection arrived in.

| Application period | Recorded applications | Matched rejections |
|---|---:|---:|
| 24–31 July | 9 | 9 |
| August | 394 | 168 |
| September | 470 | 148 |
| 1–5 October | 413 | 20 |
| **Total** | **1,286** | **345** |

## What the figures establish

The 1,050 supported applications include 1,011 backed by a receipt, an initial sent email, a recorded completion, or reviewed application evidence. Matching rejection messages independently corroborated another 39 recorded applications. These forms of evidence do not all have the same strength: a saved completion record is less direct than an employer receipt.

The remaining 236 dated records are recorded as sent but lack independent supporting evidence in the audited sources. They are included in the recorded total and in the 26.8% calculation. The alternative 32.9% calculation uses only the supported subset, and all 345 matched rejected applications belong to that subset.

Another 31 application records have no reliable submission date and are excluded from this period. There are also 100 actual rejection messages whose role or submission date could not be matched confidently to this cohort. They are not counted as 100 additional rejected applications: some may be duplicates or replies to older applications.

These totals describe recovered records rather than a guaranteed exhaustive census. The July row contains only the nine dated applications recovered for 24–31 July; it should not be read as proof that every application sent that week was rejected.

The 941 applications without a matched rejection are not classified as successes, acceptances, or pending solely from the absence of a negative message. There are 413 applications dated 1–5 October, so many have had only a few days to receive replies. This is an observed rejection share as of the audit time, not an eventual rejection probability.

## Sources and counting method

- Reconciled the canonical applications.csv snapshot with historical application logs and sent/completion records in the workspace.
- Counted applications.csv, loop/applications.csv, and data/csvs/applications.csv as one source because the latter two are mirrors.
- Checked Gmail receipts, initial outgoing applications, and actual rejection bodies, including archived mail. Full message bodies were inspected where snippets or labels were ambiguous.
- Counted each distinct job or requisition once. Repeated receipts, repeated submissions to the same job, and repeated negative emails were deduplicated. Distinct roles at one employer were counted separately.
- Matched rejection messages to a dated application by role, confirmation, or reviewed unambiguous evidence. Uncertain title changes and generic messages with multiple plausible applications were left unresolved.
- Excluded follow-up emails, account notices, drafts, verification messages, unrelated correspondence, conditional future-rejection language, and a rejection explicitly retracted by the employer.
- Corrected five final-review acknowledgment messages that had initially been classified as rejections. Genuine later rejections for Kayzen and Bloomreach Demo Engineer were retained.

The final negative-email audit contains 473 actual rejection messages: 373 matched messages for 345 distinct applications, plus 100 unresolved messages.

No application trackers were changed and no emails were sent. Audit figures reflect the source snapshots inspected during this session.

## Example: LumApps

LumApps Forward Deployed Engineer (FDE) M/F is included once: application dated 9 September, rejection dated 28 September 2026. The rejection was received at 10:57 Europe/Rome.

[Open the LumApps rejection in Gmail](https://mail.google.com/mail/u/?authuser=prabhavitg%40gmail.com#all/1a0e73b8a56f2454).

Python quick bite: `rejected / applications * 100` turns two counts into a percentage, like a calculated field in Bubble.
