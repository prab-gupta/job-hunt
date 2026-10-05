const puppeteer = require('puppeteer-core');
const fs = require('fs');
const path = require('path');

function getAppliedIds() {
  const ids = new Set();
  const files = ['loop/applications.csv', 'data/csvs/applications.csv'];
  for (const f of files) {
    if (fs.existsSync(f)) {
      const content = fs.readFileSync(f, 'utf8');
      const matches = content.matchAll(/\/jobs\/view\/(\d+)/g);
      for (const m of matches) {
        ids.add(m[1]);
      }
    }
  }
  return ids;
}

async function searchJobs(keyword, location = '', count = 5) {
  const appliedIds = getAppliedIds();
  console.log(`Loaded ${appliedIds.size} already-applied job IDs.`);

  const browser = await puppeteer.connect({ browserURL: 'http://127.0.0.1:9223' });
  const page = await browser.newPage();

  const queryUrl = `https://www.linkedin.com/jobs/search/?keywords=${encodeURIComponent(keyword)}&location=${encodeURIComponent(location)}&f_AL=true&f_TPR=r604800&sortBy=DD`;
  console.log(`Navigating to: ${queryUrl}`);
  await page.goto(queryUrl, { waitUntil: 'domcontentloaded', timeout: 30000 });
  await new Promise(r => setTimeout(r, 3500));

  // Extract job cards
  const jobCards = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.job-card-container, .jobs-search-results__list-item, div[data-job-id]'));
    const results = [];
    for (const card of cards) {
      const id = card.getAttribute('data-job-id') || card.getAttribute('data-occludable-job-id');
      const titleEl = card.querySelector('.job-card-list__title--link, a.job-card-container__link, a[data-control-id]');
      const companyEl = card.querySelector('.artdeco-entity-lockup__subtitle, .job-card-container__primary-description');
      const locEl = card.querySelector('.artdeco-entity-lockup__caption, .job-card-container__metadata-item');
      
      const title = titleEl ? titleEl.innerText.trim() : '';
      const company = companyEl ? companyEl.innerText.trim() : '';
      const loc = locEl ? locEl.innerText.trim() : '';

      if (id && title) {
        results.push({ id, title, company, loc, url: `https://www.linkedin.com/jobs/view/${id}/` });
      }
    }
    return results;
  });

  console.log(`Found ${jobCards.length} job cards on search page.`);
  
  // Deduplicate and filter out already applied
  const uniqueCandidates = [];
  const seenIds = new Set();
  for (const job of jobCards) {
    if (!seenIds.has(job.id) && !appliedIds.has(job.id)) {
      seenIds.add(job.id);
      uniqueCandidates.push(job);
    }
  }

  console.log(`Found ${uniqueCandidates.length} unapplied unique candidate jobs.`);

  // For the top candidates, fetch the JD
  const detailedJobs = [];
  for (const cand of uniqueCandidates.slice(0, count * 2)) {
    if (detailedJobs.length >= count) break;
    console.log(`Fetching JD for: [${cand.id}] ${cand.company} - ${cand.title}`);
    try {
      await page.goto(cand.url, { waitUntil: 'domcontentloaded', timeout: 20000 });
      await new Promise(r => setTimeout(r, 2500));

      const details = await page.evaluate(() => {
        const text = document.body.innerText;
        let jd = '';
        const idx = text.indexOf('About the job');
        if (idx !== -1) {
          const after = text.slice(idx + 'About the job'.length);
          const endMatch = after.match(/\n(About the company|People also viewed|Similar jobs|Job details|Applicant Insights)/i);
          const endIdx = endMatch ? endMatch.index : 3000;
          jd = after.slice(0, endIdx).trim();
        } else {
          const jdEl = document.querySelector('.jobs-description-content__text, .jobs-box__html-content, #job-details, article');
          jd = jdEl ? jdEl.innerText.trim() : '';
        }

        const easyApplyBtn = Array.from(document.querySelectorAll('button')).find(b => b.getAttribute('aria-label') === 'Easy Apply to this job' || b.innerText.trim() === 'Easy Apply');
        const alreadySubmitted = Array.from(document.querySelectorAll('span, div, button')).some(el => el.innerText && el.innerText.includes('Application submitted'));
        return { jd, hasEasyApply: !!easyApplyBtn, alreadySubmitted };
      });

      if (details.hasEasyApply && !details.alreadySubmitted && details.jd.length > 50) {
        detailedJobs.push({
          ...cand,
          jd: details.jd
        });
      } else {
        console.log(`Skipping [${cand.id}]: hasEasyApply=${details.hasEasyApply}, alreadySubmitted=${details.alreadySubmitted}, jdLen=${details.jd.length}`);
      }
    } catch (e) {
      console.log(`Error fetching JD for ${cand.id}: ${e.message}`);
    }
  }

  await page.close();
  browser.disconnect();

  return detailedJobs;
}

if (require.main === module) {
  const keyword = process.argv[2] || 'Automation Engineer';
  const location = process.argv[3] || 'Italy';
  const count = parseInt(process.argv[4] || '5', 10);

  searchJobs(keyword, location, count).then(results => {
    console.log(`\n=== CANDIDATE JOBS FOUND (${results.length}) ===`);
    console.log(JSON.stringify(results.map(r => ({ id: r.id, title: r.title, company: r.company, loc: r.loc })), null, 2));
    fs.writeFileSync('scripts/candidate_jobs.json', JSON.stringify(results, null, 2));
    console.log('Saved detailed candidate jobs to scripts/candidate_jobs.json');
  }).catch(err => {
    console.error('Search error:', err);
    process.exit(1);
  });
}

module.exports = { searchJobs };
