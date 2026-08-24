import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

WB = '/home/claude/sheet/Role shortlist - 8 Aug 2026.xlsx'
wb = openpyxl.load_workbook(WB)
HDR = PatternFill('solid', fgColor='1F3864')
DONE = PatternFill('solid', fgColor='D6EFD6')
TODO = PatternFill('solid', fgColor='FFF9E6')
BLOCK= PatternFill('solid', fgColor='FFF2CC')
thin = Side(style='thin', color='BBBBBB'); BOX = Border(left=thin,right=thin,top=thin,bottom=thin)

name = 'CV-only queue'
if name in wb.sheetnames: wb.remove(wb[name])
ws = wb.create_sheet(name, 1)
ws.sheet_view.showGridLines = False

ws['A1'] = 'CV-only queue - roles whose form needs nothing from you but the CV'
ws['A1'].font = Font(bold=True, size=14, color='1F3864')
ws['A2'] = ('This is the tab you asked for. "Form weight" is what the application actually demanded. '
            'GREEN = already sent. YELLOW = still open and sendable on the CV alone. '
            'AMBER = would be CV-only except for one thing only you can supply.')
ws['A2'].font = Font(size=10, italic=True, color='555555')

H = ['Company','Role','Location','Form weight','Status','What the form asked for','Link']
for i,h in enumerate(H,1):
    c=ws.cell(row=4,column=i,value=h); c.font=Font(bold=True,color='FFFFFF'); c.fill=HDR; c.border=BOX

R = [
 ('Taktile','Forward Deployed Engineer','Berlin / London','CV only','SENT',
  'Name, email, CV, relocate?, start date. Nothing else.',''),
 ('Luma AI','Forward Deployed Engineer','Remote UK / hybrid','CV only','SENT',
  'Name, email, CV, relocation. Portfolio and GitHub optional, left blank.',''),
 ('STRATOS Technologies','Forward Deployed Engineer','London (hybrid)','CV only','SENT',
  'CV, start date, city, sponsorship y/n, English level. No cover letter step at all.',
  'https://join.com/companies/stratos/16565987-forward-deployed-engineer-at-stratos'),
 ('Zauber','Forward Deployed Engineer','Berlin','CV + 3 lines','SENT',
  'CV, LinkedIn, on-site y/n, right to work y/n, start date, one short "why us".',
  'https://jobs.ashbyhq.com/zauber/c11db72e-3a33-4df5-ae33-e1cc39cb0ba7'),
 ('Seamflow','Forward Deployed Engineer','London','CV + 3 lines','SENT',
  'CV, LinkedIn, years of experience, one short "why a startup".',
  'https://jobs.ashbyhq.com/seamflow/83e5dd13-b293-462f-9cb6-bc9cc325b155'),
 ('SolveAI','Forward Deployed Engineer','London','CV + short fields','SENT',
  'CV, LinkedIn, location, salary, UK eligibility, notice period, on-site y/n. No essay.',
  'https://jobs.ashbyhq.com/solve.ai/1179e1af-6930-4271-b4b5-75294c13f806'),
 ('Otherworldly','Forward Deployed Engineer (f/m/x)','Berlin','CV + letter','SENT',
  'CV, cover-letter file, start date, salary, full/part time, on-site y/n.',
  'https://join.com/companies/otherworldly-artistscom/16557950-forward-deployed-engineer-f-m-x'),
 ('dexter health','Applied AI Developer','Remote','CV + letter','SENT',
  'CV, cover-letter file, city, start date, remote y/n.',
  'https://join.com/companies/dexter-health/16549765-applied-ai-developer-remote'),
 ('Laioutr','AI Engineer - Full Stack','Remote (Germany)','CV + letter','SENT',
  'CV, cover-letter file, start date, salary, remote y/n, two work-permit questions.',
  'https://join.com/companies/laioutr/16553103-ai-engineer-m-f-d-full-stack-typescript-nuxt-next-vue-react'),
 ('Atmen Solutions','Customer Solutions Engineer','Madrid','CV + letter','SENT',
  'CV, cover-letter file, start date, salary.',
  'https://join.com/companies/atmen/16529717-customer-solutions-engineer'),
 ('Camunda','AI Forward Deployed Engineer, EMEA','Remote EMEA','CV + self-ratings','SENT',
  'CV plus three self-rating dropdowns with no cleanly-true option. See the red block on the Applications tab.',''),
 ('Cohere','FDE, Agentic Platform','UK / Europe','CV + 1 answer','SENT',
  'CV plus one free-text answer.',''),
 ('OMMAX','Forward Deployed AI Engineer','Munich / Berlin / London / Amsterdam / Paris / MILAN','CV + 2 documents','BLOCKED ON YOU',
  'CV uploaded and form filled, but Personio requires an EMPLOYMENT REFERENCE letter and ACADEMIC TRANSCRIPTS as separate mandatory files. Send me both PDFs.',
  'https://ommax.jobs.personio.com/job/2550344?language=en'),
 ('GTM Base','Forward-Deployed CRM Architect','Remote','CV + HubSpot test','BLOCKED ON YOU',
  'Question 2 is a HubSpot build-design test. Needs a few lines from you or it stays unsent.',
  'https://join.com/companies/gtmbaseio/16539004-forward-deployed-crm-architect'),
 ('GTM Base','Senior GTM Engineer','Remote','CV + Loom of your Clay work','BLOCKED ON YOU',
  'They want a walkthrough video of Clay tables you built. Only you can record it.',
  'https://join.com/companies/gtmbaseio/16516200-senior-gtm-engineer'),
 ('Swans','Forward Deployed Engineer','-','CV + mandatory video','BLOCKED ON YOU',
  'Highest-scoring role on the sheet. Mandatory video walkthrough.',''),
 ('n8n','Forward Deployed Engineer EMEA','Remote EMEA','CV + choice','BLOCKED ON YOU',
  'One application per 15 days across ALL n8n roles. Tell me which one to spend it on.',''),
 ('xAI','-','-','CV + GitHub','BLOCKED ON YOU','Wants a GitHub profile URL.',''),
 ('Codekeeper','QA Verifications Specialist','-','CV + personality test + captcha','BLOCKED ON YOU',
  '16personalities result, profile URL, device details, captcha.',''),
 ('Kadoa','-','-','Email','BLOCKED ON YOU','Gmail draft written. Attach the CV and send.',''),
]

FILL = {'SENT':DONE,'BLOCKED ON YOU':BLOCK}
r=5
for row in R:
    for i,v in enumerate(row,1):
        c=ws.cell(row=r,column=i,value=v)
        c.alignment=Alignment(vertical='top',wrap_text=(i in (2,6)))
        c.border=BOX; c.fill=FILL.get(row[4],TODO)
        if i==5: c.font=Font(bold=True)
        if i==7 and v:
            c.hyperlink=v; c.value='open'; c.font=Font(color='0563C1',underline='single')
    r+=1

for col,w in zip('ABCDEFG',[24,40,44,26,18,78,8]):
    ws.column_dimensions[col].width=w
ws.freeze_panes='A5'
ws.auto_filter.ref=f'A4:G{4+len(R)}'
wb.save(WB)
print('cv-only tab built:', len(R))
