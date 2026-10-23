---
name: link-lake
description: Link inside and across knowledge lakes — wikilinks and hubs, qualified cross-lake ids, connecting a member lake to its main lake, overriding an inherited rule. Use when linking documents, citing another lake, setting up extends, or changing an inherited rule.
---

# Link Lakes

## Inside one lake

- `[[filename]]` or `[[filename|label]]`. Formal documents are named by id, so `[[RULE-PY-001]]` works.
- Every document links its folder hub; every hub links up to `[[HOME]]`. No orphans.
- Never link into another lake with a wikilink — Obsidian cannot resolve it and `check.py` reports a dead link.

## Across lakes

Write the qualified id as plain text: `shepard:RULE-CORE-001`, `prog:NOTE-PY-017`.
The prefix is the target lake's `id` from its `lake.yaml`. The Memory Layer and MCP Hub resolve it; Obsidian does not.

## Member → main

1. `lake.yaml`: `role: member`, `extends: <main lake git URL or local path>`.
2. Until the Memory Layer serves the main lake, clone it next to the member so agents can read the inherited law:

   ```bash
   git clone https://github.com/shepard-system/shepard-knwl-lake ../shepard-knwl-lake
   ```

   Effective Statute = main `20_Statute/` + `30_Skills/` (status `active`) + local documents − overridden ones.

## Override an inherited rule

1. Create a local rule with a local id (`RULE-PY-004`) via [`write-note`](../write-note/SKILL.md).
2. Add `overrides: shepard:RULE-CORE-002` to its frontmatter and explain why in the body.
3. Never override `00_Codex/` or anything with `risk: critical` — escalate to the Architect instead.

The original stays in force in every other lake.
