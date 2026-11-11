# Worked Examples — Three Stimuli, One Problem

The same problem is used three times so the differences come from the stimulus, not the brief. Each connection is scored and probed independently; the point is not that all three are good, but that each proposes a different mechanism.

## The problem (intake)

A B2B SaaS support organization has 40 agents, about 9,000 tickets a month, and a help centre with 400 articles. Roughly 28% of ticket volume repeats questions the help centre already covers, and agents routinely solve recurring issues inside tickets without writing the answer back.

- **Goal:** cut repeat-question volume by 25% within one quarter.
- **Constraints:** Zendesk, two engineer-weeks, no new headcount, no content team.
- **Baseline ideas already on the table:** a quarterly article sprint, reminders to agents, and an AI write-back vendor demo.
- **Appetite:** medium. **Labels:** 28% and 400 articles are facts; "agents are lazy" is an assumption; "AI write-back would work" is speculation.

## Connection 1 — word stimulus: *compost*

Drawn from the word bank with `python3 scripts/connect.py --type word`. Literal properties: consumes dead material; needs a carbon-to-nitrogen balance; must be turned periodically; generates heat; takes months; produces soil; smells when anaerobic; the decomposers are invisible.

| Property | Forced move |
|---|---|
| Consumes dead material | Resolved tickets are the raw material, not waste |
| Periodic turning | A scheduled act exposes buried material and mixes it |
| Carbon:nitrogen balance | Mix quick one-line fixes with deep explanations, or the pile stalls |
| Smells when anaerobic | Drafts that nobody turns become stale and visible |

**Connection:** a "compost queue." At ticket close, the agent nominates one reusable sentence from the resolution. Each squad has a rotating 30-minute weekly "turn" role that converts nominations into article patches. A patch is only counted when it links back to the source ticket.

**Mechanism:** a fixed cadence and a narrow input (one sentence) reduce the activation energy of writing back, while the rotating role moves the work from "everyone, always" to "someone, weekly."

**Evaluation:** novelty 4, usefulness 4 — no new tooling; Zendesk macro plus a spreadsheet. **Probe:** two squads, four weeks, against two control squads. Signals: nominations per agent-week, patches published per week, repeat-question rate. **Kill:** fewer than two patches per agent-month, or no repeat-rate movement by week six. **Risk:** nomination fatigue; measure ticket close time.

## Connection 2 — object stimulus: *turnstile*

Literal properties: admits one person at a time; a ratchet prevents reverse movement; counts passages; requires a token; creates a queue; bulky items do not fit; separates paid from unpaid.

| Property | Forced move |
|---|---|
| Ratchet | Closing a solved ticket cannot slip back to "no article" |
| Counting | Every article reuse is counted at close |
| Bulky items do not fit | The reusable answer must be short enough to fit |
| Creates a queue | The gate must not add more than a few seconds |

**Connection:** a "one-way close." A ticket cannot be marked solved unless it either links an existing article or creates a stub pre-filled with the agent's last public reply. Stubs are short by construction. Reuse is counted at the gate, so the help centre's coverage becomes measurable.

**Mechanism:** a gate changes the default path. Reminders ask agents to write back; a close condition makes the article the artifact that closes the ticket. Counting at the gate supplies the metric without a separate reporting project.

**Evaluation:** novelty 3, usefulness 5 — one Zendesk trigger, within the two engineer-weeks. **Probe:** one queue for three weeks. Signals: share of closes via existing article, stub creation rate, median close time. **Kill:** median close time rises more than 25%, or more than half of stubs are abandoned. **Risk:** the gate can encourage a low-value stub just to close; sample stub quality.

This is the least surprising idea of the three — a gate is a familiar pattern — and it scores highest on usefulness. Forced connections are allowed to produce practical ideas, not only strange ones.

## Connection 3 — concept stimulus: *escrow*

Chosen from a legal glossary by arbitrary entry. Literal properties: a neutral third party holds an asset; release requires conditions written in advance; it protects both sides; there is an audit trail; assets can be returned; release can fail.

| Property | Forced move |
|---|---|
| Neutral holder | A review queue, not the author, holds the draft |
| Conditions written in advance | "Released when a different agent resolves a real ticket using it" |
| Protects both sides | The author gets credit; the next agent gets a vetted answer |
| Audit trail | Every release records which ticket proved it |
| Return on failure | Failed drafts come back with the failure note |

**Connection:** "answer escrow." When an agent writes a fix, the draft sits in escrow. Another agent claims it for a similar ticket. If it resolves the ticket, the draft is published and the author gets recognition; if not, it returns with the failure note.

**Mechanism:** credit is released only on proven reuse, which aligns the incentive to write reusable answers rather than more documentation. The second user is also the quality check.

**Evaluation:** novelty 5, usefulness 3 — the matching between drafts and tickets is the hard part, and the two engineer-weeks are probably insufficient. **Probe:** paper escrow for one squad, ten drafts over 30 days, no customer-facing change. Signals: share claimed within 14 days, time from draft to publication. **Kill:** fewer than 30% claimed, or publication takes more than ten minutes of handling. **Risk:** urgent tickets cannot wait for escrow; keep it to non-urgent recurring issues.

## Discarded draws

- **Word "volcano"** → "erupt with ideas", "make the help centre lava-hot." Shared heat imagery, no mechanism. Killed under wordplay.
- **Object "mirror"** → "agents should reflect on their tickets." A familiar management phrase; substituting any noun leaves the idea intact. Killed under substitution.
- **Concept "immune system"** → "articles should learn from attacks." The source mechanism was not understood well enough to state a causal path; parked, not kept.

## What the set shows

- The same problem yields a **ritual** (compost), a **gate** (turnstile), and an **incentive** (escrow). None of the three could have been predicted from the problem's own vocabulary.
- The concept draw produced the most novel and least practical connection; the object draw produced the most practical. That trade-off is normal, and it is why evaluation scores both axes.
- Two of three survived; the discarded draws are recorded so the session's curation is visible.
- Each keeper states a mechanism, a signal, and a kill criterion. A connection without all three is not ready to test.
