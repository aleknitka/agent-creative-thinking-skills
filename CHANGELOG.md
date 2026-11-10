# Changelog

All notable changes to `agent-thinking-skills` follow Keep a Changelog and align with the `plugin.json` / `marketplace.json` versions.

## [0.3.0] — 2026-11-10

### Added — Example gallery, agent workflows, and shared workspace

- **Example gallery** (`examples/gallery.md`) — Quick start (60 s) → one runnable prompt per category (4 sections: Reframe 6, Generate 9, Perspectives 7, Stronger 5) → end-to-end `thinking-router → skill → probe` chain → links to catalog, workflows, and offline helpers (`scripts/*.py`).

- **Agent workflows** (`plugins/thinking-skills/workflows/`) — prove the catalog note: "Agent-based workflows may be useful for some methods" (single-conversation remains default).

  | Workflow | Topology | When |
  |---|---|---|
  | `brainwriting-workflow.md` | **Parallel** — fan N=3 generators via `task` in one `tasks[]` batch (silent pass1 → self-build pass2), one rotation build pass, then freeze → main-agent cluster (3–6) → harvest | Group anchors early / timezone spread / need 30–100 ideas + builds |
  | `six-thinking-hats-workflow.md` | **Sequential** — Blue opens (chooses sequence via `scripts/sequence.py`) → chain White→Red→Yellow→Black→Green (parallel participants *inside* each hat, hats strictly sequential) → Blue closes | Critique interrupts brainstorming; need one-hat-at-a-time enforced |

  Workflows are **workflow layer only** — method detail stays in the skill hub (`skills/brainwriting/SKILL.md`, `skills/six-thinking-hats/SKILL.md`) with their leaf `references/*.md`. Linked from each hub's `Going deeper` and from `skills/thinking-router/SKILL.md` for handoff.

- **Workspace** (`workspace/`) — lightweight browser board usable by both agents and humans (sticky notes ✱ lanes ✱ drawing ✱ dot voting ✱ timer ✱ clustering). No build, no deps, vanilla JS.

  Files: `workspace/index.html` + `workspace/app.js` + `workspace/style.css`, schema `workspace/boards/_schema.json`, demo board `workspace/boards/demo.json`.

  Aids: sticky notes (text, color, votes, fact/assumption/speculation/action/question), lanes/columns (hats, SCAMPER, sheets, phases), freehand/line drawing on canvas, dot voting, timer (5/10/15 min), clustering by lane, import/export **JSON** + **PNG**.

  Agent I/O: read/write `workspace/boards/<id>.json` (open `?board=<id>`), file drop or `window.workspace.apply(state)`, optional `POST /api/state` via the ~40-line companion server when localStorage is not enough. Templates: blank · six hats · brainwriting · SCAMPER · crazy-8s · backcasting · morph box. Research note on reuse-vs-build (Scrumlr, Excalidraw, Drawnix, WBO, Retrospected, Kanvana) in `megamouth/research/workspace-aids/report.md` (76 lines + appendix, sources cited).

### Changed

- `README.md` — new sections **Example Gallery**, **Agent Workflows**, and **Workspace** (run instructions, aids, agent I/O, schema refs); version `0.2.0` → `0.3.0`.
- `.claude-plugin/marketplace.json` and `plugins/thinking-skills/.claude-plugin/plugin.json` — version `0.2.0` → `0.3.0`; keywords expanded (`workspace`, `whiteboard`).
- `skills/brainwriting/SKILL.md`, `skills/six-thinking-hats/SKILL.md`, `skills/thinking-router/SKILL.md` — wired `workflows/` and `workspace/` in `Going deeper` (relative links verified; `scripts/validate.py → OK`).

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
