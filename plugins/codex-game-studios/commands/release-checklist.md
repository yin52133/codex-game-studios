# /release-checklist

Generates a comprehensive pre-release validation checklist covering build verification, certification requirements, store metadata, and launch readiness. (source alias: /release-checklist).

## Arguments

- `input`: [platform: pc|console|mobile|all]

## Workflow

1. Use the `$codex-game-studios:release-checklist` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/release-checklist <task details>
```
