"""Render ranked pain clusters into a human-readable opportunity report."""

from __future__ import annotations

import json
from datetime import date
from pathlib import Path


def render(clusters_json: str | Path, out_md: str | Path) -> None:
    clusters = json.loads(Path(clusters_json).read_text(encoding="utf-8"))
    lines = [
        f"# Pain-Point Opportunity Report — {date.today().isoformat()}",
        "",
        f"{len(clusters)} clusters, ranked by opportunity score.",
        "",
    ]
    for i, c in enumerate(clusters, 1):
        lines += [
            f"## {i}. {c['name']} — score {c['opportunity_score']}/10",
            "",
            f"**Audience:** {c['audience']}",
            f"**Evidence:** {c['mention_count']} mentions, avg intensity {c['avg_intensity']:.1f}, "
            f"{c['wtp_mentions']} with willingness-to-pay signals",
            "",
            c["problem_statement"],
            "",
            f"**Existing solutions:** {c['existing_solutions']}",
            "",
            "**Offer ideas:**",
            *[f"- {idea}" for idea in c["product_ideas"]],
            "",
            "**Sources:**",
            *[f"- {u}" for u in c["evidence_urls"]],
            "",
            f"> Rationale: {c['score_rationale']}",
            "",
        ]
    out = Path(out_md)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"report -> {out}")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("clusters_json")
    ap.add_argument("-o", "--out", default="data/opportunity_report.md")
    args = ap.parse_args()
    render(args.clusters_json, args.out)
