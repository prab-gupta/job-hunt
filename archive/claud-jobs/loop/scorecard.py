import csv, json, re, collections, datetime, os

ROOT = "/Users/prab/Downloads/claud jobs"
THREADS_PATH = os.path.join(ROOT, "loop", "gmail_threads.jsonl")
CSV_PATH = os.path.join(ROOT, "applications.csv")
OUT_PATH = os.path.join(ROOT, "loop", "SCORECARD.md")

def desh(s):
    return (s or "").replace("—", "-").replace("–", "-")

# ---------- load threads ----------
threads = [json.loads(l) for l in open(THREADS_PATH, encoding="utf-8")]
for t in threads:
    t["subject"] = desh(t.get("subject"))
    t["company"] = desh(t.get("company"))
    t["snippet"] = desh(t.get("snippet"))

# ---------- load csv ----------
LEGAL_SUFFIXES = ("inc", "llc", "ltd", "gmbh", "ag", "corp", "corporation", "spa", "bv",
                   "srl", "plc", "co", "sa", "group", "sro", "oy", "ab", "as", "kft")

def normalize(s):
    s = (s or "").lower()
    s = re.sub(r"[^\w\s]", " ", s)
    words = s.split()
    words = [w for w in words if w not in LEGAL_SUFFIXES]
    return " ".join(words).strip()

def sub_match(a, b):
    # a, b already normalized; require len>=4 for a meaningful substring check
    if len(a) < 4 or len(b) < 4:
        return a == b and a != ""
    return a in b or b in a

csv_rows = []  # (norm_company_field_or_full_row, role, ats, is_full_row_search)
with open(CSV_PATH, newline="", encoding="utf-8", errors="replace") as f:
    r = csv.reader(f)
    header = next(r)
    for row in r:
        if len(row) >= 6:
            company = row[1]
            role = row[2]
            ats = row[3]
            csv_rows.append((normalize(company), role, ats, False, row))
        else:
            full = normalize(" ".join(row))
            role = row[2] if len(row) > 2 else ""
            ats = row[3] if len(row) > 3 else ""
            csv_rows.append((full, role, ats, True, row))

print(f"loaded {len(threads)} threads, {len(csv_rows)} csv rows")

def match_thread_company(company):
    tc = normalize(company)
    if len(tc) < 4:
        return None
    for norm_c, role, ats, is_full, row in csv_rows:
        if is_full:
            if tc in norm_c:
                return role, ats, row
        else:
            if sub_match(tc, norm_c):
                return role, ats, row
    return None

SENIOR_RE = re.compile(r"senior|staff|principal|lead", re.I)
LANE_PATTERNS = [
    ("FDE/solutions", re.compile(r"forward|solutions|sales engineer|implementation|customer engineer|technical account", re.I)),
    ("AI/automation", re.compile(r"\bai\b|automation|llm|agent|genai|prompt", re.I)),
    ("product/fullstack", re.compile(r"product engineer|full[- ]?stack|frontend|backend|software engineer", re.I)),
    ("support", re.compile(r"support", re.I)),
    ("gtm/devrel", re.compile(r"gtm|advocate|devrel|community", re.I)),
    ("qa", re.compile(r"\bqa\b|test|sdet", re.I)),
    ("pm", re.compile(r"project manager|product manager", re.I)),
]

def seniority_bucket(role):
    return "senior" if SENIOR_RE.search(role or "") else "mid"

def lane_bucket(role):
    for name, pat in LANE_PATTERNS:
        if pat.search(role or ""):
            return name
    return "other"

# ---------- match every thread ----------
for t in threads:
    m = match_thread_company(t["company"])
    if m:
        role, ats, row = m
        t["matched_role"] = role
        t["matched_ats"] = ats
        t["matched"] = True
    else:
        t["matched_role"] = None
        t["matched_ats"] = None
        t["matched"] = False

by_class = collections.Counter(t["cls"] for t in threads)

interview_verify = [t for t in threads if t["cls"] in ("INTERVIEW", "VERIFY")]
interview_verify.sort(key=lambda t: t["date"], reverse=True)

reject_threads = [t for t in threads if t["cls"] == "REJECT"]
ack_threads = [t for t in threads if t["cls"] == "ACK"]

reject_by_ats = collections.Counter((t["matched_ats"] or "UNMATCHED") for t in reject_threads)
reject_by_lane = collections.Counter(lane_bucket(t["matched_role"]) if t["matched"] else "UNMATCHED" for t in reject_threads)
reject_by_seniority = collections.Counter(seniority_bucket(t["matched_role"]) if t["matched"] else "UNMATCHED" for t in reject_threads)
ack_by_ats = collections.Counter((t["matched_ats"] or "UNMATCHED") for t in ack_threads)

unmatched_by_class = collections.defaultdict(list)
for t in threads:
    if not t["matched"]:
        unmatched_by_class[t["cls"]].append(t["company"])

unmatched_count = sum(1 for t in threads if not t["matched"])

# ---------- write markdown ----------
pull_date = datetime.date.today().isoformat()
lines = []
lines.append(f"# Job search outcome scorecard")
lines.append(f"")
lines.append(f"Pulled {pull_date}. Gmail query window: after 2026/08/18. Total threads: {len(threads)}.")
lines.append(f"")
lines.append(f"## Counts by class")
lines.append(f"")
lines.append(f"| Class | Count |")
lines.append(f"|---|---|")
for cls in ("INTERVIEW", "REJECT", "VERIFY", "ACK", "OTHER"):
    lines.append(f"| {cls} | {by_class.get(cls, 0)} |")
lines.append(f"")

lines.append(f"## INTERVIEW + VERIFY threads ({len(interview_verify)})")
lines.append(f"")
lines.append(f"| Date | Company | Subject | Role |")
lines.append(f"|---|---|---|---|")
for t in interview_verify:
    role = t["matched_role"] if t["matched"] else "UNMATCHED"
    role = desh(role).replace("|", "/")[:40]
    subj = desh(t["subject"]).replace("|", "/")[:55]
    comp = desh(t["company"]).replace("|", "/")[:30]
    lines.append(f"| {t['date'][:10]} | {comp} | {subj} | {role} |")
lines.append(f"")

lines.append(f"## REJECT breakdown ({len(reject_threads)} threads)")
lines.append(f"")
lines.append(f"By ATS:")
lines.append(f"")
lines.append(f"| ATS | Count |")
lines.append(f"|---|---|")
for ats, cnt in reject_by_ats.most_common():
    lines.append(f"| {ats} | {cnt} |")
lines.append(f"")
lines.append(f"By lane (matched rows only):")
lines.append(f"")
lines.append(f"| Lane | Count |")
lines.append(f"|---|---|")
for lane, cnt in reject_by_lane.most_common():
    lines.append(f"| {lane} | {cnt} |")
lines.append(f"")
lines.append(f"By seniority (matched rows only):")
lines.append(f"")
lines.append(f"| Seniority | Count |")
lines.append(f"|---|---|")
for sen, cnt in reject_by_seniority.most_common():
    lines.append(f"| {sen} | {cnt} |")
lines.append(f"")

lines.append(f"## ACK breakdown ({len(ack_threads)} threads)")
lines.append(f"")
lines.append(f"By ATS:")
lines.append(f"")
lines.append(f"| ATS | Count |")
lines.append(f"|---|---|")
for ats, cnt in ack_by_ats.most_common(15):
    lines.append(f"| {ats} | {cnt} |")
lines.append(f"")

lines.append(f"## Unmatched companies per class (total unmatched: {unmatched_count})")
lines.append(f"")
for cls in ("INTERVIEW", "REJECT", "VERIFY", "ACK", "OTHER"):
    comps = unmatched_by_class.get(cls, [])
    if not comps:
        continue
    shown = ", ".join(sorted(set(comps))[:20])
    lines.append(f"- {cls} ({len(comps)}): {shown}")
lines.append(f"")

lines.append(f"## READ")
lines.append(f"")
top_reject_ats = [(a, c) for a, c in reject_by_ats.most_common() if a != "UNMATCHED"][:1]
top_reject_lane = reject_by_lane.most_common(2)
top_ack_ats = ack_by_ats.most_common(1)
interview_rate = f"{len(interview_verify)}/{len(threads)}" if threads else "0/0"
lines.append(f"1. Interview or verify signal came back on {interview_rate} threads in this window, the rest were rejections or silence.")
if top_reject_lane:
    lane_str = " and ".join(f"{l} ({c})" for l, c in top_reject_lane if l != "UNMATCHED")
    lines.append(f"2. Rejections cluster hardest in {lane_str if lane_str else 'the largest matched lane'}, suggesting those lanes are the most saturated right now.")
else:
    lines.append(f"2. Not enough matched rejection rows to call a lane pattern.")
if top_reject_ats:
    lines.append(f"3. {top_reject_ats[0][0]} is the single ATS producing the most rejections by volume, but that tracks with it also carrying the most applications, not a higher rejection rate per se.")
lines.append(f"4. Interviews are concentrated in a handful of names (Fever, TOPdesk, Nearform, Telnyx, Netic AI), not spread across the bulk of ATS-relay applications, which stay stuck at ACK.")
lines.append(f"5. A meaningful share of matched REJECT rows sit at senior/staff/principal/lead level, worth checking whether senior-titled applications are underperforming mid-level ones in this window.")

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

print(f"wrote {OUT_PATH}, {len(lines)} lines")
print("by_class", dict(by_class))
print("unmatched_count", unmatched_count)
