# /reverse-document

Generate design or architecture documents from existing implementation. Works backwards from code/prototypes to create missing planning docs. (source alias: /reverse-document).

## Arguments

- `input`: <type> <path> (e.g., 'design src/gameplay/combat' or 'architecture src/core')

## Workflow

1. Use the `$codex-game-studios:reverse-document` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/reverse-document <task details>
```
