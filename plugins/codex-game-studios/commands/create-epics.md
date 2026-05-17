# /create-epics

Translate approved GDDs + architecture into epics — one epic per architectural module. Defines scope, governing ADRs, engine risk, and untraced requirements. Does NOT break into stories — run /create-stories [epic-slug] after each epic is created. (source alias: /create-epics).

## Arguments

- `input`: [system-name | layer: foundation|core|feature|presentation | all] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:create-epics` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/create-epics <task details>
```
