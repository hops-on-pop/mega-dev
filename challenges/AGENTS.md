# Working on course challenges

These rules capture lessons from [S01E03](s01e03/LESSONS.md).
Use [HANDOFF-TEMPLATE.md](HANDOFF-TEMPLATE.md) for each challenge's current state.

## Establish the requirements before changing anything

1. Read the original challenge tool response and the complete challenge page.
   A handoff is an index to evidence, not a substitute for those sources.
2. Record each deliverable, proof field, submission shape, and acceptance condition
   in the handoff checklist, with its source and verification method.
3. Recover missing issued proofs using the course's documented recovery method.
   Do not invent values or substitute a person's name for an issued signature.
4. Read all page sections, including updates and expanded details. If a tool
   truncates the page, retrieve the missing content before calling it unchanged.
5. Preserve the user's existing authorization and constraints. Do not repeatedly
   ask for permission already granted. Never commit without explicit instruction.

Keep credentials out of tracked notes and logs. Record proof names, their intended
destination, and how to recover them. Publish an issued proof only when the
challenge explicitly requires it in the deliverable; do not generalize that
permission to credentials or other proofs.

## Verify the actual deliverable

- When the task depends on a rendered page, build and inspect that page. Check
  its counts, classification, and signature. Separate analyses can cross-check
  the result; they must not silently replace the supplied counting rules.
- Distinguish observations from confirmed causes. Preserve the source's counting
  rules unless the task explicitly asks you to change them.
- Recheck the current update source before closing issues or claiming completion.
  An unchanged dated export does not establish that the challenge page is unchanged.
- Compare issue bodies, states, closure reasons, source files, and rendered files.
  Updating one does not update the others.
- Before submitting, verify the published artifacts, not just local files.
  Record the remote commit and exact issue state used for that attempt.

## Respond to rejection without guessing

- Record the exact verdict, the evidence behind the proposed correction, and the
  expected result. Distinguish a rejected answer from a tool or server failure.
- Change one justified hypothesis at a time. If a coherent correction requires
  several edits, say that acceptance cannot identify which individual edit mattered.
- Do not repeat an unchanged submission unless the course asks for it or verified
  external state changed. Do not cycle counts, closure reasons, or issue states.
- After two consecutive submissions without a new diagnostic or verified external
  change, pause submissions and re-audit the original requirements and full sources.
  Continue useful read-only investigation; do not make the user do available checks.
- If you cannot name an evidence-backed correction, report the exact missing
  evidence. Do not invent a polling or notification mechanism.
- A different rejection is new evidence, not proof that every earlier hypothesis
  was correct. Only an explicit solve establishes completion.

## Leave usable state for the next agent

- Rewrite the top of `HANDOFF.md` after each meaningful change. It must state the
  current verdict, verified facts with sources, unknowns, and one next action.
- Keep history in a separate attempt log. Do not accumulate contradictory Facts
  and NEXT sections in the current handoff.
- Store complete redacted instructions and attempt records in the challenge's
  ignored `private/` folder. Tracked notes must still explain what is required and
  how another machine can recover missing evidence; do not rely on local files alone.
- Record failed hypotheses so the next agent does not repeat them. Mark the
  challenge solved and retire pending actions after acceptance; save its debrief.
