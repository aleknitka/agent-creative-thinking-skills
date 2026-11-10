# Rebuilding Heuristics — From Fundamentals to Alternatives

## Start from invariants

Begin with what must be true — latency bounds, conservation, access, information — and sketch the simplest mechanism that satisfies them. Add nothing else until it earns its place.

## Add back selectively

For each inherited constraint you set aside, ask: does restoring it improve the design on a dimension that fundamentals alone miss (trust, adoption, cost, risk)? If yes, keep it; if merely familiar, leave it out and note the risk you accept.

## Generate 2–3 rebuilt approaches

Each approach must:

- satisfy all fundamentals and observed facts;
- use a different mechanism or structure (not just a different parameter);
- state which inherited constraints it keeps and which it drops.

Prefer one approach that is minimal (fewest added constraints), one that reuses a known pattern but justifies it, and one that is deliberately strange yet still fundamental-sound. The strangeness tests whether fundamentals alone already suggest a better shape.
