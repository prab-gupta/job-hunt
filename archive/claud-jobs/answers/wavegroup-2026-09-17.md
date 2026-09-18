# wave group - 2026-09-17

## CV tailoring (Prabhavit_CV_EN.tex -> Prabhavit_CV_WaveGroup.tex)
Reused the Sia/Thoughtworks FDE tailoring pattern verbatim (script-verified: every \item line exists in Prabhavit_CV_EN.tex, zero invented lines). Same reordering as Galtea (AI-agents bullet to top of FlowSpace Product Responsibilities, AI-automation bullet to top of Get2Germany, Career Summary trimmed to 2 bullets). Compiled 2 pages with tectonic.

## Dedupe
`dedupe.py --check "Wave Group" <url>` = HIT COMPANY (exact). `grep -i "Wave Group" applications.csv | grep -i forward` returned nothing - no prior Wave Group row exists at all in applications.csv (dedupe.py's company index must carry a stale/fuzzy entry); treated as NEW, no blocking row found.

## Hard gate re-check (USER RULE 2026-09-17 FDE-ALL)
Live JD (LinkedIn guest API job id 4463480170): apply-button count 2, not closed. Language line: "Professional fluency in English (plus Spanish, Italian and/or German)" - an and/or set of three, Italian is one of them and Prabhavit has conversational Italian, so the explicit requirement is met; not a kill. Python/FastAPI listed as "must have" stack but FDE-ALL rule forbids stack kills for this batch. No anti-AI disclaimer.

## Letter pairing
Lead: FlowSpace (AI listing bot, support AI agents in production). Pair: UltraStrategy (CV-parsing pipeline). Spain work-authorisation transparency line (Madrid/Barcelona).
Salary: JD states EUR 80-100k base (recruiter post) plus bonus/equity; standing default EUR 45,000-55,000 given only if a form field asks, aligned to bottom of stated band description if forced to pick a number (not reached - LinkedIn Easy Apply, no salary field expected).
Years of experience: 3.
