# Nearform - Forward Deployed Engineer - Ireland - 2026-09-17

LinkedIn URL: https://www.linkedin.com/jobs/view/4432575344/
Applied direct: https://job-boards.greenhouse.io/nearform/jobs/7644791003

## Dedupe / requisition check
`python3 loop/dedupe.py --check "Nearform" "https://www.linkedin.com/jobs/view/4432575344/"` returned HIT COMPANY. A prior Nearform FDE row exists (2026-09-11, SUBMITTED, Greenhouse job 7834813003, Italy remote). Confirmed via Nearform's own Greenhouse jobs API that this is a genuinely different, country-specific requisition:
- US: 7619114003
- Italy: 7834813003 (already submitted 2026-09-11)
- Ireland: 7644791003 (this application)
- UK: 7619129003

Fetched job 7644791003's own content and matched it word for word against the LinkedIn JD (based in Ireland, travel to client sites in Europe, salary starts EUR75,000). Treated as a new, distinct requisition, not a duplicate.

## CV tailoring record (Prabhavit_CV_NearformFDE.tex/.pdf)
Built from Prabhavit_CV_EN.tex. Parity-diffed: every kept bullet verbatim, only reordering/pruning (plus two lines where sub-items within one bullet were reordered, no new text). Reused the same selection as the already-submitted Prabhavit_CV_Nearform.tex (Italy) since the job content is materially the same "Forward Deployed Engineer" agentic-platform role; swapped the photo asset to the current photo_small.jpg. Career Summary 2 bullets. FlowSpace >=3 bullets (RAG support agent, API integrations, migration/scale). UltraStrategy 2 bullets kept per AI/automation rule. Get2Germany kept Google APIs + AI automation tools bullets. 2 pages confirmed via pdfinfo.

## Cover letter (CoverLetter_NearformFDE.txt/.pdf)
FlowSpace (OfficeRnD/Nexudus integrations, live Next.js/Laravel migration, RAG support agent) as lead paragraph, paired with UltraStrategy (Affinda/Claude API CV-parsing pipeline) and Urlink (AI-assisted platform build, client automations) as the second proof paragraph, per the letter-evidence rule (never FlowSpace alone). Honest 3 years. Ireland work-authorisation transparency line verbatim from answers/work-authorisation.md: Ireland is explicitly excluded from the EU long-term-resident mobility directive (same as Denmark), so not authorised, needs the ordinary national employment permit, ready to relocate. 0 em-dashes (grep-verified). 305 words.

## Hard gates re-checked on live JD
"Significant experience delivering at a Senior Engineer level...typically at least 8 years"; core stack asks Python + LangGraph/CrewAI/AutoGen + Kubernetes, which Prabhavit cannot claim hands-on. Not a kill under the 2026-09-17 FDE-ALL rule (ignore fit/years/seniority/stack for FDE postings). No anti-AI disclaimer. No explicit non-English language requirement.

## Form fields (Greenhouse, job-boards.greenhouse.io/nearform/jobs/7644791003)
- First Name: Prabhavit / Last Name: Gupta / Email: prabhavitg@gmail.com
- Country: Italy +39 / Phone: +39 351 610 7807
- Location (City): Venice, Venezia, Italy (autocomplete selection)
- Resume/CV: Prabhavit_CV_NearformFDE.pdf (verified filename before submit)
- Cover Letter: CoverLetter_NearformFDE.pdf (verified filename before submit)
- LinkedIn Profile: linkedin.com/in/prabhavit
- How did you hear about Nearform: LinkedIn
- Are you currently residing in Ireland: No, I am not currently based in Ireland
- Do you require sponsorship to work in Ireland: Yes, I require sponsorship to work in Ireland
- Travel to client sites within Europe, able/willing: Yes, I am open/willing to do frequent travels within Europe
- Salary range: EUR 70,000 - 80,000 (the only bucket containing the JD's own stated floor of EUR75,000; no bucket below EUR60,000 was offered)
- Data Privacy: Confirm ticked

Confirmation: "Yay! You've submitted your application." at confirmations/NearformFDE-2026-09-17.txt
