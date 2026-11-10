# Clustering Failure Causes by Mechanism

A raw inversion list is long and redundant. Clustering turns it into a small number of causal stories, each of which can be negated into a principle. Cluster by **how the failure happens**, never by where it happens in the org or the project plan.

## Why not cluster by department or phase

Grouping by "marketing / product / support" or "launch / grow / retain" tells you who might fix things, not why they break. The same mechanism often appears in several phases, and one department can host three unrelated mechanisms. Mechanism clusters survive reorgs; departmental clusters do not.

## Procedure

1. **Spread the routes out.** One route per line, verbatim, with an ID (F1, F2, …). Do not rewrite during sorting.
2. **Merge synonyms.** Two routes with the same mechanism and actor are one route; keep the sharper wording.
3. **Sort by causal mechanism.** Ask of each pair: *would fixing one plausibly fix the other?* If yes, same cluster. If they merely co-occur, keep them apart.
4. **Name each cluster with a causal story** in one sentence, in the form "⟨actor/condition⟩ → ⟨behaviour⟩ → ⟨outcome⟩." "Activation has no owner → drop-off is never reviewed → users churn before value" is a cluster. "Onboarding issues" is a bucket.
5. **Count.** Expect **3–6 clusters** from 15–25 routes. More than 6 usually means you are clustering by symptom; fewer than 3 usually means one mechanism has swallowed the list.
6. **Check coverage.** Does the set include at least one route from incentive, information, ownership, capability, and environment? Missing domains are blind spots, not evidence of safety.
7. **Rank only now.** Frequency of mention is a weak signal; a route mentioned once can be the load-bearing one. Use severity and reachability instead of vote counts.

## Distinguish mechanism from trigger

- **Mechanism** — the standing condition that makes failure likely: "no one owns activation."
- **Trigger** — the event that makes it fail now: "the launch doubles signup volume."

A cluster is a mechanism. Triggers belong inside the causal story, and they matter later for signals. If a cluster is named after a trigger ("the migration"), rewrite it as the condition the trigger exposes.

## Merge, split, or discard

| Situation | Action |
|---|---|
| Two clusters share the same actor, condition, and outcome | Merge; keep the sharper causal story |
| One cluster contains routes with different fix types | Split by mechanism, even if the same team owns both |
| A route is the goal restated ("we fail because we don't succeed") | Discard or push upstream |
| A route is a solution in disguise | Rewrite as the absent condition; then cluster |
| A cluster has one route and no plausible fix | Keep it, mark speculative, and revisit at probe time |

## Output format

For each cluster record:

- **ID and name** — short, mechanism-flavoured ("unowned activation").
- **Causal story** — one sentence, actor → behaviour → outcome.
- **Member routes** — the F-IDs, with the strongest wording kept.
- **Coverage note** — which domain(s) it draws from.
- **Evidence status** — observed, inferred, or speculative.
- **Candidate principle direction** — one phrase, not the full principle yet.

This record is the input to the principles step; it should be possible to write each principle without reopening the raw list.

## Traps

- **Symptom clustering** produces tidy groups that all invert into the same advice.
- **Superclusters** ("culture") absorb everything and yield no testable principle.
- **Single-route clusters** are allowed, but mark them: they may be the most important or the least grounded.
- **Voting** rewards familiar risks. Ask which cluster, if unaddressed, would make the others irrelevant.
- **Premature prioritization** during clustering hides low-frequency, high-severity mechanisms.
