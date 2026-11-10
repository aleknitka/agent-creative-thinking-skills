# Constraints, Facts, and Preferences

The central move of first-principles thinking is classification, not assertion. Most failures come from treating an inherited choice as a law, or a real limit as an opinion. This reference gives the categories, the capture table, and the tests that keep the labels honest.

## Four families of fundamental constraint

A fundamental constraint is a limit that any acceptable solution must respect, independent of the current design.

| Family | What it means | Typical cues | How to verify | Accountable owner |
| --- | --- | --- | --- | --- |
| **Physical** | Limits set by matter, energy, geometry, human perception, or current engineering envelopes | speed, heat, weight, latency floor, precision, material strength, manufacturing tolerance, bandwidth, battery density | Measurement, engineering calculation, supplier spec, independent test. Ask for the achieved number and its conditions, not a rule of thumb | Engineer or domain specialist |
| **Regulatory** | Law, sector rules, signed contracts, platform terms, or license conditions that carry penalties | "required by law", GDPR, HIPAA, SOX, PCI, export control, data residency, statutory filing, contract clause, SLA with remedies | Read the exact text and scope with counsel or the compliance owner. Determine whether the obligation is external or merely stated policy | Legal, compliance, or contract owner |
| **Resource** | A real ceiling or tradeoff: money, people, time, compute, supply, attention | budget, headcount, deadline, quota, capacity, inventory, dollar or hour limits, "at most", "no more than" | Verify the number, the period, and who controls it. Distinguish "cannot be infinite" from "this specific number is fixed" | Budget or resource owner |
| **Invariant** | Something that must remain true for any acceptable solution: identity, safety, security boundary, data integrity, accounting balance | must never lose, must remain, always, never, atomic, idempotent, reconcilable, non-negative, unique, auditable, uptime floor | Identify the failure mode and what it would cost. Separate a true invariant from a chosen guarantee or an SLA | Risk, security, or operations owner |

When a constraint sits on a boundary, record both readings and the test that would settle it. A platform rate limit may be a hard external constraint today and a negotiable commercial term tomorrow; label it "regulatory/contractual — verify renewal terms", not "physics".

## Inherited assumptions and preferences

These are real forces, but they are not fundamentals.

**Inherited** items are existing choices that no one has re-justified: conventions, legacy architecture, copied competitor flows, internal policy, team habits, tool defaults, and "best practice". They usually have an owner and a date, even if nobody remembers either. Ask: who chose this, what problem did it solve then, and would we choose it again under today's facts? An internal approval process is inherited even when it is written down; an external regulation is not.

**Preferences** are tastes and wishes: brand feel, comfort, aesthetics, stakeholder enthusiasm, "it would be nice if". They can legitimately shape a solution, but they should be traded explicitly, not smuggled in as requirements.

## Capture table

One row per assertion. No compound "and" claims; split first.

| ID | Assertion (checkable) | Kind (fact / fundamental / inherited / preference) | Family | Evidence and source | Strength (observed / documented / asserted / speculative) | Owner | If false or removed, what changes? | Status (keep / test / drop) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |

Rules for filling it:

- Phrase as an assertion someone could disagree with: "enterprise buyers require SSO before purchase", not "enterprise".
- Cite an artifact, measurement, contract, or named person. "The team believes" is a source but it is not evidence.
- Strength is about the evidence, not the confidence of the speaker. A confident assertion is still "asserted".
- Status changes only after evidence, a test, or an explicit decision by the owner.
- Keep the fact rows separate from the constraint rows. Observed behavior is evidence about the current design; it is not automatically a permanent law.

## Classification tests

Run all five on anything load-bearing:

1. **Counterfactual.** Would this be true in a world where the current system was never built? If no, it is inherited or a consequence of the design.
2. **Change test.** Who could waive or change it, and what would that cost? A limit nobody can waive is closer to fundamental; a limit a manager can waive is usually inherited.
3. **Scope test.** Does the rule actually cover this case, or is that an interpretation? Regulations and contracts are narrower than their folklore.
4. **Refutation test.** What observation would show this is false? If nothing could, it is a belief or a definition, not an empirical constraint.
5. **Cost test.** What do we pay to preserve it — money, time, risk, opportunity? A high cost with no evidence is a signal that a preference has been dressed as a constraint.

## Boundary cases

- **Internal policy vs external regulation.** Internal policy is inherited until an external obligation requires it. Even then, the obligation's scope is the fundamental, not the local procedure.
- **Budget.** "We cannot spend infinitely" is a resource fundamental. "The number is 50k" is a level choice with an owner. Keep both, but do not let the number hide behind the principle.
- **Observed user behavior.** "Users abandon at step 3" is a fact about the current flow. "Users will not tolerate more than three steps" is a hypothesis. The first constrains the diagnosis; the second needs a test.
- **Platform limits.** Rate limits and API terms can be contractual, technical, or default settings. Check which, and when it changes.
- **Safety and security invariants.** Never remove them for the sake of a cleaner rebuild. Redesign within them, and verify the threat model rather than assuming the current control is the only implementation.
- **"Users won't pay."** Usually a hypothesis about a price, segment, and packaging, not a fundamental. It may still be the most important thing to test.
- **Legal questions.** Interpret with counsel. This skill classifies claims; it does not provide legal advice.

## Common mislabels

| Statement | Likely classification | Why |
| --- | --- | --- |
| "Everyone does it this way" | Inherited | Popularity is not necessity |
| "We tried that once and it failed" | Evidence about one attempt | The attempt's conditions matter more than the verdict |
| "It's impossible" | Unclassified | Force the question: which law, limit, or invariant makes it impossible? |
| "We can't afford it" | Resource | The level may be negotiable; separate the ceiling from the number |
| "It's policy" | Inherited, unless externally mandated | Find the policy owner and the obligation behind it |
| "Users need X" | Hypothesis, unless observed | Stated needs are often preferences or solutions |
| "Security requires X" | Invariant, verify scope | Check the threat model and whether X is the only control |
| "The contract requires it" | Regulatory/contractual | Read the clause and its remedies before treating it as absolute |
