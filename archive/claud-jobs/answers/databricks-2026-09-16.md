# Databricks - AI Forward Deployed Engineer, France - 2026-09-16

URL (LinkedIn): https://www.linkedin.com/jobs/view/4465994667/
Apply form (Greenhouse embed on Databricks' own careers site): https://www.databricks.com/company/careers/professional-services-operations/ai-forward-deployed-engineer---france-8813516002?gh_jid=8813516002&gh_src=62a881d62
Req ID: CSQ427R333 / gh_jid 8813516002 (different requisition from the earlier SKIP rows for gh_jid 8747605002, Amsterdam - non-blocking).

## Why stopped
The LinkedIn "Apply" button opens the Databricks careers page above, which renders the Greenhouse application form inside a cross-origin iframe. Confirmed with Claude in Chrome's `find` tool: searching for "First Name input field" returned "not present in the accessibility tree" even though the form was clearly visible on screen (screenshot showed First Name/Last Name/Preferred First Name fields). Cross-origin iframes are invisible to the accessibility tree Claude in Chrome relies on for `find`/`read_page`/`form_input`/`file_upload` refs, so the Resume/CV upload control (a required field) cannot be reached from Chrome. Per the brief's "Browser alternative" section this is exactly the documented Greenhouse cross-origin-iframe case: stop and hand off to Playwright rather than fight the iframe from Chrome, and never open Playwright myself (shared browser, other agents may be using it).

## Full known field values (visible on screen, gathered via screenshots/scrolling; not entered anywhere)
- First Name: Prabhavit
- Last Name: Gupta
- Preferred First Name: (leave blank)
- Resume/CV (required, Attach/Dropbox/Enter manually, accepts pdf/doc/docx/txt/rtf): upload `Prabhavit_CV_Databricks.pdf` (tailored from Prabhavit_CV_EN.tex, parity-diffed - reorder/delete only, no invented claims, 2 pages, compiled with tectonic)
- Cover Letter (Attach/Dropbox/Enter manually, same accepted types): upload `CoverLetter_Databricks.pdf` (or paste `CoverLetter_Databricks.txt` if only "Enter manually" text box is usable)
- LinkedIn Profile* (required text): https://www.linkedin.com/in/prabhavit/
- How did you hear about this job? (free text, optional): LinkedIn
- "Please confirm whether you are based in France or are willing to relocate there. The office is based in Paris and will require you to come in regularly for team or client meetings."* (dropdown): pick the "willing to relocate" option (he is Venice, Italy based, not France; standing answer = relocation Yes, anywhere in the EU, comfortable with regular on-site time)
- "Are you legally authorized to work in the country in which you are applying?"* (dropdown): No - per answers/work-authorisation.md, France is a different EU country from Italy; EU long-term residence in Italy does not auto-authorise work in France
- "Do you now or will you in the future need sponsorship for employment visa status in the country in which you are applying?"* (dropdown): Yes
- Sanctions/export-control checkboxes* ("Citizen or permanent resident of Cuba, Iran, North Korea, or Syria" / Crimea-Donetsk-Luhansk-Zaporizhzhia-Kherson resident / Russia-or-Belarus resident-not-willing-to-relocate / "None of the above")*: check "None of the above"
- Follow-up immigration-status checkboxes* (U.S. citizen / U.S. non-citizen national / U.S. permanent resident / asylum / refugee / other-country citizenship / other-country permanent residency / "None of these apply to me" / "Not applicable (i.e., I selected 'none of the above' for the prior question)")*: check "Not applicable (i.e., I selected 'none of the above' for the prior question)"
- "Do you currently or have you previously worked for Databricks in the past?"* (dropdown): No
- Submit application button at the bottom

## Work authorisation transparency line used in the letter (France, per answers/work-authorisation.md)
"I hold Italian EU long-term resident status. I am not currently authorised to work in France and would need the applicable employer-side permit or sponsorship process. I am ready to relocate and complete that process."

## Materials ready
- Prabhavit_CV_Databricks.tex / .pdf (2 pages, parity-diffed against Prabhavit_CV_EN.tex: FlowSpace AI-agents bullet led, UltraStrategy both AI bullets kept, Get2Germany AI-automation-tools bullet led, Tractionboard trimmed to the ChatGPT/OpenAI + Sendgrid bullets - dropped Google Ads/responsive-design/Figma-to-Bubble as JD-irrelevant)
- CoverLetter_Databricks.tex / .pdf / .txt (0 em-dashes, grep-verified; two evidence paragraphs, FlowSpace lead + UltraStrategy pair, Get2Germany named as an aside; states 3 years plainly; France transparency line)

Nothing was submitted. No account was created.
