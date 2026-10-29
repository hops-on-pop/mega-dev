# S01E03: why the repeated attempts failed

The course accepted commit `056062bdf8ddb583ceccccc767ce6515b9c5fc75`
on 2026-10-29. The [saved debrief](https://hq.mega.dev/challenges/what-it-shows#debrief)
records the solve. Earlier work and failures are recorded in `HANDOFF.md`.

## What went wrong

1. **The analysis replaced the supplied classification.** The first parser count
   was 374 because five one-day observations were promoted into a separate cause.
   The exported `causes.ts` and rendered table assign 379 to parser and 33 to hint.
   Those five observations are included within parser. Independent analysis did
   not justify changing the desk's counting rules.
2. **A partial page read was treated as complete.** Earlier agents read truncated
   challenge text and missed the engineering update. Repeatedly downloading an
   unchanged archive and polling GitHub comments could not establish its contents.
   The complete update said parser fixed and hint won't fix because the form retired.
3. **Artifacts disagreed.** The revised page described two causes and engineering
   outcomes, while the closed issue bodies still described three problems and no
   outcomes. Correcting both bodies changed the rejection to a signature error.
   Several text edits were submitted together, so the exact decisive edit is unknown.
4. **The handoff omitted an explicit requirement.** The original start response
   required its issued `ticket` as the page's `signature`. Agents used an author
   name instead. Recovering that response, applying the issued value, and rebuilding
   the rendered page led to acceptance after the human pushed the artifacts.

The later review also recovered the original start response too late. A review
that claims to start from the instructions must obtain those instructions first.

## What the result proves—and what it does not

- Parser 379 and hint 33 were the accepted classification and counts.
- The accepted state had parser closed/completed and hint closed/not planned,
  with engineering outcomes documented in their bodies.
- The final blocker explicitly required the course-issued signature. The corrected
  source and rendered HTML/PNG were verified against GitHub before the accepted claim.
- Investigation #3 remained open during acceptance. Closing every issue in the
  repository was not necessary for this solve.
- The result does not establish that closure comments are required, that one-day
  observations have a timezone cause, or which individual body edit passed a check.

## Preserve the method

The repeatable rules live in [the challenge agent instructions](../AGENTS.md),
and the current-state structure lives in [the handoff template](../HANDOFF-TEMPLATE.md).
Future challenges should preserve complete requirements, source coverage, proof
destinations, published-state checks, and failed hypotheses before handing off.

The build setup remains in `support-kb/`; run `npm run build` there. The standalone
HTML helper is `scripts/standalone.py`. Inspect the rendered output as well as the
source. Do not copy this challenge's issued signature into another challenge.
