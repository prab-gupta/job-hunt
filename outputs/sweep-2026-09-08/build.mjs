import fs from 'node:fs/promises';
import {Workbook, SpreadsheetFile} from '@oai/artifact-tool';
const dir = '/Users/prab/Downloads/claud jobs/outputs/sweep-2026-09-08';
const data = JSON.parse(await fs.readFile('/Users/prab/Downloads/claud jobs/loop/shortlist-2026-09-08.json','utf8'));
const wb = Workbook.create();
function sheet(name,headers,rows,widths){
  const s=wb.worksheets.add(name);
  s.showGridLines=false;
  s.getRangeByIndexes(0,0,rows.length+1,headers.length).values=[headers,...rows];
  const all=s.getUsedRange();
  all.format.font={name:'Arial',size:11};
  all.format.wrapText=true;
  all.format.verticalAlignment='top';
  all.format.rowHeight=120;
  s.getRangeByIndexes(0,0,1,headers.length).format={fill:'#17324D',font:{bold:true,color:'#FFFFFF'},rowHeight:34};
  widths.forEach((w,i)=>s.getRangeByIndexes(0,i,rows.length+1,1).format.columnWidth=w);
  rows.forEach((r,i)=>{if(i%2===0)s.getRangeByIndexes(i+1,0,1,headers.length).format.fill='#EFF5FA';});
  s.freezePanes.freezeRows(1);
  return s;
}
sheet('Priority leads',['Fit /100','Company and role','Location / freshness','Why it fits','Gaps and conditions','Compensation','Posting URL','Verification'],data.roles.map(r=>[r.fit,r.company+'\n'+r.title,r.location+'\n'+r.posted,r.why,r.watch_outs,r.comp,r.url,r.verification]),[10,32,35,53,56,34,55,45]);
sheet('Flagged outcomes',['Company and role','Status','Reason / next check','Source URL'],data.watch.map(r=>[r.company+'\n'+r.title,r.status,r.reason,r.url]),[33,30,92,65]);
const notes=sheet('Search notes',['Sweep notes'],data.notes.map(t=>[t]),[135]);
notes.getUsedRange().format.rowHeight=55;
notes.getRange('A1').format.rowHeight=30;
wb.recalculate();
console.log((await wb.inspect({kind:'table',range:'Priority leads!A1:B6',include:'values',tableMaxRows:6,tableMaxCols:2})).ndjson);
for(const [name,range,file] of [['Priority leads','A1:E6','priority.png'],['Flagged outcomes','A1:C10','flagged.png'],['Search notes','A1:A10','notes.png']]){
  const preview=await wb.render({sheetName:name,range,scale:1,format:'png'});
  await fs.writeFile(dir+'/'+file,new Uint8Array(await preview.arrayBuffer()));
}
await (await SpreadsheetFile.exportXlsx(wb)).save(dir+'/New job shortlist - 2026-09-08.xlsx');
console.log('Exported shortlist.');
