# /security-audit

Audit the game for security vulnerabilities: save tampering, cheat vectors, network exploits, data exposure, and input validation gaps. Produces a prioritised security report with remediation guidance. Run before any public release or multiplayer launch. (source alias: /security-audit).

## Arguments

- `input`: [full | network | save | input | quick]

## Workflow

1. Use the `$codex-game-studios:security-audit` skill.
2. Read only the role, template, rule, or engine references that the skill requests.
3. Apply repository `AGENTS.md` instructions before editing files.
4. Report the concrete artifact paths and verification result.

## Examples

```text
/security-audit <task details>
```
