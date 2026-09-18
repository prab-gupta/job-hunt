# SSE Airtricity - Product Owner - 2026-09-09

Job: Product Owner, SSE Airtricity, Dublin, Ireland (50% week in Dublin office). Salary band EUR 65,300-97,900.
LinkedIn: https://www.linkedin.com/jobs/view/4464644501/
Apply-on-company-website target: https://careers.sse.com/jobs/product-owner-dublin-ireland-ireland (Job Number 559519)
ATS actually used: PageUp People, guest apply (no account/password), applicationID 2370280.

## CV tailoring (Prabhavit_CV_SSEAirtricity.tex/.pdf)
Built from Prabhavit_CV_EN.tex. Changes:
- Career Summary: kept 2 bullets ("Transformed business requirements into production-ready features..." and "Skilled in AI-assisted development, prompt engineering, and orchestrating complex API integrations."). Dropped: "AI Solutions & Automation Engineer with hands-on experience building LLM-driven applications and intelligent workflows across European tech projects."
- Technical Skills: reordered to Project/Design, AI/ML, Development, Automation (agile/collab tools first for a Product Owner audience).
- FlowSpace (kept 6 bullets, >= 3 required):
  - Product Responsibilities kept: "Collaborated with team of developers for product logic and business logic documentation", "Facilitated communication between internal team and Agency", "Scaled platform from 2000 to 4500+ users through iterative product development".
  - Product Responsibilities dropped: "Overseeing the migration of app from Bubble.io to Next.JS and Laravel" (duplicate also in Technical, less relevant to a data/analytics stakeholder-facing JD), "Streamlined customer support with AI agents" (less relevant to this specific data-product JD).
  - Technical Responsibilities kept: "AI tool for processing and scraping of data and increasing listings on platform", "Integration of external APIs (Office Rnd and Nexudus) for automated bookings", "Consolidated leads in CRM and automated lead capture by developing integration between CRM used by the organization".
  - Technical Responsibilities dropped: "GTM automations for sales funnel, lead enrichment and outbound", "AI tool for processing of data and increasing listings on platform" (duplicate), "Overseeing the migration..." (duplicate), "Developed a tool for companies to calculate commute times".
- Urlink: kept "Implementing automations in regards to client requirements"; dropped "Using AI for building the platform and logics", "Implementing UIs made with AI".
- UltraStrategy.com: kept "Developed platform for different user profiles"; dropped "Made a CV parsing tool using n8n and Eden AI".
- Qomodo: kept "Made a dashboard to be used by the companies to manage their branches"; dropped "Implementation of Figma designs".
- Get2Germany.com: kept "Integration of Google APIs for effective tracking of the platform" and "Building the platform, database optimization"; dropped "UI/UX work, design from Figma to Bubble", "Developed AI based automation tools for finding courses, internships and jobs".
- Clubee.com: kept "Developed tools for: domain integration, shop, federation dashboard"; dropped "Integration of Clubee API for all of frontend", "Unit testing and quality assurance of new features".
- Tractionboard.co: kept "ChatGPT/OpenAI integration"; dropped "Implementation of designs from Figma to Bubble", "Implementation of Sendgrid", "Responsive designs, de-bugging", "Google Ads 4 implementation".
- Additional Information: removed "Low code development/" prefix from the IT Skills line (JD has no relation to low-code/Bubble); reordered so Project Management, Communication comes first; reordered Tools line to put Jira, Slack first.
- No sentence rewritten, no new claims added. 2 pages after tectonic compile (verified with pdfinfo). Parity check: normalized every pdftotext line >25 chars against the base .tex text; only mismatches were font-icon glyph garbling in the header (cosmetic, FontAwesome ligatures) and the two intentionally reordered skills/tools lines (permitted reordering, same tokens).

## Cover letter (CoverLetter_SSEAirtricity.txt/.pdf, 227 words)
Traceable to Prabhavit - Master Experience.md: FlowSpace product-logic/business-logic collaboration, internal-team/agency point of contact, OfficeRnD + Nexudus integrations, CRM lead consolidation/automation, 2,000->4,500+ user scaling. No em-dashes (grep -c "—" = 0). No "no-code"/"low-code"/"Bubble" wording. No Claude/Anthropic mention.

## Form answers given (PageUp guest-apply, 5 steps)
1. Begin application: email prabhavitg@gmail.com.
2. Save time / resume pre-fill: uploaded Prabhavit_CV_SSEAirtricity.pdf to the parse-and-prefill widget (parsing failed server-side, sPrefillMessage=PREFILL_ERROR, so all personal fields were filled manually in step 3 - no data lost).
3. Personal details: Title Mr, First name Prabhavit, Last name Gupta, Email prabhavitg@gmail.com, Home address "Via Zanetti, 10", City/Town Venice, Country Italy, County/Province Venezia, Postcode 30175, Phone +39 351 610 7807.
4. CV and Employment Details:
   - CV upload: Prabhavit_CV_SSEAirtricity.pdf (formal attach, separate from the earlier pre-fill widget).
   - Cover Letter upload: CoverLetter_SSEAirtricity.pdf.
   - "Do you have the right to work in the UK or Ireland?" -> "No, I will require assistance / sponsorship" (per answers/work-authorisation.md: Ireland is outside the EU long-term-resident mobility directive, authorised No / sponsorship Yes).
   - "Are you currently employed by the SSE Group?" -> "No, I have never worked for the SSE Group." (hid the conditional redeployment/department/line-manager follow-up questions, confirmed via DOM display:none / no offsetParent).
   - "Please confirm your current salary and benefits package?" (free text) -> "I currently work as an independent freelance contractor, with day rates in the region of EUR 250 to 300 depending on the engagement, and no fixed benefits package. My salary expectation for this role is around EUR 65,300, in line with the advertised band." (per task instruction to state EUR 65,300, the bottom of the JD's EUR 65,300-97,900 band, honestly framed around actual freelance/day-rate status per Prabhavit - Master Experience.md salary notes.)
   - "Do you have a full, current driving licence?" -> "No, I do not have a full, current driving licence." (no evidence in master file that Prabhavit holds one; declined rather than fabricate).
5. SSE Equal Opportunities Commitments: Disability, Ethnic Origin, Age range, Gender, Sexual orientation, Relationship status, Religion, Socio-economic occupation, Socio-economic school type all answered "Prefer not to say". "Is the role you are applying for based in Northern Ireland?" -> "No" (Dublin is in the Republic of Ireland; the conditional Protestant/Catholic/neither community-background question stayed hidden as a result).
6. Submit application page: "How did you hear about this opportunity?" -> LinkedIn (native <select>, distinct widget from the custom comboboxes used elsewhere on the form).

Cookies: declined optional/performance cookies on the careers.sse.com landing page ("I do not accept").
Years of experience: not asked as a distinct field on this ATS form (no bucket/numeric field presented).
EEO: declined to self-identify on every category, per standing instruction.
