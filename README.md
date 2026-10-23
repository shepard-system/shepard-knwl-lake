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
```

One rigid structure for every lake. Core Obsidian only — no community plugins.

## Start a New Lake

```bash
git clone https://github.com/shepard-system/shepard-knwl-lake.git lake-prog
cd lake-prog
rm -rf .git 20_Statute/rules/* 20_Statute/policies/*   # inherited rules stay in the main lake
git init
```

Edit `lake.yaml`:

```yaml
id: prog
name: Programming & Sciences
role: member
extends: https://github.com/shepard-system/shepard-knwl-lake
template_version: 0.1.0
domains:
  PY: Python
```

Push to your **private** repository, open the folder as an Obsidian vault, start at `HOME.md`.

For a company, fork this repository as your own main lake (`role: main`) and point team lakes at it.

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
Agents write only to `01_Inbox/agents/`; everything else goes through a pull request.

## License

MIT
