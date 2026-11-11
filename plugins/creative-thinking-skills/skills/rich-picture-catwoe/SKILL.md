---
name: rich-picture-catwoe
description: Build a visual rich picture of the messy situation and define it rigorously with CATWOE — Customers, Actors, Transformation, Worldview, Owners, Environment — to surface worldviews and root definitions before modeling. Use when the situation is messy, stakeholders see it differently, or no shared picture exists.
---

# Rich Picture + CATWOE

Draw the mess, then define the system. A rich picture makes the situation visible — actors, flows, tensions, concerns — before any model is imposed; CATWOE turns that picture into a testable root definition.

The failure mode it prevents is modeling or improving a system that no one has pictured together, so worldview clashes stay hidden until an intervention fails.

## When to use

- The situation is messy with no shared picture of actors, flows, and tensions.
- Stakeholders see the problem differently and worldview clashes are suspected.
- You need a root definition before building a model or mapping stakeholders.

If unsure this is the right method, start with [thinking-router](../thinking-router/SKILL.md) — or see [references/when-not-to-use.md](references/when-not-to-use.md).

## When NOT to use (brief)

- A clear, agreed problem statement already exists → validate it, not redraw it.
- You need causal feedback analysis → `causal-loop-diagram`.
- Near commitment and need to harden → `premortem`.

## Process

1. **Intake — name the situation of concern.** State where it is, who cares, and what feels stuck (3–5 sentences). Mark what is observed vs. interpreted. See [references/rich-picture.md](references/rich-picture.md).

2. **Draw the rich picture.** Sketch actors, structures, processes, flows, tensions, and concerns on one page. Capture worldview hints as thought bubbles. Keep it visual; labels are annotations. See [references/rich-picture.md](references/rich-picture.md) and [scripts/rich_picture.py](scripts/rich_picture.py).

3. **Examine with CATWOE.** For one candidate system in the picture, fill Customers, Actors, Transformation, Worldview, Owners, Environment. Each component must be observable or stateable; worldview is the assumption that makes the transformation meaningful. See [references/catwoe.md](references/catwoe.md).

4. **Write the root definition.** Compose: "A system owned by [O], operated by [A], to transform [input→output] for [C], under worldview [W], within constraints [E]." Test it against the picture.

5. **Compare and debate.** Show the picture and CATWOE to those whose worldviews differ; note where the picture reveals a conflict that CATWOE makes explicit. Record dissent.

6. **Decide next — probes or models.** For the gap between current situation and root definition, name the smallest probe or the handoff to `stakeholder-perspectives`, `soft-systems-methodology`, or `systems-mapping` work. See [references/examples.md](references/examples.md).

## Rules

- The picture comes before the definition — drawing first prevents premature modeling.
- CATWOE worldview must be stated: "W = …" — an unspoken W hides the design bet.
- One system per CATWOE — do not blend multiple transformations into one definition.
- Every CATWOE component must be observable or stateable; no vague "everyone" for Customers.
- Label fact / assumption / speculation; the rich picture is observed, the root definition is proposed.
- Honest provenance: attribute Rich Picture and CATWOE to Checkland and the SSM tradition; call this workflow an adaptation. See [references/provenance.md](references/provenance.md).

## Going deeper

- Rich picture — what to draw and how: [references/rich-picture.md](references/rich-picture.md)
- CATWOE — components, test, and root definition: [references/catwoe.md](references/catwoe.md)
- Comparing picture and CATWOE in debate: [references/debate.md](references/debate.md)
- Worked example (clinic capacity → picture → CATWOE → root definition → probe): [references/examples.md](references/examples.md)
- When not to use — triage vs causal-loop / stakeholder: [references/when-not-to-use.md](references/when-not-to-use.md)
- Provenance, lineage, and evidence limits: [references/provenance.md](references/provenance.md)
- Rich picture and CATWOE helper (offline): [scripts/rich_picture.py](scripts/rich_picture.py)
