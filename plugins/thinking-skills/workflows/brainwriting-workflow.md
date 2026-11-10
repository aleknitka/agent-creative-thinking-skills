# Brainwriting — Agent Workflow

Proves the catalog note: "Agent-based workflows may be useful for some methods" — single-conversation skills also work; this is the parallel-generation variant.

## Goal

Reproduce Rohrbach/Warfield brainwriting faithfully: **parallel generators, no cross-talk, synthesis owns the final artifact**. Demonstrates that subagents (one per slot) can stand in for human participants while the main agent enforces process.

## When this workflow fits

- Early voices anchor, loud voices dominate, or timezone spread makes a synchronous meeting costly.
- You need many distinct ideas (30–100) plus the build layer that compounding creates.

Otherwise use the single-conversation `brainwriting/SKILL.md` inside one session.

## Topology

```
Intake
 │
 ├─ Spawn N generators in parallel (task subagents)
 │   ├─ Generator A — pass 1, sheet A (silent, one idea per row, stable IDs)
 │   ├─ Generator B — pass 1, sheet B
 │   └─ Generator C — pass 1, sheet C  (N = 3–6; default 3 for AI)
 │
 ├─ Each generator also runs pass 2 on its own sheet (self-build, still silent)
 │
 ├─ Collect verbatim — no merging yet
 │
 ├─ Distribute & build — one or two rotations, each generator adds 1–3 ideas per other sheet
 │   (rule: builds must cite ID they build on; add, never overwrite)
 │
 └─ Freeze → synthesize (main agent owns it: cluster by mechanism, 3–6 clusters → 2–3 concepts + probes)
```

- **Integration owner:** main agent. Subagents do not see each other, do not vote, do not synthesize.
- **Max concurrency:** ≤ 32 subagents (hard cap); default 3 keeps output tractable; scale to 6 for large prompts.
- **No extra scripts:** the `scripts/brainwrite.py` template generator remains optional for sheet layout; workflow uses `task` + `wait`.

## Process (what each agent does)

### Main agent

1. Intake — prompt, constraints, horizon. Choose mode: `635` / `small` / `solo` / `async` (see `skills/brainwriting/references/procedure.md`). Default for AI: `small` (3 generators × 2 passes).
2. Spawn generators with: problem, constraints, forbidden: "do not see other sheets, do not evaluate, one idea per row, verbatim."
3. `wait` on all generators.
4. Distribute & build — assign each generator 1–2 other sheets to build on (one rotation for N=3).
5. Freeze → cluster by mechanism (not author), name each cluster, count, expectation 3–6 clusters from 30+ raw ideas.
6. Harvest 2–3 strongest clusters into one-paragraph concepts with smallest probe + keep/kill signal. Option: hand off to `premortem` or `options-portfolio`.

### Generator subagents

- Pass 1: 5–10 ideas, one per row, IDs `Px-1 … Px-N`, no talking.
- Pass 2 (self-build): extend own most interesting 2–3 ideas (2–3 additions per starting idea).
- Build pass: 1–3 ideas per received sheet, each prefixed `build on #<id> — …`.

## Interface contract

```yaml
Input to generator:
  prompt: "How might we …?"
  constraints: ["no new headcount", "limited EHR changes"]
  ids: P1|P2|P3

Output from generator (per pass):
  rows:
    - { id: "P1-3", text: "auto-fill cancellations via waitlist" }
    - { id: "P1-7", text: "build on #P2-3 — also send it by SMS" }

Final collect (owner synthesizes):
  clusters:
    - { theme: "Confirmed arrival", members: [P1-1, P1-4, ...], build_edges: ["P1-4→P1-1"] }
  concepts:
    - { cluster: C1, concept: "Two-touch confirmation loop", probe: "one site × 4 weeks, ≥60% confirmed at 24h" }
```

## Launch sketch (Codex / Claude Code)

```python
# main agent spawns parallel generators; then waits
tasks = [
  dict(name=f"Brainwriter{i+1}", task=f"Run brainwriting pass 1+2 for problem: {prompt} ...",
       agent="sonic", solutionSpace="one fix: scaffold brainwriting sheet, IDs given")
  for i in range(3)
]
# wait, then one distribute-and-build round, then freeze→cluster→harvest in main agent
```

`agent: sonic` is the low-reasoning mechanical worker; `scout` is read-only and must not be used here (generation required). Tool `task` receives `tasks[]` in one batch so launches fan in parallel.

## Verification

- Raw count (30–40 written rows) preserved verbatim before clustering; duplicate detection via exact/near-duplicate note in cluster.
- Build edges tracked — every concept traces to cited IDs.
- Anti-patterns from `when-not-to-use.md` checked: no comments during generation, no premature summary after pass 1, no circulating examples.

## Progressive disclosure

- This file is the workflow layer; the single-conversation skill `skills/brainwriting/SKILL.md` stays the hub for the method.
- Skill `references/procedure.md` + `examples.md` (clinic 18→3 trace) remain the method detail; workflow adds only the parallel orchestration.

## References

- `skills/brainwriting/SKILL.md` + `references/procedure.md` (6-3-5, rotations, async variant)
- `workflows/six-thinking-hats-workflow.md` — sequential contrast workflow
- `examples/gallery.md` — runnable prompts linking here
