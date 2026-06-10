"""End-to-end pain-point mining pipeline.

Usage:
    python pipeline.py --subreddits dogtraining puppy101 --out-dir data/run1

Optional sources (need API keys, see README):
    --x-query '...'           requires X_BEARER_TOKEN
    --tiktok-urls url1 url2   requires APIFY_TOKEN

Requires ANTHROPIC_API_KEY for the analysis stage.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from analyze import pain_extract, report
from collectors import reddit_collector


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--subreddits", nargs="*", default=[], help="subreddits to mine")
    ap.add_argument("--x-query", default=None)
    ap.add_argument("--tiktok-urls", nargs="*", default=[])
    ap.add_argument("--out-dir", default="data/run")
    ap.add_argument("--limit", type=int, default=25, help="reddit posts per pain query")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    posts_path = out_dir / "posts.jsonl"

    rows: list[dict] = []
    for sub in args.subreddits:
        print(f"[reddit] r/{sub}")
        posts = reddit_collector.collect_pain_signals(sub, limit_per_query=args.limit)
        rows.extend(json.loads(json.dumps(p.__dict__)) for p in posts)

    if args.x_query:
        from collectors import x_collector

        print(f"[x] {args.x_query}")
        rows.extend(x_collector.collect_x(args.x_query, pages=2))

    if args.tiktok_urls:
        from collectors import tiktok_apify_collector

        print(f"[tiktok] {len(args.tiktok_urls)} videos")
        rows.extend(tiktok_apify_collector.collect_tiktok_comments(args.tiktok_urls))

    with posts_path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    print(f"collected {len(rows)} posts -> {posts_path}")

    clusters_path = out_dir / "pain_clusters.json"
    pain_extract.run(posts_path, clusters_path)
    report.render(clusters_path, out_dir / "opportunity_report.md")


if __name__ == "__main__":
    main()
