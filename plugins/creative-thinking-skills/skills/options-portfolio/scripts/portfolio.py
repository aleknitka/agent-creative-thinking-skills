#!/usr/bin/env python3
"""portfolio.py — offline helper for options-portfolio."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Portfolio helper (offline)")
    p.add_argument("--ideas", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"ideas": args.ideas or "broad idea set", "buckets": ["achievable","ambitious","exploratory"], "next": "score on feasibility/upside/learning, then compose one of each"}, indent=2, ensure_ascii=False))
    else:
        print(f"Ideas: {args.ideas or '(broad set)'}")
        print("Buckets: achievable, ambitious, exploratory — one probe per option.")
if __name__=="__main__": main()
