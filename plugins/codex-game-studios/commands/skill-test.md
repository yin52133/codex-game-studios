# /skill-test

Validate skill files for structural compliance and behavioral correctness. Three modes: static (linter), spec (behavioral), audit (coverage report). (source alias: /skill-test).

## Arguments

- `input`: static [skill-name | all] | spec [skill-name] | category [skill-name | all] | audit

## Workflow

1. Use the `$codex-game-studios:skill-test` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/skill-test <task details>
```
