# /estimate

Estimates task effort by analyzing complexity, dependencies, historical velocity, and risk factors. Produces a structured estimate with confidence levels. (source alias: /estimate).

## Arguments

- `input`: [task-description]

## Workflow

1. Use the `$codex-game-studios:estimate` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/estimate <task details>
```
