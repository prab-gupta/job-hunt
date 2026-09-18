import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const historyPath = "/Users/prab/Downloads/claud jobs/applications.csv";
const outputPath = "/Users/prab/Downloads/claud jobs/pending_applications_2026-08-24.xlsx";

const sweep = [
  [1, "High", "AI Engineer - Generative AI & Autonomous Agents", "Hays", "Milan, Italy", "2026-08-24", "https://it.linkedin.com/jobs/view/ai-engineer-generative-ai-autonomous-agents-at-hays-4439208386"],
  [2, "High", "AI Software Engineer", "Jet HR", "Turin, Italy", "2026-08-20", "https://it.linkedin.com/jobs/view/ai-software-engineer-at-jet-hr-4456762931"],
  [3, "High", "Backend Developer (Node.js / TypeScript) - Full Remote", "WeHunt", "Milan, Italy (Remote)", "2026-08-04", "https://it.linkedin.com/jobs/view/backend-developer-node-js-typescript-full-remote-at-wehunt-4448290485"],
  [4, "High", "AI Engineer", "Live Story", "Milan, Italy", "2026-06-08", "https://it.linkedin.com/jobs/view/ai-engineer-at-live-story-4425916662"],
  [5, "High", "AI Engineer", "Moviri", "Milan, Italy", "2026-07-31", "https://it.linkedin.com/jobs/view/ai-engineer-at-moviri-4445094325"],
  [6, "High", "Backend / Full-Stack Developer (Node.js + MongoDB)", "Yakkyo", "Milan, Italy", "2026-08-19", "https://it.linkedin.com/jobs/view/backend-full-stack-developer-node-js-mongodb-at-yakkyo-4456308134"],
  [7, "High", "Software Engineer (TypeScript/Node.js)", "Amaris Consulting", "Varese, Italy", "2026-08-22", "https://it.linkedin.com/jobs/view/software-engineer-typescript-node-js-italian-speaker-at-amaris-consulting-4411457839"],
  [8, "High", "Backend Developer Node.js & TypeScript", "TeamSystem", "Milan, Italy", "2026-08-07", "https://it.linkedin.com/jobs/view/backend-developer-node-js-typescript-at-teamsystem-4445160506"],
  [9, "Med", "Software / Machine Learning Engineer", "Prima", "Milan, Italy", "2026-08-12", "https://it.linkedin.com/jobs/view/software-machine-learning-engineer-at-prima-4443791348"],
  [10, "Med", "Fullstack Developer", "Accessiway", "Turin, Italy", "2026-08-20", "https://it.linkedin.com/jobs/view/fullstack-developer-at-accessiway-4419441356"],
  [11, "Med", "Backend Developer", "Accessiway", "Turin, Italy", "2026-08-08", "https://it.linkedin.com/jobs/view/backend-developer-at-accessiway-4404944451"],
  [12, "Med", "AI & Machine Learning Engineer", "DUNE Talent", "Rome, Italy", "2026-07-28", "https://it.linkedin.com/jobs/view/ai-machine-learning-engineer-at-dune-talent-4445745869"],
  [13, "Med", "Full Stack Engineer (On-site)", "Translated", "Rome, Italy", "2026-08-19", "https://it.linkedin.com/jobs/view/full-stack-engineer-on-site-at-translated-4453400720"],
  [14, "Med", "Full Stack Developer - Web Applications", "Alpitronic", "Bolzano, Italy", "2026-08-15", "https://it.linkedin.com/jobs/view/full-stack-developer-web-applications-m-f-d-at-alpitronic-4414300635"],
  [15, "Med", "Software Developer Front-End", "Fujifilm Italia", "Bolzano, Italy", "2026-08-19", "https://it.linkedin.com/jobs/view/software-developer-front-end-at-fujifilm-italia-4456335016"],
  [16, "Med", "Software Developer - User Interfaces", "Alpitronic", "Bolzano, Italy", "2026-08-22", "https://it.linkedin.com/jobs/view/software-developer-user-interfaces-m-f-d-at-alpitronic-4411889069"],
  [17, "Low", "Senior AI Software Engineer", "TAS", "Bologna, Italy", "2026-06-24", "https://it.linkedin.com/jobs/view/senior-ai-software-engineer-at-tas-4310735002"],
  [18, "Low", "Senior AI Software Engineer", "TAS", "Rome, Italy", "2026-06-24", "https://it.linkedin.com/jobs/view/senior-ai-software-engineer-at-tas-4331741158"],
  [19, "Low", "Senior Machine Learning Engineer", "NTT DATA", "Rome, Italy", "2026-08-07", "https://it.linkedin.com/jobs/view/senior-machine-learning-engineer-at-ntt-data-europe-latam-4441472240"],
  [20, "Low", "Senior Machine Learning Engineer", "NTT DATA", "Cosenza, Italy", "2026-08-07", "https://it.linkedin.com/jobs/view/senior-machine-learning-engineer-at-ntt-data-europe-latam-4441454933"],
];

const risks = {
  1: "Recruiting agency. Check Italian and remote or hybrid expectations.",
  2: "Check Italian working-language requirement. A different Jet HR role is already tracked.",
  5: "Verify whether the role requires ML research or model training.",
  6: "Verify remote scope and required MongoDB depth.",
  7: "The title states Italian speaker. Candidate Italian is beginner level.",
  8: "Check Italian language requirement and remote policy.",
  9: "ML-heavy title. Verify applied engineering versus model training.",
  10: "Check Italian language requirement and Turin attendance.",
  11: "Check Italian language requirement and Turin attendance.",
  12: "Recruiting agency. Verify end client, language, and ML depth.",
  13: "On-site in Rome. Check relocation or attendance feasibility.",
  14: "Check Bolzano attendance, remote policy, and language requirement.",
  15: "Frontend-focused role. Check Bolzano attendance and role fit.",
  16: "UI-focused role. Check Bolzano attendance and role fit.",
  17: "Senior title and ML-specific experience gap.",
  18: "Senior title and ML-specific experience gap.",
  19: "Senior ML title and ML-specific experience gap. A different NTT DATA role is tracked.",
  20: "Senior ML title and ML-specific experience gap. A different NTT DATA role is tracked.",
};

function normalize(value) {
  return String(value ?? "")
    .normalize("NFKD")
    .toLowerCase()
    .replace(/[^a-z0-9]+/g, " ")
    .trim();
}

function jobId(url) {
  const match = String(url ?? "").match(/(\d{10})(?:[/?#]|$)/);
  return match ? match[1] : "";
}

function companiesMatch(a, b) {
  const left = normalize(a);
  const right = normalize(b);
  return left === right || left.includes(right) || right.includes(left);
}

function isTerminal(status) {
  return /^(SUBMITTED|DROPPED|REJECTED|CLOSED|WITHDRAWN|DUPLICATE)/i.test(String(status ?? ""));
}

function nextAction(fit, risk) {
  if (risk?.includes("Italian speaker")) return "Check language gate before applying";
  if (risk?.includes("On-site")) return "Check on-site feasibility";
  if (fit === "High") return "Review JD, then apply";
  if (fit === "Med") return "Evaluate fit before applying";
  return "Low priority, verify seniority and ML depth";
}

const historyCsv = await fs.readFile(historyPath, "utf8");
const historyWorkbook = await Workbook.fromCSV(historyCsv, { sheetName: "Applications" });
const historySheet = historyWorkbook.worksheets.getItem("Applications");
const historyValues = historySheet.getUsedRange().values;
const headers = historyValues[0];
const history = historyValues.slice(1).map((row) => Object.fromEntries(headers.map((header, index) => [header, row[index] ?? ""])));

const reconciled = sweep.map(([number, fit, role, company, location, posted, url]) => {
  const exactId = jobId(url);
  const exact = history.find((entry) => exactId && jobId(entry.url) === exactId);
  const sameRole = history.find((entry) => companiesMatch(entry.company, company) && normalize(entry.role) === normalize(role));
  const match = exact || sameRole;
  const otherCompanyRoles = history.filter((entry) => companiesMatch(entry.company, company) && entry !== match);
  const done = Boolean(match && isTerminal(match.status));
  let historyCheck = "No matching role found";
  if (match) historyCheck = `${match.status}: ${match.role}`;
  else if (otherCompanyRoles.length) historyCheck = `Different role tracked: ${otherCompanyRoles[0].role}`;
  return {
    number,
    fit,
    role,
    company,
    location,
    posted,
    url,
    match,
    historyCheck,
    decision: done ? "DONE" : "PENDING",
    risk: risks[number] ?? "Review full job description before applying.",
  };
});

const pending = reconciled.filter((job) => job.decision === "PENDING");

const workbook = Workbook.create();
const summary = workbook.worksheets.add("Queue Summary");
const queue = workbook.worksheets.add("Pending Queue");
const reconciliation = workbook.worksheets.add("Reconciliation");

summary.mergeCells("A1:D1");
summary.getRange("A1").values = [["Job Application Queue - 24 Aug 2026"]];
summary.getRange("A1:D1").format = {
  fill: "#1F4E78",
  font: { bold: true, color: "#FFFFFF", size: 16 },
  horizontalAlignment: "center",
  verticalAlignment: "center",
};
summary.getRange("A1:D1").format.rowHeight = 30;
summary.getRange("A3:B8").values = [
  ["Metric", "Count"],
  ["Sweep roles", null],
  ["Already completed", null],
  ["Pending applications", null],
  ["Pending high fit", null],
  ["Pending medium fit", null],
];
summary.getRange("B4:B8").formulas = [
  ["=COUNTA(Reconciliation!A2:A1000)"],
  ["=COUNTIF(Reconciliation!I2:I1000,\"DONE\")"],
  ["=COUNTA('Pending Queue'!A2:A1000)"],
  ["=COUNTIF('Pending Queue'!B2:B1000,\"High\")"],
  ["=COUNTIF('Pending Queue'!B2:B1000,\"Med\")"],
];
summary.getRange("A3:B3").format = { fill: "#D9EAF7", font: { bold: true, color: "#1F1F1F" } };
summary.getRange("A3:B8").format.borders = {
  insideHorizontal: { style: "thin", color: "#D9E2F3" },
  insideVertical: { style: "thin", color: "#D9E2F3" },
  bottom: { style: "thin", color: "#A6A6A6" },
};
summary.getRange("A10:D13").values = [
  ["Queue rule", "Meaning", "Status", "Action"],
  ["Done", "Exact job submitted or a terminal decision already recorded", "DONE", "Do not reapply"],
  ["Pending", "No completed match for this exact role", "PENDING", "Review and apply in priority order"],
  ["Company match", "A different role at the same company exists in history", "PENDING", "Treat as a separate application"],
];
summary.getRange("A10:D10").format = { fill: "#1F4E78", font: { bold: true, color: "#FFFFFF" } };
summary.getRange("A11:D13").format.wrapText = true;
summary.getRange("A3:A13").format.font = { bold: true };
summary.getRange("A1:A13").format.columnWidth = 25;
summary.getRange("B1:B13").format.columnWidth = 54;
summary.getRange("C1:C13").format.columnWidth = 16;
summary.getRange("D1:D13").format.columnWidth = 34;

const queueHeaders = [["Priority", "Fit", "Company", "Role", "Location", "Posted", "Queue status", "Next action", "Risk or gate", "URL"]];
const queueRows = pending.map((job, index) => [
  index + 1,
  job.fit,
  job.company,
  job.role,
  job.location,
  job.posted,
  "PENDING REVIEW",
  nextAction(job.fit, job.risk),
  job.risk,
  job.url,
]);
queue.getRange(`A1:J${queueRows.length + 1}`).values = [...queueHeaders, ...queueRows];
queue.tables.add(`A1:J${queueRows.length + 1}`, true, "PendingQueueTable").style = "TableStyleMedium2";
queue.freezePanes.freezeRows(1);
queue.getRange("A1:J1").format = { fill: "#1F4E78", font: { bold: true, color: "#FFFFFF" }, wrapText: true };
queue.getRange(`A2:J${queueRows.length + 1}`).format.verticalAlignment = "top";
queue.getRange(`D2:J${queueRows.length + 1}`).format.wrapText = true;
queue.getRange(`A1:A${queueRows.length + 1}`).format.columnWidth = 10;
queue.getRange(`B1:B${queueRows.length + 1}`).format.columnWidth = 9;
queue.getRange(`C1:C${queueRows.length + 1}`).format.columnWidth = 22;
queue.getRange(`D1:D${queueRows.length + 1}`).format.columnWidth = 43;
queue.getRange(`E1:E${queueRows.length + 1}`).format.columnWidth = 26;
queue.getRange(`F1:F${queueRows.length + 1}`).format.columnWidth = 13;
queue.getRange(`G1:G${queueRows.length + 1}`).format.columnWidth = 18;
queue.getRange(`H1:H${queueRows.length + 1}`).format.columnWidth = 34;
queue.getRange(`I1:I${queueRows.length + 1}`).format.columnWidth = 58;
queue.getRange(`J1:J${queueRows.length + 1}`).format.columnWidth = 66;
queue.getRange(`B2:B${queueRows.length + 1}`).conditionalFormats.add("containsText", { text: "High", format: { fill: "#E2F0D9", font: { color: "#375623", bold: true } } });
queue.getRange(`B2:B${queueRows.length + 1}`).conditionalFormats.add("containsText", { text: "Med", format: { fill: "#FFF2CC", font: { color: "#7F6000", bold: true } } });
queue.getRange(`B2:B${queueRows.length + 1}`).conditionalFormats.add("containsText", { text: "Low", format: { fill: "#FCE4D6", font: { color: "#9C0006", bold: true } } });

const reconciliationHeaders = [["Sweep #", "Fit", "Company", "Role", "LinkedIn job ID", "Posted", "History check", "Recorded status", "Decision", "URL"]];
const reconciliationRows = reconciled.map((job) => [
  job.number,
  job.fit,
  job.company,
  job.role,
  jobId(job.url),
  job.posted,
  job.historyCheck,
  job.match?.status ?? "",
  job.decision,
  job.url,
]);
reconciliation.getRange("A1:J21").values = [...reconciliationHeaders, ...reconciliationRows];
reconciliation.tables.add("A1:J21", true, "ReconciliationTable").style = "TableStyleMedium2";
reconciliation.freezePanes.freezeRows(1);
reconciliation.getRange("A1:J1").format = { fill: "#1F4E78", font: { bold: true, color: "#FFFFFF" }, wrapText: true };
reconciliation.getRange("A2:J21").format.verticalAlignment = "top";
reconciliation.getRange("D2:J21").format.wrapText = true;
reconciliation.getRange("A1:A21").format.columnWidth = 10;
reconciliation.getRange("B1:B21").format.columnWidth = 9;
reconciliation.getRange("C1:C21").format.columnWidth = 24;
reconciliation.getRange("D1:D21").format.columnWidth = 45;
reconciliation.getRange("E1:F21").format.columnWidth = 15;
reconciliation.getRange("G1:G21").format.columnWidth = 54;
reconciliation.getRange("H1:I21").format.columnWidth = 24;
reconciliation.getRange("J1:J21").format.columnWidth = 66;
reconciliation.getRange("I2:I21").conditionalFormats.add("containsText", { text: "DONE", format: { fill: "#E2F0D9", font: { color: "#375623", bold: true } } });
reconciliation.getRange("I2:I21").conditionalFormats.add("containsText", { text: "PENDING", format: { fill: "#FFF2CC", font: { color: "#7F6000", bold: true } } });

const output = await SpreadsheetFile.exportXlsx(workbook);
await output.save(outputPath);

const summaryInspect = await workbook.inspect({ kind: "region", sheetId: "Queue Summary", range: "A1:D13", maxChars: 5000 });
const queueInspect = await workbook.inspect({ kind: "region", sheetId: "Pending Queue", range: `A1:J${queueRows.length + 1}`, maxChars: 8000, tableMaxRows: 25, tableMaxCols: 10 });
const errors = await workbook.inspect({ kind: "match", searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A", options: { useRegex: true, maxResults: 100 }, summary: "final formula error scan" });

console.log(JSON.stringify({
  outputPath,
  sweepCount: reconciled.length,
  pendingCount: pending.length,
  completedCount: reconciled.length - pending.length,
  completed: reconciled.filter((job) => job.decision === "DONE").map((job) => ({ company: job.company, role: job.role, status: job.match?.status })),
  pending: pending.map((job) => ({ number: job.number, company: job.company, role: job.role })),
  summaryInspect: summaryInspect.ndjson,
  queueInspect: queueInspect.ndjson,
  errors: errors.ndjson,
}, null, 2));
