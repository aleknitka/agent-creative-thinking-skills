#!/usr/bin/env python3
"""
what_if.py — offline assumption picker and world-sketch generator for the what-if skill.

No dependencies, no network. Deterministic with --seed. The output is a set of
mutation prompts plus blank world-sketch scaffolds; it does not generate insights.

Usage:
  python scripts/what_if.py --list
  python scripts/what_if.py --subject "internal knowledge base" --types resource,interface --seed 7
  python scripts/what_if.py --subject "clinic scheduling" --types all --count 2
  python scripts/what_if.py --subject "onboarding" --json --seed 42
"""
from __future__ import annotations

import argparse
import json
import random
import sys

TYPES: dict[str, dict] = {
    "resource": {
        "name": "Resource",
        "why": "Scarcity assumptions shape capacity and business model. Removing the constraint reveals what becomes worth doing.",
        "questions": [
            "What if the binding resource were effectively unlimited?",
            "What if it were free but every other resource stayed scarce?",
            "What if a different resource became the constraint?",
        ],
        "moves": [
            {
                "assumption": "The binding resource is expert time.",
                "mutation": "What if expert time were effectively unlimited?",
            },
            {
                "assumption": "Money is the constraint on what can be attempted.",
                "mutation": "What if the budget were 100x larger but headcount were fixed?",
            },
            {
                "assumption": "User attention is scarce and must be earned.",
                "mutation": "What if every user had unlimited attention for this?",
            },
            {
                "assumption": "The resource must be owned or controlled by us.",
                "mutation": "What if the resource were shared across competitors?",
            },
        ],
    },
    "interface": {
        "name": "Interface",
        "why": "Interfaces encode assumptions about where, when, and how work reaches the system. Removing or moving one changes discovery and ownership.",
        "questions": [
            "What if there were no interface at all?",
            "What if the interface were ambient, or inside someone else's workflow?",
            "What if the system initiated the interaction instead of waiting?",
        ],
        "moves": [
            {
                "assumption": "Users come to our interface: app, site, form, or counter.",
                "mutation": "What if there were no interface at all?",
            },
            {
                "assumption": "The system waits to be asked.",
                "mutation": "What if the system initiated the interaction at the right moment?",
            },
            {
                "assumption": "The interface belongs to us and carries our brand.",
                "mutation": "What if the interface lived inside someone else's workflow?",
            },
            {
                "assumption": "The unit of interaction is a page, screen, or form.",
                "mutation": "What if there were no screens or pages, only ambient signals?",
            },
        ],
    },
    "actor": {
        "name": "Actor",
        "why": "Actor assumptions hide in the word 'user'. A different actor forces different vocabulary, permissions, and success criteria.",
        "questions": [
            "What if the primary user were someone else entirely?",
            "What if the user had no context, training, or shared vocabulary?",
            "What if a machine agent were the primary actor?",
        ],
        "moves": [
            {
                "assumption": "The primary user is the current, trained customer.",
                "mutation": "What if the primary user were a day-one beginner with no shared vocabulary?",
            },
            {
                "assumption": "The buyer decides on behalf of the user.",
                "mutation": "What if the end user held the buying power?",
            },
            {
                "assumption": "The actor is a human being.",
                "mutation": "What if a machine agent were the primary actor?",
            },
            {
                "assumption": "The operator and the beneficiary are different people.",
                "mutation": "What if the operator and the beneficiary were the same person?",
            },
        ],
    },
    "rule": {
        "name": "Rule",
        "why": "Rules encode past fears and current power. Repealing or inverting one exposes what the rule was protecting.",
        "questions": [
            "What if this rule did not exist?",
            "What if the opposite were required?",
            "What if success were measured by a different variable?",
        ],
        "moves": [
            {
                "assumption": "Changes require approval before they take effect.",
                "mutation": "What if no approval were required?",
            },
            {
                "assumption": "Success is measured by the current primary metric.",
                "mutation": "What if success were measured by the metric's opposite?",
            },
            {
                "assumption": "Access is default-denied and must be granted.",
                "mutation": "What if access were default-granted and revocation were explicit?",
            },
            {
                "assumption": "The rule applies equally to everyone.",
                "mutation": "What if the rule applied only to the most powerful actor?",
            },
        ],
    },
    "scale": {
        "name": "Scale",
        "why": "Scale assumptions decide what feels efficient. Changing the unit or volume changes the operating model, not just the size.",
        "questions": [
            "What if there were 1000x more or fewer users?",
            "What if the unit were one person, one interaction, or one planet?",
            "What if it had to work everywhere at once?",
        ],
        "moves": [
            {
                "assumption": "The design target is the current number of users.",
                "mutation": "What if there were 1000x more users?",
            },
            {
                "assumption": "The unit of analysis is the whole organization.",
                "mutation": "What if the unit were one person or one interaction?",
            },
            {
                "assumption": "The service is local or regional.",
                "mutation": "What if it had to work globally on day one?",
            },
            {
                "assumption": "The scope is the full end-to-end workflow.",
                "mutation": "What if you could serve only one step of the workflow?",
            },
        ],
    },
    "time": {
        "name": "Time",
        "why": "Latency, cadence, and sequence change which failure modes matter. Speed exposes trust problems; slowness exposes commitment problems.",
        "questions": [
            "What if it happened instantly, or took a decade?",
            "What if it were continuous rather than episodic?",
            "What if the order were reversed?",
        ],
        "moves": [
            {
                "assumption": "The process takes days or weeks.",
                "mutation": "What if the process were instant?",
            },
            {
                "assumption": "The cadence is periodic: weekly, monthly, annually.",
                "mutation": "What if the cadence were continuous?",
            },
            {
                "assumption": "The sequence is fixed from first step to last.",
                "mutation": "What if the last step came first?",
            },
            {
                "assumption": "The artifact is reviewed and refreshed periodically.",
                "mutation": "What if every artifact expired daily and had to be re-earned?",
            },
        ],
    },
}

ORDER = ["resource", "interface", "actor", "rule", "scale", "time"]

SKETCH_FIELDS = [
    ("Premise", "one sentence: what if <mutation> were simply true?"),
    ("Held fixed", "3-5 assumptions you are not changing (the control group)"),
    ("What changes immediately", "direct, mechanical consequences of the premise"),
    ("What stays the same", "what the mutation does not touch"),
    ("What must be true", "physical, economic, social, or technical preconditions"),
    ("Who thrives / who loses", "distributional effects; name both"),
    ("New frictions", "at least two problems the world creates"),
    ("Artifact", "what exists in this world that does not exist now"),
    ("Open questions", "what you would need to know to take the world seriously"),
    ("Transferable insight", "the mechanism that survives without the impossible premise"),
    ("Probe", "smallest test in current reality, with leading signal and kill criterion"),
]

PROCESS = [
    "Pick one mutation and hold everything else fixed.",
    "Fill the world sketch concretely, including at least two new frictions.",
    "Trace first-, second-, and third-order consequences; include gains and harms.",
    "Extract one insight that still makes sense without the impossible premise.",
    "Define a probe in current reality; label the rest as speculation.",
]

SOURCES = [
    "Counterfactual reasoning (Lewis, 1973); scenario planning (Kahn/Wack/Schwartz); futures wheel (Glenn, 1972); pre-mortem (Klein, 2007)",
    "Six-type taxonomy, world sketch, and this script are adaptations by this repository; see references/provenance.md",
]


def parse_types(raw: str | None) -> list[str]:
    if not raw or raw.strip().lower() == "all":
        return ORDER
    chosen: list[str] = []
    for part in raw.split(","):
        key = part.strip().lower()
        if not key:
            continue
        if key not in TYPES:
            print(f"error: unknown type '{key}' (choose from {', '.join(ORDER)} or all)", file=sys.stderr)
            sys.exit(2)
        if key not in chosen:
            chosen.append(key)
    return chosen or ORDER


def pick_worlds(types: list[str], count: int, seed: int | None) -> list[dict]:
    rnd = random.Random(seed)
    worlds: list[dict] = []
    for key in types:
        moves = TYPES[key]["moves"]
        n = min(count, len(moves))
        for move in rnd.sample(moves, n):
            worlds.append({"type": key, "type_name": TYPES[key]["name"], **move})
    return worlds


def print_list() -> None:
    for key in ORDER:
        data = TYPES[key]
        print(f"{key} — {data['name']}")
        print(f"  Why: {data['why']}")
        for q in data["questions"]:
            print(f"  - {q}")
        print(f"  Moves: {len(data['moves'])}")
        print()


def print_worlds(subject: str, worlds: list[dict], seed: int | None) -> None:
    print(f"Subject: {subject}")
    print(f"Seeded: {seed if seed is not None else 'no'}")
    print()
    for i, world in enumerate(worlds, 1):
        print(f"=== {i}. {world['type_name']} — {world['mutation']} ===")
        print(f"Assumption under test: {world['assumption']}")
        print("World sketch:")
        for label, hint in SKETCH_FIELDS:
            print(f"  {label}: [{hint}]")
        print()


def main() -> None:
    p = argparse.ArgumentParser(description="What-if assumption picker and world sketches (offline)")
    p.add_argument("--subject", type=str, default="", help="the subject in 3-5 sentences, or a short label")
    p.add_argument("--types", type=str, default="all", help="comma-separated: resource,interface,actor,rule,scale,time, or all")
    p.add_argument("--count", type=int, default=1, help="worlds per selected type (default 1)")
    p.add_argument("--seed", type=int, default=None, help="seed for reproducible picks")
    p.add_argument("--list", action="store_true", help="list assumption types and triggers, then exit")
    p.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = p.parse_args()

    if args.list:
        print_list()
        return

    if args.count < 1:
        print("error: --count must be >= 1", file=sys.stderr)
        sys.exit(2)

    subject = args.subject.strip() or "(unspecified — define it before branching)"
    types = parse_types(args.types)
    worlds = pick_worlds(types, args.count, args.seed)
    payload = {
        "subject": subject,
        "seed": args.seed,
        "types": types,
        "worlds": [
            {
                "type": w["type"],
                "assumption": w["assumption"],
                "mutation": w["mutation"],
                "sketch_fields": [{"field": label, "hint": hint} for label, hint in SKETCH_FIELDS],
            }
            for w in worlds
        ],
        "process": PROCESS,
        "sources": SOURCES,
    }
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
        return

    print_worlds(subject, worlds, args.seed)
    print("Next:")
    for step in PROCESS:
        print(f"  - {step}")
    print()
    print(f"Source: {SOURCES[0]}")
    print(SOURCES[1])


if __name__ == "__main__":
    main()
