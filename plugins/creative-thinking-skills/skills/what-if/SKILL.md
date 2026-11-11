---
name: what-if
description: Change one major assumption at a time and follow the consequences — what if the resource were abundant, the interface disappeared, or the user were someone else? Use for blue-sky thinking, strategic exploration, and stress-testing assumptions — produce alternative worlds and ideas that transfer back to current conditions.
---

# What-If Exploration

Change one load-bearing assumption, build the world it implies, follow the consequences, then carry one insight back to current conditions.

The failure mode it prevents is optimizing inside inherited constraints without ever asking whether they are real — and the opposite failure, blue-sky theatre that never returns to something you can act on.

## When to use

- Blue-sky or strategic exploration: the current answer feels bounded, not wrong.
- Constraints feel inherited ("that's how it works") rather than proven.
- You need alternatives at the level of assumptions, not feature variations.
- You want to stress-test how much a strategy depends on one belief.
- The goal is ideas that transfer back, not a forecast.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- You need plausible futures driven by external uncertainty → `scenario-planning`.
- You have a desired future and need the route to it → `backcasting`.
- You need the ripple map of one given change → `futures-wheel`.
- You want failure causes before committing → `premortem`.
- You only need the assumption inventory → `challenge-assumptions`.
- You need volume inside the current frame → `divergent-thinking`.

## Process

1. **Intake — reuse before you ask.** State the subject in 3–5 sentences: who it serves, how it works today, the limiting resources, the interfaces, the rules, the scale, and the time horizon. Add the goal, hard constraints, and appetite for impossible worlds (low / medium / high). Mark each input **fact / assumption / speculation**. Ask only for what is missing. See [references/branching.md](references/branching.md).

2. **Pick one assumption to mutate.** Inventory candidates across the six types — **resource, interface, actor, rule, scale, time** — then choose the most load-bearing one: the assumption whose removal changes the most downstream decisions. State the mutation explicitly: *"What if X were Y?"* Hold every other assumption fixed for now. Use [references/assumption-types.md](references/assumption-types.md) and [scripts/what_if.py](scripts/what_if.py).

3. **Branch the world.** Sketch the world in which the mutation is simply true: premise, what changes immediately, what stays, what must be true for it to hold, who thrives and who loses. Do not hedge back to reality yet — feasibility filtering belongs later. Timebox 10–15 minutes per world. Use the template in [references/branching.md](references/branching.md).

4. **Trace consequences.** Follow first-, second-, and third-order effects: behaviors, incentives, economics, power, risk, equity, and the environment. Include opportunities and harms; name feedback loops and new frictions. Stop when a ring produces only restatements. See [references/tracing.md](references/tracing.md).

5. **Extract transferable insight.** Separate world-specific detail from the mechanism. Write 1–3 candidate insights and test each: *does it still make sense without the impossible premise?* Keep the strongest and translate it into an option that works under current conditions.

6. **Probe back in current reality.** Define the smallest probe, the leading signal, the kill criterion, and what remains speculative. Hand the probe to `premortem`, `experiment-design`, or `options-portfolio` as appropriate. Confirm with the user before running another method.

## Rules

- One major assumption at a time; only run a combinatorial pass after each mutation has its own sketch.
- Declare the world as fiction. Never present a world's plausibility as evidence.
- No feasibility filtering inside the world; filter only at the transfer-back step.
- Every world must produce a transferable insight or be explicitly abandoned — no tourism.
- Rewordings do not count as new worlds; the mutation must change a constraint, mechanism, or actor.
- Visible uncertainty: label **fact / assumption / speculation** throughout.
- Honest provenance: no single canonical inventor; call adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- The six assumption types — triggers, examples, and selection guidance: [references/assumption-types.md](references/assumption-types.md)
- One-at-a-time mutation and the world sketch template: [references/branching.md](references/branching.md)
- Futures-wheel-style consequence tracing: [references/tracing.md](references/tracing.md)
- Three worlds on one problem (abundant resource / no interface / different user): [references/examples.md](references/examples.md)
- When not to use + handoff map: [references/when-not-to-use.md](references/when-not-to-use.md)
- Lineage, adaptations, and evidence limits: [references/provenance.md](references/provenance.md)
- Assumption picker and world sketches (offline): [scripts/what_if.py](scripts/what_if.py)
