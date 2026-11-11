---
name: lotus-blossom
description: Expand one central theme into eight petals, then each petal into eight sub-ideas, yielding up to 72 ideas on a three-layer radial board. Use when you need breadth beyond a quick eight-slot burst, want ideas that stay traceable to one theme, or want hierarchical divergence that exposes sub-themes before details — not convergence, and not a combinations matrix.
---

# Lotus Blossom

One theme blooms outward: eight petals around the center, then eight concrete ideas around each petal. The 8×8 structure produces up to 72 idea slots while keeping every idea traceable to the theme and to the angle that generated it.

The failure mode it prevents is the long list that drifts: forty ideas on a wall, none of them clearly answering the same question, and no way to see which part of the space is thin.

## When to use

- You have one central theme or question and need many ideas that must stay connected to it.
- Eight quick concepts (Crazy Eights) are not enough: you want a second, deeper layer under each direction.
- You want sub-themes visible before details, so the group can see where the space is empty or over-farmed.
- You are working solo or with an AI agent and a structured board keeps generation from collapsing into repetition.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- The job is to choose among candidates → `options-portfolio`, dot voting, or plain decision analysis; another expansion pass makes the pile worse.
- The design space has independent dimensions and you need coverage or combination shortlists → `morphological-analysis`; the box is the right geometry.
- There is no central theme yet, or the question is wrong → `question-storming`, `divergent-thinking`, or `lateral-thinking` first.
- You need eight comparable concepts under time pressure → `crazy-eights`; 72 slots is the wrong size for a ten-minute burst.
- The work needs one defensible, compliant answer → breadth is not the constraint; stop generating.

## Process

1. **Intake — fix the center.** Write the theme as one phrase or one "How might we…" question, plus audience, success, hard constraints, and what has already been tried. The center is the whole board's scope: if it holds two problems, split it. Mark fact / assumption / speculation. See [references/procedure.md](references/procedure.md).

2. **Build the center — eight petals.** Place the theme in the middle and write eight angles that together cover it: actors, moment, place, mechanism, incentive, artifact, constraint, signal (or a domain-specific set). Each petal is a distinct mechanism of attack, not a synonym of the theme. Test: could two petals produce the same idea? If yes, replace one. See [references/procedure.md](references/procedure.md) and [scripts/lotus.py](scripts/lotus.py).

3. **Expand each petal — eight sub-ideas.** Take one petal at a time and fill its own 3×3 block: the petal label in that block's center, eight concrete ideas around it. Concrete means a mechanism plus an object or action, not a slogan. Complete a petal before moving on; each block is a small independent burst. See [references/facilitation.md](references/facilitation.md).

4. **Prune and score the 72.** Freeze generation. Merge duplicates, cut infeasible slots, and group the rest by petal. Then score against three to five criteria fixed during intake. Keep a short reason for each cut. Pruning is a finding about the problem, not lost work. See [references/procedure.md](references/procedure.md).

5. **Harvest the top five and probe.** Turn five survivors into one-paragraph concepts with a concrete mechanism and its strongest assumption. Give each the smallest next probe and the signal that would change your mind. Keep portfolio variety: at least one safe, one ambitious, one cheap-and-strange. See [references/examples.md](references/examples.md).

## Rules

- One theme per board. A second theme needs a second board, not a busier center.
- Petals must be distinct mechanisms. Rewordings of the center or of each other do not count.
- No judging during expansion — no crossing out, ranking, or "that won't work" until all petals are full.
- Concrete over clever: every sub-slot needs an actor, action, or artifact; a label is not an idea.
- Fill the petal before harvesting from it; stopping at three ideas is how one direction masquerades as a board.
- Prune and score only after generation; keep the raw slots beside the scores.
- Label facts, assumptions, and speculation. Seventy-two slots are hypotheses, not a plan.
- Honest provenance: attribute the method to Matsumura Yasuo; call timing and text adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Three-layer structure, timing, and board layout: [references/procedure.md](references/procedure.md)
- Facilitation — solo, AI-agent, team, and colour coding: [references/facilitation.md](references/facilitation.md)
- Worked example (onboarding friction → 8 petals → 72 slots → top 5): [references/examples.md](references/examples.md)
- When not to use + handoff map vs morphology and Crazy Eights: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, Matsumura's lineage, evidence limits: [references/provenance.md](references/provenance.md)
- Board and JSON generator (offline): [scripts/lotus.py](scripts/lotus.py)
