# ICE Scoring

ICE scores an item on three 1–10 dimensions and combines them into one number.
It is a lightweight way to order a shortlist, not a measurement. Its value
comes from forcing three separate questions: does it matter (Impact), can we
believe it will work (Confidence), and how cheap is it to try (Ease).

Originally popularized in growth experimentation as a backlog sorter for tests
and campaigns; it is now used far beyond growth. Keep that origin in mind: it
was designed for many cheap, reversible experiments, not for large irreversible
bets.

## The three dimensions

| Dimension | Question | 1 means | 10 means |
|---|---|---|---|
| Impact | If this works, how much does it move the goal? | barely measurable | changes the trajectory |
| Confidence | How much do we trust the impact estimate? | pure guess | measured or strongly evidenced |
| Ease | How cheap is the test or first version? | multi-quarter, high friction | days, existing tools |

### Impact anchors (1–10)

1–2: cosmetic or local. 3–4: small, one segment. 5–6: clear effect on one
metric. 7–8: large effect on a primary goal. 9–10: changes the plan or the
business. Define the goal before scoring; "impact on what?" must have one
answer for the whole sheet.

### Confidence anchors (1–10)

1–2: intuition only. 3–4: analogy or one anecdote. 5–6: qualitative interviews
or a small internal sample. 7–8: direct data from the target context. 9–10:
measured repeatedly, or a controlled result. Confidence is evidence for the
*impact estimate*, not for the idea being popular.

### Ease anchors (1–10)

1–2: multi-quarter, new capability, approvals. 3–4: a quarter, cross-team.
5–6: a month. 7–8: 1–2 weeks. 9–10: days with existing tools. Ease includes
maintenance and coordination costs.

## Combining the scores

Two common formulas:

```
ICE (average)  = (Impact + Confidence + Ease) / 3
ICE (product)  = Impact × Confidence × Ease
```

- **Average** keeps the 1–10 scale readable, treats dimensions as
  compensating, and is easier to explain.
- **Product** punishes any weak dimension hard; it is more volatile and
  sensitive to a single low score. Use it when all three must be strong, and
  say that you are using it.

Pick one and state it on the sheet. Never compare scores computed with
different formulas.

## Bands

| Average ICE | Typical reading |
|---|---|
| 8–10 | Strong candidate; still needs a probe if confidence is low |
| 6–7.9 | Worth staging; check whether ease or confidence carries it |
| 4–5.9 | Park or reshape; the weak dimension is the work |
| 1–3.9 | Kill or leave in the idea bank |

For the product formula, define bands separately (e.g. under 200 = parked).

## Calibration discipline

1. **Score the dimensions independently**, then discuss. One person scoring
   all three invites halo effects.
2. **Write the anchors down** and keep them visible for the whole session.
3. **Cap confidence by evidence**, not by enthusiasm. If nobody can name the
   data, confidence is at most 5.
4. **Blind the scorer to popularity** where possible. A high vote count is not
   evidence for confidence.
5. **Re-score when evidence changes**, and record the date and reason. Silent
   re-scoring destroys the audit trail.
6. **Do not compare ICE across unrelated goals.** A score is only meaningful
   inside one decision context.

## When ICE misleads

- **Confidence inflation** — teams score belief, not evidence, and the metric
  becomes a confidence contest.
- **Ease dominates** — cheap items rise even when the impact is negligible.
  Check the top of the list for low-impact quick wins.
- **False comparability** — averaging subjective 1–10 judgments yields a
  precise-looking decimal that overstates certainty.
- **Irreversible bets** — a high ICE score is not a risk assessment. Send
  irreversible or safety-critical items to `premortem` instead.
- **One-shot strategy** — ICE is built for a portfolio of cheap experiments;
  for a single big commitment, use a decision memo.

## Relation to Impact–Effort

Impact–Effort collapses to two axes and is faster in a live session. ICE adds
Confidence, which is useful when the shortlist contains claims of varying
evidential quality. A practical sequence: vote → Impact–Effort to triage →
ICE to order the handful that remain. Do not run both on the full set; the
second formula mostly re-encodes the first.
