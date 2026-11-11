# When NOT to Use Lateral Thinking — and What to Use Instead

Lateral thinking is for **reframing**, not for correctness, research, or hardening. If your next artifact is not "alternative frames / unexpected directions," another method fits better.

## Quick triage

| Your situation | Better fit | Why |
|---|---|---|
| You need stepwise correctness — proof, optimization, debugging, compliance, safety-critical sequence | **Vertical / critical thinking** | Digs the same hole deeper with rigor; lateral would add noise |
| You don't know the facts yet — unknown constraints, missing user data | **Research first**, then `challenge-assumptions` or `first-principles` | Bottleneck is knowledge, not framing |
| You need structured variations on an existing baseline concept | `scamper` | Narrower and systematic; lateral is too indirect |
| A recurring technical tradeoff blocks progress ("fix A, break B") | `triz-contradictions` | Treats the tradeoff as a contradiction to separate |
| You need breadth quickly without discontinuity | `divergent-thinking` (10+ ideas + lenses → cluster → converge) | Quantity-first divergence; lateral adds *break* |
| Ideas come from other domains and you can transfer a mechanism | `analogical-thinking` / `forced-connections` | Lateral's random entry overlaps but analogical is mechanism-specific |
| Critique and ideation keep interrupting each other | `six-thinking-hats` (Green Hat **is** lateral thinking) | Isolates modes |
| You have candidates and need to choose or harden them | `premortem`, `options-portfolio`, `concept-blending`, `double-diamond` | Convergence and stress-testing, not divergence |
| You want random stimulus specifically | `forced-connections` | Focused on forced-connections craft |
| You want better questions before answers | `question-storming`, `abstraction-laddering` | Problem-finding, not frame-breaking |

## Don't confuse with adjacent methods

- **Divergent thinking** = breadth (many options, then converge). **Lateral** = discontinuity (challenge → Po → movement → harvest). They pair well: run lateral to break the cluster, then divergent to populate alternatives.
- **SCAMPER** applies 7 prompts *to an existing idea*. Lateral has no baseline requirement.
- **TRIZ** mines inventive principles from patents; lateral invents provocations deliberately.
- **Six Thinking Hats** contains lateral as the **Green Hat** mode; the other five hats are different modes, not lateral.

## Handoff triggers

When lateral isn't the right entry point, triage with `thinking-router` (it maps into *better question / more ideas / broader perspectives / stronger options* and recommends 1–2 methods with tradeoffs).

Lateral thinking hands off to:

| Next | Trigger |
|---|---|
| `challenge-assumptions` | Harvest revealed hidden "musts" you want to inventory and test |
| `analogical-thinking` | A moved Po points to another domain's mechanism |
| `scamper` | You picked one frame and want systematic variations on it |
| `question-storming` | The dominant idea was the wrong question entirely |
| `what-if` / `scenario-planning` | A frame suggests an alternative world worth exploring |
| `premortem` | You want to harden a frame before committing |

## Anti-patterns

- Generating Pos without a harvest step — "randomness theatre."
- Treating forced connections as user research — label AI-generated perspectives as hypotheses to validate.
- Forcing weirdness when appetite is low — if the user cannot suspend judgment, lateral will read as unserious and erode trust; use `challenge-assumptions` instead and note the gap.
