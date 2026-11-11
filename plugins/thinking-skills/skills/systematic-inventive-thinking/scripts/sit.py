#!/usr/bin/env python3
"""
sit.py — offline helper for Systematic Inventive Thinking (SIT).

Closed-world operator picker + virtual-product generator; no network, no deps.

Usage:
  python scripts/sit.py --list
  python scripts/sit.py --operator subtraction --subject "onboarding flow: invite, welcome email, tour, activation DB"
  python scripts/sit.py --subject "..." --json
  python scripts/sit.py --subject "..." --operator all --json
"""
from __future__ import annotations
import argparse, json, textwrap

OPERATORS = {
    "subtraction": {
        "name": "Subtraction",
        "recipe": "List components, pick one essential, remove it entirely. Keep the system otherwise unchanged.",
        "prompt": "If this component did not exist, how would the system still deliver its core benefit?",
        "check": "Is the removed component truly essential? If removal changes nothing, pick another.",
    },
    "multiplication": {
        "name": "Multiplication",
        "recipe": "Choose a component, copy it (same type, not just more), change a key attribute (time/place/performer/form). Copies must differ.",
        "prompt": "If we had two of this, differing in one meaningful way, what new value appears between them?",
        "check": "Are copies different in kind, not just quantity?",
    },
    "division": {
        "name": "Division",
        "recipe": "Split a product/process/set along a non-obvious boundary, then reorganize parts in space/time/responsibility.",
        "prompt": "If we cut along a different seam and rearranged the pieces, what hidden benefit appears?",
        "check": "Is the cut non-obvious? Cutting where everyone cuts produces the same design.",
    },
    "task-unification": {
        "name": "Task Unification",
        "recipe": "Give an existing component or nearby environmental element a new task that another component currently does — remove the other from that task.",
        "prompt": "Which existing element could do this job instead, so we no longer need the current performer?",
        "check": "Does an existing element truly perform the task, or did you just rename the old performer?",
    },
    "attribute-dependency": {
        "name": "Attribute Dependency",
        "recipe": "Pick two currently independent variables (often internal vs external). Create a dependency where one controls the other.",
        "prompt": "If X changed with Y — when Y moves, X must move — what rule would make the dependency valuable?",
        "check": "Were the variables independent before?",
    },
}

def build_payload(subject: str, keys):
    out = []
    for k in keys:
        op = OPERATORS[k]
        out.append({
            "key": k,
            "name": op["name"],
            "recipe": op["recipe"],
            "prompt": op["prompt"],
            "check": op["check"],
            "virtual_product_hint": f"Apply to: {subject or '(describe the system and its components)'}",
            "closed_world": "Do not add a new kind of resource; enrichment is the only place to add the minimal feasible fix.",
        })
    return out

def main():
    p = argparse.ArgumentParser(description="SIT closed-world operator helper (offline)")
    p.add_argument("--subject", type=str, default="", help="system + components in 3-5 sentences")
    p.add_argument("--operator", type=str, default="all", help="operator key or 'all' | 'list'")
    p.add_argument("--list", action="store_true", help="list operators and exit")
    p.add_argument("--json", action="store_true", help="emit JSON")
    args = p.parse_args()

    if args.list or args.operator == "list":
        if args.json:
            print(json.dumps([{"key": k, **v} for k, v in OPERATORS.items()], indent=2, ensure_ascii=False))
        else:
            for k, v in OPERATORS.items():
                print(f"{k} — {v['name']}: {v['recipe']}")
                print(f"  Prompt: {v['prompt']}")
                print(f"  Check: {v['check']}\n")
        return

    subject = args.subject.strip()
    key = args.operator.strip().lower()
    if key == "all":
        keys = list(OPERATORS.keys())
    elif key in OPERATORS:
        keys = [key]
    else:
        # fuzzy: allow 'subtraction' prefix
        matches = [k for k in OPERATORS if k.startswith(key)]
        keys = matches if matches else list(OPERATORS.keys())

    payload = build_payload(subject, keys)

    if args.json:
        print(json.dumps({
            "subject": subject or "(no subject — describe the closed world)",
            "operators": payload,
            "sources": ["https://www.sitsite.com/method", "https://openalex.org/W4407721440"],
            "provenance": "SIT (Horowitz/Goldenberg); C-K neighbour https://openalex.org/W2049599278"
        }, indent=2, ensure_ascii=False))
        return

    if not subject:
        print("SIT helper — describe the closed world first (system + components, 3-5 sentences).\n")
    else:
        print(f"Subject: {subject}\nClosed world: listed components and immediate environment only.\n")
    for item in payload:
        print(f"{item['key']} — {item['name']}")
        print(f"  Recipe: {item['recipe']}")
        print(f"  Prompt: {item['prompt']}")
        print(f"  Check: {item['check']}")
        print(f"  Hint: {item['virtual_product_hint']}\n")
    if len(payload) == len(OPERATORS):
        print("Next: pick one operator → virtual product → enrichment (minimal fix) → probe.")
    else:
        print("Next: generate the virtual product without feasibility filtering; enrich afterwards.")

if __name__ == "__main__":
    main()
