#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import process from "node:process";
import { chromium } from "/Users/prab/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright/index.mjs";

const value = name => {
  const index = process.argv.indexOf(`--${name}`);
  if (index < 0 || !process.argv[index + 1]) throw new Error(`missing --${name}`);
  return process.argv[index + 1];
};
const manifest = JSON.parse(fs.readFileSync(value("manifest"), "utf8"));
const profile = JSON.parse(fs.readFileSync(value("profile"), "utf8"));
const cv = value("cv");
const letter = value("letter");
const evidenceDir = value("evidence-dir");
const submit = process.argv.includes("--submit");
const headed = process.argv.includes("--headed");

if (!manifest.released || manifest.state !== "CONFIRMED") throw new Error("manifest not released");
if (manifest.company !== manifest.confirmed_item?.company || manifest.role !== manifest.confirmed_item?.role) {
  throw new Error("manifest identity mismatch");
}

const browser = await chromium.launch({ headless: !headed });
const page = await browser.newPage();
try {
  const applicationUrl = manifest.direct_url.replace(/\/job\/(\d+)(\?)/, "/job/$1/apply$2");
  if (applicationUrl === manifest.direct_url) throw new Error("unsupported Personio URL");
  await page.goto(applicationUrl, { waitUntil: "domcontentloaded", timeout: 45000 });
  await page.getByRole("textbox", { name: "First", exact: true }).fill(profile.first_name);
  await page.getByRole("textbox", { name: "Last", exact: true }).fill(profile.last_name);
  await page.getByRole("textbox", { name: "Email (required)", exact: true }).fill(profile.email);
  const phone = page.getByRole("textbox", { name: "Phone", exact: true });
  if (await phone.count()) await phone.fill(profile.phone);
  const linkedin = page.getByRole("textbox", { name: "LinkedIn", exact: true });
  if (await linkedin.count()) await linkedin.fill(profile.linkedin_url);
  const available = page.getByRole("textbox", { name: "Available from (required)", exact: true });
  if (await available.count()) await available.fill("Immediately");
  await page.getByRole("textbox", { name: "Expected salary (required)", exact: true })
    .fill("EUR 30,000-40,000, negotiable");
  const consent = page.getByRole("combobox", { name: /talent pool/i });
  if (await consent.count()) await consent.selectOption({ label: "No" });
  await page.locator("#doc-input-cv").setInputFiles(cv);
  await page.locator("#doc-input-other").setInputFiles(letter);
  const cvName = await page.locator("#doc-input-cv").evaluate(input => input.files?.[0]?.name || "");
  const letterName = await page.locator("#doc-input-other").evaluate(input => input.files?.[0]?.name || "");
  if (cvName !== path.basename(cv) || letterName !== path.basename(letter)) {
    throw new Error("uploaded filenames are not visible");
  }
  const button = page.getByRole("button", { name: "Submit Application", exact: true });
  for (let attempt = 0; attempt < 10 && !(await button.isEnabled()); attempt++) {
    await page.waitForTimeout(500);
  }
  if (!(await button.isEnabled())) throw new Error("Submit Application is disabled after filling");
  if (!submit) {
    console.log(JSON.stringify({ state: "DRY_RUN", opportunity_id: manifest.opportunity_id }));
  } else {
    await button.click();
    await page.waitForTimeout(2500);
    const bodyAfter = await page.locator("body").innerText();
    const confirmation = bodyAfter.split("\n").find(line => /thank|application.+received/i.test(line)) || "";
    if (!confirmation) throw new Error("confirmation evidence absent after Submit");
    fs.mkdirSync(evidenceDir, { recursive: true, mode: 0o700 });
    const screenshot = path.join(evidenceDir, `${manifest.opportunity_id}-personio-submitted.png`);
    await page.screenshot({ path: screenshot, fullPage: true });
    fs.chmodSync(screenshot, 0o600);
    console.log(JSON.stringify({ state: "SUBMITTED", opportunity_id: manifest.opportunity_id,
      evidence: confirmation.trim(), evidence_path: screenshot }));
  }
} finally {
  await browser.close();
}
