#!/usr/bin/env python3
"""constrain.py — offline helper for constraint-driven-ideation."""
import argparse, json
CONSTRAINTS = ["no interface","no budget","one day / one hour","offline-only","solo-only","peer-only","10x cheaper","most constrained user first","no new code"]
def main():
    p = argparse.ArgumentParser(description="Constraint picker (offline)")
    p.add_argument("--problem", type=str, default="")
    p.add_argument("--pick", type=str, default="")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        for c in CONSTRAINTS: print(c)
        return
    chosen = [c.strip() for c in args.pick.split(",") if c.strip()] if args.pick else CONSTRAINTS[:3]
    if args.json:
        print(json.dumps({"problem": args.problem or "(no problem)", "constraints": chosen, "next": "generate 3-5 concepts per constraint, then extract transferable mechanism"}, indent=2, ensure_ascii=False))
    else:
        print(f"Problem: {args.problem or '(no problem)'}")
        print("Constraints:")
        for c in chosen: print(f"  - {c}")
if __name__ == "__main__": main()
