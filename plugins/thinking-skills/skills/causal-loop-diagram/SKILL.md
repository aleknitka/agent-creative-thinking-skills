---
name: causal-loop-diagram
description: Map reinforcing and balancing feedback loops, mark delays and archetypes, and surface leverage points that linear cause-and-effect misses. Use when a fix keeps making its problem worse, you need to see where to intervene, or the system's behavior comes from its structure, not a single cause.
---

# Causal Loop Diagram

Draw the loops, not the line. A causal loop diagram shows where action feeds back on itself — reinforcing growth or decay and balancing toward limits — and where delays hide the leverage.

The failure mode it prevents is treating a feedback-driven problem as a linear cause to push harder on, which amplifies the loop you meant to break.

## When to use

- A fix keeps making its problem worse (e.g., more reminders create less attention).
- Behavior persists or oscillates despite local improvements.
- You need to name where to intervene — leverage points, not more effort.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- A one-time decision with no feedback matters more than system dynamics.
- The bottleneck is missing facts, not structure → research first.
- You need a visual situation picture before causality → `rich-picture-catwoe`.

## Process

1. **Intake — bound the system and its behavior over time.** State the problematic behavior, the time horizon, and the boundary (what is inside vs. taken as given). Add a reference-mode sketch if possible. See [references/structure.md](references/structure.md).

2. **Name variables and causal links.** List 6–10 variables that can go up or down; draw polarity (+: same direction, –: opposite) and mark delays (||). See [references/links.md](references/links.md) and [scripts/cld.py](scripts/cld.py).

3. **Close the loops.** Follow links until each returns to a loop — label reinforcing (R) and balancing (B), count loops, and name delays. See [references/loops.md](references/loops.md).

4. **Check archetypes and gaps.** Compare against common archetypes (shifting the burden, fixes that fail, limits to growth, success to the successful) and note what's missing or misnamed. See [references/archetypes.md](references/archetypes.md).

5. **Surface leverage points.** Following Meadows' leverage hierarchy, rank where an intervention would move the system with least effort — not the easy effort, but the high-leverage change.

6. **Probe and decide next.** For the top 1–2 leverage points, name the smallest intervention, its signal, and the owner. See [references/examples.md](references/examples.md).

## Rules

- One polarity per link — + means "more of A → more of B," – means "more of A → less of B"; never blend.
- Every link must be causal, not correlational — state the mechanism that transmits the effect.
- Mark delays explicitly (||) — delays are where leverage hides and where unintended consequences grow.
- Label loops R or B; a diagram without labeled loops is a cause map, not a CLD.
- Label fact / assumption / speculation; loop polarity is observed or hypothesized, not assumed.
- Honest provenance: attribute CLD and archetypes to the System Dynamics / Systems Thinking tradition; call this workflow an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- System boundary and behavior over time: [references/structure.md](references/structure.md)
- Variables, polarity, and delays: [references/links.md](references/links.md)
- Closing loops — reinforcing, balancing, and delays: [references/loops.md](references/loops.md)
- Archetypes — shifting the burden, fixes that fail, limits to growth, success to the successful: [references/archetypes.md](references/archetypes.md)
- Leverage points (Meadows 12): [references/leverage.md](references/leverage.md)
- Worked example (reminder → attention → activation loop): [references/examples.md](references/examples.md)
- When not to use — triage vs futures-wheel/scenario: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- CLD helper (offline): [scripts/cld.py](scripts/cld.py)
