# Sampling and Scoring — Coverage-First

## Counting the space

Multiply options per dimension: D1 × D2 × ... × Dn. Note the raw total and the pruned total separately. If raw > ~500, plan to sample rather than score exhaustively.

## Coverage-first sampling

Rather than reading rows top to bottom, ensure coverage:

- Every option appears at least once in the shortlist.
- Include: the baseline combination, the extremes (all low / all high), and the likely sweet spot.
- Add one "cheap-and-strange" combination that survived pruning.

For ~100 combinations or fewer, scoring all is reasonable; above that, sample.

## Scoring criteria

Fix 3-5 criteria during intake (before scoring), weighted and defined:

- Common set: feasibility, user value, cost, time to probe, strategic fit.
- Keep the raw combination beside each score — the combination is the hypothesis, the score is judgment.
- Keep a safe, an ambitious, and a cheap-and-strange candidate in the portfolio regardless of scores to preserve variety.

## From scored combinations to concepts

Turn the strongest scored rows into 1-2 sentence concepts with a concrete mechanism — do not present the matrix as the deliverable.
