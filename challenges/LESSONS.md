# Challenge lessons

Lessons that apply to any challenge, not just the one that taught them. The rules
that put them into practice are in [AGENTS.md](AGENTS.md). Each challenge's own
history stays in its `HANDOFF.md`, ignored attempt log and course debrief.

## Requirements

1. **The handoff is an index, not a source.** Read the original tool reply and the
   whole challenge page before acting. A summary drops details, and a dropped
   detail can be the whole answer. *S01E03: the handoff left out that the issued
   ticket was the page's signature, so agents signed with a name.*
2. **A partial read is not a complete read.** Truncated pages hide updates. If a
   tool cuts a page off, get the rest before calling it unchanged. *S01E03.*
3. **Keep the supplied rules.** Your own analysis can cross-check the source's
   counting or classification rules. It must not quietly replace them. *S01E03.*
4. **Issued proofs are values.** Recover a lost proof the way the course says.
   Never substitute a name, a test value or a guess. *S01E03.*
5. **The title and description are requirements too.** Short phrases often name
   the trap. *S01E04: "before i looked" and "the reviewer gets to things when they
   get to them" described the exact mistake that was then made.*

## Waiting on someone else

6. **Sent is not received, and received is not reviewed.** When a step depends on
   another party, it stays open until that party confirms. Anything that undoes or
   cleans up after it is blocked until then. *S01E04: closing the preview issue
   once the link was sent got the claim rejected: "you closed #6 before the
   reviewer looked."*
7. **Waiting is a capability you have to set up.** If the harness can only wait
   for the operator's next prompt, every outside delay costs a round trip. Use a
   bounded wait routine, and never treat a "progress" reply as the solve.

## Plans and handoffs

8. **A step in a handoff is a hypothesis until it cites a source.** Agents follow
   written steps with confidence they haven't earned. Tie each close, cleanup or
   irreversible step to the course text that requires it, or mark it as a guess.
   *S01E04: the rejected close came from a handoff step with no source.*
9. **Check that tools and hosts are current while planning.** A host that is
   being phased out, or a capability the harness lacks, is cheap to change early
   and expensive at the publish step. Ask the course what the lane supports.
   *S01E04: the host changed from Pages to Workers at publish time.*
10. **Decisions about a graded repo belong in that repo.** When the operator
    decides a convention for the repo the course reviews, such as what every
    issue must carry, write it into that repo's instructions, skill or ADR.
    Local notes don't count as part of the repo. *S01E04.*

## Changing course after a "no"

11. **Change one thing, then resend.** A rejection that names the problem is
    evidence. Fix exactly that, and resend the same answer. Several edits at
    once hide which one mattered. *S01E03: several edits together; S01E04: one
    reopen, then accepted.*
12. **Every copy has to agree.** Source files, rendered output, issue bodies
    and issue states are separate copies. Updating one does not update the
    others. *S01E03.*
13. **Record what failed.** A failed hypothesis that isn't written down gets
    tried again by the next agent.

## Publishing

14. **Check the link the way the other side will open it.** Fetch the public
    URL over HTTPS and compare it with the local file. Check that no second
    public copy exists, such as a per-version or preview URL. *S01E04.*
15. **Public copies can't be recalled.** Approve each upload separately, and
    know the undo before you upload.

## Working with the operator

16. **Pre-approve narrow permissions for actions already approved.** Safety
    checks can block an action the operator has approved. A narrow allow rule
    (one command, one repo prefix) saves round trips without widening authority.
    *S01E04: issue close and reopen were blocked three times.*
17. **The operator owns outside actions; the harness does the rest.** Do every
    check and local step yourself. Ask only for approvals, sign-ins, commits and
    pushes, and give the exact command when you ask.
