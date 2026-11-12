# agent-creative-thinking-skills

[![GitHub release](https://img.shields.io/github/v/release/aleknitka/agent-creative-thinking-skills)](https://github.com/aleknitka/agent-creative-thinking-skills/releases) [![skills.sh](https://skills-badge.vercel.app/badge/aleknitka/agent-creative-thinking-skills)](https://www.skills.sh/aleknitka/agent-creative-thinking-skills) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Claude Code](https://img.shields.io/badge/Claude%20Code-marketplace-8b5cf6?logo=anthropic)](https://code.claude.com/docs/en/plugin-marketplaces) [![Codex](https://img.shields.io/badge/Codex-skills-000000?logo=openai)](https://developers.openai.com/codex/skills) [![OMP & Pi](https://img.shields.io/badge/OMP%20%26%20Pi-marketplace-ff6b35)](https://pi.dev/packages) [![Built with AI — human-guided](https://img.shields.io/badge/Built%20with%20AI-human--guided%20%E2%80%A2%20OMP%20%2B%20Muse%20Spark%20%E2%80%A2%20~95%25%20AI-8b5cf6)](https://github.com/aleknitka/agent-creative-thinking-skills)

> **Make any AI a better thought partner.** 40 micro-methods — with a router, offline helpers, and a shared board — that turn "give me ideas" into *a better question, a wilder set, a stress-tested bet, and a probe you can run tomorrow*.

![Launch film — 40 methods in 36 seconds](assets/launch.gif)

No prompt engineering. Works with Claude Code, Codex, and any harness that loads skills. Every method: one sharp instruction → a concrete artifact → a tiny experiment.

```bash
# Claude Code
/plugin marketplace add aleknitka/agent-creative-thinking-skills
/plugin install creative-thinking-skills@agent-creative-thinking-skills
# OMP (same catalog — .omp-plugin/marketplace.json now shipped)
/marketplace add aleknitka/agent-creative-thinking-skills
/marketplace install creative-thinking-skills@agent-creative-thinking-skills
# Pi / any skills.sh harness
npx skills add aleknitka/agent-creative-thinking-skills
# Run offline helpers with uv (pip also works)
uv run python plugins/creative-thinking-skills/skills/thinking-router/scripts/route.py --text "brief is vague, are we solving the right problem?"
# then in any conversation:
> Help me think this through — not sure which method fits.
# → thinking-router triages and hands off to 1–2 methods with your okay.
```

**Try without an agent (offline, seeded, no network — `uv` or `python`):**
```bash
uv run python plugins/creative-thinking-skills/skills/thinking-router/scripts/route.py --text "brief is vague, are we solving the right problem?"
uv run python plugins/creative-thinking-skills/skills/scamper/scripts/scamper.py --subject "welcome letter — 3 days after signup" --select S,E
# pip fallback: python plugins/creative-thinking-skills/skills/...
```

---

## Why this, not just "be more creative"?

Most prompting tricks give you variations on the *first* idea. This does something else: it forces a different question, a different lens, or a different constraint — then makes you test the result before you commit.

- **Routed, not scattered.** A 38-method router scores your brief and shortlists 1–2 methods — so you don't method-shop from 40 tabs.
- **Artifact, not advice.** Each skill ends in something you can hand to someone: a reframed question, 8 wild alternatives, a loop diagram with a leverage point, a keep/kill portfolio — plus the probe that proves it.
- **Offline & deterministic.** `scripts/*.py` (`--list/--json/--seed`) run with no network and no guesswork; re-run with a seed and you get the same prompt set.
- **Human + agent board.** A vanilla-JS workspace (`workspace/index.html`) — sticky notes, lanes, votes — that both sides read/write (`workspace/boards/<id>.json`).

**When to use something else:** you need a one-off writing polish (use a copilot/inline assistant), a validated simulator (build a model, not a board game), or a deep simulation of stakeholders (do real interviews, not `stakeholder-perspectives` hypotheses). [Full triage in each `references/when-not-to-use.md`.](plugins/creative-thinking-skills/skills/thinking-router/references/catalog.md)

---

## What you get in 60 seconds

1. **Tell the router one sentence** about what's stuck. It returns *Primary / Alternate / Not now* with why.
2. **Run the skill** for 15–40 min: you do the intake, it does the prompts, you harvest 2–3 bets.
3. **Ship a probe:** "we'll try X for 2 weeks; if Y happens we keep it."

Small example (no install):

```bash
python plugins/creative-thinking-skills/skills/lateral-thinking/scripts/random_entry.py --count 3 --seed 7 --problem "retention drops in week 2"
# → 3 provocations (Po:) + movement + reframed probe — not tweaked discounts
```

Full method list and triggers: [`plugins/creative-thinking-skills/skills/thinking-router/references/catalog.md`](plugins/creative-thinking-skills/skills/thinking-router/references/catalog.md).

---

## The toolkit — 40 skills, one router

Every skill follows progressive disclosure: `SKILL.md` (lean process, always loaded) → `references/*.md` (on demand) → `scripts/*.py` (offline helpers). No bundled worksheets.

### Reframe the problem

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `lateral-thinking` | Provocations (Po) → movement → fresh frames | Answers feel predictable / stuck on the obvious | [de Bono](plugins/creative-thinking-skills/skills/lateral-thinking/references/provenance.md) |
| `first-principles` | Strip to fundamentals, rebuild without convention | "This is how it's done" dominates | [Aristotle/Descartes](plugins/creative-thinking-skills/skills/first-principles/references/provenance.md) |
| `challenge-assumptions` | Inventory beliefs → test false/unnecessary/reversed | Problem feels overconstrained | [de Bono/Argyris](plugins/creative-thinking-skills/skills/challenge-assumptions/references/provenance.md) |
| `question-storming` | Questions before answers, revise the brief | Brief is vague / prematurely solution-focused | [Design framing](plugins/creative-thinking-skills/skills/question-storming/references/provenance.md) |
| `abstraction-laddering` | Why-up / how-down across vision → action | Framing too narrow or too abstract | [LUMA](plugins/creative-thinking-skills/skills/abstraction-laddering/references/provenance.md) |
| `inversion` | Guarantee failure → derive design principles | Direct reasoning misses obstacles | [Kahneman/Inversion](plugins/creative-thinking-skills/skills/inversion/references/provenance.md) |

### Generate more varied ideas

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `scamper` | 7 operators on a baseline | Baseline exists to improve | [Eberle](plugins/creative-thinking-skills/skills/scamper/references/provenance.md) |
| `reverse-brainstorming` | Worsen, then reverse | Brainstorming has stalled | [Osborn/Brainstorming](plugins/creative-thinking-skills/skills/reverse-brainstorming/references/provenance.md) |
| `forced-connections` | Random stimulus → forced mapping | Ideas too similar | [de Bono/Gordon](plugins/creative-thinking-skills/skills/forced-connections/references/provenance.md) |
| `analogical-thinking` | Transfer mechanism, not surface feature | Another field may have solved this | [Gentner](plugins/creative-thinking-skills/skills/analogical-thinking/references/provenance.md) |
| `morphological-analysis` | Dimensions × options matrix | Several independent choices | [Zwicky](plugins/creative-thinking-skills/skills/morphological-analysis/references/provenance.md) |
| `brainwriting` | Silent written passes, build, cluster | Early voices anchor / loud voices dominate | [Rohrbach](plugins/creative-thinking-skills/skills/brainwriting/references/provenance.md) |
| `crazy-eights` | 8 distinct concepts in 8 minutes | Need a quick burst | [Knapp/Sprint](plugins/creative-thinking-skills/skills/crazy-eights/references/provenance.md) |
| `constraint-driven-ideation` | Forcing constraints → insights | Open brief → generic ideas | [TRIZ-adjacent](plugins/creative-thinking-skills/skills/constraint-driven-ideation/references/provenance.md) |
| `ideal-final-result` | Best benefit, no added harm/cost | Incremental improvement insufficient | [Altshuller/TRIZ](plugins/creative-thinking-skills/skills/ideal-final-result/references/provenance.md) |

### Explore perspectives & possibilities

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `six-thinking-hats` | 6 modes one at a time (W/R/Y/Bl/G/Bu) | Critique interrupts brainstorming | [de Bono](plugins/creative-thinking-skills/skills/six-thinking-hats/references/provenance.md) |
| `dreamer-realist-critic` | Disney 3 rooms (dream → realism → critique) | Bold idea needs a path to execution | [Dilts/Disney](plugins/creative-thinking-skills/skills/dreamer-realist-critic/references/provenance.md) |
| `stakeholder-perspectives` | Tensions across groups, better tradeoffs | One group's fix hurts another | [Freeman/Mitchell](plugins/creative-thinking-skills/skills/stakeholder-perspectives/references/provenance.md) |
| `what-if` | Single-assumption worlds | Blue-sky / strategic exploration | [Scenario logic](plugins/creative-thinking-skills/skills/what-if/references/provenance.md) |
| `scenario-planning` | 2×2 worlds, robust options, signals | Future uncertain | [Wack/Schwartz](plugins/creative-thinking-skills/skills/scenario-planning/references/provenance.md) |
| `backcasting` | Future → milestones | No route to a long-term ambition | [Robinson](plugins/creative-thinking-skills/skills/backcasting/references/provenance.md) |
| `futures-wheel` | 1st/2nd/nth-order consequences | Ripple effects matter | [Glenn](plugins/creative-thinking-skills/skills/futures-wheel/references/provenance.md) |

### Turn exploration into stronger options

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `double-diamond` | Discover/Define → Develop/Deliver; orchestrates | Need discovery *and* delivery | [Design Council](plugins/creative-thinking-skills/skills/double-diamond/references/provenance.md) |
| `triz-contradictions` | Break a recurring tradeoff (40 principles) | Same tradeoff keeps reappearing | [Altshuller](plugins/creative-thinking-skills/skills/triz-contradictions/references/provenance.md) |
| `concept-blending` | Synthesize mechanisms, not feature piles | Several partial ideas each carry value | [Fauconnier/Turner](plugins/creative-thinking-skills/skills/concept-blending/references/provenance.md) |
| `premortem` | "Already failed" → prevention | Before commitment | [Kahneman](plugins/creative-thinking-skills/skills/premortem/references/provenance.md) |
| `options-portfolio` | Achievable / ambitious / exploratory + probe | Broad set needs narrowing | [Portfolio logic](plugins/creative-thinking-skills/skills/options-portfolio/references/provenance.md) |
| `dot-voting-prioritize` | N/3 dots → Impact–Effort / ICE → keep/pivot/kill | Need visible priority | [Dotmocracy](plugins/creative-thinking-skills/skills/dot-voting-prioritize/references/provenance.md) |
| `nominal-group-technique` | Silent write → round-robin → vote / Delphi | Need hierarchy-proof ranking | [Delbecq & Van de Ven](plugins/creative-thinking-skills/skills/nominal-group-technique/references/provenance.md) |

### From the literature — 11 research-backed extensions beyond the core 27

| Skill | What it does | Use when | Provenance |
|---|---|---|---|
| `systematic-inventive-thinking` | 5 closed-world operators — no new resource types | Concrete system, strict constraints | [SIT · Horowitz/Goldenberg](plugins/creative-thinking-skills/skills/systematic-inventive-thinking/references/provenance.md) · [W4407721440](https://openalex.org/W4407721440) |
| `c-k-theory` | Expand Concept & Knowledge together | Variation exhausted | [C-K · Hatchuel & Weil](plugins/creative-thinking-skills/skills/c-k-theory/references/provenance.md) · [W2049599278](https://openalex.org/W2049599278) |
| `bodystorming` | Enact with props/space | Interaction hard to picture | [Bodystorming · HCI](plugins/creative-thinking-skills/skills/bodystorming/references/provenance.md) · [arXiv:1308.4978](https://arxiv.org/abs/1308.4978) |
| `rich-picture-catwoe` | Visual mess → CATWOE → root definition | No shared picture | [SSM · Checkland](plugins/creative-thinking-skills/skills/rich-picture-catwoe/references/provenance.md) |
| `causal-loop-diagram` | R/B loops, delays, leverage (Meadows) | Fix keeps making its problem worse | [Systems · Forrester/Meadows](plugins/creative-thinking-skills/skills/causal-loop-diagram/references/provenance.md) |
| `synectics` | 4 analogies + excursion → springboards | Forced connections too shallow | [Gordon & Prince](plugins/creative-thinking-skills/skills/synectics/references/provenance.md) |
| `liberating-structures` | 6 micro-structures (1-2-4-All … Ecocycle) | Hierarchy dominates | [Lipmanowicz/McCandless](plugins/creative-thinking-skills/skills/liberating-structures/references/provenance.md) |
| `lotus-blossom` | 8×8 radial — 72 blooms with lineage | 8 not enough; need layered breadth | [Matsumura](plugins/creative-thinking-skills/skills/lotus-blossom/references/provenance.md) |
| `board-game-abstraction` | Playable mechanics → 1-page rules + 3 playtests | Too political/complex to discuss directly | [Beer Game · Sterman](plugins/creative-thinking-skills/skills/board-game-abstraction/references/provenance.md) |
| `dot-voting-prioritize` | Structured dot voting (N/3) + Impact–Effort · ICE | Need visible priority | [Dotmocracy](plugins/creative-thinking-skills/skills/dot-voting-prioritize/references/provenance.md) |
| `nominal-group-technique` | Silent write → vote → Delphi | Need hierarchy-proof ranking | [Delbecq & Van de Ven](plugins/creative-thinking-skills/skills/nominal-group-technique/references/provenance.md) |

> **Research synthesis:** these 11 were selected from 41 candidates across 6 families — see [synthesis.md](megamouth/research/extended-methods/synthesis.md) (ranked table + gaps) and [papers.md](megamouth/research/extended-methods/papers.md) (20 papers: Guilford/Osborn/de Bono/Rohrbach/Altshuller, meta-analyses Scott 2004, Sio 2024, Mullen 1991, + 7 arXiv/8 OpenAlex). Every skill's full lineage and evidence limits live in its `references/provenance.md` linked above.

### Router & shared surface

| | What it does | Use when |
|---|---|---|
| `thinking-router` | Scores 38 methods → Primary/Alternate/Not now + handoff | "Help me think creatively" / unsure which method fits |
| `divergent-thinking` | 10+ options → lenses → cluster → converge | Need breadth before choosing |
| **Workspace** | Browser board — notes, lanes, drawing, votes, timer, file I/O | Human + agent on one board |
| **Workflows** | `brainwriting` (parallel N=3) · `six-thinking-hats` (sequential Blue→Green→Blue) | Group needs orchestration, not just one chat |

---

## Gallery — copy-paste prompts

**Start here:** [`examples/gallery.md`](examples/gallery.md) — 60-s quick start → one prompt per family → end-to-end `router → skill → probe` chain → offline helpers.

```bash
uv run python plugins/creative-thinking-skills/skills/thinking-router/scripts/route.py --text "every option looks blocked — what's actually fixed?"
uv run python plugins/creative-thinking-skills/skills/board-game-abstraction/scripts/gameify.py --problem "onboarding drops 32% before first value" --seed 7
uv run python plugins/creative-thinking-skills/skills/causal-loop-diagram/scripts/cld.py --problem "more reminders → less attention"
```

---

## Who this is for (and not for)

**For:** anyone who works with an AI and wants better thinking — product, design, research, strategy, teaching, ops, solo or team. Code is one use; problem-solving, brainstorming, evaluation, and mental experiments are the others.

**Not for:** replacing user research, stakeholder interviews, or a validated simulation. Many skills deliberately produce *hypotheses labeled as speculation* — they make the probe clearer, they don't replace evidence.

---

## Status, licence, and maintenance

- **Status:** actively maintained, `0.8.0` — breaking changes bump minor while pre-1.0; every skill ships with `references/provenance.md`.
- **Licence:** MIT (see `LICENSE`).
- **Requirements:** `uv` (or Python ≥3.13) for `scripts/*.py` (`uv sync` once, then `uv run python …`); Claude Code, Codex, OMP or Pi for `SKILL.md` auto-loading; workspace needs any modern browser, no build, no deps.
- **Releases:** [`CHANGELOG.md`](CHANGELOG.md) — `scripts/validate.py` gates every release (`OK` on 40 skills, 38-method router, hub-and-spoke).



---

## Transparency · AI disclosure — EU AI Act Art. 50

**Human-guided, ~95% AI-generated — OMP + Meta Muse Spark (muse-spark-1.2).** This repo, its docs, skills, and the launch film were generated with AI (OpenAI Codex / OMP harness + Meta Muse Spark as coding agent) under human guidance, review and editorial control. All content remains the author's responsibility.

<table>
<tr>
<td width="220">

**EU official disclosure — voluntary.**

[![EU — AI Generated — light](assets/eu-ai/eu-ai-generated-black.svg)](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content)
</td>
<td>

[EU Icons for labelling AI-generated content](https://digital-strategy.ec.europa.eu/en/policies/eu-icons-labelling-ai-generated-content) — official set for **Article 50 AI Act** + [Code of Practice §2](https://digital-strategy.ec.europa.eu/en/policies/code-practice-ai-generated-content) (enforcement 2 Aug 2026, penalties to €15M / 3% turnover). The icons are **free to use without attribution** (Commission/AI Office). This project is not a deepfake nor a publication informing the public on matters of public interest, so the legal labelling duty does not strictly apply — we disclose voluntarily for transparency.

- **Mark used here:** `AI GENERATED` (white pill · black text for dark backgrounds · black pill for light) — variant reproduced locally at [`assets/eu-ai/`](assets/eu-ai/) from the official [SVG ZIP](https://ec.europa.eu/newsroom/dae/redirection/document/129546) / [PNG ZIP](https://ec.europa.eu/newsroom/dae/redirection/document/129547). (`AI` + `AI MODIFIED` variants also available.)
- **Where shown:** README transparency section, launch film end card (12s), and as an embedded mark on AI-generated artefacts when shared.

</td>
</tr>
</table>

**Development transparency (CC0):** model-level badge via [AI Disclosure Badges](https://disclosingai.com/) ([mau-vera/built-with-ai-badges](https://github.com/mau-vera/built-with-ai-badges), CC0) — local copies in [`assets/badges/`](assets/badges/), adapted from `AI Assisted · Claude` to **AI Assisted · OMP + Muse Spark · human-guided**.

> *No validator, no compliance checklist — a voluntary "nutrition label" for how this was made.*

---

## Contributing & docs furniture

- Layout & progressive-disclosure rules: [`CLAUDE.md`](CLAUDE.md)
- Start a new skill: `cp -r templates/skill plugins/creative-thinking-skills/skills/<name>` → `python3 scripts/validate.py`
- Full docs site: link when published (currently code-host + `megamouth/docs/` + `examples/gallery.md`)