# S01E03 "what it shows" — handoff

## CURRENT STATE — 2026-10-29, supersedes historical NEXT entries below

**SOLVED** at 2026-10-29T23:51:31Z. Accepted commit: 056062bdf8ddb583ceccccc767ce6515b9c5fc75. Remote source, rendered HTML and PNG matched verified local artifacts byte-for-byte. Debrief saved: https://hq.mega.dev/challenges/what-it-shows#debrief. No remaining challenge work; do not follow historical NEXT instructions.

- Issues #1 and #2 now describe two classified causes and record the exact engineering outcomes. Verified by independent GET: #1 closed/completed (379), #2 closed/not_planned (33); #3 unchanged, open investigation.
- Resubmission advanced to a DIFFERENT rejection: no .svx carries the course-issued signature. The course explicitly requires the `ticket` from start-challenge as frontmatter `signature:`, not the author's name.
- Called start-challenge again to recover that ticket. Its `proofs` and `ticketUse` fields explicitly specify this requirement. Prior handoffs omitted it. Do not use the historical human-name signature or its desk ref.
- Corrected +page.svx locally with the exact issued ticket and rebuilt; regenerated rendered.html and rendered.png. The rendered stamp was checked against the signature algorithm and counts remain 379 / 33 / 412.
- Human pushed the corrected artifacts; resubmission returned `solved`. Acceptance is verified. Issue #3 remains open; it did not prevent acceptance.
- User authorized GitHub work; no agent commit was authorized. Do not commit automatically. This progress is evidence of a new validation stage, not proof of which individual issue-body edit mattered.

Challenge uuid: c0000000-0000-4000-8000-0000005e01e3 · page: https://hq.mega.dev/challenges/what-it-shows
Exact page text: see log.md (first entry). Every request/reply is logged there.

## Status
- [x] Brief shown to human; human re-authed gh (hops-on-pop, scopes repo) and committed earlier work.
- [x] Opened Challenge page in signed-in preview browser; recorded rules in log.md.
- [x] Human downloaded kb-export-267efc5e.zip into s01e03/ (sha256 starts 267efc5e — matches name).
- [x] Unpacked to media/support-kb/ (pristine; untrusted, run nothing from it).
- [x] Analysis: scripts/analyze.py, scripts/flips.py, scripts/counts.py → out/unique.json, out/counts.json.
- [x] Human approved repo and issue work.
- [x] Signed .svx and rendered page published with the course-issued signature.
- [x] Repository submitted, solve accepted, debrief saved.

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

## Claim 2 — progress (tickets accepted), 2026-10-29
- Issues edited: #1 → 379 (title+body, bodies/issue-parser.v2.*), #3 body notes overlap (bodies/issue-one-day.v2.md). Human pushed 18c2fbc (page shows parser 379, one-day 5 "also in parser").
- message: "Step one passed: the course accepted your tickets. Not solved yet. When the work on #4471 is done, close your tickets, then send the repo again."
- desk: "Two tickets, both real. The desk isn't done with #4471 yet. When it is, close yours and submit again."  (note: we filed THREE; "two" unexplained)
- resume-challenge → "That challenge has nothing to pick back up."
- Signal for "desk done" unknown. Checked: Challenge page unchanged, export still kb-export-267efc5e.zip (public URL, no auth; page itself needs sign-in), issues have no comments.
- NEXT: watch for the desk finishing #4471 (new export name on the page / changed 4471 page / issue comments) → close #1–#3 (gh issue close --reason, read --help) → claim again → debrief. Also: save the gh routine as a skill (check-lane "keep").
- Skill saved: ~/.claude/skills/gh-issues/SKILL.md (create/edit/close/inspect issues; ask before every change).
- check-lane hint for code "progress" → "unknown-code" (no hint).
- Theory (human): the desk will post on our open issues (anyone can comment on a public repo). Watcher: scripts/watch-issues.sh → out/watch.log, polls #1–#3 every 2 min for any non-hops-on-pop event/state/label/comment change; started 2026-10-29T22:40Z, max 2h.
- Human: wait to close issues until the desk says #4471 is done.

## 2026-10-29 follow-up — closure rejected
- Unchanged resubmission: rejected; course explicitly requested closing tickets then submitting again. This supersedes the unsupported waiting plan above.
- Human approved closing #1–#3 and resubmitting. Closed all three with reason completed; verified CLOSED through GitHub. No commits or pushes.
- Resubmission rejected: "Not accepted: your tickets are closed, but not the way the course expects. Check them against the task, then send the repo again."
- Desk hint: "Closed, but not the way the desk would. Things moved since your first submit."
- Checked timelines: only hops-on-pop edits/cross-references/closures, no desk comments. Re-downloaded original export: SHA256 still 267efc5ea61aca6efaaca842160ac4d0377d56bcbf5123e61c604d6ae99597f2.
- Closure reason or supporting closure information remains unresolved. Do not assume all problems were fixed or blindly cycle closure reasons. Need current desk evidence; original export only records queued work.
- check-lane hint for rejected returned unknown-code. Challenge remains unsolved; no debrief yet.

## 2026-10-29 — missing engineering update found
- Read the full signed-in Challenge page, including below the prompt. It has a NEW · DESK UPDATE / engineering update section.
- Exact update: #4471 · closed 05 oct; parser FIXED — fix(dates): parse dd/mm for eu locales; hint WON’T FIX — booking-v3 form retired.
- This resolves the missing source: the original export need not change. Earlier page text reads truncated at 2500 characters missed the lower section.
- Correct closure mapping: #1 parser completed; #2 hint not planned. #2 is currently incorrectly completed. No GitHub mutations made during this evaluation.
- #3 one-day is not addressed by this update; do not claim it was fixed based on this evidence.
- Next concrete action: correct #2 closure reason to not planned and resubmit. Keep page claims consistent with the engineering update; human retains commits/pushes.

## 2026-10-29 — hint closure corrected, still rejected
- Human approved changing #2 to not planned and resubmitting. GitHub PATCH confirmed state closed / state_reason not_planned.
- Claim returned the same rejection: "Not accepted: your tickets are closed, but not the way the course expects. Check them against the task, then send the repo again." Desk: "Closed, but not the way the desk would. Things moved since your first submit."
- Subsequent independent GET of all issues confirmed #1 completed, #2 not_planned, #3 completed. Correction persisted; do not repeat it.
- Remaining discrepancies: #3 has no demonstrated fix in the desk update; signed page still says parser fix queued and the other two stay open until fixed. Course rejection does not identify which remaining detail it checks. No further GitHub changes, commits, or pushes.

## 2026-10-29 — page reconciled; investigation reopened
- User approved page reconciliation and reopening #3. #3 is verified OPEN; revised title/body describe unresolved one-day symptoms, with no claim of a confirmed cause or fix.
- problems.ts now returns two cause groups and separate observations. ProblemTable shows 379 + 33 = 412, with five one-day reports footnoted within parser rather than counted again.
- Signed page records 5 October engineering outcomes: parser fixed, hint won't fix because booking-v3 retired. Investigation #3 remains open.
- Regenerated rendered.html and rendered.png. npm run build passed; rendered counts/signature checked; screenshot visually inspected and literal Markdown link corrected.
- NEXT: human reviews, commits and pushes local changes, then resubmit. No commit or push by agent. Course acceptance is still unverified; reopening #3 may affect its all-tickets-closed check.

## 2026-10-29 — reconciled page pushed and submitted
- Verified local HEAD and GitHub main both 1e08fceeb395dbfdbc7534ae6b97a13fec14d45e; working tree was clean before this handoff entry.
- Submitted unchanged answer {repo: https://github.com/hops-on-pop/mega-dev}.
- Still rejected: "Not accepted: your tickets are closed, but not the way the course expects. Check them against the task, then send the repo again." Desk: "Closed, but not the way the desk would. Things moved since your first submit."
- #3 is OPEN, so the response's "tickets are closed" appears to refer to the two classified tickets, or is generic. It does not establish that #3 must close.
- Do not repeat speculation as a confirmed diagnosis. #1 completed and #2 not_planned match the visible engineering outcomes, but the remaining acceptance requirement is unidentified.
