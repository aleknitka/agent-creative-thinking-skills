# Provenance — Attribution, Lineage, and Evidence Limits

## Nominal Group Technique

- **André L. Delbecq and Andrew H. Van de Ven** formalised the Nominal Group
  Technique in the late 1960s and published the group-process model in 1971:
  "A Group Process Model for Problem Identification and Program Planning,"
  *Journal of Applied Behavioral Science*, 7(4), 466–492.
- Their companion study, Van de Ven & Delbecq, "Nominal versus Interacting
  Group Processes for Committee Decision-Making Effectiveness," *Academy of
  Management Journal*, 14(2), 203–212 (1971), compared nominal groups with
  conventional interacting groups. It is the usual citation for the claim that
  the nominal structure reduces production blocking, evaluation apprehension,
  and domination by high-status speakers.
- The practical manual is Delbecq, Van de Ven & Gustafson, *Group Techniques
  for Program Planning: A Guide to Nominal Group and Delphi Processes*
  (Scott, Foresman, 1975). It covers question framing, facilitation, and the
  Delphi process alongside NGT.
- The canonical NGT sequence is: silent written generation → round-robin
  recording → serial clarification → independent voting → discussion →
  final vote. The exact number of ballots and the scoring rule vary by
  practitioner. The 5-4-3-2-1 weighting used here is a common adaptation of
  rank ordering, not a rule handed down by the originators.

## Delphi

- The Delphi method was developed at the **RAND Corporation** in the 1950s and
  1960s for structuring expert judgment where direct confrontation is
  impractical or undesirable. The standard early citation is Dalkey & Helmer,
  "An Experimental Application of the Delphi Method to the Use of Experts,"
  *Management Science*, 9(3), 458–467 (1963).
- Helmer's 1966 report, *The Delphi Method for Systematizing Judgments about
  the Future* (Institute of Government and Public Affairs, University of
  California), is an early programmatic statement.
- The four properties usually attributed to Delphi are **anonymity,
  iteration, controlled feedback, and a statistical group response**. The
  method was designed for forecasting; using it to prioritize a frozen option
  set is an adaptation, and the median/IQR summaries are standard statistical
  descriptions rather than a required feature of the original procedure.

## What is original in this skill

The following are workflow adaptations for this repository, not claims about
the founders' text:

- The six-step combined pipeline (intake, silent generation, round-robin,
  clarify/cluster, vote/rank, dissent/handoff).
- The choice architecture between synchronous NGT and asynchronous Delphi,
  including the round-by-round feedback schedule.
- The specific timeboxes, panel-size guidance, stopping thresholds, tie-break
  rules, dissent-log fields, and report format.
- The 5-4-3-2-1 and N/3 aggregation descriptions, and their implementation in
  `scripts/ngt.py`.
- The worked examples, triage tables, and facilitation scripts.
- The claim that a ranking is an input to a decision owner rather than the
  decision itself.

Attribute NGT to Delbecq and Van de Ven, Delphi to Dalkey, Helmer, and RAND,
and treat the elaborations above as adaptations.

## Evidence and limits

- **The nominal-group advantage is real but bounded.** Early experiments and
  field studies found that nominal groups often produce more ideas and fewer
  dominance effects than interacting groups. Reviews of group brainstorming
  identify production blocking and evaluation apprehension as robust causes of
  process loss. The effect on *decision quality* is less consistent than the
  effect on idea count; structure can also suppress the exchange of tacit
  knowledge that a good discussion would surface.
- **NGT is not immune to facilitation effects.** A facilitator who advocates,
  a visible early tally, or a senior participant who speaks first can erase the
  method's advantage. The protocol is the intervention; the label alone is not.
- **Delphi consensus is not accuracy.** A panel can converge on a wrong answer,
  especially with a homogeneous panel, a leading question, or feedback that
  omits dissent. Reviews and critiques (for example Sackman's 1974 RAND
  assessment, Woudenberg's 1991 evaluation, Rowe & Wright's 1999 analysis, and
  Landeta's 2006 review) document sensitivity to panel selection, question
  framing, response rates, and the handling of feedback. Report dispersion and
  attrition; do not present a median as a prediction.
- **Anonymity is procedural, not absolute.** Small panels and distinctive
  comments can deanonymise respondents. Say what anonymity the process can
  actually protect, and strip identifying detail from quoted reasons.
- **The specific thresholds here are conventions.** "70% within ±1 of the
  median", "IQR ≤ 1", and "three rounds" are practical defaults, not
  validated constants. Fix them before Round 1 and report what was used.
- **The examples are invented.** The activation and reliability numbers in the
  worked examples illustrate the record format; they are not study results.
- **No claim of superiority over a well-run criteria matrix.** For many
  organisational decisions, a transparent scoring rubric with agreed weights
  is cheaper and at least as defensible. NGT and Delphi earn their cost when
  equal voice, anonymity, or a traceable group judgment matters.

## Permissions note

No third-party text is reproduced beyond short attributed facts. The method is
summarised and cited; the helper script generates synthetic ballots and applies
documented arithmetic. It bundles no proprietary worksheet, checklist, or
software.
