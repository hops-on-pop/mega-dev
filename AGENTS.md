# Repository instructions

- Never commit to git unless explicitly instructed by the user.
- For work under `challenges/`, read `challenges/AGENTS.md` before taking action.

## Nested repositories

- Nested repositories have their own Git history, remotes and ignore rules.
  Check the parent `.gitignore` and the project's current handoff or workspace
  settings to locate them; do not assume a fixed directory layout.
- Record each project's verified repository location and remote URL in its
  `HANDOFF.md` or equivalent project notes. Keep machine-specific absolute paths
  in ignored local notes or local workspace settings, not in this guidance.
  Update those records when a repository moves.
- Before changing files or Git state, check the working directory, then use
  `git rev-parse --show-toplevel`, `git remote -v` and `git status --short` to
  verify the target against the project notes. Do not rely on a previous `cd`
  or `pwd` alone. Stop on a mismatch and repeat these checks before any
  authorized commit or push.
- Read the child's `AGENTS.md` and any applicable directory instructions before
  working there. Carry the user's safeguards and authorization limits into worker
  briefs; a child repository's instructions do not grant permission to commit,
  push or publish. The user currently manages challenge commits and pushes.
- Parent ignore rules do not protect files from commits inside a child repository.
  Check the child's exclusions for secrets, environment files and generated output.
- Ignore rules do not untrack existing files. If a nested repository was previously
  tracked by the parent, inspect the parent index and discuss cleanup before
  removing entries. Do not accidentally stage a child as an embedded repository
  or configure a submodule without an explicit request.
- After moving a repository, check scripts, workspace settings, symlinks and notes
  for stale paths. A `.git` file can refer to location-dependent worktree or
  submodule metadata; verify it before assuming the move preserved Git operations.
