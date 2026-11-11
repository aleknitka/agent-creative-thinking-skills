#!/usr/bin/env python3
"""scenarios.py — offline helper for scenario-planning."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Scenario helper (offline)")
    p.add_argument("--question", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"focal_question": args.question or "(no question)", "axes": ["uncertainty A", "uncertainty B"], "worlds": 4, "next": "score each option in each world; name signals per world"}, indent=2, ensure_ascii=False))
    else:
        print(f"Focal question: {args.question or '(no question)'}")
        print("Axes: two top uncertainties -> 2x2 = 4 worlds; wildcards noted separately.")
if __name__=="__main__": main()
