import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

wb = openpyxl.load_workbook('Role shortlist - 8 Aug 2026.xlsx')
ws = wb['Applications sent']

GREEN = PatternFill('solid', fgColor='D9EAD3')
AMBER = PatternFill('solid', fgColor='FCE5CD')
GREY  = PatternFill('solid', fgColor='EFEFEF')
FILL  = {'SUBMITTED': GREEN, 'NEEDS YOU': AMBER, 'HELD': AMBER, 'CLOSED': GREY, 'DROPPED': GREY}
THIN  = Side(style='thin', color='BBBBBB')
BOX   = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

NEW = [
 ['Lleverage','AI Engineer','Amsterdam, Netherlands (on-site/hybrid)','SUBMITTED','12 Aug 2026',
  '"All done! Your application has been successfully submitted!"',
  'EUR 80,000-110,000 PUBLISHED, and the closest domain match found anywhere: they build the AI workflow automation platform your n8n work lives inside, and "background in SaaS or low-code platforms" is listed as a nice-to-have, which is literally your CV. No years bar. Heavy form and I answered it properly. "Do you consider yourself the top 1%?" got a plain No plus the narrower claim you can actually defend. The required "have you tried our platform" question got the truth - there is no self-serve trial, only Book a demo, so I did NOT sign up (that means creating an account) and said so, then gave a real read of their public product plus three pieces of substantive feedback. Dutch work permit answered Yes with the Directive 2003/109/EC position written out in full so the Yes is not a surprise later. Their site now advertises "forward deployed engineers" as part of delivery.',
  'https://lleverage.recruitee.com/o/ai-engineer-2'],
 ['BAS Group','AI Engineer','Veghel, Noord-Brabant, Netherlands (on-site)','SUBMITTED','12 Aug 2026',
  '"All done! Your application has been successfully submitted!"',
  'LOWEST EXPERIENCE BAR OF ANY ROLE IN ANY SWEEP: "1+ year as an AI Engineer, or 2+ years as a Data Scientist/Data Engineer with strong AI focus". Posting in English, no Dutch requirement. They already have three AI agents deployed against CRM, ERP, order processing and support, so this is production work not a pilot. AWS Enterprise org, 1,000+ colleagues, family business since 1962, automotive. Letter names two gaps: n8n and direct chaining rather than LangGraph, and no AWS-first Terraform experience (Bedrock, Sagemaker, Terraform all new). On-site in Veghel, so relocation. Salary not disclosed.',
  'https://basgroup.recruitee.com/o/ai-engineer-1?lang=en'],
 ['Freeday','Forward Deployed Engineer','Rotterdam, Netherlands (hybrid)','SUBMITTED','12 Aug 2026',
  '"All done! Your application has been successfully submitted!"',
  'They build "digital employees". The role is the one you have been doing without the title: translate business processes into implementation, configure and deploy, prototype, build integrations (they name Discord, HubSpot, SharePoint), troubleshoot. NO years bar at all. English fluent, no Dutch. Two requirements you miss and the letter says so: they ask for a CS/AI/Econometrics background (yours is BA Philosophy, International Studies and Economics) and for you to be based in the Netherlands (you would relocate, no sponsorship needed).',
  'https://freeday.recruitee.com/o/forward-deployed-engineer'],
 ['EggAI','AI software engineer','Remote, EU +/- 2hrs (EU, Norway, UK, Switzerland only)','SUBMITTED','12 Aug 2026',
  '"Thank you for applying. Your application has been received."',
  'Munich enterprise GenAI consultancy whose stated mission is moving AI from prototyping into production, which is your lane. The posting contradicts itself: stated bar is "Core LLM Engineering (2+ years)" but the body says "We are looking for a Senior Engineer". The letter names that contradiction and says if Senior is the real bar you are not the candidate. Three gaps stated: no Braintrust or Langfuse, evaluation has been hand-built regression checks not model-graded eval suites, no formal prompt versioning pipelines.',
  'https://job-boards.eu.greenhouse.io/eggai/jobs/4772834101'],
 ['SERA Intelligence / Super Technologies','AI Engineer (Bucharest/Munich) / AI Automation Engineer','Munich hybrid / Zagreb or Bucharest','CLOSED','12 Aug 2026','-',
  'Both dead on the live page. SERA said "archived 1 month ago" despite the sweep reading it as updated within the last minute - that is the SECOND join.com posting today whose metadata lied about freshness (Novosafe was the first). Super Technologies redirected to their board index with ?error=true; their board still has 187 jobs but the only AI engineering ones left want 4+ yrs SWE plus 3+ yrs cloud infrastructure.',
  'https://job-boards.eu.greenhouse.io/super'],
]

ws.insert_rows(5, amount=len(NEW))
r = 5
for row in NEW:
    for i, v in enumerate(row, 1):
        c = ws.cell(row=r, column=i, value=v)
        c.alignment = Alignment(vertical='top', wrap_text=(i in (2, 3, 6, 7)))
        c.border = BOX
        c.fill = FILL.get(row[3], GREY)
        if i == 4:
            c.font = Font(bold=True)
        if i == 8 and v:
            c.hyperlink = v; c.value = 'open'
            c.font = Font(color='0563C1', underline='single')
    r += 1

ws['A1'] = 'Applications sent - live log, last updated 12 August 2026 (late: second deep-dive batch added)'
ws['A1'].font = Font(bold=True, size=13)

# Follow up rows
fu = wb['Follow up']
SENT = PatternFill('solid', fgColor='D9EAD3')
FUNEW = [
 ['Lleverage','AI Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/lleverage/','-',
  'EUR 80-110k and the closest domain match found. Amsterdam. If they come back, the thing to lead with is the Bubble-to-Next.js migration, because their whole product sits on that line. Their site advertises "forward deployed engineers" as part of delivery, so if the AI Engineer role goes cold, ask about that instead.'],
 ['BAS Group','AI Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/bas-world/','-',
  'The 1+ year bar means you are comfortably inside their range for once, which is rare. Automotive, 1,000+ people in Veghel. Find whoever owns the AI agents (they have three in production) rather than HR.'],
 ['Freeday','Forward Deployed Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/freeday-ai/','-',
  'Rotterdam scale-up, no years bar, and the role description is your actual job. They say they prefer being in the office together, so a follow-up that confirms you would genuinely relocate is worth more here than usual.'],
 ['EggAI','AI software engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/eggai/','-',
  'Small Munich team. Worth asking directly whether the role is the 2-year bar in the requirements or the "Senior Engineer" in the body, since the posting says both. That question is a legitimate reason to message them.'],
]
fu.insert_rows(5, amount=len(FUNEW))
r = 5
for row in FUNEW:
    for i, v in enumerate(row, 1):
        c = fu.cell(row=r, column=i, value=v)
        c.alignment = Alignment(vertical='top', wrap_text=(i in (2, 7, 8)))
        c.border = BOX; c.fill = SENT
        if i == 5: c.font = Font(bold=True)
        if i == 6 and v:
            c.hyperlink = v; c.value = 'LinkedIn'
            c.font = Font(color='0563C1', underline='single')
    r += 1

wb.save('Role shortlist - 8 Aug 2026.xlsx')
print('done')
