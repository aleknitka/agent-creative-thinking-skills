---
name: challenge-assumptions
description: Make hidden beliefs explicit, test what happens if each is false, unnecessary, or reversed. Use when a problem feels overconstrained, every option looks impossible, or "we've always done it this way" / "policy says" dominates — inventory, test, and reframe before you solve.
---

# Challenge Assumptions

Most problems arrive pre-solved: a problem statement wrapped in beliefs that were never chosen, only inherited. "Onboarding *must* be a tutorial." "Approvals *have to* be manual." "Customers *won't* pay for that." If every option looks impossible, the constraint doing the blocking is usually a belief, not a fact.

This skill makes those beliefs explicit, tests which ones actually carry the problem, and reframes the problem only where the evidence permits. It prevents two failures: accepting unnecessary constraints, and "challenging" constraints that are real and getting burned.

## When to use

- The problem feels overconstrained; all obvious options are ruled out.
- "We've always done it this way," "policy says," or "users need X" closes discussion.
- A problem has been restated several times without getting smaller.
- You suspect the stated problem is a solution in disguise.

If unsure whether this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- You need a new idea once the frame is sound → use `lateral-thinking` or `scamper`.
- The bottleneck is missing facts about the world → research first; this skill will only label your ignorance.
- There is a real engineering tradeoff to resolve → use `triz-contradictions`.
- You are choosing among viable options → use `premortem` / `options-portfolio`.
- The work is correctness-bound (proof, safety sequence, compliance audit) → use vertical / critical thinking.

## Process

1. **Intake — reuse before you ask.** In one sentence each: the stated problem, the goal behind it, the constraints you have been told are hard and who imposed them, what has already been tried, and appetite for changing scope (low / medium / high). Use existing context; ask only for gaps. Write the problem as an assertion, not a topic: "X must Y because Z."

2. **Inventory hidden beliefs.** List **8–15 beliefs**, phrased as checkable assertions, not themes. Cover inherited vs. proven, stakeholder vs. system, boundary, and continuity beliefs — including the ones buried in the problem statement itself. For each: type, source/owner, available evidence, confidence (low / medium / high), and what breaks if it is false. Use [references/inventory.md](references/inventory.md) and [scripts/inventory.py](scripts/inventory.py). Generate before judging.

3. **Pressure-test the drivers.** Rank beliefs by **impact × uncertainty** and test the top handful, not all of them. For each, ask three questions: *If false, what changes? If unnecessary, could the goal still be met? If reversed, what becomes possible?* Collect evidence, label every claim **fact / assumption / speculation**, and record what evidence would settle it. See [references/testing.md](references/testing.md).

4. **Reframe alternatives.** For the 2–4 load-bearing beliefs, apply the reframe patterns — **negate, relax, invert, re-scope, re-attribute** — and write **3 distinct problem statements** of the form "How might we [goal] without [assumption]?" Distinct means a different constraint is gone, not different wording. See [references/reframe-patterns.md](references/reframe-patterns.md).

5. **Small probes.** Choose the cheapest probe that could change your mind for each surviving uncertainty: existing data → desk check → one conversation → prototype → pilot. For each probe state the observable, the decision rule (what result means keep / kill / investigate), cost, and owner. Prefer evidence over debate; never test a safety- or compliance-critical assumption in production. Sizing and rules: [references/testing.md](references/testing.md).

6. **Decide next.** Recommend one of: (a) proceed under a reframed statement, (b) run a probe before deciding, (c) keep the constraint and record why, or (d) hand off — `lateral-thinking` for unexpected directions, `scamper` for variations, `first-principles` for rebuilding from constraints, `premortem` to harden a reframe. Confirm with the user before starting another method. Worked example: [references/examples.md](references/examples.md).

## Rules

- State beliefs as assertions someone could disagree with. "Onboarding is a tutorial" — not "onboarding."
- Separate inventory from evaluation: generate first, rank and test after. No premature "that's obviously true."
- Test what blocks options. A belief that is uncertain but irrelevant is not worth a probe.
- Never relitigate facts as if they were beliefs: physics, arithmetic, signed contracts, and observed behavior stay. Challenge *scope* and *policy*, then verify.
- Reframes must remove or reverse a named belief. Rewording is not a reframe.
- Label fact / assumption / speculation; do not present a plausible story as evidence.
- One probe, one decision rule. A probe without a pre-committed interpretation is theater.
- Honest provenance: name the lineage and call adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Inventory — belief types, prompt list, capture table: [references/inventory.md](references/inventory.md)
- Pressure-testing — falsify / unnecessary / reversal tests, evidence, probe sizing: [references/testing.md](references/testing.md)
- Reframe patterns — negate, relax, invert, re-scope, re-attribute: [references/reframe-patterns.md](references/reframe-patterns.md)
- Worked example — "onboarding must be a tutorial": [references/examples.md](references/examples.md)
- When not to use + triage against lateral / SCAMPER / TRIZ / vertical: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Inventory and test helper (offline): [scripts/inventory.py](scripts/inventory.py)
