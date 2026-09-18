# Central Consulting Company — AI/ML Engineer — 2026-09-09

URL: https://www.linkedin.com/jobs/view/4463007786/
Method: LinkedIn Easy Apply

## Hard gate re-check (on live JD)
- Required years: 2-5. True number 2.5 clears the lower bound of 2. PASS.
- Seniority level tag on posting: Entry level. No Senior/Staff/Lead/Principal/Manager/CTO title. PASS.
- No MSc/PhD requirement stated. PASS.
- JD entirely in English, no Bulgarian requirement stated. PASS.
- Core daily job: "integrating, configuring, and adapting pre-existing databases and AI/ML models into real business environments," translating algorithms into business language for clients — an application/integration layer role, not core model training/research. Fine-tuning and validation are listed as one of several responsibilities, not the sole focus. PASS (claimable per claim ladder: fine-tuning, embeddings, evals as working knowledge; strongest claim is production LLM pipelines).
- Location: Sofia, Bulgaria (EU), on-site. Work authorisation = No (not automatically authorised outside Italy under EU LTR), employer-side permit/sponsorship = Yes. Ready to relocate. PASS per standing rules (on-site EU roles are acceptable targets).

Decision: no KILL conditions met. Proceeded to apply.

## Dedupe
`python3 loop/dedupe.py --check "Central Consulting Company" "https://www.linkedin.com/jobs/view/4463007786/"` → NEW.
`grep -i "central consulting" applications.csv` → no prior rows. Clear to apply.

## Form fields (LinkedIn Easy Apply — single page)
- Email: prabhavitg@gmail.com (LinkedIn profile default, correct)
- Phone country code: Italy (+39)
- Phone: +39 351 610 7807
- Resume: Prabhavit_CV-.pdf selected from LinkedIn's resume library (this is the canonical CV, matches ROOT/Prabhavit_CV_Original_EN.pdf)
- Follow Central Consulting Company checkbox: unticked (was ticked by default)
- No years-of-experience numeric field, no salary field, no notice-period field, no free-text essay questions, and no cover-letter upload/paste field existed on this particular Easy Apply form. It was a minimal 4-element form: contact info + resume + follow checkbox + submit.

## Cover letter
Written per brief to `ROOT/CoverLetter_CentralConsulting.txt` (200 words, 0 em-dashes) and compiled to `ROOT/CoverLetter_CentralConsulting.pdf` via `ROOT/CoverLetter_CentralConsulting.tex` (tectonic, 1 page confirmed). Not attached to this application because the Easy Apply form had no field to receive it (no message box, no upload slot). Kept on file for reference / in case of a follow-up email to the recruiter.

Claims traced to `ROOT/Prabhavit - Master Experience.md`:
- "production LLM extraction pipeline that has drafted 900+ workspace listings" → Master Experience "Added by the loop 2026-09-06" section (900+ listings drafted, verified figure) and "AI listing bot" section.
- "RAG-backed support agents ... escalate to a human on low confidence" → Master Experience FlowSpace "Other work" bullet: "Support AI agents that answer customer queries against live platform data and escalate to a human on low confidence."
- "Python, ... Supabase and PostgreSQL" → Master Experience Skills section (APIs & data: Supabase, Postgres) and Stack line.
- "deploy models and agents through APIs" → Master Experience Skills (LLM integration & pipelines, OpenAI/Claude APIs).
- ML depth honesty line (working knowledge: fine-tuning, embeddings, evaluation) → Master Experience "Claim ladder" guardrail: ML work (fine-tuning, embeddings, evals, PyTorch) claimable as working knowledge only, never as production/research depth.
- Location/relocation/permit line → Master Experience Snapshot (Venice, Italy; Italian EU LTR) and `answers/work-authorisation.md` transparency line for relocation roles.

## Work authorisation answer used
Not asked directly on this form (no such field existed), but per standing rule for Bulgaria (EU, non-Italy): authorised now = No, sponsorship/employer-side permit needed = Yes. Transparency line included in the cover letter instead: "I am not currently authorised to work in [country] and would need the applicable employer-side permit or sponsorship process. I am ready to relocate and complete that process," adapted to Sofia.

## Salary
Not asked on this form. Standing answer if it comes up later: EUR 45,000 (band bottom per task instruction).
