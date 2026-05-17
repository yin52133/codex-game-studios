# /soak-test

Generate a soak test protocol for extended play sessions. Defines what to observe, measure, and log during long play sessions to surface slow leaks, fatigue effects, and edge cases that only appear after sustained play. Primarily used in Polish and Release phases. (source alias: /soak-test).

## Arguments

- `input`: [duration: 30m | 1h | 2h | 4h] [focus: memory | stability | balance | all]

## Workflow

1. Use the `$codex-game-studios:soak-test` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/soak-test <task details>
```
