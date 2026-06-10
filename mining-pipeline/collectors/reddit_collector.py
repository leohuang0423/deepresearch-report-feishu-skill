"""Reddit collector — uses Reddit's public JSON endpoints (no API key needed
for read-only listing at low volume; respect rate limits: ~10 req/min unauthenticated).

For production volume, register a script app at https://www.reddit.com/prefs/apps
and pass OAuth credentials via REDDIT_CLIENT_ID / REDDIT_CLIENT_SECRET.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict, dataclass
from pathlib import Path

import requests

USER_AGENT = "niche-pain-miner/0.1 (product research; contact: owner)"
BASE = "https://www.reddit.com"


@dataclass
class Post:
    source: str
    id: str
    title: str
    text: str
    score: int
    num_comments: int
    url: str
    subreddit: str
    created_utc: float
    top_comments: list[str]


def _get(path: str, params: dict | None = None, retries: int = 3) -> dict:
    for attempt in range(retries):
        resp = requests.get(
            f"{BASE}{path}", params=params, headers={"User-Agent": USER_AGENT}, timeout=30
        )
        if resp.status_code == 429:
            time.sleep(10 * (attempt + 1))
            continue
        resp.raise_for_status()
        return resp.json()
    raise RuntimeError(f"rate limited after {retries} retries: {path}")


def fetch_top_comments(subreddit: str, post_id: str, limit: int = 8) -> list[str]:
    data = _get(f"/r/{subreddit}/comments/{post_id}.json", {"limit": limit, "sort": "top"})
    comments = []
    try:
        for child in data[1]["data"]["children"]:
            body = child.get("data", {}).get("body")
            if body and len(body) > 20:
                comments.append(body[:1500])
    except (IndexError, KeyError):
        pass
    return comments[:limit]


def collect_subreddit(
    subreddit: str,
    query: str | None = None,
    listing: str = "top",
    timeframe: str = "year",
    limit: int = 50,
    with_comments: bool = True,
) -> list[Post]:
    """Pull posts from a subreddit, optionally filtered by a search query."""
    if query:
        data = _get(
            f"/r/{subreddit}/search.json",
            {"q": query, "restrict_sr": 1, "sort": "relevance", "t": timeframe, "limit": limit},
        )
    else:
        data = _get(f"/r/{subreddit}/{listing}.json", {"t": timeframe, "limit": limit})

    posts: list[Post] = []
    for child in data["data"]["children"]:
        d = child["data"]
        if d.get("stickied"):
            continue
        post = Post(
            source="reddit",
            id=d["id"],
            title=d.get("title", ""),
            text=(d.get("selftext") or "")[:3000],
            score=d.get("score", 0),
            num_comments=d.get("num_comments", 0),
            url=f"https://reddit.com{d.get('permalink', '')}",
            subreddit=subreddit,
            created_utc=d.get("created_utc", 0),
            top_comments=[],
        )
        if with_comments and post.num_comments > 3:
            time.sleep(1.5)  # stay under unauthenticated rate limit
            post.top_comments = fetch_top_comments(subreddit, post.id)
        posts.append(post)
    return posts


# Search phrasings that correlate with purchase-intent pain points
PAIN_QUERIES = [
    '"I wish there was"',
    '"why does no one make"',
    '"I would pay for"',
    '"is there a product"',
    '"so frustrating"',
    '"drives me crazy"',
]


def collect_pain_signals(subreddit: str, limit_per_query: int = 25) -> list[Post]:
    """Run all pain-signal queries against one subreddit and dedupe."""
    seen: dict[str, Post] = {}
    for q in PAIN_QUERIES:
        try:
            for p in collect_subreddit(subreddit, query=q, limit=limit_per_query):
                seen[p.id] = p
        except Exception as e:  # noqa: BLE001 — one failing query shouldn't kill the run
            print(f"  [warn] query {q} on r/{subreddit} failed: {e}")
        time.sleep(2)
    return list(seen.values())


def save_jsonl(posts: list[Post], out_path: str | Path) -> None:
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for p in posts:
            f.write(json.dumps(asdict(p), ensure_ascii=False) + "\n")


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Mine pain-point posts from subreddits")
    ap.add_argument("subreddits", nargs="+", help="subreddit names, no r/ prefix")
    ap.add_argument("-o", "--out", default="data/reddit_posts.jsonl")
    ap.add_argument("--limit", type=int, default=25, help="posts per pain query")
    args = ap.parse_args()

    all_posts: list[Post] = []
    for sub in args.subreddits:
        print(f"collecting r/{sub} ...")
        all_posts.extend(collect_pain_signals(sub, limit_per_query=args.limit))
    save_jsonl(all_posts, args.out)
    print(f"saved {len(all_posts)} posts -> {args.out}")
