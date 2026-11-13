# agent-creative-thinking-skills

[![GitHub release](https://img.shields.io/github/v/release/aleknitka/agent-creative-thinking-skills)](https://github.com/aleknitka/agent-creative-thinking-skills/releases) [![skills.sh](https://skills-badge.vercel.app/badge/aleknitka/agent-creative-thinking-skills)](https://www.skills.sh/aleknitka/agent-creative-thinking-skills) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Built with AI — human-guided](https://img.shields.io/badge/Built%20with%20AI-human--guided%20%E2%80%A2%20OMP%20%2B%20Muse%20Spark%20%E2%80%A2%20~95%25%20AI-8b5cf6)](https://github.com/aleknitka/agent-creative-thinking-skills)

> **Make any AI a better thought partner.** 40 micro-methods — with a router, offline helpers, and a shared board — that turn "give me ideas" into *a better question, a wilder set, a stress-tested bet, and a probe you can run tomorrow*.

![Launch film — 40 methods in 36 seconds](assets/launch.gif)

Every method: one instruction → a concrete artifact → a tiny experiment you can run tomorrow. Works with Claude Code, Codex, OMP, Pi — any skills harness.

## Install

```bash
# Claude Code
/plugin marketplace add aleknitka/agent-creative-thinking-skills
/plugin install creative-thinking-skills@agent-creative-thinking-skills
# OMP / Codex / Pi (same catalog)
npx skills add aleknitka/agent-creative-thinking-skills
```

Then: `> Help me think this through — not sure which method fits.` → router shortlists 1–2 methods.

**Try without an agent (offline, no network):**

```bash
uv run python plugins/creative-thinking-skills/skills/thinking-router/scripts/route.py --text "brief is vague, are we solving the right problem?"
python plugins/creative-thinking-skills/skills/lateral-thinking/scripts/random_entry.py --count 3 --seed 7 --problem "retention drops in week 2"
# → 3 provocations (Po) + movement + probe  (--seed for deterministic helpers)
```

## Why this, not just "be more creative"?

Most prompts vary the first idea. This forces a different question, lens, or constraint — then makes you test the result.

- **Routed, not scattered.** 38-method router picks 1–2 methods so you don't browse 40 tabs.
- **Artifact, not advice.** Each skill ends in something hand-offable — a reframed question, 8 alternatives, a loop diagram, a keep/kill portfolio — plus the probe.
- **Offline & deterministic.** Helpers use `--seed` where supported, no network — same input, same prompts.
- **Human + agent board.** `workspace/index.html` — sticky notes, lanes, votes — both sides read/write `workspace/boards/<id>.json`.

Not for one-off polish, validated simulation, or replacing real interviews. See each skill's `references/when-not-to-use.md`.

## In 60 seconds

1. One sentence about what's stuck → router returns *Primary / Alternate / Not now*.
2. Run the skill (15–40 min) → 2–3 bets.
3. Ship a probe: "Try X for 2 weeks; if Y, keep it."

Full triggers: [`thinking-router/references/catalog.md`](plugins/creative-thinking-skills/skills/thinking-router/references/catalog.md).

## Toolkit — 40 skills, one router

Every skill is `SKILL.md` → `references/*.md` → `scripts/*.py`. No worksheets.

| Bucket | What you get | When to reach for it |
|---|---|---|
| **Reframe** (6) | Better question — lateral, first-principles, challenge assumptions, question-storming, abstraction-laddering, inversion | Brief is vague or stuck on the obvious |
| **Generate** (9) | Wilder set — SCAMPER, forced connections, analogical, morphological, brainwriting, crazy-eights, constraints, ideal final result | Baseline exists or ideas are too similar |
| **Explore** (7) | Broader views — six hats, dreamer/realist/critic, stakeholder, what-if, scenario, backcasting, futures-wheel | Need to stress-test views or futures |
| **Decide** (7) | Harder bets — double-diamond, TRIZ, concept-blending, premortem, portfolio, dot-voting, NGT | Need to choose, sequence, or de-risk |
| **Research** (11) | Extra breadth — SIT, C-K, bodystorming, CATWOE, causal-loop, synectics, liberating structures, lotus 8×8, board-game | 29 weren't enough |

<details>
<summary>Full list with sources</summary>

- **Reframe:** `lateral-thinking` (de Bono) · `first-principles` (Aristotle/Descartes) · `challenge-assumptions` (Argyris) · `question-storming` · `abstraction-laddering` (LUMA) · `inversion` (Kahneman)
- **Generate:** `scamper` (Eberle) · `reverse-brainstorming` (Osborn) · `forced-connections` (Gordon) · `analogical-thinking` (Gentner) · `morphological-analysis` (Zwicky) · `brainwriting` (Rohrbach) · `crazy-eights` (Knapp) · `constraint-driven-ideation` · `ideal-final-result` (Altshuller/TRIZ)
- **Explore:** `six-thinking-hats` · `dreamer-realist-critic` (Dilts/Disney) · `stakeholder-perspectives` (Freeman) · `what-if` · `scenario-planning` (Wack/Schwartz) · `backcasting` (Robinson) · `futures-wheel` (Glenn)
- **Decide:** `double-diamond` (Design Council) · `triz-contradictions` · `concept-blending` (Fauconnier/Turner) · `premortem` · `options-portfolio` · `dot-voting-prioritize` · `nominal-group-technique` (Delbecq & Van de Ven)
- **Research (11):** `systematic-inventive-thinking` · `c-k-theory` (Hatchuel & Weil) · `bodystorming` · `rich-picture-catwoe` (Checkland) · `causal-loop-diagram` (Meadows) · `synectics` (Gordon & Prince) · `liberating-structures` · `lotus-blossom` (Matsumura) · `board-game-abstraction` (Sterman) — see `references/provenance.md` in each skill

</details>

| | What it does | When |
|---|---|---|
| `thinking-router` | Scores 38 methods → Primary / Alternate / Not now | "Not sure which method fits" |
| `divergent-thinking` | 10+ options → lenses → cluster → converge | Need breadth before choosing |
| **Workspace** | Browser board — notes, lanes, drawing, votes, timer, file I/O | Human + agent on one board |

## Gallery — copy-paste prompts

Start here: [`examples/gallery.md`](examples/gallery.md) — 60-s quickstart → one prompt per family → `router → skill → probe`.

```bash
uv run python plugins/creative-thinking-skills/skills/thinking-router/scripts/route.py --text "every option looks blocked — what's actually fixed?"
```

More: `board-game-abstraction/scripts/gameify.py` · `causal-loop-diagram/scripts/cld.py` — see `examples/gallery.md`.

## Who this is for (and not for)

**For:** product, design, research, strategy, teaching, ops — solo or team — anyone who wants a better thought partner.

**Not for:** replacing interviews or validated simulation. Skills produce *speculation labeled as such* — they clarify the probe, not the evidence.

## Status, licence, and maintenance

- **Status:** `0.8.0` — breaking changes bump minor pre-1.0. Every skill ships with `references/provenance.md`.
- **Licence:** MIT · **Requires:** `uv` or Python ≥3.13; Claude Code / Codex / OMP / Pi for auto-loading; any modern browser for the workspace.
- **Releases:** [`CHANGELOG.md`](CHANGELOG.md) · `scripts/validate.py` gates releases.

---

## Transparency · AI disclosure — EU AI Act Art. 50

**Human-guided, ~95% AI-generated — OMP + Meta Muse Spark (muse-spark-1.2).** Docs, skills, and film were built with AI under human guidance and review. Author remains responsible.

[<img src="assets/eu-ai/eu-ai-generated-black.svg" alt="EU AI GENERATED" width="220">](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content) Voluntary use of the [EU official icons](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content) ([Art. 50](https://artificialintelligenceact.eu/article/50) · [Code of Practice §2](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content), enforceable 2 Aug 2026) — `AI GENERATED` variant at [`assets/eu-ai/`](assets/eu-ai/) · also on the film end card. Not a deepfake or public-interest publication, so the duty doesn't strictly apply; we disclose anyway. Badges via [AI Disclosure Badges](https://disclosingai.com/) (CC0) at [`assets/badges/`](assets/badges/).

---

## Contributing & docs

- Rules: [`CLAUDE.md`](CLAUDE.md) · New skill: `cp -r templates/skill plugins/creative-thinking-skills/skills/<name>` → `python3 scripts/validate.py`
