# When NOT to Use Challenge Assumptions — and What to Use Instead

This skill is for **overconstrained problems with hidden, testable beliefs**. If the next artifact you need is not "a ranked assumption inventory plus reframed problem statements," another method is likely a better first move.

## Quick triage

| Your situation | Better fit | Why |
| --- | --- | --- |
| Answers feel predictable or samey; you need unexpected directions | `lateral-thinking` | Its job is deliberate discontinuity; this skill tests beliefs rather than generating provocations |
| You have a concrete baseline and want many structured variations | `scamper` | Variation operators on an existing design; no assumption inventory needed |
| A specific engineering contradiction resists all options ("stronger but lighter") | `triz-contradictions` | Resolves tradeoffs by separating them; here the tradeoff may be real |
| The problem is correctness-bound: proof, debugging, safety sequence, compliance audit | Vertical / critical thinking | Rigor on one line of reasoning; reframing would add noise |
| You believe the current design rests on conventions that may not hold at all | `first-principles` | Rebuilds from verified constraints; stronger when the frame itself must be replaced, not just tested |
| The brief is vague or solution-shaped and you do not yet know the question | `question-storming` | Generates questions before assumptions; a good precursor |
| You lack facts about the world: users' behavior, market size, contract terms | Research first | Labeling ignorance as an "assumption" does not create evidence |
| You have several viable options and must choose under uncertainty | `premortem`, `options-portfolio` | Stress-testing and selection, not frame discovery |
| Different stakeholders keep talking past each other | `six-thinking-hats` or `stakeholder-perspectives` | Separates modes and surfaces interests; this skill inventories beliefs, not feelings |
| The framing is too narrow or too abstract, but not obviously false | `abstraction-laddering` | Moves levels deliberately; useful before deciding what to challenge |
| You want to approach the goal through guaranteed failure | `inversion` | Failure-first design; broader than single-belief reversal |

## Don't confuse with adjacent methods

- **Lateral thinking** challenges assumptions as a route to provocation (`Po`). Challenge-assumptions treats the assumptions themselves as the deliverable: inventory, evidence, rank, reframe. Lateral can run with zero known beliefs; this skill needs a dominant frame to interrogate. They pair well: inventory first, then provoke inside the most promising reframe.
- **First-principles thinking** also separates assumptions from facts, but its output is a rebuild from fundamentals. Here the output is a tested belief map and 3 reframed statements. If the foundational constraints are unknown, first-principles is the better tool.
- **SCAMPER** assumes the baseline is roughly right and varies it. If the baseline's existence is the question, SCAMPER will optimize the wrong object.
- **TRIZ** assumes a real contradiction and looks for inventive principles that resolve it. Challenge-assumptions asks whether the contradiction is an artifact of a boundary belief. If the tradeoff survives inspection, switch to TRIZ.
- **Question storming** produces questions; this skill produces assertions and evidence. Questions are a good input — run question storming if the inventory feels thin.
- **Inversion** asks how to guarantee failure. The reversal test here is narrower: assume one belief is false and look for a mechanism. Full failure-first design belongs to inversion or `premortem`.
- **Six Thinking Hats** is a mode structure. It can host this skill (White Hat for evidence, Black Hat for risk), but it does not itself inventory or test beliefs.

## Constraints that should not be "challenged"

Keep the distinction between a belief and a fact:

- Physical limits, arithmetic, and measured performance envelopes.
- Signed contracts and applicable law as written — challenge the *interpretation* and *scope*, not the existence, and verify with the accountable expert.
- Observed behavior: what users actually did, not what you wish they did.
- Safety and privacy controls whose failure mode is irreversible — test in a dry run, never in production.

Challenging these without evidence reads as unserious and burns credibility for the beliefs that genuinely deserve challenge.

## Signs you are in the wrong method

- You cannot name a belief, only a feeling that "there must be a better way" → use `lateral-thinking` or `divergent-thinking`.
- The inventory keeps filling with facts and preferences, not constraints → you may need `stakeholder-perspectives` or research.
- Every reframe is really a feature request → you are solutioning; return to the problem statement or use `scamper`.
- The debate is about which option is best, not whether the frame is right → use `premortem` or `options-portfolio`.
- The constraint turns out to be real → record it and move to design under constraint; do not keep challenging to save face.

## Handoff triggers

| Next | Trigger |
| --- | --- |
| `lateral-thinking` | A reframe needs many unexpected directions, not one |
| `scamper` | A reframe is chosen and needs systematic variations |
| `first-principles` | The inventory shows the whole design rests on unverified conventions |
| `triz-contradictions` | A tradeoff survives the tests and now needs resolution |
| `premortem` | A reframe looks promising and needs hardening before commitment |
| `question-storming` | The inventory is thin because the question itself is unclear |
| `thinking-router` | The need is mixed or you cannot tell which method fits |
| Vertical execution | The frame is sound and the remaining work is engineering |

## Anti-patterns

- **Challenge theater.** Treating every constraint as negotiable to look bold. Real constraints exist; the skill is for finding which ones are not.
- **Inventory without ranking.** Fifteen beliefs and no priority produce paralysis.
- **Probe without a decision rule.** Data is collected to confirm, not to decide.
- **Reframe by adjective.** "A more user-centric onboarding" is not a reframe; nothing was removed.
- **Strawman beliefs.** Inventing a weak version of the constraint to knock down instead of stating the strongest version.
- **Evidence laundering.** Calling an anecdote "user research" or a vendor claim "a system limit."
- **Skipping the owner.** Reframing around a constraint owned by someone who is not in the conversation produces a plan that cannot be approved.
