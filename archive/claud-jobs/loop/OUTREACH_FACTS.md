# OUTREACH_FACTS.md

Canonical facts for cover letters, tailored CVs and cold outreach emails. Sources: `Prabhavit - Master Experience.md` (20 Aug 2026) and Prabhavit's voice note of 10 Sep 2026. If a claim is not on this page, do not make it.

## 1. The rule

Every cover letter, CV summary and outreach email must draw on at least two roles. Pick the role nearest to the job description as the lead example and pair it with at least one more. Never present FlowSpace alone. Prabhavit has worked at eight European companies in about three years, and for most AI and automation roles the CV-parsing work at UltraStrategy, the AI-assisted platform build at Urlink and the API and search automations at Get2Germany are as relevant as FlowSpace. Use FlowSpace for scale, live migration, marketplace operations and production AI agents. Always describe the FlowSpace origin as "a legacy stack" and never name the old platform.

Style for anything written from this file: no em-dashes, plain sentences, British or neutral English, no attribution lines for AI tools (naming the Claude API or Claude Code as tools used in the work is fine).

## 2. Role to JD mapping

| JD theme | Lead role | Pair with |
|---|---|---|
| CV parsing, document AI, data extraction, HR or recruiting tech | UltraStrategy | FlowSpace listing bot (brochure to structured listing) or the llm-doc-parser demo |
| Platform builds with AI-assisted development, client automations, agency or freelance delivery | Urlink | UltraStrategy or FlowSpace |
| API integrations, search or discovery automations, Google APIs | Get2Germany | Clubee or FlowSpace (OfficeRnD, Nexudus) |
| Marketplace operations, live migration, RAG support agents, OfficeRnD or Nexudus, CRM and GTM automation | FlowSpace | Urlink or Get2Germany |
| Dashboards, Figma to UI implementation | Qomodo | Clubee or Get2Germany |
| API integration plus QA and testing | Clubee | FlowSpace (Playwright) |
| OpenAI or Sendgrid integration, early-stage product | Tractionboard | FlowSpace (Sendgrid, CRM) |

## 3. Per-role facts (safe to reuse verbatim)

### UltraStrategy, AI Automation Developer (Collaborator), Dec 2024 to May 2025, France, ultrastrategy.com
- Built a CV-parsing pipeline integrated into the UltraStrategy platform. A user uploads a CV, the pipeline extracts the data and assesses how relevant the candidate is for specific types of roles, the result is delivered to the frontend, and a standardised "Ultra CV" is then generated.
- Affinda and the Claude API were used for the parsing and generation.
- The CV-parsing tool (LLM data extraction) was built with n8n and Eden AI.
- Also built the platform that serves different user profiles.

### Urlink, Project Manager and AI-Assisted Developer (Freelance), Apr 2025 to Jul 2025, Barcelona, smarturlink.com
- Built the platform and its logic with AI-assisted development and implemented client-driven automations.
- Acted as project manager on client requirements.
- Stack: Next.js, Supabase, Netlify, GitHub, bolt.new.

### Get2Germany, Developer and Automation Specialist (Part-time), Jan 2024 to May 2024, Berlin, get2germany.com
- Integrated Google APIs and built AI tools that find courses, internships and jobs.
- Optimised the database. Stack: n8n, Google APIs.

### FlowSpace, Lead Developer (Full-time, Freelance), Mar 2024 to Aug 2026, London (remote), flowspace.co
- Took over a live workspace marketplace and automated its data migration off a legacy stack onto Next.js and Laravel: mapped the old structure to the new one, chose the migration path per entity (API endpoints or CSV exports), and drove the cutover while the product stayed live. The platform grew from 2,000 to 4,500+ users.
- Built and owns an AI listing bot: give it a workspace provider's name and a brochure in any format (PDF, website, photo or spreadsheet) and it drafts the full listing with a human in the loop, then sends it to the backend. 900+ draft listings produced. Stack: n8n, the Claude API, TypeScript.
- Built support AI agents that answer customer queries from live platform data and escalate to a human on low confidence.
- Shipped OfficeRnD and Nexudus API integrations for automated bookings, plus CRM and GTM automations (lead capture, enrichment, routing, outbound).
- Role-level stack: TypeScript, Next.js, Node.js, Laravel, Supabase, Claude / Claude Code, n8n, Playwright; OfficeRnD, Nexudus, Google, CRM, Sendgrid integrations.

### Qomodo, AI Developer (Collaborator), 2024 to Jan 2025, Milan, qomodo.me
- Built a dashboard for companies to manage their branches.
- Implemented Figma designs.

### Clubee, Developer and QA (Full-time, Freelance), Sep 2023 to Aug 2024, Foetz, Luxembourg, clubee.com
- Integrated the Clubee API across the frontend.
- Ran unit testing and QA of new features.
- Built shop, domain-integration and federation-dashboard tools.

### Tractionboard, Developer (Internship), Aug 2023 to Oct 2023, Utrecht, tractionboard.co
- Integrated ChatGPT/OpenAI and Sendgrid.
- Built responsive designs and debugged features.

Never claim: BPMN, cloud admin (AWS, GCP, Azure), computer vision, edge computing, ML research, production experience at a 1,000+ person company, or any language beyond English (professional C2) and conversational Italian (B1-B2). See the guardrails in the Master Experience file.

## 4. Links
- GitHub demo: https://github.com/prab-gupta/llm-doc-parser (LLM document to structured JSON)
- LinkedIn: https://www.linkedin.com/in/prabhavit/

## 5. Italian mini-glossary (for Italian outreach)

Sono uno sviluppatore full-stack e AI con esperienza in otto aziende europee in circa tre anni. Per UltraStrategy (Francia) ho costruito una pipeline di parsing dei CV integrata nella piattaforma: l'utente carica il CV, la pipeline estrae i dati e valuta la rilevanza del candidato per tipi di ruolo specifici, il risultato viene mostrato nel frontend e infine viene generato un "Ultra CV" standardizzato; per il parsing e la generazione sono stati usati Affinda e le API di Claude, e lo strumento di parsing dei CV è stato costruito con n8n ed Eden AI. Per Urlink (Barcellona) ho sviluppato la piattaforma con sviluppo assistito da AI e automazioni su richiesta del cliente, e per Get2Germany (Berlino) ho integrato le Google API e costruito strumenti AI per trovare corsi, stage e offerte di lavoro. Per FlowSpace (Londra) ho automatizzato la migrazione dei dati da uno stack legacy a Next.js e Laravel con il prodotto in produzione, portando la piattaforma da 2.000 a oltre 4.500 utenti, e ho costruito un bot AI che redige annunci di spazi di lavoro a partire da brochure in qualsiasi formato.
