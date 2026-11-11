---
name: inversion
description: Approach a goal through its opposite — ask how to guarantee failure or produce the unwanted outcome, then identify what that reveals about success. Use when direct reasoning misses obstacles, you need failure conditions, or you want to derive design principles by inversion — produce failure analysis and preventive principles.
---

# Inversion

Direct reasoning asks "what would make this succeed?" and answers with a plan that inherits the blind spots of whoever wrote it. Inversion asks the opposite first: **how would we guarantee failure — or reliably produce the outcome we do not want?** Those answers come more easily, are harder to dismiss, and convert into principles that outlive the plan.

Jacobi solved hard mathematics by "inverting, always inverting"; Munger turned it into a reasoning habit — avoid stupidity rather than seek brilliance. The move is not pessimism. It is a different search direction through the same problem, and it works because failure is usually easier to specify than success.

The failure mode it prevents is a success plan built from unexamined assumptions, where risks are mentioned once in a meeting and never designed against.

## When to use

- A goal or strategy is stated only in positive terms and you cannot see how it would fail.
- Planning is stuck in "what should we do?" and every suggestion is a variation of the same idea.
- You need explicit failure conditions to test a launch, process, product, or argument against.
- You want durable design principles, not a one-off risk list.
- A convention feels obviously right; invert it to see what would have to be true for the opposite.
- You are reviewing a confident plan — someone else's or your own.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- A concrete proposal is near commitment and needs hardening → `premortem`.
- You need many alternatives, not failure routes → `divergent-thinking`, `what-if`.
- You need quantified, auditable hazard analysis → FMEA / HAZOP / fault-tree analysis.
- You need evidence about one belief → experiment, pilot, base rates.
- The plan or decision is locked and cannot change → track risks, then postmortem.

## Process

1. **Intake — reuse before you ask.** State the goal as a verb phrase with a subject: "get new accounts to first value within 7 days," not "improve onboarding." Add who it serves, the horizon, the success measure, hard constraints, and what has already been tried. Mark each input **fact / assumption / speculation**; ask only for what is missing. See [references/failure-generation.md](references/failure-generation.md).

2. **Define success — observably.** Write the success condition as measure + threshold + horizon, and write the unwanted outcome beside it. If success cannot be observed, inversion produces vague failure routes ("bad onboarding") that invert into platitudes. Fix the definition until a stranger could tell whether it happened.

3. **Invert — generate guaranteed failure.** Ask **"How could we guarantee this fails?"** and, separately, **"How could we reliably produce the unwanted outcome?"** Generate 15–25 specific routes without judging them: incentives, information, sequencing, capability, ownership, environment, psychology, measurement. Keep the absurd and the impolitic; they expose real gradients. Generate independently before discussing. Use [references/failure-generation.md](references/failure-generation.md) and [scripts/invert.py](scripts/invert.py).

4. **Cluster the failure modes.** Group routes by **causal mechanism**, not by department, phase, or symptom. Give each cluster a one-line causal story ("activation had no owner, so nobody saw the drop-off") and keep 3–6 clusters. Check coverage across people, process, information, and environment; label mechanisms, not labels. See [references/clustering.md](references/clustering.md).

5. **Extract preventive principles.** Negate each cluster: if this route guarantees failure, its opposite is a design condition. Rewrite it in positive, testable form with an observable signal and the decision it changes — "instrument each activation step, name an owner for the drop-off, review weekly," not "don't ignore activation." Keep 3–6 principles; each must trace to a cluster. See [references/principles.md](references/principles.md) and [references/examples.md](references/examples.md).

6. **Probe.** Choose the 1–3 principles that are cheapest to act on now and most load-bearing. For each, define the smallest change, the leading indicator, and the kill criterion. State which failure routes remain speculative. Hand off to `premortem`, `experiment-design`, or `options-portfolio` when those fit better; confirm before running another method.

## Rules

- **Invert the goal, not the wording.** "How to fail at onboarding" must yield mechanisms; "don't succeed" is not a route.
- **Generate before judging.** No filtering during step 3 — premature plausibility checks reproduce the original blind spots.
- **Every route names a mechanism and an actor.** "Poor execution" is a label. "No one owns activation, so the drop-off is never reviewed" is a route.
- **A negative principle is not a principle.** "Don't neglect onboarding" restates the failure; rewrite it to an action with a signal.
- **Keep the goal fixed.** Inversion is not contrarianism; you are mapping failure routes, not arguing against the goal.
- **Label uncertainty.** Facts, assumptions, and speculation stay distinct; a failure route is a hypothesis, not a forecast.
- **Honest provenance.** Attribute Jacobi, Munger, and Adams; call the workflow here an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- How to generate guaranteed-failure routes — prompts, domains, quality tests: [references/failure-generation.md](references/failure-generation.md)
- Clustering routes by causal mechanism and checking coverage: [references/clustering.md](references/clustering.md)
- Turning failure routes into positive, testable principles: [references/principles.md](references/principles.md)
- Worked example (guaranteeing onboarding failure → five principles): [references/examples.md](references/examples.md)
- When not to use, plus comparisons and handoffs: [references/when-not-to-use.md](references/when-not-to-use.md)
- Lineage, evidence limits, and what is original here: [references/provenance.md](references/provenance.md)
- Inversion prompt generator (offline): [scripts/invert.py](scripts/invert.py)
