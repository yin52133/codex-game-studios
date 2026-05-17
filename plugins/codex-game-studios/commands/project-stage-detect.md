# /project-stage-detect

Automatically analyze project state, detect stage, identify gaps, and recommend next steps based on existing artifacts. Use when user asks 'where are we in development', 'what stage are we in', 'full project audit'. (source alias: /project-stage-detect).

## Arguments

- `input`: [optional: role filter like 'programmer' or 'designer']

## Workflow

1. Use the `$codex-game-studios:project-stage-detect` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/project-stage-detect <task details>
```
