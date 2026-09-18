# Club Magellano - Sviluppatore web junior - 2026-09-11

LinkedIn Easy Apply: https://www.linkedin.com/jobs/view/4461123786/
Tavazzano con Villavesco (Lodi), Italy, on-site. JD saved to
/private/tmp/claude-501/-Users-prab/237a3cff-dd16-4810-8bd3-960e29fe6c44/scratchpad/jd/4461123786.txt
(Italian). Stack: Vue.js, PHP vanilla, Laravel, WordPress, custom solutions; REST API integration;
frontend + backend; collaboration with marketing/customer care. Entry-level stage (internship contract)
with concrete path to permanent hire. No anti-AI disclaimer in the JD.

## Dedupe
`python3 loop/dedupe.py --check "Club Magellano" "https://www.linkedin.com/jobs/view/4461123786/"` -> NEW.
`grep -i "magellano" applications.csv` -> no hits. Cheap check: apply-button count 1 (open).

## Hard gates
Not Senior/Staff/Lead/Principal/Manager, no MSc/PhD requirement, JD in Italian but role does not require
Italian at any specific level (standing rule: Italian JD -> Italian letter, CV stays English), core stack
is Laravel/PHP which Prabhavit can claim, on-site in Italy (no remote-from-Italy issue since it already
is Italy). Not a kill.

## CV
Prabhavit_CV_ClubMagellano.tex / .pdf built from Prabhavit_CV_EN.tex, tectonic-compiled, 2 pages. Diff vs
original (verbatim bullets only, reorder/prune only, no rewrites, no new claims):
- Career Summary: dropped the "AI Solutions & Automation Engineer... LLM-driven applications" bullet
  (heaviest AI framing, least relevant to a plain junior web dev role), kept the two most
  general-web-dev-relevant bullets (API integrations bullet; production-ready features + QA testing
  bullet).
- Technical Skills: reordered categories Development (Laravel, Typescript) and Project/Design (Figma,
  Jira, GitHub, Postman, Trello) first since they match the JD's PHP/Laravel/API stack most directly;
  AI/ML and Automation moved after.
- FlowSpace Product Responsibilities: moved "Overseeing the migration of app from Bubble.io to Next.JS
  and Laravel" to the top (Laravel/backend match).
- FlowSpace Technical Responsibilities: reordered so "Integration of external APIs (Office Rnd and
  Nexudus) for automated bookings" (REST API match), the Laravel migration line, and "Developed a tool
  for companies to calculate commute times" (feature dev) lead; AI data-processing and CRM/GTM
  automation bullets moved after. Nothing deleted, still well above the 3-bullet FlowSpace minimum.
  This JD is plain web development, not AI/automation, so the brief's UltraStrategy/Get2Germany
  AI-JD minimum (2 bullets each) does not apply; both roles already carry their existing bullets
  unchanged (UltraStrategy 2, Get2Germany reordered only).
- Get2Germany: reordered "Integration of Google APIs..." and "Building the platform, database
  optimization" ahead of the UI/UX and AI-automation-tools bullets (API integration + platform building
  are the closest match to this JD); nothing deleted.
- Other roles (Urlink, UltraStrategy, Qomodo, Clubee, Tractionboard): left as-is, each already has at
  least 1 bullet and Clubee's existing bullets (API integration across frontend; unit testing and QA)
  are already highly relevant without needing reorder.
- Additional Information: dropped "Low code development/AI based development" from IT Skills per the
  tailoring rule (this JD has no relation to low-code/Bubble); reordered the remaining IT Skills items so
  "AI (RAG, Chatbot) and API integration" leads (API integration is the JD match); Tools reordered
  Laravel and Typescript first.

## Letter
CoverLetter_ClubMagellano.txt / .tex (Italian, "voi" plural, no em-dash, 271 words). Em-dash check:
`grep -c "$(printf '\xe2\x80\x94')" CoverLetter_ClubMagellano.txt` = 0. Two proof paragraphs per the
brief's letter-evidence rule: FlowSpace (automated migration to Next.js+Laravel live in production,
2,000->4,500+ users, OfficeRnD/Nexudus API integrations) as lead, Get2Germany (Google API integration,
database optimisation, automated course/internship/job-search tools) as second proof. Clubee (API
integration across the frontend, unit testing and QA) appears as a one-line aside per the map's rule for
that role, since the JD asks for exactly that combination. States 3 years plainly, Venice residence,
availability to relocate to Tavazzano con Villavesco, Italian EU long-term resident authorised to work in
Italy without sponsorship, Italian level stated honestly as "intermedio".

## Standing answers used
Years of experience: 3. Salary: junior band, if asked answer EUR 30,000-40,000 (this is a junior/stage
role, the standard 45-55k band does not fit). Italy: authorised Yes, sponsorship No. Relocation: Yes to
Tavazzano con Villavesco. Italian: intermediate/conversational, never fluent/native.
