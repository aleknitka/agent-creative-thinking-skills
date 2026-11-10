# Prioritization

A storm produces more questions than anyone can answer. Ranking decides which
questions earn investigation. Rank by what the answer would change, not by
curiosity, novelty, or ease.

## Three criteria

Score each question cluster 1–3 on each axis. Use the low/medium/high anchors
below so different people score comparably.

### Leverage — how much would the answer change the work?

| Score | Anchor |
|---|---|
| 1 | Answer is interesting but no decision or plan changes |
| 2 | Answer changes a detail, wording, or local tactic |
| 3 | Answer changes scope, priority, target user, or whether we proceed |

Ask: "If this came back surprising, what would we stop, start, or re-scope?"

### Tractability — can we answer it, and at what cost?

| Score | Anchor |
|---|---|
| 1 | No accessible evidence; would need a long study or unavailable data |
| 2 | Answerable with a bounded probe: one conversation, query, or prototype |
| 3 | Answerable now from existing data, documents, or a knowledgeable person |

Tractability is not importance. A highly tractable question with no leverage
is trivia; a high-leverage question that cannot be answered may need to be
parked and monitored rather than probed.

### Reframing power — could the answer change the frame itself?

| Score | Anchor |
|---|---|
| 1 | Confirms or adjusts the current frame |
| 2 | Could change a boundary, beneficiary, or constraint within the frame |
| 3 | Could make the original question obsolete or reveal a different goal |

Reframing power is the criterion specific to this method. A question that
merely fills a gap in a sound plan is useful, but it should not crowd out the
question that might reveal the plan is aimed at the wrong target.

## Combining the scores

Simple approaches, in order of preference:

1. **Gate on reframing power, then rank by leverage × tractability.** Any
   question scoring 3 on reframing power is investigated regardless of rank;
   the rest compete on impact and cost.
2. **Leverage × tractability** where reframing is not in question.
3. **Weighted sum** (leverage 2, reframing 2, tractability 1) when a single
   ordering is required for a meeting.

Do not average away a 3 on reframing power into a mediocre total. The point of
the method is to give frame-changing questions a path to the top.

## Triage labels

For each of the top 5–8 questions, assign exactly one label:

- **Answer now** — existing data, document, or person can settle it today.
  These are cheap wins; do them before revising the statement if they take
  minutes.
- **Probe** — a bounded test or conversation could settle it. Specify the
  observable and the decision rule.
- **Research** — needs external evidence, a literature scan, or a measurement
  campaign. Name the owner and deadline.
- **Park** — high leverage but not tractable now, or the decision is not live.
  Record the trigger that would reopen it.
- **Discard** — no leverage, or it is an assertion disguised as a question.

Park and discard must be visible. A silently dropped question looks like it
was answered.

## Selection heuristics

- Keep at least one question from each of the six categories, unless the
  category is genuinely irrelevant — and say why.
- Keep at least one question whose answer could change the problem statement.
- Prefer questions where a surprising answer is possible; a question with one
  acceptable answer is a confirmation ritual.
- Prefer questions the requester cannot answer alone; those expose assumptions
  the team shares.
- Drop questions whose only purpose is to assign blame or justify a decision
  already made.

## Common scoring errors

- **Ease bias.** The most answerable question wins. Guard with the leverage
  gate.
- **Sponsor bias.** Questions implying the sponsor was wrong get down-ranked.
  Score before attributing questions.
- **False precision.** A 1–3 scale is for ordering; do not defend a 7.3.
- **Double counting.** A question is not high-leverage merely because it is
  urgent; urgency belongs to the decision, not the question.
- **Unbounded probes.** "Do user research" is not a probe. Name the
  observable, the sample, and the decision rule, or park it.

## Output of prioritization

Produce a short table:

| Question | Leverage | Tractability | Reframing | Triage | Next action / owner |
|---|---|---|---|---|---|

Then state the top three in prose, with the decision each could change. This
is the input to the revised problem statement.
