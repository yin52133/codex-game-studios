# /onboard

Generates a contextual onboarding document for a new contributor or agent joining the project. Summarizes project state, architecture, conventions, and current priorities relevant to the specified role or area. (source alias: /onboard).

## Arguments

- `input`: [role|area]

## Workflow

1. Use the `$codex-game-studios:onboard` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/onboard <task details>
```
