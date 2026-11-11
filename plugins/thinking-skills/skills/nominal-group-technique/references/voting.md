# Voting and Aggregation — Rules That Survive Scrutiny

A ranking is only as credible as the aggregation rule. Decide the rule, the
shortlist size, and the tie-break before the first ballot, then apply them
without adjustment. If the rule has to change because the result is
inconvenient, that is a new decision and needs a recorded reason.

## Choosing the rule

| Rule | Ballot | Best for | Main risk |
|---|---|---|---|
| Ranked 5-4-3-2-1 | Rank the top five; points 5,4,3,2,1 | 8–20 comparable items; a clear shortlist | Items below fifth get no signal; points are ordinal |
| N/3 dots | Distribute N/3 dots, capped per item | Larger sets; fast visible convergence; mixed familiarity | Popularity can beat judgment; dot counts are coarse |
| Delphi 1–5 ratings | Rate every item privately, repeat with feedback | Dispersed experts; contentious or uncertain items | Consensus can be manufactured by leading feedback |

All three produce a **preference ordering**, not a measurement of value. Do not
report a difference of one point or one dot as if it were a meaningful effect.

## Ranked vote — 5-4-3-2-1

Each voter ranks items and the top five receive 5, 4, 3, 2, 1 points. Sum the
points across voters; highest total ranks first. If there are fewer than five
items, start at 5 and descend through the available positions.

Example ballot: `I7, I2, I9, I1, I12` → I7 +5, I2 +4, I9 +3, I1 +2, I12 +1.

Report per item:

- **Points** — the primary ranking key.
- **First-place votes** — evidence of committed support.
- **Last-place votes** — evidence of active resistance.
- **Number of ballots** — the denominator, including abstentions.

Sorting key: points descending, then first-place votes descending, then stable
ID for determinism. A different secondary key can be agreed in advance, but it
must not be invented after the tally.

Limits:

- Items outside every voter's top five score zero even if they are everyone's
  sixth choice. With more than about 20 items, use N/3 or a preliminary cut.
- The gap 5–4–3–2–1 is a convention, not a cardinal scale. Do not average
  points across sessions with different item counts.
- Strategic ranking (burying a rival) is possible; secrecy and a culture of
  judgment reduce it but do not eliminate it.

Ties: carry both items forward, or apply the pre-agreed tie-break. Never split
a tie by facilitator preference or by "who seems more senior".

## N/3 dots

Budget per voter:

```
dots = max(3, min(12, ceil(N / 3)))
```

For 12 items each voter gets 4 dots; for 30 items, 10; for 4 items, 3. The cap
keeps the ballot quick and forces trade-offs. Common variants:

- **Max per item** — usually 1, 2, or 3. A cap of 3 prevents one enthusiastic
  voter from deciding the outcome alone; the script uses 3.
- **Colour dots** — one colour for "must do", another for "exploratory"; tally
  them separately rather than summing unlike things.
- **Negative dots** — avoid. They turn prioritisation into vetoes and punish
  proposals for being visible.

Report per item: total dots and the number of distinct voters who gave at least
one dot. Dots measure intensity; voter count measures breadth. An item with 6
dots from 2 voters is a narrower coalition than one with 6 dots from 6 voters —
record both and discuss the difference.

Limits: dot counts are coarse (a difference of one dot is noise), and visible
dot-stacking creates bandwagons. Use secret ballots or hide the board until all
ballots are in.

## Delphi — median, IQR, and consensus

Ratings use a bounded ordinal scale, usually 1–5, with written anchors:

| Score | Meaning |
|---|---|
| 1 | Strongly oppose /very low priority |
| 2 | Oppose / low priority |
| 3 | Neutral / unsure |
| 4 | Support / high priority |
| 5 | Strongly support / critical |

For each item and round, compute:

- **Median** — the middle rating; resistant to a single extreme score.
- **Q1, Q3** — the 25th and 75th percentiles (linear interpolation for small
  samples is acceptable; state the method).
- **IQR = Q3 − Q1** — dispersion. IQR 0 means the middle half agreed exactly;
  IQR 2 or more means the panel is materially split.
- **Consensus share** — percentage of ratings within ±1 of the median. This is
  a spread indicator, not proof of agreement.
- **High support** — count of 4s and 5s; **low support** — count of 1s and 2s.

Common stopping thresholds, fixed before Round 1:

- at least 70–80% of ratings within ±1 of the median, **and**
- IQR ≤ 1 for the items that matter, **and**
- no median movement greater than 0.5 between consecutive rounds.

Use median rather than mean: one panellist scoring 1 on a 5-point scale can
move a mean enough to look like a trend, while the median stays stable. If you
report a mean, report the distribution beside it.

Do not average ranks as if they were interval data without saying so. "Mean
rank" is a convenience summary; median and IQR are the defensible description
of an ordinal panel.

### Feedback between rounds

Show each panellist: item, own prior rating, group median, IQR, and anonymised
reasons for outliers. Do not show a ranked leaderboard with names, and do not
show how a particular role voted. Feedback is for calibration, not persuasion.

### Reporting the final result

Report an item table: `ID | item | median | IQR | consensus % | n`. Add the
response rate per round and the number of panellists who dropped out. Report
items that remain split as split — an unresolved disagreement is a finding, not
a failure to be smoothed away.

## Ties, cut lines, and dissent

- **Define the cut before voting.** "Top 3" is a rule; "the best ones" is not.
- **Tie at the cut line:** apply the pre-agreed tie-break (for example, higher
  first-place count, lower implementation cost, higher risk reduction), or
  carry the tied items into a separate run-off. Record which rule was used.
- **Do not break ties by discussion alone.** Discussion before the run-off can
  reintroduce the dominance the ballot was meant to remove.
- **Dissent is part of the output.** For every selected item, log the strongest
  objection and its basis. For every near-miss with real support, log why it
  did not make the cut and what would revive it.
- **No revote without new information.** A second ballot after the first result
  is only legitimate if new evidence, a corrected item, or a changed constraint
  is recorded. Otherwise it is pressure with a procedural costume.

## Mapping to the helper script

`scripts/ngt.py` applies exactly these rules to synthetic ballots:

- `--method ranked` implements 5-4-3-2-1, first-place and last-place counts,
  and a cut-line tie warning.
- `--method n3` implements the N/3 budget with a maximum of 3 dots per item.
- `--method delphi` implements 1–5 ratings over rounds, median, IQR, consensus
  share, stability, and split-item warnings.

The seed makes the rehearsal reproducible. The script's numbers are not
evidence: replace the synthetic ballots with real ones before any decision.
