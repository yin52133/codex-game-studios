# /asset-spec

Generate per-asset visual specifications and AI generation prompts from GDDs, level docs, or character profiles. Produces structured spec files and updates the master asset manifest. Run after art bible and GDD/level design are approved, before production begins. (source alias: /asset-spec).

## Arguments

- `input`: [system:<name> | level:<name> | character:<name>] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:asset-spec` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/asset-spec <task details>
```
