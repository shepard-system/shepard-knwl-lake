---
name: new-lake
description: Create a new knowledge lake from the shepard-knwl-lake template — repository, lake.yaml, removal of inherited law, first check. Use when the user asks to start, create, or bootstrap a lake.
---

# New Lake

Every lake is its own vault and its own repository. Never create a lake inside another one.

## 1. Ask

- `id` — short, lowercase, unique across the user's lakes (`prog`, `langs`). Becomes the cross-lake prefix `prog:RULE-PY-001`.
- `name`, domain codes (`PY: Python`), owner (user or org).
- `role` — `member` (default: inherits a main lake) or `main` (a company's own root lake).

## 2. Create the repository

```bash
gh repo create <owner>/lake-<id> --private --template shepard-system/shepard-knwl-lake --clone
cd lake-<id>
```

Private by default — a lake holds personal or company knowledge. No `gh`: GitHub → **Use this template**.

## 3. Identity — `lake.yaml`

```yaml
id: prog
name: Programming & Sciences
role: member
extends: https://github.com/shepard-system/shepard-knwl-lake   # or a local path: ../shepard-knwl-lake
template_version: 0.1.0                                          # keep as cloned
domains:
  PY: Python                                                     # own codes only, never CORE
```

## 4. Remove inherited law (member only)

The main lake's Statute stays in the main lake; a copy would double it.

```bash
git rm -q 20_Statute/rules/RULE-CORE-*.md 20_Statute/policies/POLICY-*.md
touch 20_Statute/rules/.gitkeep 20_Statute/policies/.gitkeep
```

Replace the body of `CHANGELOG.md` with an empty `## Unreleased` section (keep the frontmatter).
A `main` lake keeps everything; it only changes `id`, `name` and its domains.

## 5. Make it yours

- `HOME.md` — title and one-line purpose.
- `.github/CODEOWNERS` — real owners; the Architect owns `00_Codex/`, `20_Statute/`, `99_Templates/`.
- `.ai/AGENTS.local.md` — private agent rules (identity, push policy). Gitignored.

Never edit `00_Codex/` or `99_Templates/` in a member lake — they are replaced on template sync.

## 6. Verify

```bash
python3 tools/check.py      # must print ok
git add -A && git commit -m "chore: initialize lake <id>"
```

Push only when the user asks. Then connect it: [`link-lake`](../link-lake/SKILL.md).
