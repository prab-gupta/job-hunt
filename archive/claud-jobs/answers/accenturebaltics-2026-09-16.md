# Accenture Baltics (Riga) - GenAI Forward Deployed Engineer - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4453240970/

USER RULE 2026-09-16: apply to every FDE posting on LinkedIn in Italy/EU, no kill for fit/years/seniority/agency/stack. Latvia line, offsite. Task instruction: Accenture Workday - try Apply Manually as guest; if only account creation remains, build CV+letter under slug AccentureBaltics, log NEEDS YOU with the exact URL, do not create an account.

## Dedupe
`dedupe.py --check "Accenture" <url>` returned HIT COMPANY~ (fuzzy, expected - many Accenture entities on file). `grep -i accenture applications.csv | grep -i forward`: Accenture Italia FDE Manager (R00345222), Accenture UK & Ireland FDE Specialist (R00345688), Accenture Espana FDE (R00345180) - all different countries/requisitions, all NEEDS YOU not SUBMITTED. No row for Accenture Baltics / Riga / GenAI FDE. Different requisition, does not block. Proceeded, built a distinct CV/letter pair under the AccentureBaltics slug per the task note so none of the existing Accenture files are touched.

## Hard gates
JD requires "candidates must currently hold EU work permit" - Prabhavit holds Italian EU long-term resident status, which is EU-wide mobility-eligible but not an automatic Latvian work permit; per work-authorisation.md this is the standard "No, Yes sponsorship/permit" answer, not a hard block, and the standing FDE-blanket rule waives location/authorisation-shaped fit gates for this batch. 5+ years JS and 3+ years leading dev teams required - waived per the same rule, stated honestly in the letter (3 years, no formal team-lead title). No language he lacks required (English only). No anti-AI clause; JD explicitly wants GitHub Copilot/Claude-native delivery.

## CV tailoring (Prabhavit_CV_AccentureBaltics.tex/.pdf, from the verified Prabhavit_CV_Harmattan.tex base)
- Career Summary: default 2 bullets unchanged.
- Technical Skills reordered: Development (Claude Code, Laravel, Typescript) first, then AI/ML, then Automation, then Project/Design - JD leads with modern-JS web app development and GenAI-tool fluency (Copilot/Claude) over pure AI/ML.
- FlowSpace Product Responsibilities reordered: "Collaborated with team of developers for product logic and business logic documentation" moved to lead position (closest evidence to the JD's "3+ years leading development teams" ask), then AI-agent support, scale, migration, agency comms. Technical Responsibilities unchanged (AI listing tool, API integrations, CRM, GTM, commute tool).
- UltraStrategy, Urlink, Get2Germany, Qomodo, Clubee, Tractionboard unchanged from the Harmattan base, all verbatim.
- Compiled 2 pages via tectonic.

## Cover letter
CoverLetter_AccentureBaltics.pdf/.txt. Lead FlowSpace (Claude Code / Claude API used daily in the AI listing bot and support agents - directly on theme for "GenAI embedded at every stage of the SDLC"; team collaboration on product/business logic), paired with UltraStrategy (Claude API + Affinda CV-parsing pipeline as a second GenAI-in-production example). States plainly: 3 years total experience, no formal people-management title (the JD's "3+ years leading development teams" is not met), and includes the work-authorisation.md transparency line for Latvia. 0 em-dashes.

## Workday handling
accenture.wd103.myworkdayjobs.com tenant: every requisition tried this month has walled at "Apply Manually" -> step 1 of 6 mandatory Create Account/Sign In, no guest path (see LEARNINGS.md and the three other 2026-09-16 Accenture NEEDS YOU rows). Expect the same here.

## Standing answers if a form is reached
Years: 3. Salary: JD publishes Baltic management-level bands (Senior Analyst 1700-3400, Team Lead 1900-4700, Associate Manager 2400-5600 EUR gross, presumably monthly); the standing EUR 45,000-55,000 annual default is higher than these bands, so per the "align to band bottom only when the posting's band is higher" rule the standing default (EUR 45,000, stated as intended base) is used as-is rather than downgraded to the Baltic scale. Work authorisation: Latvia = No/Yes sponsorship, transparency line added. Italian: conversational. Driver's license: No.
