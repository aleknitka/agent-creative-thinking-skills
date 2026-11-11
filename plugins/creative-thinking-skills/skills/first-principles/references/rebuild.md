# Rebuilding from Fundamentals

Input: the irreducible outcome plus the minimum fundamental constraint set. Output: two or three distinct feasible approaches, each with its assumptions, costs, and cheapest test.

## Start from the invariant, not the components

Write the outcome and invariants at the top. Design the smallest mechanism that satisfies them. Then add constraints back one at a time only when evidence or a test demands it, recording the reason.

Useful opening questions:

- What is the smallest system that produces the outcome?
- What would we build if the current tooling and org chart did not exist?
- Which actor is closest to the value moment, and why are they not doing it?
- Which step exists only to compensate for a limitation we no longer have?
- What is the cheapest irreversible step, and can it be moved later?

## Add back only what is needed

For every optional constraint, state what it protects, what it costs, who owns it, and what evidence supports it. If the evidence is missing, leave it out of the first design and flag the risk. Constraints added for comfort or familiarity are preferences and should be labeled as such.

Keep a **re-add log**:

| Constraint | Fundamental? | Why added | Evidence | Cost | Owner |
| --- | --- | --- | --- | --- | --- |

The log is the defense against rebuilding the old system by accident.

## Heuristics for genuinely distinct alternatives

Vary one fundamental axis at a time, not the styling:

- **Unit of value.** Outcome, artifact, access, or guarantee. What exactly does the user receive?
- **Actor.** Self-serve user, peer, expert, marketplace, or automation. Who performs the expensive step?
- **Channel and medium.** In-product, human, API, partner, physical. Where does the value moment happen?
- **Cost curve.** Fixed versus marginal, prepaid versus metered, centralized versus distributed. Who pays when volume grows?
- **Sequencing.** Valuable step first, or gate first? Which prerequisite can be deferred until after the first success?
- **Instrumentation.** Observe and verify afterward, or gate with approval beforehand. Which risk actually requires prevention?
- **Granularity.** One workflow, one job, one segment, or one integration. What is the smallest unit that proves the outcome?

Two alternatives that differ only in UI copy are one alternative. Aim for options that each remove a *different* inherited default.

## Constraint budget

Prefer the design that satisfies the fundamentals with the fewest unverified assumptions, not the fewest features. Compare:

- number of fundamental constraints satisfied, and at worst case;
- number of inherited constraints re-added, and why;
- operational and coordination burden;
- time and cost to first real evidence;
- reversibility if the core assumption is wrong.

A small comparison table is enough:

| Alternative | Fundamentals satisfied | Inherited defaults removed | New assumptions | Cheapest probe | Kill criterion |
| --- | --- | --- | --- | --- | --- |

## Stress the rebuild

- Does it satisfy every fundamental under realistic worst-case conditions, including resource ceilings?
- What coordination does it require? Who must act, and do they have an incentive to?
- Which assumption is it most sensitive to, and what is the cheapest way to test that one?
- What breaks first in operation, and is the failure reversible?
- Is it actually different from the incumbent, or the same design with new names?
- Does it depend on behavior that has not been observed at the required scale?
- Does it create a new single point of failure, or hide a cost in an unowned team?
- For regulated or safety-critical work, has compliance or security reviewed the change before any pilot?

## Common rebuild failures

- **Novelty without fundamentals.** Ignoring a real limit because it is inconvenient.
- **Solution transplant.** Copying a design from another context and calling it first-principles.
- **Hidden coordination cost.** "The team will just..." without an owner or incentive.
- **Incremental re-adds.** Adding constraints back until the original design reappears.
- **Metric substitution.** Optimizing an easy local metric instead of the stated outcome.
- **No probe.** A rebuild with no decision rule is a proposal, not a test.
- **Rebuilding what should be improved.** If the incumbent is basically sound, use an improvement or variation method instead.
