#!/usr/bin/env python3
"""wheel.py — offline helper for futures-wheel."""
import argparse, json
def main():
    p=argparse.ArgumentParser(description="Futures wheel helper (offline)")
    p.add_argument("--change", type=str, default="")
    p.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.json:
        print(json.dumps({"center": args.change or "(no change)", "rings": ["first-order (5-8)", "second-order (2-3 per first)", "third-order (strongest branches)"], "next": "ring 1 then ring 2 then signals"}, indent=2, ensure_ascii=False))
    else:
        print(f"Center: {args.change or '(no change)'}")
        print("Rings: first (5-8) -> second (2-3 per) -> third (strongest) -> signals per branch")
if __name__=="__main__": main()
