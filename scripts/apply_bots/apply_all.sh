#!/bin/bash
set -e

JOBS=(
  "https://www.linkedin.com/jobs/view/4426822677/;/Users/prab/Downloads/claud jobs/cv/main_Workday_AgenticAI.pdf"
  "https://www.linkedin.com/jobs/view/4453440697/;/Users/prab/Downloads/claud jobs/cv/main_kausable_SoftwareEngineer.pdf"
  "https://www.linkedin.com/jobs/view/4437140753/;/Users/prab/Downloads/claud jobs/cv/main_BambooWorks_AIAutomation.pdf"
  "https://www.linkedin.com/jobs/view/4411355407/;/Users/prab/Downloads/claud jobs/cv/main_scandiweb_GTM.pdf"
  "https://www.linkedin.com/jobs/view/4374760503/;/Users/prab/Downloads/claud jobs/cv/main_Capgemini_DataEngineer.pdf"
)

# Read the external links using get_ats_urls output if possible
# Since we didn't save them cleanly, I'll just rely on the user to run apply.mjs themselves,
# because apply.mjs doesn't natively handle LinkedIn -> External ATS redirect (it stops on LinkedIn).

