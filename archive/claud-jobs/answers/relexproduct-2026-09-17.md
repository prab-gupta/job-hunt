# RELEX Solutions — Product Engineer (Greater Venice area)

Job (LinkedIn, offsite apply): https://www.linkedin.com/jobs/view/4467704517/
Date: 2026-09-17
Slug: RELEXProduct

## Gate check
- LI-PICK row (user standing rule 2026-09-11/2026-09-16): apply regardless of fit/years/seniority/stack. Kill only if closed, same requisition already SUBMITTED, or a language he lacks is required.
- JD text checked for anti-AI disclaimer: none found (grep clean).
- No hard-gate language requirement beyond "fluent in written and spoken English" (has C2 English). No non-English requirement.
- Dedupe: `dedupe.py --check "RELEX Solutions" <url>` = HIT COMPANY. `grep -i relex applications.csv` showed one prior row: 2026-09-06 SUBMITTED, "Forward Deployed Engineer | Merchandising", Greenhouse job-boards.greenhouse.io/relex/jobs/7901313003. Different title, different requisition, different ATS URL from this LinkedIn posting (which offsite-redirects to RELEX's own careers site). Not the same requisition, so proceeded per task instructions.
- Location: Greater Venice area matches Prabhavit's actual location (Venice, Italy) — role is performed in Italy, so standard Yes/No sponsorship pattern applies, no relocation transparency line needed.

## CV tailoring (Prabhavit_CV_RELEXProduct.tex/.pdf, built from Prabhavit_CV_EN.tex)
- Career Summary: kept bullet 1 (AI Solutions & Automation Engineer / LLM-driven apps and intelligent workflows) and bullet 3 (business requirements to production-ready features, AI agents, LLM data parsing, rigorous QA) — matches the JD's product-ownership-through-QA framing. Dropped bullet 2 (prompt engineering/API orchestration, less relevant here).
- FlowSpace Product Responsibilities: reordered to lead with "Scaled platform from 2000 to 4500+ users through iterative product development" (matches "own your deployed product and iterate fast") then "Streamlined customer support with AI agents" (customer-facing), then documentation/collaboration, then the migration bullet, then agency communication. All 5 bullets kept verbatim.
- FlowSpace Technical Responsibilities: led with the AI data-processing/listing bullet (AI/ML + data, matches "designing solutions spanning data, AI/ML, UX, and system integration"), then OfficeRnD/Nexudus API integration (system integration), then CRM integration, then GTM automations. Deduped the repeated "AI tool for processing... listings" line (appears twice in the master) and dropped the commute-time-calculator bullet as clearly irrelevant to this JD (same dedup/drop already applied in the precedent Prabhavit_CV_GitLab.tex).
- UltraStrategy / Get2Germany: JD covers AI/ML + agentic engineering exposure, so treated as an AI/automation JD per the tailoring rule and kept both UltraStrategy bullets (of 2) and all 4 Get2Germany bullets (exceeds the min 2).
- Urlink, Qomodo, Clubee, Tractionboard: left as in the master, minimums satisfied (>=1 each).
- Technical Skills: reordered to AI/ML, Development, Automation, Project/Design (Development promoted ahead of Automation given the JD's "solid software engineering and DevOps skills" ask).
- Additional Information IT Skills: dropped the "Low code" phrase (JD has no relation to it) — same wording as the precedent GitLab CV: "AI-based development (RAG, Chatbot) and API integration, Automation (n8n), Project Management, Communication".
- Parity check: every remaining bullet verified verbatim against Prabhavit_CV_EN.tex (script diff, only the sanctioned IT Skills line differs). 2 pages with photo, compiled with tectonic.

## Cover letter (CoverLetter_RELEXProduct.tex/.pdf/.txt, English)
- Two proof paragraphs per the letter-evidence rule: FlowSpace (lead — marketplace ownership, AI listing bot, support AI agents, OfficeRnD/Nexudus DevOps) paired with Urlink (PM + AI-assisted platform build + translating client requirements into automations, close match to "translate customer needs... into priorities" and being customer-facing).
- No em-dashes (checked, count 0). No mention of the legacy platform's original brand. Closing states Greater Venice location, Italy work authorisation Yes / sponsorship No.
- ~280 words.

## Standing answers to use on the form
- Years: 3. Salary: EUR 45000 (task override; JD states no band). Location: Venice, Italy / Greater Venice area. Work authorisation: Yes, no sponsorship (role is in Italy). Languages: English C2, Italian conversational B1-B2, Hindi native. Notice: immediate, start two weeks after offer. Relocation: Yes (moot, already local). How did you hear: LinkedIn.

## Playwright completion (agent P36, 2026-09-17)

Custom question answer: "Describe a time you built and deployed a solution to a complex customer or business problem using an existing engineering framework or platform. What was your role, and what was the outcome?"
- FlowSpace AI listing bot: pipeline turns a provider brochure in any format into a drafted listing with a human review, built on the existing Next.js and Laravel stack. Role: owned data schema, review workflow, and production rollout. Outcome: 900+ listing drafts, large cut in manual data entry. Second sentence: the legacy-platform-to-Next.js/Laravel migration while live, 2,000 to 4,500+ users.

Other answers:
- Are you fluent in English: Yes
- Are you currently based in one of our mentioned office locations: Yes (posting location is Greater Venice, matches home address, honest per LI-PICK never-inflate rule)
- Legal work permit for the mentioned office locations: Yes (Italian EU long-term resident, authorised in Italy, no sponsorship)
- Monthly salary expectations: EUR 3,750 gross/month (approx. EUR 45,000 gross/year) - task specified EUR 45000 annual, converted to the field's monthly ask, same pattern as answers/sixt-2026-09-11.md
- Privacy policy confirmation: Yes

Submitted successfully via Playwright (direct boards.greenhouse.io URL redirected back to the relexsolutions.com embed, but Playwright's frame-aware locators reached every field regardless). Confirmation: "Thank you for applying. / Your application has been received. Please check your email for further details."
