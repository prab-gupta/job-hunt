# Search playbook — where the roles actually are

Everything here was tested with the WebSearch / WebFetch tools rather than assumed. The point
of writing it down is that a job sweep burns most of its budget on dead ends: SPA boards that
render nothing, aggregators reposting stale listings, and postings that quietly closed weeks
ago. Use the verified paths, skip the graveyard, and spend the saved calls on verification.

**Never fetch job pages with curl, wget, or python requests.** WebSearch and WebFetch are the
only permitted ways to reach the web here. If something is blocked, it stays blocked.

---

## 1. The two mechanisms

**WebSearch with `allowed_domains`** — this is a *hard* filter, unlike a `site:` operator which
is only a ranking hint. Restricting to ATS hosts is the single highest-precision move
available: it returns individual live postings instead of SEO farms and aggregators. Prefer it.

```
WebSearch(query="AI automation engineer remote Europe",
          allowed_domains=["jobs.ashbyhq.com","job-boards.greenhouse.io"])
```

**WebFetch on a board listing page** — good boards expose path-based taxonomies (region,
country, category) that return dozens of listings in one call, with posting ages. Use these
for breadth and for freshness, then verify individual postings.

Run several of both in parallel in one message. Sweeping six sources at once and then
verifying is far faster than a serial crawl — with one exception noted below (Himalayas).

---

## 2. ATS domains, ranked by yield

| Domain | Why | Notes |
|---|---|---|
| `jobs.ashbyhq.com` | **Best single source for discovery.** Modern AI companies, EMEA-aware titles, no index-page noise. The only ATS that reliably discloses **salary bands**, often in several currencies. | Canonical URL is `jobs.ashbyhq.com/<org>/<uuid>` — strip `?embed=js`, `/application`, `?utm_data=…`, `?locationId=…`. **But read the posting through the API, not the page:** Ashby HTML pages frequently come back as an unrendered JS shell ("You need to enable JavaScript"), and a shell looks exactly like a closed role. One API call per org covers every posting it has, so it's cheaper anyway. |
| `job-boards.greenhouse.io` | High volume, clean single postings. Salary usually absent. | Note the **hyphenated** host. |
| `job-boards.eu.greenhouse.io` | EU data-residency variant that surfaces European employers the `.com` host misses (JetBrains, Prolific, Clarity AI, saasgroup). | Query it *in addition to* the `.com` host, not instead. |
| `jobs.smartrecruiters.com` | Solid individual postings, location often in the title string. | Use this host. **`careers.smartrecruiters.com` returns only board index pages — skip it.** |
| `join.com` | Good for European startups and, unusually, plenty of explicit contract / part-time listings. | Clean single-posting parse. |
| `jobs.personio.com` | DACH-heavy, low competition. Real host is `<company>.jobs.personio.com/job/<id>`. | Append `?language=en` — many boards default to German. |
| `jobs.lever.co` | Works, but the noisiest. | **Snippets lie about location.** A posting titled "…(Remote, Full-Time)" surfaced under a "remote Europe" query and turned out to be India-only. Also heavy with aggregators (Jobgether) and outsourcing firms. Always fetch before trusting. |

Legacy `boards.greenhouse.io/<co>/jobs/<id>` 302-redirects off-host (costs two calls), and
`boards.greenhouse.io/embed/job_board` is robots-disallowed. `apply.workable.com` job pages are
a client-side SPA that silently degrade to the company's "Current Openings" page — read Workable
through its widget API instead (§5).

---

## 3. Query recipes that returned real hits

Role phrase + remote + region, domain-restricted:

- `AI automation engineer remote Europe` → n8n, Quora, Quadrivia, Oh (MarTech AI & Automation, remote Europe), Bifrost, DoiT
- `"forward deployed engineer" remote Europe` → Cohere, ElevenLabs, Luma, Camunda EMEA
- `AI solutions engineer remote EMEA` → Mistral, Camunda, WunderGraph, Omni
- `"technical product manager" remote Europe`

**Contract intent — put the literal contract vocabulary in the query.** Asking for "contract"
generically returns permanent roles; these words work:

- `freelance contractor AI automation engineer "contract" remote day rate n8n` → Kairos "Contract Software Engineer", Hippocratic AI "Junior Forward Deployment Engineer (Contract)", a 12-month Ansible AAP contract on join.com, Scalia "AI Automation Specialist (Part time)", G2i
- Also try: `"6-month contract"`, `"12-month contract"`, `"fixed-term"`, `(Contract)`, `B2B`, `part time`, `fractional`

**Stack keywords are his edge.** `n8n`, `low-code`, `AI agents`, `Bubble.io`, `Playwright`,
`Zapier`/`Make`/`Tray.ai` postings are far less crowded than generic "AI Engineer" listings.
Run at least one stack-keyword query per sweep.

**Company-direct.** For a named company, `WebFetch` its board index —
`job-boards.greenhouse.io/<company>` fetches fine as a bulk company-wide listing with no API
token — or query `allowed_domains=["jobs.ashbyhq.com"]` with the company name.

Unrestricted generic queries (`AI solutions engineer remote EMEA jobs`) return aggregator SEO
farms with almost no direct-apply links. Their one use is **host discovery** — that's how
`job-boards.eu.greenhouse.io` turned up.

---

## 4. Job boards worth fetching

| Board | What it gives | Verified URL templates |
|---|---|---|
| **euremotejobs.com** | Best European board tested. Region strings distinguish "Europe" / "EMEA" / worldwide — exactly the filter that matters. Freshest feed seen (listings minutes old). Salary on roughly a third. | `/job-region/remote-jobs-europe/` · `/job-region/remote-jobs-emea/` · `/job-region/{spain,portugal,germany,ireland,uk}/` · `/jobs/remote-software-engineering-jobs/` · `/jobs/remote-data-jobs/` · `/jobs/all-remote-jobs/` |
| **remoterocketship.com** | **Signal only** — it surfaces on-target Italy-remote roles other sources miss, but its pages expose no direct-apply URLs, so a row can't be sourced from here. Use it to learn *company + title*, then find the original posting via an ATS search. Keyword + country + recency compose in one URL; EUR salaries, dates to the minute. | `https://www.remoterocketship.com/country/italy?page=1&sort=DateAdded&jobTitle=AI%20Engineer` · `https://www.remoterocketship.com/?page=1&sort=DateAdded&locations=Europe` |
| **himalayas.app** | Uniquely states the **region restriction per job** ("Netherlands only", "Global", "United Kingdom only") — kills the biggest time-waster, the secretly-US-only "remote" role. | `/jobs` · `/jobs/countries/italy` · `/jobs/python` · `/jobs/engineering` · `?page=N`. **Serialize these calls** — it 429s under concurrency, and paths don't compose (`/jobs/countries/italy/skills/python` → 404). |
| **arbeitnow.com** (JSON) | Clean JSON: title, company, `remote`, `location`, `tags`, `created_at` epoch. DACH-heavy, mixed non-tech — filter hard. | `https://arbeitnow.com/api/job-board-api` |
| **remoteok.com** (JSON only) | HTML page is an empty JS shell; the API works. Global overflow. **Its `salary_min`/`salary_max` are `$0` — ignore them.** | `https://remoteok.com/api` |
| **aijobs.net** | Best salary transparency of any board (EUR bands on most rows), strongly on-target for AI/ML. Company names don't always extract. | `https://aijobs.net/` — filter params unverified, don't invent them |
| **wellfound.com** | US-skewed, no posting dates — but now in scope since he's open to non-EU and contract work. | `https://wellfound.com/role/r/software-engineer` |

**Dead or blocked — don't spend calls here:** weworkremotely.com (returns binary),
welcometothejungle.com, landing.jobs, jobicy.com, linkedin.com/jobs (all robots-disallowed),
nofluffjobs.com (403), EURES / europa.eu jobs portal and jobs.eu (JS shell / bad TLS),
workatastartup.com (renders fragments only), remotive.com and workingnomads.com (listing pages
render navigation only — no jobs), freelancermap.com (paths 404 without discovery).

Freelance marketplaces — Malt, Braintrust, Contra, Upwork, Toptal — are login-walled or
client-rendered. Don't burn a sweep on them. Contract work comes through the ATS contract
queries in §3, contract-first shops with public boards (e.g. **G2i** on Ashby), and the
part-time/contract listings on **join.com** and **euremotejobs.com**.

---

## 5. Public JSON APIs — use these to verify

These fetch as text and expose exactly the fields needed to confirm a posting is live:

- **Greenhouse:** `https://boards-api.greenhouse.io/v1/boards/<token>/jobs?content=true` → `absolute_url`, `updated_at`, locations. Best freshness check available.
- **Ashby:** `https://api.ashbyhq.com/posting-api/job-board/<org>?includeCompensation=true` → `isRemote`, `isListed`, `publishedAt`, `compensation`.
- **Lever:** `https://api.lever.co/v0/postings/<co>?mode=json` → `workplaceType` (Remote/Hybrid), location. Fails on very large aggregator boards.
- **Workable:** `https://apply.workable.com/api/v1/widget/accounts/<subdomain>?details=true` → the only readable route into Workable.

**WebFetch truncates long JSON**, and its summariser will quietly under-report: asking
"list all jobs" on a big board returned 7 of N and omitted roles that exist. Ask a *targeted*
question instead — "does this board currently list a Forward Deployed Engineer role, and what
is its location and posted date?"

**A negative answer from a board API is not evidence on its own.** Truncation produces
*fabricated* negatives — one read stated four target roles were "not present" when the board
simply hadn't been fully returned. Before concluding a role is closed, either get two
independent reads that agree, or corroborate with a differently-shaped source. Concluding
"closed" wrongly costs him a real opportunity, so the burden of proof sits on the negative.

---

## 6. Verification traps

Search indexes run stale across every ATS, so a posting found in search may already be gone.
These are the specific failure modes, and the first one is dangerous because the fetch
*succeeds*:

1. **Greenhouse closed postings degrade to the board index.** Fetching a dead job URL returns the company's entire open-roles list with the target role absent, and nothing flags it. **Detection rule: if a single-posting fetch comes back describing many different jobs, the posting is closed.** Drop it.
2. **Personio closed postings hard-404** even while still indexed in search. Clean failure — just drop.
3. **Lever snippets misstate location.** Fetch the posting and read the location from the page body.
4. **"Remote" ≠ eligible.** Read the eligibility sentence, not the word "Remote" in the title. Titles like "AI Automation Engineer (Remote – ES/UK only)" are common, and boards sometimes label a region-locked role "worldwide".
5. **Aggregators masquerade as employers.** Jobgether, Jobgether-on-Lever, and similar reposts have no named end client. Skip them; find the original posting if the role looks good.
6. **Himalayas orders results non-chronologically** — page 1 mixed "2 mins ago" with "27 days ago". Read the date on each row rather than trusting position.
7. **Ashby pages return JS shells intermittently.** `meta-title: Jobs` or "You need to enable JavaScript to run this app" means the fetch failed, *not* that the role closed. Go to the org's posting API (§5) — and remember §5's rule that a negative there needs a second read. Three failures like this nearly cost the highest-relevance company of one sweep.

---

## 7. Freshness

- Minute-level ages: euremotejobs, remoterocketship, himalayas, aijobs.net (parse from the page).
- Sortable by recency in the URL: only `remoterocketship.com/?sort=DateAdded` is verified.
- Programmatic date filtering: only via the JSON APIs (`created_at` / `date` / `epoch` / `updated_at`).
- No board tested exposes a verified "posted within N days" parameter — filter client-side.
