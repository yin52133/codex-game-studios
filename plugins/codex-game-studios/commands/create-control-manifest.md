# /create-control-manifest

After architecture is complete, produces a flat actionable rules sheet for programmers — what you must do, what you must never do, per system and per layer. Extracted from all Accepted ADRs, technical preferences, and engine reference docs. More immediately actionable than ADRs (which explain why). (source alias: /create-control-manifest).

## Arguments

- `input`: [update — regenerate from current ADRs]

## Workflow

1. Use the `$codex-game-studios:create-control-manifest` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/create-control-manifest <task details>
```
