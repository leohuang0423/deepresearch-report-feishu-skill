"""Render failures.json into a client-facing report draft (markdown).

The draft contains [REVIEW] markers wherever human judgment is required —
never deliver without resolving them. Convert to PDF with e.g. pandoc.
"""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path

MODE_TITLES = {
    "hallucination": "Fabricated facts",
    "lost_context": "Lost context",
    "wrong_tool_call": "Wrong tool usage",
    "retrieval_miss": "Retrieval misses",
    "instruction_violation": "Instruction violations",
    "dead_end_loop": "Dead-end loops",
    "premature_handoff": "Premature human handoff",
    "missed_handoff": "Missed human handoff",
    "format_failure": "Formatting failures",
    "over_refusal": "Over-refusals",
    "verbosity_mismatch": "Verbosity mismatch",
    "language_tone": "Language & tone mismatch",
}


def render(data: dict, client_name: str) -> str:
    total, clean = data["total_conversations"], data["clean_conversations"]
    failed = total - clean
    lines = [
        f"# AI Agent Diagnostic Report — {client_name}",
        f"\n*Prepared {date.today().isoformat()} · {total} conversations analyzed*\n",
        "## Executive summary\n",
        f"Of **{total}** conversations analyzed, **{failed}** ({100 * failed / max(total, 1):.0f}%) "
        f"contained at least one failure, totalling **{data['total_failures']}** distinct failures "
        f"across **{len(data['modes'])}** failure modes.\n",
        "[REVIEW: 2-3 sentence narrative — what story do the top modes tell about this agent?]\n",
        "## Failure modes, ranked by impact\n",
        "| # | Failure mode | Failures | % of conversations | S1 / S2 / S3 |",
        "|---|---|---|---|---|",
    ]
    for i, m in enumerate(data["modes"], 1):
        sev = m["severity_mix"]
        lines.append(
            f"| {i} | {MODE_TITLES.get(m['mode'], m['mode'])} | {m['count']} | "
            f"{m['pct_of_conversations']}% | {sev['S1']} / {sev['S2']} / {sev['S3']} |"
        )

    lines.append("\n## Findings in detail\n")
    for i, m in enumerate(data["modes"], 1):
        lines.append(f"### {i}. {MODE_TITLES.get(m['mode'], m['mode'])}\n")
        for ex in m["examples"][:3]:
            lines.append(f"> **{ex['severity']}** · conversation `{ex['conversation_id']}`")
            lines.append(f"> “{ex['evidence']}”\n>")
            lines.append(f"> {ex['explanation']}\n")
        lines.append("**Likely root cause:** [REVIEW]\n")
        lines.append("**Recommended fix:** [REVIEW]\n")

    lines += [
        "## Top 3 recommendations\n",
        "[REVIEW: pick the 3 highest-leverage fixes; each must reference findings above "
        "and include a concrete change — prompt diff, tool-definition change, or retrieval config.]\n",
        "## Methodology\n",
        f"Each of the {total} conversations was independently audited against a 12-mode failure "
        "taxonomy by an LLM-based pipeline, with every reported failure backed by a verbatim quote. "
        "All findings above were then human-verified. Severity: S1 = revenue-level (churn risk, "
        "false commitments, compliance), S2 = trust-level (visible frustration), S3 = experience-level.",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("failures_json")
    ap.add_argument("--client", required=True, help="Client display name")
    ap.add_argument("-o", "--out", default="data/report.md")
    args = ap.parse_args()
    data = json.loads(Path(args.failures_json).read_text(encoding="utf-8"))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(data, args.client), encoding="utf-8")
    print(f"report draft -> {out}  (resolve all [REVIEW] markers before delivery)")
