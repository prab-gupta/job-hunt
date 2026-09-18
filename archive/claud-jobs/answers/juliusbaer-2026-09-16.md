# Julius Baer - Machine Learning Engineer 100% (f/m/d) - 2026-09-16

Verifier-flagged account-wall row. Task's LinkedIn URL (job 4466556120) turned out to point at an unrelated Eurofins lab-technician posting in France (checked via the jobs-guest API JD fetch). Searched LinkedIn (logged in) for "Machine Learning Engineer Julius Baer Madrid" and found two listings for the same underlying requisition: job 4466552214 (posted 21 hours ago) and job 4431210733 (reposted 1 hour ago), both apply-button count 1 (open). Used the fresher repost, which linked out to Julius Baer's own Workday tenant: https://juliusbaer.wd3.myworkdayjobs.com/en-US/External/job/Madrid/Machine-Learning-Engineer-100---f-m-d-_r-18155 (requisition r-18155).

## Gate re-check on the live JD
- Degree: "Bachelor's or Master's degree" - Bachelor's accepted, not a hard MSc-only requirement.
- Years: no explicit number stated ("Relevant work experience..."), not a 5+ years gate.
- Title: plain "Machine Learning Engineer", not Senior/Staff/Lead/Principal/Manager/CTO; LinkedIn tags it Seniority level Not Applicable.
- Language: English required, "Spanish is a plus" (not mandatory) - no non-English-language gate.
- Location: Madrid on-site, Spain is in the EU - not the "outside the EU, no remote-from-Italy" gate. Standing answers cover on-site/relocation as Yes.
- Core stack: RAG, multi-agent systems, tool-calling, LLM orchestration, Python - matches Prabhavit's claimable skills (RAG and LLM APIs explicitly claimable per the brief). TensorFlow/PyTorch/classical-ML/statistics are asked for but not in the "cannot claim" list (Java/.NET/C++/Go/Rust/Django-FastAPI-core/cloud-admin); handled with an honest caveat in the letter rather than a false claim or a KILL.
- No anti-AI disclaimer anywhere in the JD.
- Verdict: no gate fails, proceed.

## Apply path
Clicked "Apply" on the LinkedIn posting, which opened the Julius Baer Workday job page in a new tab (external, "Responses managed off LinkedIn"). Clicked Apply, then "Apply Manually" in the Start Your Application dialog. Unlike the Workday and Accenture rows logged earlier this session (which dead-ended at Create Account/Sign In), this tenant opened directly into a genuine 5-step guest application (My Information, My Experience, Application Questions, Voluntary Disclosures, Review) with no login wall at any step.

## CV
Prabhavit_CV_JuliusBaer.tex built from Prabhavit_CV_EN.tex. Diffed all `\item` bullets between the two files: every difference was word-order-only within an existing bullet (Development/IT Skills/Tools lines), no invented content. Compiled clean with tectonic, 2 pages.
- Career Summary: 2 bullets (AI/LLM-driven applications + AI agents/LLM-powered data parsing).
- FlowSpace: Technical Responsibilities led with the AI-tool/API-integration/CRM/GTM bullets; Product Responsibilities led with the AI-agents bullet; 7 bullets total (minimum 3 met).
- UltraStrategy: both existing bullets kept (CV-parsing tool, user-profiles platform) - the required AI/automation pair.
- Get2Germany: both existing bullets kept (AI automation tools for courses/internships/jobs, Google APIs) - the required AI/automation pair.
- Urlink 2 bullets, Qomodo 1, Clubee 1, Tractionboard 1 - all above the 1-bullet minimum, no role/date/location deleted.
- Additional Information: AI/RAG/API item moved first, Low-code item kept but moved later (per the "drop only if unrelated" rule - it was reordered, not dropped, matching the Adevinta precedent).

## Cover letter
CoverLetter_JuliusBaer.pdf/.txt. Two proof paragraphs: FlowSpace (AI listing bot + support agents grounded in live platform data, Claude API/n8n/TypeScript stack) as lead, UltraStrategy (CV-parsing pipeline, Affinda + Claude API + n8n/Eden AI) as the pair, per the material rule that FlowSpace may never be the only proof paragraph. Zero em-dashes (grep -c confirmed 0). Honest gap statement: applied LLM engineering/agents/RAG rather than classical TensorFlow/PyTorch model training. Spain work-authorisation transparency line from answers/work-authorisation.md, verbatim.

## Form answers given
- My Information: Prabhavit Gupta, Via Zanetti 10, 30175 Venice, Venezia province, Italy; prabhavitg@gmail.com; Mobile +39 351 610 7807; How Did You Hear About Us = LinkedIn (found under the Social Media submenu, no flat "LinkedIn" top-level option); worked at Julius Baer before = No.
- My Experience: uploaded Prabhavit_CV_JuliusBaer.pdf and CoverLetter_JuliusBaer.pdf via the hidden file input (both showed "Successfully Uploaded!"); LinkedIn URL = https://www.linkedin.com/in/prabhavit/. Left Work Experience/Education/Languages/Skills sub-forms empty (not marked required, no red asterisk, and the uploaded CV/letter already carry that information).
- Application Questions: currently live in Spain = No; citizen of the EU/EFTA = No (Indian citizen, EU long-term resident, not a citizen); eligible to work in Spain = No (per work-authorisation.md, another EU country requires the employer-side permit); expected salary = EUR 50,000 gross annually (standing answer); notice period = "Available immediately; can start two weeks after an offer" (standing answer); ideal start date = 09/30/2026 (two weeks out); willing to relocate = Yes; English level = Fluent; Spanish level = Basic (no Spanish is claimed anywhere in the CV or letter; the dropdown had no "None" option, so the floor of the scale, Basic, was the most honest available choice; nothing in the letter or CV claims Spanish); can work the 100% workload = Yes; willing to work on-site with home office option = Yes; checked both required acknowledgement checkboxes that Julius Baer might ask for a criminal record / debt-collection-register extract if an offer is made (an awareness acknowledgement, not submitting any actual sensitive document or number).
- Voluntary Disclosures: Primary Nationality = India; checked the required "Yes, I have read and taken note of the Declaration" GDPR data-protection consent (this is the mandatory privacy-processing consent, not an optional marketing/talent-pool checkbox - there was no separate marketing opt-in on this tenant).

## Result
Submit returned an immediate "Congratulations!" confirmation and the URL updated to carry Job_Application_ID=298379a1aa26900155a9498db3230000, confirming the application was recorded. A post-submission "Create Account" modal then appeared (optional, to track the application) with password fields; per standing rule no account was created and no password was entered - the modal was closed without action. Logged SUBMITTED.
