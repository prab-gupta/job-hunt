# hello again - AI Solutions Engineer (d/f/m) - 2026-09-16

Source: https://www.linkedin.com/jobs/view/4464778729/ (Leonding or Vienna, Austria, on-site/hybrid)

## Dedupe
`python3 loop/dedupe.py --check "hello again" "https://www.linkedin.com/jobs/view/4464778729/"` -> NEW. No matching company row in applications.csv or NEEDS_YOU.md.

## Hard gates (checked on live LinkedIn guest JD text)
- Seniority: LinkedIn metadata "Not Applicable"; title "AI Solutions Engineer" - not Senior/Staff/Lead/Principal/Manager/CTO.
- Years: no explicit years-required clause; qualifications are described as a "background in tech consulting, solution engineering, or applied AI", not a year count.
- Degree: no MSc/PhD requirement anywhere in the JD.
- Language: "Language: Professional English skills; German is a welcome plus." JD is fully in English (not German-only), so an English letter applies, not a kill.
- Core stack: Python (Pandas, basic ML frameworks), OpenAI/Anthropic/LangChain APIs, RAG/grounding, LLM integration, applied/pragmatic classical ML on tabular data - all within the claimable list (LLM APIs, RAG, Python for pipelines/automation). Not a Java/.NET/Go/Rust-core or Django/FastAPI-core role, no cloud-admin requirement.
- Anti-AI disclaimer: grepped the guest-API JD text, no hits.
- Location: on-site Leonding or Vienna, Austria - outside Italy, so the Austria work-authorisation transparency line applies (not remote-from-Italy).

All gates pass.

## CV
Built `Prabhavit_CV_HelloAgain.tex`/.pdf from `Prabhavit_CV_EN.tex`. Parity checked via item-line diff; only differences are reordering (AI/ML skills category first, IT Skills/Tools reordered to lead with AI/RAG and n8n/Claude Code) - no invented claims. Compiled 2 pages with photo.

JD is squarely AI/automation and solution-engineering themed (LLM integration, RAG grounding, use-case design, business translation, rapid prototyping), matching the task's specified angle (UltraStrategy pipeline + FlowSpace client automations). Kept 2 UltraStrategy bullets (CV-parsing pipeline with n8n/Eden AI, platform for different user profiles) and 2 Get2Germany bullets (AI automation tools for courses/internships/jobs, Google APIs) per the AI-themed tailoring rule, plus 3 FlowSpace bullets (support AI agents, AI data-processing tool, GTM/CRM automation) and 1 bullet each for the remaining roles, picking the ChatGPT/OpenAI integration bullet for Tractionboard as the closest match to "LLM Integration & Grounding".

## Cover letter
`CoverLetter_HelloAgain.tex`/.pdf/.txt, written in English (JD is in English, not German-only). Two-role evidence per the task-specified angle: UltraStrategy (CV-parsing pipeline: extraction with Affinda/Claude API, relevance scoring, platform for user profiles) as lead, paired with FlowSpace (support AI agents with confidence-based escalation, the AI listing-drafting tool, CRM/GTM automation) as the second paragraph. States Python/TypeScript, LLM APIs (Claude API, OpenAI), RAG grounding, and n8n pipelines. Includes the Austria transparency line from `answers/work-authorisation.md` ("I am not currently authorised to work in Austria and would need the applicable employer-side permit or sponsorship process, and I am ready to relocate to Leonding or Vienna and complete that process"). No em-dashes (grep on compiled .txt returned 0).

## Easy Apply flow (4 pages, LinkedIn UI rendered in German on this posting)
1. Contact info (Kontaktinfo): email prabhavitg@gmail.com (prefilled/selected), phone country code Italy +39 (prefilled), Handynummer (phone number) field blank - typed 351 610 7807.
2. Lebenslauf (resume): pre-selected file was Prabhavit_CV_Antal.pdf (leftover from the prior row). Clicked "Upload resume" and explicitly uploaded Prabhavit_CV_HelloAgain.pdf; verified its radio button was checked.
3. Weitere Fragen (additional questions), two required radio questions:
   - "Koennen Sie sich vorstellen, vor Ort zu arbeiten?" (Can you imagine working on-site?) - answered Ja (Yes), matching the standing "Hybrid/on-site: Yes" answer.
   - "Sind Sie rechtlich befugt, in diesem Land zu arbeiten: Oesterreich?" (Are you legally authorised to work in this country: Austria?) - answered Nein (No), matching the standing work-authorisation table (any country other than Italy = not authorised, needs employer-side permit/sponsorship).
   Verified both radios showed `[checked]` in the accessibility tree before proceeding.
4. Review: confirmed CV filename (Prabhavit_CV_HelloAgain.pdf) was correct, unchecked "Follow hello again", clicked Submit application.

## Result
"Application submitted" shown in the job page's own Application status panel immediately after submit. Screenshot: confirmations/HelloAgain-2026-09-16.png. Confirmation text: confirmations/HelloAgain-2026-09-16.txt.
