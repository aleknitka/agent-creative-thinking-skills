#!/usr/bin/env python3
"""diamond.py — offline helper for double-diamond."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Double diamond helper (offline)")
    p.add_argument("--problem", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"problem": args.problem or "(no problem)", "phases": ["discover","define","develop","deliver"], "next": "diverge in diamond 1, converge, diverge in diamond 2, converge"}, indent=2, ensure_ascii=False))
    else:
        print(f"Problem: {args.problem or '(no problem)'}")
        print("Phases: discover (diverge) -> define (converge) -> develop (diverge) -> deliver (converge)")
if __name__=="__main__": main()
