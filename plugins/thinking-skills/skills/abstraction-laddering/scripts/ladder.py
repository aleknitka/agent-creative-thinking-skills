#!/usr/bin/env python3
"""ladder.py — offline helper for abstraction-laddering."""
import argparse, json
def main():
    p = argparse.ArgumentParser(description="Abstraction ladder helper (offline)")
    p.add_argument("--statement", type=str, default="")
    p.add_argument("--direction", choices=["up","down","both"], default="both")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    stmt = args.statement or "(no statement)"
    prompts = {
        "up": ["Why does this matter?", "What is this in service of?", "What outcome would make this level irrelevant?"],
        "down": ["How could this happen?", "What would have to be true?", "What mechanism would produce this?"],
    }
    chosen = prompts["up"] + prompts["down"] if args.direction=="both" else prompts[args.direction]
    if args.json:
        print(json.dumps({"statement": stmt, "direction": args.direction, "prompts": chosen, "levels": ["vision","purpose","function","mechanism","action"]}, indent=2, ensure_ascii=False))
    else:
        print(f"Statement: {stmt}")
        print(f"Direction: {args.direction}")
        for q in chosen: print(f"  - {q}")
if __name__ == "__main__": main()
