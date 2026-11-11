#!/usr/bin/env python3
"""
scamper.py — offline helper for the SCAMPER skill.

Generates operator-focused trigger questions for a given baseline subject.
No dependencies, no network. Supports full 7-operator pass or selective mode.

Usage:
  python scripts/scamper.py --subject "banking onboarding: account opening in branch, welcome letter, card/PIN mailings"
  python scripts/scamper.py --subject "dashboard AI summaries" --select S,C,E --time 25
  python scripts/scamper.py --subject "our support callback process" --json
  python scripts/scamper.py --list
"""
from __future__ import annotations

import argparse
import json
import textwrap

OPERATORS = {
    "S": {
        "name": "Substitute",
        "question": "What can be replaced with something else?",
        "triggers": [
            "Which material, component, or ingredient could be used instead?",
            "Which process step could be replaced by a different one?",
            "Which technology could replace an existing one?",
            "Which human touchpoint could become digital — or vice versa?",
            "Which channel (phone, email, chat) or pricing mechanism (fixed, subscription, pay-per-use) could replace the current one?",
        ],
    },
    "C": {
        "name": "Combine",
        "question": "What can be combined with something else?",
        "triggers": [
            "Which two separate steps or touchpoints could become one?",
            "Which services from different industries could be bundled?",
            "Which internal processes could be merged so the customer feels a seamless flow?",
            "Which data from different systems could be combined for new value?",
        ],
    },
    "A": {
        "name": "Adapt",
        "question": "What can be borrowed or adapted from elsewhere?",
        "triggers": [
            "Which solution from another industry solves a similar problem?",
            "Which analogy from nature, art, or technology could inspire?",
            "Which customer experience from hospitality, e-commerce, or gaming could be adapted?",
            "Which best practice from another country or company could be transferred?",
        ],
    },
    "M": {
        "name": "Modify / Magnify / Minimize",
        "question": "What can be enlarged, reduced, intensified, or toned down?",
        "triggers": [
            "What happens if we double or halve the frequency?",
            "What happens if we shorten response time from 24 hours to 1 hour?",
            "What happens if we radically expand or strip the scope to essentials?",
            "What happens if we massively increase personalization — or narrow to the top 10% of customers?",
        ],
    },
    "P": {
        "name": "Put to other use",
        "question": "What else could this (or part of it) be used for?",
        "triggers": [
            "Are there other target groups or contexts where this provides value?",
            "Which data collected during the service could be offered as standalone value?",
            "Could an internal training process or tool be offered externally?",
            "Which internal capability could be marketed as a product?",
        ],
    },
    "E": {
        "name": "Eliminate",
        "question": "What can be removed, simplified, or omitted?",
        "triggers": [
            "Which process step exists only for historical reasons?",
            "Which feature is used by fewer than 10% of users?",
            "Which form, input, or approval could be replaced by automatic data transfer?",
            "What could we leave out without losing core value?",
        ],
    },
    "R": {
        "name": "Reverse / Rearrange",
        "question": "What happens if we reverse the order or rearrange elements?",
        "triggers": [
            "What happens if we reverse the order of steps?",
            "What happens if the customer configures the service instead of the company?",
            "What happens if we deliver at the customer's location instead of ours?",
            "What happens if we shift from reactive to proactive — act before the problem occurs?",
        ],
    },
}

ORDER = ["S", "C", "A", "M", "P", "E", "R"]

SELECT_GUIDANCE = {
    "E": "Highest ROI for legacy processes with bloat — historic steps that no longer earn their keep.",
    "S": "Highest ROI for legacy channels/materials to digitize or swap.",
    "C": "When integration is the goal — merge touchpoints into a seamless flow.",
    "R": "When roles or sequence are the constraint — reverse who does what, when.",
    "A": "When differentiation is needed — import a mechanism from another industry.",
    "M": "When scope or intensity is the lever — magnify or minimize.",
    "P": "When byproducts or data are underused — repurpose what already exists.",
}

SUBJECT_HINTS = [
    "Define the baseline in 3–5 sentences: steps, touchpoints, who is involved, what triggers it, what the outcome is.",
    "Name what works and what doesn't before you generate — don't start from a topic label like 'our customer service'.",
    "Pick 3–4 most relevant operators if time is short; quality beats racing through all 7 superficially.",
]


def parse_selection(s: str | None) -> list[str]:
    if not s:
        return ORDER
    raw = [x.strip().upper() for x in s.split(",")]
    # Expand single letters; allow full names loosely — map first letter
    out: list[str] = []
    for x in raw:
        if x in OPERATORS:
            out.append(x)
        elif x and x[0] in OPERATORS:
            out.append(x[0])
    # Preserve ORDER for chosen ones
    chosen = [k for k in ORDER if k in out]
    return chosen if chosen else ORDER


def main() -> None:
    p = argparse.ArgumentParser(description="SCAMPER checklist helper (offline)")
    p.add_argument("--subject", type=str, default="", help="baseline subject in 3-5 sentences (or free text)")
    p.add_argument("--select", type=str, default=None, help="comma-separated operators subset, e.g. S,C,E or S,E")
    p.add_argument("--time", type=int, default=None, help="total minutes available (affects guidance)")
    p.add_argument("--list", action="store_true", help="list operators and exit")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    if args.list:
        for k in ORDER:
            op = OPERATORS[k]
            print(f"{k} — {op['name']}: {op['question']}")
            for t in op["triggers"]:
                print(f"  - {t}")
            print(f"  Guidance: {SELECT_GUIDANCE[k]}")
            print()
        return

    subject = args.subject.strip()
    selected = parse_selection(args.select)

    if not subject:
        # Still useful without subject — print checklist for selected operators
        if args.json:
            out = {
                "mode": "checklist",
                "operators": [
                    {"key": k, "name": OPERATORS[k]["name"], "question": OPERATORS[k]["question"], "triggers": OPERATORS[k]["triggers"], "guidance": SELECT_GUIDANCE[k]}
                    for k in selected
                ],
                "hints": SUBJECT_HINTS,
                "sources": ["Alex F. Osborn — Applied Imagination (1953); Bob Eberle — SCAMPER (1971)", "This repo: references/operators.md"],
            }
            print(json.dumps(out, indent=2, ensure_ascii=False))
        else:
            print("SCAMPER checklist — define your baseline subject first (3–5 sentences).")
            print()
            for k in selected:
                op = OPERATORS[k]
                print(f"{k} — {op['name']}: {op['question']}")
                for t in op["triggers"]:
                    print(f"  - {t}")
            print()
            for h in SUBJECT_HINTS:
                print(f"Hint: {h}")
        return

    # With subject: emit per-operator prompts tailored with subject header
    per_op_minutes = None
    if args.time:
        # reserve ~10 min prep + 15 min follow-up heuristics
        gen_minutes = max(12, args.time - 20)
        per_op_minutes = max(3, gen_minutes // len(selected))

    if args.json:
        out = {
            "subject": subject,
            "selected_operators": selected,
            "total_minutes": args.time,
            "per_operator_minutes": per_op_minutes,
            "operators": [
                {
                    "key": k,
                    "name": OPERATORS[k]["name"],
                    "question": OPERATORS[k]["question"],
                    "triggers": OPERATORS[k]["triggers"],
                    "guidance": SELECT_GUIDANCE[k],
                }
                for k in selected
            ],
            "process": textwrap.dedent("""
                Per operator: 4-5 min silent brainwriting (everyone notes ideas), then 2 min sharing — no clustering until all operators are done.
                Follow-up: cluster → dot-vote or 2x2 (innovation × feasibility) → select top 2-3 concepts → define one next probe each.
            """).strip(),
            "sources": ["Alex F. Osborn — Applied Imagination (1953); Bob Eberle — SCAMPER (1971)"],
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    print(f"Subject: {subject}")
    if args.time:
        print(f"Time: ~{args.time} min total ({'selective' if len(selected) < 7 else 'sequential'} mode, ~{per_op_minutes} min per operator)")
    print(f"Operators: {', '.join(selected)} ({'all 7' if len(selected) == 7 else 'selective — ' + ', '.join(SELECT_GUIDANCE[k] for k in selected[:2])})")
    print()
    for k in selected:
        op = OPERATORS[k]
        print(f"{k} — {op['name']}: {op['question']}")
        for t in op["triggers"]:
            print(f"  - {t}")
        print()
    print("Per operator: 4-5 min silent brainwriting, then 2 min sharing — no clustering yet.")
    print("Follow-up: cluster → evaluate (dot-vote or 2×2) → select top 2-3 concepts → define one next probe each.")
    if len(selected) < 7:
        print()
        print("Selective mode hint: prefer 3–4 deep passes over 7 shallow ones.")
        for k in selected:
            print(f"  {k}: {SELECT_GUIDANCE[k]}")


if __name__ == "__main__":
    main()
