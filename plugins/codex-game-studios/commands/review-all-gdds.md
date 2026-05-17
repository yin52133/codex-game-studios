# /review-all-gdds

Holistic cross-GDD consistency and game design review. Reads all system GDDs simultaneously and checks for contradictions between them, stale references, ownership conflicts, formula incompatibilities, and game design theory violations (dominant strategies, economic imbalance, cognitive overload, pillar drift). Run after all MVP GDDs are written, before architecture begins. (source alias: /review-all-gdds).

## Arguments

- `input`: [focus: full | consistency | design-theory | since-last-review]

## Workflow

1. Use the `$codex-game-studios:review-all-gdds` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/review-all-gdds <task details>
```
