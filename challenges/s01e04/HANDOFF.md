# S01E04 "before i looked" — current state

Read [SAFEGUARDS.md](SAFEGUARDS.md) and [plan.md](plan.md) before acting. Chronology is in the
ignored `private/attempt-log.md`. The template's own `plan.md` (in the repo) is the feature plan.

## Status

- Verdict: SOLVED. The course accepted claim 5 at 2026-10-30T19:29:41Z. The debrief is saved on the course page
  (https://hq.mega.dev/challenges/before-i-looked#debrief) and summarized in `private/debrief.md`.
- Final state: repo https://github.com/hops-on-pop/mega-dev-s1e4, main `0d85429` (plan archived in
  `docs/plans/done/2026-10-30-morning-digest.md`), and issues #1–#7 closed.
- The preview `https://mega-dev-s1e4-preview.hops-on-pop.workers.dev` is live with no marker
  (version `2c5a6a48-…`). Version URLs are off.
- Lesson: an issue that waits on the reviewer stays open until a course reply says they looked.
  Closing #6 once the link was sent got claim 2 rejected. History is in `private/attempt-log.md`.
- Pending actions: none for the course. Optional student cleanup:
  - revoke the Cloudflare account token (it expires 2026-11-07)
  - delete the Worker with `wrangler delete`
  - delete the public repo, which the course allows after acceptance

## Requirements and evidence

| Requirement | Source | Destination | Verification | State |
| --- | --- | --- | --- | --- |
| New public repo from template | start-challenge `repo` | hops-on-pop/mega-dev-s1e4 | `gh repo view`; contents matched template | verified |
| Plan → issues via shared skill, human-approved split and fields | brief `you`; skill steps 3–4 | #1–#7 | student approved 2026-10-30 | verified |
| Each issue opens `Source: plan.md § <n>`, label `plan:morning-digest` | start-challenge `issues` | all 7 issues | live `gh issue list` read 2026-10-30 | verified |
| Reader contract committed first | plan § 1 | `src/digest/types.ts` in 9a81363 | that commit holds types.ts alone | verified |
| §§ 1–2d built, tests green | plan §§ 1–2d | main 1e1d53d | 14 tests, tsc clean; 2026-10-28 → 5 jobs, 1 bad line; board 2/2/1 | verified |
| Closing comment format per issue | template AGENTS.md | #1–#5 | `done/worker/commit` lines present | verified |
| Public HTML preview with marker | plan § 3, ADR 0003, proofs | `https://mega-dev-s1e4-preview.hops-on-pop.workers.dev` | live fetch matches local file; banner shows marker | verified 2026-10-30 |
| Send link + issues to reviewer | plan § 3, brief `submit` | `claim-challenge` | course reply | sent 2026-10-30 (progress) |
| Marker removed at same URL after review | plan § 4, ADR 0003 | same URL | live banner reads "no marker set"; version URLs off | verified 2026-10-30 |
| Plan archived with issue list | plan § 4 | `docs/plans/done/2026-10-30-morning-digest.md` | file present on remote main | local, uncommitted |
| Solved | page, start reply | course | explicit acceptance only | missing |

- Instructions: `private/start-challenge.redacted.json` and `private/challenge-page.txt`.
  Recover them with `start-challenge` (UUID above) and the page URL. Re-read the live page before submitting.
- Issued proof: only `laneMarker`. It goes to `.env` as `LANE_MARKER` (ignored by the repo), then
  into the public preview HTML. Its value is in no file. Recover it with `start-challenge`. Never substitute a test value.
- Submission: `claim-challenge` with `{ repo: "hops-on-pop/mega-dev-s1e4", preview: "<public https URL>" }`.
  Send the same answer on every call. The course's replies vary (student confirmed).
  Expect a "review pending" stage before the cleanup (§ 4) and a second claim. Follow each reply.

## Verified facts

- Decisions (student, 2026-10-30):
  - The Source line uses the plan's heading number (§ 1, § 2a–§ 2d, § 3, § 4).
  - Board counts are jobs: fail = last status fail; retry = retries > 0 and not fail; ok = the rest.
  - Workers are Codex `gpt-6-luna`: high effort for #1, medium for #2–#5.
  - The host is Cloudflare Workers with static assets on the student's existing account. They switched from Pages
    on 2026-10-30 because Pages is being phased out. ADR 0003 needs only the same link and an upload over it.
    Workers versions can't be deleted one by one. So set `preview_urls: false`, and then old versions have no public URL.
- Commit convention: the template styleguide asks for `closes #n` in commit messages. Use it only
  after the harness has verified the work. GitHub then auto-closes the issue, and the harness posts
  the 3-line closing comment with the short SHA.
- Closing comments say `worker: Codex · gpt-6-luna · <effort>`.
- Tooling:
  - Global pnpm 9.1.0 can't read this repo. Use `npx -y pnpm@12.16.1 <cmd>`, or `./node_modules/.bin/*`.
  - `src/server.ts` binds all interfaces. A brief local run is acceptable, because the marker is going public anyway.
  - `var/` is git-ignored, so save previews to `var/preview/`.
- Workers: T3 `delegate_task` worktrees come from the parent mega-dev repo, not the nested repo.
  - Workers run one at a time in the shared checkout, each on its own branch.
  - Codex sandboxes have no network. Workers use local binaries and `node --import tsx/esm`.
  - The harness re-runs all checks before the student commits.

## Unknowns

| Question | Checked | Status |
| --- | --- | --- |
| How "review is in" arrives | course page, start reply | Through `claim-challenge` replies; exact wording unknown |
| Cloudflare inputs | none yet | need an account-scoped Workers Scripts:Edit token (via `request_secret`), account ID, workers.dev subdomain, Worker name |
| Other receipts or tickets | start reply had none | check each course reply |

## Remaining steps (#6, #7)

1. Make the preview (#6):
   1. Put the recovered marker in `sub-repos/mega-dev-s1e4/.env`, copied from `.env.example`.
      Confirm `git status` doesn't list it.
   2. Run `npx -y pnpm@12.16.1 start` briefly, then
      `curl -sf http://localhost:8787/digest/2026-10-28 -o var/preview/index.html`. Stop the server.
   3. Inspect the file: banner shows the marker, 5 rows, no `<script`, only sample data.
2. Publish (#6). This needs approval of the wrangler install via npx, the Worker name, the public
   upload and how to undo it. Use the account-scoped token from `request_secret`, not `wrangler login`. Keep the
   wrangler config outside the repo, or git-ignore it: `name`, `compatibility_date`, `assets.directory` set to `var/preview`,
   `workers_dev: true`, `preview_urls: false`, and no `main`. Run `wrangler deploy`. Fetch the workers.dev URL over HTTPS,
   compare it with the local file and record the version ID.
3. Submit: `claim-challenge` with repo + preview. Log the redacted reply in `private/`. Do NOT close #6 yet.
   Close it (commit `none`) only after a course reply shows the reviewer has looked.
4. When a reply shows the review is in (#7):
   1. Unset `LANE_MARKER` everywhere, including `.env`, then regenerate the page and confirm it says "no marker set".
   2. With approval, run `wrangler deploy` again to the same Worker, so the URL stays the same.
   3. Verify the live URL and confirm that version URLs are still off. Undo: `wrangler delete` removes the Worker.
5. Archive (#7): the student commits a move of `plan.md` to `docs/plans/done/`, with its issue list
   (#1–#7 URLs) added. Close #7 with its closing comment. Claim again with the same answer.
6. Only an explicit solve counts. Then write the debrief and retire pending actions.
