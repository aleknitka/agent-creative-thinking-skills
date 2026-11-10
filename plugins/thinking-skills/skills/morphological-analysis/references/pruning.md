# Pruning — Compatibility and Feasibility Filters

## Pairwise compatibility matrix

For every pair of options across different dimensions, mark incompatible pairs (cannot coexist). Record a reason for each incompatibility — the reason is a finding about the problem, not lost work.

Table shape: rows are options from one dimension, columns are options from another. Mark X where incompatible, with a short note: physics, law, budget, capability, brand, or mutual exclusion.

Example: if D1 "trigger = invite" and D2 "channel = paper letter" coexist they are compatible; "trigger = real-time event" with "channel = batch email" is incompatible due to timing.

## Feasibility filters (applied after pairwise pruning)

- Law and regulation.
- Budget and headcount.
- Technical capability in the current window.
- Brand and channel constraints.

Apply each filter uniformly; if a filter removes more than half the space, it may be too aggressive — split or relax it.

## Audit trail

- Keep the raw space size beside the pruned size (e.g., 240 → 38 viable = 84% pruned).
- For each removed pair, one-line reason; a reviewer should be able to reverse any decision from the note.
- Do not prune on preference — score taste later.
