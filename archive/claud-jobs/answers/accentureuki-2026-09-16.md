# Accenture UK & Ireland — Forward Deployed Engineering Specialist (Dublin)

Job (LinkedIn): https://www.linkedin.com/jobs/view/4453234984/
Job page (accenture.com): https://www.accenture.com/ie-en/careers/jobdetails?id=R00345688_en&src=LINKEDINJP (req R00345688, Dublin)
Apply URL (Workday): https://accenture.wd103.myworkdayjobs.com/AccentureCareers/job/Dublin/Forward-Deployed-Engineer_R00345688/apply
Date: 2026-09-16

## Gate check
- Cheap check: apply-button present on LinkedIn posting (Apply on company website, 92 clicked apply). Not closed.
- USER RULE 2026-09-16 (apply to every FDE posting in Italy/EU, no fit/years/seniority/agency/stack kills): applies here, but seniority tag is "Not Applicable" anyway.
- Dedupe: `dedupe.py --check "Accenture" <url>` = HIT COMPANY~ (fuzzy). `grep -i accenture applications.csv`: multiple Accenture Greece LEAD rows (different company/entity, not blocking); Accenture Italia rows (Analyst, Specialist, Slovakia, DACH: all NEEDS YOU, different requisitions/countries); Accenture UK & Ireland "Engineering Lead" (SKIPPED, different role); Accenture Italia "Forward Deployed Engineer Manager" (NEEDS YOU, different entity + different requisition R00345222 vs this R00345688). None SUBMITTED for this requisition. Proceeded per this session's task instruction ("other Accenture entities today are different requisitions").
- Ireland: EU LTR mobility directive excludes Ireland (per answers/work-authorisation.md). Authorised No, sponsorship Yes. Transparency line used in the letter.

## Apply flow result: account creation required (user-only)
LinkedIn "Apply on company website" opened the accenture.com job page in a new tab; its "Apply for this job" link went straight to the Workday apply URL. Declined cookies. Workday's "Start Your Application" chooser offered Autofill with Resume / Apply Manually / Use My Last Application. "Apply Manually" advanced straight to a Workday "Sign In" page (title becomes "Sign In"), offering "Sign in with Google" or "Sign in with email" only, with a "Create Account/Sign In" step label. No guest-checkout path. Per the brief, account creation is user-only: stopped here, nothing submitted, no account created.

## Materials prepared for the user to submit after they sign in
- CV: Prabhavit_CV_AccentureUKI.tex/.pdf (2 pages, verified with `pdfinfo`).
  - Career Summary: kept bullets 1 and 2 (LLM-driven applications/workflows; AI-assisted development, prompt engineering, API integrations), dropped bullet 3.
  - FlowSpace Product Responsibilities: "Streamlined customer support with AI agents" moved to top; kept scale (2000->4500+) and migration bullets, plus the two collaboration/agency bullets.
  - FlowSpace Technical Responsibilities: deduped the repeated AI-tool and migration lines, dropped the one-off commute-time tool bullet; kept AI listing tool, OfficeRnD/Nexudus integration, CRM/lead-capture, GTM automation.
  - UltraStrategy: kept both bullets (AI/automation JD minimum of 2).
  - Urlink: kept all 3 bullets (client-embedded automation theme).
  - Get2Germany: reordered AI-automation-tools bullet ahead of Google-API bullet (AI/automation JD minimum of 2, both kept); kept remaining two bullets.
  - Additional Information / IT Skills: dropped the "Low code" phrase (JD has no low-code relation); order otherwise led with AI/API.
  - No sentences rewritten, no claims added.
- Cover letter: CoverLetter_AccentureUKI.tex/.txt/.pdf. Two-role evidence: FlowSpace (AI listing bot 900+ drafts, support AI agents with confidence-based escalation, live migration 2,000->4,500+ users, OfficeRnD/Nexudus, CRM/GTM automation) and Urlink (AI-assisted platform build, client-driven automations, Next.js/Supabase/Netlify). No em-dashes (`grep -c` for U+2014 = 0). Ireland transparency line: not currently authorised, would need employer-side permit/sponsorship, ready to relocate.

## Incident note
An earlier step in this session's own work (`cp Prabhavit_CV_EN.tex Prabhavit_CV_Accenture.tex`) overwrote the pre-existing 2026-09-11 Accenture Italia Specialist materials (req R00344641, NEEDS_YOU.md row 17f) before this file's CV/letter were renamed to the AccentureUKI slug. The Sept 11 materials were reconstructed from answers/accenture-2026-09-11.md's documented spec and re-verified (2 pages); this session's own materials now live under Prabhavit_CV_AccentureUKI.pdf / CoverLetter_AccentureUKI.pdf. See loop/LEARNINGS.md 2026-09-16 23:20 entry.

## What the user needs to do
1. Open https://accenture.wd103.myworkdayjobs.com/AccentureCareers/job/Dublin/Forward-Deployed-Engineer_R00345688/apply
2. Sign in / create the account (their own credentials).
3. Say "Accenture UKI ready" so the rest of the form can be filled with Prabhavit_CV_AccentureUKI.pdf + CoverLetter_AccentureUKI.pdf and the Ireland answers (authorised No, sponsorship Yes, salary EUR 45,000-55,000, years 3).

Logged in loop/results/AccentureUKI.txt and appended as row 22 in NEEDS_YOU.md.
