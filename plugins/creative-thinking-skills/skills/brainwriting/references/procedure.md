# Procedure — Passes, Timing, and the 6-3-5 Protocol

Brainwriting is a family of protocols, not one fixed script. All of them share the same skeleton: independent written generation, a build pass over existing material, then clustering. The 6-3-5 variant adds strict sheet rotation.

## The core pass structure

| Pass | What happens | Time | Output |
|---|---|---|---|
| Intake | Prompt, constraints, mode, target, sheet setup | 10–15 min | One written prompt everyone can see |
| Silent pass 1 | Each person writes alone, no discussion | 5–10 min | 3–5 ideas per person, verbatim |
| Silent pass 2 | Each person extends and mutates their own list | 5 min | 2–3 additions/mutations per starting idea |
| Distribute & build | Sheets rotate; participants add to others' ideas | 5–10 min per rotation | Builds labelled with the ID they extend |
| Cluster | Freeze, merge, group, name | 15–20 min | 3–6 named clusters |
| Harvest & probe | Elaborate 2–3 concepts; define cheapest probe | 20–30 min | Concepts, probes, owners |

The two solo passes matter. Pass 1 produces breadth; pass 2 produces depth on the writer's own strongest threads before any external idea can redirect them. The build pass then imports other frames deliberately, with attribution, instead of accidentally through conversation.

## The 6-3-5 protocol

Numbers: **6 participants, 3 ideas each, 5 minutes per round**. Sheets pass clockwise. Six rounds produce 6 sheets × 18 entries = **108 idea slots** in about 30 minutes of writing, excluding briefing and clustering.

1. **Prepare sheets.** One sheet per participant. Six rows, each row with three numbered cells: `#1a #1b #1c` through `#6a #6b #6c`. Put the prompt and participant ID in the header.
2. **Round 1 (5 min).** Each participant writes three ideas in row 1 of their own sheet — one per cell, a phrase or sentence, legible enough for a stranger to read.
3. **Rotate clockwise.** Everyone passes their sheet one seat clockwise and receives a neighbour's sheet.
4. **Rounds 2–6 (5 min each).** Read the existing entries, then write three new ideas in the next empty row: stimuli, extensions, or combinations prompted by what is already there. Do not cross out, rewrite, or "improve" earlier entries.
5. **Stop after six rounds.** Every sheet has passed through six pairs of hands and is full. Collect all sheets; do not discuss while collecting.
6. **Transcribe and cluster.** Number every entry globally (sheet, row, cell) before sorting. Keep the original wording.

### Why five minutes

Five minutes is short enough to prevent perfectionism and long enough to produce three ideas. Let the facilitator call time; do not let discussion leak into a round. If a group is new to the method, allow one practice round on a trivial prompt (e.g., "uses for a brick") to calibrate.

### Rotating the other way, and other mechanics

- Passing **left vs. right** makes no difference; pick one and keep it consistent so nobody receives their own sheet twice before the end.
- With fewer than six participants, reduce the sheet count and run the same number of rounds; total ideas scale roughly linearly. With four people, expect about 72 slots over six rounds.
- With more than six, run parallel tables of six rather than enlarging the circle; a table of eight makes rounds slow and reading hard.
- If a participant stalls, they may write a question or a constraint instead of an idea — both are legitimate raw material — but not a critique of an existing entry.
- Facsimile, shared files, or a whiteboard grid work; the physical pass is not sacred, only the silence and the build-on-existing rule are.

## Small-team variant (3–5 people)

1. Silent pass 1: 5 ideas each, 7 minutes.
2. Silent pass 2: extend own list, 5 minutes.
3. One rotation: pass sheets once, add 2 ideas per sheet, 5 minutes. Optional second rotation if energy is high.
4. Cluster together, reading every entry aloud once before grouping (each entry read by someone other than its author where authorship is known).
5. Harvest 2–3 concepts; assign a probe per concept.

Total: 45–60 minutes for four people, roughly 25–35 raw ideas.

## Solo variant

1. Timed pass 1: 10 ideas in 10 minutes, no editing.
2. Timed pass 2: pick the five most interesting entries and write two mutations of each.
3. Deliberate "other person" pass: add the ideas a sceptical operator, a new customer, and a budget owner would write. Label these as simulated perspectives, not real ones.
4. Cluster, then probe. Do not skip the second pass; solo brainwriting collapses into a list without it.

## Async variant

| Phase | Duration | Rule |
|---|---|---|
| Brief | Before the window | Prompt, constraints, target, and board link posted once; no examples |
| Silent generation | 24–48 h | Each person owns a column; no reading other columns if the tool allows hiding them |
| Build | 24 h | Read everything; add entries prefixed `build on #⟨id⟩:` |
| Freeze | Facilitator action | Lock the board, export a snapshot, announce the freeze |
| Cluster | 60–90 min | Facilitator or small group clusters; circulate names before discussion |
| Discussion | 45–60 min | Start from clusters, not from the raw board |

In async mode the anti-anchoring guarantee is weaker — people can read early entries before writing — so hide columns during generation where possible, or use simultaneous submission into a form that only the facilitator can see until the window closes.

## Sheet layout

```
Problem: ______________________________________________  Participant: P3
--------------------------------------------------------------------------
Round 1 | 1a ....................... | 1b ....................... | 1c ........
Round 2 | 2a ....................... | 2b ....................... | 2c ........
...
Round 6 | 6a ....................... | 6b ....................... | 6c ........
```

Generate a filled-in version with `scripts/brainwrite.py`:

```
python scripts/brainwrite.py --problem "reduce clinic no-shows" --people 6
python scripts/brainwrite.py --mode small --people 4 --json
```

## Timing summary

| Setting | People | Writing time | Total session |
|---|---|---|---|
| Full 6-3-5 | 6 | 30 min (6 × 5) | 75–90 min |
| Small team | 3–5 | 15–20 min | 45–60 min |
| Solo | 1 | 15 min | 30–40 min |
| Async | 4–12 | 24–48 h window | 2–3 h facilitator time |

## What goes wrong

- **Silent pass 2 skipped.** The list stays shallow and the build pass has nothing strong to extend.
- **Rounds turn into conversation.** A single "oh, like…" restarts social anchoring. Enforce silence with a timer.
- **Sheets collected too late.** Someone summarises aloud while stacking; the clustering then anchors on that summary.
- **Illegible entries.** Require one idea per cell and a dark pen; transcribe before clustering.
- **Six rounds with a tired group.** Drop to four rounds rather than let quality collapse; record the reduced target.
- **No IDs.** Builds cannot cite their source, and clustering loses provenance.
