---
name: feedback_linkedin_picks_apply_all
description: "User rule (2026-09-11) - apply to everything LinkedIn suggests (Top job picks, My Jobs, recommendations), junior positions first; soft gates off for those rows"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 237a3cff-dd16-4810-8bd3-960e29fe6c44
  modified: 2026-09-11T07:57:46.981Z
---

On 2026-09-11 the user said: "don't drop anything LinkedIn suggests, specially junior positions."

**Why:** The planner and haiku verifiers had killed most LinkedIn picks on soft gates (fit floor 50, years 3+, "Mid-Senior" label, agency, senior title), leaving only 2 of 119 picks applied. The user considers LinkedIn's suggestions worth an application regardless, and cares most about junior/entry-level roles.

**How to apply:** Queue rows tagged `LI-PICK` in loop/queue.csv skip fit, years, seniority and agency kills. Drop only closed postings, exact duplicates, or JDs that explicitly require a language he lacks (he has English C2 and Italian; nothing else). Italian JDs get an Italian cover letter. Junior/intern/entry/associate first, Italy second, Easy Apply before offsite. Account walls, CAPTCHAs, assessments still go to NEEDS_YOU with materials prepared. Rule recorded in loop/RULES.md and the LI-PICK section of loop/APPLY_AGENT_BRIEF.md. See [[project_job_search]] and [[feedback_letters_use_all_experience]].
