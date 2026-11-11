# agent-thinking-skills

[![GitHub release](https://img.shields.io/github/v/release/aleknitka/agent-thinking-skills)](https://github.com/aleknitka/agent-thinking-skills/releases) [![skills.sh](https://skills.sh/badge/aleknitka/agent-thinking-skills)](https://skills.sh/aleknitka/agent-thinking-skills) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![Claude Code & Codex](https://img.shields.io/badge/harness-Claude%20Code%20%7C%20Codex-blueviolet)](https://github.com/aleknitka/agent-thinking-skills#install)


> **Make any AI a better thought partner.** 40 micro-methods — with a router, offline helpers, and a shared board — that turn "give me ideas" into *a better question, a wilder set, a stress-tested bet, and a probe you can run tomorrow*.

No prompt engineering. Works with Claude Code, Codex, and any harness that loads skills. Every method: one sharp instruction → a concrete artifact → a tiny experiment.

```bash
/plugin marketplace add <github-user>/agent-thinking-skills
/plugin install thinking-skills@agent-thinking-skills
# then in any conversation:
> Help me think this through — not sure which method fits.
# → thinking-router triages and hands off to 1–2 methods with your okay.
```

**Try without an agent (offline, seeded, no network):**
```bash
python plugins/thinking-skills/skills/thinking-router/scripts/route.py --text "brief is vague, are we solving the right problem?"
python plugins/thinking-skills/skills/scamper/scripts/scamper.py --subject "welcome letter — 3 days after signup" --select S,E
```

---

## Why this, not just "be more creative"?

Most prompting tricks give you variations on the *first* idea. This does something else: it forces a different question, a different lens, or a different constraint — then makes you test the result before you commit.

- **Routed, not scattered.** A 38-method router scores your brief and shortlists 1–2 methods — so you don't method-shop from 40 tabs.
- **Artifact, not advice.** Each skill ends in something you can hand to someone: a reframed question, 8 wild alternatives, a loop diagram with a leverage point, a keep/kill portfolio — plus the probe that proves it.
- **Offline & deterministic.** `scripts/*.py` (`--list/--json/--seed`) run with no network and no guesswork; re-run with a seed and you get the same prompt set.
- **Human + agent board.** A vanilla-JS workspace (`workspace/index.html`) — sticky notes, lanes, votes — that both sides read/write (`workspace/boards/<id>.json`).

**When to use something else:** you need a one-off writing polish (use a copilot/inline assistant), a validated simulator (build a model, not a board game), or a deep simulation of stakeholders (do real interviews, not `stakeholder-perspectives` hypotheses). [Full triage in each `references/when-not-to-use.md`.](plugins/thinking-skills/skills/thinking-router/references/catalog.md)

---

## What you get in 60 seconds

1. **Tell the router one sentence** about what's stuck. It returns *Primary / Alternate / Not now* with why.
2. **Run the skill** for 15–40 min: you do the intake, it does the prompts, you harvest 2–3 bets.
3. **Ship a probe:** "we'll try X for 2 weeks; if Y happens we keep it."

Small example (no install):

```bash
python plugins/thinking-skills/skills/lateral-thinking/scripts/random_entry.py --count 3 --seed 7 --problem "retention drops in week 2"
# → 3 provocations (Po:) + movement + reframed probe — not tweaked discounts
```

Full method list and triggers: [`plugins/thinking-skills/skills/thinking-router/references/catalog.md`](plugins/thinking-skills/skills/thinking-router/references/catalog.md).

---

## The toolkit — 40 skills, one router

Every skill follows progressive disclosure: `SKILL.md` (lean process, always loaded) → `references/*.md` (on demand) → `scripts/*.py` (offline helpers). No bundled worksheets.

### Reframe the problem

| Skill | What it does | Use when |
|---|---|---|
| `lateral-thinking` | Provocations (Po) → movement → fresh frames | Answers feel predictable / stuck on the obvious |
| `first-principles` | Strip to fundamentals, rebuild without convention | "This is how it's done" dominates |
| `challenge-assumptions` | Inventory beliefs → test false/unnecessary/reversed | Problem feels overconstrained |
| `question-storming` | Questions before answers, revise the brief | Brief is vague / prematurely solution-focused |
| `abstraction-laddering` | Why-up / how-down across vision → action | Framing too narrow or too abstract |
| `inversion` | Guarantee failure → derive design principles | Direct reasoning misses obstacles |

### Generate more varied ideas

| Skill | What it does | Use when |
|---|---|---|
| `scamper` | 7 operators on a baseline | Baseline exists to improve |
| `reverse-brainstorming` | Worsen, then reverse | Brainstorming has stalled |
| `forced-connections` | Random stimulus → forced mapping | Ideas too similar |
| `analogical-thinking` | Transfer mechanism, not surface feature | Another field may have solved this |
| `morphological-analysis` | Dimensions × options matrix | Several independent choices |
| `brainwriting` | Silent written passes, build, cluster | Early voices anchor / loud voices dominate |
| `crazy-eights` | 8 distinct concepts in 8 minutes | Need a quick burst |
| `constraint-driven-ideation` | Forcing constraints → insights | Open brief → generic ideas |
| `ideal-final-result` | Best benefit, no added harm/cost | Incremental improvement insufficient |

### Explore perspectives & possibilities

| Skill | What it does | Use when |
|---|---|---|
| `six-thinking-hats` | 6 modes one at a time (W/R/Y/Bl/G/Bu) | Critique interrupts brainstorming |
| `dreamer-realist-critic` | Disney 3 rooms (dream → realism → critique) | Bold idea needs a path to execution |
| `stakeholder-perspectives` | Tensions across groups, better tradeoffs | One group's fix hurts another |
| `what-if` | Single-assumption worlds | Blue-sky / strategic exploration |
| `scenario-planning` | 2×2 worlds, robust options, signals | Future uncertain |
| `backcasting` | Future → milestones | No route to a long-term ambition |
| `futures-wheel` | 1st/2nd/nth-order consequences | Ripple effects matter |

### Turn exploration into stronger options

| Skill | What it does | Use when |
|---|---|---|
| `double-diamond` | Discover/Define → Develop/Deliver; orchestrates | Need discovery *and* delivery |
| `triz-contradictions` | Break a recurring tradeoff (40 principles) | Same tradeoff keeps reappearing |
| `concept-blending` | Synthesize mechanisms, not feature piles | Several partial ideas each carry value |
| `premortem` | "Already failed" → prevention | Before commitment |
| `options-portfolio` | Achievable / ambitious / exploratory + probe | Broad set needs narrowing |
| `dot-voting-prioritize` | N/3 dots → Impact–Effort / ICE → keep/pivot/kill | Need visible priority |
| `nominal-group-technique` | Silent write → round-robin → vote / Delphi | Need hierarchy-proof ranking |

### Beyond the original 27 — what research added

| Skill | What it does | Use when | Source |
|---|---|---|---|
| `systematic-inventive-thinking` | 5 closed-world operators — no new resource types | Concrete system, strict constraints |
| `c-k-theory` | Expand Concept & Knowledge together | Variation exhausted |
| `bodystorming` | Enact with props/space | Interaction hard to picture |
| `rich-picture-catwoe` | Visual mess → CATWOE → root definition | No shared picture |
| `causal-loop-diagram` | R/B loops, delays, leverage (Meadows) | Fix keeps making its problem worse |
| `synectics` | 4 analogies + excursion → springboards | Forced connections too shallow |
| `liberating-structures` | 6 micro-structures (1-2-4-All … Ecocycle) | Hierarchy dominates |
| `lotus-blossom` | 8×8 radial — 72 blooms with lineage | 8 not enough; need layered breadth |
| `board-game-abstraction` | Playable mechanics → 1-page rules + 3 playtests | Too political/complex to discuss directly |

Source: [`megamouth/research/extended-methods/synthesis.md`](megamouth/research/extended-methods/synthesis.md) (11 from 41 candidates + 7 arXiv/8 OpenAlex).

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
python plugins/thinking-skills/skills/thinking-router/scripts/route.py --text "every option looks blocked — what's actually fixed?"
python plugins/thinking-skills/skills/board-game-abstraction/scripts/gameify.py --problem "onboarding drops 32% before first value" --seed 7
python plugins/thinking-skills/skills/causal-loop-diagram/scripts/cld.py --problem "more reminders → less attention"
```

---

## Who this is for (and not for)

**For:** anyone who works with an AI and wants better thinking — product, design, research, strategy, teaching, ops, solo or team. Code is one use; problem-solving, brainstorming, evaluation, and mental experiments are the others.

**Not for:** replacing user research, stakeholder interviews, or a validated simulation. Many skills deliberately produce *hypotheses labeled as speculation* — they make the probe clearer, they don't replace evidence.

---

## Status, licence, and maintenance

- **Status:** actively maintained, `0.7.0` — breaking changes bump minor while pre-1.0; every skill ships with `references/provenance.md`.
- **Licence:** MIT (see `LICENSE`).
- **Requirements:** Python ≥3.13 for `scripts/*.py`; Claude Code or Codex for `SKILL.md` auto-loading; workspace needs any modern browser, no build, no deps.
- **Releases:** [`CHANGELOG.md`](CHANGELOG.md) — `scripts/validate.py` gates every release (`OK` on 40 skills, 38-method router, hub-and-spoke).

---

## Contributing & docs furniture

- Layout & progressive-disclosure rules: [`CLAUDE.md`](CLAUDE.md)
- Start a new skill: `cp -r templates/skill plugins/thinking-skills/skills/<name>` → `python3 scripts/validate.py`
- Full docs site: link when published (currently code-host + `megamouth/docs/` + `examples/gallery.md`)

