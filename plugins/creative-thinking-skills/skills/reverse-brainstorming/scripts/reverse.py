#!/usr/bin/env python3
"""reverse.py — offline reverse-brainstorming prompt generator.

Reverse brainstorming asks how to make an existing problem worse, then reverses
those bad ideas into improvement directions. This helper builds the worsening
prompts, sweeps them across domains, and prints the reversal checklist.

Usage:
  python scripts/reverse.py --problem "new users never finish setup"

  python scripts/reverse.py --problem "support tickets keep reopening" \
      --domains incentive,information,friction

  python scripts/reverse.py --problem "release notes are ignored" --json

  python scripts/reverse.py --list

No network, no dependencies, no third-party content.
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap

CORE_PROMPTS: list[str] = [
    "How could we guarantee this problem gets worse: {problem}?",
    "How could we make this problem permanent?",
    "How would we cause this problem from scratch, on purpose?",
    "What does this problem need in order to survive? Give it exactly that.",
    "How would an indifferent team accidentally make it worse?",
    "How would a competitor worsen this problem for us?",
    "What would we do if we were paid to make it worse?",
    "How do we already make it slightly worse without noticing?",
]

DOMAINS: list[tuple[str, list[str]]] = [
    (
        "incentive",
        [
            "Who is rewarded for the behavior that sustains the problem?",
            "What is measured instead of the real outcome?",
            "Where is the rational workaround for the intended process?",
            "Who bears the cost of the problem, and who captures the upside?",
        ],
    ),
    (
        "information",
        [
            "What is never observed, or reported too late?",
            "Who learns about the failure last?",
            "What does the dashboard average away?",
            "Which signal would need to exist to notice the problem early?",
        ],
    ),
    (
        "friction",
        [
            "Which step demands effort before any benefit?",
            "Where can we add a form, approval, or wait?",
            "What asks the user to repeat information the system already has?",
        ],
    ),
    (
        "sequence",
        [
            "What could we move before the moment of value?",
            "What could we make irreversible or hard to resume?",
            "What happens if the hardest step comes first?",
        ],
    ),
    (
        "ownership",
        [
            "Which decision has no owner?",
            "Which handoff has two owners, or none?",
            "Who is accountable when the problem repeats?",
        ],
    ),
    (
        "capability",
        [
            "Which skill, system, or person is load-bearing and unreplaceable?",
            "What breaks at 2x volume or half the staffing?",
            "Which step needs a capability we do not actually have?",
        ],
    ),
    (
        "coordination",
        [
            "Where do teams' definitions of done diverge?",
            "Which dependency sits on the critical path?",
            "What breaks if one team is late or reads the interface differently?",
        ],
    ),
    (
        "trust",
        [
            "Where do we ask for trust before evidence?",
            "Where do we punish the user for our mistake?",
            "What promise is made that the process does not keep?",
        ],
    ),
    (
        "environment",
        [
            "Which external condition must hold (network, platform, regulation, supplier)?",
            "What happens if the price, policy, or platform changes?",
            "What assumes a stable connection or device?",
        ],
    ),
    (
        "psychology",
        [
            "What does the user actually attend to, and where does friction exceed motivation?",
            "What does the user believe that is false?",
            "Where does the process require motivation before proof?",
        ],
    ),
    (
        "time",
        [
            "What decays if nobody maintains it?",
            "What is true only at launch?",
            "What takes longer than the patience or budget available?",
        ],
    ),
]

REVERSAL_OPERATORS: list[tuple[str, str]] = [
    (
        "negate the mechanism",
        "If X sustains the problem, what standing condition removes X?",
    ),
    (
        "invert the actor",
        "Who should act here instead of the current actor (system, policy, peer)?",
    ),
    (
        "remove the precondition",
        "What must exist for the bad idea to work, and can we delete it?",
    ),
    (
        "re-scope",
        "Apply the harm to a smaller or larger slice; what changes?",
    ),
    (
        "reverse the sequence",
        "What if the last step came first, or value came before setup?",
    ),
    (
        "turn the harm into a signal",
        "If the bad idea hides something, what would exposing it enable?",
    ),
]

DIRECTIONS = [
    "more frequent",
    "more severe",
    "more persistent",
    "more contagious",
]

QUALITY_CHECKS: list[str] = [
    "Actor: a role, system, metric, or policy does it.",
    "Mechanism: it says how the problem gets worse, not that it might.",
    "Specificity: the sequence of events could be drawn on a whiteboard.",
    "Causal distance: it is upstream of the problem's persistence.",
]


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(2)


def wrap(label: str, text: str, width: int = 88) -> str:
    body = textwrap.fill(
        text, width=width, initial_indent="", subsequent_indent=" " * len(label)
    )
    return f"{label}{body}"


def domain_list(value: str) -> list[str]:
    names = [d.strip().lower() for d in value.split(",") if d.strip()]
    known = {name for name, _ in DOMAINS}
    unknown = [n for n in names if n not in known]
    if unknown:
        fail(f"unknown domain(s): {', '.join(unknown)} (use --list)")
    return names


def build(problem: str, domains: list[str]) -> dict:
    selected = [(n, qs) for n, qs in DOMAINS if not domains or n in domains]
    return {
        "problem": problem,
        "note": (
            "Generate 15-25 specific bad ideas independently before discussing any. "
            "Do not reverse or fix during this pass."
        ),
        "directions": DIRECTIONS,
        "core_prompts": [p.format(problem=problem) for p in CORE_PROMPTS],
        "domains": {name: questions for name, questions in selected},
        "reversal_operators": [
            {"operator": op, "question": q} for op, q in REVERSAL_OPERATORS
        ],
        "reversal_checklist": QUALITY_CHECKS,
    }


def render(data: dict) -> str:
    lines: list[str] = [f"Problem: {data['problem']}", "", data["note"], ""]
    lines.append("Worsen in one of four directions: " + ", ".join(data["directions"]))
    lines.append("")
    lines.append("Core prompts")
    for prompt in data["core_prompts"]:
        lines.append(wrap("  - ", prompt))
    for name, questions in data["domains"].items():
        lines.append("")
        lines.append(name.replace("_", " ").title())
        for question in questions:
            lines.append(wrap("  - ", question))
    lines.append("")
    lines.append("Reverse: cluster the bad ideas by mechanism first (3-6 clusters).")
    lines.append("Apply one operator per cluster:")
    for entry in data["reversal_operators"]:
        lines.append(wrap(f"  - {entry['operator']}: ", entry["question"]))
    lines.append("")
    lines.append("Write each direction as actor + action + condition, then check:")
    for check in data["reversal_checklist"]:
        lines.append(f"  [ ] {check}")
    lines.append("")
    lines.append("Harvest 2-3 concepts; for each: first probe, leading signal, kill criterion.")
    return "\n".join(lines)


def render_list() -> str:
    lines = ["Worsening domains:"]
    for name, questions in DOMAINS:
        lines.append(f"  {name}: {questions[0]}")
    lines.append("")
    lines.append("Reversal operators:")
    for op, question in REVERSAL_OPERATORS:
        lines.append(f"  {op}: {question}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Generate worsening prompts, the domain sweep, and the reversal checklist "
            "for reverse brainstorming."
        )
    )
    parser.add_argument("--problem", help="the persisting problem, verbatim")
    parser.add_argument("--domains", help="comma-separated subset of domains")
    parser.add_argument("--list", action="store_true", help="list domains and operators")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    if args.list:
        print(render_list())
        return 0

    if not args.problem:
        fail("pass --problem (or --list)")

    domains = domain_list(args.domains) if args.domains else []
    data = build(args.problem, domains)
    print(json.dumps(data, indent=2) if args.json else render(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
