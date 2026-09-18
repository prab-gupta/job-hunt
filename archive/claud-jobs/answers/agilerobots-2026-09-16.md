# Agile Robots SE - Forward Deployed Engineer for Robotics (Munich) - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4465201869/
Apply decodes to: https://job-boards.eu.greenhouse.io/agilerobotsse/jobs/4964789101

## Dedupe
`python3 loop/dedupe.py --check "Agile Robots SE" "https://www.linkedin.com/jobs/view/4465201869/"` = NEW.

## Hard gates
- No anti-AI disclaimer.
- English JD.
- No German-language requirement stated ("Fluency in English" is the only language line).
- Per USER RULE 2026-09-16: years (4+), Master's degree, and no-robotics-background are not kills.

## Outcome: KILLED (posting closed on the real ATS)
LinkedIn's "Apply on company website" link decodes (via LinkedIn's safety redirect) to `https://job-boards.eu.greenhouse.io/agilerobotsse/jobs/4964789101`. Navigating there directly returns HTTP 200 but lands on `https://job-boards.eu.greenhouse.io/agilerobotsse?error=true`, Greenhouse's own invalid-job-id error state, showing the company's general 63-open-role board instead. Searched that live board for "Forward Deployed", "Robotics", and "Deploy" keywords: no listing titled "Forward Deployed Engineer for Robotics" or anything close exists among the current 63 postings. The requisition has been pulled from Agile Robots' live Greenhouse board. LinkedIn's own jobs-guest API still reports `apply-button=1` (its cache has not caught up), so the cheap LinkedIn-side check alone would have missed this; the direct Greenhouse resolution is what surfaced it.

Per the brief's hard gates ("posting closed/404" = KILL), this is killed on that basis, independent of the task's fit/language-only kill rule for LI-PICK-style rows.

## Materials built before the closure was discovered (kept on file, not submitted)
- Prabhavit_CV_AgileRobots.tex/.pdf (2 pages): Career Summary kept the hands-on-LLM and AI-assisted-development/API-integration bullets; FlowSpace Product Responsibilities led with "Streamlined customer support with AI agents"; Technical Responsibilities led with the AI listing-bot bullets; Technical Skills reordered AI/ML first.
- CoverLetter_AgileRobots.pdf/.txt: FlowSpace (AI listing bot, support AI agents) paired with UltraStrategy (Affinda + Claude API CV-parsing pipeline integrated into a production platform) as the two proof paragraphs, honest gap paragraph naming no robot-arm/AGV/C++/VLA/NVIDIA-embedded experience, Germany work-authorisation transparency line. `grep -c` for U+2014 on the txt = 0.
