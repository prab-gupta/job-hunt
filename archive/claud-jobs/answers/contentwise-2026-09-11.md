# ContentWise — DevOps Engineer (Milan) — 2026-09-11

LinkedIn: https://www.linkedin.com/jobs/view/4459204957/
ATS: Greenhouse — https://job-boards.greenhouse.io/contentwisespa/jobs/7522303003?gh_src=1tjkyfao3us&source=LinkedIn
Queue note: LI-PICK (reapply); user rule 2026-09-11 — apply regardless of years/seniority/stack fit, soft gates off.

## Dedupe
- `python3 loop/dedupe.py --check "ContentWise" "https://www.linkedin.com/jobs/view/4459204957/"` = NEW
- `python3 loop/dedupe.py --check "ContentWise" "https://job-boards.greenhouse.io/contentwisespa/jobs/7522303003"` = NEW
- `grep -i contentwise applications.csv` = no prior row before this run.

## Hard gates re-check on live JD
- No anti-AI disclaimer anywhere in the JD text.
- Title "DevOps Engineer", not Senior/Staff/Lead/Principal/Manager.
- No hard MSc/PhD requirement (BS/MS listed as "who we're looking for", not mandatory).
- JD is in English.
- Core stack is cloud automation (AWS/GCP/on-prem, Ansible, Terraform, Docker, Kubernetes) — Prabhavit has not administered cloud infrastructure. This is an LI-PICK row so stack fit does not kill it; task explicitly required an honest cloud-gap statement instead of a claim.
- Milan/Padua, Italy, hybrid — in scope.

## CV tailoring (Prabhavit_CV_ContentWise.tex/.pdf, from Prabhavit_CV_EN.tex)
Reorder/delete only — diffed against the source .tex to confirm no sentence was rewritten and no role/date/location was touched.
- Career Summary: trimmed 3 -> 2 bullets (kept the Automation Engineer bullet and the AI-assisted-development/API-orchestration bullet; dropped the business-requirements/QA bullet).
- Technical Skills: reordered Automation and Development categories first (closest to CI/CD and orchestration), AI/ML moved last.
- FlowSpace (9 bullets total, minimum 3 satisfied): Product Responsibilities reordered to lead with the Bubble.io-to-Next.js/Laravel migration bullet and the documentation bullet; Technical Responsibilities reordered to lead with the OfficeRnD/Nexudus API-integration bullet and GTM/CRM automation bullets; dropped 2 duplicate lines that existed in the original CV ("AI tool for processing of data..." repeated, and the migration bullet repeated) and the least-relevant "Facilitated communication between internal team and Agency" bullet.
- UltraStrategy: kept both existing bullets (CV-parsing tool, user-profiles platform) — satisfies the 2-bullet AI/automation-JD minimum.
- Get2Germany: reordered to lead with "Developed AI based automation tools..." and "Integration of Google APIs..." (the 2-bullet AI/automation-JD minimum), kept the database-optimization bullet, dropped the UI/UX-from-Figma bullet as unrelated to a DevOps JD.
- Qomodo/Clubee/Tractionboard: each kept at least 1 bullet (Qomodo 2, Clubee trimmed to 2 leading with QA/testing, Tractionboard trimmed to 1, ChatGPT/OpenAI integration).
- Additional Information: dropped the "Low code development/AI based development" item entirely (JD has no relation to low-code/Bubble), reordered Automation (n8n) first in both IT Skills and Tools.
- `tectonic Prabhavit_CV_ContentWise.tex` compiled clean; `pdfinfo` confirms 2 pages.

## Cover letter (CoverLetter_ContentWise.txt/.pdf)
- 265 words, 0 em-dashes (`grep -c` verified), no "no-code"/"low-code"/"Bubble" text.
- Two-role minimum per the letter-evidence rule: FlowSpace (automated legacy-stack migration to Next.js/Laravel, 2,000 to 4,500+ users, plus ongoing platform operations — CI workflows around Docker, Supabase/Postgres, OfficeRnD/Nexudus API integrations) as the lead paragraph; Get2Germany (Google API integration, n8n automation tools) and UltraStrategy (n8n/Affinda/Claude API CV-parsing pipeline) as the second proof paragraph.
- Explicit honesty paragraph: "my automation experience sits at the application level, not cloud administration. I have not administered AWS or GCP infrastructure or run Kubernetes in production... I want to grow that into infrastructure automation."
- Three years stated plainly ("I have three years of experience...").
- Closing: Venice-based, authorised to work in Italy without sponsorship, Italian conversational / English professional, available immediately for the Milan hybrid role.

## Form fields (Greenhouse, auto-filled by Chrome's MyGreenhouse extension, verified against brief's standing identity)
- First Name: Prabhavit / Last Name: Gupta
- Email: prabhavitg@gmail.com
- Country: Italy (+39) / Phone: 351 610 7807
- Location (City): Venice, Venezia, Italy
- Resume/CV: replaced the autofill's generic resume with Prabhavit_CV_ContentWise.pdf (removed the pre-attached file first, then uploaded via the Attach control)
- Cover Letter: CoverLetter_ContentWise.pdf uploaded via the separate Attach control
- LinkedIn Profile: https://www.linkedin.com/in/prabhavit (autofilled)
- Website: left blank (not asked, no personal site to add)
- No salary, years-of-experience, work-authorisation, EEO, or anti-AI attestation questions were present on this form. No CAPTCHA.

## Result
Submitted. Confirmation page: "Thank you for applying. Your application has been received. If there is a fit, someone will be getting back to you."
