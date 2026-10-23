---
id: NOTE-CORE-005
tags: [nav/codex, type/convention]
status: active
created: 2026-10-23
updated: 2026-10-23
---

# Federation

> Many lakes, one law. Like federal and state law: global rules are mandatory, local rules extend them.

## Roles

| Role | What it holds | Example |
|------|---------------|---------|
| `main` | Codex + global Statute that applies to every member | this repository, or a company fork of it |
| `member` | Its own Context, Skills, local Statute | `lake-prog`, `lake-langs`, `team-billing` |

Each lake is a separate Obsidian vault and a separate git repository.
Identity lives in `lake.yaml`:

```yaml
id: prog
name: Programming & Sciences
role: member
extends: https://github.com/shepard-system/shepard-knwl-lake
template_version: 0.1.0
domains:
  PY: Python
```

## Cross-Lake References

Inside one lake use normal `[[wikilinks]]`.
To point at another lake write the qualified ID as text: `shepard:RULE-CORE-001`.
Obsidian does not resolve it; the Memory Layer and MCP Hub do.

## Inheritance

1. A member inherits every `active` document of its main lake's `20_Statute/` and `30_Skills/`.
2. A member adds local documents with its own IDs.
3. To change an inherited rule, create a local one and set `overrides: shepard:RULE-CORE-001`.
   The original stays in force everywhere else.
4. A member cannot override [[Codex]] documents or anything with `risk: critical`.

**Effective Statute = main + local − overridden.** Computed by tooling, not by Obsidian.

## Search

Lakes are passive: `lake.yaml` + stable `id` in every document is all they provide.
Searching across all lakes is the job of the Memory Layer.

## Template Sync

Not automated yet. Later a script will replace `00_Codex/` and `99_Templates/` from the template and bump `template_version`.
Never edit those two folders in a member lake.

**Up:** [[Codex]]
