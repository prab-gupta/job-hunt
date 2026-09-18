#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { chromium } from "/Users/prab/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";

const arg = name => {
  const i = process.argv.indexOf(`--${name}`);
  if (i < 0 || !process.argv[i + 1]) throw new Error(`missing --${name}`);
  return process.argv[i + 1];
};
const manifest = JSON.parse(fs.readFileSync(arg("manifest"), "utf8"));
const profile = JSON.parse(fs.readFileSync(arg("profile"), "utf8"));
const cv = arg("cv");
const letter = arg("letter");
const evidenceDir = arg("evidence-dir");
const submit = process.argv.includes("--submit");
if (!manifest.released || manifest.state !== "CONFIRMED") throw new Error("manifest not released");
if (manifest.company !== manifest.confirmed_item?.company || manifest.role !== manifest.confirmed_item?.role) {
  throw new Error("manifest identity mismatch");
}

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage();
try {
  await page.goto(manifest.direct_url, { waitUntil: "domcontentloaded", timeout: 45000 });
  await page.getByLabel("First Name", { exact: true }).fill(profile.first_name);
  await page.getByLabel("Last Name", { exact: true }).fill(profile.last_name);
  await page.getByLabel("Preferred First Name", { exact: true }).fill(profile.first_name);
  await page.getByLabel("Email", { exact: true }).fill(profile.email);
  await page.locator("#resume").setInputFiles(cv);
  await page.locator("#cover_letter").setInputFiles(letter);
  await page.getByLabel("Please provide a link to your LinkedIn profile.", { exact: true })
    .fill(profile.linkedin_url);
  const shipped = page.getByRole("combobox", { name: /built and shipped an AI\/LLM-powered/i });
  await shipped.click();
  await page.getByRole("option", { name: "Yes", exact: true }).click();
  await page.getByLabel("Tell us about the most sophisticated AI or agentic system you’ve built and shipped to production.", { exact: true }).fill(
    "The most sophisticated AI system I have shipped was part of FlowSpace, a live marketplace that grew from around 2,000 to more than 4,500 users. I built AI support agents alongside scraping and parsing tools, then integrated them into the product while migrating the platform from Bubble to Next.js and Laravel. The challenge was not simply calling a model. It was making AI useful within real workflows and real marketplace data. I also built an n8n and Eden AI workflow at UltraStrategy for parsing CVs. Across these projects, I worked directly with OpenAI and Anthropic APIs and learned how to connect model outputs to practical product actions."
  );
  await page.getByLabel("How do you currently use AI coding agents in your day-to-day engineering work?", { exact: true }).fill(
    "I use Claude Code daily to inspect existing codebases, trace behavior across files, propose focused implementations, debug issues and review changes. I still verify generated code, understand it line by line and test the resulting behavior before shipping. This is especially useful across a Next.js frontend and Laravel backend, where a small feature can touch several layers. I treat the agent as an engineering collaborator, not as a replacement for technical judgment."
  );
  await page.getByLabel("Tell us about a time an AI/LLM system you built behaved differently in production than you expected.", { exact: true }).fill(
    "A model can perform well on clean examples but behave less consistently with real user or scraped data. Inputs vary in structure, completeness and wording, so output is not always as predictable as the prototype suggests. I encountered this while building scraping and parsing tools and a CV-parsing workflow. It changed my approach: I define the expected output clearly, validate the response and design the surrounding workflow so that an imperfect model response does not silently become trusted application data."
  );
  await page.getByLabel("What is your current location and right to work status?", { exact: true }).fill(
    "Venice, Italy. I hold an Italian EU long-term residence permit and do not require sponsorship to work in the EU."
  );
  await page.getByLabel("What is your notice period / availability to start?", { exact: true }).fill("Available immediately.");
  const uploaded = await page.locator("input[type=file]").evaluateAll(inputs =>
    inputs.map(input => input.files?.[0]?.name || ""));
  if (!uploaded.includes(path.basename(cv)) || !uploaded.includes(path.basename(letter))) {
    throw new Error("CV or cover letter attachment missing");
  }
  const missing = await page.locator("input[required],textarea[required],select[required]").evaluateAll(elements =>
    elements.filter(element => element.type !== "hidden" && !element.value).map(element => element.name || element.id));
  if (missing.length) throw new Error(`required fields missing: ${missing.join(",")}`);
  fs.mkdirSync(evidenceDir, { recursive: true, mode: 0o700 });
  const preflight = path.join(evidenceDir, `${manifest.opportunity_id}-dwelly-pre-submit.png`);
  await page.screenshot({ path: preflight, fullPage: true });
  fs.chmodSync(preflight, 0o600);
  if (!submit) {
    console.log(JSON.stringify({ state: "DRY_RUN", opportunity_id: manifest.opportunity_id, uploaded }));
  } else {
    await page.getByRole("button", { name: "Submit application", exact: true }).click();
    await page.waitForTimeout(4000);
    const text = await page.locator("body").innerText();
    const evidence = text.split("\n").find(line => /thank you|application.+submitted|application.+received/i.test(line)) || "";
    if (!evidence) throw new Error("Submit attempted but success evidence absent; CAPTCHA or validation may be blocking");
    const screenshot = path.join(evidenceDir, `${manifest.opportunity_id}-dwelly-submitted.png`);
    await page.screenshot({ path: screenshot, fullPage: true });
    fs.chmodSync(screenshot, 0o600);
    console.log(JSON.stringify({ state: "SUBMITTED", opportunity_id: manifest.opportunity_id,
      evidence: evidence.trim(), evidence_path: screenshot }));
  }
} finally {
  await browser.close();
}
