---
name: first-principles
description: Separate fundamental constraints and observed facts from inherited assumptions, then rebuild an approach from those foundations. Use when "this is how it is done" dominates, conventions masquerade as constraints, or you need approaches that do not depend on existing conventions — produce a constraint map and rebuilt alternatives.
---

# First Principles

Most approaches are inherited designs: a tutorial, a review step, a weekly meeting, a pricing tier that someone copied because it worked elsewhere. First-principles thinking separates what is actually true — physical limits, external obligations, real resource ceilings, observed behavior — from what merely exists, then rebuilds an approach that follows from the surviving fundamentals.

This is a rebuilding method, not an audit. It prevents optimizing a design whose parts were never chosen, while keeping real limits in place so the rebuild is feasible.

## When to use

- "That's how it's done here" is doing more work than any argument.
- A cost or step is treated as irreducible because every existing option includes it.
- A convention has been imported from a different company, market, or era.
- You need an approach that would still work if the current tool, vendor, or org chart vanished.
- Current performance is far from a theoretically achievable floor, and nobody can say why.

If the frame is mostly sound and you need surprising directions, use `lateral-thinking`. If the task is to test particular beliefs rather than rebuild, use `challenge-assumptions`.

## Process

1. **Intake.** Restate the problem as an outcome — "a new user reaches first success" — not as a solution ("build a seven-step onboarding wizard"). Record the incumbent approach, the outcome it is supposed to produce, and the limits believed to force it. Use available context; ask only for gaps.

2. **List constraints and facts.** Write every claimed limit as a checkable assertion ("signup requires a work email because the identity provider needs it"). Separately list observations ("62% abandon at step 3") and the outcome that must occur. Cover physics, regulation, resources, invariants, conventions, and preferences. Capture table: [references/constraints.md](references/constraints.md).

3. **Classify.** For each item ask: *Would this be true if no one had ever built the current system? Who could change it, and at what cost? What observation would refute it?* Label **fundamental** (physics, external regulation, real resource ceiling, true invariant), **inherited** (convention, legacy, copied design, internal policy), or **preference**. Record evidence strength and owner. Uncertain stays uncertain; do not upgrade a guess to a law.

4. **Strip to fundamentals.** Reduce to the irreducible outcome plus the smallest set of constraints that binds every possible solution. Remove solution nouns, inherited sequencing, and requirements that are merely consequences of another constraint. Keep a dropped-item log so anything omitted can be re-added with evidence. Method and stopping rules: [references/decomposition.md](references/decomposition.md).

5. **Rebuild from foundations.** Starting only from the retained fundamentals and the outcome, construct **2–3 distinct approaches**. Vary the unit of value, the actor, the channel, or the cost curve — not cosmetic details. Add an optional constraint back only when evidence demands it, and record why. Heuristics: [references/rebuild.md](references/rebuild.md). Worked example: [references/examples.md](references/examples.md).

6. **Probe and decide next.** For each alternative state what must be true, the cheapest probe, the decision rule, the likely failure, and its cost. Select or test; record which fundamental killed each rejected option. Hand off to `premortem` before commitment, `scamper` once a direction needs variations, or execution when the foundation is stable.

## Rules

- A fact is observed, a constraint is a limit, a convention is neither until verified.
- Real constraints stay. Removing physics or regulation with rhetoric produces a plan that cannot ship.
- Do not rebuild by renaming the incumbent. If the old steps reappear, an inherited constraint slipped back in.
- Fundamentals are context-bound: a latency ceiling, budget, or legal obligation may differ by segment, region, or year. State the scope.
- Test the rebuild against the whole fundamental set, including coordination, operations, and safety costs.
- Label evidence and provenance; call local adaptations adaptations, not established science.

## Going deeper

- Constraint types, fact table, classification tests, boundary cases: [references/constraints.md](references/constraints.md)
- Stripping to fundamentals, why-ladder, stopping rules: [references/decomposition.md](references/decomposition.md)
- Rebuild heuristics, constraint budget, re-add log: [references/rebuild.md](references/rebuild.md)
- Worked example — onboarding rebuilt from first principles: [references/examples.md](references/examples.md)
- When NOT to use, and triage against adjacent methods: [references/when-not-to-use.md](references/when-not-to-use.md)
- Lineage, evidence limits, attribution: [references/provenance.md](references/provenance.md)
- Offline constraint classification helper: [scripts/decompose.py](scripts/decompose.py)
