#!/usr/bin/env python3
"""brainwrite.py — offline helper for brainwriting."""
import argparse, json
def main():
    p = argparse.ArgumentParser(description="Brainwriting template (offline)")
    p.add_argument("--problem", type=str, default="")
    p.add_argument("--passes", type=int, default=2)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if args.json:
        print(json.dumps({"problem": args.problem or "(no problem)", "passes": args.passes, "template": "Pass 1: 3 ideas alone; Pass 2: build on others; cluster by mechanism"}, indent=2, ensure_ascii=False))
    else:
        print(f"Problem: {args.problem or '(no problem)'}")
        print(f"Template: {args.passes} passes — write alone before speaking; build on exchange.")
if __name__ == "__main__": main()
