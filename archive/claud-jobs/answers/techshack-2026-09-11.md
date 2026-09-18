# TechShack - Software Engineer (Backend Engineer, Stockholm) - 2026-09-11

URL: https://www.linkedin.com/jobs/view/4465813293/
ATS: LinkedIn Easy Apply
Lane C, fit 70, Mid-Senior level label only (no explicit years floor in the JD text).

## Dedupe
`python3 loop/dedupe.py --check "TechShack" "<url>"` -> NEW. No prior rows in applications.csv.

## Cheap check
`curl ... jobPosting/4465813293 | grep -c apply-button` -> 1. Live page confirmed Easy Apply control present, no "not currently accepting" banner.

## Agency check (task-specified gate)
JD text: "We're looking for a strong Backend Engineer to join a growing technology company building intelligent, AI-powered products." The employer is never named anywhere in the JD.

Checked TechShack's own LinkedIn company page (https://www.linkedin.com/company/https-www.tech-shack.co-about/about/):
- Tagline: "The House of Tech Recruitment"
- Industry: "Staffing and Recruiting"
- Overview: "TechShack is a tech recruitment partner building high-performing engineering teams across the UK, EU and US. We work across product engineering, cloud, AI, mobile, and security-cleared environments... If you're hiring, drop us a message here or connect with one of the team."
- "People also viewed" sidebar lists other recruitment agencies (Opus Recruitment Solutions, Oliver Bernard, Crossing Hurdles), consistent with TechShack itself being a recruiter, not an employer.

Both conditions of the brief's agency rule are met: TechShack is confirmed a recruitment agency, and the employer behind this posting is unnamed. KILLED before drafting any material, per the rule "if the employer is unnamed and TechShack is a recruiter, KILL with the quote (agency rule)."

## Result
KILLED (reason: agency rule, unnamed client + confirmed recruiter). No CV, no letter, no application submitted. Screenshots: confirmations/TechShack-2026-09-11.png (job posting) and confirmations/TechShack-2026-09-11-agency.png (TechShack About page evidence).
