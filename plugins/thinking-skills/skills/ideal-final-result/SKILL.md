---
name: ideal-final-result
description: Describe the desired benefit as if it could appear with minimal added complexity, cost, or harm, then work backward toward practical approximations. Use when incremental improvement feels insufficient — produce an ideal-state description and steps that move toward it.
---

# Ideal Final Result

Describe the end you actually want as if it could happen with nothing added — no new parts, no extra cost, no added harm, no added effort. Then close the gap.

The failure mode it prevents is polishing the current design while the ideal keeps moving further away.

## When to use

- Incremental tweaks keep producing diminishing returns.
- The problem is framed as "improve the current thing" rather than "achieve the benefit."
- You want a forcing ideal that makes compromises visible.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- No baseline benefit is agreed → define the problem first.
- Near commitment and need to harden → `premortem`.
- You need many ideas at once → `divergent-thinking`.

## Process

1. **Intake — reuse before you ask.** State the benefit sought, for whom, under what limits, and what "incremental" looks like today. Mark fact / assumption / speculation. See [references/ideal.md](references/ideal.md).

2. **State the ideal.** Write the result as if it achieved the benefit with no added complexity, cost, harm, or effort — the ideal final result. Keep it to one sentence per benefit dimension. Use [references/ideal.md](references/ideal.md) and [scripts/ideal.py](scripts/ideal.py).

3. **Name the gap.** For each ideal sentence, record what prevents it today: missing capability, cost, harm, or complexity. Tag each barrier as physical, regulatory, resource, or inherited.

4. **Close the gap in steps.** For each barrier, generate approximation moves that reduce added cost/complexity without abandoning the benefit. Compare each move against the ideal, not against the baseline.

5. **Synthesize 2–3 approximations.** Keep the closest practical paths, each with the benefit preserved, cost added, and harm introduced stated explicitly. See [references/examples.md](references/examples.md).

6. **Probe.** Choose the smallest step toward the ideal, name its signal, and define the decision rule. See [references/approximation.md](references/approximation.md).

## Rules

- The ideal is the benefit without the system — not a better version of the system.
- Separate the ideal from feasibility; filtering belongs at the approximation step, not during the ideal.
- Every approximation must be scored against the ideal, not just against the status quo.
- Label uncertainty: fact / assumption / speculation.

## Going deeper

- Stating the ideal and checking ideality: [references/ideal.md](references/ideal.md)
- Approximation moves and tradeoffs: [references/approximation.md](references/approximation.md)
- Worked example (from ideal to practical): [references/examples.md](references/examples.md)
- When not to use + triage: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and lineage: [references/provenance.md](references/provenance.md)
- Ideal helper (offline): [scripts/ideal.py](scripts/ideal.py)
