# Structure Mapping and Its Pitfalls

This reference adapts structure-mapping theory to a practical worksheet. The core claim: an analogy is a correspondence between **relations**, and a good mapping is systematic — it prefers a connected system of relations over isolated similarities.

## Align relations, not objects

| Match type | Example | Verdict |
|---|---|---|
| Object similarity | Both involve "tickets" | Weak; often a false friend |
| Attribute similarity | Both are "high volume" | Weak; says nothing about behavior |
| First-order relation | Tickets wait in a queue in both | Useful start |
| Higher-order relation | A queue grows, which raises wait time, which increases abandonment, which reduces load | Strong; carries causal structure |

Prefer mappings where a **chain** of relations lines up. One deep chain supports inference; ten loose object matches do not.

## The mapping table

Write this before judging the analogy.

| Source element | Relation it participates in | Your element | Relation holds? | Notes / mismatch |
|---|---|---|---|---|
| Triage nurse | Classifies arrival before treatment | Intake reviewer | Partly | Source has measured vitals; yours has self-reported severity |
| Acuity scale | Converts observations to priority | Severity rubric | No | Source scale is validated; yours is not |
| Resuscitation bay | Reserved capacity for worst cases | Escalation lane | Yes | Both are protected from routine work |

Every row must name a relation. "Nurse → reviewer" alone is an object match and earns nothing.

## Procedure

1. **List source relations** from a credible description: what causes what, what must precede what, what regulates what.
2. **Match candidates** in your problem. Mark each relation as holds, holds with adaptation, or absent.
3. **Check systematicity.** Do the matched relations connect into a coherent system? A cluster of connected matches is more trustworthy than the same number of scattered ones.
4. **Generate candidate inferences.** What follows in the source that you have not considered locally? Mark these as hypotheses, not facts.
5. **Test the inferences against your constraints.** Reject inferences that depend on a source condition you lack.
6. **Name the mechanism.** One sentence: "X achieves Y by Z, because W."

## Breakpoint analysis

For every source dependency, fill one row. This is where most analogies actually die, and where the useful ones become precise.

| Dependency | Source value | Your value | Consequence if different | Verdict |
|---|---|---|---|---|
| Failure cost | High; errors can kill | Low; errors are reversible | Source over-invests in checks | Adapt: reduce checkpoints |
| Information quality | Measured vitals at intake | Self-reported, gameable | Acuity score unreliable | Fails: need independent signal |
| Authority to redirect | Legal mandate | Voluntary customers | Cannot force routing | Adapt: incentives instead |
| Scale | 200 arrivals/day | 20/day | Dedicated lane underused | Fails: share capacity |

Verdicts are **holds**, **adapt**, or **fails**. Do not average them into "promising." A single failed load-bearing dependency can invalidate the transfer even when everything else matches.

## Pitfalls

- **Surface copy.** Importing visible features (signs, colors, dashboards) while missing the causal mechanism (checkpoint verification, escalation authority).
- **Object substitution.** Mapping "nurse" to "reviewer" and stopping there. No relations, no inference.
- **Single-feature analogy.** Building the whole argument on one shared attribute such as "both are high-stakes."
- **Overextension.** Applying the source mechanism beyond the conditions that made it work, without marking the boundary.
- **Causal mismatch.** Source relation is "A reduces B"; your context has "B reduces A" (e.g., feedback that stabilizes versus feedback that amplifies).
- **False inference.** Treating a source detail as necessarily true locally because the analogy is appealing.
- **Source romanticism.** Describing the source field as flawless. Real domains have workarounds, politics, and failure modes too.
- **Metric transfer.** Importing the source's success metric, which may reward the wrong behavior in your context.

## Quality checks

- Can you state the mechanism without naming either domain? If not, it is not yet abstract.
- Does the mapping predict something you did not already believe? If not, it is decoration.
- Can you name the condition under which the transfer fails? If not, you have not done step 5.
- Is the probe cheaper than the decision it informs? If not, shrink it.
- Would a practitioner of the source domain recognize your description as fair? If not, verify before using it.
