# /design-review

Reviews a game design document for completeness, internal consistency, implementability, and adherence to project design standards. Run this before handing a design document to programmers. (source alias: /design-review).

## Arguments

- `input`: [path-to-design-doc] [--depth full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:design-review` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/design-review <task details>
```
