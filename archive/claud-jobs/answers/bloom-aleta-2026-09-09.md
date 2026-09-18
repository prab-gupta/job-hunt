# Bloom (for Aleta) — Platform Engineer (AI-First), Aarhus — 2026-09-09

ATS: Matador Jobs plugin embedded directly on https://bloom.dk/jobs/platform-engineer-ai-first-406/ (Danish recruitment agency Bloom, hiring on behalf of client Aleta). No separate ATS redirect, no login/account wall, no CAPTCHA.

## Form fields submitted

| Field | Value |
|---|---|
| Fornavn (First name) | Prabhavit |
| Efternavn (Last name) | Gupta |
| Email adresse | prabhavitg@gmail.com |
| Mobiltelefon | +39 351 610 7807 |
| Nuværende/seneste jobtitel | Lead Developer |
| Nuværende/seneste arbejdsgiver | FlowSpace |
| Foretrukket sprog | English (default, unchanged) |
| Land | Italy |
| Upload dit CV | Prabhavit_CV_Original_EN.pdf |
| Upload ansøgning og/eller andre dokumenter | CoverLetter_Bloom_Aleta.pdf |
| Consent checkbox (data storage / sharing with hiring company) | Ticked, via computer left_click on ref (not form_input) |

No numeric years, salary, or work-authorisation radio/dropdown existed on this form — it is a lean 8-field contact/CV form. Those answers are recorded below for the record since the brief requires re-checking them, even though the form itself never asked.

## Hard gates re-checked on live JD

- Years: JD explicitly deprioritises years ("We care more about what you've learned and what you've owned than the number of years on your CV") — no numeric threshold anywhere. Passes.
- Title: "Platform Engineer" — not Senior/Staff/Lead/Principal/Manager/CTO. Passes.
- Degree: no MSc/PhD requirement mentioned. Passes.
- Language: JD entirely in English; no Danish-language requirement stated anywhere (this is a Danish recruiter's site but the posting and form are English-first, "Foretrukket sprog" defaulted to English). Passes.
- Core stack: TypeScript + Next.js (app layer) is the claimable core; Rust is named for the calculation engine but explicitly "welcome, not required." No Java/.NET/C++/Go/Rust-as-core, no Django/FastAPI-as-core, no cloud-admin requirement. Passes.
- Location: Aarhus, Denmark, in-EU geographically, so no EU-exclusion kill. "Based in or near Aarhus" is a relocation expectation, not a remote-only-EU gate; Prabhavit is ready to relocate anywhere in the EU. Passes.
- Posting live, not closed/404. Passes.

No KILL gate triggered.

## Work authorisation (Denmark — not asked on this form, held in reserve)

Per `answers/work-authorisation.md`: Denmark is excluded from the EU long-term-resident mobility directive. Standard answer if ever asked: authorised now = No, sponsorship/employer-side permit needed = Yes. Transparency line used in the cover letter: holds Italian EU long-term resident status, which does not cover Denmark, so would need an employer-side permit and is ready to start that process. Ready to relocate to Aarhus.

## Dedupe

`python3 loop/dedupe.py --check "Bloom" "https://bloom.dk/jobs/platform-engineer-ai-first-406/"` → `HIT COMPANY~` (fuzzy).

`grep -i "bloom" applications.csv` rows found: Bloomreach (x3, SUBMITTED/LEAD/SKIP), ReBloom (SUBMITTED), Bloomwell Group GmbH (LEAD), Bloom & Wild Group (LEAD, then DEAD). None of these is "Bloom" the Aarhus recruitment agency — all different companies (Bloomreach = MarTech SaaS, ReBloom = different product, Bloomwell = German cannabis/health co, Bloom & Wild = UK flower delivery). Per brief this fuzzy hit never blocks. Proceeded as NEW.

## Cover letter

`CoverLetter_Bloom_Aleta.txt` (198 words) and `CoverLetter_Bloom_Aleta.pdf` (1 page, built from `CoverLetter_Bloom_Aleta.tex`, copied from the `CoverLetter_eduBITES.tex` template, compiled with `tectonic`). 0 em-dashes (`grep -c "—"` = 0). No "no-code"/"low-code"/"Bubble"/"Anthropic" (Claude Code named as a daily dev tool only, which is permitted). Claims traced to `Prabhavit - Master Experience.md`: FlowSpace Next.js/Laravel/Supabase production ownership, live legacy-stack migration, LLM listing pipeline (900+ listings, human review), OfficeRnD + Nexudus integrations, Claude Code as daily driver. No fabricated "on-call for booking flows broke" framing beyond what the Master doc supports (FlowSpace day-to-day = "maintaining the platform... understanding and resolving customer issues as they come up," which covers debugging live booking-integration issues).

## Salary / notice

Not asked on this form. Standard answer on file if a follow-up screen asks: EUR 45,000–55,000 (aligned to bottom of a higher band if the posting states one; this posting states none), available immediately, two weeks after offer.
