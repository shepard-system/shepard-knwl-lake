---
id: AGENT-{name}
tags: [type/agent]
status: draft
version: 0.1.0
role: 
created: {{date}}
updated: {{date}}
author: 
aliases: []
llm-ready: false
---

# AGENT: <!-- name -->

<!-- 
Agent specification defines what an agent can and cannot do.
ROLE: builder | reviewer | synchronizer | indexer
STATUS: draft → experimental → active → deprecated

Rule: Agents without specs do not exist.
-->

## Role

<!-- builder | reviewer | synchronizer | indexer -->

---

## Purpose

<!-- Single sentence. What is this agent for? -->

---

## Capabilities

<!-- What can this agent do? -->

- 
- 
- 

---

## Constraints

<!-- What can this agent NOT do? Be explicit. -->

- ❌ 
- ❌ 
- ❌ 

---

## Allowed Skills

<!-- Skills this agent can use -->

| Skill | Purpose |
|-------|---------|
| [[SKILL-xxx]] | |

---

## Governing Rules

<!-- Rules this agent must follow -->

- [[RULE-XXX]]
- 

---

## MCP Tools

| Tool | Server | Permission | Rationale |
|------|--------|------------|-----------|
| | | read | |
| | | write | |

---

## Workflows

<!-- Workflows this agent participates in -->

| Workflow | Role in Workflow |
|----------|------------------|
| [[WFLOW-XXX]] | |

---

## Logging Requirements

All actions must log:

- [ ] Timestamp
- [ ] Session ID
- [ ] Tools used
- [ ] Rules consulted
- [ ] Decision summary
- [ ] Artifacts produced

---

## Escalation Triggers

<!-- When should this agent escalate to human? -->

| Trigger | Action |
|---------|--------|
| No applicable rule found | Escalate |
| Confidence < 70% | Escalate |
| High-risk operation | Request approval |
| | |

---

## Performance Metrics

| Metric | Target |
|--------|--------|
| Success rate | |
| Avg execution time | |
| Escalation rate | |

---

## Related

- Other agents: 
- Skills: 
- Policies: `shepard:POLICY-agent-access`

---

## Changelog

| Version | Date | Change | Author |
|---------|------|--------|--------|
| 0.1.0 | {{date}} | Created | |
