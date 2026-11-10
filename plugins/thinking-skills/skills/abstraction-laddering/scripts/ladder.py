#!/usr/bin/env python3
"""Emit abstraction-ladder prompts for a problem statement.

Offline helper: takes a statement and prints why-up / how-down prompt rungs
plus stop checks. No network, no dependencies.
"""
from __future__ import annotations

import argparse
import json
import sys

UP_PROMPTS = [
    ("Why does this matter?", "Answer with a goal or outcome, not a restatement of the solution."),
    ("What is this in service of?", "Name a beneficiary and what changes for them."),
    ("If this worked perfectly, what would be different?", "Describe the outcome, not the feature."),
    ("Which higher commitment does this serve?", "Prefer a purpose you can act on over a value you cannot."),
    ("Who ultimately benefits, and from what?", "Stop if the next answer is universal."),
]

DOWN_PROMPTS = [
    ("How could this happen?", "Answer with a mechanism or enabling condition, not a task list."),
    ("What would have to be true for that?", "Name a condition that could be checked."),
    ("What currently prevents this?", "Name a cause, not an owner."),
    ("What is the smallest version that would still test it?", "Keep it observable."),
    ("How would we know it happened?", "Define the observable before acting."),
]

STOP_UP = [
    "The answer names the ultimate beneficiary and no further stakeholder is added.",
    "The next why becomes universal (\"so people are happy\").",
    "The next why leaves the scope you can influence or measure.",
    "Another why would only restate the same purpose in grander words.",
]

STOP_DOWN = [
    "The rung is observable and testable within budget.",
    "Further decomposition needs knowledge you do not have; record the unknown.",
    "You have reached an owner or scheduled action with no mechanism question left.",
    "You are writing task tickets rather than causal conditions.",
]

LEVEL_HINTS = {
    1: "nearby (function / mechanism)",
    2: "broader (purpose)",
    3: "wide (purpose / vision)",
    4: "very wide (vision)",
    5: "at the ceiling (vision / values)",
}


def clean(text: str) -> str:
    return " ".join(text.split())


def build(statement: str, rounds: int, direction: str) -> dict:
    up = []
    down = []
    if direction in ("both", "up"):
        for i in range(rounds):
            q, hint = UP_PROMPTS[i % len(UP_PROMPTS)]
            up.append({"rung": i + 1, "prompt": q, "hint": hint,
                       "label": f"Up +{i + 1}"})
    if direction in ("both", "down"):
        for i in range(rounds):
            q, hint = DOWN_PROMPTS[i % len(DOWN_PROMPTS)]
            down.append({"rung": i + 1, "prompt": q, "hint": hint,
                         "label": f"Down -{i + 1}"})
    return {
        "statement": statement,
        "up": up,
        "down": down,
        "stop_up": STOP_UP,
        "stop_down": STOP_DOWN,
        "level_hints": {str(k): v for k, v in LEVEL_HINTS.items()},
    }


def render(payload: dict) -> str:
    lines = [f"# Abstraction Ladder — {payload['statement']}", ""]
    if payload["up"]:
        lines += ["## Up — why", ""]
        for rung in payload["up"]:
            lines.append(f"**{rung['label']}** — {rung['prompt']}")
            lines.append(f"- hint: {rung['hint']}")
            lines.append(f"- answer: ____________________  [{LEVEL_HINTS.get(rung['rung'], '')}]")
            lines.append("")
    if payload["down"]:
        lines += ["## Down — how", ""]
        for rung in payload["down"]:
            lines.append(f"**{rung['label']}** — {rung['prompt']}")
            lines.append(f"- hint: {rung['hint']}")
            lines.append("- answer: ____________________  [more specific + testable]")
            lines.append("")
    if payload["up"]:
        lines += ["## Stop check (up)", ""]
        lines += [f"- {item}" for item in payload["stop_up"]]
        lines.append("")
    if payload["down"]:
        lines += ["## Stop check (down)", ""]
        lines += [f"- {item}" for item in payload["stop_down"]]
        lines.append("")
    lines += ["## Before you choose", "",
              "- Label each rung: fact / assumption / speculation.",
              "- Check each adjacent pair: does the lower rung serve the one above?",
              "- Pick a leverage point on impact x controllability x evidence,",
              "  then write one observable and one decision rule.",
              ""]
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Emit abstraction-ladder prompts for a problem statement.")
    parser.add_argument("statement", nargs="?", help="problem statement; omit or '-' to read stdin")
    parser.add_argument("--rounds", type=int, default=3, choices=range(1, 6),
                        help="number of rungs per direction (1-5, default 3)")
    parser.add_argument("--direction", choices=("both", "up", "down"), default="both",
                        help="which way to ladder (default both)")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of markdown")
    args = parser.parse_args(argv)

    raw = args.statement
    if raw in (None, "-"):
        raw = sys.stdin.read()
    statement = clean(raw or "")
    if not statement:
        parser.error("empty statement; pass one as an argument or on stdin")

    payload = build(statement, args.rounds, args.direction)
    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print(render(payload))
    return 0


if __name__ == "__main__":
    sys.exit(main())
