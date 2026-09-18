# BlockTech - Quantitative Developer - 2026-09-09

Posting: https://www.linkedin.com/jobs/view/4437783362/ (LinkedIn "Apply" -> redirected off-platform, "Responses managed off LinkedIn")
Real ATS: Ashby, https://jobs.ashbyhq.com/blocktech/15d042b3-077c-49aa-b3fc-77993ab865f3/application

## Fields filled

- Name: Prabhavit Gupta
- Email: prabhavitg@gmail.com
- Phone Number: +39 351 610 7807
- LinkedIn Profile URL: https://linkedin.com/in/prabhavit
- Resume: Prabhavit_CV_Original_EN.pdf (uploaded)
- Cover Letter: CoverLetter_BlockTech.pdf (uploaded; rebuilt from CoverLetter_BlockTech.txt via CoverLetter_BlockTech.tex + tectonic, 0 em-dashes)
- What is your earliest start date? -> 09/23/2026 (two weeks from today, per standing "available immediately, start two weeks after offer" rule)
- Where are you currently based? -> Italy (combobox rejected "Venice" city-level text with "No results"; country-level granularity, selected "Italy")
- Do you require visa sponsorship to work in The Netherlands? -> Yes (not authorised in NL, needs employer-side TWV permit per work-authorisation.md)
- How did you hear about BlockTech? -> LinkedIn
- "Do you agree to allow BlockTech to contact you about job opportunities for up to 1 year?" (optional, no asterisk, talent-pool/marketing-style consent) -> left unticked, per standing rule

No numeric years-of-experience field, no STEM-degree screening question, and no separate free-text/additional-info box existed on this form, so the TWV transparency line lives only in the cover letter PDF (see below), not pasted separately.

## Cover letter transparency line (from CoverLetter_BlockTech.pdf)

> Logistics: I hold an Italian EU long-term residence permit. I am not yet authorised to work in the Netherlands and would need an employer-side TWV permit, which I am ready to start alongside relocating. English is fluent, available immediately.

## Hard-gate re-check against live JD

- "2+ years of software engineering experience" -> not >3, passes.
- Seniority level on posting: "Not Applicable" (title is Quantitative Developer, not Senior/Staff/Lead/Principal/Manager/CTO) -> passes.
- "A strong academic foundation in a STEM discipline" -> no explicit MSc/PhD or bachelor's-required wording found; not a kill per brief (bachelor's-level framing, and no explicit STEM-degree screening question was ever asked on the form, so the "answer No honestly" branch never triggered).
- "Strong programming skills in Python and ideally Rust and/or C++" -> Rust/C++ stated as "ideally", not required core; live JD text matches the quote given in task, not a kill.
- Location: Amsterdam, Netherlands, On-site, no remote option -> inside the EU, so the "location outside the EU with no remote-from-Italy" gate does not apply; user is ready to relocate per task instructions.
- JD in English throughout -> passes.
- Posting live (175 applicants, reposted 15 hours ago at time of application) -> passes.

No kill triggered. Degree: Prabhavit's actual degree (Ca' Foscari BA Philosophy, International Studies & Economics) was never entered anywhere and never misstated; it did not come up as a form field.

## Dedupe

`python3 loop/dedupe.py --check "BlockTech" <url>` returned `HIT COMPANY~` (fuzzy). Checked `grep -i "block" applications.csv` by column: only two prior rows contain "block" in the company field - "Block Labs" (2026-08-24, Applied AI Engineer, SUBMITTED) and "Blockhouse" (2026-08-28, Experienced Rust Engineer, SKIP). Both are different companies from "BlockTech" (per brief's explicit Kraken/GitKraken example of a non-blocking fuzzy hit). No row for "BlockTech" itself exists. Treated as NEW, proceeded.
