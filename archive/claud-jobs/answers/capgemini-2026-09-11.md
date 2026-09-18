# Capgemini - Data Engineer (Marcon, Venice) - 2026-09-11

Status: NEEDS YOU. Blocked by mandatory account creation on Capgemini's SuccessFactors ATS
before any application field could be submitted, so no free-text answers were entered on the
live form. This file records the gate check, dedupe decision, and the material ready for the
user to use.

## LI-PICK row

Queue row: `Capgemini,Data Engineer,https://www.linkedin.com/jobs/view/4374760503/,"LinkedIn offsite...",?,LI-PICK,2026-09-11,CV+CL,APPLYING,"LI-PICK (italian_jd); user rule 2026-09-11: apply everything LinkedIn suggests, junior first; soft gates off; Chrome agent 15:54"`.
Per the 2026-09-11 LI-PICK rule, applied regardless of years/seniority/fit and regardless of
the JD asking for Big Data tooling (Apache Spark, Hadoop, Kafka, Kubernetes) that Prabhavit
cannot honestly claim. Italian JD is fine (he is conversational). Kill conditions (closed /
already-submitted duplicate / language he lacks) did not apply.

## Dedupe

`python3 loop/dedupe.py --check "Capgemini" "https://www.linkedin.com/jobs/view/4374760503/"`
-> `HIT COMPANY` (company-name match only, not a URL hit).

`grep -i capgemini applications.csv`:
- 2026-08-06, Capgemini, Automation Engineer - NL, status LEAD (never applied; different role,
  different country, non-blocking status).
- 2026-09-09, Capgemini Engineering, Software Engineer, SuccessFactors, req 436075-en_GB,
  status NEEDS YOU (different requisition, different role title; NEEDS YOU is not one of the
  blocking statuses (SUBMITTED / NEEDS YOU-for-this-exact-req / INTERVIEW / REJECTED) for a
  DIFFERENT requisition - the brief's dup rule blocks on the same requisition or same-level
  role within 60 days with a blocking status; this is Data Engineer vs. Software Engineer, a
  different requisition (341449 vs 436075), so does not block).

No prior SUBMITTED/NEEDS YOU/INTERVIEW/REJECTED row for req 341449 (Data Engineer, Marcon).
Decision: proceed, not a duplicate.

## Hard gates (LI-PICK overrides fit/seniority/years, but closed/anti-AI/language gates still apply)

- Anti-AI disclaimer: none found in the JD.
- Language: JD is in Italian; Italian is fine per the LI-PICK rule (he is conversational).
  English also required ("Inglese fluente") - he has C2, not a kill.
- Posting: confirmed open (LinkedIn apply-button count 1 via jobs-guest API; Apply control
  present on the LinkedIn page and on the capgemini.com page, no "not accepting applications"
  banner).
- Everything else (years, seniority label "Mid-Senior level", Spark/Hadoop/Kafka stack) would
  normally gate a non-LI-PICK row but is waived here per the 2026-09-11 rule. No Spark,
  Hadoop, Kafka, Kubernetes, or Databricks experience is claimed anywhere in the CV or letter.

## What blocked the application

LinkedIn's Apply button opened a safety-reminder interstitial, then
https://www.capgemini.com/jobs/341449-en_GB_SAPBTP/Data-Engineer (same JD text and req ID as
the LinkedIn posting, "Marcon VE" among the listed locations). "Apply for this job" opened
https://career5.successfactors.eu/careers?company=capgemitecP3, the same SAP SuccessFactors
portal family hit on 2026-09-09 for a different Capgemini requisition. Its single-page form
puts mandatory Valid Email / Retype Valid Email / Choose Password (8-18 chars, upper+lower
case, number or punctuation) directly alongside the CV upload and the rest of the application
questions (name, phone, country of residence, work authorisation, consent checkboxes, privacy
notice, Apply button) - there is no guest-apply path and no way to submit without registering.

Per the brief ("if it demands an account with no guest path, do not create one") this is a
hand-back: no account was created, no email or password entered, nothing submitted.

## Material prepared for the user

- CV: `Prabhavit_CV_Capgemini.pdf`, freshly re-tailored for this Data Engineer req (overwrites
  the 2026-09-09 Software Engineer version). See `answers/cv-tailoring-capgemini-2026-09-11.md`
  for the full bullet-by-bullet record. 2 pages, tectonic, parity-checked.
- Cover letter (Italian, 266 words, 0 em-dashes, "voi" plural, no "Lei") -
  `CoverLetter_Capgemini.txt` / `.pdf` (tectonic, 1 page):

Gentili Signori,

mi rivolgo a voi per candidarmi al ruolo di Data Engineer presso Capgemini a Marcon. Vivo a
Venezia, a due passi da Marcon, e sono autorizzato a lavorare in Italia senza bisogno di
sponsorizzazione.

Ho tre anni di esperienza come sviluppatore full-stack e AI in diverse aziende europee, con un
focus su pipeline che elaborano e strutturano dati. Per UltraStrategy (Francia) ho costruito
una pipeline di parsing dei CV integrata nella piattaforma: l'utente carica il CV, la pipeline
estrae i dati con Affinda e le API di Claude e valuta la rilevanza del candidato per tipi di
ruolo specifici, il risultato viene mostrato nel frontend e infine viene generato un "Ultra CV"
standardizzato.

Per FlowSpace, un marketplace di spazi di lavoro con sede a Londra, ho guidato la migrazione dei
dati da uno stack legacy a Next.js e Laravel: ho mappato la struttura dati esistente su quella
nuova, scelto per ogni entita il percorso di migrazione (endpoint API o esportazioni CSV) e
gestito il passaggio mentre il prodotto restava in produzione, portando la piattaforma da 2.000
a oltre 4.500 utenti.

Come seconda prova, per Get2Germany (Berlino) ho integrato le Google API e costruito
automazioni di ricerca che trovano corsi, stage e offerte di lavoro, oltre a ottimizzare il
database della piattaforma.

La mia esperienza con schemi Postgres e Supabase e con pipeline di trasformazione ed estrazione
dati mi permette di contribuire rapidamente a un contesto di data engineering. Il mio inglese e
di livello C2, il mio italiano e conversazionale e in costante miglioramento.

Resto a disposizione per un colloquio.

Cordiali saluti,
Prabhavit Gupta

## Standard answers ready if the user signs in and continues

- Legally entitled to work in Italy: Yes.
- Country of Application / Country of Residence: Italy.
- Employed by Capgemini before: No.
- Disability disclosure / gender disclosure consent checkboxes: leave unticked ("prefer not to
  say" per standing rule); "How do you identify?" leave blank if it appears.
- WhatsApp contact consent: No (not required).
- Notification / recruitment-events marketing consent checkboxes: leave unticked.
- Privacy Notice acknowledgement: required, must be ticked to submit.
- Phone: +39 351 610 7807, Country/Region Code: Italy (+39).
- Name: Prabhavit Gupta (Legal First Name: Prabhavit, Legal Last Name: Gupta).
- Salary if asked: EUR 45,000-55,000 (JD's own RAL band is EUR 33,000-47,000 for the CCNL
  level stated; align toward the top of that band, around EUR 45,000-47,000, since the JD band
  is lower than the standing default).
