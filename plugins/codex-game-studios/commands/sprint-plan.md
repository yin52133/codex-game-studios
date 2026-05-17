# /sprint-plan

Generates a new sprint plan or updates an existing one based on the current milestone, completed work, and available capacity. Pulls context from production documents and design backlogs. (source alias: /sprint-plan).

## Arguments

- `input`: [new|update|status] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:sprint-plan` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/sprint-plan <task details>
```
