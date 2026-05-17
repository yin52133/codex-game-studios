# /ux-review

Validates a UX spec, HUD design, or interaction pattern library for completeness, accessibility compliance, GDD alignment, and implementation readiness. Produces APPROVED / NEEDS REVISION / MAJOR REVISION NEEDED verdict with specific gaps. (source alias: /ux-review).

## Arguments

- `input`: [file-path or 'all' or 'hud' or 'patterns']

## Workflow

1. Use the `$codex-game-studios:ux-review` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/ux-review <task details>
```
