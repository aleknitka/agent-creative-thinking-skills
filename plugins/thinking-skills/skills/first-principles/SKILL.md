---
name: first-principles
description: Separate fundamental constraints and observed facts from inherited assumptions, then rebuild an approach from those foundations. Use when "this is how it is done" dominates, conventions masquerade as constraints, or you need approaches that do not depend on existing conventions — produce a constraint map and rebuilt alternatives.
---

# First-Principles Thinking

Rebuild from what must be true, not from what is usually done. Start with physics, regulation, and invariants — then add back only the conventions you can justify.

The failure mode it prevents is optimizing a tradition while calling it a constraint.

## When to use

- "This is how it is done" dominates and nobody can source why.
- Conventions, benchmarks, and analogues are treated as limits.
- You need an approach that does not depend on the current design.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- You need stepwise correctness (proof, compliance) → vertical thinking.
- The bottleneck is missing facts → research first.
- You need variations on a fixed baseline → `scamper`.

## Process

1. **Intake — reuse before you ask.** In 2–3 sentences: what must be achieved, for whom, by when, and the hard context (budget, law, physics, platform). Reuse available context; ask only for what is missing.

2. **List candidates.** Capture every stated constraint, fact, and "must" in a table (statement, source, type). Include the quiet ones: defaults, handoffs, deadlines, and formats. See [references/constraints.md](references/constraints.md).

3. **Classify.** For each, mark fundamental (physics, regulation, invariant), inherited (convention, benchmark, habit), or preference (taste, risk tolerance). Keep the evidence that would move it. See [references/decomposition.md](references/decomposition.md).

4. **Strip to fundamentals.** Keep only fundamentals and directly observed facts; set inherited constraints aside explicitly — do not delete them yet. State what remains as the minimal problem to solve.

5. **Rebuild from foundations.** From fundamentals alone, generate 2–3 approaches that achieve the goal while satisfying only what must be true. Add back inherited constraints only where they earn their keep. See [references/rebuild.md](references/rebuild.md).

6. **Probe and decide.** For each rebuilt approach, name the smallest test of its load-bearing claim, what would falsify it, and which inherited constraint would return if it fails. See [references/examples.md](references/examples.md).

## Rules

- Separate fundamentals from inherited before you generate alternatives — generation before classification reproduces the tradition.
- Make the source explicit for every "must" — unsourced is inherited until proven otherwise.
- Every rebuilt approach must satisfy fundamentals; inherited constraints are optional until justified.
- Keep uncertainty visible: label fact / assumption / speculation and state falsification conditions.
- Honest provenance: note Aristotle and Descartes as distant lineage, Musk as popularizer; call workflow here adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- Constraint types and fact table: [references/constraints.md](references/constraints.md)
- Stripping to fundamentals and decomposition: [references/decomposition.md](references/decomposition.md)
- Rebuilding heuristics and alternatives: [references/rebuild.md](references/rebuild.md)
- Worked example (rebuilding from minimal constraints): [references/examples.md](references/examples.md)
- When not to use + triage: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence: [references/provenance.md](references/provenance.md)
- Constraint classifier (offline): [scripts/decompose.py](scripts/decompose.py)
