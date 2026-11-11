# Facilitation — Equal Airtime, Clean Ballots, Honest Records

NGT fails quietly. The agenda can look perfect while a senior voice, a shared
screen that reveals early votes, or a "quick clarification" that turns into a
pitch destroys the independence the method depends on. Facilitation is the
guardrail.

## Roles and materials

| Role | Does | Does not |
|---|---|---|
| Facilitator | Holds time, enforces rules, reads the question, calls turns | Contribute opinions, defend an item, vote twice |
| Scribe | Records items verbatim, assigns IDs, keeps the merge log | Paraphrase, cluster by author, rank during harvest |
| Decision owner | Accepts the record, commits to the next action | Campaign for an item or edit the question mid-session |
| Participants | Generate silently, share one at a time, clarify, vote independently | Lobby, caucus, or reopen generation during voting |

Materials: one card or private document per person, a visible timer, a numbered
master list (paper or board), printed or digital ballots, and a dissent log.
For Delphi the equivalents are a mailing list with a blind or pseudonymous
channel, a rating form that does not show other responses, and a versioned
feedback pack.

## Opening script

> "The question is ⟨question⟩. The decision is ⟨decision⟩, and the constraint
> is ⟨constraint⟩. We will generate alone, share one item at a time, clarify
> facts only, then vote by ⟨rule⟩. The top ⟨K⟩ go to ⟨owner⟩ for ⟨next step⟩.
> Please do not discuss items yet."

Then check comprehension with questions of fact. Do not answer "which ideas do
you like?" and do not give an example item.

## Phase discipline

### Silent generation

- Start the timer only after every person has the question in front of them.
- No talking, no peeking, no shared document open in edit mode.
- Circulate quietly; if someone is stuck, point to the question, not to an idea.
- Collect or freeze the cards before the round-robin begins.

Phrases: "Write first; we will discuss nothing until every card is in."

### Round-robin

- Call turns in a fixed order so no one has to fight for the floor.
- Accept "pass" without comment; return to the person after the circle.
- One item per turn. If someone reads a list, stop them: "One item now; you
  will get another turn."
- Record verbatim. If the item is unclear, write it as spoken and clarify later.
- Park reactions on a visible parking lot, not in the discussion.
- Keep the facilitator's own turn in the same format as everyone else's.

Phrases: "That goes on the parking lot; we clarify after the circle." "Next
item, not next comment."

### Clarification

Allow questions of fact: what, who, when, how much, compared with what.
Block advocacy: "that won't work", "we tried it", "this is the obvious one".
Ask the author to answer, then move on. Merge duplicates only with consent.

Example rewrite:

- Advocacy: "This is clearly the cheapest option, so I think we should all
  rate it highly." → Block.
- Clarification: "Does the cost estimate include the support contract?" →
  Allow.

### Voting

- Distribute ballots after the rules are restated; read the rule aloud.
- Everyone votes at once. No show of hands for a preliminary tally; hands
  create a visible bandwagon.
- Collect all ballots before tallying. If voting digitally, hide results until
  the form closes.
- Do not let the decision owner "just add a weighting" after seeing the tally.
- Announce the tally with counts, not a narrative about who won.

### Discussion and final vote

Show both the distribution and the item list. Ask what would change a rating,
which assumption is doing the most work, and what cost is missing. Do not ask
"who voted for this?" — the ballot is not a confession. If new information
arrives, log it, state whether it changes any ratings, and re-vote the whole
set with the same rule.

## Handling hierarchy and dominance

- **Senior leader in the room:** give them a turn like everyone else. Ask them
  to speak last in the round-robin if their view predictably anchors the room;
  better, have them state the constraints and then hand over the floor.
- **Serial talker:** enforce one item per turn and use the parking lot. Do not
  debate the rule mid-round; point to the agreed process.
- **Silent participant:** invite in the round-robin, not with "any thoughts?".
  The fixed turn order protects them. Never fill their silence with your own
  idea.
- **Side conversations:** pause, restate the rule, resume at the same turn.
- **Expertise gradient:** clarify expertise as evidence ("what have you seen
  that supports that?"), not as a trump card. An expert's confidence is not a
  vote.
- **Remote rooms:** mute everyone during generation, use breakout rooms for
  privacy, and call names in a stable order. A shared doc that everyone can
  edit during generation is a dominance channel.

## Ballot integrity

- Same budget and the same item list for every voter.
- No negative points, no proxy votes, no bloc coordination before the ballot.
- Record spoiled or incomplete ballots; do not silently repair them.
- Keep raw ballots (anonymised if promised) with the tally, so the record can
  be audited.
- If a voter abstains, record abstention rather than filling their ballot with
  the mean.

## Dissent log template

| Field | Content |
|---|---|
| Item | Stable ID and short label |
| Decision | Selected / not selected / tie |
| Objection | The strongest opposing case, in one sentence |
| Basis | Evidence, assumption, or values disagreement |
| Held by | "Two voters" or a role, not necessarily a name |
| Revisit trigger | New evidence, date, or condition that reopens the item |

Unanimity that hides disagreement is not a decision record. If no dissent is
recorded, ask explicitly: "What is the strongest case against the top item?"

## Delphi facilitation

- **Invite for expertise and stake.** State the purpose, the time commitment
  (about 20–30 minutes per round), the number of rounds, and the anonymity
  terms in the invitation.
- **Over-invite by 30–50%.** Attrition is normal. Track response rate per
  round; below roughly 70% the final distribution is fragile, so report the
  rate rather than hiding it.
- **Anonymity mechanics.** Collect responses through a form or a neutral
  coordinator. Strip names before analysis; do not quote a comment that
  identifies its author by role or project.
- **Feedback wording.** "For item I4, the panel median is 4 (IQR 1). Your
  Round 1 rating was 2. Comments cited cost and support load; no identities are
  attached." No leaderboard, no sponsor commentary.
- **Extreme scores.** Ask the outlier to give a reason, then include the reason
  anonymously in the next pack. Do not ask them to justify themselves to the
  group.
- **Reminders.** One reminder two days before the deadline, one on the final
  day. More than that reads as pressure.
- **Dropouts.** Report the final n. Do not replace a panellist mid-round with a
  new person who has not seen the earlier feedback; that breaks the shared
  information state.
- **Sponsor pressure.** A sponsor may set the question and receive the report;
  they do not get a vote or a private channel to the panel.

## Agent and AI-assisted mode

An agent can draft the question, simulate a ballot for rehearsal, cluster
statements, and compute medians. It cannot manufacture independent expertise.
Running "one agent per voter" produces correlated text from the same model, not
a panel. Use it to rehearse the process and check the arithmetic; mark any
synthetic output as synthetic, and never present it as stakeholder input.

## Common failure modes

| Symptom | Likely cause | Fix |
|---|---|---|
| Everyone converges on the first spoken idea | Discussion started before silent generation | Restart generation; collect cards before any talk |
| Top items are all from senior people | Round-robin order or airtime favours them | Fixed turn order; senior speaks last; silent cards first |
| Tally is suspiciously unanimous | Visible voting, no secret ballot, or fear | Independent ballots; collect before discussing |
| Same item returns every quarter | No dissent or kill reason recorded | Keep the dissent log and a revival trigger |
| Delphi panel agrees in one round | Homogeneous panel or leading feedback | Diversify the panel; strip sponsor commentary; test spread |
| Long report, no decision | No owner or handoff agreed at intake | Name owner and next action before the session ends |
