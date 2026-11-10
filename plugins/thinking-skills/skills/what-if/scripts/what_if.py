#!/usr/bin/env python3
"""what_if.py — offline helper for what-if."""
import argparse, json, random
TYPES = {
    "resource": "what if this resource were abundant or free?",
    "interface": "what if this interface disappeared?",
    "actor": "what if someone else were the actor?",
    "rule": "what if this rule were lifted or reversed?",
    "scale": "what if this were 10x or 1/10?",
    "time": "what if time order reversed or the window shifted?",
}
def main():
    p = argparse.ArgumentParser(description="What-if assumption picker (offline)")
    p.add_argument("--pick", type=str, default="random", help="type key or 'random'")
    p.add_argument("--problem", type=str, default="")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        for k, v in TYPES.items(): print(f"{k}: {v}")
        return
    key = args.pick.lower().strip()
    if key == "random" or key not in TYPES:
        key = random.choice(list(TYPES.keys()))
    prompt = TYPES[key]
    if args.json:
        print(json.dumps({"problem": args.problem or "(no problem text)", "assumption_type": key, "prompt": prompt, "template": "Assumption mutated: [type + form -> new form]; World sketch: 3-5 sentences; Kept fixed: [...]"}, indent=2, ensure_ascii=False))
    else:
        print(f"Problem: {args.problem or '(no text)'}")
        print(f"Mutate: {key} — {prompt}")
        print("World sketch: 3-5 sentences; trace 2-3 consequences; extract principle with boundary.")
if __name__ == "__main__": main()
