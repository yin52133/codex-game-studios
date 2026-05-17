# /day-one-patch

Prepare a day-one patch for a game launch. Scopes, prioritises, implements, and QA-gates a focused patch addressing known issues discovered after gold master but before or immediately after public launch. Treats the patch as a mini-sprint with its own QA gate and rollback plan. (source alias: /day-one-patch).

## Arguments

- `input`: [scope: known-bugs | cert-feedback | all]

## Workflow

1. Use the `$codex-game-studios:day-one-patch` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/day-one-patch <task details>
```
