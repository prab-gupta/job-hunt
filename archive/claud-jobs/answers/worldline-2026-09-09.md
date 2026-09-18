# Worldline — Product Owner, Data, Bucharest — 2026-09-09

Status: NEEDS YOU. No form fields were reached — SuccessFactors' account-creation step (Email Address, Retype Email Address, Choose Password) gates the entire application, shown alongside the resume/cover-letter upload boxes on the very first screen. No account was created, per brief guardrails (no creating accounts / setting passwords on Prabhavit's behalf).

## Hard-gate re-check (live JD, curl jobs-guest jobPosting API)
- Seniority: title is plain "Product Owner" (internally "Product Owner Data" in the JD body), no Senior/Staff/Lead/Principal/Manager qualifier. Pass.
- Years required: "Experience in Project Management, Product Operations or Digital Transformation" — no numeric threshold stated. Pass.
- Degree: "Bachelor's degree in Business Administration, IT, or related field; Master's preferred" — Master's is preferred, not required. Pass.
- Certification: "Professional certifications (PMP, SAFe, Scrum Master/Product Owner)" listed as a nice-to-have alongside other "familiarity with" items, not stated as required. Pass.
- Language: "fluent in English" required; no Romanian-language requirement anywhere in the JD. Pass.
- Location: Bucharest, Romania, hybrid, full-time — EU, in scope with relocation. Pass.
- Core stack: role is data-portfolio governance/delivery ownership (Jira, Confluence, PowerBI, Azure as "working knowledge" nice-to-haves), not a disqualifying core-stack language (no Java/.NET/C++/Go/Rust/Django/FastAPI-as-core/cloud-admin-as-core requirement). Pass.
- Posting live: active, 81 people clicked apply, not closed/404. Pass.
- No kill gate hit. Fit as given: 45 (hard-gates-only rule: apply since no gate fails).

## Dedupe
`python3 loop/dedupe.py --check "Worldline" "https://www.linkedin.com/jobs/view/4455341422/"` -> NEW.
`grep -i worldline applications.csv` -> no prior rows for Worldline.

## What was prepared and staged (ready once the account exists)
- CV: Prabhavit_CV_Original_EN.pdf (never any other CV).
- Cover letter: CoverLetter_Worldline.txt (203 words, no em-dashes, grep -c "—" = 0) and CoverLetter_Worldline.pdf (built from CoverLetter_Worldline.tex via tectonic, verified 1 page).
  - Content: why a Product Owner role in payments; FlowSpace proof (owned discovery-to-rollout for three products: LLM listing pipeline for 900+ listings, RAG support agents, OfficeRnD/Nexudus integrations), wrote specs, ran backlog and iteration with operators and engineers; why Worldline (Data Office portfolio steering/governance is the same shape of work at payments-data scale); logistics (Venice-based, ready to relocate to Bucharest, honest Romania permit transparency line).
- Standard answers that would apply once the form is reachable (not yet entered anywhere):
  - Years of experience: 3 (numeric field, threshold-safe) / "about three years, 2.5 at FlowSpace" (free text).
  - Work authorisation: Authorised in Romania = No; sponsorship/employer-side permit needed = Yes; transparency line used verbatim from answers/work-authorisation.md ("I hold Italian EU long-term resident status. I am not currently authorised to work in Romania and would need the applicable employer-side permit or sponsorship process. I am ready to relocate and complete that process.").
  - Salary: EUR 45,000 (no band disclosed on this posting).
  - Notice/start: available immediately; start date two weeks after offer.
  - Relocation: Yes, ready to relocate to Bucharest.
  - Follow Worldline checkbox: would be left unticked (not reached).

## Blocker detail
LinkedIn's "Apply" button on this posting is not Easy Apply ("Responses managed off LinkedIn", external-link icon) and opens a new tab directly to Worldline's own careers site (jobs.worldline.com/job/Product-Owner/305050-en_US). Its "Apply now" button redirects to Worldline's SAP SuccessFactors career portal (career2.successfactors.eu/careers?company=Worldline). The landing screen shows Resume/CV and Cover Letter upload boxes, immediately followed by mandatory Email Address, Retype Email Address, and Choose Password fields (with an "8-18 chars, upper+lower, number/punctuation, no spaces/unicode" complexity note) and a "Please sign in" link for existing users — i.e. this is a hard account-creation wall before any job-specific question is shown. No genuine apply-without-account path exists on this tenant.

Tab left open for Prabhavit: Chrome MCP tab group, tabId 550849784 (career2.successfactors.eu registration screen), nothing typed into it. Origin LinkedIn tab (550849783) and the Worldline careers-site tab also left as-is since they are part of the same click chain.
