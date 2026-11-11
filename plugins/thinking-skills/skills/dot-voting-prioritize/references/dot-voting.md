# Dot Voting

Dot voting (also called dotmocracy, sticky-dot voting, or multi-voting) gives
each participant a fixed number of marks to distribute across a visible set of
options. The constraints are the method: equal budgets, silent ballots, and a
public tally. Speed is a side effect, not the goal — the goal is a preference
signal that cannot be bought with meeting airtime.

## Why the budget matters

An unlimited "raise your hand for the ones you like" produces a long list and
no ranking. A fixed budget forces tradeoffs: spending a dot here means not
spending it there. The scarcity is what creates information.

## The N/3 rule

A common starting budget is one dot per three options:

```
dots_per_voter = max(3, ceil(number_of_options / 3))
```

Then cap total dots per voter (e.g. 12) so a 90-item board does not produce an
unreadable tally. Examples:

| Options | N/3 | Practical budget |
|---|---|---|
| 9 | 3 | 3 |
| 18 | 6 | 6 |
| 30 | 10 | 10 |
| 60 | 20 | 12 (cap) |
| 6 | 2 | 3 (minimum) |

Adjustments:

- **More options than people can read** — cluster first. N/3 is not a reason
  to vote on 200 sticky notes.
- **High-stakes shortlist** — reduce the budget (3–5 dots) to sharpen the top.
- **Portfolio breadth desired** — allow at most 1 or 2 dots per item; this
  spreads support instead of concentrating it.
- **Single-winner decision** — use a different method; dot voting is for
  shortlisting, not for picking one option under adversarial stakes.

State the budget and the per-item cap *before* the first dot. Changing either
mid-ballot invalidates the comparison.

## Color dots

Colors add a second dimension without a second ballot. Common encodings:

- **One color = support.** Simplest and least gameable.
- **Green = do it, red = concern/risk.** Voters may assign red dots to flag
  blockers; red dots subtract from or annotate the total. Publish the rule.
- **Three colors = keep / explore / kill.** Useful after a first ranking to
  separate "strong yes" from "interesting but not now".
- **Color per voter.** Makes coalition patterns visible; useful in small
  groups, but it removes anonymity and increases politics.

Pick one encoding and write it on the board. Mixed color semantics are the
most common way a dot vote becomes unusable.

## Running the ballot

1. Display every item with its ID and a one-sentence neutral description.
2. Read the items aloud (or have authors read them) with no advocacy.
3. Answer clarifying questions; park persuasive arguments.
4. Hand out the budget; allow multi-dot up to the stated cap.
5. Vote silently and in parallel — paper dots, board stickers, or a poll tool.
6. Collect ballots before counting. Do not count live if late dots can change.
7. Publish raw totals and the number of voters.

## Anti-gaming

- **No proxy voting.** One ballot per participant; absent stakeholders are
  represented in a separate, clearly labelled consultation, not by extra dots.
- **No trading visible.** "I'll dot yours if you dot mine" is coalition
  building, not prioritization. Silent ballots and simultaneous collection
  reduce it; they do not eliminate it in a recurring group.
- **No serial advocacy.** A short neutral read-out per item; the author of an
  item does not get a closing pitch.
- **No escalating budgets.** If the first result is inconvenient, the fix is
  new information or a changed constraint, not more dots.
- **Watch concentration.** If one item takes most dots, check whether voters
  coordinated or whether the item is genuinely dominant. Ask, do not assume.
- **Name the missing voices.** A vote among five engineers on a user-facing
  feature is a preference sample, not user evidence.

## Reading the result

- **Clear top cluster** — carry those items into scoring; they have earned a
  closer look, not automatic approval.
- **Flat distribution** — the item set may be too broad, or the group lacks a
  shared frame. Cluster or clarify before re-voting.
- **High abstention / many unused dots** — items may not be understood, or
  people do not feel entitled to choose. Fix comprehension and permission
  before treating the tally as signal.
- **One item dominates** — check for a hard constraint or a shared assumption;
  a dominant item may be the only one that fits the real budget.

## Relation to other methods

- Dot voting ranks *group preference*. NGT/Delphi ranks *expert judgment* with
  anonymity and controlled feedback. Do not use dots when the risk is
  conformity pressure from a few experts.
- Dot voting shortlists. `options-portfolio` decides *which mix* to keep, and
  Impact–Effort/ICE decides *what to do first*. A vote that ends with a single
  winner has skipped the portfolio question.
