# /consistency-check

Scan all GDDs against the entity registry to detect cross-document inconsistencies: same entity with different stats, same item with different values, same formula with different variables. rg search-first approach — reads registry then targets only conflicting GDD sections rather than full document reads. (source alias: /consistency-check).

## Arguments

- `input`: [full | since-last-review | entity:<name> | item:<name>]

## Workflow

1. Use the `$codex-game-studios:consistency-check` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/consistency-check <task details>
```
