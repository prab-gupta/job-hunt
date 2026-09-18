# Stern Stewart & Co. (SITECO) - AI Solution Engineer for our Portfolio Companies - 2026-09-10

Role: AI Solution Engineer for our Portfolio Companies, Munich, Germany (LinkedIn Easy Apply)
URL: https://www.linkedin.com/jobs/view/4464518989/
Lane C, fit 65.

## Hard gates re-checked on live JD
- Years required: none stated numerically. Not a gate fail.
- Title: "AI Solution Engineer" - not Senior/Staff/Lead/Principal/Manager/CTO. Pass.
- Degree: "You hold a Bachelor's or Master's degree in Computer Science, AI, Data Science, or a related field - or bring equivalent practical experience." Not a hard MSc requirement. Pass.
- Language: JD entirely in English, no German requirement stated. Pass.
- Core stack: "Python and TypeScript are part of your toolkit" - both claimable. Not Java/.NET/C++/Go/Rust/Django/FastAPI-core/cloud-admin. Pass.
- Location: Munich, Germany, Hybrid, Full-time - EU location. Pass.
- Anti-AI disclaimer: none found in JD. Pass.
- Posting status: no "Application submitted" panel, no "no longer accepting applications" banner; Easy Apply button present, 50 applicants shown. Pass.

Verdict: all gates pass, proceeding.

## Dedupe
`python3 loop/dedupe.py --check "Stern Stewart" "https://www.linkedin.com/jobs/view/4464518989/"` -> NEW.
`grep -i "stern\|siteco" applications.csv` -> no rows. Clean, no block.

## CV tailoring (Prabhavit_CV_SternStewart.tex/.pdf, 2 pages, tectonic)
Career Summary: kept bullets 1 and 3 (LLM-driven applications/intelligent workflows; production-ready features/AI agents/LLM data parsing/QA). Dropped: "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations."

Technical Skills: reordered Development first, then AI/ML, Automation, Project/Design (no items deleted).

FlowSpace (min 3 required, kept 7):
- Product Responsibilities kept, reordered: migration to Next.JS/Laravel, AI agents for customer support, scaled 2000->4500+ users. Dropped: "Collaborated with team of developers for product logic and business logic documentation", "Facilitated communication between internal team and Agency".
- Technical Responsibilities kept, reordered: AI tool for processing/scraping data, OfficeRnD/Nexudus API integration, CRM integration, GTM automations. Dropped: duplicate "AI tool for processing of data and increasing listings on platform", duplicate migration bullet (already in Product), "Developed a tool for companies to calculate commute times".

Other roles (min 1 required):
- Urlink: kept "Using AI for building the platform and logics". Dropped "Implementing UIs made with AI", "Implementing automations in regards to client requirements".
- UltraStrategy.com: kept "Made a CV parsing tool using n8n and Eden AI". Dropped "Developed platform for different user profiles".
- Qomodo: kept "Made a dashboard to be used by the companies to manage their branches". Dropped "Implementation of Figma designs".
- Get2Germany.com: kept "Developed AI based automation tools for finding courses, internships and jobs", "Building the platform, database optimization". Dropped "Integration of Google APIs for effective tracking of the platform", "UI/UX work, design from Figma to Bubble".
- Clubee.com: kept "Unit testing and quality assurance of new features", "Integration of Clubee API for all of frontend". Dropped "Developed tools for: domain integration, shop, federation dashboard".
- Tractionboard.co: kept "ChatGPT/OpenAI integration", "Responsive designs, de-bugging". Dropped "Implementation of designs from Figma to Bubble", "Implementation of Sendgrid", "Google Ads 4 implementation".

Additional Information: IT Skills item "Low code development/AI based development" -> kept only the "AI based development" half (JD has no relation to low-code; precedent from prior tailored CVs, e.g. Prabhavit_CV_Axis.tex, which split this same compound item the same way). Tools line reordered: Typescript, Laravel, Claude Code, Supabase, n8n, Jira, Slack.

Parity check: pdftotext (no -layout) vs LaTeX-stripped base Prabhavit_CV_EN.tex, normalized for ligatures/dashes/whitespace. 51 lines >25 chars checked, 49 exact hits; 2 near-misses are the reordered Additional Information lines ("IT Skills..." and "Tools...") where every individual token exists in the base text, just in a different order (intentional per tailoring rule 4) plus one artificial pdftotext line-wrap split. No fabricated content.

## Cover letter (CoverLetter_SternStewart.txt/.pdf, 245 words)
Claims traced to `Prabhavit - Master Experience.md`: FlowSpace lead developer ~3 years, migration off legacy stack to Next.js/Laravel while live, 2,000->4,500+ users, AI listing pipeline (n8n, TypeScript, LLM API, brochure-to-draft-listing, human reviewer), support AI agents with confidence-based escalation, CRM/GTM automations, OfficeRnD/Nexudus integrations, stack TypeScript/Python/Node.js/Laravel/REST APIs/Git/Postgres, Venice Italy + Italian EU long-term resident status, Germany work-authorisation transparency line, ready to relocate to Munich.
No em-dashes (`grep -c "—"` = 0). No "no-code"/"low-code"/"Bubble" wording. No mention of Claude/Anthropic (rewrote the pipeline description to say "an LLM API" instead of naming Claude, since only "Claude Code" as a dev tool is exempted, not the model/API name).

## Screening answers used
- Years of professional experience: 3 (bucket containing 3, e.g. "2-3" or "3-5" per standing rule).
- Germany work authorisation: authorised to work in Germany = No; will require employer-side permit/sponsorship = Yes; transparency line (from answers/work-authorisation.md, relocation-role version) pasted into any free-text field: "I hold Italian EU long-term resident status. I am not currently authorised to work in Germany and would need the applicable employer-side permit or sponsorship process. I am ready to relocate and complete that process."
- Willing to relocate to Munich: Yes.
- Salary expectation: EUR 50,000 (or 45,000-55,000 band if a range field).
- English: C1/professional. German: none claimed.
- How did you hear about this job: LinkedIn.
