# Worked Example — 12 Ideas to a Ranked Top 3

The numbers below are invented to show the record format. Do not cite them as
findings.

## The setup

A B2B SaaS company has a week-1 activation drop: 38% of new accounts never
complete setup. The decision owner is the VP of Product; two engineers are
available for one quarter; pricing and sales cannot change.

**Ranking question:** "Which three onboarding changes should we pilot next
quarter to raise week-1 activation, given two engineers and no pricing
changes?"

Twelve items were generated in an earlier divergence pass and frozen with IDs.
Eight voters take part: product (P1, P2), engineering (E1, E2), support (S1,
S2), sales (L1), and the decision owner (D1).

## Draft items

| ID | Item |
|---|---|
| I1 | Ask role and goal on the invite, then tailor the first screen |
| I2 | Delay the first onboarding email by 24 hours |
| I3 | Put a 90-second inline demo in the first session |
| I4 | Remove the tutorial entirely and rely on tooltips |
| I5 | Add SMS fallback for account verification |
| I6 | Show a progress bar in the setup checklist |
| I7 | Offer a one-click template that pre-fills the workspace |
| I8 | Add an in-app checklist with three steps |
| I9 | Show a peer's example artifact in the empty workspace |
| I10 | Pre-configure the workspace from the role selected at signup |
| I11 | Have a success manager send a timed nudge on day two |
| I12 | Offer concierge onboarding to the top 20 accounts |

## Session record

Silent generation took 10 minutes. The round-robin produced 12 items in 14
minutes, with no merges. Clarification established that I3 and I10 share front-
end work, I7 is mostly configuration, and I12 is out of scope for the quarter
because it needs a success-manager hire. I12 stayed on the ballot — scope
concerns are for the discussion, not for the facilitator to delete.

Voting used 5-4-3-2-1 across the top five. Preliminary ballot: I3 31, I1 30,
I10 27, I7 18, rest below 10. Discussion clarified that the inline demo (I3)
could reuse an existing recording, cutting its estimate from six weeks to two;
one voter moved I3 from fourth to first on the final ballot. Final tally:

| Rank | ID | Item | Points | First-place | Last-place |
|---|---|---|---|---|---|
| 1 | I1 | Role-and-goal intake | 35 | 4 | 0 |
| 2 | I3 | Inline 90-second demo | 30 | 2 | 0 |
| 3 | I10 | Role-based pre-configuration | 29 | 2 | 0 |
| 4 | I7 | One-click template | 15 | 0 | 0 |
| 5 | I8 | In-app checklist | 4 | 0 | 1 |
| 6 | I9 | Peer example artifact | 3 | 0 | 0 |
| 7 | I2 | Delay first email | 1 | 0 | 0 |
| 8 | I5 | SMS verification fallback | 1 | 0 | 0 |
| 9 | I6 | Setup progress bar | 1 | 0 | 0 |
| 10 | I12 | Concierge onboarding | 1 | 0 | 0 |
| 11 | I4 | Remove the tutorial | 0 | 0 | 3 |
| 12 | I11 | Day-two success-manager nudge | 0 | 0 | 2 |

The top three are **I1, I3, I10**. The cut is clean on points, but I3 and I10
are one point apart and I10 received two first-place votes — record that as a
near-tie, not a settled gap.

## Dissent log

| Item | Decision | Objection | Basis | Held by | Revisit trigger |
|---|---|---|---|---|---|
| I10 | Selected (3rd) | "Role-based setup assumes buyers know the role; agencies sign up with mixed roles. It may help enterprises and hurt the long tail." | Segment assumption, no data by account type | Sales and one product voter | Split activation results by self-serve vs sales-led after the pilot |
| I7 | Not selected | "The template is cheaper than I3 and gets a working artifact in front of the user on day one." | Implementation estimate, not a value judgment | Two engineering voters | If I3's recording cannot be produced in two weeks, fund I7 instead |
| I3 | Selected (2nd) | "Demo length is not the problem; the empty workspace after the demo is." | Support ticket themes | Support voter | Review empty-workspace tickets during the pilot |
| I4 | Not selected | "Removing the tutorial would at least stop people clicking through without reading." | Observation from session recordings | One support voter | If setup completion rises but week-2 retention does not, revisit |

The I4 objection is recorded even though the item scored zero points: it names
a real failure mode of the top items ("completion without comprehension") that
the shortlist does not address.

## Handoff

- **I1, I3, I10** go to `options-portfolio` as one package with a shared
  success metric: week-1 activation, measured against a four-week baseline.
- **I1** gets a `premortem` before build because it changes the signup flow and
  implicates legal review of role data.
- **I7** stays on the shelf with an explicit revival trigger, not as an
  unrecorded runner-up.
- **I12** is returned to scoping: it is a staffing decision disguised as an
  onboarding experiment.

## What made the record usable

- The question named the outcome, the constraint, and the horizon.
- Items were frozen and comparable; duplicates were not re-litigated.
- The rule (5-4-3-2-1, top 3) was fixed before the first ballot.
- The preliminary and final votes were both kept; the shift after clarification
  is visible.
- Dissent was recorded per item, with a trigger for reopening.
- The handoff named owners and next actions rather than ending at a ranking.

## Delphi variant — reliability investments

A platform team asks 12 panellists to rate eight reliability investments over
three anonymous rounds. Ratings are 1–5; the stopping rule is three rounds or
IQR ≤ 1 on 80% of items. Response rates were 12/12, 11/12, and 10/12; the report
includes those denominators.

| ID | Investment | R1 median | Final median | Final IQR | Within ±1 |
|---|---|---|---|---|---|
| D1 | Automated postmortem follow-ups | 3.0 | 4.0 | 1.0 | 70% |
| D2 | Explicit error-budget policy | 4.0 | 5.0 | 1.0 | 80% |
| D3 | Cap on-call load per engineer | 3.0 | 3.0 | 2.5 | 60% |
| D4 | Quarterly chaos drills | 2.0 | 2.0 | 1.0 | 80% |
| D5 | Buy a managed status page | 3.0 | 3.0 | 1.0 | 80% |

Top two: **D2, D1**. D3 remains genuinely split: the median did not move, the
IQR stayed wide, and only 60% of ratings were within ±1 of the median.
The correct report says "the panel did not converge on on-call load; the
distribution is bimodal between engineers and managers" and includes the
anonymised reasons. It does not average the split into a false middle and call
it consensus.

D1 moved from 3 to 4 after two panellists cited repeated incident recurrence in
their reason comments. That movement is recorded, alongside the fact that the
facilitator did not add a sponsor argument to the feedback pack.
