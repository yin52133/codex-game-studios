# /create-stories

Break a single epic into implementable story files. Reads the epic, its GDD, governing ADRs, and control manifest. Each story embeds its GDD requirement TR-ID, ADR guidance, acceptance criteria, story type, and test evidence path. Run after /create-epics for each epic. (source alias: /create-stories).

## Arguments

- `input`: [epic-slug | epic-path] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:create-stories` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/create-stories <task details>
```
