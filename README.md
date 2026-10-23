# shepard-knwl-lake

**The Pasture** — the knowledge lake of [shepard-system](https://github.com/shepard-system).

An Obsidian vault that is the single source of truth for humans and AI agents:
the rules agents obey, the skills they have, the context they need.

This repository is two things at once:

- **The template** — clone it to start a new lake with the right structure.
- **The main lake** — the Codex and global Statute every other lake inherits.

## Structure

```
lake.yaml          # lake identity: id, role (main|member), extends, domains
HOME.md            # navigation root
00_Codex/          # constitution — principles, roles, federation, conventions
01_Inbox/          # drafts: shared/ (humans), agents/ (agents), private/ (gitignored)
10_Context/        # understanding — one folder per product or domain
20_Statute/        # law — rules, workflows, policies, checklists
30_Skills/         # capabilities — skills and agent specs
90_Bases/          # Obsidian Bases views
99_Templates/      # document templates
tools/check.py     # lake linter
.ai/               # coding-agent instructions + skills (CLAUDE.md, AGENTS.md, GEMINI.md link here)
.github/           # CODEOWNERS, CI (runs the linter)
```

One rigid structure for every lake. Core Obsidian only — no community plugins.

## Start a New Lake

```bash
gh repo create <owner>/lake-prog --private --template shepard-system/shepard-knwl-lake --clone
```

Or **Use this template** on GitHub. Then set `id`, `role: member`, `extends` and your domains in `lake.yaml`,
remove the inherited `20_Statute/rules/*` and `policies/*`, and run `python3 tools/check.py`.
Full steps: [`.ai/skills/new-lake`](.ai/skills/new-lake/SKILL.md) — readable by humans and agents alike.

Open the folder as an Obsidian vault and start at `HOME.md`.
For a company, create your own main lake (`role: main`) the same way and point team lakes at it.

## How Lakes Work Together

- Each lake is its own vault and its own repo.
- A member inherits the main lake's active Statute and can override rules with `overrides: shepard:RULE-CORE-001`.
- Cross-lake references use qualified IDs: `shepard:POLICY-agent-access`.
- Search across all lakes is provided by [The Memory](https://github.com/shepard-system/shepard-mem-layer).

Details: [`00_Codex/Federation.md`](00_Codex/Federation.md).

## Check a Lake

```bash
python3 tools/check.py        # required frontmatter, unique ids, dead links; exit 1 on errors
```

Stdlib only, no dependencies.

## For AI Agents

Read [`00_Codex/agent-instructions.md`](00_Codex/agent-instructions.md) first.
`CLAUDE.md`, `AGENTS.md` and `GEMINI.md` point to [`.ai/AGENTS.md`](.ai/AGENTS.md), the entry point for coding CLIs.
Agents write only to `01_Inbox/agents/`; everything else goes through a pull request.

Skills for coding agents in [`.ai/skills/`](.ai/skills/) (Claude Code finds them via `.claude/skills`):
`new-lake`, `write-note`, `link-lake`, `lake-hygiene`.
Private, machine-local agent rules go in `.ai/AGENTS.local.md` — gitignored.

## License

MIT
