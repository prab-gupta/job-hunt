import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "/Users/prab/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/@oai/artifact-tool/dist/artifact_tool.mjs";

const outputPath = "/Users/prab/Downloads/claud jobs/pending_applications_2026-08-24.xlsx";
const previewPath = "/Users/prab/Downloads/claud jobs/tmp/pending_applications_2026-08-24-preview.png";

const pending = [
  [1, "Progress Partners", "Middle AI Automation Engineer", "AI Automation", "European Union", "Remote", "2026-08-24", 94, "READY TO APPLY", "CV and factual fields", "Not disclosed", "https://jobs.ashbyhq.com/progress-partners/4ffba6ff-6936-46b3-a149-1452a6119ff9", "2+ years, LLM automation, REST APIs, JavaScript or Python, support AI", "No major gate. Salary field asks monthly gross", "New, not in applications.csv or seen_jobs.json"],
  [2, "ESTO Group", "AI Automation Engineer", "AI Automation", "Tallinn, Estonia", "Hybrid", "2026-08-19", 91, "FORM REVIEW", "Employer form", "Not disclosed", "https://jobs.esto.eu/jobs/8235300-ai-automation-engineer", "Agentic workflows, APIs, integrations, back-office automation, attitude over credentials", "Relocation to Tallinn likely", "New, not in applications.csv or seen_jobs.json"],
  [3, "FIRST.bet", "AI Automation Engineer", "AI Automation", "Sofia, Bulgaria", "Office / flexible hours", "2026-08-18", 90, "FORM REVIEW", "LinkedIn listing", "Not disclosed", "https://www.linkedin.com/jobs/view/4445500490", "TypeScript or Python, LLMs, agents, APIs, cloud, workflow orchestration", "Betting domain. Decline optional future-retention consent", "New, not in applications.csv or seen_jobs.json"],
  [4, "Insurely", "AI Automation Engineer", "AI Automation", "Stockholm, Sweden", "Hybrid", "2026-08-18", 88, "FORM REVIEW", "Employer form", "Not disclosed", "https://careers.insurely.com/jobs/8236484-ai-automation-engineer", "Hands-on AI automation, LLMs, scripts, APIs, internal tooling, fintech", "Relocation to Stockholm likely", "New, not in applications.csv or seen_jobs.json"],
  [5, "Proxima Fusion", "AI Solutions Engineer", "AI Solutions", "Munich, Germany", "On-site", "2026-08-20", 86, "FORM REVIEW", "Ashby form", "Not disclosed", "https://jobs.ashbyhq.com/proxima-fusion/2810dcc6-770f-43a3-9fb6-d7c8a39a0833", "n8n, LangGraph, agents, REST APIs, MCP and internal automation", "Stronger Python, Docker and GCP expectations", "New, not in applications.csv or seen_jobs.json"],
  [6, "WaveSix", "AI & Automation Engineer", "AI Automation", "Berlin, Germany", "Remote / client visits", "2026-08-24", 84, "FORM REVIEW", "Company careers page", "Not disclosed", "https://wavesix.ai/career", "Agents, RAG, LLM APIs, integrations, n8n and Make listed as bonuses", "Core asks Python and data engineering depth", "New, not in applications.csv or seen_jobs.json"],
  [7, "Solutions 360", "AI Automation Engineer", "AI Automation", "Pyrgos, Greece", "Not stated", "2026-08-23", 83, "VERIFY LANGUAGE", "LinkedIn listing", "Not disclosed", "https://www.linkedin.com/jobs/view/4455094303", "n8n, LLM APIs, Supabase, Postgres, REST APIs, webhooks, entry level", "Posting is in Greek; work language and location policy not stated", "New, not in applications.csv or seen_jobs.json"],
  [8, "C12", "AI Automation Engineer", "AI Automation", "Paris, France", "On-site", "2026-08-17", 82, "STRETCH", "Lever form", "EUR 46,000-50,000", "https://jobs.lever.co/c12qe/ed14ed9c-b652-4d64-b9e5-d2852ef0f995", "n8n, agents, MCP, API integrations, workflow ownership", "Strong Python, self-hosted LLM, DevOps, GPU and Ansible depth", "New, not in applications.csv or seen_jobs.json"],
  [9, "Scout24", "AI Automation Engineer", "Applied AI / Automation", "Berlin, Germany", "Hybrid, 3 office days", "2026-08-24", 76, "NEEDS USER", "Required project answers", "Not disclosed", "https://www.scout24.com/en/career/jobs/engineering/ai-automation-engineer-d-m-f-8102734", "Production AI apps, enterprise workflows, APIs, background jobs, observability", "Senior-level wording and two required written project questions", "New, not in applications.csv or seen_jobs.json"],
];

const removed = [
  ["Hays", "AI Engineer", "Already submitted; unnamed client and ML-heavy requirements"],
  ["Jet HR", "AI Software Engineer", "ML/data role requiring advanced Python and model tuning"],
  ["Moviri", "AI Engineer", "Already submitted through Greenhouse"],
  ["Yakkyo", "Backend / Full-Stack", "Generic backend/full-stack, outside target lanes"],
  ["Amaris", "Software Engineer", "Outside target lanes and requires Italian speaker"],
  ["TeamSystem", "Backend Developer", "Generic backend, outside target lanes"],
  ["Prima", "Software / ML Engineer", "Python and ML-core gate"],
  ["Accessiway", "Fullstack Developer", "Generic full-stack, outside target lanes"],
  ["Accessiway", "Backend Developer", "Generic backend, outside target lanes"],
  ["DUNE Talent", "AI / ML Engineer", "Unnamed recruiting intermediary and ML-heavy"],
  ["Translated", "Full Stack Engineer", "Generic full-stack, outside target lanes"],
  ["Alpitronic", "Full Stack Web", "Generic web/full-stack, outside target lanes"],
  ["Fujifilm", "Front-End Developer", "Frontend-only, outside target lanes"],
  ["Alpitronic", "UI Developer", "UI-only, outside target lanes"],
  ["TAS Bologna", "Senior AI Software Engineer", "No verified JD to clear seniority and ML gates"],
  ["TAS Rome", "Senior AI Software Engineer", "Duplicate role family, no verified JD to clear gates"],
  ["NTT DATA Rome", "Senior ML Engineer", "Senior model-building role"],
  ["NTT DATA Cosenza", "Senior ML Engineer", "Senior model-building role"],
];

const workbook = Workbook.create();
const queue = workbook.worksheets.add("Pending Queue");
queue.showGridLines = false;
queue.getRange("A1:O1").merge();
queue.getRange("A1").values = [["Corrected FDE, AI and Automation Application Queue"]];
queue.getRange("A2:O2").merge();
queue.getRange("A2").values = [["Source of truth: .proficiently/preferences.md. Only live roles from the last 14 days. Dedupe checked against applications.csv and seen_jobs.json on 2026-08-24."]];
const headers = [["Rank", "Company", "Role", "Lane", "Location", "Work mode", "Posted", "Fit", "Readiness", "Form", "Salary", "URL", "Why it fits", "Risks / gaps", "Dedupe"]];
queue.getRange("A4:O4").values = headers;
queue.getRange(`A5:O${4 + pending.length}`).values = pending;
queue.tables.add(`A4:O${4 + pending.length}`, true, "PendingQueueTable");
queue.freezePanes.freezeRows(4);
queue.getRange("A1:O1").format = { fill: "#172554", font: { bold: true, color: "#FFFFFF", size: 16 }, verticalAlignment: "center" };
queue.getRange("A1:O1").format.rowHeight = 30;
queue.getRange("A2:O2").format = { fill: "#DBEAFE", font: { color: "#1E3A8A", italic: true }, wrapText: true };
queue.getRange("A4:O4").format = { fill: "#1D4ED8", font: { bold: true, color: "#FFFFFF" }, wrapText: true };
queue.getRange(`A5:O${4 + pending.length}`).format = { verticalAlignment: "top", wrapText: true };
queue.getRange(`H5:H${4 + pending.length}`).format.numberFormat = "0";
queue.getRange(`H5:H${4 + pending.length}`).conditionalFormats.add("colorScale", {
  criteria: [
    { type: "lowestValue", color: "#FEE2E2" },
    { type: "percentile", value: 50, color: "#FEF3C7" },
    { type: "highestValue", color: "#DCFCE7" },
  ],
});
queue.getRange(`I5:I${4 + pending.length}`).conditionalFormats.add("containsText", { text: "READY", format: { fill: "#DCFCE7", font: { color: "#166534", bold: true } } });
queue.getRange(`I5:I${4 + pending.length}`).conditionalFormats.add("containsText", { text: "NEEDS USER", format: { fill: "#FEF3C7", font: { color: "#92400E", bold: true } } });
queue.getRange(`I5:I${4 + pending.length}`).conditionalFormats.add("containsText", { text: "STRETCH", format: { fill: "#FEE2E2", font: { color: "#991B1B", bold: true } } });

const widths = [7, 18, 29, 21, 22, 20, 12, 8, 17, 18, 18, 46, 44, 44, 38];
for (let col = 0; col < widths.length; col++) {
  queue.getRangeByIndexes(0, col, 4 + pending.length, 1).format.columnWidth = widths[col];
}
queue.getRange(`A5:A${4 + pending.length}`).format.horizontalAlignment = "center";
queue.getRange(`H5:H${4 + pending.length}`).format.horizontalAlignment = "center";

const audit = workbook.worksheets.add("Removed Old Queue");
audit.showGridLines = false;
audit.getRange("A1:C1").merge();
audit.getRange("A1").values = [["Removed from the previous generic-tech queue"]];
audit.getRange("A3:C3").values = [["Company", "Role", "Removal reason"]];
audit.getRange(`A4:C${3 + removed.length}`).values = removed;
audit.tables.add(`A3:C${3 + removed.length}`, true, "RemovedQueueTable");
audit.freezePanes.freezeRows(3);
audit.getRange("A1:C1").format = { fill: "#7F1D1D", font: { bold: true, color: "#FFFFFF", size: 15 } };
audit.getRange("A3:C3").format = { fill: "#991B1B", font: { bold: true, color: "#FFFFFF" } };
audit.getRange(`A4:C${3 + removed.length}`).format = { wrapText: true, verticalAlignment: "top" };
audit.getRange(`A1:A${3 + removed.length}`).format.columnWidth = 22;
audit.getRange(`B1:B${3 + removed.length}`).format.columnWidth = 32;
audit.getRange(`C1:C${3 + removed.length}`).format.columnWidth = 70;

const scope = workbook.worksheets.add("Sweep Rules");
scope.showGridLines = false;
scope.getRange("A1:B1").merge();
scope.getRange("A1").values = [["Definitive sweep scope"]];
scope.getRange("A3:B12").values = [
  ["Priority 1", "Forward Deployed Engineer / Forward-Deployed AI Engineer"],
  ["Priority 2", "AI Engineer / Applied AI Engineer building agents and LLM applications"],
  ["Priority 3", "Technical AI Solutions Engineer / Sales Engineer"],
  ["Priority 4", "AI Automation Engineer using n8n or Make plus code"],
  ["Priority 5", "AI-tooling Developer Advocate / DevRel"],
  ["Priority 6", "GTM Engineer"],
  ["Exclude", "Generic frontend, backend, full-stack, QA, SDET, data science and technical PM"],
  ["Hard gate", "5+ years, technical degree, undeclared language, model training, unnamed staffing, unpaid or talent pool"],
  ["Geography", "EU on-site or hybrid allowed; outside EU remote only"],
  ["Recency", "Posted within 14 days"],
];
scope.getRange("A1:B1").format = { fill: "#172554", font: { bold: true, color: "#FFFFFF", size: 15 } };
scope.getRange("A3:A12").format = { fill: "#DBEAFE", font: { bold: true, color: "#1E3A8A" } };
scope.getRange("A3:B12").format = { wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: "#CBD5E1" } };
scope.getRange("A1:A12").format.columnWidth = 18;
scope.getRange("B1:B12").format.columnWidth = 80;

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);
const preview = await workbook.render({ sheetName: "Pending Queue", autoCrop: "all", scale: 0.75, format: "png" });
await fs.writeFile(previewPath, new Uint8Array(await preview.arrayBuffer()));

const inspection = await workbook.inspect({ kind: "sheet,table,region", sheetId: "Pending Queue", range: `A1:O${4 + pending.length}`, maxChars: 12000, tableMaxRows: 14, tableMaxCols: 15, tableMaxCellChars: 120 });
console.log(inspection.ndjson);
