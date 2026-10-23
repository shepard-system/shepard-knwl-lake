---
id: NOTE-CORE-008
tags: [type/convention]
status: active
created: 2026-01-22
updated: 2026-10-23
---

# Structure & Domains

One rigid structure for every lake. Adding a top-level folder requires an Architect decision recorded in an ADR.

## Folders

| Range | Purpose | Folder |
|-------|---------|--------|
| 00-09 | Meta | `00_Codex` (constitution), `01_Inbox` (drafts) |
| 10-19 | Understanding | `10_Context` |
| 20-29 | Law | `20_Statute` |
| 30-39 | Capabilities | `30_Skills` |
| 40-69 | Reserved | — |
| 70-79 | Cases | `70_Cases` — create on the first documented incident |
| 80-89 | Reserved (Logs, Ops) | — |
| 90-99 | Infrastructure | `90_Bases`, `99_Templates` |

```
lake.yaml
HOME.md
00_Codex/         # from template — never edit in a member lake
01_Inbox/
  shared/         # human drafts
  agents/         # agent drafts
  private/        # gitignored
10_Context/{Product}/
20_Statute/{rules,workflows,policies,checklists}/
30_Skills/agents/
90_Bases/
99_Templates/     # from template — never edit in a member lake
```

## Domain Codes

Domain codes namespace IDs (`RULE-{DOMAIN}-{NNN}`). Each lake declares its own in `lake.yaml`:

```yaml
domains:
  CORE: Framework-wide rules
  PY: Python
```

`CORE` belongs to the main lake. Members pick their own codes.

**Up:** [[Conventions]]
