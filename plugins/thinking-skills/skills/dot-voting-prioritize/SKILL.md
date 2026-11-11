---
name: dot-voting-prioritize
description: Prioritize a large idea set with structured dot voting plus Impact–Effort mapping and ICE scoring, then record keep/pivot/kill decisions and probes. Use when too many ideas compete for attention, when the group needs a visible and defensible ranking, or when loud voices and seniority are steering choices instead of evidence — gives anti-hero-bias prioritization with a recorded decision trail.
---

# Dot Voting + Impact–Effort/ICE

Turn a crowded idea set into a small, defensible list of bets. Dot voting makes group preference visible and bounded; Impact–Effort and ICE add explicit criteria so the ranking is not just popularity. The output is a decision record — keep, pivot, or kill — each with an owner and a probe.

The failure mode it prevents is a room that "agrees" on the loudest idea, then cannot say why it was chosen or what it displaced.

## When to use

- More clustered ideas than the team can pursue, and everyone can see the full set.
- The ranking must be visible and traceable — the group will be asked why this and not that.
- A few voices or job titles dominate verbal ranking; anonymous, equal dot budgets help.
- You need a quick first cut now, with honest labels for what is evidence and what is judgment.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- You need a ranking by anonymous experts with controlled feedback → `nominal-group-technique` (NGT/Delphi).
- You need to preserve a mix of safe, ambitious, and exploratory bets → `options-portfolio`.
- The idea set is not yet clustered or deduplicated → cluster during divergence first.
- The decision is a hard constraint, safety issue, or irreversible commitment → a governance process, not a vote.
- You only need to rank issues by severity for one team → a simple criteria table may be cheaper.

## Process

1. **Intake — clustered ideas, one line each.** Freeze generation. Merge duplicates, name each item with a stable ID, and put the whole set on one board. Items must be comparable in scope; split an item that bundles several bets. Write the decision question and the constraint (budget, people, time) at the top. See [references/facilitation.md](references/facilitation.md).

2. **Dot voting round.** Give every voter the same budget — N/3 dots, where N is the number of items, rounded up and capped (typically 1 dot per 3 items; minimum 3, maximum ~12). Voters may put up to a small limit (default 3) on one item. Explain items before voting, then vote silently and in parallel. See [references/dot-voting.md](references/dot-voting.md).

3. **Impact–Effort scoring.** Take the top vote getters plus any item flagged as a risk. Score impact and effort on a shared 1–5 anchor scale; plot the 2×2 (quick wins, big bets, fill-ins, money pits). Voting and scoring are separate passes — do not re-vote while scoring. See [references/impact-effort.md](references/impact-effort.md).

4. **ICE where data exists.** For items that survived the matrix, score Impact, Confidence, and Ease 1–10 against written anchors; ICE = (I + C + E) / 3 (or the product variant, stated openly). Use ICE only where the team can defend the inputs; otherwise leave the item unscored and say so. See [references/ice-scoring.md](references/ice-scoring.md).

5. **Plot and decide — keep / pivot / kill.** Combine votes, matrix quadrant, and ICE into one ranked shortlist of 3–5 items. Record every decision, including kills, with the reason and the dissent. A kill is a decision, not a silence. See [references/facilitation.md](references/facilitation.md).

6. **Assign probes and hand off.** For each kept item, name an owner, the cheapest probe that produces evidence, the signal that means keep or kill, and the review date. Hand off uncertain items to `premortem` or `options-portfolio`; send under-specified items back to divergence. See [references/examples.md](references/examples.md).

`nominal-group-technique`, `options-portfolio`, and this skill are siblings in the convergence family: NGT/Delphi controls expert judgment, options-portfolio preserves variety, dot-voting-prioritize makes a group ranking visible and bounded.

### Solo and async variants

Solo: run the vote as a written preference tally from interviews, keep the dot budget, and mark the result as one person's sample. Async: circulate the frozen item list with the budget and a deadline; collect ballots without discussion; publish totals and the scoring sheet together. Never mix the ballot window with a comment thread — it turns into a campaign.

## Rules

- **Bound the votes.** Same budget for everyone, stated before the first dot; no extra dots for seniority or "just one more".
- **Explain before voting.** Every item gets a short, neutral read-out; no persuasive speeches during the ballot.
- **Vote and score in separate passes.** Do not re-vote to fix an inconvenient matrix.
- **Record dissent.** Name the strongest opposing case and who made it; unanimity that hides disagreement is not a decision record.
- **No revote without new information.** New evidence, a corrected item, or a changed constraint — otherwise the second ballot is just pressure.
- **One item, one bet.** Split bundles before voting; a vote for "platform + hiring + rebrand" means nothing.
- **Label evidence.** Mark scores as data, estimate, or guess; ICE confidence must reflect which.
- **Kills are recorded.** Every killed item gets a reason and a revival trigger; this prevents the same idea returning every quarter.
- **Votes are input, not the decision.** The ranking is justified by votes + criteria + constraints; a high dot count never overrides a hard constraint.

## Going deeper

- Dot-voting rules, N/3 budget, color dots, anti-gaming: [references/dot-voting.md](references/dot-voting.md)
- Impact–Effort matrix and anchors: [references/impact-effort.md](references/impact-effort.md)
- ICE scoring, calibration, and variants: [references/ice-scoring.md](references/ice-scoring.md)
- Facilitation script, dissent, remote and async: [references/facilitation.md](references/facilitation.md)
- Worked example (18 ideas → vote → matrix → top 3): [references/examples.md](references/examples.md)
- When not to use + handoff map: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and evidence limits: [references/provenance.md](references/provenance.md)
- Offline scorer and ballot planner: [scripts/vote.py](scripts/vote.py)
- Shared workspace — sticky notes, lanes, drawing, votes: [workspace/index.html](../../../../workspace/index.html)
