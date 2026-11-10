# The Matrix — Zwicky Box Notation and Size

The morphological box is a table: **parameters as columns, alternatives as rows**. A candidate solution is one alternative drawn from every column.

## Notation

Use stable IDs so combinations can be discussed and pruned without ambiguity:

- Dimensions: `D1`, `D2`, … with a short name — `D1 Trigger`.
- Options: `D1.1`, `D1.2`, … in column order.
- Combinations: `C1`, `C2`, … assigned after pruning, plus the option IDs — `C7 = D1.3 × D2.1 × D3.4 × D4.2`.

A Zwicky box in Markdown:

| D1 Trigger | D2 Channel | D3 Timing | D4 Owner |
|---|---|---|---|
| D1.1 signup | D2.1 in-app | D3.1 immediate | D4.1 automated |
| D1.2 first login | D2.2 email | D3.2 day 1–3 | D4.2 support |
| D1.3 first value event | D2.3 human call | D3.3 day 7 | D4.3 product |
| D1.4 inactivity | D2.4 SMS/WhatsApp | D3.4 day 30 | D4.4 sales |

Rules for the table:

- Fill column-wise, not row-wise: finish one dimension before starting the next. Row-wise filling invites fake combinations.
- Keep the physical order of options meaningful (cheapest→most expensive, earliest→latest). It makes patterns visible and sampling easier.
- Do not add a "combination" column inside the box; combinations belong to the enumeration step.
- If an option cannot be named in 1–4 words, it is a concept, not an option — move it to a note.

## What the box is for

Three uses, in order:

1. **Coverage check** — are there whole regions of the space nobody has considered? The box makes the gaps visible.
2. **Combination generation** — enumerate the cross-product, not a hand-picked diagonal.
3. **Communication** — the box is a compact artifact a stakeholder can read and challenge.

It is not a decision matrix; scores come later and live beside the box, not inside it.

## Size heuristics

The raw size is the product of the option counts:

| Dimensions | Options each | Raw combinations | Handling |
|---|---|---|---|
| 2–3 | 2–4 | 4–64 | Enumerate all; score all |
| 3–4 | 3–5 | 27–625 | Enumerate; prune hard; score survivors |
| 4–5 | 4–6 | 256–7,776 | Prune, then sample systematically |
| 6+ | any | >10,000 | Reduce dimensions or split the problem into sub-boxes |

Practical thresholds from field use, not theory:

- **≤100 survivors** — read and score every one.
- **100–500** — prune again on the third criterion, then sample 15–30 for review.
- **>500** — do not enumerate by hand. Use `scripts/morph.py` and a coverage sampler; revisit whether every dimension carries a live decision.

Two ways to shrink a box legitimately:

- **Fewer dimensions** by merging correlated axes (accept some fidelity loss, record it).
- **Coarser options** by banding degrees (`day 1–3`, `week`, `month`) instead of listing every value.

Do not shrink by deleting awkward options before pruning: that is taste masquerading as structure.

## Option taxonomy

Populate each dimension with a deliberate spread:

- **Baseline** — what happens today, or the do-nothing path. Always include it; it is the comparison that makes the box honest.
- **Boring / proven** — the option a conservative operator would choose.
- **Adjacent** — a known option from a neighboring domain or channel.
- **Wildcard** — legal, feasible in principle, and culturally odd. One per dimension is enough; it prevents the box from encoding the current org chart.

Record a one-line note under the box for options that need explanation.

## Partial and staged boxes

The box does not have to be complete before use.

- **Partial box** (Zwicky's own practice): leave unknown options as `?` and mark the dimension as provisional. A partially filled box still exposes gaps.
- **Staged box**: run one box for the concept (what the solution is) and a second for the delivery (how it reaches people). Two small boxes beat one unreadable one, and the second can reuse the first's concepts as options.
- **Wildcard column**: add a final dimension "surprise" with options `none`, `recombine two rows`, `import from another industry`. Use sparingly; it is a stimulus, not a parameter.

## Anti-patterns

- **The trophy row** — filling the box only along one already-chosen combination, then presenting the others as decoration.
- **Dimension drift** — mid-population, options start describing a different level of abstraction.
- **Fake exhaustiveness** — 30 vague options ("AI", "personalization", "community") that cannot be built or compared.
- **Box as deliverable** — handing over a 256-cell table without pruning, sampling, or a recommendation. The box is an instrument.
- **Mixing constraints into options** — "must be GDPR compliant" is a filter, not an alternative; it belongs in pruning.

## Minimal worksheet

```
D1 <name>: D1.1 <opt>  D1.2 <opt>  D1.3 <opt>
D2 <name>: ...
D3 <name>: ...
D4 <name>: ...
Raw size: __ × __ × __ × __ = ____
Pruned:   ____   (see pruning.md)
Sampled:  ____   (see sampling.md)
```
