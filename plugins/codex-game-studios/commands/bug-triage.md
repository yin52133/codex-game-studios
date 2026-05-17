# /bug-triage

Read all open bugs in production/qa/bugs/, re-evaluate priority vs. severity, assign to sprints, surface systemic trends, and produce a triage report. Run at sprint start or when the bug count grows enough to need re-prioritization. (source alias: /bug-triage).

## Arguments

- `input`: [sprint | full | trend]

## Workflow

1. Use the `$codex-game-studios:bug-triage` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/bug-triage <task details>
```
