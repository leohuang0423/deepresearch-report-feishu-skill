"""Diagnose conversations against the 12-mode failure taxonomy (taxonomy.md)
and aggregate into a ranked failure map.

Requires ANTHROPIC_API_KEY.
"""

from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from typing import Literal

import anthropic
from pydantic import BaseModel, Field

MODEL = "claude-opus-4-8"
BATCH_SIZE = 8  # conversations per call; keep small so evidence quotes stay precise

FailureMode = Literal[
    "hallucination", "lost_context", "wrong_tool_call", "retrieval_miss",
    "instruction_violation", "dead_end_loop", "premature_handoff", "missed_handoff",
    "format_failure", "over_refusal", "verbosity_mismatch", "language_tone",
]


class Failure(BaseModel):
    conversation_id: str
    mode: FailureMode
    severity: Literal["S1", "S2", "S3"] = Field(
        description="S1 revenue-level (churn/false promise/compliance), S2 trust-level (visible frustration), S3 experience-level"
    )
    evidence: str = Field(description="Short verbatim quote(s) from the conversation proving the failure")
    explanation: str = Field(description="One sentence: why this is a failure and what likely causes it")


class BatchResult(BaseModel):
    failures: list[Failure]
    clean_conversation_ids: list[str] = Field(description="IDs in this batch with no failures")


SYSTEM = """You are an expert AI-agent quality auditor. Diagnose each conversation \
against the failure taxonomy. Be precise and conservative: only report failures you \
can support with a verbatim quote. A conversation can have multiple failures or none. \
Judge the ASSISTANT's behavior, not the user's. Severity: S1 = churn risk, false \
commitments, or compliance exposure; S2 = visible user frustration or retries; \
S3 = noticeable but self-recovered."""


def _render(conv: dict, max_chars: int = 6000) -> str:
    lines = [f"=== conversation {conv['conversation_id']} ==="]
    for m in conv["messages"]:
        lines.append(f"{m['role'].upper()}: {m['content']}")
    text = "\n".join(lines)
    return text[:max_chars] + ("\n[truncated]" if len(text) > max_chars else "")


def diagnose(convs: list[dict], client: anthropic.Anthropic) -> tuple[list[Failure], int]:
    failures: list[Failure] = []
    clean = 0
    for i in range(0, len(convs), BATCH_SIZE):
        batch = convs[i : i + BATCH_SIZE]
        corpus = "\n\n".join(_render(c) for c in batch)
        response = client.messages.parse(
            model=MODEL,
            max_tokens=8000,
            system=SYSTEM,
            messages=[{"role": "user", "content": f"Diagnose these conversations:\n\n{corpus}"}],
            output_format=BatchResult,
        )
        if response.parsed_output:
            failures.extend(response.parsed_output.failures)
            clean += len(response.parsed_output.clean_conversation_ids)
        print(f"  batch {i // BATCH_SIZE + 1}/{-(-len(convs) // BATCH_SIZE)}: {len(failures)} failures")
    return failures, clean


def aggregate(failures: list[Failure], total: int, clean: int) -> dict:
    by_mode: dict[str, list[Failure]] = defaultdict(list)
    for f in failures:
        by_mode[f.mode].append(f)
    sev_weight = {"S1": 3, "S2": 2, "S3": 1}
    modes = []
    for mode, items in by_mode.items():
        modes.append({
            "mode": mode,
            "count": len(items),
            "pct_of_conversations": round(100 * len({f.conversation_id for f in items}) / max(total, 1), 1),
            "severity_mix": {s: sum(1 for f in items if f.severity == s) for s in ("S1", "S2", "S3")},
            "impact_score": sum(sev_weight[f.severity] for f in items),
            "examples": [f.model_dump() for f in sorted(items, key=lambda x: x.severity)[:5]],
        })
    modes.sort(key=lambda m: m["impact_score"], reverse=True)
    return {
        "total_conversations": total,
        "clean_conversations": clean,
        "total_failures": len(failures),
        "modes": modes,
    }


def run(conversations_jsonl: str | Path, out_json: str | Path) -> dict:
    client = anthropic.Anthropic()
    convs = [json.loads(l) for l in Path(conversations_jsonl).read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"loaded {len(convs)} conversations")
    failures, clean = diagnose(convs, client)
    result = aggregate(failures, total=len(convs), clean=clean)
    out = Path(out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"{result['total_failures']} failures across {len(result['modes'])} modes -> {out}")
    return result


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("conversations_jsonl")
    ap.add_argument("-o", "--out", default="data/failures.json")
    args = ap.parse_args()
    run(args.conversations_jsonl, args.out)
