#!/usr/bin/env python3
"""inventory.py - offline helper for the challenge-assumptions skill.

Turns a problem statement plus optional beliefs into an assumption inventory
with falsification, necessity, and reversal prompts. No dependencies, no
network, no fabricated evidence: every row starts unverified.

Usage:
  python scripts/inventory.py --problem "New users must complete a tutorial before they can use the product"
  python scripts/inventory.py --problem "..." --assumption "Onboarding must be a tutorial" \
      --assumption "Support is chat-only" --format csv
  python scripts/inventory.py --problem "..." --assumptions "Users want fewer clicks; The CMS cannot publish without an editor"
  python scripts/inventory.py --test --assumption "Onboarding must be a tutorial" --seed 7
  python scripts/inventory.py --list
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import random
import re
import sys
from dataclasses import asdict, dataclass

# Coarse families are the teaching lenses; subtypes are what the helper prints.
FAMILIES = ("origin", "source", "boundary", "continuity", "unclassified")

FAMILY_HELP = {
    "origin": "Inherited convention versus proven constraint. Ask who decided, when, and on what evidence.",
    "source": "Attributed to a stakeholder or to a system/policy/tool. Separate preference from invariant.",
    "boundary": "Where the box was drawn: scope, users, channels, budget, deadline, geography.",
    "continuity": "Assumed order, sequence, or persistence: 'must first', 'always', 'this step'.",
    "unclassified": "No reliable cue. Restate as a prediction and test it directly.",
}

SUBTYPE_HELP = {
    "origin/inherited": "Inherited convention: nobody in the room chose it, and no evidence is on file.",
    "origin/proven": "Proven constraint: a test, incident, contract, or physical limit stands behind it.",
    "source/stakeholder": "A belief attributed to people: users, customers, managers, regulators, support.",
    "source/system": "A belief attributed to a mechanism: tool, policy, contract, architecture, economics.",
    "boundary": "A scope or boundary belief: who/what is inside the problem, and at what cost or deadline.",
    "continuity": "An order or persistence belief: the sequence, a step, or 'this must stay'.",
    "unclassified": "No reliable cue. Restate as a prediction and test it directly.",
}

PROMPTS = {
    "origin": {
        "falsify": [
            "Find the decision record, test, or incident that established this. If none exists, what observation would show it is obsolete?",
            "Who first asserted this, and would they still defend it on today's evidence? What would contradict it?",
            "Compare with one team or competitor that does the opposite. What do they observe that we do not?",
        ],
        "unnecessary": [
            "Name the concrete harm this prevents today. If the harm is hypothetical, what would removing it break in one low-risk case?",
            "If this had never existed, would anyone recreate it now? What would they put in its place?",
            "What is the cheapest bounded exception, and who would have to approve it?",
        ],
        "reverse": [
            "Assume a newcomer chose the opposite convention. What would they do instead, and what would have to be true for it to work?",
            "If this were replaced tomorrow, what would the replacement have to preserve?",
            "What does the opposite make possible that the current belief forbids?",
        ],
        "evidence": "Decision record, incident history, test result, or a team that works differently.",
        "probe": "Search the decision record and incident log (desk check); if none, compare with one team using the opposite convention.",
    },
    "stakeholder": {
        "falsify": [
            "Ask the named stakeholder directly, or inspect their behavior. What would they do that contradicts this attribution?",
            "Find the primary statement (quote, ticket, survey) rather than the retelling. Does it say what we think it says?",
            "Whose preference is this attributed to, and have they been asked recently? What would they say if the cost were theirs?",
        ],
        "unnecessary": [
            "Is this a preference or a hard constraint? What happens if the preference is legitimately overridden?",
            "If the stakeholder never mentioned this, would the plan still need it?",
            "Could the stakeholder's underlying interest be met another way, without treating this as fixed?",
        ],
        "reverse": [
            "Assume the stakeholder wants the opposite. What would explain that, and what would change?",
            "Assume they do not care. What would you do differently, and who would object?",
            "Put the cost of this belief on the stakeholder. Would they still hold it?",
        ],
        "evidence": "Direct quote, observed behavior, or survey - separate stated from revealed preference.",
        "probe": "One conversation with the named stakeholder plus one behavioral trace (half day).",
    },
    "system": {
        "falsify": [
            "Read the actual policy, contract, or configuration. Is this an invariant, a default, or someone's local setup?",
            "Ask the accountable owner to point to the clause, setting, or test that requires this.",
            "Try the opposite in a sandbox or non-production copy. What actually blocks it?",
        ],
        "unnecessary": [
            "Which part of the mechanism requires this? Could a different tier, config, or path meet the goal?",
            "Is this a guardrail someone chose or a hard limit? Who could change the guardrail?",
            "What would the process look like if this mechanism were unavailable for a day?",
        ],
        "reverse": [
            "If the system allowed the opposite, what would break - and is that a real invariant or a chosen guardrail?",
            "Assume the constraint applies only to one segment. Which segment, and why?",
            "Move enforcement to another layer (vendor, contract, review). Does the constraint survive?",
        ],
        "evidence": "Primary document, schema, config, sandbox test, or accountable owner.",
        "probe": "Read the primary policy/schema/config and ask the accountable owner to cite the clause (desk check).",
    },
    "boundary": {
        "falsify": [
            "Who set this boundary, and what evidence supports it? Is it a real limit or a chosen scope?",
            "Is the boundary stated anywhere, or does it exist because the problem's nouns imply it?",
            "What would have to change outside the boundary for it to move - and is that change actually blocked?",
        ],
        "unnecessary": [
            "What goal is the boundary serving? Would a narrower or wider boundary serve it better?",
            "Which parts of the boundary are load-bearing and which are convenience?",
            "What is the smallest version of the problem outside the boundary that still matters?",
        ],
        "reverse": [
            "Assume the boundary is gone. What is the first thing you would try, and what real constraint would you hit?",
            "Assume the boundary is twice as tight. Does the problem get clearer or just smaller?",
            "Move the boundary one level up: what is the goal that makes the current problem optional?",
        ],
        "evidence": "Named owner, external commitment, contract or regulation, measured limit, or an admission that it is convenience.",
        "probe": "Interview the boundary owner: state the goal and ask what would justify changing it (one conversation).",
    },
    "continuity": {
        "falsify": [
            "Does the order or step have a test or incident behind it? What happens if it runs in parallel, backwards, or not at all?",
            "Has this step or order ever been skipped under pressure or in a workaround? What happened to the outcome?",
            "Which step exists only because the previous step exists?",
        ],
        "unnecessary": [
            "Remove the step in thought (or in a dry run). Which guarantee actually disappears?",
            "Can the same outcome be reached with the step optional, deferred, or merged into another?",
            "What would an operator do if the step were unavailable for a day?",
        ],
        "reverse": [
            "Reverse who acts first or the sequence. What guarantee from the old order must be preserved?",
            "Let the last step happen first. What becomes possible or impossible?",
            "Run the steps in parallel. Which dependency is real and which is habit?",
        ],
        "evidence": "Workflow trace, dry run, exception handling by an operator, or a step that has been skipped before.",
        "probe": "Trace one real case through the workflow, then simulate removing or reordering the step in a dry run (half day).",
    },
    "unclassified": {
        "falsify": [
            "Restate the belief as a prediction: if it is true, what should we observe? Find the cheapest existing data that could contradict it.",
            "What would a skeptic point to as counter-evidence, and can you check that now?",
            "What is the strongest version of this belief, and what evidence would settle it?",
        ],
        "unnecessary": [
            "What goal does this belief serve? If it disappeared, which goal is actually harmed?",
            "Could a smaller or conditional version satisfy the same goal?",
            "Is this belief doing any work in the decision, or is it background?",
        ],
        "reverse": [
            "Assume the belief is false. What would become possible, and what mechanism would make that work?",
            "State the functional opposite, not just the negation. What would have to be true?",
            "Who would benefit if the belief were false, and what would they try first?",
        ],
        "evidence": "Any primary source that bears on the prediction: data, document, observation, or accountable person.",
        "probe": "Rewrite the belief as a prediction and look for an existing dataset or document that could contradict it (desk check).",
    },
}

# Checked in order; first hit wins. Labels are suggestions for the inventory,
# not verdicts about the belief.
SUBTYPE_CUES = (
    ("source/system", re.compile(
        r"\b(polic(?:y|ies)|platform|system|tool|vendor|api|architecture|database|schema|"
        r"integration|contract|regulat\w*|compliance|budget|headcount)\b", re.I)),
    ("boundary", re.compile(
        r"\b(only|within|inside|outside|scope|deadline|quarter|market|region|channel|"
        r"cannot|can't|no more than|limited to|budget|headcount|geograph\w*)\b", re.I)),
    ("origin/proven", re.compile(
        r"\b(measured|tested|observed|logged|verified|evidence|rate[- ]?limit|contractual)\b", re.I)),
    ("origin/inherited", re.compile(
        r"\b(best practice|tradition|standard|usually|industry|everyone|we've|we have|"
        r"convention|norm|habit|always)\b", re.I)),
    ("continuity", re.compile(
        r"\b(before|after|first|then|next|order|sequence|steps?|workflow|process|must|"
        r"has to|have to|needs? to|requires?|never|every)\b", re.I)),
    ("source/stakeholder", re.compile(
        r"\b(users?|customers?|clients?|people|stakeholders?|managers?|leadership|"
        r"executives?|team|support|sales)\b", re.I)),
)

MODAL_CUE = re.compile(
    r"\b(must|has to|have to|needs? to|requires?|cannot|can't|only|before|after|always|never|every)\b",
    re.I,
)


@dataclass
class Belief:
    id: str
    assumption: str
    type: str
    status: str
    falsify: str
    unnecessary: str
    reverse: str
    evidence: str
    probe: str


def classify(text: str) -> str:
    for subtype, pattern in SUBTYPE_CUES:
        if pattern.search(text):
            return subtype
    return "unclassified"


def pack_for(subtype: str) -> str:
    if subtype == "source/stakeholder":
        return "stakeholder"
    if subtype == "source/system":
        return "system"
    return subtype.split("/")[0]


def normalize(text: str) -> str:
    text = text.strip()
    return text if text.endswith((".", "?", "!")) else text + "."


def split_assumptions(raw: str | None) -> list[str]:
    if not raw:
        return []
    parts = re.split(r"[;\n]+", raw)
    return [normalize(p) for p in parts if p.strip()]


def extract_candidates(problem: str, limit: int = 5) -> list[str]:
    """Pull modal/ordering clauses out of the problem statement, if present."""
    text = re.sub(r"\s+", " ", problem).strip()
    sentences = re.split(r"(?<=[.!?])\s+", text)
    picked = [s for s in sentences if MODAL_CUE.search(s)]
    if not picked:
        picked = [text] if text else []
    return picked[:limit]


def build(assumptions: list[str], seed: int) -> list[Belief]:
    rng = random.Random(seed)
    rows: list[Belief] = []
    for i, text in enumerate(assumptions, 1):
        subtype = classify(text)
        pack = PROMPTS[pack_for(subtype)]
        rows.append(
            Belief(
                id=f"A{i}",
                assumption=text,
                type=subtype,
                status="unverified",
                falsify=rng.choice(pack["falsify"]),
                unnecessary=rng.choice(pack["unnecessary"]),
                reverse=rng.choice(pack["reverse"]),
                evidence=pack["evidence"],
                probe=pack["probe"],
            )
        )
    return rows


def esc(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", " ")


def render_markdown(problem: str, rows: list[Belief], notes: list[str]) -> str:
    out = ["# Assumption inventory", ""]
    if problem:
        out += ["**Problem statement:** " + problem.strip(), ""]
    out += [
        "All beliefs start **unverified**. Type labels are suggestions, not verdicts.",
        "",
    ]
    if notes:
        out += [f"- {n}" for n in notes] + [""]
    out += [
        "| ID | Belief (assertion) | Type (suggested) | Falsify | Unnecessary | Reversed | Evidence needed | Cheapest probe |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for r in rows:
        out.append(
            "| {id} | {a} | {t} | {f} | {u} | {v} | {e} | {p} |".format(
                id=r.id,
                a=esc(r.assumption),
                t=r.type,
                f=esc(r.falsify),
                u=esc(r.unnecessary),
                v=esc(r.reverse),
                e=esc(r.evidence),
                p=esc(r.probe),
            )
        )
    out += [
        "",
        "Rank by **impact x uncertainty** before testing; test the top handful, not all rows.",
        "Write a decision rule before each probe runs.",
        "",
        "Coverage prompts if the table feels thin:",
    ]
    out += [f"- **{family}:** {FAMILY_HELP[family]}" for family in FAMILIES if family != "unclassified"]
    out += [""]
    return "\n".join(out)


def render_csv(rows: list[Belief]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(
        [
            "id",
            "assumption",
            "type_suggested",
            "status",
            "falsify_test",
            "unnecessary_test",
            "reversal_test",
            "evidence_needed",
            "cheapest_probe",
        ]
    )
    for r in rows:
        writer.writerow(
            [r.id, r.assumption, r.type, r.status, r.falsify, r.unnecessary, r.reverse, r.evidence, r.probe]
        )
    return buf.getvalue()


def render_json(problem: str, rows: list[Belief], notes: list[str], seed: int) -> str:
    return json.dumps(
        {
            "problem": problem.strip() if problem else None,
            "seed": seed,
            "notes": notes,
            "count": len(rows),
            "assumptions": [asdict(r) for r in rows],
        },
        indent=2,
    )


DECISION_RULE = (
    "keep if supported; reframe if contradicted; inconclusive -> next probe "
    "or accept provisionally with a review trigger; label result fact/assumption/speculation"
)


def render_test_markdown(rows: list[Belief]) -> str:
    out = ["# Pressure-test plan", ""]
    for r in rows:
        out += [
            f"## {r.id}. {r.assumption}",
            "",
            f"- **Suggested type:** {r.type} - {SUBTYPE_HELP[r.type]}",
            f"- **Status:** {r.status}",
            "",
            "### 1. Falsification test",
            "",
            r.falsify,
            "",
            "### 2. Unnecessary test",
            "",
            r.unnecessary,
            "",
            "### 3. Reversal test",
            "",
            r.reverse,
            "",
            f"- **Evidence to gather:** {r.evidence}",
            f"- **Cheapest probe:** {r.probe}",
            "- **Decision rule (fill before running):** keep if ___; reframe if ___; "
            "inconclusive -> next probe or accept provisionally with a review trigger.",
            "- **Label the result:** fact / assumption / speculation.",
            "",
        ]
    out += [
        "Do not run safety-, legal-, privacy-, or financial-control probes in production.",
        "",
    ]
    return "\n".join(out)


def render_test_csv(rows: list[Belief]) -> str:
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(
        ["id", "assumption", "type_suggested", "test", "question", "evidence", "probe", "decision_rule"]
    )
    for r in rows:
        for test, question in (
            ("falsify", r.falsify),
            ("unnecessary", r.unnecessary),
            ("reverse", r.reverse),
        ):
            writer.writerow([r.id, r.assumption, r.type, test, question, r.evidence, r.probe, DECISION_RULE])
    return buf.getvalue()


def render_test_json(rows: list[Belief], seed: int) -> str:
    items = []
    for r in rows:
        items.append(
            {
                "id": r.id,
                "assumption": r.assumption,
                "type_suggested": r.type,
                "status": r.status,
                "tests": {
                    "falsify": r.falsify,
                    "unnecessary": r.unnecessary,
                    "reverse": r.reverse,
                },
                "evidence_needed": r.evidence,
                "cheapest_probe": r.probe,
                "decision_rule": DECISION_RULE,
            }
        )
    return json.dumps({"seed": seed, "count": len(items), "assumptions": items}, indent=2)


def list_families() -> str:
    lines = [
        "Belief subtypes and example prompts",
        "===================================",
        "",
    ]
    for subtype, help_text in SUBTYPE_HELP.items():
        pack = PROMPTS[pack_for(subtype)]
        lines += [f"{subtype}: {help_text}", ""]
        for test in ("falsify", "unnecessary", "reverse"):
            lines.append(f"  {test}: {pack[test][0]}")
        lines += [f"  evidence: {pack['evidence']}", f"  probe: {pack['probe']}", ""]
    lines += [
        "Examples",
        "--------",
        '  inventory.py --problem "New users must complete a tutorial before they can use the product"',
        '  inventory.py --problem "..." --assumption "Onboarding must be a tutorial" --assumption "Support is chat-only" --format csv',
        '  inventory.py --test --assumption "Onboarding must be a tutorial" --seed 7',
        "",
        "Assumptions start unverified. The helper does not infer evidence or confidence.",
        "",
    ]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Build an assumption inventory and test prompts. Offline; no network.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--problem", help="Problem statement to inventory")
    parser.add_argument(
        "--assumption",
        action="append",
        default=[],
        metavar="BELIEF",
        help="A belief to inventory; repeat for multiple",
    )
    parser.add_argument(
        "--assumptions",
        metavar="LIST",
        help="Beliefs separated by semicolons or newlines",
    )
    parser.add_argument("--test", action="store_true", help="Emit a detailed falsify/unnecessary/reverse plan")
    parser.add_argument("--seed", type=int, default=0, help="Seed for prompt variant selection (default 0)")
    parser.add_argument("--format", choices=("md", "csv", "json"), default="md", help="Output format (default md)")
    parser.add_argument("--list", action="store_true", help="List belief subtypes and prompt examples, then exit")
    args = parser.parse_args(argv)

    if args.list:
        print(list_families())
        return 0

    problem = (args.problem or "").strip()
    assumptions = [normalize(a) for a in args.assumption if a.strip()]
    assumptions += split_assumptions(args.assumptions)

    notes: list[str] = []
    if not assumptions and problem:
        assumptions = [normalize(a) for a in extract_candidates(problem)]
        notes.append(
            "No --assumption supplied; rows below are modal/ordering clauses extracted from the problem "
            "statement. Add explicit beliefs for coverage across boundary and source."
        )
    elif not assumptions:
        parser.error("provide --problem or at least one --assumption (or use --list)")

    rows = build(assumptions, args.seed)

    if args.test:
        if args.format == "json":
            print(render_test_json(rows, args.seed))
        elif args.format == "csv":
            sys.stdout.write(render_test_csv(rows))
        else:
            print(render_test_markdown(rows))
        return 0

    if args.format == "json":
        print(render_json(problem, rows, notes, args.seed))
    elif args.format == "csv":
        sys.stdout.write(render_csv(rows))
    else:
        print(render_markdown(problem, rows, notes))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
