---
name: nominal-group-technique
description: Run Nominal Group Technique — silent write → round-robin share → clarify → vote — and its async cousin Delphi for anonymized expert consensus. Use when ideas need credible, bias-resistant ranking, hierarchy would distort open discussion, or you need a traceable decision with dissent logged — not just a vote.
---

# Nominal Group Technique (NGT) + Delphi

Rank credibly by never debating before writing. NGT holds the group in the same room but keeps minds separate until harvest; Delphi keeps minds separate across rounds and rooms so expertise — not rank — drives convergence.

The failure mode it prevents is the premature consensus where the first proposal to sound reasonable wins because critique and ranking are tangled with generation.

## When to use

- A decision needs ranking among 8–20 candidates and the group must visibly own the result.
- Hierarchy or expertise gradients would distort open discussion (whoever speaks first sways the group).
- You need a traceable record — who proposed what, how votes fell, what dissent remains — for later audit or handoff.
- Async expertise is available but co-located time is scarce → run Delphi.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- You need divergence, not convergence → `brainwriting`, `forced-connections`, or `crazy-eights`.
- A quick preference signal is enough → `dot-voting-prioritize` (lighter).
- The question is still vague → `question-storming` before any ranking.

## Process

1. **Intake — frame one question.** State the decision as a single ranking question with constraints and voter set. NGT: same-time room; Delphi: anonymized rounds. See [references/procedure.md](references/procedure.md).

2. **Silent generation.** NGT 10 min silent write — one idea per line, no talking. Delphi round 1 — anonymous proposals collected centrally. No evaluation yet. See [references/procedure.md](references/procedure.md).

3. **Round-robin share.** NGT: each person reads one idea in turn until exhausted; scribe records verbatim. No discussion during the circle. Delphi: facilitator circulates the aggregated, de-identified list. See [references/procedure.md](references/procedure.md).

4. **Clarify and cluster.** Group duplicates, clarify wording, merge only with author consent. Do not judge or rank while clustering. See [references/procedure.md](references/procedure.md).

5. **Vote and rank.** Each voter distributes votes: the common NGT ballot is 5-4-3-2-1 across a top 5, or N/3 dots; Delphi uses median/IQR feedback between rounds. Tally visibly. See [references/voting.md](references/voting.md) and [scripts/ngt.py](scripts/ngt.py).

6. **Log dissent and handoff.** Record top-ranked items, vote spread, and explicit dissent (who disagrees and why). Hand off to `options-portfolio` (package into bets) or `premortem` (stress-test the winner). See [references/examples.md](references/examples.md).

## Rules

- Write before you speak — every idea is written before any discussion.
- Generation is evaluation-free — no praise, criticism, or "we tried that" until every idea is recorded and clarified.
- One idea per turn in round-robin; no piggy-backing.
- Clarification only — "what do you mean?" is allowed; "that won't work" is not until after voting.
- Agree the aggregation rule, shortlist size, and consensus threshold before round 1; never move them after seeing the tally.
- Delphi anonymity is real — no attribution across rounds.
- Dissent is part of the record — name the strongest objection and its basis, not just the objector.
- Votes are traceable but not weaponizable — tallies shown, dissent named, coercion forbidden.
- Label fact / assumption / speculation; ranking is preference, not evidence.
- Honest provenance: attribute NGT to Delbecq & Van de Ven (1971), Delphi to Dalkey & Helmer (RAND); call this workflow an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- NGT/Delphi procedure — timing, question framing, room vs async: [references/procedure.md](references/procedure.md)
- Facilitation — anti-anchoring, scribe discipline, virtual boards: [references/facilitation.md](references/facilitation.md)
- Voting and aggregation — 5-4-3-2-1, N/3, Delphi median/IQR: [references/voting.md](references/voting.md)
- Worked example (12 ideas → ranked 3 + dissent log): [references/examples.md](references/examples.md)
- When not to use — triage vs dot-voting/brainwriting/portfolio: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Ranking helper (offline): [scripts/ngt.py](scripts/ngt.py)
- Shared workspace — sticky notes + lanes: [workspace/index.html](../../../../workspace/index.html)
