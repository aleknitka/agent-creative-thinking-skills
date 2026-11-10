# Three Worlds, One Problem

The same problem is mutated three ways — once per assumption type — so you can compare what each axis buys you. All worlds, numbers, and traces are **invented illustrations**, not case evidence.

## Shared baseline

Subject: a 900-person software company whose internal knowledge base (KB) gets ~11% monthly active use. Most routine questions are answered by asking a colleague in chat. Roughly 60% of the 4,000 pages have not been updated in a year. New hires report ~6 weeks to find routine answers.

Inherited assumptions:

- **Resource:** expert writing time is scarce; documentation competes with delivery work.
- **Interface:** people must go to the KB and search; a page is the unit of knowledge.
- **Actor:** the primary user is an existing employee who knows what to search for.
- **Rule:** anyone may edit, but nobody must.
- **Scale:** company-wide, 4,000 pages, all departments.
- **Time:** pages are reviewed annually; answers are asynchronous.

---

## World A — Abundant resource

**Mutation:** What if expert time to write and maintain documentation were effectively unlimited?

**Held fixed:** same employees, same tools, same budget for tooling, same readers, same review rules.

**World sketch**

- **Premise:** Documentation can be produced and refreshed as fast as work happens.
- **Changes immediately:** every answered chat question can become a durable answer; stale pages can be rewritten instead of patched; duplicates can be merged on sight.
- **Stays the same:** experts still dislike writing; readers still must find the right page; edit permissions still open.
- **Must be true:** capture is cheap enough that writing does not compete with delivery work; someone still owns structure and conflict resolution.
- **Thrives / loses:** new hires and support staff gain; people whose status comes from being the only source of an answer lose leverage.
- **New frictions:** volume grows faster than quality control; contradictory answers coexist; nobody's incentive changes.
- **Artifact:** a KB that grows as a by-product of answering questions, with a curator role rather than an author role.

**Trace**

- **First order:** (+ ) more answers are captured; (+ ) pages refresh faster; (−) duplication and near-duplicates multiply.
- **Second order:** (+ ) support shifts from writing to curating; (−) readers face more results with less certainty; (−) experts spend the saved time on delivery, not more writing.
- **Third order:** (+ ) "the answer is written down" becomes normal; (−) authorship-based status erodes; (−) a new curation bottleneck replaces the writing bottleneck.
- **Loop:** reinforcing — more captured answers → better coverage → more questions asked in chat; balancing — more pages → lower trust → back to asking colleagues.

**Transferable insight:** The scarce resource was never writing — it was *capture and curation*. Make answering a question produce a durable artifact automatically, and move expert effort from authoring to arbitration. This works without unlimited time.

**Probe:** instrument one support channel for two weeks; auto-draft KB entries from resolved threads; measure how many drafts survive curation and how many are reused.

---

## World B — No interface

**Mutation:** What if there were no knowledge-base interface at all — no search box, no pages, no site to visit?

**Held fixed:** same content, same readers, same edit rights, same accuracy expectations.

**World sketch**

- **Premise:** Knowledge arrives inside the tools where work already happens — chat, editor, ticket, meeting notes — and has no separate home.
- **Changes immediately:** retrieval becomes push or inline; browsing and coverage judgment disappear; knowledge is composed per request rather than per page.
- **Stays the same:** somebody must still decide what is true; stale or conflicting source material still exists.
- **Must be true:** a retrieval layer can reach the underlying material; answers carry provenance; silence is distinguishable from "no answer."
- **Thrives / loses:** frontline staff gain; content teams lose a shared surface for spotting gaps; tool vendors gain a strategic position.
- **New frictions:** answer quality is invisible until it is wrong; users cannot audit coverage; errors propagate silently.
- **Artifact:** an answer layer embedded in the workflow, with citations, and a separate curation console only maintainers see.

**Trace**

- **First order:** (+ ) less search effort; (+ ) answers appear at the moment of need; (−) users cannot browse or discover adjacent knowledge.
- **Second order:** (+ ) content is written for retrieval, not for page structure; (−) gaps become harder to see; (+/−) the assistant's owner becomes the real gatekeeper of organizational memory.
- **Third order:** (+ ) knowledge quality is measured by answer accuracy; (−) whoever controls the assistant controls what the organization knows; (−) "look it up" disappears as a shared skill.
- **Loop:** reinforcing — more in-flow questions → more captured answers → better retrieval; balancing — more automated answers → more silent errors → lower trust.

**Transferable insight:** If the interface disappears, *measure knowledge by correctness at the point of need, not by page views*. Add retrieval inside chat now, with citations, and instrument wrong-answer reports even before the content is complete.

**Probe:** ship an in-chat assistant over the top 200 pages with mandatory citations; track deflection, citation clicks, and wrong-answer reports for 30 days.

---

## World C — Different actor

**Mutation:** What if the primary KB user were a new hire on day one, who does not yet know the company's vocabulary?

**Held fixed:** same company, same content, same tools, same colleagues available to ask.

**World sketch**

- **Premise:** The design target cannot form a good query because they do not know what exists or what it is called.
- **Changes immediately:** search terms are vague or wrong; pages assume acronyms and context; orientation material becomes more valuable than reference material.
- **Stays the same:** experienced staff still want fast lookup; the underlying facts are unchanged.
- **Must be true:** role-based entry paths exist; internal vocabulary can be mapped to plain-language questions; content is labeled by task, not department.
- **Thrives / loses:** new hires and their managers gain; long-tenured gatekeepers lose; experienced users may find orientation content noisy.
- **New frictions:** two content genres (orientation vs reference) compete for the same pages; onboarding paths can become outdated propaganda.
- **Artifact:** role-based "start here" paths that lead into task pages, plus query expansion from plain language to internal terms.

**Trace**

- **First order:** (+ ) day-one questions get answered; (−) search success drops for existing users as orientation content floods results.
- **Second order:** (+ ) content is reorganized around tasks and roles; (−) department owners resist reframing their pages; (+ ) new hires ask better questions after week one.
- **Third order:** (+ ) documentation becomes onboarding infrastructure, not an archive; (−) whoever owns the onboarding path shapes what new people believe; (−) deep reference material gets less attention.
- **Loop:** reinforcing — better day-one answers → new hires contribute corrections sooner → content improves; balancing — more orientation content → more duplication → curation load rises.

**Transferable insight:** Design for the person who does not know the words, not the person who knows what to search for. Role-based entry paths and plain-language query mapping help everyone, not just new hires.

**Probe:** build three role-based entry paths for the next onboarding cohort; measure time-to-first-correct-answer against the previous cohort.

---

## What good looks like

- Each world mutates exactly one assumption and names what stayed fixed.
- The world is concrete enough to have an artifact and at least two new frictions.
- Traces include both gains and harms, and at least one feedback loop.
- Every world yields one insight that survives without the impossible premise, plus a probe.
- The three worlds are genuinely different: resource, interface, and actor each change the design logic, not just the wording.
- Worlds are labeled as fiction; no world is presented as a forecast or as evidence.
