# Kyndryl - Senior Forward Deployed Engineer, Milan (2026-09-16)

Source: LinkedIn https://www.linkedin.com/jobs/view/4466872754/ -> Apply on company website
-> https://kyndryl.wd5.myworkdayjobs.com/KyndrylProfessionalCareers/job/Italy-Milan-ITMILVP22-Office/Senior-Forward-Deployed-Engineer_R-65797-1?source=REC_APPLICANT_SOURCE_LinkedIn
Requisition R-65797-1 (Milan/Roma, Partially Remote). Distinct from the plain "Forward Deployed Engineer" requisition R-65787-1 (ITMILCOP) already logged NEEDS YOU earlier today under a separate applications.csv row.

## Gates
- No anti-AI disclaimer in JD.
- "Senior" title, generative/agentic AI + cloud-native data architecture ask: no kill per USER FDE-ALL rule 2026-09-16.
- English JD, no hard degree requirement, Italy location (already authorised, no sponsorship needed).

## Dedupe
`python3 loop/dedupe.py --check "Kyndryl" "https://www.linkedin.com/jobs/view/4466872754/"` -> HIT COMPANY.
`grep -i kyndryl applications.csv`: one prior row today, status NEEDS YOU, for the separate plain-FDE requisition R-65787-1 (Milan, ITMILCOP). Different requisition number and different job title (no "Senior"), so per the dedupe rule (blocks only on SUBMITTED/NEEDS YOU/INTERVIEW/REJECTED for the SAME requisition) this does not block: it is a same-company, different-requisition row. Proceeded.

## Blocker (re-checked per task instruction)
Clicked Apply -> "Start Your Application" modal -> tried "Apply Manually" (not Autofill with Resume, not Use My Last Application) to look for a guest path. Same as the earlier Kyndryl row today: Workday still forces step 1 "Create Account/Sign In" with Email Address / Password / Verify New Password fields, no guest-apply link, no Sign-In-with-SSO option visible either. Per the brief and the standing no-account-creation rule, stopped here without creating an account or entering a password.

## Materials built and saved (ready for user)
- CV: Prabhavit_CV_Kyndryl.pdf, reused after a parity check. Diff against Prabhavit_CV_EN.tex found one non-verbatim addition ("while the product stayed live" appended to the Bubble.io migration bullet) which was a rewrite, not present in the master; fixed it in Prabhavit_CV_Kyndryl.tex back to the exact EN.tex wording and recompiled (2pp, tectonic). All remaining differences are allowed deletions/reordering (Career Summary trimmed to 2 bullets, FlowSpace/UltraStrategy/Get2Germany reordered and trimmed, "Low code development/" prefix dropped from IT Skills since this JD has no low-code relation).
- Letter: CoverLetter_KyndrylSenior.pdf/.txt (new letter, distinct from the existing CoverLetter_Kyndryl.pdf/.txt built for the other requisition), English, 0 em-dashes (grep-verified). Lead paragraph FlowSpace (migration + AI listing bot + support agents + OfficeRnD/Nexudus, generative/agentic AI framing matched to the JD), second paragraph UltraStrategy (CV-parsing pipeline, Affinda + Claude API + n8n/Eden AI, framed as the closest match to "model lifecycle and orchestration"). Honest about 3 years vs the Senior data-architecture title, and honest that no AWS/Azure/GCP enterprise-scale AI workload experience exists. Italy work location: authorised, no sponsorship needed (no transparency line required).

## For the user
Sign in or create the Workday account at the URL above, then either finish the 5-step form yourself (My Information / My Experience / Application Questions / Voluntary Disclosures / Review) using Prabhavit_CV_Kyndryl.pdf and CoverLetter_KyndrylSenior.pdf, or ping to have the rest filled in once logged in.
