# Tracing Consequences — Rings, Sweeps, and Loops

A world sketch lists what changes. Tracing asks what those changes cause, and what those causes cause. Use a futures-wheel structure without pretending it is a forecast: every ring is a hypothesis about this fictional world.

## Ring structure

| Ring | Time scale | Question | Example |
|---|---|---|---|
| **First order** | days–weeks | What happens directly because the premise is true? | Documentation is captured from every answered question. |
| **Second order** | months | How do people and systems adapt to the first-order effects? | Support staff stop writing pages; they curate captured answers. |
| **Third order** | years | What norms, institutions, or power structures change? | "Knowing where the answer lives" stops being a status signal. |

Rules:

- Trace at least **three rings** before judging.
- Each ring should contain at least one **positive** and one **negative** consequence.
- Stop when a ring only restates earlier effects — that is saturation, not depth.
- Keep the rings separate. Mixing first- and third-order claims hides weak causal links.

## Sweep categories

After the rings, sweep the world through these lenses so you do not trace only the effects you find interesting:

| Lens | Ask |
|---|---|
| **Behavior** | What do people do differently, including workarounds? |
| **Economics** | Who pays, who saves, what gets priced differently? |
| **Incentives** | What becomes rewarded or punished? |
| **Power** | Who gains discretion, visibility, or leverage? |
| **Risk** | What new failure modes, dependencies, or single points appear? |
| **Equity** | Who is helped, burdened, or excluded? |
| **Environment** | What material, energy, or attention costs move? |
| **Trust** | What must be verified that was previously assumed? |

Not every lens applies. Skipping one should be a choice, not an oversight.

## Feedback loops

Name at least one loop and its direction:

- **Reinforcing** — the effect amplifies itself. *More captured answers → better search → more use → more captured questions.*
- **Balancing** — the effect limits itself. *More pages → harder quality control → lower trust → less use.*

Loops are often the most transferable part of a world: the loop can exist under current conditions even when the premise cannot.

## Causal honesty

Label every link:

- **Mechanistic** — the consequence follows from a described mechanism.
- **Plausible** — supported by a known pattern, but untested here.
- **Speculative** — an imaginative leap.

Do not let a speculative third-order claim carry the insight. If the transferable idea depends only on speculation, mark it as a hypothesis to test.

## Trace template

```
World: <premise>

First order (days–weeks):
+ ...
- ...

Second order (months, actors adapt):
+ ...
- ...

Third order (years, norms/institutions shift):
+ ...
- ...

Sweep:
- Behavior: ...
- Economics: ...
- Incentives: ...
- Power: ...
- Risk: ...
- Equity: ...
- Environment: ...
- Trust: ...

Loops:
- Reinforcing: ...
- Balancing: ...

Most robust link: <the consequence with the strongest mechanism>
Weakest link: <the consequence carrying too much speculation>

Candidate insights:
1. ...
2. ...
```

## Worked trace (abbreviated)

World: *What if there were no knowledge-base interface — knowledge arrived inside the tools where work happens?*

- **First order:** (＋) answers surface with less search effort; (−) users cannot browse or judge coverage.
- **Second order:** (＋) documentation is written for retrieval, not for pages; (−) content teams lose a shared surface to spot gaps; (＋/−) vendors' assistants become the real front door.
- **Third order:** (＋) knowledge quality becomes measurable by answer accuracy; (−) whoever controls the assistant controls the organization's memory.

Sweep: power concentrates with the assistant owner; trust shifts from "the wiki says" to "the assistant cited"; equity favors people already inside the workflow.

Loops: reinforcing — more in-flow questions → more captured answers → better retrieval; balancing — more automated answers → more silent errors → lower trust.

Transferable candidate: **measure knowledge by answer correctness at the point of need, not by page views.** This survives without the impossible premise.

Move to [examples.md](examples.md) for three complete worlds on one problem, or back to [SKILL.md](../SKILL.md) for step 5.
