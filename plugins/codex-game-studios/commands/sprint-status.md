# /sprint-status

Fast sprint status check. Reads the current sprint plan, scans story files for status, and produces a concise progress snapshot with burndown assessment and emerging risks. Run at any time during a sprint for quick situational awareness. Use when user asks 'how is the sprint going', 'sprint update', 'show sprint progress'. (source alias: /sprint-status).

## Arguments

- `input`: [sprint-number or blank for current]

## Workflow

1. Use the `$codex-game-studios:sprint-status` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/sprint-status <task details>
```
