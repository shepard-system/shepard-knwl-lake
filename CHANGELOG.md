---
id: NOTE-CORE-002
tags: [nav/changelog]
status: active
created: 2026-10-23
updated: 2026-10-23
---

# Changelog

All notable changes to the lake template. Format: [Keep a Changelog](https://keepachangelog.com/).

## [0.1.0] — Unreleased

### Added

- Rigid lake structure: `00_Codex`, `01_Inbox`, `10_Context`, `20_Statute`, `30_Skills`, `90_Bases`, `99_Templates`.
- `lake.yaml` — lake identity, `main`/`member` role, inheritance via `extends`, domain codes.
- Federation rules: cross-lake references (`lake:ID`), rule overrides (`overrides:`).
- Agent write policy: agents write only to `01_Inbox/agents/` (`shepard:POLICY-agent-access`).
- 13 document templates, 4 Bases views.
- `tools/check.py` — lake linter (frontmatter, unique ids, dead links).
- `.ai/` — instructions and skills for coding agents (`new-lake`, `write-note`, `link-lake`, `lake-hygiene`); private rules in gitignored `.ai/AGENTS.local.md`.
- CI: linter and private-file guard on every push and pull request; `CODEOWNERS` in `.github/`.

### Fixed

- Codex and hubs cite main-lake law by qualified id, so a member lake passes `check.py` after removing inherited rules.
