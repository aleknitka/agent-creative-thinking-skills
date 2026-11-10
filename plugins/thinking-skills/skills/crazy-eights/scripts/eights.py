#!/usr/bin/env python3
"""{slug} helper — offline."""
import argparse, json
def main():
    p = argparse.ArgumentParser(description="crazy-eights helper (offline)")
    p.add_argument("--input", type=str, default="")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list", action="store_true")
    args = p.parse_args()
    if args.list:
        print("crazy-eights: helper for Crazy Eights")
        return
    if args.json:
        print(json.dumps({"input": args.input or "(no input)", "method": "crazy-eights", "next": "follow the skill process"}, indent=2, ensure_ascii=False))
    else:
        print(f"Input: {args.input or '(no input)'}")
        print("Next: follow the skill process; helper is scaffolding only.")
if __name__ == "__main__": main()
