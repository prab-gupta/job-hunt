# Aircall - Senior Forward Deployed Engineer, Key Accounts (AI Solutions) - 2026-09-17

URL: https://www.linkedin.com/jobs/view/4458365111/
Requisition context: Berlin hybrid, senior tier, Key Accounts FDE row. Distinct requisition from the separate "Forward Deployed Engineer (AI Solutions)" Paris row (job 4458347375) a concurrent agent worked the same morning.

## Task premise re-checked
Task briefing stated "German required = kill". Re-checked the live JD body (full text, no truncation) and the entire 5-page Easy Apply screening flow: no German-language requirement anywhere, explicit or implied. The only Germany-specific questions are right-to-work/residency/sponsorship/relocation/hybrid-office, not language. Per the FDE-ALL rule (kill only for closed/dup/language he lacks, with a quotable requirement), there was no clause to quote, so this was not treated as a kill. Applied instead, honest on the years gap (task's own framing: "honest 3 years against a senior ask").

## Dedupe
`python3 loop/dedupe.py --check "Aircall" "https://www.linkedin.com/jobs/view/4458365111/"` -> HIT COMPANY (fuzzy on company name only).
`grep -i aircall applications.csv`: prior rows are LEAD, DEAD (404), SKIP - GEO/US ONLY/LANGUAGE for other Aircall roles at other levels/locations (Senior/Staff Data Engineer, NA West FDE, Developer Advocate Portugal, Customer Engineer Iberia rows) plus the same-day Paris FDE (AI Solutions) SUBMITTED row for a different requisition (job 4458347375). None SUBMITTED/NEEDS YOU/INTERVIEW/REJECTED for this exact requisition (job 4458365111). Not blocked.

## Hard gates
- Anti-AI disclaimer: none (JD only notes Aircall may use AI tools to screen applications, not a ban on candidate AI use).
- Not closed: cheap curl apply-button check and live page both showed active Easy Apply, "Actively reviewing applicants", 29 applicants.
- Core stack claimable: APIs/webhooks/JSON, JS/Python scripting, low-code orchestration (n8n), CRM automation, AI agent configuration all match Prabhavit's claimable stack.

## CV
Prabhavit_CV_AircallKeyAccounts.pdf built from Prabhavit_CV_EN.tex, 2 pages, deletions/reordering only (parity-diffed clean).
- Career Summary: kept 2 bullets (unchanged from template).
- Technical Skills: Automation (n8n) moved first given the JD's heavy emphasis on low-code orchestration (Zapier/Make/n8n/Workato) and CRM automation.
- FlowSpace: CRM/GTM automation and OfficeRnD/Nexudus integrations moved to the top of Technical Responsibilities (closest match to "Design, build, and deploy integrations using low/no-code platforms... and CRM automation tools").
- UltraStrategy: both existing bullets kept (>=2, AI/automation JD).
- Get2Germany: all 4 existing bullets kept (>=2 satisfied).
- Note: this CV/letter slug was renamed from the plain "Aircall" slug to "AircallKeyAccounts" after discovering a same-day file collision with a concurrent agent's Paris FDE (AI Solutions) application under the same company slug (see confirmations/Aircall-2026-09-17.txt and applications.csv for that row). The plain "Aircall" slug files were reconstructed back to the other agent's original Paris-FDE tailoring from their answers/aircall-2026-09-17.md spec; this session's own materials now live under the AircallKeyAccounts slug.

## Letter
CoverLetter_AircallKeyAccounts.pdf/.txt (0 em-dashes grep-verified): FlowSpace led (CRM/GTM automation on n8n, OfficeRnD/Nexudus integrations, support AI agents, legacy-stack migration 2,000 to 4,500+ users) paired with Urlink (AI-assisted platform build, client-facing project management), honest that 3 years is against the 6+ years senior ask, Germany work-authorisation transparency line (relocation required, sponsorship needed), Claude/Claude Code daily-use line.

## Answers given
- LinkedIn Profile: linkedin.com/in/prabhavit
- Website: github.com/prab-gupta
- Desired salary: EUR 50,000
- Right to work in Germany: No
- Currently live in Germany: No
- Require sponsorship now/future: Yes
- Sponsorship details free text: "I hold Italian EU long-term resident status and would need the applicable employer-side work permit for Germany, ready to start the process on an offer."
- Willing to relocate: Yes
- Comfortable in office 3 days/week (hybrid): Yes
- Customer-facing role experience: Yes
- "Mark job as a top choice": left unticked (optional, not needed)
- "Follow Aircall" checkbox: unticked (not required consent, kept minimal per marketing-checkbox convention)

## Result
SUBMITTED. Confirmation: "Your application was sent to Aircall!" / "Application submitted - now". Saved to confirmations/AircallKeyAccounts-2026-09-17.txt.
