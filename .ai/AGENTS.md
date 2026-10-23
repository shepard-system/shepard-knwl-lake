# Agent Instructions — Knowledge Lake

For AI coding agents (Claude Code, Codex, Gemini CLI) working in a lake repository.
`CLAUDE.md`, `AGENTS.md` and `GEMINI.md` are symlinks to this file — edit `.ai/AGENTS.md` only.
If `.ai/AGENTS.local.md` exists, read it too: private, machine-local rules that extend this file. It is gitignored — never commit it.

## What This Is

An Obsidian vault, not a code project. The only code is `tools/check.py` (stdlib linter).
Two kinds of "skills" live here — do not mix them:

- `.ai/skills/` — how **you**, a coding agent, operate this repository.
- `30_Skills/` — vault content: capabilities of the system's own agents, written from `_tpl_skill`.

## Before Any Change

1. Read `lake.yaml` — which lake this is (`id`, `role`) and what it `extends`.
2. Read `00_Codex/agent-instructions.md` and follow it. It overrides anything you assume.
3. Obey `POLICY-agent-access` (main lake `20_Statute/policies/`): write only to `01_Inbox/agents/` with `status: draft`;
   everything else goes through a branch and a pull request. Never read `01_Inbox/private/`.
4. Create documents only from `99_Templates/`; frontmatter rules are in `00_Codex/conventions/Metadata.md`.
5. Run `python3 tools/check.py` after every change; it must print `ok`.

## Skills

Read the skill before the task. Claude Code also discovers them through `.claude/skills` (symlink).

| Skill | Use when |
|-------|----------|
| [`new-lake`](skills/new-lake/SKILL.md) | Creating a lake from this template |
| [`write-note`](skills/write-note/SKILL.md) | Adding a document or filling a draft |
| [`link-lake`](skills/link-lake/SKILL.md) | Linking documents, connecting a member lake to its main lake, overriding a rule |
| [`lake-hygiene`](skills/lake-hygiene/SKILL.md) | Periodic cleanup: lint, pending drafts, stale documents, leaks |

## Git

- Conventional Commits: `feat:`, `fix:`, `docs:`, `chore:`, `ci:`.
- Never commit `01_Inbox/private/`, `*.local.md`, or secrets (`RULE-CORE-001`).
- CI runs `tools/check.py` on every push and pull request.
