# /localize

Full localization pipeline: scan for hardcoded strings, extract and manage string tables, validate translations, generate translator briefings, run cultural/sensitivity review, manage VO localization, test RTL/platform requirements, enforce string freeze, and report coverage. (source alias: /localize).

## Arguments

- `input`: [scan|extract|validate|status|brief|cultural-review|vo-pipeline|rtl-check|freeze|qa]

## Workflow

1. Use the `$codex-game-studios:localize` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/localize <task details>
```
