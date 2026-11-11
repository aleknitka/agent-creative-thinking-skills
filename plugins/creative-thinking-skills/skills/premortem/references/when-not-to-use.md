# When NOT to Use Premortem — and What to Use Instead

A premortem is a **pre-commitment ritual for a concrete plan**. If the plan is not concrete, the decision cannot change, or the question is "which option?", another method fits better.

## Quick triage

| Your situation | Better fit | Why |
|---|---|---|
| Still generating options; no proposal on the table | `divergent-thinking`, brainstorming, `what-if` | Premature critique selects against novelty and anchors on the first concept; failure imagination needs something specific to fail |
| Exploring a topic from several angles, caution included | `six-thinking-hats` (Black hat within the sequence) | In-session caution, not a dedicated failure ritual; no declared scene, no independent generation protocol |
| Quantified, safety-critical hazards (medical, aviation, process plant) | FMEA, HAZOP, fault-tree analysis, formal technical risk assessment | Standards-based, auditable, severity/probability-rated; a premortem is qualitative and cannot certify safety |
| Decision is already locked, or the team has no authority to change the plan | Risk tracking, tripwires, postmortem/incident review | The premortem's value is shaping the plan while change is still cheap |
| Choosing among 3–5 options | `options-portfolio`, decision matrix | Premortem stress-tests one proposal; comparison needs shared criteria |
| You need evidence about what will happen | Pilot, experiment, reference-class forecasting, base rates | A premortem produces hypotheses and warnings, not estimates |
| The culture punishes dissent or the plan owner will rebut every point | Anonymous written collection, outside facilitator — then premortem | Otherwise the room produces polished optimism and the real doubts stay private |
| The proposal is a one-off, low-cost, reversible experiment | Just run it | The ceremony costs more than the mistake; cap the downside instead |

## Premortem vs Black hat (six-thinking-hats)

Both invite caution, but they are different instruments.

| | Black hat | Premortem |
|---|---|---|
| **Purpose** | Apply deliberate caution while examining a topic | Strengthen a chosen plan before commitment |
| **Trigger** | Any topic or idea, inside a hat sequence | Concrete proposal plus a failure horizon |
| **Premise** | "This could fail because…" | "It is ⟨date⟩; it failed. Why?" |
| **Output** | Concerns, weaknesses, checks | Clustered reasons, likelihood × impact, prevention and monitors with owners |
| **Generation** | Open discussion within the hat | Independent silent generation first, then capture |
| **Risk** | Can feel like blanket negativity; often shallow | Can become a defence session if facilitation slips |

Use the Black hat when caution is one mode among several in an exploratory conversation. Use a premortem when a plan is about to be committed and the output must change it. Running a Black hat is not a substitute for the prospective-hindsight frame, and a premortem is too heavy for a routine idea review.

## Premortem vs technical risk assessment (TRA/FMEA/HAZOP)

- **TRA/FMEA/HAZOP** decompose a known system, enumerate failure modes, and rate severity and probability against standards. They are auditable and repeatable, and they are the right tool when harm to life, health, or regulated operations is at stake.
- **Premortem** is qualitative and imagination-led. It is strong at organisational and human failure modes — incentives, ownership, coordination, morale, sponsorship — that formal hazard analyses often omit. It is weak at rare technical failure modes and cannot certify anything.
- **Use both when stakes justify it:** formal analysis for the safety case, premortem for delivery and adoption. Do not let a successful premortem stand in for a required risk assessment.

## The premature-critique trap

A premortem run during ideation is not rigorous; it is a novelty filter. Early ideas are underspecified, so failure reasons are easy to generate and hard to refute, and the safest-looking concept wins by default. Symptoms:

- The "plan" is still a paragraph of intent with no owner, date, or measure.
- Reasons are about the idea's category ("customers won't pay for this") rather than its mechanism.
- The exercise ends with "maybe we shouldn't do this" instead of a changed design.

**Rule:** the proposal must be concrete enough to fail in a *specific* way. If you cannot say who ships what by when and how you will know it worked, go back to divergence or scoping first.

## Handoff triggers

Use `thinking-router` when unsure. Common handoffs:

| Next | Trigger |
|---|---|
| `challenge-assumptions` | The premortem keeps producing the same foundational doubt about the premise |
| `divergent-thinking` / `what-if` | Reasons point to design alternatives rather than fixes |
| `options-portfolio` | Hardening produces several candidate responses that need choosing between |
| `six-thinking-hats` | The team needs to explore benefits and caution together, not only failure |
| Pilot/experiment | A top reason can be tested cheaply before commitment |
| Formal TRA/FMEA | A top reason is a safety or regulatory hazard |
| Postmortem/incident review | The event already happened; stop imagining and reconstruct |

## Anti-patterns

- Running it after the decision is announced, when dissent is costly and nothing can change.
- Using it as a veto tool: a long failure list with no hardening budget is an argument, not an analysis.
- Confusing it with a risk register: the premortem's distinctive output is a changed plan and early warning signals.
- Treating plausible reasons as probabilities. Likelihood scores are judgments to be tested, not forecasts.
- Skipping the independent generation step, which reduces the exercise to a meeting about known concerns.
