# Changelog

All notable changes to `agent-thinking-skills` follow Keep a Changelog and align with the `plugin.json` / `marketplace.json` versions.

## [0.2.0] — 2026-11-10

### Added — 29 skills (full catalog coverage)

**Reframe the problem (6):** `lateral-thinking`, `first-principles`, `challenge-assumptions`, `question-storming`, `abstraction-laddering`, `inversion`.

**Generate more varied ideas (9):** `scamper`, `reverse-brainstorming`, `forced-connections`, `analogical-thinking`, `morphological-analysis`, `brainwriting`, `crazy-eights`, `constraint-driven-ideation`, `ideal-final-result`.

**Explore perspectives and possibilities (7):** `six-thinking-hats`, `dreamer-realist-critic`, `stakeholder-perspectives`, `what-if`, `scenario-planning`, `backcasting`, `futures-wheel`.

**Turn exploration into stronger options (5):** `double-diamond`, `triz-contradictions`, `concept-blending`, `premortem`, `options-portfolio`.

**Router & baseline:** `thinking-router` (27-method catalog scorer, offline `scripts/route.py`) and `divergent-thinking` (pre-existing, retained).

Every skill ships with:

- YAML front matter (`name` = directory, `description` ≤1024 with WHAT + WHEN + trigger phrases).
- Lean `SKILL.md` (≤71 lines, hub links only) + 5–7 leaf `references/*.md` (one topic per file, no nested chains) + offline `scripts/*.py` (`--json` / `--list` / `--seed`, no deps).

Cross-links: `thinking-router` catalog lists all 27 + ★ suggested first 8; individual skills link to the router for triage.

### Changed

- `README.md` — full 29-skill table by category with “what it does / use when” and progressive-disclosure note; version set to `0.2.0`.
- `.claude-plugin/marketplace.json` and `plugins/thinking-skills/.claude-plugin/plugin.json` — version `0.1.0` → `0.2.0`; enriched keywords and descriptions; packaging verified against Claude Code, Codex, and `agSys` strict frontmatter (only `name` + `description`).

### Provenance & packaging

- Provenance audit: no bundled third-party long verbatim; 29/29 skills have `references/provenance.md` with lineage, adaptation distinction, and evidence/limits; word banks are short/original per provenance notes.
- Hub-and-spoke progressive disclosure verified: no nested markdown links in any `references/` leaf; all `SKILL.md` outbound links resolve.
- Portable method instructions confirmed for Codex and Claude Code (same `SKILL.md` tree, `scripts/validate.py → OK`).

### Notes

- Source catalog: `megamouth/docs/creative-thinking-methodologies.md` (27 methods; terminology note: “Feihatz” → Six Thinking Hats).
- `megamouth/` retains the worktree's `docs/` + `research/lateral-thinking/` extras; canonical `plugins/` is authoritative for the marketplace.
- Suggested first 8 (doc §Suggested): all 8 shipped — `lateral-thinking`, `six-thinking-hats`, `scamper`, `challenge-assumptions`, `analogical-thinking`, `what-if`, `morphological-analysis`, `premortem`.

## [0.1.0] — 2026-11-06

- Initial marketplace and `divergent-thinking` skill.
