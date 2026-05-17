# /ux-design

Guided, section-by-section UX spec authoring for a screen, flow, or HUD. Reads game concept, player journey, and relevant GDDs to provide context-aware design guidance. Produces ux-spec.md (per screen/flow) or hud-design.md using the studio templates. (source alias: /ux-design).

## Arguments

- `input`: [screen/flow name] or 'hud' or 'patterns'

## Workflow

1. Use the `$codex-game-studios:ux-design` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/ux-design <task details>
```
