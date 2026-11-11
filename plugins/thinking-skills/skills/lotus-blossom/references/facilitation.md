# Facilitation — Solo, AI-Agent, and Team

Lotus Blossom is a filling exercise, so facilitation is mostly about protecting the board's geometry: one theme, eight distinct petals, eight concrete slots per petal. Everything below serves that.

## Solo mode

One person fills all nine blocks. Use a timer per petal (2–3 minutes) and a hard rule against editing earlier cells.

1. State the theme and constraints on a separate line, visible while writing.
2. Write the eight petals in one pass; do not start layer 3 until the ring is stable.
3. Fill petals in the order that feels least familiar first. The familiar petals are easiest and eat the session.
4. When a slot stalls, apply the next expansion operation rather than forcing a "good" idea.
5. Prune and score in a second sitting if possible; same-sitting scoring favours recency.

Solo bias to watch: the first petal tends to absorb 40% of total writing time. Enforce equal blocks.

## AI-agent mode

An agent can fill 72 slots quickly, which is exactly the risk: volume without variety. Structural rules that keep it honest:

- **Generate layer by layer, stop between layers.** Ask for petals first, confirm they are distinct, then expand one petal at a time. A single "give me 72 ideas" request produces paraphrases.
- **Constrain each slot** to actor + action + artifact, or a mechanism label. Reject "improve onboarding" as a slot.
- **Force mechanism diversity per petal** by walking the eight expansion operations explicitly.
- **Keep IDs** (`2.5`) so later pruning and scoring can cite slots without re-quoting them.
- **Separate generation from critique** into different passes or different agents. Do not let the generator rank its own output in the same call.
- **Deduplicate mechanically** across petals before scoring; agents repeat ideas under different angles more often than people do.

A useful split: one agent fills the board from the theme, a second agent (or a second pass with a fresh context) prunes and scores against criteria fixed in advance. See the repository's orchestration guidance if you are running multiple agents.

## Team mode

Physical or shared-board sessions usually run 25–40 minutes with 3–6 people.

- **Center and petals together (5 min).** The group agrees the theme and the eight angles. This is the only negotiation; it prevents eight people filling eight different boards.
- **One petal per person (15–20 min).** Each participant owns a petal block and fills its eight cells alone. Silent, same rule as brainwriting: writing before talking.
- **Gallery pass (5 min).** Blocks are read in ring order without defence. Participants add one idea per block on sticky notes, labelled with their initials.
- **Prune and dot-vote (5–10 min).** Merge duplicates, cut infeasible slots aloud with a reason, then dot-vote on the survivors. Voting is the first evaluation step and happens only after all blocks are read.

Equal-size blocks matter more in groups: a senior participant's petal will otherwise get three times the elaboration of everyone else's.

## Colour coding

If you have three colours (pens, sticky notes, or text labels), use them consistently:

| Colour | Meaning | Rule |
|---|---|---|
| Neutral / black | raw idea slots | written during generation only |
| Green | assumption or unknown | mark the slot; it needs a probe, not a defence |
| Red | cut or constraint violation | added only during pruning, never during generation |

A text equivalent: suffix slots with `[?]` for assumption and `[x]` for pruned, and add a one-line reason next to each `[x]`. Colour is a retrieval aid, not a scoring system — do not use red/green as a quality judgement during layer 3.

Optional fourth colour: blue for "builds on 3.4" cross-links, so a merged idea keeps its lineage visible.

## Boards and artifacts

- **Physical:** nine 3×3 blocks on one sheet or a wall grid; the theme block stays in the middle.
- **Digital:** a 3×3 grid of 3×3 tables; one table per petal, theme in the centre table's middle cell.
- **Text:** the generator (`scripts/lotus.py`) prints either the block board or a numbered text list; the text list is easier to prune, the board is easier to scan.

Keep the raw board until scoring is finished. A pruned list without the original slots loses the evidence that the space was covered.

## Keeping variety honest

Three checks, in order:

1. **Petal check:** read the eight petal names aloud. If two could be swapped without changing any idea, merge or replace.
2. **Block check:** within a petal, name the mechanism of each of the eight slots in three to six words. Fewer than five distinct mechanisms means the block is paraphrased.
3. **Board check:** across all petals, count how many slots are "in-product, at first login". If more than a third, the board is over-farmed in one region; fill the thin petals deliberately.

Record the checks' results next to the board. They are the difference between 72 ideas and 72 sentences.

## Anti-anchoring rules

- Do not show example ideas before layer 3 is full; examples become the template.
- Read petals in ring order, not in the order they were written.
- Do not let the facilitator's petal be the first one expanded.
- In AI mode, do not seed the prompt with the team's favourite idea; it will bloom into 64 variants of it.
- Keep a parking lot for critiques; move them there and continue filling.
