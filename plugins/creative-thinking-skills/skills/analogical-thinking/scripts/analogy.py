#!/usr/bin/env python3
"""
analogy.py — offline helper for the analogical-thinking skill.

Turns a short problem description into:
  * structural abstractions to try,
  * far-domain candidates scored by structural signature overlap,
  * a mapping table skeleton and breakpoint/probe checklists.

No dependencies, no network, no model calls. Suggestions are prompts, not
answers: every mapping still needs the manual checks in references/mapping.md.

Usage:
  python scripts/analogy.py --problem "new users abandon setup before building a dashboard"
  python scripts/analogy.py --problem "on-call incidents are routed by arrival order" --domains 5
  python scripts/analogy.py --problem "..." --json
  python scripts/analogy.py --list
  echo "problem text" | python scripts/analogy.py
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys

# Structural tags are relation-level cues, not industry labels.
DOMAINS = [
    {
        "name": "Emergency department triage",
        "tags": ["priority", "urgency", "uncertainty", "scarce", "queue", "risk", "allocation", "feedback"],
        "mechanisms": [
            "sort by observed acuity, not arrival order",
            "independent signals resist self-report",
            "reassess after first contact",
            "reserve capacity for the worst class",
        ],
        "ask": "How is urgency estimated before the true cost is known, and who may override the score?",
    },
    {
        "name": "Airport wayfinding",
        "tags": ["navigation", "sequence", "onboarding", "information", "handoff", "steps", "trust"],
        "mechanisms": [
            "restate destination and current position at each decision",
            "landmarks confirm progress without a full map",
            "make wrong turns recoverable",
        ],
        "ask": "Where does the user choose without knowing their current state or the remaining path?",
    },
    {
        "name": "Logistics hub and cross-docking",
        "tags": ["flow", "throughput", "queue", "handoff", "capacity", "bottleneck", "batch", "inventory"],
        "mechanisms": [
            "consolidate flows at a hub to raise frequency",
            "standardize the unit to make transfer cheap",
            "place buffers where variability is highest",
        ],
        "ask": "Where does variability accumulate, and is the buffer before or after the bottleneck?",
    },
    {
        "name": "Air-traffic control sequencing",
        "tags": ["priority", "capacity", "queue", "safety", "schedule", "uncertainty", "throughput"],
        "mechanisms": [
            "separate sequencing from execution",
            "hold short of the constraint instead of queueing everywhere",
            "degrade the schedule before degrading safety margins",
        ],
        "ask": "What is the one scarce resource, and who decides its order under uncertainty?",
    },
    {
        "name": "Immune system",
        "tags": ["detection", "uncertainty", "false-positive", "adaptive", "memory", "risk", "feedback", "scale"],
        "mechanisms": [
            "two-signal activation reduces false positives",
            "memory shortens response to repeat threats",
            "containment before elimination",
        ],
        "ask": "What is the cost of a false positive versus a false negative here?",
    },
    {
        "name": "Ecology and succession",
        "tags": ["growth", "competition", "niche", "feedback", "scale", "incentive", "retention", "diversity"],
        "mechanisms": [
            "early colonizers change the conditions for later ones",
            "redundancy stabilizes a system under shock",
            "a niche is a relation, not a location",
        ],
        "ask": "What changes the environment for the next entrant, and which redundancy is intentional?",
    },
    {
        "name": "Games: tutorials, matchmaking, respawn",
        "tags": ["onboarding", "learning", "difficulty", "motivation", "failure", "feedback", "trust", "retention"],
        "mechanisms": [
            "teach through a safe version of the real task",
            "calibrate difficulty to demonstrated skill",
            "make failure cheap and fast to retry",
        ],
        "ask": "Where can failure be made reversible so users learn without loss?",
    },
    {
        "name": "Restaurant kitchen pass",
        "tags": ["flow", "queue", "bottleneck", "coordination", "priority", "batch", "throughput", "quality"],
        "mechanisms": [
            "one caller owns the sequence",
            "plate at the pass only when the whole order is ready",
            "protect the bottleneck station from side work",
        ],
        "ask": "Who owns the sequence when several workstreams must converge?",
    },
    {
        "name": "Manufacturing: kanban and andon",
        "tags": ["flow", "inventory", "feedback", "quality", "bottleneck", "batch", "capacity", "process"],
        "mechanisms": [
            "limit work in progress to expose bottlenecks",
            "make the signal to stop the line cheap and legitimate",
            "small batches shorten feedback",
        ],
        "ask": "What is the smallest safe batch, and who can stop the line?",
    },
    {
        "name": "Insurance and escrow",
        "tags": ["risk", "trust", "incentive", "uncertainty", "contract", "verification", "allocation", "compliance"],
        "mechanisms": [
            "price risk and transfer it to the party best able to bear it",
            "hold value in escrow until verification",
            "deductibles align incentives by keeping some downside local",
        ],
        "ask": "Who bears the downside when verification fails, and does that align incentives?",
    },
    {
        "name": "Military defense in depth",
        "tags": ["risk", "security", "redundancy", "detection", "failure", "escalation", "authority", "uncertainty"],
        "mechanisms": [
            "layer independent defenses so one failure is not fatal",
            "push authority down with clear rules of engagement",
            "keep a reserve uncommitted",
        ],
        "ask": "What is contained by one layer failing, and what is the uncommitted reserve?",
    },
    {
        "name": "Scientific peer review",
        "tags": ["quality", "verification", "trust", "feedback", "uncertainty", "incentive", "review", "allocation"],
        "mechanisms": [
            "independent reviewers reduce single-point bias",
            "separate evaluation from authorship",
            "revise before commitment",
        ],
        "ask": "Who evaluates independently, and what do they not know about the author?",
    },
    {
        "name": "Market auctions and marketplaces",
        "tags": ["matching", "allocation", "incentive", "price", "trust", "scale", "competition", "uncertainty"],
        "mechanisms": [
            "the mechanism, not the price, determines who wins",
            "reputation lowers the cost of trusting strangers",
            "thick markets need liquidity, thin markets need matchmaking",
        ],
        "ask": "Is this an allocation problem in disguise, and what is the actual matching rule?",
    },
    {
        "name": "Theater rehearsal and understudy",
        "tags": ["coordination", "failure", "learning", "redundancy", "sequence", "quality", "risk", "handoff"],
        "mechanisms": [
            "rehearse the expensive moment cheaply",
            "an understudy turns a single point of failure into redundancy",
            "tech check before performance, not during",
        ],
        "ask": "What is the expensive moment, and how is it rehearsed before it counts?",
    },
    {
        "name": "Software: backpressure and circuit breakers",
        "tags": ["load", "capacity", "failure", "feedback", "queue", "scale", "timeout", "degradation"],
        "mechanisms": [
            "reject early rather than fail slowly",
            "open the circuit to let a dependency recover",
            "make retries idempotent before adding them",
        ],
        "ask": "What absorbs load, and what happens to work in flight when it stops?",
    },
    {
        "name": "Craft: jigs, dry fitting, editorial passes",
        "tags": ["quality", "sequence", "rework", "verification", "process", "learning", "cost", "batch"],
        "mechanisms": [
            "a jig makes the right action the easy one",
            "dry-fit before irreversible cuts",
            "separate structural pass from polish pass",
        ],
        "ask": "Which irreversible step is being taken before a cheap dry run?",
    },
]

# Problem cues map wording to structural tags.
LEXICON = {
    "queue": ["queue", "backlog", "waiting", "wait", "latency", "delay", "line", "arrival"],
    "priority": ["priority", "prioritize", "urgent", "severity", "triage", "order", "rank", "loud"],
    "urgency": ["deadline", "urgent", "time-critical", "incident", "emergency", "real-time"],
    "uncertainty": ["unclear", "unknown", "ambiguous", "uncertain", "guess", "incomplete", "noisy"],
    "scarce": ["scarce", "limited", "few", "budget", "headcount", "attention", "capacity"],
    "capacity": ["capacity", "throughput", "load", "scale", "volume", "traffic", "growth"],
    "bottleneck": ["bottleneck", "slow", "constrained", "congestion", "choke"],
    "handoff": ["handoff", "handover", "transfer", "between", "routing", "dispatch", "referral"],
    "flow": ["flow", "pipeline", "process", "workflow", "chain", "stage"],
    "feedback": ["feedback", "monitor", "measure", "metric", "signal", "alert", "loop"],
    "inventory": ["inventory", "stock", "buffer", "warehouse", "supply"],
    "batch": ["batch", "bulk", "group", "cluster", "wave"],
    "onboarding": ["onboarding", "setup", "signup", "activation", "new user", "first-time", "tutorial"],
    "navigation": ["navigate", "navigation", "wayfinding", "find", "discover", "path", "journey"],
    "steps": ["step", "sequence", "stage", "funnel", "checklist", "flow"],
    "information": ["information", "docs", "documentation", "guidance", "instructions", "context", "visible"],
    "learning": ["learn", "training", "skill", "practice", "teach", "expertise"],
    "motivation": ["motivation", "engage", "engagement", "abandon", "churn", "drop", "retention"],
    "retention": ["retention", "churn", "abandon", "loyalty", "repeat"],
    "difficulty": ["difficult", "hard", "complex", "confusing", "friction", "overload"],
    "failure": ["failure", "fail", "error", "outage", "downtime", "break", "crash"],
    "risk": ["risk", "danger", "harm", "compliance", "safety", "liability"],
    "trust": ["trust", "fraud", "cheat", "abuse", "authentic", "verify", "verification"],
    "incentive": ["incentive", "reward", "pay", "bonus", "game", "misalign", "agency"],
    "allocation": ["allocate", "assignment", "assign", "distribute", "share", "match", "routing"],
    "matching": ["match", "matching", "pair", "marketplace", "supply and demand"],
    "competition": ["competition", "competitor", "race", "market share"],
    "growth": ["growth", "scale up", "expand", "acquisition", "viral"],
    "diversity": ["diversity", "variety", "redundancy", "duplicate", "backup", "resilience"],
    "quality": ["quality", "defect", "review", "inspection", "accuracy", "correct"],
    "process": ["process", "procedure", "standard", "policy", "governance"],
    "coordination": ["coordination", "coordinate", "align", "team", "collaborate", "synchronize"],
    "escalation": ["escalation", "escalate", "override", "exception", "incident command"],
    "authority": ["authority", "decision", "approval", "owner", "permission"],
    "schedule": ["schedule", "forecast", "planning", "timeline", "calendar"],
    "degradation": ["degrade", "degradation", "fallback", "graceful", "reserve"],
    "timeout": ["timeout", "retry", "stuck", "hang", "deadlock"],
}

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "for", "with", "without", "from", "into",
    "to", "of", "in", "on", "at", "by", "as", "is", "are", "was", "were", "be",
    "been", "it", "its", "this", "that", "these", "those", "we", "our", "you",
    "your", "they", "their", "them", "he", "she", "his", "her", "i", "my",
    "not", "no", "so", "than", "then", "when", "where", "which", "who", "whom",
    "what", "why", "how", "all", "any", "some", "more", "most", "less", "very",
    "can", "could", "should", "would", "may", "might", "must", "do", "does",
    "did", "have", "has", "had", "up", "down", "out", "about", "over", "under",
    "again", "each", "other", "same", "such", "only", "own", "too", "also",
}

ABSTRACTION_PROMPTS = [
    "Function: what transformation happens, from what state to what state?",
    "Flow: what moves between whom — material, information, decisions, money — and where does it wait?",
    "Constraint: what is fixed (capacity, time, law, attention, reversibility), and which one binds?",
    "Feedback: what measures deviation, how fast, and what actually adjusts in response?",
    "Rewrite without industry nouns: units, relations, binding constraint, success, failure.",
    "Replace 'small' with '10x larger'. Which relations survive? Those are the exportable ones.",
]

MAPPING_CHECKLIST = [
    "Name at least two relations in the source (causes, precedes, regulates).",
    "Match each relation to a local relation; mark holds / adapt / fails.",
    "Do not map objects alone; every row needs a relation.",
    "Prefer a connected chain of relations over scattered similarities.",
    "For each source dependency, record the local value and the consequence of the difference.",
    "Name the mechanism in one sentence without using either domain's nouns.",
    "List candidate inferences you had not considered; keep them as hypotheses.",
]

BREAKPOINT_PROMPTS = [
    "Scale: does the mechanism still work at your volume, or 10x it?",
    "Failure cost: is a local error reversible, and does the source assume it is not?",
    "Information quality: does the source rely on a measurement you cannot make?",
    "Authority: can you actually enforce the routing/refusal/stop the source relies on?",
    "Incentives: who is rewarded for defeating the mechanism?",
    "Time: does the source assume minutes, days, or seasons?",
    "Uniformity: does the source assume standard units or a common vocabulary you lack?",
]

PROBE_CHECKLIST = [
    "State the principle as: when relation X holds, mechanism Y yields Z.",
    "State the boundary condition under which it should fail.",
    "Pick the smallest reversible test that distinguishes 'mechanism works' from 'placebo'.",
    "Name the metric and the comparison group before running it.",
    "Say what result would falsify the principle.",
    "Keep it a probe, not a rollout.",
]


def tokenize(text: str) -> list[str]:
    words = re.findall(r"[a-z0-9][a-z0-9'-]*", text.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]


def infer_tags(tokens: list[str], raw: str) -> dict[str, list[str]]:
    """Map each structural tag to the problem words that triggered it.

    Single words match exactly or by a shared 4+ character stem; multi-word
    cues are matched against the raw lowercased text.
    """
    words = set(tokens)
    text = raw.lower()
    hits: dict[str, list[str]] = {}
    for tag, cues in LEXICON.items():
        found = []
        for cue in cues:
            if " " in cue:
                if cue in text:
                    found.append(cue)
                continue
            if cue in words:
                found.append(cue)
                continue
            if len(cue) >= 4 and any(w.startswith(cue) or cue.startswith(w) for w in words if len(w) >= 4):
                found.append(cue)
        if found:
            hits[tag] = found
    return hits


def score_domains(tags: dict[str, list[str]], tokens: list[str]) -> list[dict]:
    """Score domains by tag overlap, with a light bonus for relational tags."""
    structural = {"feedback", "handoff", "flow", "uncertainty", "allocation", "bottleneck"}
    scored = []
    shown = set(tokens)
    for d in DOMAINS:
        overlap = sorted(set(d["tags"]) & set(tags))
        if not overlap:
            continue
        score = len(overlap) + 0.5 * len(set(overlap) & structural)
        hit_words = sorted({w for t in overlap for w in tags[t]})
        scored.append(
            {
                "domain": d["name"],
                "score": score,
                "shared_tags": overlap,
                "problem_cues": hit_words,
                "mechanisms": d["mechanisms"],
                "ask": d["ask"],
            }
        )
    scored.sort(key=lambda x: (-x["score"], x["domain"]))
    return scored


def wildcard(scored: list[dict], tokens: list[str], n: int, seed: int) -> list[dict]:
    """Pick deterministic unexpected domains from the tail or from zero-overlap entries."""
    chosen_names = {s["domain"] for s in scored[:n]}
    pool = [d for d in DOMAINS if d["name"] not in chosen_names]
    if not pool:
        return []
    digest = hashlib.sha256((" ".join(tokens) + str(seed)).encode()).digest()
    picked = []
    idx = 0
    while len(picked) < min(2, len(pool)):
        pick = pool[(digest[idx % len(digest)] + idx * 7) % len(pool)]
        if pick not in picked:
            picked.append(pick)
        idx += 1
        if idx > 100:
            break
    return [
        {"domain": d["name"], "mechanisms": d["mechanisms"], "ask": d["ask"]}
        for d in picked
    ]


def render(problem: str, tokens: list[str], tags: dict[str, list[str]], ranked: list[dict],
           surprises: list[dict], limit: int) -> str:
    out: list[str] = []
    out.append("PROBLEM")
    out.append(f"  {problem.strip()}")
    out.append("")
    out.append("STRUCTURAL CUES DETECTED (verify, do not trust)")
    if tags:
        for tag in sorted(tags):
            out.append(f"  - {tag}: {', '.join(tags[tag])}")
    else:
        out.append("  (none matched; rewrite with more concrete verbs and constraints)")
    out.append("")
    out.append("ABSTRACTION PROMPTS")
    for p in ABSTRACTION_PROMPTS:
        out.append(f"  - {p}")
    out.append("")
    out.append(f"FAR-DOMAIN CANDIDATES (top {min(limit, len(ranked))})")
    if not ranked:
        out.append("  No structural overlap found. Use the search-heuristics prompt bank manually.")
    for i, r in enumerate(ranked[:limit], 1):
        out.append(f"  {i}. {r['domain']}  [score {r['score']:.1f}; tags: {', '.join(r['shared_tags'])}]")
        for m in r["mechanisms"]:
            out.append(f"     mechanism: {m}")
        out.append(f"     ask: {r['ask']}")
    out.append("")
    out.append("UNEXPECTED / LATERAL CANDIDATES (use at least one)")
    for r in surprises:
        out.append(f"  - {r['domain']}")
        out.append(f"     ask: {r['ask']}")
    out.append("")
    out.append("MAPPING CHECKLIST")
    for c in MAPPING_CHECKLIST:
        out.append(f"  [ ] {c}")
    out.append("")
    out.append("BREAKPOINT PROMPTS")
    for c in BREAKPOINT_PROMPTS:
        out.append(f"  [ ] {c}")
    out.append("")
    out.append("PROBE CHECKLIST")
    for c in PROBE_CHECKLIST:
        out.append(f"  [ ] {c}")
    out.append("")
    out.append("Reminder: a domain match is a prompt, not a finding. Map relations and name the breakpoints.")
    return "\n".join(out)


def main() -> int:
    p = argparse.ArgumentParser(description="Analogical-thinking helper (offline, deterministic)")
    p.add_argument("--problem", "-p", help="problem description; reads stdin if omitted")
    p.add_argument("--domains", "-n", type=int, default=4, help="number of scored domains (default 4)")
    p.add_argument("--seed", type=int, default=0, help="seed for the unexpected-domain pick")
    p.add_argument("--json", action="store_true", help="emit JSON instead of text")
    p.add_argument("--list", action="store_true", help="list the domain catalog and exit")
    args = p.parse_args()

    if args.list:
        for d in DOMAINS:
            print(f"{d['name']}\n  tags: {', '.join(d['tags'])}\n  ask: {d['ask']}")
        return 0

    problem = args.problem if args.problem is not None else sys.stdin.read()
    if not problem.strip():
        p.error("no problem text; pass --problem or pipe stdin")

    tokens = tokenize(problem)
    tags = infer_tags(tokens, problem)
    ranked = score_domains(tags, tokens)
    surprises = wildcard(ranked, tokens, args.domains, args.seed)

    if args.json:
        payload = {
            "problem": problem.strip(),
            "tokens": tokens,
            "structural_cues": tags,
            "domains": ranked[: args.domains],
            "unexpected": surprises,
            "abstraction_prompts": ABSTRACTION_PROMPTS,
            "mapping_checklist": MAPPING_CHECKLIST,
            "breakpoint_prompts": BREAKPOINT_PROMPTS,
            "probe_checklist": PROBE_CHECKLIST,
        }
        print(json.dumps(payload, indent=2))
    else:
        print(render(problem, tokens, tags, ranked, surprises, args.domains))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
