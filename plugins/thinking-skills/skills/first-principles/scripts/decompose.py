#!/usr/bin/env python3
"""decompose.py — offline helper for first-principles."""
import argparse, json, re
TYPES = ["fundamental","regulation","observed fact","inherited","preference"]
def main():
    p = argparse.ArgumentParser(description="First-principles constraint classifier (offline)")
    p.add_argument("--statement", type=str, default="")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        for t in TYPES: print(t)
        return
    stmt = args.statement or "(no statement)"
    # naive cue
    cues = {
        "fundamental": ["latency","physics","must","cannot"],
        "regulation": ["policy","regulation","compliance","legal"],
        "inherited": ["always","standard","usual","how it is done"],
    }
    hint = "inherited (unsourced until proven)"
    low = stmt.lower()
    for k, words in cues.items():
        if any(w in low for w in words):
            hint = k
            break
    if args.json:
        print(json.dumps({"statement": stmt, "suggested_type": hint, "types": TYPES, "next": "source it; mark fact/assumption/speculation; state falsification"}, indent=2, ensure_ascii=False))
    else:
        print(f"Statement: {stmt}")
        print(f"Suggested: {hint}")
        print(f"Types: {', '.join(TYPES)}")
if __name__ == "__main__": main()
