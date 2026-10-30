# Working on course challenges

These rules put the lessons in [LESSONS.md](LESSONS.md) into practice.
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
6. Treat the challenge title and description as requirements. Note any phrase that
   names a wait, an order or a trap in the handoff checklist.
7. During planning, check that each tool and host is current, and ask the course
   what the lane supports with `check-lane` (needs such as `gh`, `upload-cli`,
   `skill-wiring` and `browser`). Change course before building, not at publish time.
8. If the live page needs a sign-in you can't get, use the latest course tool reply
   as current. Record in the handoff that the page wasn't re-read.

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

## Steps that wait on someone else

- A step that waits on another party, such as a reviewer or the course, stays open
  until a course reply confirms it. "Link sent" is not "reviewed". Don't close
  that issue, clean up after it or start dependent steps before confirmation.
- In the handoff, record each wait: who you're waiting on, the signal that ends the
  wait, and which issues stay open meanwhile.
- Wait with the `mega-wait` skill (`.agents/skills/mega-wait/`), not by stopping
  until the user's next prompt. Never treat a `progress` reply as the solve.

## Skills and workers

- Shared skills for this repo live in `.agents/skills/<name>/SKILL.md`, the folder
  Codex reads. `.claude/skills/<name>` is a relative symlink to it, so Claude Code
  sees the same file. Never copy a skill into both folders.
- Codex looks for `.agents/skills` only from its working directory up to the repo
  root. A worker that starts inside a nested challenge repo therefore doesn't see
  this repo's skills. Name the skill's absolute path in the worker brief instead.
- Hybrid workers (decided by the user 2026-10-30): the coordinating thread stays
  in the mega-dev project for context. With the user's yes for each challenge,
  register the challenge repo as its own T3 project. Then launch worker threads
  there, each in its own worktree, so issues can run in parallel. Brief workers
  with absolute paths to the parent notes they need, and carry the user's limits
  into each brief: no commits, pushes or publishing.

## Record conventions where they are graded

- When the user decides a convention for the repo the course reviews, such as the
  fields every issue must carry, write it into that repo's `AGENTS.md`, skill or
  ADR, ready for the user to commit. Local notes aren't part of the repo.

5. Preserve the user's existing authorization and constraints. Do not repeatedly
   ask for permission already granted. Never commit without explicit instruction.
6. Treat the challenge title and description as requirements. Note any phrase that
   names a wait, an order or a trap in the handoff checklist.
7. During planning, check that each tool and host is current, and ask the course
   what the lane supports with `check-lane` (needs such as `gh`, `upload-cli`,
   `skill-wiring` and `browser`). Change course before building, not at publish time.
8. If the live page needs a sign-in you can't get, use the latest course tool reply
   as current. Record in the handoff that the page wasn't re-read.


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
- Every remaining step that closes, cleans up or can't be undone cites the course
  text that requires it, or is marked as a guess. A later agent will follow a
  written step with confidence it hasn't earned.
- Keep history in a separate attempt log. Do not accumulate contradictory Facts
  and NEXT sections in the current handoff.
- Store complete redacted instructions and attempt records in the challenge's
  ignored `private/` folder. Tracked notes must still explain what is required and
  how another machine can recover missing evidence; do not rely on local files alone.
- Record failed hypotheses so the next agent does not repeat them. Mark the
  challenge solved and retire pending actions after acceptance; save its debrief.
