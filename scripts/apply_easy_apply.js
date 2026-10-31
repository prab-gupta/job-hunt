const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

async function applyToJob(jobId, pdfPath, answers = {}) {
  if (!pdfPath || !fs.existsSync(pdfPath)) {
    throw new Error(`Bespoke CV PDF not found at: ${pdfPath}`);
  }
  const resolvedPdfPath = path.resolve(pdfPath);
  console.log(`Starting application for Job ${jobId} with bespoke CV: ${resolvedPdfPath}`);

  const cdpUrl = process.env.CDP_URL || 'http://127.0.0.1:9222';
  const browser = await puppeteer.connect({ browserURL: cdpUrl });
  const pages = await browser.pages();
  const page = pages[0] || (await browser.newPage());

  const url = `https://www.linkedin.com/jobs/view/${jobId}/`;
  console.log(`Navigating to ${url}...`);
  await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await new Promise(r => setTimeout(r, 2500));

  // Extract Title & Company
  const jobInfo = await page.evaluate(() => {
    const title = document.querySelector('.job-details-jobs-unified-top-card__job-title, h1')?.innerText.trim() || '';
    const company = document.querySelector('.job-details-jobs-unified-top-card__company-name, .job-details-jobs-unified-top-card__primary-description a')?.innerText.trim() || '';
    const easyApplyBtn = Array.from(document.querySelectorAll('button')).find(b => b.getAttribute('aria-label') === 'Easy Apply to this job' || b.innerText.trim() === 'Easy Apply');
    const alreadyApplied = Array.from(document.querySelectorAll('span, div, button')).some(el => el.innerText && el.innerText.includes('Application submitted'));
    return { title, company, hasEasyApply: !!easyApplyBtn, alreadyApplied };
  });

  console.log('Job Info:', jobInfo);

  if (jobInfo.alreadyApplied) {
    console.log('Job already applied!');
    browser.disconnect();
    return { status: 'ALREADY_APPLIED', ...jobInfo };
  }

  if (!jobInfo.hasEasyApply) {
    console.log('No Easy Apply button found.');
    browser.disconnect();
    return { status: 'NO_EASY_APPLY', ...jobInfo };
  }

  // Click Easy Apply
  await page.evaluate(() => {
    const btn = Array.from(document.querySelectorAll('button')).find(b => b.getAttribute('aria-label') === 'Easy Apply to this job' || b.innerText.trim() === 'Easy Apply');
    if (btn) btn.click();
  });
  await new Promise(r => setTimeout(r, 2000));

  let uploadedPdf = false;
  let step = 1;
  while (step <= 15) {
    console.log(`--- Processing Step ${step} ---`);
    await new Promise(r => setTimeout(r, 1000));

    // Check for safety warning modal (e.g. stealth startups)
    const handledWarning = await page.evaluate(() => {
      const continueBtn = Array.from(document.querySelectorAll('button, a')).find(el => el.innerText && el.innerText.trim().toLowerCase() === 'continue applying');
      if (continueBtn) {
        continueBtn.click();
        return true;
      }
      return false;
    });
    if (handledWarning) {
      console.log('Dismissed Job search safety reminder by clicking Continue applying.');
      await new Promise(r => setTimeout(r, 2000));
      continue;
    }

    // Check if we are on the Resume page and have not uploaded yet
    const isResumePage = await page.evaluate(() => {
      const dialog = document.querySelector('dialog, div[role="dialog"]') || document.body;
      const text = dialog.innerText.toLowerCase();
      const hasUploadBtn = Array.from(dialog.querySelectorAll('button')).some(b => b.innerText.toLowerCase().includes('upload resume') || b.innerText.toLowerCase().includes('carica'));
      return hasUploadBtn || text.includes('select or upload a resume') || text.includes('curriculum');
    });

    if (isResumePage && !uploadedPdf) {
      console.log('Detected Resume selection page! Uploading bespoke curated CV...');
      try {
        const [fileChooser] = await Promise.all([
          page.waitForFileChooser({ timeout: 5000 }),
          page.evaluate(() => {
            const uploadBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.toLowerCase().includes('upload resume') || b.innerText.toLowerCase().includes('carica'));
            if (uploadBtn) uploadBtn.click();
          })
        ]);
        await fileChooser.accept([resolvedPdfPath]);
        console.log(`Successfully uploaded bespoke CV: ${path.basename(resolvedPdfPath)}`);
        uploadedPdf = true;
        await new Promise(r => setTimeout(r, 3500));
      } catch (e) {
        console.log(`File upload via chooser failed: ${e.message}. Verifying radio fallback.`);
      }
    }

    // Robust city/location typeahead selection
    try {
      const box = await page.evaluate(() => {
        const dialog = document.querySelector('dialog, div[role="dialog"]') || document.body;
        const el = dialog.querySelector('input[data-testid="typeahead-input"], input[placeholder*="city" i], input[placeholder*="location" i], input[placeholder*="città" i]');
        if (!el || (el.value && el.value.toLowerCase().includes('venice'))) return null;
        el.scrollIntoView({ block: 'center' });
        const r = el.getBoundingClientRect();
        return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
      });
      if (box) {
        console.log('Detected city/location typeahead input. Selecting Venice, Veneto, Italy...');
        await page.mouse.click(box.x, box.y);
        await new Promise(r => setTimeout(r, 300));
        await page.keyboard.down('Meta');
        await page.keyboard.press('a');
        await page.keyboard.up('Meta');
        await page.keyboard.press('Backspace');
        await new Promise(r => setTimeout(r, 200));
        await page.keyboard.type('Venice', { delay: 80 });
        await new Promise(r => setTimeout(r, 1500));
        await page.evaluate(() => {
          const opt = document.querySelector('div[role="option"], li[role="option"], [data-testid*="typeahead"] div, ul[role="listbox"] li');
          if (opt) opt.click();
        });
        await new Promise(r => setTimeout(r, 500));
      }
    } catch (e) {
      console.log('Typeahead selection error:', e.message);
    }

    const state = await page.evaluate((customAnswers) => {
      const dialog = document.querySelector('dialog, div[role="dialog"]') || document.body;

      // 1. Phone number
      const phoneInput = dialog.querySelector('input[type="tel"]') || document.getElementById('_r_i_');
      if (phoneInput && !phoneInput.value) {
        phoneInput.focus();
        Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(phoneInput, '3516107807');
        phoneInput.dispatchEvent(new Event('input', { bubbles: true }));
        phoneInput.dispatchEvent(new Event('change', { bubbles: true }));
      }

      // 2. Text & Numeric inputs (Years of experience, salary, etc.)
      const textInputs = Array.from(dialog.querySelectorAll('input[type="text"], input[type="number"], textarea'));
      for (const input of textInputs) {
        if (!input.value) {
          const label = (dialog.querySelector(`label[for="${input.id}"]`)?.innerText || input.getAttribute('aria-label') || '').toLowerCase();
          let fillVal = '3';
          if (label.includes('stipendio') || label.includes('salary') || label.includes('retribuzione')) {
            fillVal = '50000';
          } else if (label.includes('python') || label.includes('sql') || label.includes('eng') || label.includes('esperienza') || label.includes('years')) {
            fillVal = '4';
          } else if (label.includes('notice') || label.includes('preavviso')) {
            fillVal = '2 weeks';
          }
          input.focus();
          Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set.call(input, fillVal);
          input.dispatchEvent(new Event('input', { bubbles: true }));
          input.dispatchEvent(new Event('change', { bubbles: true }));
        }
      }

      // 3. Checkboxes (Consent / Terms / Required)
      const checkboxes = Array.from(dialog.querySelectorAll('input[type="checkbox"]'));
      for (const cb of checkboxes) {
        const aria = (cb.getAttribute('aria-label') || '').toLowerCase();
        const container = cb.closest('fieldset, .jobs-easy-apply-form-section__grouping, div[data-test-form-builder-group], div.fb-single-checkbox') || cb.parentElement?.parentElement || cb.parentElement;
        const containerText = ((container?.innerText || '') + ' ' + (cb.getAttribute('aria-label') || '') + ' ' + dialog.innerText.slice(0, 1000)).toLowerCase();
        const isFollowCompany = (cb.closest('div')?.innerText || '').toLowerCase().includes('follow') && (cb.closest('div')?.innerText || '').toLowerCase().includes('stay up to date');
        if (!isFollowCompany) {
          if (cb.required || containerText.includes('consent') || containerText.includes('agree') || containerText.includes('privacy') || containerText.includes('termini') || containerText.includes('autorizzo') || containerText.includes('required') || containerText.includes('*')) {
            if (!cb.checked) {
              cb.click();
              cb.checked = true;
              cb.dispatchEvent(new Event('change', { bubbles: true }));
            }
          }
        }
      }

      // 4. Radio choices (Yes/No questions)
      const radios = Array.from(dialog.querySelectorAll('input[type="radio"]'));
      const radioGroups = {};
      for (const r of radios) {
        const name = r.name || r.getAttribute('name') || 'default';
        if (!radioGroups[name]) radioGroups[name] = [];
        radioGroups[name].push(r);
      }
      for (const name in radioGroups) {
        const group = radioGroups[name];
        const isChecked = group.some(r => r.checked);
        if (!isChecked) {
          let selected = group.find(r => {
            const labelText = (r.closest('label')?.innerText || r.parentElement?.innerText || r.getAttribute('aria-label') || '').toLowerCase();
            return labelText.includes('sì') || labelText.includes('si') || labelText.includes('yes');
          }) || group[0];
          selected.click();
          selected.checked = true;
          selected.dispatchEvent(new Event('change', { bubbles: true }));
        }
      }

      // 5. Select dropdowns
      const selects = Array.from(dialog.querySelectorAll('select'));
      for (const sel of selects) {
        if (!sel.value || sel.value === '') {
          const opt = Array.from(sel.options).find(o => 
            o.value.toLowerCase().includes('prof') || 
            o.text.toLowerCase().includes('prof') ||
            o.value.toLowerCase().includes('yes') ||
            o.text.toLowerCase().includes('sì')
          ) || sel.options[1];
          if (opt) {
            sel.value = opt.value;
            sel.dispatchEvent(new Event('change', { bubbles: true }));
          }
        }
      }

      // Check buttons
      const buttons = Array.from(dialog.querySelectorAll('button'));
      const submitBtn = buttons.find(b => b.innerText.trim() === 'Submit application' || b.getAttribute('aria-label') === 'Submit application');
      const reviewBtn = buttons.find(b => b.innerText.trim() === 'Review' || b.getAttribute('aria-label') === 'Review your application');
      const nextBtn = buttons.find(b => b.innerText.trim() === 'Next' || b.getAttribute('aria-label')?.includes('Next'));

      return {
        hasSubmit: !!submitBtn,
        hasReview: !!reviewBtn,
        hasNext: !!nextBtn,
        dialogTitle: dialog.querySelector('h2, h3, h1')?.innerText || ''
      };
    }, answers);

    console.log('Step state:', state);

    if (state.hasSubmit) {
      console.log('Submitting application...');
      await page.evaluate(() => {
        const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Submit application' || b.getAttribute('aria-label') === 'Submit application');
        if (btn) btn.click();
      });
      await new Promise(r => setTimeout(r, 3000));

      // Dismiss confirmation dialog
      await page.evaluate(() => {
        const dismissBtn = Array.from(document.querySelectorAll('button')).find(b => b.getAttribute('aria-label') === 'Dismiss' || b.innerText.trim() === 'Done');
        if (dismissBtn) dismissBtn.click();
      });

      console.log('Application submitted successfully!');
      browser.disconnect();
      return { status: 'SUBMITTED', uploadedPdf, ...jobInfo };
    }

    if (state.hasReview) {
      console.log('Clicking Review...');
      await page.evaluate(() => {
        const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Review' || b.getAttribute('aria-label') === 'Review your application');
        if (btn) btn.click();
      });
      step++;
      continue;
    }

    if (state.hasNext) {
      console.log('Clicking Next...');
      await page.evaluate(() => {
        const btn = Array.from(document.querySelectorAll('button')).find(b => b.innerText.trim() === 'Next' || b.getAttribute('aria-label')?.includes('Next'));
        if (btn) btn.click();
      });
      step++;
      continue;
    }

    console.log('No Next/Review/Submit button found. Breaking.');
    break;
  }

  browser.disconnect();
  return { status: 'UNKNOWN', ...jobInfo };
}

if (require.main === module) {
  const jobId = process.argv[2];
  const pdfPath = process.argv[3];
  if (!jobId || !pdfPath) {
    console.error('Usage: node apply_easy_apply.js <jobId> <pdfPath>');
    process.exit(1);
  }
  applyToJob(jobId, pdfPath).then(res => {
    console.log('RESULT:', JSON.stringify(res, null, 2));
    process.exit(res.status === 'SUBMITTED' ? 0 : 1);
  }).catch(err => {
    console.error('Error applying to job:', err);
    process.exit(1);
  });
}

module.exports = { applyToJob };
