---
name: morphological-analysis
description: Break a solution into independent dimensions, list options for each, and explore combinations systematically. Use when a solution has several independent choices, the design space is under-mapped, or you need an option matrix and promising combinations — not one-off ideas.
---

# Morphological Analysis

Map the space, then choose in it. Split a solution into independent dimensions, enumerate the options on each, and explore combinations systematically.

The failure mode it prevents is improvising one combination at a time — usually the first familiar one — while most of the design space stays invisible.

## When to use

- The solution has several visibly independent choices: trigger × channel × timing × owner, or material × shape × process × cost profile.
- The team keeps producing variations of the same two or three combinations.
- The design space is under-mapped and you want coverage, not another idea.
- You need an option matrix and a defensible shortlist from it.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- One baseline to improve → `scamper`; the question is "what to change", not "what combinations exist".
- You need raw breadth before structure → `divergent-thinking`; build the dimensions afterwards.
- Candidates already exist and the job is to choose or harden → `options-portfolio`, `premortem`.
- The "dimensions" are causally entangled → model the system first (`first-principles`, `scenario-planning`); a box would fabricate independence.
- What the options even are is unknown → research first, then populate.

## Process

1. **Intake — fix the question and the bounds.** In one paragraph: what is being designed, for whom, what success means, hard constraints (budget, law, brand, deadline), and what artifact is needed (full matrix or shortlist). One sentence per item; do not start the box before this is stable. See [references/decomposition.md](references/decomposition.md).

2. **Decompose into dimensions.** Choose 3–6 parameters that together describe any candidate and can vary independently. Test each: swapping an option in D1 must leave D2's options meaningful. Split dimensions whose options smuggle in a second choice; merge dimensions whose options are two lists of the same thing. Label D1…Dn and write one sentence on why each is independent.

3. **Populate options per dimension.** 3–6 concrete alternatives at one abstraction level per dimension. Include the current baseline, one deliberately boring option, and one unusual-but-legal option; "do nothing / keep as-is" counts. Flag options that are really bundles. Note unknown options explicitly instead of filling space with vague labels. See [references/matrix.md](references/matrix.md).

4. **Prune infeasible combinations.** Build a pairwise compatibility matrix — which option pairs cannot coexist — then apply external filters: physics, law, budget, capability, brand. Record a reason for every removal; a pruned pair is a finding about the problem, not lost work. Prune incompatibility only, never taste. See [references/pruning.md](references/pruning.md).

5. **Score or sample combinations.** Count the surviving space. At roughly ≤100 combinations, score them all; above that, sample for coverage — every option exercised, plus baseline, extremes, and the sweet spot — rather than reading rows top to bottom. Score against 3–5 criteria fixed during intake, weighted, and keep the raw combinations beside the scores. See [references/sampling.md](references/sampling.md).

6. **Harvest 2–3 concepts + probes.** Turn the strongest combinations into 1–2 sentence concepts with a concrete mechanism. Keep portfolio variety — one safe, one ambitious, one cheap-and-strange. Give each one next probe (prototype, test, interview, estimate) and name which dimensions are still unresolved. See [references/examples.md](references/examples.md).

## Rules

- Dimensions must be independent; if you cannot state the independence in one sentence, split or merge.
- One abstraction level across options; a dimension of "email / chat / rebuild the CRM" is broken.
- Separate generation, pruning, and scoring — never prune during population.
- Prune on stated incompatibility and constraints, not preference; score preference later.
- Sampling must show coverage: prove each option appears at least once in the shortlist.
- Explosion is normal: 4×5×4×3 = 240 combinations. Decide how you will prune before you populate.
- Label facts, assumptions, and speculation; every combination is a hypothesis until probed.
- Honest provenance: attribute the box to Zwicky and its extensions to Ritchey. See [references/provenance.md](references/provenance.md).

## Going deeper

- Picking orthogonal dimensions (MECE, splits, domain templates): [references/decomposition.md](references/decomposition.md)
- Building the matrix — Zwicky box notation, labels, size heuristics: [references/matrix.md](references/matrix.md)
- Pruning — compatibility matrix, feasibility filters, audit trail: [references/pruning.md](references/pruning.md)
- Sampling and scoring — coverage-first sampling, extremes, criteria: [references/sampling.md](references/sampling.md)
- Worked example (onboarding trigger × channel × timing × owner, 2 concepts): [references/examples.md](references/examples.md)
- When not to use + handoff map: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, Zwicky's lineage, evidence limits: [references/provenance.md](references/provenance.md)
- Matrix helper (offline): [scripts/morph.py](scripts/morph.py)
