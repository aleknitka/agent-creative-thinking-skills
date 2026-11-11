# Worked Example — 18 Ideas → Vote → Matrix → Top 3

**Decision question:** Which onboarding experiments do we run next quarter with
two engineers, no new budget, and no changes to auth?

**Input:** 18 clustered ideas from a brainwriting session (raw set had 61
notes). Six voters, six dots each (N/3 = 6), max 3 dots per item. All names are
illustrative.

## 1. Ballot

| ID | Item | Dots |
|---|---|---|
| A1 | Guided setup checklist | 5 |
| A5 | Invite a teammate during setup | 4 |
| A2 | Onboarding progress bar | 3 |
| A3 | Pre-filled sample data | 3 |
| A6 | Template gallery | 3 |
| A9 | Let users skip optional steps | 3 |
| A12 | Import existing data from CSV | 3 |
| A15 | Interactive product demo | 3 |
| A18 | Concierge onboarding for top accounts | 3 |
| A11 | SSO setup wizard | 2 |
| A4 | 90-second video tour | 1 |
| A7 | Day-2 email nudge | 1 |
| A10 | Personalized path by role | 1 |
| A14 | Role presets | 1 |
| A8 | In-app chat | 0 |
| A13 | Mobile-specific onboarding | 0 |
| A16 | Public onboarding API | 0 |
| A17 | Gamified badges | 0 |

36 dots allocated, 6 voters, no abstentions. The tally was published before
any discussion of scores. Note that A18 is mid-table on votes but high on
impact — votes are input, not the decision.

## 2. Impact–Effort (1–5, impact ≥4 = high, effort ≥3 = high)

| ID | Impact | Effort | Quadrant |
|---|---|---|---|
| A1 | 4 | 2 | Quick win |
| A12 | 4 | 2 | Quick win |
| A5 | 4 | 3 | Big bet |
| A11 | 4 | 3 | Big bet |
| A15 | 4 | 4 | Big bet |
| A18 | 5 | 5 | Big bet |
| A2 | 3 | 1 | Fill-in |
| A3 | 3 | 2 | Fill-in |
| A6 | 3 | 2 | Fill-in |
| A9 | 3 | 1 | Fill-in |
| A14 | 3 | 2 | Fill-in |
| A7 | 2 | 2 | Fill-in |
| A4 | 2 | 3 | Money pit |
| A10 | 3 | 3 | Money pit |
| A8 | 2 | 4 | Money pit |
| A13 | 3 | 4 | Money pit |
| A16 | 3 | 5 | Money pit |
| A17 | 2 | 4 | Money pit |

The fill-ins are deliberately not promoted just because they are cheap; the
constraint is two engineers, so spare capacity is not real.

## 3. ICE on the contenders

ICE average = (Impact + Confidence + Ease) / 3, all 1–10.

| ID | I | C | E | ICE | Evidence note |
|---|---|---|---|---|---|
| A12 | 8 | 8 | 7 | 7.7 | Funnel data shows import drop-off |
| A1 | 8 | 7 | 8 | 7.7 | Prior test in another segment |
| A9 | 6 | 7 | 9 | 7.3 | Analytics only; untested |
| A2 | 6 | 7 | 9 | 7.3 | Convention, weak local data |
| A5 | 8 | 6 | 6 | 6.7 | Analogous social proof result |
| A3 | 6 | 6 | 8 | 6.7 | Interviews, small sample |
| A18 | 9 | 7 | 2 | 6.0 | Account data; high-touch cost |
| A15 | 8 | 5 | 3 | 5.3 | Vendor claim only |
| A11 | 7 | 5 | 4 | 5.3 | Enterprise requests, no sizing |

ICE re-orders but does not overturn the matrix: A18 remains a big bet with low
ease, and A15 is parked until A3 or A2 produces evidence.

## 4. Decisions

| ID | Decision | Reason | Dissent / note |
|---|---|---|---|
| A12 | **Keep** — probe | Quick win, high confidence, direct funnel evidence; one-week build | None recorded |
| A1 | **Keep** — probe | Quick win, strong vote, cheap to test against A12 | "Checklist may duplicate progress bar" — R.M. |
| A18 | **Pivot** — staged probe | High impact but effort 5; run concierge for 10 accounts, not all | Sales wanted full rollout; recorded |
| A5 | **Park** | Big bet; needs a dependent share-permission change | Revisit after A1 results |
| A2 | **Park** | Fill-in; do alongside A12 if the progress component is already touched | — |
| A15 | **Kill for now** | Vendor claim only, effort 4; revive if demo request volume exceeds 20/month | — |
| A4, A8, A10, A13, A16, A17 | **Kill** | Money pits; low votes, low impact, high effort | Reasons recorded; revival triggers set |
| A3, A6, A9, A11, A14 | **Park** | Fill-ins or dependent big bets; batch with a kept item | A9 dissent: "we should test skip first" — J.L. |

## 5. Probes and handoff

| Item | Owner | Probe | Keep signal | Review |
|---|---|---|---|---|
| A12 | P.K. | CSV import on 10% of new accounts | ≥15% lift in activation; no support spike | 3 weeks |
| A1 | R.M. | Checklist for half of new accounts | ≥10% lift; not worse with sample data | 3 weeks |
| A18 | Sales + eng | Concierge for 10 accounts, manual | ≥3 of 10 convert to paid within 30 days | 6 weeks |

The unkept items go to the idea bank with their revival triggers. The decision
record — not just the ranking — is the artifact that survives the meeting.
