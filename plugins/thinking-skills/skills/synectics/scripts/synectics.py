#!/usr/bin/env python3
"""
synectics.py — offline helper for Synectics (four analogies + excursion).

No network, no deps. Emits analogy prompts and excursion guidance.

Usage:
  python scripts/synectics.py --problem "onboarding activation as a gate"
  python scripts/synectics.py --problem "..." --json
"""
from __future__ import annotations
import argparse, json
import textwrap

ANALOGIES = [
    ("personal", "Personal — be the element", 'Speak as the element: "I am the invite — I feel rushed, then discarded."'),
    ("direct", "Direct — parallel mechanism elsewhere", "Where else does a stranger become a member without a formal gate? How does that system handle it?"),
    ("symbolic", "Symbolic — compressed paradox", 'State the tension as two words that should not go together: "trusted stranger," "guided abandonment," "silent signal."'),
    ("fantasy", "Fantasy — wishful, constraint-free", "If nothing were forbidden, how would activation happen? Record the wish without censoring."),
]

def main():
    p = argparse.ArgumentParser(description="Synectics four-analogies helper (offline)")
    p.add_argument("--problem", type=str, default="", help="problem or familiar metaphor to estrange")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    problem = args.problem.strip() or "(no problem — state the familiar to estrange)"

    if args.json:
        print(json.dumps({
            "problem": problem,
            "analogies": [{"key": k, "name": n, "prompt": pr} for k, n, pr in ANALOGIES],
            "excursion": "Choose the most evocative analogy and explore its world separately for 5–10 minutes with no attempt to solve the original problem.",
            "provenance": "Synectics (Gordon/Prince, 1960s)",
        }, indent=2, ensure_ascii=False))
        return

    print(f"Problem (to estrange): {problem}\n")
    print("Four analogies — build all four in order:")
    for k, n, pr in ANALOGIES:
        print(f"  - {n}: {pr}")
    print(textwrap.dedent("""
        Excursion — depart fully:
          Choose the most evocative analogy and explore its world separately
          for 5–10 minutes with no attempt to solve the original problem.
          Record the excursion as a separate page.

        Then force the return: map the excursion world back onto the problem
        and write springboards — mechanism-flavored possibilities to probe.
    """).strip())

if __name__ == "__main__":
    main()
