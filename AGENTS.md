# Codex Game Studios

This repository contains a Codex-native port of Claude Code Game Studios.

## Active Port Package

- Plugin root: `plugins/codex-game-studios`
- Source inventory: `plugins/codex-game-studios/references/source-inventory.json`
- Porting spec: `design/index.html`

## Codex Usage Rules

- Use plugin skills through `$codex-game-studios:<skill-name>` or matching command files under `plugins/codex-game-studios/commands`.
- Treat role files under `plugins/codex-game-studios/references/roles` as guidance for review and decision quality.
- Do not write new Codex routing rules under `.claude` or `.trae`.
- Keep the plugin self-contained; do not require a local `ref/` checkout for validation or installation.
- Preserve upstream attribution in `plugins/codex-game-studios/references/source-docs/` and `plugins/codex-game-studios/references/source-attribution.md`.
