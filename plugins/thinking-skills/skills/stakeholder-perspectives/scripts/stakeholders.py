#!/usr/bin/env python3
"""stakeholders.py — offline helper for stakeholder-perspectives."""
import argparse, json
GROUPS = ["primary users","secondary / support","overlooked / low-power","operators / implementers","decision-makers"]
def main():
    p=argparse.ArgumentParser(description="Stakeholder helper (offline)")
    p.add_argument("--problem", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"problem": args.problem or "(no problem)", "groups": GROUPS, "next": "map needs/constraints per group, then name tensions as tradeoffs"}, indent=2, ensure_ascii=False))
    else:
        print(f"Problem: {args.problem or '(no problem)'}")
        print("Groups: " + ", ".join(GROUPS))
if __name__=="__main__": main()
