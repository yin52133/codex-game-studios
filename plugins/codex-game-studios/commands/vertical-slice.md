# /vertical-slice

Pre-Production validation — build a production-quality end-to-end build to confirm the full game loop is achievable before committing to Production. Run after GDDs, architecture, and UX specs are complete. Produces a PROCEED/PIVOT/KILL verdict that gates the Pre-Production → Production transition. (source alias: /vertical-slice).

## Arguments

- `input`: [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:vertical-slice` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/vertical-slice <task details>
```
