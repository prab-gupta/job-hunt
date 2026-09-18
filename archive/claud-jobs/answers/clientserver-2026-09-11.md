# Client Server — Backend Software Engineer Scala Java — 2026-09-11

LinkedIn Easy Apply (Broadbean ATS, recruiter), https://www.linkedin.com/jobs/view/4464321812/

## Dedupe
`python3 loop/dedupe.py --check "Client Server" "https://www.linkedin.com/jobs/view/4464321812/"` -> NEW. `grep -i "client server" applications.csv` -> no prior rows. Not blocked.

## Hard gates / anti-AI
No anti-AI disclaimer in the JD. LI-PICK row: applied even though he has no Scala or Java experience, per user rule 2026-09-11. JD is in English. Note the JD itself is softer than the LinkedIn title suggests ("you'll be working with Scala (you can pick this up on the job)"), which supports the honest-gap-plus-willingness-to-learn framing used in the letter.

## Incident during this application (no data sent anywhere wrong)
On the first attempt, the resume-upload step navigated away mid-flow to an unrelated job page (NinjaOne "Solutions Engineer - Italian", https://www.linkedin.com/jobs/view/4466068547/) immediately after the file_upload call — most likely a stray click landed on a "more jobs" carousel link as the modal state changed. No dialog, resume field or application-in-progress was present on the NinjaOne page afterward, and nothing was filled or submitted there. Navigated straight back to the Client Server posting; Easy Apply had not registered any submission (button still said "Easy Apply to this job", not "Applied"), so restarted the flow cleanly from step 1 and completed it without incident. No action was taken on NinjaOne and it is not being applied to as part of this task.

## Trap caught
Easy Apply again pre-selected the previous lead's CV (Prabhavit_CV_Signify.pdf) on the resume step, both on the aborted first attempt and the clean restart. Explicitly clicked "Upload resume" and uploaded Prabhavit_CV_ClientServer.pdf each time; verified "Prabhavit_CV_ClientServer.pdf" as the selected file on the review page before submitting.

## Answers given
- Email: prabhavitg@gmail.com (pre-filled, correct)
- Phone: Italy (+39), 351 610 7807
- Resume: Prabhavit_CV_ClientServer.pdf (explicitly uploaded, verified filename)
- No additional screening questions on this ATS (only contact info, resume, and an optional "mark as top choice", left unticked)

## CV tailoring (Prabhavit_CV_ClientServer.tex/.pdf, 2 pages)
Not an AI JD, standard tailoring. Career Summary trimmed to 2 bullets (API integrations + QA testing, both backend-relevant). Technical Skills reordered Development (Laravel/TypeScript) first. FlowSpace reordered to lead with the Next.js/Laravel migration bullet and the external-API-integration bullet (REST APIs match the JD directly). IT Skills line: dropped the "Low code development/" prefix.

## Cover letter (CoverLetter_ClientServer.txt/.pdf/.tex, 246 words, 0 em-dashes)
States plainly, in the first paragraph, that his backend experience is TypeScript/Node.js, Laravel (PHP) and Python, not Java or Scala, that he has no production experience in either, and that he is ready to learn Scala on the job (the JD itself says this is acceptable: "you can pick this up on the job"). Lead: FlowSpace (owns backend end to end: migration, REST integrations with OfficeRnD/Nexudus, CRM/GTM automations). Pair: Clubee (API integration + QA/testing discipline). No claim of Java or Scala anywhere. Not uploaded — this Easy Apply flow had no cover letter step.

## Result
Application status: Application submitted. Screenshots: confirmations/ClientServer-2026-09-11-before.png (review page) and confirmations/ClientServer-2026-09-11.png (submitted confirmation).
