# S01E04 — review and execution plan

Reviewed 2026-10-30. Phases 1–4 are done: the repo is created, issues #1–#7 are filed, and #1–#5 are built
and closed. Current state and next steps are in [HANDOFF.md](HANDOFF.md), which takes precedence over
the planning-time notes below. The student accepted [SAFEGUARDS.md](SAFEGUARDS.md) and retains commits and pushes.
Those safeguards apply to every phase and worker. This document grants no external
write permission. Nothing has been deployed and no claim has been made.

## Account decision before execution

The [complete challenge page](https://hq.mega.dev/challenges/before-i-looked)
explicitly says: “Use a personal GitHub account for the course, never your work account.”
The student has one account used for both. This conflicts with the course guidance
and was discussed with the student. The student chose to proceed with safeguards
and paced automation, then authorized the named repository. A new repository and manual pushes do not isolate employer
access from an account suspension. Do not create another account without permission.

The account decision is recorded; do not ask for it again. Future external actions
still require their own scoped authorization.

The course describes problems with fresh accounts, VPNs and bursts of writes.
Treat these as course observations, not guaranteed thresholds. Use finite, reviewed,
serial writes from the student's normal environment. Stop on any platform warning;
never evade restrictions. No promise of zero account risk is possible.

## Sources reviewed

- Repository [AGENTS.md](../../AGENTS.md), [challenge rules](../AGENTS.md),
  [handoff template](../HANDOFF-TEMPLATE.md), and S01E03
  [lessons](../LESSONS.md) and [handoff](../s01e03/HANDOFF.md).
  No additional AGENTS.md files were found under earlier challenges.
- Course `list-challenges` and `start-challenge`, UUID
  `c0000000-0000-4000-8000-0000005e01e4`.
- Full signed-in challenge page, including the GitHub warning, completion rule,
  prompt, and lower sections. There were no collapsed `details` sections.
- [Template](https://github.com/MEGA-DOT-DEV/rig-handover): root AGENTS.md,
  plan.md, plan-to-issues SKILL.md, vision, styleguide, ADRs 0001–0004,
  both completed plans, package scripts, configuration, source and existing tests.
  API tree identifier observed: `7213e1391dd22e5b4cabc4734ae821d909a81d32`.
  This is a tree identifier, not a verified commit SHA. Recheck the template revision
  when creating the actual repository.
- Read-only template snapshot and complete page text are in ignored `private/`.
  Recover them from the links above; never treat the snapshot as a current update check.

This file is the course execution plan. It must not replace the template's root
`plan.md`, which specifies the morning-digest feature and later moves to its archive.

## Requirements and verification

| Requirement | Source | Deliverable and verification |
| --- | --- | --- |
| New public repo from template | Start brief, repo | Approved personal destination; inspect origin, visibility and template contents. Do not reuse mega-dev or an employer repo. |
| Run the shared plan-to-issues skill | Template AGENTS, skill | Use the repository's `.agents/skills/plan-to-issues/SKILL.md`; link/configure it if necessary, do not duplicate it. Record invocation. |
| Human approves split and issue contents | Brief, skill steps 3–4 | Present the table below and exact proposed fields before publication. |
| Source and label on every issue | Brief, issues | Body starts `Source: plan.md § <n>`; label `plan:morning-digest`; verify published bodies and labels. |
| Reader contract first | Template plan §1 | `src/digest/types.ts` contains DigestRow and readNight signature; student commits this before section 2 starts. |
| Reader and page behavior | Template plan §§1–2 | Tests and rendered artifact checks listed below. |
| Worker provenance | Template AGENTS | One issue per worker, separate branch/worktree, actual harness/model/effort in exact closing format. |
| Public static preview | Plan §3, ADRs 0001/0003 | One command-generated HTML file, sample data and lane banner, public HTTPS hostname, replaceable at same URL. |
| Issued marker | Brief, proofs/laneMarkerUse | Exact issued `laneMarker` becomes `.env` key `LANE_MARKER`; verify it in initial HTML. Never substitute a name or test marker. |
| Review before cleanup | ADR 0003, plan §4 | Preserve evidence review is in before removing marker; merely sending a link is insufficient. |
| Cleanup and archive | Plan §4 | Regenerate with marker unset; same URL says `no marker set`; archive feature plan with real issue list. |
| Submission | Brief, submit | `claim-challenge` answer has `repo` (owner/name or GitHub URL) and `preview` (public HTTPS URL); keep the same answer across calls. |
| Completion | Page and tool instructions | Only explicit course acceptance means solved; then save debrief. |

Only `laneMarker` was issued in the start reply; no ticket or receipt was issued.
Its value must stay out of tracked planning notes. The initial preview is its
explicitly authorized destination once publication is approved. Preserve the value
privately; if lost, recover the original start reply or use the repeat start call,
checking what the course returns. Pass future receipts under their issued names.

## Proposed issue split — awaiting human approval

These are draft identifiers, not GitHub issue numbers. Publish in dependency order
and record real URLs from tool responses. Do not manufacture issue numbers.

| Draft | Title / section | Scope | Done when | Blocked by |
| --- | --- | --- | --- | --- |
| A | Run log reader / §1 | Shared types first, then aggregate JSONL by job, retaining null owners and counting malformed lines | Fixture 2026-10-28 yields 5 jobs and 1 bad line; reader tests pass | None |
| B | Digest HTML page / §2a | GET /digest/:night; sorted table; mark retries ≥3 and failures; missing/empty states | /digest/2026-10-28 renders locally | A contract committed; complete reader for final integration |
| C | Digest JSON endpoint / §2b | GET /api/digest/:night using shared reader and sort | Same jobs in same order as HTML | A contract committed; complete reader for final integration |
| D | Status board digest links / §2c | Link each fixture night with ok/retry/fail counts | Both nights link to working digests | A contract committed; B for final verification |
| E | Digest route tests / §2d | Temp fixtures; 200, missing 404, empty, malformed line; HTML/JSON parity | pnpm test passes with new cases | A contract committed; B/C for passing integration |
| F | Public preview and review submission / §3 | Save sample digest HTML with banner by command; publish approved host; submit repo and URL | Link and issue references sent through documented reviewer route | A–E integrated and verified; publication approval |
| G | Preview cleanup and plan archive / §4 | Remove marker at same URL; archive template plan and issue list | Live URL has no marker; archive reflects actual issues | Review received; separate replacement approval |

Proposed fields in every issue: exact Source line, scope, Done when, Blocked by,
verification steps, relevant safeguards, and worker ownership. Use the required
plan label. The student must decide whether these fields are sufficient or add others.
The skill says “Publish nothing until they approve it.” The draft is not approval.

Closing comment, exactly three lines:

```text
done: <what changed, one line>
worker: <harness> · <model> · <effort>
commit: <sha or "none">
```

Close only when the issue's condition actually holds. Prefer verified student commit
SHAs when available; never invent them. Template commit conventions must not trigger
premature auto-closure: the student should use `closes #n` only after verification.
GitHub issues are the default. ADR 0004 permits files only when issues cannot be
created through any available route; it is not a general workaround for account risk.
Never maintain both trackers for this plan.

## Execution phases and approval boundaries

1. **Resolve account and destination.** Confirm repo owner/name and an existing host
   that supports replacing a single HTML file. Prepare the exact creation action,
   public visibility and deletion consequences before asking approval. Public copies
   cannot be recalled. No new account, permissions or paid service without approval.
2. **Prepare repository and skill.** After approval, create from the template and
   inspect the resulting revision. Read its current rules again. Make safeguards
   available to every worker. Keep the shared skill as the single source; inspect any
   proposed link/config change first. Ask before installing dependencies or software.
3. **Approve and publish issues.** Present exact bodies and obtain the student's
   issue-field decision. Request a named, bounded set of issue/label changes in this
   repo. Publish serially; stop on errors, warnings or rate limits. No extra mentions,
   notification spam, speculative issues or retry loops.
4. **Implement through workers.** Assign A to a strong logic model. Deliver its types
   first for the student's commit, then let B–E work against that contract. The template
   requests separate workers and cheaper models for smaller parts. Select available
   models explicitly; do not invent provider availability. Use separate branches or
   properly provisioned worktrees and limit concurrency to available slots. Queue work
   if four workers cannot run together. No workers are started during this review.
   Workers cannot commit, push, publish, close issues or access employer resources.
   Coordinate shared app.tsx edits during integration to avoid overwritten routes.
5. **Verify and prepare publication.** Run approved dependencies, tests and typecheck.
   Inspect rendered output, source and fixture results together. Student commits and
   pushes; verify the remote SHA and artifacts before submitting. Prepare the exact
   HTML and destination before requesting publication approval.
6. **Publish and request review.** Publish only the reviewed sample HTML with issued
   marker. Confirm the URL is public HTTPS and returns the expected artifact. Submit
   the same repo/preview answer. Follow the actual course response for reviewer state;
   do not invent polling, watchers, email or GitHub comment mechanisms.
7. **Clean up after review.** Once review is confirmed, prepare a replacement with
   LANE_MARKER truly unset, including in .env. Ask separately to overwrite the same
   public URL. Verify the live response and cache behavior, close G only when its
   condition holds, and archive the plan with its issue list. Student commits/pushes.
8. **Claim and debrief.** Recheck current course updates, remote source, issues and
   live preview. Submit only when the course's next step permits it. Explicit solve
   is required; save the debrief and retire pending work after acceptance.

## Implementation checks and open questions

- Strict TypeScript, Hono server-rendered JSX, one inline stylesheet, no client JS.
  No new scheduler, database, notifications, authentication or multi-night history.
- Keep `runs/` unchanged. Use temporary directories for tests. Preserve original
  timestamp offsets for display and render null owners as `—`.
- Test one row per job, retries, last status/error, first/last time, malformed input,
  missing file, empty file, and consistent ordering between HTML and JSON.
  Board counts (approved by the student 2026-10-30, written into issue #4): count jobs, derived
  from the reader's DigestRows: fail = last status `fail`; retry = retries > 0 and
  last status not `fail`; ok = the rest. 2026-10-28 → 2 ok / 2 retry / 1 fail;
  2026-10-27 → 4 / 0 / 0. Alternative: raw line counts (2026-10-28 → 10 / 4 / 1).
  State the chosen definition in issue D. Also clarify handling
  of changing owners, nonchronological events and invalid-but-parseable JSON if the
  fixtures or implementation require those decisions.
- Validate night names at the route boundary; do not allow paths outside runsDir.
- `src/server.ts` passes no explicit hostname to `serve`. The plan claims localhost
  only, but that claim is not established by this code. Verify/bind loopback before
  running a marker-bearing service. Use a static export for public hosting.
- Package scripts contain no project lifecycle install hooks, and the inspected tree
  has no GitHub Actions workflows. This does not audit transitive dependencies.
  `pnpm-workspace.yaml` allows esbuild builds; no lockfile was present. Review resolved
  dependencies and build permissions before an approved installation.
- The template ignores `.env` and PNGs, but does not generally ignore HTML previews.
  Add a dedicated ignored export folder before generating previews. Never commit
  previews, secrets, course logs or marker-bearing screenshots; never attach them
  to issues/chat. Publish only to the approved replaceable host.
- Render all fixtures and inspect HTML escaping, warning marks, missing-owner text,
  dates and banner. Tests use a dummy marker; publication uses the issued marker.
- Decided 2026-10-30 (see HANDOFF.md): standardized issue fields with heading-number
  Source lines, harness creates the label, workers on Codex `gpt-6-luna`, and review
  state followed through course MCP replies. Host is Cloudflare. Use one replaceable
  URL. A Pages deployment also stays live at its own hash URL, so delete the
  marker-bearing deployment after cleanup, or use an R2 object overwritten in place.
  Prefer a scoped API token over a broad `wrangler login` grant. Installing wrangler
  needs approval. Subsequent receipt requirements remain open.

## Lessons retained from previous challenges

Read complete original sources before acting; do not let an old handoff replace
the brief. Record every proof's name and destination. Recheck updates before issue
closure and submission. Verify that issue bodies, states, rendered HTML and remote
commits agree. Preserve source definitions instead of substituting an inferred one.

Log redacted requests and responses in ignored `private/`, with an attempt log
separate from current state. Keep HANDOFF.md current using the repository template.
Never repeat an unchanged rejected claim without new evidence or a course instruction.
After two submissions without a new diagnostic or verified state change, pause and
re-audit sources. A changed rejection is evidence, not a solve. For a course server
failure, retry at most once. Keep useful read-only investigation separate from retries.
