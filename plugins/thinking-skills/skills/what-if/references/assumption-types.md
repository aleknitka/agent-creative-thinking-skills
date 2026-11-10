# Assumption Types — The Six Mutation Axes

Most strategies rest on six kinds of assumptions. Naming the type helps you find the assumption that actually carries the design, and keeps you from generating five variations of the same mutation.

Use this page during **step 2**. Read the type descriptions, list 2–3 candidate assumptions per type, then pick the one with the highest downstream reach.

## Selection test

A good mutation candidate is:

1. **Load-bearing** — remove it and many other decisions change.
2. **Contestable** — it could plausibly be otherwise, even if not today.
3. **Productive** — the resulting world suggests mechanisms you can transfer back.
4. **Single** — you can state it as one "What if X were Y?" without smuggling in a second change.

Prefer the assumption everyone treats as background. If a mutation feels comfortable, it is probably not touching the real constraint.

## Quick reference

| Type | The assumption sounds like | Mutation pattern | Usually unlocks |
|---|---|---|---|
| **Resource** | "We cannot afford / staff / store enough X." | abundance, zero, substitution | business-model and capacity ideas |
| **Interface** | "Users come to our app / form / counter." | removal, ambient, new channel | workflow and experience ideas |
| **Actor** | "The user is the analyst / adult / customer." | different actor, non-human, outsider | user-model and access ideas |
| **Rule** | "We must collect / approve / report X." | repeal, inversion, new rule | policy, governance, incentive ideas |
| **Scale** | "This works for N users / one region." | 1000×, 1/1000×, granularity | operating-model ideas |
| **Time** | "This takes weeks / happens monthly / in this order." | instant, decades, reversed, continuous | latency, cadence, sequencing ideas |

## Resource

Covers money, people, expertise, attention, compute, energy, materials, data, space, and trust. Resource assumptions are usually stated as scarcity: "we can't hire," "experts are expensive," "attention is limited."

**Triggers**
- What if the binding resource were effectively unlimited?
- What if it were free but everything else stayed scarce?
- What if a different resource became the constraint?
- What if the resource were renewable, shared, or self-producing?

**Example mutations**
- "What if expert time to write documentation were unlimited?"
- "What if storage and compute cost nothing?"
- "What if every customer had unlimited attention for onboarding?"

**Watch for:** abundance rarely removes coordination problems. The interesting world is not "the same process, but bigger" — it is "what becomes worth doing once the constraint disappears?"

## Interface

Covers how actors reach the system: apps, forms, search boxes, APIs, meetings, counters, phone trees, physical touchpoints, and the handoffs between them. Interface assumptions hide in phrases like "the user opens the dashboard" or "the customer submits a request."

**Triggers**
- What if there were no interface at all?
- What if the interface were everywhere, or ambient?
- What if the interface were another actor's existing workflow?
- What if the system initiated the interaction instead of waiting?

**Example mutations**
- "What if there were no knowledge-base UI — no search box, no pages?"
- "What if booking required no form, because the system already knew?"
- "What if the product surfaced inside the customer's own tools?"

**Watch for:** "no interface" usually means the interaction moves somewhere else, not that it vanishes. Name where it goes.

## Actor

Covers who is involved: the primary user, buyer, operator, administrator, regulator, bystander, contractor, future employee, or a non-human agent. Actor assumptions are often encoded in pronouns: "the user" is treated as a single, motivated, trained adult.

**Triggers**
- What if the primary user were someone else entirely?
- What if the user had no context, no training, or no English?
- What if the operator, not the end user, were the customer?
- What if a machine agent were the primary reader or actor?
- What if the person most affected had decision power?

**Example mutations**
- "What if the primary knowledge-base user were a day-one hire who cannot ask a colleague?"
- "What if the buyer were the compliance officer, not the team lead?"
- "What if an AI agent maintained the documentation instead of a human?"

**Watch for:** switching actors is not the same as adding a persona. The world changes only when the new actor's constraints force a different design.

## Rule

Covers formal and informal rules: laws, policies, contracts, approvals, permissions, definitions, incentives, norms, and success criteria. Rule assumptions sound like "we have to," "it must be audited," or "the metric is revenue."

**Triggers**
- What if this rule did not exist?
- What if it were inverted — the opposite were required?
- What if the rule applied to a different actor?
- What if success were measured by a different variable?
- What if permission were default-granted rather than default-denied?

**Example mutations**
- "What if nobody had to approve documentation changes?"
- "What if the success metric were time-to-first-correct-answer, not page views?"
- "What if external contractors could read everything internal staff can?"

**Watch for:** removing a rule often exposes the fear that created it. Trace that fear; it is usually the transferable insight.

## Scale

Covers number of users, transaction volume, organizational size, geographic spread, granularity, and unit of analysis. Scale assumptions are often implicit: "a team," "a region," "one ticket," "per customer."

**Triggers**
- What if there were 1000× more / fewer users?
- What if the unit were one person, one interaction, or one planet?
- What if it had to work in one day with the same scope?
- What if it had to work across every region at once?
- What if we zoomed in until the average disappeared?

**Example mutations**
- "What if the knowledge base had one user per document?"
- "What if the company had 100× the employees but the same number of experts?"
- "What if onboarding were designed for one new hire at a time?"

**Watch for:** scaling up rewards automation and self-service; scaling down rewards craft and context. Both directions can transfer.

## Time

Covers latency, frequency, cadence, duration, lifetime, deadlines, and sequence. Time assumptions hide in "within two weeks," "quarterly," "before launch," and "step 1, then step 2."

**Triggers**
- What if it happened instantly?
- What if it took a decade — or arrived once a year?
- What if the sequence were reversed, or all steps happened at once?
- What if it were continuous rather than episodic?
- What if the deadline were removed, or moved much earlier?

**Example mutations**
- "What if documentation updated itself the moment a question was answered?"
- "What if the annual review happened daily?"
- "What if onboarding began before the hire accepted the offer?"

**Watch for:** speed changes which failure modes matter. Instant worlds expose trust and verification problems; slow worlds expose commitment and memory problems.

## After choosing

Record the chosen assumption, its type, and the mutation in one sentence. Then move to [branching.md](branching.md). Keep the rejected candidates: they are useful for a later pass, and they show the user what was considered.
