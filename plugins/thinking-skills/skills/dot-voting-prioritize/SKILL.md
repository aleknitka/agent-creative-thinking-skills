---
name: dot-voting-prioritize
description: Prioritize visibly with structured dot voting (N/3 dots, at-most-one-per-item), then score top items on an Impact–Effort matrix and optional ICE — to turn many ideas into keep/pivot/kill with owners. Use when you have 10+ candidates needing quick, bias-resistant ordering, or portfolio/pitch decisions need a defensible shortlist — not a statistical ranking.
---

# Dot Voting + Impact–Effort

Make preference visible and effort honest. Dots turn silent preference into a countable map; impact–effort turns the map into a next-move (quick wins, strategic bets, fill-ins, avoid). ICE sharpens where data exists.

The failure mode it prevents is the polite meeting where everything is "good" and nothing is chosen, or where the HiPPO picks after a vague show of hands.

## When to use

- You have 10–30 candidates (clusters or raw ideas) and need a visible shortlist in minutes.
- Open voting would bias toward senior voices or groupthink.
- Portfolio or pitch needs a defensible keep/pivot/kill with a plot, not just a list.
- You have impact/effort signals but not enough data for formal scoring.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- Need credible, anonymized expert ranking with dissent traceable → `nominal-group-technique` (NGT/Delphi).
- Need to package options into bets first → `options-portfolio`.
- Need divergence, not convergence.

## Process

1. **Intake — clustered items.** Start from already-clustered items (ideally from lotus-blossom / brainwriting / morph box). Display one item per sticky, no advocacy yet. See [references/facilitation.md](references/facilitation.md).

2. **Dot vote — N/3 dots, at-most-one-per-item.** Each voter gets floor(N_items/3) dots (e.g., 18 items → 6 dots). Dots placed simultaneously, at most one per item per voter. No discussion during voting. See [references/dot-voting.md](references/dot-voting.md) and [scripts/vote.py](scripts/vote.py).

3. **Impact–Effort score the top.** For top-voted items, score impact (1–5) and effort (1–5, where 5 = hardest) as a pair; plot in 2×2: quick wins (high impact/low effort), strategic (high/high), fill-ins (low/low), avoid (low/high). See [references/impact-effort.md](references/impact-effort.md).

4. **ICE where data exists.** For items with evidence, score Impact/Confidence/Ease each 1–10; ICE = (I×C×E)/100 or simple sum — use one formula consistently. See [references/ice-scoring.md](references/ice-scoring.md).

5. **Plot and decide keep/pivot/kill.** Place topped items on the board matrix; announce keep (do next), pivot (reshape), kill (stop). Record dissent — one sticky per objection. See [references/examples.md](references/examples.md).

6. **Probe assignment and handoff.** For keeps, assign owner + next-day/week probe. Handoff to `premortem` for keeps before commitment, or to `options-portfolio` to bundle. See [references/examples.md](references/examples.md).

## Rules

- Votes limited — N/3 is the ceiling; scarcity is the point.
- At most one dot per item per voter — no stacking to game the count.
- Simultaneous reveal — no sequential persuasion.
- Impact and effort are paired — scoring one without the other overranks easy filler.
- Dissent is recorded, not resolved — one sticky per objection with a name.
- No revote without new information — a second vote needs new data or a new framing.
- Label fact / assumption / speculation; dot count is preference, not truth.
- Honest provenance: dot voting is a facilitation technique (common-practice); impact–effort and ICE are practitioner frameworks — see references. See [references/provenance.md](references/provenance.md).

## Going deeper

- Dot voting — N/3 rule, simultaneity, anti-gaming: [references/dot-voting.md](references/dot-voting.md)
- Impact–Effort matrix — scoring and 2×2 reading: [references/impact-effort.md](references/impact-effort.md)
- ICE scoring — when and how to use it: [references/ice-scoring.md](references/ice-scoring.md)
- Facilitation — lanes, virtual reveal, timebox: [references/facilitation.md](references/facilitation.md)
- Worked example (18 ideas → 6 dots each → matrix → keep 3): [references/examples.md](references/examples.md)
- When not to use — triage vs NGT/portfolio/brainwriting: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Voting helper (offline): [scripts/vote.py](scripts/vote.py)
- Shared workspace — dot overlay: [workspace/index.html](../../../../workspace/index.html)
