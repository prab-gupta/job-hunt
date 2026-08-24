import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side

wb = openpyxl.load_workbook('Role shortlist - 8 Aug 2026.xlsx')
ws = wb['Follow up']

SENT = PatternFill('solid', fgColor='D9EAD3')
THIN = Side(style='thin', color='BBBBBB')
BOX  = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)

NEW = [
 ['opus','Founding Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/opus-techai/','Tarkan Akbogra (contact person on the posting)',
  'Berlin, 6-person-ish stage. Small enough that a direct message to Tarkan will land. Lead with the agentic work in production and the fact you are relocating-ready, not with the FastAPI gap.'],
 ['Avery','Founding Engineer (Core)','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/getaveryai/','Alisher Jafarov, Founder',
  'Early-stage Amsterdam, founder is the contact. A founder-direct message is very likely to be read. Their pay band is above what you asked for, so if they come back, you have room.'],
 ['The Quality Group (ESN / More)','AI Engineer (gn)','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/the-quality-group-gmbh/','-',
  'Best stack match of the sweep - they run n8n, Claude Enterprise and ChatGPT Enterprise. Your open question is whether day-one German residency is a hard gate; I asked in the form, so the follow-up is a fair place to ask again. Look for whoever owns AI/automation, not HR.'],
 ['Reedsy','AI Engineer - Remote Europe','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/reedsy/','-',
  'EUR 70-120k, the best-paid role in the sweep. Italy was not in their country list, so the follow-up should confirm they can hire remotely into Italy before anything else. Ask that first, plainly.'],
 ['Spyrosoft','Forward Deployed Engineer (OpenAI)','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/spyrosoft/','-',
  '1,800 people, so the ATS is real and a recruiter will screen it. The thing worth confirming is whether Regular level and invoicing from Italy both work, since the engagement is Poland-based.'],
 ['Hexa (Waniwani)','Forward Deployed Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/hexa-scale/','Max (CTO), Robin (CEO), Luiza',
  'Seed-stage with named founders in the process description. Message Max the CTO. Their process includes a live work sample on a real client scenario - scope a flow, draft architecture, handle a mock procurement Q&A. Worth preparing for even before they reply.'],
 ['Nuitée','GTM Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/nuitee/','Gian, VP Growth (you would report to him); Lina, inbound SDR',
  'Gian is named in the posting as the person you would work directly with. Message him, not a recruiter. Their process is stated as 2-3 weeks, so 21 Aug is about right.'],
 ['Pliant','Software Engineer - AI Experience','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/getpliant/','-',
  'Fintech, Berlin-headquartered, remote Germany. Posted within a day of your application so you are early in the pile. Their stack is Java/Spring Boot and/or Python; if you follow up, lead with shipped AI features rather than language depth.'],
 ['HiPeople','Applied AI Engineer - Systems & Reliability','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/hipeople/','-',
  'They sell reference-checking and talent assessment, so they think hard about hiring signal. The application was CV-only, which means the CV is doing all the work - a follow-up message adds real information here.'],
 ['Jamie','AI Engineer','12 Aug 2026','21 Aug 2026','SENT','https://www.linkedin.com/company/meetjamieai/','Egor Spirin, Recruiting Team',
  '11-50 people and the posting was updated 19 hours before you applied, so it is actively being worked. Egor is named. The 2+ years bar means you are genuinely in range here - say so.'],
]

start = 5
ws.insert_rows(start, amount=len(NEW))
r = start
for row in NEW:
    for i, v in enumerate(row, 1):
        c = ws.cell(row=r, column=i, value=v)
        c.alignment = Alignment(vertical='top', wrap_text=(i in (2, 7, 8)))
        c.border = BOX
        c.fill = SENT
        if i == 5:
            c.font = Font(bold=True)
        if i == 6 and v:
            c.hyperlink = v
            c.value = 'LinkedIn'
            c.font = Font(color='0563C1', underline='single')
    r += 1

ws['A1'] = 'Follow up - every application sent, with the company LinkedIn to chase on (updated 12 Aug 2026, evening)'
ws['A1'].font = Font(bold=True, size=13)
wb.save('Role shortlist - 8 Aug 2026.xlsx')
print('added', len(NEW))
