# When NOT to Use Morphological Analysis — and What to Use Instead

Morphological analysis maps a **space of independent choices** and samples combinations. If the work is not "which combination of independent decisions", another method fits better.

## Quick triage

| Your situation | Better fit | Why |
|---|---|---|
| One baseline to improve; you need targeted variations | `scamper` | Seven prompts on an existing object; no dimension modelling |
| Blank page, no structure yet, need raw breadth | `divergent-thinking`, `brainstorming` | Generate first; a box built on an empty space encodes the same few ideas |
| You already have a candidate list and must choose | `options-portfolio` | Comparison and portfolio construction, not space mapping |
| Need to stress-test one chosen concept | `premortem` | Failure imagination, not combination coverage |
| The choices are causally entangled (a system, a market, a policy feedback loop) | `scenario-planning`, `systems-thinking`, `first-principles` | A matrix would assert independence that does not exist |
| The facts about what options exist are missing | **Research first**, then return | Populating from ignorance produces plausible-looking fiction |
| A single technical contradiction blocks progress ("fast, but it overheats") | `triz-contradictions` | Resolve the contradiction rather than enumerate around it |
| You need one decision under time pressure with clear criteria | `options-portfolio` or plain decision analysis | The box is overhead when the option set is already small |
| You want to reframe the problem itself | `lateral-thinking`, `question-storming` | Morphology works inside a fixed frame |

## Don't confuse with adjacent methods

- **SCAMPER** changes one object through seven prompts. Morphology **builds a space of objects** from independent parameters. SCAMPER produces 7–30 variations; a morphological box can produce hundreds, and its value is coverage plus pruning, not variation count.
- **Divergent thinking** is quantity-first and judgment-free. Morphology is structured from the start: dimensions constrain generation, and pruning/scoring follow. Divergence helps *populate* a difficult dimension; it is not a substitute for the box.
- **Options portfolio** starts from candidates and asks which set to carry. Morphology starts from dimensions and asks which combinations deserve to become candidates. They chain: box → sample → portfolio.
- **Scenario planning** explores a few plausible external futures. Morphology explores internal design choices. Combine them when the future changes which options are feasible (e.g., regulation × channel).
- **Design of experiments / covering arrays** are statistical cousins. Use them when combinations must be *tested* empirically at scale; morphology is for generating and reasoning about them first.

## Overkill signals

Morphology is the wrong tool when:

- Fewer than three live decisions exist — a 2×2 conversation is faster.
- The dimensions would have one real option each in practice (constraints dressed as choices).
- The decision is already made and the box would be post-hoc justification. This is the most common misuse: a "systematic" matrix that always lands on the preferred row. If the outcome cannot change, do not run the box.
- The team will not act on more than one combination. Then the method's only remaining value is documenting why the chosen combination is reasonable — write that directly.

## Handoff triggers

Morphology hands off to:

| Next | Trigger |
|---|---|
| `divergent-thinking` | A dimension has too few real alternatives — generate before structuring |
| `scamper` | One promising combination needs systematic variation before piloting |
| `concept-blending` | Two combinations from different corners should be fused into one concept |
| `options-portfolio` | The shortlist is ready and needs portfolio-level selection |
| `premortem` | A concept is chosen and needs failure analysis before commitment |
| `scenario-planning` | External uncertainty changes which options are feasible |
| `first-principles` | The dimension set keeps collapsing because the model of the problem is wrong |

## Anti-patterns

- **Box theatre** — presenting 256 combinations as rigor while the recommendation was decided in advance.
- **Dimension soup** — mixing user segments, features, and business models in one table; the cross-product is meaningless.
- **Enumeration without pruning** — dumping the product on a stakeholder and calling it analysis.
- **Ignoring the baseline** — no do-nothing/current option, so no combination can be judged as an improvement.
- **Treating combinations as validated** — a cell in a matrix is a hypothesis; only a probe upgrades it.
- **Rebuilding the org chart** — populating options only with what the current team already knows how to ship.
