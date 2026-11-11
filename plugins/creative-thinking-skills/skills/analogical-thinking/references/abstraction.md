# Abstracting a Problem to Mechanism

The source domain can only match your problem if you compare structures. Most bad analogies fail here: the problem was never abstracted, so the first domain with a similar-looking situation wins.

## Surface vs structure

- **Surface features** are nouns, settings, and sensory details: nurses, tickets, terminals, students, warehouses.
- **Structure** is the relational pattern: A produces B, B waits on C, C is scarce, delay in C feeds back into A. These relations survive renaming.

Strip the nouns and see what remains. If nothing remains, you have a topic, not a problem.

## Four lenses

Describe the problem through each lens, one or two sentences each.

| Lens | Question | What it exposes |
|---|---|---|
| **Function** | What transformation does the system perform — input to output, state to state? | The invariant job, independent of the current implementation |
| **Flow** | What moves between whom or what — material, information, decisions, people, money? Where does it queue, branch, or leak? | Coordination structure, bottlenecks, handoffs |
| **Constraint** | What is fixed and why — capacity, time, budget, law, trust, attention, reversibility? | The boundary that any borrowed mechanism must respect |
| **Feedback** | What measures deviation, and what adjusts in response — and how fast? | Control structure, delay, oscillation, gaming risks |

## Procedure

1. **Write the concrete intake** first (3–5 sentences). Keep names and quantities; they are needed later for the mapping.
2. **Name the job.** "This system exists to ___ under ___ constraints."
3. **Draw the flow.** List the units and the edges between them. Mark queues, decision points, and return paths.
4. **Mark the binding constraint.** Identify which constraint, if relaxed, would change the design most. That constraint is the one a source mechanism must address.
5. **Mark the feedback loops.** For each, note sensor, delay, and actuator. Missing or delayed feedback is often the real problem.
6. **Restate structurally.** One to three sentences, no domain nouns. Include quantities and relations where they matter.

## Statement template

> A set of ___ [units] with ___ [differing properties] must be routed through ___ [process] under ___ [binding constraint]. Success is ___; failure is ___. Feedback about ___ arrives ___ [when], and actors respond by ___.

Example: "A set of requests with unknown and unequal urgency must be matched to a small set of specialized handlers under limited attention and incomplete information. Mismatches are expensive and partly irreversible; feedback about true urgency arrives only after work starts."

That statement can now match an emergency room, a support queue, or a field-service dispatch — which is the point.

## Tests

- **Noun-strip test:** remove every industry noun. Does the statement still constrain a design? If not, it was a label.
- **Relation test:** can you list at least three relations (causes, waits-on, feeds-back)? Fewer means the problem is under-analyzed.
- **Inversion test:** does the statement explain what failure looks like? Structure should predict failure, not just success.
- **Scale test:** replace "small" with "10× larger." Which relations survive? Those are the exportable ones.

## Anti-patterns

- Abstracting until everything matches ("it's a system with inputs and outputs") — too vague to transfer anything.
- Keeping a favorite solution in the statement ("we need better triage") — that is a conclusion, not a structure.
- Ignoring quantities — a mechanism that works at 10 items may fail at 10,000.
- Hiding the constraint — analogies then import mechanisms that depend on slack you do not have.
