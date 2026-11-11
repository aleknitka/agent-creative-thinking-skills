# When NOT to Use First Principles — and What to Use Instead

First principles is for **rebuilding an approach from verified fundamentals**. If the next artifact you need is not "a constraint map plus approaches that do not depend on existing conventions", another method is probably a better first move.

## Quick triage

| Your situation | Better fit | Why |
| --- | --- | --- |
| Answers feel predictable; you need unexpected directions | `lateral-thinking` | Generates discontinuity and provocations; it does not require verified fundamentals first |
| You want to know whether specific beliefs are true | `challenge-assumptions` | Audits and tests the current frame; does not rebuild it |
| A specific engineering contradiction resists all options ("stronger but lighter") | `triz-contradictions` | Resolves a real tradeoff by separating it; the contradiction may be genuine |
| You need to guarantee failure in order to see obstacles | `inversion` | Failure-first reasoning is broader than rebuilding one design |
| You have several viable approaches and must choose | `premortem` / `options-portfolio` | Selection and stress-testing, not foundation discovery |
| You need many structured variations of a sound baseline | `scamper` | Operator-driven variation assumes the baseline is roughly right |
| The brief is vague or solution-shaped and you do not know the question | `question-storming` | Generates questions before answers |
| The frame is too narrow or too abstract, but not obviously false | `abstraction-laddering` | Moves levels deliberately while keeping the frame |
| You lack facts about the world: user behavior, market size, contract terms | Research first | A fundamental you cannot verify is a guess in a confident voice |
| The work is correctness-bound: proof, debugging, safety sequence, compliance audit | Vertical / critical thinking | Rigor on one line of reasoning; rebuilding adds noise |
| You need a large, diverse idea set before any evaluation | `divergent-thinking` | Quantity and variety first; foundations come later |
| Safety-critical change where you are not the accountable domain expert | Compliance-led change | The authority to redefine constraints is not yours alone |

## Don't confuse with adjacent methods

- **Challenge assumptions** makes hidden beliefs explicit and tests them within the current frame. First principles assumes some of those beliefs are inherited and asks what a solution would look like without them. If you only need to know whether a constraint is true, challenge-assumptions is cheaper. If you need to know what to build instead, first principles. They pair: challenge first to find the inherited items, then rebuild.
- **Lateral thinking** produces movement and unexpected directions; it does not require the fundamentals to be true. First principles demands verified foundations before generation. Using lateral thinking to escape a bad frame is fine, but it will not tell you which constraints are real.
- **TRIZ** starts from a contradiction inside a system and resolves it with inventive principles. First principles may remove the system or the contradiction entirely. If the tradeoff is real and local, TRIZ is the better tool; if the tradeoff exists only because of the current design, first principles may dissolve it.
- **Abstraction laddering** moves between "why" and "how" levels. It changes the altitude of the question but does not classify which constraints are fundamental. Use it when the problem is framed at the wrong level, not when the constraints are suspect.
- **Inversion** asks how to guarantee failure. It can supply failure conditions that a rebuild must prevent, but it does not produce the rebuilt design.
- **SCAMPER** assumes a valid baseline and varies it. If the baseline's existence is the question, SCAMPER optimizes the wrong object.
- **Premortem and options-portfolio** evaluate and select. They are the right next step after a rebuild, not a substitute for it.

## Signs you are in the wrong method

- You cannot name a fundamental, only a feeling that "there must be a better way" → use `lateral-thinking` or `divergent-thinking`.
- The constraint map is filling with preferences and opinions → research or `challenge-assumptions` first.
- The question is whether one belief is true, not what to build instead → use `challenge-assumptions`.
- A real tradeoff survives classification and needs resolution → use TRIZ.
- The decision is needed immediately and no evidence is available → decide under uncertainty, then test; a rebuild on guesses is theater.
- The incumbent is basically sound and the need is incremental improvement → use improvement or variation methods.
- The domain is regulated or safety-critical and you lack authority → work with compliance and domain owners; do not unilaterally remove constraints.
- The organization cannot absorb a structural change right now → sequence the rebuild or use a smaller improvement.

## Constraints that should not be "rebuilt away"

- Physical and engineering limits, including measured performance envelopes.
- Law, signed contracts, and applicable regulation as written; challenge interpretation and scope only with the accountable expert.
- Safety, security, and privacy invariants whose failure is irreversible.
- Observed behavior at the scale that matters, treated as evidence rather than preference.
- Resource ceilings that are externally fixed for the planning horizon.

Removing these is not first-principles thinking; it is ignoring the problem's actual conditions.

## Handoff triggers

| Next | Trigger |
| --- | --- |
| `challenge-assumptions` | You need to test which inherited item is actually load-bearing |
| `lateral-thinking` | The rebuilt direction exists but needs unexpected variations |
| `scamper` | A direction is chosen and needs systematic variation |
| `triz-contradictions` | A fundamental tradeoff survives and must be resolved |
| `premortem` | An alternative looks promising and needs hardening before commitment |
| `options-portfolio` | Several alternatives need comparison under uncertainty |
| `abstraction-laddering` | The outcome itself is framed at the wrong level |
| `question-storming` | The problem statement is too vague to classify constraints |
| Research or domain expert | Fundamentals are unknown or disputed |
| `thinking-router` | The need is mixed or you cannot tell which method fits |
