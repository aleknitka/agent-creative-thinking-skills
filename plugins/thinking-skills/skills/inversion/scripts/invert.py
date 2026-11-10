#!/usr/bin/env python3
"""invert.py — offline inversion prompt generator.

Inversion starts with the opposite question: how could we guarantee failure?
This helper builds that question, sweeps it across domains, and shows the
negate -> positive -> testable transformation for a failure route.

Usage:
  python scripts/invert.py --goal "60% of new accounts reach first value in 7 days"

  python scripts/invert.py --goal "cut onboarding time in half" \
      --domains incentive,information,ownership

  python scripts/invert.py --outcome "accounts stall after setup and churn" --json

  python scripts/invert.py --route "activation has no owner, so drop-off is never reviewed"

  python scripts/invert.py --list-domains

No network, no dependencies, no third-party content.
"""
from __future__ import annotations

import argparse
import json
import sys
import textwrap

CORE_PROMPTS: list[str] = [
    "How could we guarantee that {target}?",
    "What would make {target} impossible?",
    "How would a competent adversary make {target}?",
    "How would a well-meaning team sabotage {target} without noticing?",
    "What would we do if we were paid to make {target}?",
    "What did the last five attempts at this do that kept {target} from happening?",
]

DOMAINS: list[tuple[str, list[str]]] = [
    (
        "incentive",
        [
            "Who is rewarded for the opposite outcome?",
            "Who bears the cost of failure, and who captures the upside?",
            "Where is the rational workaround for the intended process?",
            "What would a person optimising their own bonus do?",
        ],
    ),
    (
        "information",
        [
            "What is never measured, or measured with a proxy that hides the outcome?",
            "Who learns about the problem last?",
            "What does the dashboard average away?",
            "Which signal would need to exist to notice this failing early?",
        ],
    ),
    (
        "sequencing",
        [
            "What must happen before value is delivered, and what if it never does?",
            "What happens if the hardest step comes first?",
            "Where does the process require motivation before proof?",
        ],
    ),
    (
        "capability",
        [
            "Which skill, system, or person is load-bearing and unreplaceable?",
            "What breaks at 3x volume or half the staffing?",
            "Which step needs a capability we do not actually have?",
        ],
    ),
    (
        "ownership",
        [
            "Which decision has no owner?",
            "Which handoff has two owners, or none?",
            "Who is accountable when the metric stalls?",
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
        "environment",
        [
            "Which external condition must hold (market, regulation, platform, supplier)?",
            "What happens if the price, policy, or platform changes?",
        ],
    ),
    (
        "psychology",
        [
            "What does the user actually attend to, and where does friction exceed motivation?",
            "What does the user believe that is false?",
            "Where does the process ask for trust before evidence?",
        ],
    ),
    (
        "measurement",
        [
            "What proxy could replace the real goal?",
            "What would look like success while the goal fails?",
            "Which cohort is excluded from the metric?",
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

PRINCIPLE_TEMPLATE = {
    "negate": "Negated mechanism: {negation}",
    "positive": "Principle: {actor} does {action}, so that {condition}.",
    "signal": "Signal: {signal}",
    "decision": "Owner / decision: {owner} may change {decision}.",
    "tradeoff": "Trade-off: {tradeoff}",
}


def fail(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(2)


def wrap(label: str, text: str, width: int = 88) -> str:
    body = textwrap.fill(text, width=width, initial_indent="", subsequent_indent=" " * len(label))
    return f"{label}{body}"


def domain_list(value: str) -> list[str]:
    names = [d.strip().lower() for d in value.split(",") if d.strip()]
    known = {name for name, _ in DOMAINS}
    unknown = [n for n in names if n not in known]
    if unknown:
        fail(f"unknown domain(s): {', '.join(unknown)} (use --list-domains)")
    return names


def build(goal: str | None, outcome: str | None, domains: list[str]) -> dict:
    target = goal or outcome
    if not target:
        fail("pass --goal, --outcome, or --route (or --list-domains)")
    mode = "goal" if goal else "outcome"
    selected = [(n, qs) for n, qs in DOMAINS if not domains or n in domains]
    return {
        "mode": mode,
        "target": target,
        "note": (
            "Generate 15-25 specific routes before judging any of them. "
            "Each route needs a mechanism and an actor; reject labels."
        ),
        "core_prompts": [p.format(target=target) for p in CORE_PROMPTS],
        "domains": {
            name: [q.replace("{target}", target) for q in questions]
            for name, questions in selected
        },
        "principle_template": PRINCIPLE_TEMPLATE,
    }


def render(data: dict) -> str:
    lines: list[str] = []
    title = "Guaranteed failure" if data["mode"] == "goal" else "Guaranteed unwanted outcome"
    lines.append(f"{title}: {data['target']}")
    lines.append("")
    lines.append(data["note"])
    lines.append("")
    lines.append("Core prompts")
    for prompt in data["core_prompts"]:
        lines.append(wrap("  - ", prompt))
    for name, questions in data["domains"].items():
        lines.append("")
        lines.append(f"{name.replace('_', ' ').title()}")
        for question in questions:
            lines.append(wrap("  - ", question))
    lines.append("")
    lines.append("After generating: cluster by causal mechanism (3-6 clusters), then")
    lines.append("negate each cluster into a positive, testable principle:")
    for key, template in data["principle_template"].items():
        lines.append(f"  {key}: {template}")
    return "\n".join(lines)


def render_route(route: str) -> str:
    return "\n".join(
        [
            f"Failure route: {route}",
            "",
            "1. Negate it — what standing condition is absent?",
            "2. Make it positive — who does what, so that which condition holds?",
            "3. Make it testable — what signal would show it is violated, and",
            "   what decision can the owner change?",
            "",
            "Fill in:",
            "  Principle: <actor> does <action>, so that <condition>.",
            "  Signal: <observable indicator>.",
            "  Owner / decision: <owner> may change <decision>.",
            "  Trade-off: <what this costs>.",
        ]
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate inversion prompts, the domain sweep, and a principle template."
    )
    parser.add_argument("--goal", help="the outcome you want (verb phrase)")
    parser.add_argument("--outcome", help="the unwanted outcome to make reliable")
    parser.add_argument("--route", help="a single failure route to convert into a principle")
    parser.add_argument("--domains", help="comma-separated subset of domains")
    parser.add_argument("--list-domains", action="store_true", help="list domain names and exit")
    parser.add_argument("--json", action="store_true", help="machine-readable output")
    args = parser.parse_args()

    if args.list_domains:
        for name, questions in DOMAINS:
            print(f"{name}: {questions[0]}")
        return 0

    if args.route:
        print(render_route(args.route))
        return 0

    if args.goal and args.outcome:
        fail("pass --goal or --outcome, not both")

    domains = domain_list(args.domains) if args.domains else []
    data = build(args.goal, args.outcome, domains)
    print(json.dumps(data, indent=2) if args.json else render(data))
    return 0


if __name__ == "__main__":
    sys.exit(main())
