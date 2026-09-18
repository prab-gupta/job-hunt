# Harmattan AI - Forward Deployed Software Engineer - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4468214613/
Apply routes to: https://jobs.ashbyhq.com/harmattan-ai/361b01cd-1e9a-4827-9bcc-36b8aa403aa3/application (Ashby)
Status: SUBMITTED

## Dedupe
`python3 loop/dedupe.py --check "Harmattan AI" "https://www.linkedin.com/jobs/view/4468214613/"` -> NEW.
Note: a different Harmattan posting (Founding FDE) was dropped earlier in this batch for a years clause per the
task instructions; this Forward Deployed Software Engineer req is a separate requisition and the standing rule
explicitly said to apply to it.

## Standing rule applied
USER RULE 2026-09-16: apply to every FDE posting in Italy/EU on LinkedIn, no kills for fit/years/seniority/
agency/stack. JD requires "4+ years building and shipping production software, in Python and at least one
lower-level language (C++, Rust, Go)" - years and core-stack language both waived under the standing rule.
"Proficiency in English is mandatory" - satisfied (C2). No other language required in the JD text.

## Hard gates re-checked on the live Ashby form
No anti-AI disclaimer. English JD and English-only resume requirement (satisfied). Not closed. Defense-sector
company (Harmattan AI, autonomous defense systems) - not a listed kill criterion under the brief or the standing
rule, so not treated as a block.

## Fields and answers
- Name -> Prabhavit Gupta
- Email -> prabhavitg@gmail.com
- "Why are you interested in Harmattan AI?" -> honest pitch built from the FlowSpace live-migration + AI-agents
  track record, explicitly framed as wanting to apply that end-to-end ownership to a higher-stakes domain (no
  invented defense/robotics experience).
- "How did you hear about us?" -> LinkedIn
- "What are your salary expectations?" -> EUR 45,000 (this batch's stated target; JD gives no band)
- "When can you start?" -> "Available immediately, ready to start within two weeks of an offer. I hold Italian
  EU long-term resident status and am not currently authorised to work in France; I would need the applicable
  employer-side permit or sponsorship process, and I am ready to relocate to Paris and complete that process."
  (work-authorisation.md relocation transparency line, folded in here since no dedicated visa field existed)
- "Do you have the Right to Work in France?" -> No (per work-authorisation.md: EU country other than Italy =
  not automatically authorised)
- Resume (English only, required) -> Prabhavit_CV_Harmattan.pdf
- "Are you willing to relocate to Paris?" -> Yes

## Materials built
Prabhavit_CV_Harmattan.pdf (2 pages, same AI/FDE tailoring pattern as DataSnipper/Parallel: career summary
trimmed to 2 bullets, FlowSpace AI-agent/production bullets led, all content verbatim from Prabhavit_CV_EN.tex).
CoverLetter_Harmattan.tex/.txt written (no upload field existed on the Ashby form, so the letter's substance was
folded into the "Why are you interested" answer instead; the standalone letter file is kept on record). Lead
role FlowSpace (live migration + AI listing bot + support AI agents), paired with Get2Germany (API integrations,
automation tools), explicitly honest that his production language background is TypeScript/PHP rather than
Python plus C++/Rust/Go. 0 em-dashes (grep-verified on the .txt).

## Bug encountered and fixed
Ashby's "How did you hear about us?" textbox on this form showed the filled value "LinkedIn" but the form's own
validation rejected the submission with "Missing entry for required field: How did you hear about us?" - a
React-state desync similar to the documented Chrome/Ashby form_input issue, but here triggered via Playwright's
fill(). A double-fill (retype from a cleared field) then a blur click fixed it before the second submit attempt
succeeded.
