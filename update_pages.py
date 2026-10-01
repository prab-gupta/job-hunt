with open(".claude/skills/job-application-assistant/05-cv-templates.md", "r") as f:
    content = f.read()

import re

# Update directive
content = content.replace("a highly tailored 1-page CV", "a highly tailored 2-page CV")

# Update Other Experience
old_other = r"""### Other Experience & Education
- Add `Urlink`, `UltraStrategy.com`, `Get2Germany.com`, etc., as space allows to fill precisely 1 page.
- Always conclude with the `Education` and `Certifications` sections as found in the master reference."""

new_other = r"""### Other Experience & Education
- The CV is permitted to be up to 2 pages long. Do not aggressively prune experience to force a 1-page fit.
- Include ALL roles (`Urlink`, `UltraStrategy.com`, `Qomodo`, `Get2Germany.com`, `Clubee`, `Tractionboard`) as they appear in the master file.
- Always conclude with the `Education` and `Certifications` sections as found in the master reference."""

content = content.replace(old_other, new_other)

# Remove the 1-page constraint on Flowspace cutting
content = content.replace("You may cut 1-2 less relevant sub-bullets to fit the 1-page constraint, but", "Do not cut sub-bullets to save space.")

with open(".claude/skills/job-application-assistant/05-cv-templates.md", "w") as f:
    f.write(content)

with open("/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/cv-rules.md", "r") as f:
    cv_rules = f.read()

cv_rules = cv_rules.replace("1-page", "2-page")
cv_rules = cv_rules.replace("1-page limit", "2-page limit")

with open("/Users/prab/.gemini/antigravity/brain/ef77eada-777c-44ce-be2a-d6a8b4c47c87/cv-rules.md", "w") as f:
    f.write(cv_rules)

print("Updated rules to 2 pages.")
