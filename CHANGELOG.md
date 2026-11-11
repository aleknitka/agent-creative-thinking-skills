# Changelog

All notable changes to `agent-thinking-skills` follow Keep a Changelog and align with the `plugin.json` / `marketplace.json` versions.

## [0.5.0] — 2026-11-11

### Added — 4 more extended skills (backlog 7–10) + workspace/gallery for all 10 extended

**New skills — completing `research/extended-methods/synthesis.md` (10 of 41 candidates; 0.4.0 shipped 6, this ships 7–10):**

| Skill | Family | One-line output | Evidence |
|---|---|---|---|
| `liberating-structures` | Facilitation — 6 Liberating Structures (1-2-4-All / Impromptu Networking / 15% Solutions / TRIZ / Wicked Questions / Ecocycle Planning) | 6 micro-structures cheatsheet + timed harvest | Lipmanowicz & McCandless (2014), liberatingstructures.com |
| `nominal-group-technique` | Convergence — NGT (Delbecq & Van de Ven 1971) + Delphi (Dalkey/Helmer RAND) | Silent write → round-robin → vote (5-4-3-2-1 / N/3 / Delphi median-IQR) + dissent log | OpenAlex NGT/Delphi lit |
| `lotus-blossom` | Divergence — MY Lotus Blossom 8×8 (Matsumura) | Centre → 8 petals → 72 blooms → prune → harvest; distinct from morph box (combinatorial) & crazy-8s (flat 8) | Matsumura / Mycoted |
| `dot-voting-prioritize` | Convergence — structured dot voting (N/3, at-most-one-per-item) + Impact–Effort + ICE (Sean Ellis) | N/3 dots → impact–effort 2×2 → keep/pivot/kill | Practitioner (ICE: Sean Ellis); complements `options-portfolio` |

Each: lean `SKILL.md` (≤59 lines) + 5–7 leaf `references/*.md` + offline `scripts/*.py` (`--list/--json/--seed`, no deps), hub-and-spoke verified.

**Cheap wins for all 10 extended skills:**

- `examples/gallery.md` — new **§5 Extended & convergence (6 + 4 beyond the 27)** with one prompt + artifact + helper per extended skill (10 total); end-to-end chain 27→33→37.
- `workspace/` — 10 new board templates (`sit`, `c-k-theory`, `bodystorming`, `rich-picture-catwoe`, `causal-loop`, `synectics`, `liberating-structures`, `nominal-group`, `lotus-blossom`, `dot-voting`) in `workspace/app.js` + `workspace/boards/_schema.json` enum (now 17) + `workspace/index.html` `<select>` (17 options). All use existing sticky-note/lane I/O; no new deps.

### Changed

- `thinking-router` — 33 → 37 methods: `scripts/route.py` 37 grouped entries (`better-question 6 / more-ideas 14 / broader-perspectives 10 / stronger-options 7`) with budgets for LS/NGT/Lotus/Dot; tuned NEED_KEYWORDS for lotus/radial/petal and ranking/consensus/ICE; `references/catalog.md` 33→37 (27+10), `SKILL.md`/`references/routing-logic.md`/`references/provenance.md` updated.
- `README.md` — 35 → 39 skills (27 base + 10 extended + router + divergent-thinking), router 33→37, Extended table 6→10 rows, source note 6→10, version `0.4.0`→`0.5.0`.
- `.claude-plugin/marketplace.json` and `plugins/thinking-skills/.claude-plugin/plugin.json` — version `0.4.0`→`0.5.0`; descriptions 35→39 / 33→37; keywords +4 new slugs.

### Notes

- Counts: 39 skills on disk (27 + 10 + router + divergent), catalog distinct slugs 39, `route.py` 37 methods (LS & relatives are facilitation layers not separately scored in every group), light patterns remain non-skill patterns.
- Packaging: `scripts/validate.py → OK` (39 skills), `route.py --list` groups correctly, `--text` routing verified for new triggers (e.g., "1-2-4-All" → LS, "NGT ranking" → nominal-group-technique, "lotus blossom" → lotus-blossom, "dot voting" → dot-voting-prioritize).


## [0.4.0] — 2026-11-11

### Added — 6 extended skills beyond the 27 + router upgrade to 33 methods

**Extended skills (source: `megamouth/research/extended-methods/synthesis.md` — top 6 of 41 candidates, 7 arXiv + 8 OpenAlex):**

| Skill | Family | One-line output | Evidence |
|---|---|---|---|
| `systematic-inventive-thinking` (SIT) | Structured inventive — inside-the-box (Subtraction/Multiplication/Division/Task Unification/Attribute Dependency) | 5-operator closed-world matrix | W4407721440, W2753361279, sitsite.com |
| `c-k-theory` (Hatchuel/Weil) | Meta-theory — joint C/K expansion | C-tree + K expansions + learning agenda | W2049599278, W4298440840 |
| `bodystorming` | Embodied — props/space/enactment | Walkthrough + friction clusters + probes | 1308.4978 |
| `rich-picture-catwoe` (Checkland/SSM) | Systems — visual sensemaking + worldview | Rich picture + CATWOE → root definition | IfM/SSM |
| `causal-loop-diagram` | Systems — feedback loops, delays, archetypes, Meadows leverage | CLD + leverage map | Systems Dynamics / Meadows |
| `synectics` (Gordon/Prince) | Analogical — 4 analogies + excursion | Four analogies + excursion → springboards | Synectics lit; complements `analogical-thinking` |

Each ships with: lean `SKILL.md` (hub, ≤500 lines) + 5–8 leaf `references/*.md` + offline `scripts/*.py` (`--list/--json/--seed`, no deps), progressively disclosed. No bundled third-party long verbatim; provenance in `references/provenance.md`.

Light touch-ups (no new skills, documented as patterns):

- `Dot Voting` + `Ecocycle Planning` + `15% Solutions` → `options-portfolio/references/portfolio.md`
- `1-2-4-All` → `brainwriting/references/facilitation.md`
- `15% Solutions` → `futures-wheel/references/when-not-to-use.md`

### Changed

- `thinking-router` — 27 → 33 methods (27 base + 6 extended): `references/catalog.md` now 33 (★ base / ◆ extended), `scripts/route.py` now 33 grouped entries with tuned triggers/budgets/appetite; `SKILL.md`/`references/routing-logic.md`/`references/provenance.md` updated; `--list` groups `better-question / more-ideas / broader-perspectives / stronger-options` correctly. Ranking verified for extended triggers (e.g., "fix keeps making it worse" → `causal-loop-diagram`, "no shared picture" → `rich-picture-catwoe`, "no new resources" → `systematic-inventive-thinking`).
- `README.md` — counts 29 → 35 skills (27 base + 6 extended + router + divergent-thinking), router 27 → 33 methods, new **Extended — beyond the 27** section, source catalog note extended, version `0.3.0` → `0.4.0`; tagline updated.
- `.claude-plugin/marketplace.json` and `plugins/thinking-skills/.claude-plugin/plugin.json` — version `0.3.0` → `0.4.0`; descriptions updated to 35 skills / 33-method router; keywords expanded.

### Notes

- Counts: 35 skills on disk (`27 + 6 extended + thinking-router + divergent-thinking`), catalog distinct slugs 35, `route.py` 33 methods; light patterns are not separate skills.
- Packaging: `scripts/validate.py → OK`, `route.py --list` groups correctly, hub-and-spoke preserved (no nested links in `references/` leaves).


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
