# Atlassian - Principal Forward Deployed Engineer, AI (Remote Poland) - 2026-09-16

Row status: NEEDS YOU (RETRY PLAYWRIGHT). Not submitted, nothing filled.

## Re-check evidence
- LinkedIn: https://www.linkedin.com/jobs/view/4466315412/ - Apply on company website, "Responses managed off LinkedIn".
- Destination: https://globalcareers-atlassian.icims.com/jobs/27182/principal-forward-deployed-engineer,-ai-(remote-poland)/job (Atlassian's own careers portal, iCIMS-hosted, not Greenhouse as the task note guessed). No Polish-language requirement anywhere in the JD.
- Blocker: the job page renders its actual content and the "Apply for this job" form inside a nested iCIMS content iframe. Claude in Chrome's find/read_page tools cannot see anything inside it (confirmed on both the widget-embed URL and the plain job URL with tracking params stripped); a JS probe of document.querySelectorAll('iframe') also could not read the frame's src (cross-origin block). This is the same pattern already logged this session for Databricks, Auterion and DataSnipper. Per the browser-ownership rule, stopped here and logged RETRY PLAYWRIGHT rather than opening Playwright myself.

## Hard gates
- No anti-AI disclaimer. English JD. No Polish requirement.
- Title is "Principal" and wants 10+ years backend plus 5+ years production AI/ML (founding/forward-deployed 0-to-1 experience). Large seniority/years gap; per this session's FDE-ALL override this does not kill the row. Letter states the gap plainly.
- Listing says "This role is available remotely anywhere in Poland" - the pitch in the letter is remote-from-Italy, with the Poland transparency line as the honest fallback since the req itself is scoped to Poland employment.

## Materials
- Prabhavit_CV_Atlassian.pdf/.tex - fresh build from Prabhavit_CV_EN.tex, 2 pages. AI/ML skills category led (agentic/AI-ML-heavy JD), FlowSpace Technical/Product Responsibilities reordered to lead with API integrations and AI agents, UltraStrategy both bullets kept, Get2Germany three relevant bullets kept, "UI/UX Figma to Bubble" bullet dropped.
- CoverLetter_Atlassian.pdf/.tex/.txt - 0 em-dashes (grep confirmed). Opens with the honest 3-years-vs-10-plus-years and stack framing, FlowSpace as lead evidence (AI listing bot, support AI agents, OfficeRnD/Nexudus, CRM/GTM automations), UltraStrategy as second evidence (CV-parsing pipeline), Claude Code daily-use line, and closes with the remote-from-Italy pitch plus the Poland work-authorisation transparency line.

## Field values for the Playwright pass
- Name: Prabhavit Gupta. Email: prabhavitg@gmail.com. Phone: +39 351 610 7807. LinkedIn: linkedin.com/in/prabhavit.
- Resume: Prabhavit_CV_Atlassian.pdf. Cover letter (if a field exists): CoverLetter_Atlassian.pdf or paste the .txt.
- Years: 3. Salary: EUR 45,000-55,000, band bottom.
- Work authorisation (Poland): not authorised, sponsorship/employer-side permit needed; open to discussing a remote-from-Italy arrangement.
- Italian: conversational/intermediate. English: professional/C2.
