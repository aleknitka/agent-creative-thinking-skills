#!/usr/bin/env python3
"""
morph.py — offline helper for the morphological-analysis skill.

Builds a morphological box from a dimension specification, enumerates the
cross-product, applies pairwise incompatibility exclusions, and samples
combinations for option coverage. No dependencies, no network.

Spec format:
  "Trigger=signup,first login,inactivity;Channel=in-app,email,call"
  Dimensions separated by ';', name and options by '=', options by ','.

Usage:
  python scripts/morph.py --dims "Trigger=signup,first login,inactivity;Channel=in-app,email,call;Timing=immediate,day 1-3,day 7;Owner=automated,support"
  python scripts/morph.py --dims "..." --forbid "email+immediate,call+immediate" --enumerate
  python scripts/morph.py --dims "..." --forbid "email+immediate" --sample 10 --seed 7
  python scripts/morph.py --dims "..." --require "Channel=call" --json
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
import sys


def fail(msg: str) -> "NoReturn":
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(2)


def parse_dims(spec: str) -> list[dict]:
    dims: list[dict] = []
    seen: set[str] = set()
    for chunk in spec.split(";"):
        chunk = chunk.strip()
        if not chunk:
            continue
        if "=" not in chunk:
            fail(f"dimension '{chunk}' needs 'Name=opt1,opt2'")
        name, raw = chunk.split("=", 1)
        name = name.strip()
        if not name:
            fail("dimension name cannot be empty")
        if name.casefold() in seen:
            fail(f"duplicate dimension '{name}'")
        seen.add(name.casefold())
        options = [o.strip() for o in raw.split(",") if o.strip()]
        if len(options) < 2:
            fail(f"dimension '{name}' needs at least two options")
        folded = [o.casefold() for o in options]
        dupes = {o for o in folded if folded.count(o) > 1}
        if dupes:
            fail(f"duplicate option(s) in '{name}': {', '.join(sorted(dupes))}")
        dims.append({"name": name, "options": options})
    if len(dims) < 2:
        fail("need at least two dimensions")
    return dims


def option_ids(dims: list[dict]) -> None:
    for di, dim in enumerate(dims, 1):
        dim["id"] = f"D{di}"
        for oi, opt in enumerate(dim["options"], 1):
            dim.setdefault("option_ids", []).append(f"D{di}.{oi}")


def find_dim(dims: list[dict], ref: str) -> int:
    ref = ref.strip()
    for di, dim in enumerate(dims):
        if dim["name"].casefold() == ref.casefold() or dim["id"].casefold() == ref.casefold():
            return di
    if ref.isdigit() and 1 <= int(ref) <= len(dims):
        return int(ref) - 1
    fail(f"unknown dimension '{ref}' (known: {', '.join(d['name'] for d in dims)})")


def resolve_option(dims: list[dict], token: str) -> tuple[int, int]:
    """Resolve an option label, 'Dim:Option', or option id 'D1.2'."""
    token = token.strip()
    if ":" in token:
        dref, oref = token.split(":", 1)
        di = find_dim(dims, dref)
        for oi, opt in enumerate(dims[di]["options"]):
            if opt.casefold() == oref.strip().casefold() or dims[di]["option_ids"][oi].casefold() == oref.strip().casefold():
                return di, oi
        fail(f"unknown option '{oref.strip()}' in dimension '{dims[di]['name']}'")
    if "." in token and token.split(".", 1)[0].casefold().startswith("d"):
        for di, dim in enumerate(dims):
            for oi, oid in enumerate(dim["option_ids"]):
                if oid.casefold() == token.casefold():
                    return di, oi
    matches = [
        (di, oi)
        for di, dim in enumerate(dims)
        for oi, opt in enumerate(dim["options"])
        if opt.casefold() == token.casefold()
    ]
    if not matches:
        fail(f"unknown option '{token}'")
    if len(matches) > 1:
        where = ", ".join(f"{dims[di]['name']}.{dims[di]['options'][oi]}" for di, oi in matches)
        fail(f"option '{token}' is ambiguous ({where}); qualify as 'Dimension:option'")
    return matches[0]


def parse_forbid(dims: list[dict], specs: list[str]) -> list[tuple[int, int, int, int]]:
    pairs = []
    seen = set()
    for spec in specs:
        for chunk in spec.split(","):
            chunk = chunk.strip()
            if not chunk:
                continue
            parts = [p.strip() for p in chunk.split("+")]
            if len(parts) != 2:
                fail(f"forbidden pair '{chunk}' must be 'optionA+optionB'")
            di, oi = resolve_option(dims, parts[0])
            dj, oj = resolve_option(dims, parts[1])
            if di == dj:
                fail(f"forbidden pair '{chunk}' is inside one dimension; options there are already exclusive")
            key = frozenset({(di, oi), (dj, oj)})
            if key in seen:
                continue
            seen.add(key)
            pairs.append((di, oi, dj, oj))
    return pairs


def parse_require(dims: list[dict], specs: list[str]) -> dict[int, int]:
    req: dict[int, int] = {}
    for spec in specs:
        if "=" not in spec:
            fail(f"require spec '{spec}' must be 'Dimension=option'")
        dref, oref = spec.split("=", 1)
        di = find_dim(dims, dref)
        oi = resolve_option(dims, f"{dims[di]['name']}:{oref.strip()}")[1]
        if di in req and req[di] != oi:
            fail(f"conflicting require for dimension '{dims[di]['name']}'")
        req[di] = oi
    return req


def filtered(dims: list[dict], forbid, require) -> list[tuple[int, ...]]:
    allowed = [[oi for oi in range(len(d["options"])) if di not in require or require[di] == oi] for di, d in enumerate(dims)]
    combos = []
    for combo in itertools.product(*allowed):
        bad = False
        for di, oi, dj, oj in forbid:
            if combo[di] == oi and combo[dj] == oj:
                bad = True
                break
        if not bad:
            combos.append(combo)
    return combos


def combo_label(dims: list[dict], combo: tuple[int, ...]) -> str:
    return " | ".join(f"{d['name']}={d['options'][oi]}" for d, oi in zip(dims, combo))


def combo_id(dims: list[dict], combo: tuple[int, ...]) -> str:
    return " x ".join(d["option_ids"][oi] for d, oi in zip(dims, combo))


def coverage(dims: list[dict], combos: list[tuple[int, ...]]) -> dict:
    per_dim = []
    absent = []
    for di, dim in enumerate(dims):
        counts = [0] * len(dim["options"])
        for combo in combos:
            counts[combo[di]] += 1
        for oi, count in enumerate(counts):
            if count == 0:
                absent.append(f"{dim['option_ids'][oi]} {dim['options'][oi]}")
        per_dim.append({
            "dimension": dim["name"],
            "options": [
                {"id": dim["option_ids"][oi], "option": opt, "count": counts[oi]}
                for oi, opt in enumerate(dim["options"])
            ],
        })
    return {"per_dimension": per_dim, "absent_options": absent}


def sample_combos(dims: list[dict], combos: list[tuple[int, ...]], n: int, seed: int) -> list[tuple[int, ...]]:
    """Coverage-first sample: baseline, then greedily maximize new (dim,option) pairs."""
    rng = random.Random(seed)
    if n >= len(combos):
        return list(combos)
    remaining = list(combos)
    rng.shuffle(remaining)
    chosen: list[tuple[int, ...]] = []

    baseline = tuple(0 for _ in dims)
    if baseline in remaining:
        chosen.append(baseline)
        remaining.remove(baseline)

    def features(combo):
        return {(di, oi) for di, oi in enumerate(combo)}

    covered: set[tuple[int, int]] = set()
    for combo in chosen:
        covered |= features(combo)

    while remaining and len(chosen) < n:
        best = max(remaining, key=lambda c: len(features(c) - covered))
        gained = features(best) - covered
        if not gained and chosen:
            break
        chosen.append(best)
        remaining.remove(best)
        covered |= gained

    # Fill any remaining slots with unsampled combinations (random, deterministic seed).
    while remaining and len(chosen) < n:
        pick = remaining.pop()
        chosen.append(pick)

    order = {c: i for i, c in enumerate(combos)}
    return sorted(chosen, key=lambda c: order[c])


def print_matrix(dims: list[dict]) -> None:
    print("| " + " | ".join(f"{d['id']} {d['name']}" for d in dims) + " |")
    print("|" + "|".join("---" for _ in dims) + "|")
    height = max(len(d["options"]) for d in dims)
    for row in range(height):
        cells = []
        for dim in dims:
            if row < len(dim["options"]):
                cells.append(f"{dim['option_ids'][row]} {dim['options'][row]}")
            else:
                cells.append("")
        print("| " + " | ".join(cells) + " |")


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Build a morphological box, enumerate combinations, prune pairwise incompatible pairs, and sample for coverage.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    ap.add_argument("--dims", required=True, help="dimension spec: 'Name=opt1,opt2;Name2=opt1,opt2'")
    ap.add_argument("--forbid", action="append", default=[], help="pairwise exclusions, e.g. 'email+immediate,call+immediate' (repeatable)")
    ap.add_argument("--require", action="append", default=[], help="restrict a dimension, e.g. 'Channel=call' (repeatable)")
    ap.add_argument("--enumerate", action="store_true", help="list all surviving combinations")
    ap.add_argument("--sample", type=int, metavar="N", help="coverage-first sample of N combinations")
    ap.add_argument("--max", type=int, help="cap the number of listed combinations")
    ap.add_argument("--seed", type=int, default=0, help="tie-break seed for sampling (default 0)")
    ap.add_argument("--json", action="store_true", help="emit JSON instead of text")
    args = ap.parse_args()

    dims = parse_dims(args.dims)
    option_ids(dims)
    forbid = parse_forbid(dims, args.forbid)
    require = parse_require(dims, args.require)

    raw = 1
    for d in dims:
        raw *= len(d["options"])
    survivors = filtered(dims, forbid, require)
    if not survivors:
        fail("all combinations were pruned; loosen --forbid/--require")

    cov = coverage(dims, survivors)
    removed = raw - len(survivors)

    forbid_report = []
    for di, oi, dj, oj in forbid:
        # Raw combinations containing both options, ignoring other filters.
        containing = raw // (len(dims[di]["options"]) * len(dims[dj]["options"]))
        forbid_report.append({
            "pair": f"{dims[di]['name']}:{dims[di]['options'][oi]} + {dims[dj]['name']}:{dims[dj]['options'][oj]}",
            "raw_combinations_containing_pair": containing,
        })

    listed = None
    mode = None
    if args.sample is not None:
        if args.sample < 1:
            fail("--sample must be at least 1")
        listed = sample_combos(dims, survivors, args.sample, args.seed)
        mode = "sample"
    elif args.enumerate:
        listed = survivors[: args.max] if args.max else survivors
        mode = "enumerate"
    if listed is not None and args.max and mode == "sample":
        listed = listed[: args.max]

    if args.json:
        out = {
            "dimensions": [
                {
                    "id": d["id"],
                    "name": d["name"],
                    "options": [{"id": oid, "option": opt} for oid, opt in zip(d["option_ids"], d["options"])],
                }
                for d in dims
            ],
            "raw_combinations": raw,
            "survivors": len(survivors),
            "removed": removed,
            "forbidden_pairs": forbid_report,
            "coverage": cov,
            "combinations": (
                [
                    {"id": f"C{i + 1}", "options": list(combo), "label": combo_label(dims, combo)}
                    for i, combo in enumerate(listed)
                ]
                if listed is not None
                else None
            ),
            "mode": mode,
        }
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return 0

    print_matrix(dims)
    print()
    print(f"Raw combinations: {raw}")
    for entry in forbid_report:
        print(f"Forbidden: {entry['pair']} (in {entry['raw_combinations_containing_pair']} raw combinations)")
    print(f"Survivors: {len(survivors)} (removed {removed})")
    if cov["absent_options"]:
        print("Options absent from survivors: " + ", ".join(cov["absent_options"]))

    if listed is not None:
        print()
        print(f"{mode.capitalize()} ({len(listed)} of {len(survivors)}):")
        index_of = {combo: i for i, combo in enumerate(survivors)}
        for combo in listed:
            cid = f"C{index_of[combo] + 1}"
            print(f"{cid}: {combo_label(dims, combo)}  [{combo_id(dims, combo)}]")
        if mode == "enumerate" and args.max and len(survivors) > args.max:
            print(f"... {len(survivors) - args.max} more (raise --max or use --sample)")

    print()
    for entry in cov["per_dimension"]:
        counts = ", ".join(f"{o['option']} {o['count']}x" for o in entry["options"])
        print(f"Coverage {entry['dimension']}: {counts}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
