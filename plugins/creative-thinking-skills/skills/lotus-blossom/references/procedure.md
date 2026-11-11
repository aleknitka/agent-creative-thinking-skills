# The Three-Layer Procedure

Lotus Blossom is a radial worksheet, not a free brainstorm. The geometry does the work: a theme in the center, eight petals around it, and eight slots around each petal. At eight petals that is 8 + 64 = **72 idea slots**, all reachable from one theme.

The method comes from Japan (see [provenance.md](provenance.md)). The standard physical form is a 3×3 grid of 3×3 blocks: nine small boards arranged as one big board, with the theme in the middle block.

## Board layout

Nine blocks in a 3×3 arrangement. Each block is itself a 3×3 cell.

```
        +-------------------+
        |  1  2  3 | 4  5  6 |
        |  4  P1 5 | 7  P2 8 |     P1..P8 = the eight petals
        |  6  7  8 | 9 10 11 |
        +----------+---------+
        |  ...     |  ...    |
        |  P8      | THEME   |     center block = the theme
        |  ...     |  ...    |
        +----------+---------+
```

Read it as layers:

| Layer | Sits in | Content | Count |
|---|---|---|---|
| 1 | center | the theme, stated once | 1 |
| 2 | ring around center | eight petals — distinct angles on the theme | 8 |
| 3 | each petal's own 3×3 block | eight concrete ideas per petal | 64 |

The center block's eight cells hold the petal labels. Each petal then becomes the center of its own block, written in the middle of that block, with eight ideas around it. A full board is nine small grids.

```
+----+----+----+   +----+----+----+
| 1  | 2  | 3  |   | 1  | 2  | 3  |
+----+----+----+   +----+----+----+
| 4  | P1 | 5  |   | 4  | P2 | 5  |   ... one block per petal
+----+----+----+   +----+----+----+
| 6  | 7  | 8  |   | 6  | 7  | 8  |
+----+----+----+   +----+----+----+
```

Use `scripts/lotus.py --theme "…" --export board` to print this structure, or `--fill blank` for an empty worksheet to fill by hand.

## Timing: 25–40 minutes

A workable rhythm for a facilitated or solo session:

| Phase | Time | What happens |
|---|---|---|
| Intake and center | 3–5 min | theme, audience, success, constraints, existing attempts |
| Layer 2 — petals | 3–5 min | write the eight angles; test they are distinct |
| Layer 3 — per petal | 2–3 min each (16–24 min) | eight concrete ideas in that petal's block |
| Prune and cluster | 3–5 min | merge duplicates, cut infeasible, group by petal |
| Score | 3–5 min | 3–5 criteria fixed at intake |
| Harvest and probe | 5 min | top five, each with a next probe |

Total: **25–40 minutes** depending on domain complexity and whether the board is filled by one person or a group. Do not extend layer 3 by stealing time from pruning; an unpruned 72-slot board is a wall of text, not a result.

At eight petals, budget roughly 2 minutes per petal. Longer than 3 minutes per petal usually means the group is elaborating the first idea instead of filling the block.

## Layer 1 — the center

Write the theme as one phrase or one "How might we…" question. It must fit in a single cell and be stable for the whole session. Record alongside it:

- **Audience and moment:** who is doing what when the idea intervenes.
- **Success:** one sentence, loose.
- **Hard constraints:** budget, law, brand, platform, deadline.
- **Already tried:** two or three approaches, so petals do not reproduce them.
- **Fact / assumption / speculation:** one line each; the board will generate mostly speculation.

A theme with an "and" in it is two themes. Split it or pick one.

## Layer 2 — the eight petals

A petal is an angle or sub-theme, not an idea. It partitions the theme so the eight blocks do not overlap. A default set that works across domains:

| Petal | Angle |
|---|---|
| Actors | who does the work, who is affected, who is missing |
| Moment | when in the journey, and what precedes it |
| Place | channel, environment, physical context |
| Mechanism | how it works, step by step |
| Incentive | what makes someone want it or stop avoiding it |
| Artifact | object, document, or interface that carries it |
| Constraint | which limit could be removed, moved, or used |
| Signal | how anyone would know it worked |

Domain-specific sets are better when they exist: for onboarding, petals might be *first login, first value, first week, social, support, pricing, data, habit*. The test is the same: could two petals produce the same idea? If yes, replace one.

Five petals are acceptable when the domain only yields five distinct angles; do not pad with synonyms to reach eight. Report the reduced count honestly (e.g. 5 + 40 idea slots).

## Layer 3 — eight ideas per petal

Take one petal at a time. Put the petal label in the center of its 3×3 block and fill the eight surrounding cells with concrete ideas. Eight expansion operations keep the block from becoming eight restatements:

1. **First concrete idea** — the obvious workable one.
2. **Add** — a missing actor, step, resource, or touchpoint.
3. **Remove** — omit the element entirely; keep the rest unchanged.
4. **Invert** — flip the direction, default, order, or incentive.
5. **Combine** — join it with a neighbouring step, idea, or channel.
6. **Magnify** — 10× frequency, scope, intensity, or duration.
7. **Minify** — toward zero cost, effort, time, or footprint.
8. **Delegate** — a different actor, machine, or community does it.

These are prompts, not required slots. If a stronger idea appears, write it and put the unused operation in a parking lot.

## Pruning, scoring, harvesting

**Prune.** Merge duplicates across petals (the same idea often appears under two angles). Cut slots that violate a hard constraint. Keep a one-line reason per cut; the pattern of cuts tells you which petals were fantasy and which were real.

**Score.** Fix 3–5 criteria during intake, before any idea exists. Score survivors 1–5 per criterion and keep raw slots beside the scores. Do not introduce a new criterion after seeing a favourite; that is retrofitting.

**Harvest five.** Not one. A portfolio of five with different mechanisms is more informative than a single winner, and the probes are cheap. For each: one-paragraph concept, strongest assumption, smallest probe, kill signal. If a probe is not affordable, the slot is not ready to be a recommendation.

See [examples.md](examples.md) for a full worked board and [when-not-to-use.md](when-not-to-use.md) for handoffs.

## Common failure modes

- **Center creep** — the theme quietly changes between petals, so the board measures nothing.
- **Petal synonyms** — eight names for the same angle; the board is one block repeated.
- **Three-and-done** — each petal gets the obvious three ideas and the board is abandoned half-full.
- **Slogan slots** — "make it delightful" in cell 3.2. No actor, no mechanism, no probe.
- **Evaluation inside generation** — crossing out during layer 3; the board shrinks to what is already believed feasible.
- **All 72 treated as candidates** — no pruning, so the session ends with a wall and no shortlist.
- **Single winner** — harvesting one idea from 72 without probes; the structure produced options, not evidence.
