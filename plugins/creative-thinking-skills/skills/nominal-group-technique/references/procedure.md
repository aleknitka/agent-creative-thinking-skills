# Procedure — NGT and Delphi

Both protocols separate four acts that meetings usually blur: **generate in
silence, share without debate, clarify facts only, then judge**. NGT compresses
them into one room and one session; Delphi stretches them across anonymous
rounds when the right experts cannot meet.

Pick the protocol before designing the agenda. Mixing them mid-session (a live
room plus an asynchronous panel voting on the same list) is possible, but then
the same people must see the same frozen items and the same aggregation rule.

## Intake — before any invitations

Write five things down and circulate them:

1. **One ranking question**, with the decision it feeds. Good: "Which three
   onboarding changes should we pilot next quarter?" Bad: "How do we improve
   onboarding?" The question must name the object, the horizon, and the
   constraint (budget, headcount, policy).
2. **The item set** — 8–20 comparable options, one line each, stable IDs
   (`I1`, `I2`, …). If generation is incomplete, run divergence first
   (`brainwriting`, `brainstorming`, `scamper`); NGT is not a generator.
3. **The voter set** — people with relevant knowledge plus people who own the
   consequences. NGT: 5–9 works well; 10–12 needs a firm facilitator. Delphi:
   10–20 panellists is common; there is no universal correct size.
4. **The aggregation rule** — `ranked` (5-4-3-2-1), `n3` (N/3 dots), or Delphi
   ratings; the shortlist size K; the tie-break. Fix these now.
5. **The decision owner and the next action** — who accepts the ranked list,
   what happens to the top K, and when the decision is reviewed.

Circulate the question and constraints, never example ideas. Examples anchor
the first round and quietly narrow the option set.

## NGT — same-room timed script (75–90 minutes)

| Minutes | Stage | Output |
|---|---|---|
| 0–10 | Frame the question, constraints, and process; questions of fact only | Shared understanding |
| 10–20 | Silent generation — 5–10 ideas per person, one per card, no talking | Private idea cards |
| 20–35 | Round-robin sharing — one item per turn, scribe records verbatim | Numbered master list |
| 35–45 | Clarification — author explains; group asks factual questions | Merged, deduplicated list |
| 45–50 | Break — ballots are prepared, no lobbying | Ballot forms |
| 50–55 | Preliminary vote — silent, written, independent | Vote distribution |
| 55–70 | Structured discussion of the distribution, not of favourite items | Revised understanding |
| 70–75 | Final vote — same rule as the preliminary ballot | Final tally |
| 75–85 | Dissent log, decision owner, handoff | Ranked shortlist + record |

### Stage notes

**Silent generation (10 minutes).** Each participant writes alone, on paper or
in a private document. One idea per line, verbatim, no editing for elegance.
Aim for 5–10; quantity is not the goal but fluency matters. No examples on the
table, no "builds" yet — this is not brainwriting, and cross-pollination before
the round-robin reintroduces anchoring.

**Round-robin (15 minutes).** Go around the table. On each turn a person reads
one item, the scribe writes it verbatim and assigns the next ID. Continue until
every card is on the board. Rules:

- One item per turn; do not read your whole list at once.
- Do not explain, defend, or critique while reading.
- Duplicates are read anyway; merging happens in the next stage with consent.
- The facilitator takes a turn like everyone else.

**Clarification (10 minutes).** The author of an item may answer "what did you
mean by…" and factual questions. Advocacy is out of scope. Merge only exact or
near-exact duplicates, and only with the author's agreement; keep a note of
which IDs were merged. If an item is genuinely ambiguous, split it now rather
than during voting.

**Preliminary vote (5 minutes).** Silent, written, simultaneous. Use the
pre-agreed rule. Collect every ballot before showing any tally. The preliminary
vote exposes the distribution; it is not a decision.

**Discussion (15 minutes).** Show the distribution. Ask neutral questions:
"Which item is underrated by the room?", "What evidence would change your
rating?", "Which top item has an unstated cost?". No speeches for a favourite,
no new items unless the whole group agrees; if a new item is admitted, log it
and re-vote both rounds.

**Final vote (5 minutes).** Same rule, fresh ballot. Report both rounds,
including movement. A large shift after discussion is information: record what
changed.

### Virtual NGT

Keep the timings; change the medium. Private breakout documents for generation,
a shared board with one lane per person for the round-robin, a numbered master
list for clarification, and a form or poll that hides results until everyone
has voted. Silent generation in breakout rooms is not optional — a shared doc
open from the start lets fast writers set the frame.

## Delphi — asynchronous rounds (3–5 weeks)

| When | Stage | What the facilitator does |
|---|---|---|
| Days 1–5 | Panel and framing | Invite 1.3–1.5× the target panel; confirm expertise, stake, and availability; send the question, constraints, and anonymity terms |
| Days 6–12 | Round 1 | Collect anonymous proposals or initial 1–5 ratings; no discussion, no visible responses |
| Days 13–18 | Analysis | Content-analyse proposals into 15–25 statements; remove duplicates; check coding with a second reader where possible; return the list to panellists to confirm nothing was lost |
| Days 19–25 | Round 2 | Circulate the anonymised distribution (median, IQR, own prior rating, reasons stripped of identity); panellists re-rate privately |
| Days 26–32 | Round 3 (if needed) | Repeat feedback with the updated distribution; stop on the pre-agreed rule |
| Days 33–35 | Report | Final medians, IQR, n, response rate per round, dissent, and the decision handoff |

### Stage notes

**Panel construction.** Expertise in the question, not seniority alone. Include
people who will implement the answer and people who bear its risk. Avoid a
panel drawn from one team or one vendor; homogeneity produces confident
consensus, not valid judgment. Record roles generically (e.g. "field engineer,
region B") so feedback can be contextual without being attributable.

**Round 1.** Open-ended ("list the three most important…") or a rating of an
already-frozen list. Open-ended rounds surface categories the facilitator did
not anticipate; ratings are faster when the list is mature. Either way, no
one sees another panellist's identity or verbatim response.

**Feedback.** Return four things: the item, the group median, the IQR, and the
panellist's own previous rating. Optionally include anonymised reason codes
("cost concern", "safety risk") when comments explain score spread. Never
return a leaderboard with names, and never let a sponsor add a "leadership
view" to the feedback — that converts Delphi into a survey with pressure.

**Stopping rule.** Fix it before Round 1: for example, "stop after three
rounds, or when at least 80% of items have IQR ≤ 1 and 70% of ratings fall
within ±1 of the median, or when no median moves by more than 0.5 between
rounds". Stop on time even if consensus is incomplete — an honest split is a
result.

**Reporting.** Report per-item median, IQR, n, and response rate per round.
Report items that stayed split. Do not publish a single "consensus score" that
hides dispersion, and do not call the result a prediction.

## Script-assisted rehearsal

`scripts/ngt.py` generates a seeded, synthetic ballot set and applies the same
aggregation rules used in the room. Use it to rehearse output format and edge
cases, not to decide anything:

```
python scripts/ngt.py --ideas options.txt --voters 7 --method ranked --seed 7
python scripts/ngt.py --count 12 --voters 7 --method n3
python scripts/ngt.py --count 12 --voters 9 --method delphi --rounds 3 --seed 7
```

- `--ideas` reads one option per line; `--count` creates placeholders.
- `--seed` makes the synthetic ballots reproducible; the same seed and inputs
  always produce the same tally.
- `--json` emits ballots, rankings, and dissent notes for inspection.
- The script does not read real ballots. If you have real ballots, aggregate
  them in the agreed rule and record the raw file alongside the decision.

## Quality checklist before you close

- [ ] One ranking question, with the decision and horizon named.
- [ ] Every item has a stable ID and comparable scope.
- [ ] Silent generation happened before any discussion.
- [ ] Round-robin was one item per turn, recorded verbatim.
- [ ] Clarification stayed factual; advocacy waited for discussion.
- [ ] The aggregation rule and shortlist size were fixed before voting.
- [ ] Ballots were independent; no show of hands, no caucusing.
- [ ] Both preliminary and final tallies are in the record.
- [ ] Dissent names the objection, not just the objector, and is preserved.
- [ ] A named owner has the shortlist and a date for the next action.
