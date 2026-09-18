# Lithosquare - Forward Deployed Engineer - 2026-09-16

URL: https://www.linkedin.com/jobs/view/4417098641/
Apply routes to: https://jobs.ashbyhq.com/lithosquare/87723620-e098-455b-89a9-d67586fb43b2/application (Ashby)
Status: SUBMITTED

## Dedupe
`python3 loop/dedupe.py --check "Lithosquare" "https://www.linkedin.com/jobs/view/4417098641/"` -> NEW.

## Standing rule applied
USER RULE 2026-09-16: apply to every FDE posting in Italy/EU on LinkedIn, no kills for fit/years/seniority/
agency/stack. JD asks for "4+ years in Solutions Engineering, customer-facing Data Science, Pre-sales
Engineering, or a similarly hybrid technical role" and "fluency in Python for data and ML, solid SQL skills" -
years and the Python-for-data/SQL depth both waived under the standing rule. "Familiarity with geology or
geospatial data tooling ... is a plus" (not required), consistent with a truthful "No" on the geospatial
screening question.

## Hard gates re-checked on the live Ashby form
No anti-AI disclaimer. English JD. Not closed (form accepted the submission). No explicit French requirement in
the JD text (role is Paris-based with a "flexible remote working policy" mentioned).

## Fields and answers
- Name -> Prabhavit Gupta
- Email -> prabhavitg@gmail.com
- Resume (required) -> Prabhavit_CV_Lithosquare.pdf
- "Are you eligible to work in France ?" -> No (work-authorisation.md: EU country other than Italy = not
  automatically authorised)
- "Will you require a visa sponsorship?" -> Yes (honest, matches the above)
- "Where are you currently based (City/Country)?" -> Venice, Italy
- "What are your salary expectations ?" -> EUR 45,000 (this batch's stated target; JD gives no band)
- Notice period -> Immediately available
- English proficiency -> Professional (standing rule: never Fluent/Native, never claim native English)
- "Do you have experience working with geospatial data...?" -> No (honest; no GIS/geospatial background per
  OUTREACH_FACTS.md guardrails)

## Materials built
Prabhavit_CV_Lithosquare.pdf (2 pages, same AI/FDE tailoring pattern as the other three rows tonight: career
summary trimmed to 2 bullets, FlowSpace AI-agent/production bullets led, all content verbatim from
Prabhavit_CV_EN.tex). CoverLetter_Lithosquare.tex/.txt written (no upload field on this Ashby form; letter kept
on file). Lead role UltraStrategy (CV-parsing LLM pipeline holding up against real, inconsistent documents,
framed as the closest analogue to turning raw geology data into insight), paired with FlowSpace (AI listing bot,
scale, being the technical face of a product for non-technical stakeholders). Honest that he has no geology or
geospatial background. 0 em-dashes (grep-verified).

## Bug encountered and fixed
Same Ashby React-state desync as the Harmattan AI application tonight: after filling all fields and clicking
Submit, the form rejected with "Missing entry for required field: Name" even though the Name textbox visibly
showed "Prabhavit Gupta". Fixed by clicking the field, Ctrl/Cmd+A, Backspace, retyping with fill(), then clicking
another field to blur before resubmitting - second submit succeeded cleanly. Two occurrences on two different
jobs.ashbyhq.com/<company> forms in the same session; flagged in loop/results/Lithosquare.txt as a likely
general Ashby-via-Playwright quirk worth a LEARNINGS.md line.
