#!/usr/bin/env python3
"""blend.py — offline helper for concept-blending."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Concept blending helper (offline)")
    p.add_argument("--ideas", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"ideas": args.ideas or "2-4 partial ideas", "next": "extract mechanisms, then blend mechanisms not features with rationale"}, indent=2, ensure_ascii=False))
    else:
        print(f"Ideas: {args.ideas or '(no ideas listed)'}")
        print("Next: extract mechanisms, blend with rationale, test coherence.")
if __name__=="__main__": main()
