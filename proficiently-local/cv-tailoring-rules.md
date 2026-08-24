# CV Tailoring Rules - READ BEFORE EVERY TAILOR

## Source of truth
Base template: ALWAYS re-read the LATEST .tex file from the most recent job folder
(or from the Distru folder as canonical base). Never work from memory of what the
template "probably" says.

## What to edit (ONLY these 3 blocks)
1. **HEADLINE** (line ~40): `{\color{accent}\large ...}`
2. **SUMMARY** (lines ~54-56): section content
3. **SKILLS** (lines ~59-66): 4 bullet items, reordered/reworded per role

Everything else stays UNCHANGED. Experience, education, certs, freelance, header = frozen.

## Hard rules
- ONE PAGE A4. If it overflows, shorten summary or skills. Never remove sections.
- No em-dashes. Use hyphens or commas.
- No "no-code" or "Bubble" anywhere. Say "off a legacy stack".
- Clickable company names (already in template, don't break).
- Salary blank or "negotiable" (never on the CV).
- Never claim: BPMN, deep Python-backend, FastAPI, computer-vision, edge computing,
  Kubernetes, ML research, non-English language proficiency beyond what's listed.
- No Claude/Anthropic attribution in any output.

## Compile
```bash
cd <job-folder> && tectonic resume-<slug>.tex
```
Needs `photo.jpg` in same folder. Copy from any existing job folder if missing.

## Salary on forms
- EUR forms: 50000 (midpoint of 45-55k range)
- USD forms: 54000 (EUR 50k x ~1.08)
- USD monthly forms: 4500

## Personal details for forms
- Email: prabhavitg@gmail.com
- Phone: +39 351 610 7807 (type FULL with +39 to avoid Portugal auto-detect)
- Location: Venice, Italy
- LinkedIn: https://www.linkedin.com/in/prabhavit/
- GitHub: https://github.com/prab-gupta
- Work auth: EU Long Term Residence Permit (Italy), no sponsorship needed in EU
- Available: Immediately

## Video walkthrough (Swans and similar)
- Loom 1: https://www.loom.com/share/d0f6bf69fd3f4db2a429ae6948a098f4
- Loom 2 (continuation): https://www.loom.com/share/d711fd7971ed4385a2ee7e3e948c8e73
