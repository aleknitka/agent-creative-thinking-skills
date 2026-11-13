# Contributing

## Branching regime (trunk-based, fix-forward)

```
master (protected) ← dev ← feat/* | fix/* | docs/* | chore/*
        ↑                        ↖ hotfix/* (off master, then back-merge to dev)
```

| Branch | From | PR to | Purpose |
|---|---|---|---|
| `master` | — | — | Production. No direct push, no force-push. Tag releases here (e.g. `0.9.0`). |
| `dev` | `master` | `master` | Integration. All feature/fix branches merge here first. |
| `feat/*` | `dev` | `dev` | New skills, helpers, workspace, film. Example: `feat/film-36s` |
| `fix/*` | `dev` | `dev` | Bugfixes. Example: `fix/validate` |
| `hotfix/*` | `master` | `master` (+ back-merge `dev`) | Urgent prod fix. Example: `hotfix/0.8.1-router` |
| `docs/*` | `dev` | `dev` | README, provenance, docs. |
| `chore/*` | `dev` | `dev` | CI, deps, tooling. |
| `aleknitka/*` | — | — | Legacy/exempt (e.g. `aleknitka/lionfish` worktree). |

Fix-forward: never force-push `master`; roll forward with a new `fix/*`.

## Protections (enforced via API, not UI-only)

- **`master` + `dev`** — `deletion` + `non_fast_forward` blocked, `creation` blocked, `update` blocked (no direct push), `pull_request` required (0 approvals solo, dismiss stale, threads resolved, squash/rebase merge only), `required_status_checks: validate, check` must pass.
- **Branch naming** — PR check `branch-naming.yml` rejects heads not matching `^(feat|fix|hotfix|docs|chore)/.+` (plus `master`/`dev`/`aleknitka/*` exempt). `branch_name_pattern` push ruleset is Enterprise-only on GitHub so we enforce via Actions.
- **Repo settings** — squash + rebase allowed, merge-commit off, auto-merge on, delete branch on merge.

## Daily flow

```bash
git checkout dev && git pull
git checkout -b feat/my-feature
# ...work, commit...
git push -u origin feat/my-feature
gh pr create --base dev --fill    # branch-naming + validate run here
# after merge, to release:
gh pr create --base master --head dev --title "Release 0.9.0" --fill
git tag 0.9.0 && git push origin 0.9.0
```

## Local guard (optional)

```bash
ln -sf ../../scripts/git-pre-push-hook.sh .git/hooks/pre-push  # if added
```

## Skills

Follow `CLAUDE.md` progressive disclosure: `SKILL.md` lean → `references/` → `scripts/*.py`. Run `python scripts/validate.py` before PR.
