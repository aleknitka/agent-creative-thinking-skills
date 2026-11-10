#!/usr/bin/env python3
"""disney.py — offline helper for dreamer-realist-critic."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Disney strategy helper (offline)")
    p.add_argument("--idea", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    idea = args.idea or "(no idea)"
    if args.json:
        print(json.dumps({"idea": idea, "phases": ["dreamer","realist","critic"], "next": "run one phase at a time; no mixing"}, indent=2, ensure_ascii=False))
    else:
        print(f"Idea: {idea}")
        print("Phases: dreamer (imagine) -> realist (outline) -> critic (risks with signals) -> revise once")
if __name__=="__main__": main()
