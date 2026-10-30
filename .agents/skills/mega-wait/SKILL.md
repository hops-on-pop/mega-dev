---
name: mega-wait
description: Wait for an outside event in a MEGA.dev Challenge, such as a reviewer's look, a course reply or a scheduled change, with bounded checks instead of stopping until the operator's next prompt. Use it when a course reply says "not solved yet" and someone else acts next, or when a step waits on another party.
---

# Waiting on the course

A `progress` reply means the course has your answer and someone else acts next.
Your job while waiting is to keep the submitted state unchanged, check back
on a fixed schedule, and report.

## Before you start waiting

1. **Hold the state.** Find every issue, file and public link that the wait
   depends on, using the reply, the task and the challenge title. Don't close,
   clean up or change them. "Link sent" is not "reviewed".
2. **Write the wait into the handoff.** Under `Waiting on`, record who you're
   waiting on, the signal that ends the wait, and what stays open.
3. **Choose the check.** In S01E04, `resume-challenge` returned nothing while the
   review was pending. Sending `claim-challenge` again with the same answer returned
   the review state, and the course says to send the same answer every time.
   Use a claim as the check unless the course gives another signal.
4. **Get one yes for the plan.** Each check sends a claim, so tell the operator
   the interval, the maximum number of checks and the stop rules before you start.

## Waiting

Pick the timer by the harness and the expected delay:

- **Claude Code, up to about 10 minutes:** start a background timer with the
  Bash tool (`run_in_background: true`, command `sleep <seconds>`). In T3, call
  `t3_background_wait` with its task ID. The harness wakes you when it exits,
  and the operator can still interrupt.
- **Any harness in T3 (Codex included), or a longer or unknown delay:** use
  T3 `schedule_task` with `{type: "interval", everyMs: ...}` and
  `bindToCurrentThread: true`. Its prompt runs one check and stops the
  schedule when a stop rule fires. Delete the schedule with
  `delete_scheduled_task` once the wait ends.
- **Claude Code without T3:** ask the operator to run `/loop <interval> <check prompt>`.
- **No timer available:** say so. Give the operator the time to check back,
  and stop. Don't loop or poll in the foreground.

Defaults: start at the delay the course names ("a few minutes" means 5), then
every 5–10 minutes, at most 6 checks.

## Each check

1. Confirm the held state is unchanged: the issues are still open, the link is live
   and nothing has been cleaned up early. If something changed, stop and report.
2. Send the same answer and receipts as before. Log the exact reply in the
   challenge's ignored attempt log.
3. Stop when any of these happens:
   - The reply's `message` changes, or it gives a new instruction. Act on it
     in the order the course gives, asking the operator first where the
     challenge says to.
   - The status is anything other than `progress`, such as `rejected` or `solved`.
   - You reach the maximum number of checks. Report that, and ask whether to
     keep waiting.
   - The operator interrupts.
4. Never treat `progress` as the solve. Only `solved` counts.

## Report

After each check, send one line: the check number, the course's `message`, and
whether the wait continues. When the wait ends, update the handoff's `Waiting on`
and next action, and remove any schedule you created.
