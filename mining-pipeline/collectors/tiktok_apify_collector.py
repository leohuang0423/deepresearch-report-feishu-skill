"""TikTok comments collector via Apify (hosted scraping platform).

Requires APIFY_TOKEN. Uses the 'clockworks/tiktok-comments-scraper' actor
(pay-per-result; check current pricing on apify.com). Input: TikTok video URLs —
typically the top videos for a niche hashtag, found manually or via the
'clockworks/tiktok-scraper' actor first.

Note: scraping TikTok via third parties operates in a ToS gray zone even for
public data. Keep volume modest and use for research only — see
research/raw/A1-mining-toolchain.md for the risk assessment.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

import requests

APIFY_BASE = "https://api.apify.com/v2"
COMMENTS_ACTOR = "clockworks~tiktok-comments-scraper"


def run_actor_sync(actor: str, run_input: dict, token: str, timeout_s: int = 600) -> list[dict]:
    """Start an Apify actor run and poll until it finishes, then fetch dataset items."""
    resp = requests.post(
        f"{APIFY_BASE}/acts/{actor}/runs",
        params={"token": token},
        json=run_input,
        timeout=30,
    )
    resp.raise_for_status()
    run = resp.json()["data"]
    run_id = run["id"]

    deadline = time.time() + timeout_s
    while time.time() < deadline:
        r = requests.get(f"{APIFY_BASE}/actor-runs/{run_id}", params={"token": token}, timeout=30)
        r.raise_for_status()
        status = r.json()["data"]["status"]
        if status in ("SUCCEEDED", "FAILED", "ABORTED", "TIMED-OUT"):
            if status != "SUCCEEDED":
                raise RuntimeError(f"Apify run {run_id} ended with {status}")
            break
        time.sleep(10)
    else:
        raise TimeoutError(f"Apify run {run_id} did not finish in {timeout_s}s")

    dataset_id = r.json()["data"]["defaultDatasetId"]
    items = requests.get(
        f"{APIFY_BASE}/datasets/{dataset_id}/items",
        params={"token": token, "format": "json"},
        timeout=60,
    )
    items.raise_for_status()
    return items.json()


def collect_tiktok_comments(
    video_urls: list[str], per_video: int = 100, token: str | None = None
) -> list[dict]:
    token = token or os.environ.get("APIFY_TOKEN")
    if not token:
        raise RuntimeError("APIFY_TOKEN not set — skip TikTok or create an Apify account")

    items = run_actor_sync(
        COMMENTS_ACTOR,
        {"postURLs": video_urls, "commentsPerPost": per_video},
        token,
    )
    out = []
    for it in items:
        text = it.get("text") or ""
        if len(text) < 15:  # drop emoji-only / trivial comments
            continue
        out.append(
            {
                "source": "tiktok",
                "id": str(it.get("cid", "")),
                "title": "",
                "text": text[:1500],
                "score": it.get("diggCount", 0),
                "num_comments": it.get("replyCommentTotal", 0),
                "url": it.get("videoWebUrl", ""),
                "subreddit": "",
                "created_utc": 0,
                "top_comments": [],
            }
        )
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
    ap.add_argument("video_urls", nargs="+")
    ap.add_argument("-o", "--out", default="data/tiktok_comments.jsonl")
    ap.add_argument("--per-video", type=int, default=100)
    args = ap.parse_args()
    rows = collect_tiktok_comments(args.video_urls, per_video=args.per_video)
    save_jsonl(rows, args.out)
    print(f"saved {len(rows)} comments -> {args.out}")
