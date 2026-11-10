---
name: brainwriting
description: Generate ideas in writing before discussing or evaluating them, then build on earlier contributions in structured passes. Use when early suggestions anchor the group, loud voices dominate, or you need distinct idea batches followed by combinations — separate written generation from evaluation.
---

# Brainwriting

Ideas go on paper before anyone speaks. Writing in parallel means no one's first suggestion becomes the group's frame, quiet participants contribute at full strength, and every idea is recorded verbatim for later building.

The failure mode it prevents is the meeting where the first confident voice sets the direction and the rest of the hour is spent elaborating it.

## When to use

- Early suggestions are anchoring the discussion, or one or two people dominate the floor.
- You need many distinct ideas, not a polished few.
- The group is mixed in seniority, language confidence, or temperament, and you want equal contribution.
- You want a second layer of combinations and extensions, not just a first batch.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- The problem is not yet concrete enough to write about → scope or `question-storming` first.
- You have a baseline and want targeted variations → `scamper` or `morphological-analysis`.
- You need a decision among known options → evaluation method, not another divergence pass.
- Real-time synthesis and shared energy matter more than idea count → facilitated verbal brainstorming, accepting its anchoring cost.

## Process

1. **Intake — reuse before you ask.** Write the prompt in 3–5 sentences: the problem, who it is for, constraints, and what has already been tried. Choose a mode — synchronous 6-3-5, small-team passes, solo, or async — and set a quantity target. Do not circulate example ideas: they anchor the room. See [references/procedure.md](references/procedure.md).

2. **Silent pass 1 — generate alone.** Each participant writes 3–5 ideas on their own sheet or board, one per row, timed (5–10 min). No talking, no peeking, no editing. Record verbatim; incomplete fragments are fine. See [references/facilitation.md](references/facilitation.md).

3. **Silent pass 2 — build on your own.** A second timed pass (5 min) over your own pass-1 list: extend, combine, and vary the entries you find most interesting. Aim for 2–3 additions or mutations per starting idea. Still no discussion — this pass adds depth without importing anyone else's frame.

4. **Distribute and build.** Rotate sheets (clockwise in 6-3-5) or open a shared board. Each participant adds 1–3 ideas per sheet: new ideas sparked by what is written, or a labelled build ("builds on #7 — also send it by SMS"). Rule: add, never replace or delete. One or two rotations is enough for small groups. See [references/procedure.md](references/procedure.md).

5. **Cluster.** Freeze generation. Merge duplicates, group by theme or mechanism, name each cluster, and count. Expect 3–6 clusters from 30+ raw ideas; do not vote yet. See [references/clustering.md](references/clustering.md).

6. **Harvest and probe.** Elaborate the strongest 2–3 clusters into one-paragraph concepts with a concrete mechanism. For each concept define the smallest probe — the cheapest action that produces evidence — plus the signal that would make you keep or kill it. Hand off to evaluation, `premortem`, or another divergence pass as needed. See [references/examples.md](references/examples.md).

### 6-3-5 variant

Six participants, three ideas each, five minutes per round, sheets passed clockwise; six rounds yield 108 idea slots in about 30 minutes. Use the full protocol when the group is available and the problem benefits from many contributors. Fewer people: keep 3 ideas and 5 minutes, reduce sheets, or run the same rotation with 4–5 participants. See [references/procedure.md](references/procedure.md) and [scripts/brainwrite.py](scripts/brainwrite.py).

### Async variant

Use a shared document or board with one column per participant and numbered rows. Announce a silent generation window (e.g., 24–48 hours), then a build window in which everyone adds entries prefixed with `build on #⟨id⟩:`. No comments, chat, or reactions during generation. Facilitator freezes the board, clusters offline, and circulates the cluster names before any discussion. Async trades speed for timezone and schedule independence.

## Rules

- Write before you speak — including the facilitator and the most senior person.
- Generation and evaluation never share a pass; no "that won't work" until clustering is done.
- One idea per row, verbatim, with stable IDs (P1-3, sheet 2-#7) so builds can cite them.
- Add, do not overwrite; builds must name what they build on.
- Quantity first: aim for the target count before judging quality.
- Keep variety honest: distinct mechanisms, not rewordings.
- Label fact / assumption / speculation; written ideas are hypotheses, not commitments.
- Honest provenance: attribute 6-3-5 to Rohrbach and the structured-group lineage to Warfield; call adaptations adaptations. See [references/provenance.md](references/provenance.md).

## Going deeper

- Full procedure, timing, and pass structure: [references/procedure.md](references/procedure.md)
- Facilitation — anti-anchoring, quiet-first rules, solo and AI mode: [references/facilitation.md](references/facilitation.md)
- Clustering written ideas: [references/clustering.md](references/clustering.md)
- Worked example (two passes, 18 ideas → 3 concepts): [references/examples.md](references/examples.md)
- When not to use + handoff map: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance and evidence limits: [references/provenance.md](references/provenance.md)
- Sheet and rotation template generator (offline): [scripts/brainwrite.py](scripts/brainwrite.py)
- Agent workflow — parallel generators + synthesis owner: [workflows/brainwriting-workflow.md](../../workflows/brainwriting-workflow.md)
- Shared workspace — sticky notes, lanes, drawing, votes: [workspace/index.html](../../../../workspace/index.html)
