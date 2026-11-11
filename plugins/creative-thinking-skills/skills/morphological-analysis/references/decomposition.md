# Decomposition — Choosing Dimensions

A dimension is a parameter of the solution along which a real choice exists. Getting these right decides whether the box is a useful map or a pile of cross-products.

## What counts as a dimension

A good dimension:

- has **at least two real alternatives** (a "dimension" with one option is a constraint, so move it to intake);
- varies **independently** of the others — any option in D2 can pair with any option in D1, at least conceptually;
- is **decision-relevant** — the choice changes cost, experience, risk, or feasibility;
- is stated at the **same abstraction level** as its peers (all mechanism choices, or all policy choices — not a mix).

## MECE, restated for design spaces

- **Mutually exclusive** — every candidate falls into exactly one option per dimension. If a candidate could be "email and chat", the dimension is a channel mix, not a channel; either allow "email+chat" as an option or split into primary/secondary channel.
- **Collectively exhaustive** — the options cover the realistic space, including the current baseline and "none". An empty slot is a finding: write *unknown* and plan how to learn it.

MECE governs the **options**; orthogonality governs the **dimensions**. MECE alone is not enough: "color" and "paint finish" are MECE but correlated, and a matrix of both doubles the work for little insight.

## Orthogonality tests

Run all three before accepting a dimension set.

1. **Swap test.** Pick an option in D1 and imagine every option in D2. If half the D2 options become nonsensical, D2 is conditional on D1; merge or restate.
2. **Tradeoff sentence.** For each dimension, complete: "This dimension trades ___ against ___." If you cannot, it is probably not a decision axis (it may be a quality criterion for scoring).
3. **Cause test.** If D1's option *causes* D2's option, you have a process, not a space. E.g., "synchronous vs asynchronous" determines "call vs email" — keep the mechanism, drop the consequence.

Correlation is not always fatal. If two dimensions are mildly correlated but both are decisions someone can make separately, keep them and note the interaction for pruning. Never silently keep strongly coupled dimensions.

## Common splits

| Symptom | Fix |
|---|---|
| Options in one dimension format with different scopes | Split into "scope" and "format" |
| Option list is really two independent choices | Make two dimensions; the cross-product is the point |
| Many options differ only by degree (5, 10, 20 minutes) | Make one dimension with coarse bands (immediate / same day / week / month) |
| Dimension is a vague adjective ("modern", "friendly") | Replace with observable mechanisms (channel, cadence, interface) |
| Dimension has 10+ options | Group into 3–5 families and add a follow-up dimension if the within-family choice matters |
| Two dimensions always move together | Merge into one, or model the dependency in the pruning matrix |

## Count heuristics

- **3–6 dimensions** is the practical band. Two dimensions is a 2×2 — fine, but call it that; seven or more usually means options are hiding inside dimensions.
- **3–6 options per dimension.** Fewer produces trivial spaces; more produces unreadable columns.
- **Budget the space, not the columns.** 5×5×5×5 = 625 before pruning. Prefer 4×4×4×3 = 192, or plan a sampling strategy.
- For policy or socio-technical problems, move from *components* to *drivers*: who decides, who pays, who is affected, what event triggers action — still independent choices, but closer to the real degrees of freedom.

## Domain templates (starting points, not rules)

| Domain | Candidate dimensions |
|---|---|
| Product feature | user segment × entry point × interaction mode × data source × monetization |
| Service design | trigger × channel × timing × owner × intensity |
| Process redesign | input form × step order × automation level × approval authority × exception path |
| Business model | customer × value mechanism × revenue model × delivery channel × cost structure |
| Communication | audience × message frame × medium × cadence × sender |

Treat a template as a checklist to react to, then delete dimensions that carry no live choice in this situation.

## Worked mini-example

Brief: reduce no-shows for a clinic.

Bad set: "reminder channel × reminder text × reminder effectiveness". Effectiveness is an outcome, not a choice; text is a sub-choice of message design.

Better set:

- **D1 Trigger** — at booking, 7 days before, 1 day before, 2 hours before.
- **D2 Channel** — SMS, app push, phone call, email.
- **D3 Response** — one-way reminder, confirm/cancel buttons, reschedule link, human callback.
- **D4 Owner** — automated system, front desk, clinician.

Each pair is conceptually independent; each option is a mechanism someone can choose. That is a workable 4×4×4×3 box.

## Checklist before populating

- [ ] 3–6 dimensions, each with ≥2 live options.
- [ ] Swap test passed for every pair.
- [ ] One tradeoff sentence per dimension.
- [ ] Options at one abstraction level, including baseline and "none/unknown".
- [ ] Independence rationale written down for the harvest later.
- [ ] Estimated raw combination count and a pruning plan.
