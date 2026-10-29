# S01E03: reconcile the two accepted tickets with verified evidence

Status: prepared for review; no GitHub changes or new submission made.
Planned at: 1e08fceeb395dbfdbc7534ae6b97a13fec14d45e, 2026-10-29.
Priority P1; effort S; risk LOW; category docs; dependencies none.

## Purpose and limits

Correct proven contradictions in the public issue bodies. This is NOT a confirmed
solution to the course rejection. Do not infer hidden acceptance requirements from
the generic rejection, or promise that adding resolution text will pass.

The challenge asks for one GitHub issue per problem with report counts, plus a
signed .svx page and its rendered counterpart in a public repository. The first
submission stage accepted the tickets after counts became parser 379, hint 33.
The export's causes.ts defines two causes; five one-day observations are included
within parser, not an additional cause or an extra count.

The human supplied the complete engineering update in this review:

> new · desk update
> engineering update
> #4471 · closed 05 oct
> parser
> fixed
> fix(dates): parse dd/mm for eu locales
> hint
> won't fix
> booking-v3 form retired

Current GitHub state was independently read on 2026-10-29:

- https://github.com/hops-on-pop/mega-dev/issues/1: closed, completed, 379 reports.
- https://github.com/hops-on-pop/mega-dev/issues/2: closed, not_planned, 33 reports.
- https://github.com/hops-on-pop/mega-dev/issues/3: open, reopened; investigation.
- Both #1 and #2 still say “so three different problems ended up in one ticket.”
- Neither #1 nor #2 body records the engineering outcome. The revised KB page does.

The existing source page and rendered.html at
challenges/s01e03/support-kb/src/routes/kb/incidents/4471-split/ already report the
two outcomes, the two counts, and desk ref DR-6JF1-H7XV. No rebuild is needed for
the proposed issue-body changes.

## Exact proposed changes

In both issue bodies, replace ONLY:

    so three different problems ended up in one ticket.

with:

    so two classified causes ended up in one ticket. The five one-day observations are included in the parser count; they do not establish a third cause.

In issue #1, replace ONLY:

    which also have their own ticket, #3.

with:

    tracked as an unresolved observation in investigation #3.

Append this section to issue #1:

```markdown
## Engineering outcome

The [challenge's engineering update](https://hq.mega.dev/challenges/what-it-shows) records #4471 closed on 5 October: parser **fixed**, `fix(dates): parse dd/mm for eu locales`. This ticket is closed as completed to reflect that outcome. The five one-day observations remain included in the exported count; their individual resolution has not been verified in investigation #3.
```

Append this section to issue #2:

```markdown
## Engineering outcome

The [challenge's engineering update](https://hq.mega.dev/challenges/what-it-shows) records #4471 closed on 5 October: hint **won't fix**, because booking-v3 was retired. This ticket is closed as not planned to reflect retirement of the affected form, rather than a fix to its hint. The suggested fix above describes the earlier proposal, not work engineering reports as completed.
```

## Execution and verification

1. Obtain approval for these exact public edits in hops-on-pop/mega-dev and, if
   desired, one subsequent course submission. Explain that body edits can be
   undone by restoring the saved originals. Do not treat review approval as
   unlimited permission for further experiments.
2. Read `gh issue edit --help`. Read issues #1–#3 with
   `gh api 'repos/hops-on-pop/mega-dev/issues?state=all'`. Save original bodies to
   temporary files. Stop if states, counts, or quoted text have drifted.
3. Construct new bodies from those originals using only the replacements and
   appended sections above. Preserve titles, report IDs, counts, and other text.
   Use `gh issue edit N -R hops-on-pop/mega-dev --body-file PATH` for #1 and #2.
4. Independently GET each issue. Assert body equality with its prepared file;
   #1 remains closed/completed and #2 closed/not_planned. Assert #3 is unchanged.
   No application tests or build are needed for issue-body prose.
5. If submission was approved, submit the same repository URL once through the
   course tool. Read its presentation instructions. Record the exact response;
   only an explicit solve establishes acceptance. On another rejection, stop
   mutations and report that this consistency correction was insufficient.

## Boundaries

- Do not change counts, titles, closure reasons, #3, classification code, signed
  page, rendered output, or decision records as part of this correction.
- Do not commit or push. The user reserves commits and pushes.
- Do not create closure comments as an assumed requirement; none is stated.
- Do not re-download an unchanged archive or wait for hypothetical GitHub bots.
- Preserve the pre-existing uncommitted HANDOFF.md change.

## Done criteria and maintenance

Both issue bodies match the reviewed replacements; state and counts remain as
listed; no other public object changes; any submission result is recorded without
claiming success on a rejection. Future agents should use this current evidence
instead of the stale opening Facts and NEXT items in HANDOFF.md. That file's
history includes superseded counts, unsupported timezone attribution, and failed
closure experiments. A future handoff rewrite should separate current verified
facts from history; it is outside this narrowly scoped public correction.
