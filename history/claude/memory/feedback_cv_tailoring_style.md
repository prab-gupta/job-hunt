---
name: feedback_cv_tailoring_style
description: "How to tailor Prabhavit's CV per job - keep the original CV, cut long intros, reorder/prune bullets to the job, never rewrite"
metadata: 
  node_type: memory
  type: feedback
  originSessionId: 237a3cff-dd16-4810-8bd3-960e29fe6c44
  modified: 2026-09-09T12:34:11.879Z
---

User instruction 2026-09-09 (pointing at ~/Downloads/Prabhavit_CV.pdf): "for the cv, it is too wordy, no need to write such long intros, just mold my experience and highlight the ones relevant to the job. stick to the original as much as possible."

**Why:** Earlier attempts swung between a rewritten concise CV (rejected as "bad") and the untouched 3-page original (too wordy for a given job). The user wants the original's content and layout, only trimmed and re-weighted for the target role.

**How to apply:** Per application build `Prabhavit_CV_<Co>.tex/.pdf` from `Prabhavit_CV_EN.tex` (faithful LaTeX of the original, same layout as Prabhavit_CV_IT.tex with photo): Career Summary at most 2 short lines taken from existing text; keep experience bullets verbatim, reorder so the JD-relevant ones come first, drop clearly irrelevant ones (keep at least 3 under FlowSpace, 1 per other role); reorder Technical Skills relevant-first; no new sentences, no invented claims; 2 pages max. Upload the tailored PDF instead of the original. See [[project_job_search]], [[feedback_cv_context_rot]].
