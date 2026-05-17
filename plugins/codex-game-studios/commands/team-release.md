# /team-release

Orchestrate the release team: coordinates release-manager, qa-lead, devops-engineer, and producer to execute a release from candidate to deployment. (source alias: /team-release).

## Arguments

- `input`: [version number or 'next'] [--review full|lean|solo]

## Workflow

1. Use the `$codex-game-studios:team-release` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/team-release <task details>
```
