---
name: write-note
description: Add or fill a document in a knowledge lake — pick the template, assign the id, fill frontmatter and placeholders, place and link it. Use for any new note, rule, workflow, policy, skill, agent spec, ADR, spec, component or case, and when filling an existing draft.
---

# Write a Note

## 1. Pick template and place

| Writing | Template | Folder | ID |
|---------|----------|--------|----|
| Raw idea, anything unsure | `_tpl_seedling` | `01_Inbox/agents/` (agent) · `01_Inbox/shared/` (human) | `NOTE-{DOMAIN}-{NNN}` |
| Product / domain hub | `_tpl_product` | `10_Context/{Product}/{Product}.md` | `NOTE-{DOMAIN}-{NNN}` |
| Component, spec | `_tpl_component`, `_tpl_spec` | `10_Context/{Product}/components/`, `specs/` | `NOTE-{DOMAIN}-{NNN}` |
| Decision | `_tpl_adr` | `10_Context/{Product}/decisions/` | `ADR-{DOMAIN}-{NNN}-{slug}` |
| Rule, workflow | `_tpl_rule`, `_tpl_workflow` | `20_Statute/rules/`, `workflows/` | `RULE-…`, `WFLOW-{DOMAIN}-{NNN}` |
| Policy, checklist | `_tpl_policy`, `_tpl_checklist` | `20_Statute/policies/`, `checklists/` | `POLICY-{name}`, `CHECK-{name}` |
| Skill, agent spec | `_tpl_skill`, `_tpl_agent` | `30_Skills/`, `30_Skills/agents/` | `SKILL-{name}`, `AGENT-{name}` |
| Incident | `_tpl_case` | `70_Cases/` (create on first case) | `CASE-{YYYY}-{NNN}` |

Domain codes come from `lake.yaml`. Agents: everything outside `01_Inbox/agents/` goes on a branch and into a pull request.

## 2. Assign the id

Next free number, never reuse one:

```bash
grep -rhoE '^id: RULE-PY-[0-9]+' --include='*.md' . | sort | tail -1
```

Formal documents (rule, workflow, policy, checklist, skill, agent, case, ADR) use the id as filename. Notes may keep a human filename.

## 3. Fill

- Copy the template. Obsidian fills `{{date}}` and `{{title}}`; when writing files directly, replace them yourself (`YYYY-MM-DD`, the title).
- Frontmatter: `id`, `tags` (at least one `type/`), `status: draft`, `created`, `updated`, `author` (`agent/<name>` for agents).
- Replace every `<!-- … -->` placeholder. Delete sections that do not apply instead of leaving them empty.
- Body in any language; frontmatter keys, ids and tags in English.
- No secrets (`RULE-CORE-001`): reference where a secret lives, never the value.

## 4. Link

- Link the folder hub at the bottom: `**Up:** [[Inbox]]`. New product folder → add its hub to `10_Context/Context.md`.
- Link related documents by filename: `[[RULE-PY-001]]`. Other lakes: plain text `shepard:RULE-CORE-001` ([`link-lake`](../link-lake/SKILL.md)).

## 5. Editing an existing document

Bump `updated`. Never change `id`. Never raise `status` — only the Architect promotes `draft` → `experimental` → `active`.

## 6. Check

```bash
python3 tools/check.py      # must print ok
```
