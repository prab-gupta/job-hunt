---
name: cv-two-pages
description: "CVs must be 2 pages from now on, always use original CV as blueprint, edit only HEADLINE/SUMMARY/SKILLS"
metadata: 
  node_type: memory
  type: feedback
  modified: 2026-08-26T07:15:35.572Z
  originSessionId: 804b6284-b8c4-4655-879b-09f57c45f1a4
---

CVs are now 2 pages, not 1. Always use `/Users/prab/Downloads/Prabhavit_CV_TEMPLATE.tex` as blueprint for every tailored version.

**Why:** User wants more space to show experience properly. One-pager was cutting too much.

**How to apply:** Copy TEMPLATE.tex to job folder, edit ONLY HEADLINE (~line 45), SUMMARY (~line 63), SKILLS (~lines 70-75). Change geometry to allow 2 pages (remove `\pagestyle{empty}` constraint or adjust). Never shrink to 1 page. Compile with tectonic. Related: [[feedback-no-coauthor]], [[feedback-use-existing-libraries]].
