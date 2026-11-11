# Facilitation

A prioritization session is two passes with different social rules: a silent,
equal-ballot preference pass, then an explicit, evidence-facing criteria pass.
Keep them apart. Most failures come from letting the second pass become a
second campaign.

## Before the session

- **Freeze the item set.** Cluster and deduplicate during divergence; the
  session does not vote on raw sticky notes. Aim for 6–30 comparable items.
- **Write the decision question.** "Which three experiments do we run next
  quarter within two engineers and no new budget?" A vague question produces
  a vague ranking.
- **State the constraints.** Money, people, time, regulatory limits, and any
  hard vetoes. A vote that ignores a hard constraint is theatre.
- **Assign roles.** Facilitator (does not champion an item), timekeeper,
  ballot collector, and a scribe for the decision record.
- **Publish the rules.** Budget, per-item cap, scoring anchors, and the fact
  that votes are input rather than the final decision.

## Session script (90 minutes for ~18 items)

| Time | Step | Notes |
|---|---|---|
| 0–10 | Frame | Decision question, constraints, what happens after |
| 10–25 | Neutral read-out | One sentence per item; authors do not pitch |
| 25–30 | Clarify | Questions only; park advocacy in a "concerns" list |
| 30–40 | Silent dot vote | Budget stated; ballots collected before counting |
| 40–50 | Tally and break | Publish raw totals and voter count |
| 50–65 | Impact–Effort scoring | Anchors visible; independent scores first |
| 65–75 | Plot and discuss | Quadrants; check surprises, not every item |
| 75–85 | ICE on the shortlist | Only items still in contention |
| 85–90 | Decisions and probes | Owner, probe, signal, review date |

Shorter versions are fine. Skipping the written decision record is not.

## Running each pass

### Ballot pass

1. Read the budget and per-item cap aloud.
2. Read items neutrally; no "this one is obviously great".
3. Clarifying questions only. Anything persuasive goes on a parking list.
4. Vote silently, in parallel, on paper or a locked poll.
5. Collect all ballots before showing any count.
6. Publish totals with the number of voters. Show the distribution, not just
   the winner.

### Scoring pass

1. Put the anchors on the wall or screen.
2. Score independently and silently first.
3. Reconcile only large disagreements; ask for the evidence behind the score.
4. Record the final score and whether it is data, estimate, or guess.
5. Do not let a champion score their own item's effort alone.

## Handling dissent

Dissent is data. Record it even when the decision is clear.

- Ask explicitly: "What is the strongest case against the top item?"
- Write down the opposing case and who raised it, without softening it.
- If dissent is about a fact, assign a probe to settle it.
- If dissent is about values or risk appetite, name it as such; a vote cannot
  resolve a values disagreement.
- Do not require consensus. A recorded decision with a named dissenter is
  healthier than false unanimity.

## Decision record

One row per item, including kills:

```
ID | item | votes | impact | effort | ICE | decision | reason | dissenter | owner | probe | signal | review date
```

- **keep** — funded for the next stage, with a probe.
- **pivot** — the underlying need survives; the current form does not. Say
  what changes.
- **kill** — not now, with a revival trigger ("revisit if churn exceeds 8%").
- **park** — waiting on a named dependency or evidence.

Publish the record where the team works. The most valuable column is `reason`
for killed items; it stops the same idea returning every quarter with no
memory.

## Remote and async

- Use one board with stable item IDs and a visible budget.
- Lock the ballot at a stated time; no votes after the tally starts.
- Keep the scoring sheet and the ballots separate so votes do not anchor
  scores.
- Publish results and the decision record in the same message; do not trail
  the ranking without the rationale.
- Async ballots are easy to campaign in side channels. Ask voters to submit
  before reading others' totals, and treat coordinated blocs as a signal to
  investigate, not a result to accept.
- Run a short synchronous reconciliation for anything within one standard
  deviation of the cut line; that is where the ranking is least reliable.

## Anti-hero-bias checklist

- Seniority does not buy dots.
- The item's author does not present it last with a pitch.
- Silent ballots before any tally is visible.
- Independent scores before discussion.
- Dissent is recorded, not smoothed.
- The constraint is applied after the vote, transparently, with a note on
  which items it removed.
