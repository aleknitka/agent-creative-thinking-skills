---
name: c-k-theory
description: Expand the design space by jointly growing Concept space and Knowledge space — partitioning concepts beyond existing knowledge and activating new knowledge to expand them. Use when variation of known designs is exhausted, you need a generative expansion rather than selection, or you want a meta-frame for what-if and morphological moves.
---

# C-K Theory

Variation stays inside what you already know how to do; expansion changes what is thinkable. C-K Theory separates the two by holding a Concept space (undecidable propositions) and a Knowledge space (verified facts) and growing them together.

The failure mode it prevents is treating a fixed concept as the problem and searching only inside existing knowledge for a better variant.

## When to use

- Variations of known designs (SCAMPER, morphological box) feel exhausted.
- You need generative expansion — new concepts, not better instances.
- You want a meta-frame for `what-if`, `morphological-analysis`, and `analogical-thinking` moves.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- A concrete system needs disciplined closed-world mutation → `systematic-inventive-thinking`.
- You need to choose among known candidates → `options-portfolio` or `premortem`.
- The work is near commitment and needs hardening, not expansion.

## Process

1. **Intake — name the initial concept.** State it as an undecidable proposition ("a product that … without …") — not a requirement. List what you already know that could validate it. See [references/concepts.md](references/concepts.md).

2. **Partition the Concept — expand C.** Generate restrictive partitions (adding a property) and expansive partitions (adding a property with no precedent in K). Keep at least one expansive partition per round. See [references/operators.md](references/operators.md) and [scripts/c-k.py](scripts/c-k.py).

3. **Activate Knowledge — expand K.** For each expansive partition, name the knowledge pocket that would make it decidable — or that is missing and must be learned. Add that pocket to K as a learning agenda, not as a claim.

4. **Use K to re-partition C.** Let newly activated knowledge suggest new partitions ("now that we know X, we can consider C with Y"). Record the design square as it grows.

5. **Evaluate generativity, not optimality.** Score the expanded C-tree by coverage, surprise, and learning value — not by feasibility. Keep 2–3 expansive branches; discard paths that merely refine the initial concept.

6. **Probe and decide next.** For each kept branch, name the smallest K-expansion that would make it decidable and the probe that tests it. See [references/examples.md](references/examples.md).

## Rules

- A concept is an undecidable proposition — it must not be decidable from current K.
- One partition at a time — never blend restrictive and expansive in one step.
- K is verifiable — every element must be testable or learnable; no speculation in K.
- Every C expansion must point to a K pocket that would decide it, or to a stated gap.
- Label fact / assumption / speculation; C is speculation by definition until K decides it.
- Honest provenance: attribute C-K to Hatchuel and Weil; call this workflow an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- Concept space — partitions and the design square: [references/concepts.md](references/concepts.md)
- Knowledge space — pockets, activation, and learning agenda: [references/knowledge.md](references/knowledge.md)
- The four operators — C→C, C→K, K→C, K→K: [references/operators.md](references/operators.md)
- Worked example (one concept → C-tree → probes): [references/examples.md](references/examples.md)
- When not to use — triage vs morphology/what-if/analogical: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- C-K helper (offline): [scripts/c-k.py](scripts/c-k.py)
