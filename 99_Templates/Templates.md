---
id: NOTE-CORE-019
tags: [nav/templates]
status: active
created: 2025-01-21
updated: 2026-10-23
---

# Templates

> Every document starts from a template. No freeform documents.

Setup: Settings → Core plugins → Templates → folder `99_Templates` (already in `.obsidian/templates.json`).

| Template | Use for | Location |
|----------|---------|----------|
| [[_tpl_seedling]] | New idea or note | `01_Inbox/` |
| [[_tpl_index]] | Folder hub | any folder |
| [[_tpl_product]] | Product / domain hub | `10_Context/{Product}/` |
| [[_tpl_component]] | System component | `10_Context/{Product}/components/` |
| [[_tpl_spec]] | Requirements | `10_Context/{Product}/specs/` |
| [[_tpl_adr]] | Architecture decision | `10_Context/{Product}/decisions/` |
| [[_tpl_rule]] | Atomic rule | `20_Statute/rules/` |
| [[_tpl_workflow]] | Procedure | `20_Statute/workflows/` |
| [[_tpl_policy]] | Global policy | `20_Statute/policies/` |
| [[_tpl_checklist]] | Review checklist | `20_Statute/checklists/` |
| [[_tpl_skill]] | Agent skill | `30_Skills/` |
| [[_tpl_agent]] | Agent spec | `30_Skills/agents/` |
| [[_tpl_case]] | Incident / decision | `70_Cases/` |

Variables: `{{date}}`, `{{time}}`, `{{title}}`. Everything in `<!-- -->` is filled by hand.
IDs follow [[Naming]]; frontmatter follows [[Metadata]].

**Up:** [[HOME]]
