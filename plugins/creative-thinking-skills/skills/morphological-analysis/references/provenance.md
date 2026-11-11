# Provenance — Zwicky, Morphology, and Evidence

## Named method

- **Fritz Zwicky (1898–1974)** — Swiss-American astrophysicist at Caltech, known for the discovery of dark matter (1933) and for supernova research. During the 1940s he developed a general approach he called **morphological analysis**, applying it to jet and rocket propulsion while consulting for Aerojet and later to astronomy, where it is still described as **morphological astronomy**.
- Zwicky's core device is the **morphological box** (also *Zwicky box*, *morphological matrix*): parameters as columns, alternatives as rows, candidate solutions as one alternative from each column. He described the method in *Morphology of Propulsive Power* (1962, Society for Morphological Research) and in *Entdecken, Erfinden, Forschen im morphologischen Weltbild* (1966). His earlier article "Morphological Astronomy" (1948) applies the same reasoning to cosmological problems; the book of that title followed in 1957.
- **Tom Ritchey** and the **Swedish Morphological Society** extended the approach in the 1990s into **General Morphological Analysis (GMA)** — a non-quantified modelling method for policy, defense, and other "wicked" problems, with an emphasis on cross-consistency assessment and computer-supported workshops. Ritchey's papers (e.g. "General Morphological Analysis: A general method for non-quantified modelling", 1998/2002) are the main modern methodological reference.

The terms *morphological analysis*, *morphological box*, and *Zwicky box* are Zwicky's; the compatibility-matrix procedure and the workshop format are central to Ritchey's GMA.

## Lineage and related work

- The underlying idea — decompose a problem into independent parameters, enumerate alternatives, then recombine — appears independently in engineering design (Pahl and Beitz's *Engineering Design* treats morphological charts as a standard method), in **TRIZ** (morphological analysis is one of its combination tools), and in design research as the **morphological chart**.
- **Design of experiments** and **covering arrays** solve a related but different problem: they choose combinations to *test* statistically. Morphology chooses combinations to *reason about* before any test exists.
- **Scenario planning** shares the "matrix of drivers" structure but externalizes the dimensions (uncertain futures) rather than internalizing them (design choices).

## Adaptations in this skill

- The six-step flow (intake → decompose → populate → prune → score/sample → harvest with probes), the dimension tests (swap/tradeoff/cause), the reason-code vocabulary, the coverage-first sampling procedure, and the onboarding worked example are **practical workflow adaptations** for this repository. They preserve Zwicky's box and Ritchey's cross-consistency assessment but are not their wording.
- The 100/500-combination thresholds, the 3–6 dimension band, and the 20%/90% pruning heuristics are rules of thumb from facilitation practice, not findings from controlled studies. Treat them as defaults to calibrate, not laws.
- The `scripts/morph.py` helper is original: it parses a dimension specification, enumerates the cross-product, applies pairwise exclusions, and samples for option coverage. It reproduces no proprietary material.

## Evidence and limits

- There is **no controlled experimental evidence** that morphological analysis outperforms other ideation methods. Its support is methodological argument (coverage, explicit independence, auditable pruning) and decades of application in engineering, defense, and policy analysis.
- The method's central assumption — that dimensions can be treated as independent — is often false in social and organizational settings. Ritchey's GMA addresses this with explicit cross-consistency assessment; this skill's pruning step is a lighter version of the same move. Where independence cannot be defended, the box's output is a hypothesis map, not a model of the system.
- **Combinatorial explosion** is the standard failure: the method produces more candidates than anyone can evaluate, and the pruning/sampling discipline is what keeps it useful. A box without pruning is enumeration theatre.
- **Post-hoc rationalization** is the second failure: a box can be populated so that the preferred combination wins. The reason-code and baseline requirements exist to make that visible.
- Treat every combination as a hypothesis. The skill's output is a shortlist with probes, not a validated design.

## Permissions note

Zwicky's and Ritchey's published descriptions are cited here as facts about the method; no long excerpts are reproduced. The compatibility-matrix worksheet, sampling algorithm, and example are original to this repository.
