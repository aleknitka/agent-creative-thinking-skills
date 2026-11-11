# Impact–Effort Matrix

The Impact–Effort matrix plots each candidate on two axes and sorts the plane
into four quadrants. It is deliberately coarse: the value is a shared visual
argument about where effort should go, not a precise score.

## The 2×2

```
                 High impact
                     │
   Big bets          │        Quick wins
   (plan, fund)      │        (do next)
                     │
  ───────────────────┼───────────────────
                     │
   Money pits        │        Fill-ins
   (kill/park)       │        (do if spare)
                     │
                 Low impact
        High effort        Low effort
```

Naming varies by team; the semantics do not:

| Quadrant | Impact | Effort | Action |
|---|---|---|---|
| Quick wins | high | low | Do next; these buy credibility and learning |
| Big bets | high | high | Plan and stage; require a probe before full funding |
| Fill-ins | low | low | Do only with spare capacity; batch them |
| Money pits | low | high | Kill or park with a revival trigger |

## Scoring anchors

Use 1–5 for both axes, with written anchors so different scorers are
comparable. Define "impact" once for the session — revenue, users reached,
risk removed, learning value — and do not let it drift per item.

### Impact (1–5)

| Score | Anchor |
|---|---|
| 1 | No measurable effect on the stated goal; cosmetic |
| 2 | Small local effect, one team or a narrow segment |
| 3 | Clear effect on one goal metric or a meaningful user group |
| 4 | Large effect on a primary goal, or removes a significant risk |
| 5 | Changes the trajectory of the goal or the viability of the plan |

### Effort (1–5)

| Score | Anchor |
|---|---|
| 1 | Days; existing tools and authority |
| 2 | 1–2 weeks; one team, no new approvals |
| 3 | A month or a quarter; cross-team coordination |
| 4 | A quarter or more; new capability, hiring, or integration |
| 5 | Multi-quarter; irreversible commitment or major capital |

Effort includes the full cost of ownership — maintenance, support, migration,
and the attention it consumes — not just the build.

## Plotting procedurally

1. Score every surviving item independently, then reconcile differences in
   the anchors, not by averaging silently.
2. Mark scores as evidence, estimate, or guess.
3. Use the vote totals as a third signal: annotate each item with its dot
   count; a quick win nobody wants is still a question.
4. Draw the split at the midpoint of the scales used, not at a round number
   chosen after seeing the plot.
5. Prefer relative placement over absolute precision. If two items are nearly
   identical, merge or split them.

## Reading the quadrants

- **Quick wins are not automatically approved.** Low effort can still be
  wrong, and a pile of quick wins can crowd out the big bet.
- **Big bets are not automatically funded.** They need a staged probe and a
  kill criterion; the matrix says "worth planning", not "worth all the money".
- **Money pits are the main output.** The quadrant exists to make the kill
  decision explicit and to record why.
- **Fill-ins should be batched.** Doing them one at a time is how they consume
  a quarter's attention without moving a metric.

## Common distortions

- **Effort optimism** — estimates made by the item's author or champion.
  Have someone outside the proposal score effort.
- **Impact inflation** — every item claims to be strategic. Force a ranking:
  "if only three can be high impact, which three?"
- **Sunk-cost scoring** — a project already underway gets effort discounted.
  Score the remaining cost, not the money already spent.
- **False precision** — 4.2 vs 3.9 on a subjective scale is not a decision.
  Treat differences under one point as a tie.
- **Quadrant drift** — moving the split line to rescue a favourite. Fix the
  split before plotting.

## Relation to ICE

Impact–Effort is fast and visual, good for a room. ICE adds a confidence
dimension and a finer scale, good for a ranked backlog with data. Use the
matrix to triage, ICE to order the shortlist. See
[ice-scoring.md](ice-scoring.md).
