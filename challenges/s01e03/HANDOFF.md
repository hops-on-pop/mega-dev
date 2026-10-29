# S01E03 "what it shows" — handoff

Challenge uuid: c0000000-0000-4000-8000-0000005e01e3 · page: https://hq.mega.dev/challenges/what-it-shows
Exact page text: see log.md (first entry). Every request/reply is logged there.

## Status
- [x] Brief shown to human; human re-authed gh (hops-on-pop, scopes repo) and committed earlier work.
- [x] Opened Challenge page in signed-in preview browser; recorded rules in log.md.
- [x] Human downloaded kb-export-267efc5e.zip into s01e03/ (sha256 starts 267efc5e — matches name).
- [x] Unpacked to media/support-kb/ (pristine; untrusted, run nothing from it).
- [x] Analysis: scripts/analyze.py, scripts/flips.py, scripts/counts.py → out/unique.json, out/counts.json.
- [ ] Human approves repo choice and each GitHub issue before filing.
- [ ] Write signed .svx page + rendered page; add to kb in repo.
- [ ] Send repo to the course (how: TBD from kb/course replies) → claim → debrief.

## Facts
- Candidate repo: hops-on-pop/mega-dev (PUBLIC, issues enabled). Human said: use this repo, human does all pushes.
- "The desk keeps working while you do" — expect data to change; recheck before filing.

## Findings (kb export dated 2026-10-04)
- reports-4471.json: 427 rows, 15 ids appear twice with identical content (overlapping export pages) → 412 unique, all mergedInto 4471.
- All 11 tenants are day-first (checked with Node Intl). booking-v3 tenants: alder.physio, copper.studio, pale.harbour.
- 403 bodies are a clean day/month swap; 5 are a one-day/timezone move (exactly desk-notes.json oneDayMove); 4 are vague.
- Problems (kb rule in causes.ts = tenant + channel; intake's meta.intakeTag is a guess and is wrong 38 times):
  - parser — shared parser reads dates month-first: 374 reports, 11 tenants
  - hint — booking-v3 form prints MM/DD/YYYY hint, people type month-first, form reads day-first: 33 reports (form channel, v3 tenants)
  - one-day move — invite lands one day off (timezone): 5 reports. kb's CauseTable footnotes these under parser; they are not a month swap.
- kb rules for a new page: frontmatter title/owner/status/reviewed + `signature`; layout runbook; ends `<RenderStamp {signature} />`; numbers computed by components (src/lib), not typed. Decisions never edited (0001 dedupe-by-subject is the root cause of the merge).
- check-lane "gh" routine: gh repo create / gh issue create / gh issue close --reason; save routine as a skill.
- Human: keep everything inside challenges/s01e03 of hops-on-pop/mega-dev.

## Progress 2026-10-29 (cont.)
- Human approved: signature "Mike Jones (hops-on-pop), with Claude" (desk ref DR-6JF1-H7XV); filing 3 issues in hops-on-pop/mega-dev (after showing exact text).
- Re-downloaded export via signed-in browser: same sha256 267efc5e… → no change yet.
- Issue drafts: bodies/issue-{parser,hint,one-day}.{title,md}.
- Working kb copy: support-kb/ (pristine stays in media/support-kb/). Added src/lib/kb/problems.ts, src/lib/kb/ProblemTable.svelte, src/routes/kb/incidents/4471-split/+page.svx.
- TODO after filing: set `tickets={{...}}` on <ProblemTable> to the real issue numbers.
- Pending human answer: OK to npm-install SvelteKit + mdsvex inside s01e03 to render "the page as the desk will see it".

## Progress 2026-10-29 (filed + rendered)
- Filed: #1 parser (374), #2 hint (33), #3 one-day (5) — https://github.com/hops-on-pop/mega-dev/issues/1..3 (logged in log.md).
- Page wired to issues; comparison CauseTable section removed (its "no ticket of its own" became false).
- Build: SvelteKit 3.1 / Svelte 5.57 / mdsvex 0.12.8 / Vite 8 — config lives in vite.config.js (Kit 3 rejects svelte.config.js); `npm run build` in support-kb/ → build/ (ignored).
- "Page as the desk will see it": src/routes/kb/incidents/4471-split/rendered.html (CSS inlined, no JS, via scripts/standalone.py) + rendered.png (headless Chrome).
- KbIndex lists the new page. Root .gitignore now hides s01e03 log/media/bodies/out/zip.
- NEXT: human commits + pushes → claim-challenge (answer shape unknown; no receipts held — call and follow the reply) → debrief.
- Watch: "the desk keeps working" — re-download export + check issues for comments before claiming.

## Claim 1 — rejected
- desk: "Right problems. The desk counts with its own view, as it was exported." → problems right, counts wrong.
- Desk's own view = CauseTable as exported: parser 379 (incl. the 5 one-day, "counted where they're filed, footnoted under it" per causes.ts readAs), hint 33, one-day 5 footnoted. Our #1 said 374.
- Plan: #1 → 379 (title+body), #3 body notes the 5 are also counted in #1; page ProblemTable counts the desk's way; re-push; re-claim.
