---
name: board-game-abstraction
description: Turn a real-world problem into a playable board-game abstraction — players, scarce resources, board, feedback loop, win/loss — to surface the system's hidden rules without jargon or politics. Use when the situation is too complex or political to discuss directly, you need a shared model fast, or "explain it to a player" would clarify the tradeoffs better than a deck.
---

# Board-Game Abstraction

Explain it to a player, not a stakeholder. Turning the system into a 15-minute playable game forces you to choose who matters, what is scarce, what wins, and what breaks — the four decisions a slide deck lets you dodge.

The failure mode it prevents is the abstract discussion that stays polite and inconclusive because the real rules (scarcity, incentives, loop) were never made playable — and therefore never made testable.

## When to use

- The system is too political or tangled to discuss directly — a neutral game disarms defensiveness.
- You need a shared model in an hour, not a model in a quarter.
- Repeated meetings circle the same tradeoff — making it losable would end the loop.
- Teaching or alignment: players will feel the system's pressure in 15 minutes of play.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- You need to feel friction in space, not on a table → `bodystorming`.
- You need to map causality and leverage before any game → `causal-loop-diagram`.
- You need a shared picture of actors/worldviews first → `rich-picture-catwoe`.
- You need a validated simulation, not a playful abstraction → build a model, not a game.

## Process

1. **Intake — bound the real game.** In 3–5 sentences: whose problem, what good outcome looks like, hard constraints, and who hurts if you fail. Name what is out of scope. See [references/abstraction.md](references/abstraction.md).

2. **Cast and board — abstract.** Name 2–4 *players* (roles, not org chart), 2–3 *scarce resources* (what is fought over), the *board* (queue / track / map / market), and one *feedback loop* that punishes or rewards. No mechanic yet. See [references/abstraction.md](references/abstraction.md) and [scripts/gameify.py](scripts/gameify.py).

3. **Pick a mechanic — not a theme.** Choose one mechanic whose pressure matches the loop: see [references/mechanics.md](references/mechanics.md) (e.g., worker placement for contention, push-your-luck for repeated risk, co-op with hidden info for silo failure). One mechanic per game — theme follows mechanic, not the reverse.

4. **Write the 1-page ruleset.** Turn order, 2–3 actions, costs, failure condition, win/loss. Make it playable in 15 minutes with coins or index cards — no custom art. State what real element each rule abstracts. See [references/abstraction.md](references/abstraction.md).

5. **Mental playtest ×3.** Play once honestly, once greedily (exploit the best action), once cooperatively. Log where the game diverges from reality — that divergence is the insight. Keep probe-worthy divergences. See [references/facilitation.md](references/facilitation.md).

6. **Debrief and transfer.** For each divergence: "what this mechanic teaches about the real system" as a fact/assumption/speculation-labelled probe. Hand off the strongest probe to `premortem` or `causal-loop-diagram` if leverage is unclear. See [references/examples.md](references/examples.md).

## Rules

- One mechanic at a time — never blend two games before the first is playable.
- Must be losable — a game you cannot lose teaches nothing about risk.
- Theme never substitutes for mechanic — "it's like Monopoly" is not a rule.
- Every rule must name what it abstracts in the real system.
- 15-minute playtest is mandatory — unplayed rules are speculation, not a model.
- Keep it cheap — coins, cards, sticky notes. Art hides bad mechanics.
- Label fact / assumption / speculation; the game is a hypothesis, not evidence.
- Honest provenance: Beer Game / System Dynamics and Serious Games inspire this abstraction, but the mechanic table and process are adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Mechanic catalog — pressure → mechanic → what it reveals: [references/mechanics.md](references/mechanics.md)
- Abstraction — players, resources, board, loop, win/loss: [references/abstraction.md](references/abstraction.md)
- Facilitation — timing, solo/AI mode, 15-minute playtest: [references/facilitation.md](references/facilitation.md)
- Worked example (onboarding → "Intent Race" — rules, 3 plays, transfer): [references/examples.md](references/examples.md)
- When not to use — triage vs bodystorming / causal-loop / simulation: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Abstraction helper (offline): [scripts/gameify.py](scripts/gameify.py)
- Shared workspace — board template: [workspace/index.html](../../../../workspace/index.html)
