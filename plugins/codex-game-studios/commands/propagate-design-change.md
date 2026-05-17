# /propagate-design-change

When a GDD is revised, scans all ADRs and the traceability index to identify which architectural decisions are now potentially stale. Produces a change impact report and guides the user through resolution. (source alias: /propagate-design-change).

## Arguments

- `input`: [path/to/changed-gdd.md]

## Workflow

1. Use the `$codex-game-studios:propagate-design-change` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/propagate-design-change <task details>
```
