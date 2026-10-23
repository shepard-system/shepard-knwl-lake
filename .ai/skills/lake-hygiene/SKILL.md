---
name: lake-hygiene
description: Keep a knowledge lake clean — lint, drafts waiting for review, stale documents, leaked secrets or private files, template drift. Use for periodic maintenance or when asked to clean up, audit or review a lake.
---

# Lake Hygiene

Report findings to the human. Fix only what is mechanical (dead links, missing frontmatter); never promote, demote or delete content on your own.

## 1. Lint

```bash
python3 tools/check.py
```

Fix every error: missing frontmatter, unknown status, duplicate id, dead link.

## 2. Waiting for review

```bash
grep -rl '^status: draft' --include='*.md' . | grep -v '^./99_Templates/'
```

Obsidian view: `90_Bases/pending-review.base`. List them with author and age; the Architect decides.

## 3. Stale

- Inbox notes older than 30 days: promote (move + convert to the right template) or delete — ask.
- `active` documents with `updated` older than 6 months: ask whether they still hold.
- Never delete `deprecated` documents — they are history.

## 4. Leaks

```bash
git ls-files 01_Inbox/private '*.local.md'          # must be empty
git grep -nIiE '(api[_-]?key|secret|token|passw(or)?d)[[:space:]]*[:=]|BEGIN [A-Z ]*PRIVATE KEY' # review every hit
```

A real secret: remove it, tell the human to rotate it, open a case (`RULE-CORE-001`).

## 5. Template drift (member lakes)

`00_Codex/` and `99_Templates/` must match the main lake:

```bash
diff -r ../shepard-knwl-lake/00_Codex 00_Codex && diff -r ../shepard-knwl-lake/99_Templates 99_Templates
```

A difference is either a local edit (revert it, propose the change to the main lake) or an outdated copy (sync it, bump `template_version` in `lake.yaml`).
