"""X (Twitter) collector — official API v2 recent search.

Requires a paid tier bearer token (Basic tier or above) in X_BEARER_TOKEN.
Free tier has no meaningful read access; see research/raw/A1-mining-toolchain.md
for current pricing before deciding to enable this collector.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

import requests

SEARCH_URL = "https://api.x.com/2/tweets/search/recent"


def collect_x(
    query: str,
    max_results: int = 100,
    pages: int = 1,
    bearer_token: str | None = None,
) -> list[dict]:
    """Recent search (last 7 days). Query syntax: https://developer.x.com/en/docs/x-api/tweets/search/integrate/build-a-query

    Example pain-mining query:
        '("I wish there was" OR "why does no one make") (#dogtraining OR dog) -is:retweet lang:en'
    """
    token = bearer_token or os.environ.get("X_BEARER_TOKEN")
    if not token:
        raise RuntimeError("X_BEARER_TOKEN not set — skip X or configure a paid API tier")

    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "query": query,
        "max_results": min(max_results, 100),
        "tweet.fields": "public_metrics,created_at,lang,author_id",
    }
    out: list[dict] = []
    next_token = None
    for _ in range(pages):
        if next_token:
            params["next_token"] = next_token
        resp = requests.get(SEARCH_URL, headers=headers, params=params, timeout=30)
        if resp.status_code == 429:
            time.sleep(60)
            continue
        resp.raise_for_status()
        body = resp.json()
        for t in body.get("data", []):
            m = t.get("public_metrics", {})
            out.append(
                {
                    "source": "x",
                    "id": t["id"],
                    "title": "",
                    "text": t.get("text", ""),
                    "score": m.get("like_count", 0) + 2 * m.get("retweet_count", 0),
                    "num_comments": m.get("reply_count", 0),
                    "url": f"https://x.com/i/status/{t['id']}",
                    "subreddit": "",
                    "created_utc": 0,
                    "top_comments": [],
                }
            )
        next_token = body.get("meta", {}).get("next_token")
        if not next_token:
            break
    return out


def save_jsonl(rows: list[dict], out_path: str | Path) -> None:
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("-o", "--out", default="data/x_posts.jsonl")
    ap.add_argument("--pages", type=int, default=1)
    args = ap.parse_args()
    rows = collect_x(args.query, pages=args.pages)
    save_jsonl(rows, args.out)
    print(f"saved {len(rows)} tweets -> {args.out}")
