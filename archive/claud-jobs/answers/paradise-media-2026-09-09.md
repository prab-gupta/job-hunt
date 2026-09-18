# Paradise Media — Full-stack Developer (AI-native) — 2026-09-09

ATS: Rippling (ats.rippling.com/paradise-media-recruitment), reached via LinkedIn Apply redirect (not Easy Apply).
JD: https://www.linkedin.com/jobs/view/4400778383/

## Form answers

- Résumé: Prabhavit_CV_Original_EN.pdf (uploaded, parsed successfully)
- Cover letter: CoverLetter_ParadiseMedia.pdf (uploaded; built from CoverLetter_ParadiseMedia.tex via tectonic; source CoverLetter_ParadiseMedia.txt is 181 words, 0 em-dashes)
- First name: Prabhavit
- Last name: Gupta
- Email: prabhavitg@gmail.com
- Current company: FlowSpace.co (auto-filled by résumé parse, correct)
- Phone: +39 IT / 35 1610 7807 (i.e. +39 351 610 7807) — corrected after résumé parse duplicated the country code into the local-number field (parse produced "393516107807" under a "+39 IT" selector, which would have dialed +39 393516107807; fixed via form_input to the local number only)
- Location: Venice, Italy (auto-filled by résumé parse, correct)
- "Let us know about you location": **I am not in Malta but I am open to relocation as a non-EU Citizen** — accurate: Prabhavit is an Indian citizen (non-EU) holding Italian EU long-term residence, not Maltese/EU citizenship. Per work-authorisation.md, never picks "citizen" of the destination country; this option describes citizenship status generally, which is truthfully "non-EU citizen."
- "What is your current situation?": **I have 2-5 years of professional dev experience** — true figure is 2.5 years (years-of-experience.md); falls in this bucket honestly, no 0-2/2-5 ambiguity to game.
- "What's your computer setup like?": MacBook/macOS, VS Code + Claude Code, Git/GitHub, Postman, second monitor when not travelling — factual, sourced from known tool stack in Master Experience.md (Claude Code, GitHub, Postman).
- "Have you ever built something using AI you couldn't have built without it?": Answered with the FlowSpace LLM listing pipeline (multi-format brochure -> drafted listing, human review gate, 900+ listings drafted), tools used (Claude, Claude Code, TypeScript, n8n), and the AI-vs-human split (AI: parsing/extraction across formats; me: architecture, data model, review gate). Cited github.com/prab-gupta/llm-doc-parser as a runnable sample. Traces to Master Experience.md "AI listing bot" and "Public runnable demo" entries.
- SMS text-message consent: **No — I do not consent to receiving text messages** (optional/no asterisk on this question; declined per privacy-preserving default, same as marketing/newsletter checkboxes standing rule).
- No separate work-authorisation Yes/No field on this form beyond the location dropdown above; the Malta permit/sponsorship transparency line was folded into the cover letter's closing paragraph instead ("I hold Italian EU long-term residence rather than Maltese work authorisation, so I'd need the employer-side permit process, and I'm ready to start it").
- No salary field on this form.
- No "how did you hear about us" field on this form.

## Gates re-checked live (curl jobPosting API + Rippling JD page)

- Seniority: Not Applicable (LinkedIn metadata) — no year-minimum stated anywhere in the JD text.
- Title: "Full-stack Developer (AI-native)" — not Senior/Staff/Lead/Principal/Manager/CTO.
- No MSc/PhD or degree requirement anywhere in the JD ("We care more about curiosity and craft than credentials").
- JD entirely in English; no Maltese or other language requirement.
- Core stack: HTML/CSS/JS + React/Vue nice-to-have, Python or Node.js backend, SQL basics, Docker/Railway/Render deployment — all directly claimable, no Java/.NET/C++/Go/Rust/Django/FastAPI-core/cloud-admin gate hit.
- Location: St Julian's, Malta, on-site, full-time — EU, relocation-ready per task; employer-side permit/sponsorship assumed available (task brief).
- No closed/404 posting; LinkedIn showed "Reposted 16 hours ago", over 100 applicants tracked.

No hard gate hit. Dedupe: `dedupe.py --check "Paradise Media" <url>` returned NEW; `grep -i paradise applications.csv` returned no prior rows.
