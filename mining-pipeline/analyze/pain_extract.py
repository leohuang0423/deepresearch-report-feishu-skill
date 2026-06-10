"""Pain-point extraction & clustering with the Claude API.

Two passes:
  1. extract — per batch of posts, pull out individual pain mentions
  2. cluster — merge all mentions into named pain-point clusters with scores

Requires ANTHROPIC_API_KEY.
"""

from __future__ import annotations

import json
from pathlib import Path

import anthropic
from pydantic import BaseModel, Field

MODEL = "claude-opus-4-8"
BATCH_SIZE = 40  # posts per extraction call


class PainMention(BaseModel):
    quote: str = Field(description="Verbatim quote (trimmed) expressing the pain")
    pain_summary: str = Field(description="One-line summary of the underlying problem")
    audience: str = Field(description="Who has this problem, as specific as possible")
    intensity: int = Field(description="1-5: how desperate/emotional the language is")
    willingness_to_pay_signal: bool = Field(
        description="True if the text implies they would pay / have paid / asked for a product"
    )
    source_url: str


class ExtractionResult(BaseModel):
    mentions: list[PainMention]


class PainCluster(BaseModel):
    name: str = Field(description="Short name for the pain point")
    problem_statement: str = Field(description="2-3 sentence description of the problem")
    audience: str
    mention_count: int = Field(description="How many distinct mentions support this cluster")
    avg_intensity: float
    wtp_mentions: int = Field(description="Mentions with willingness-to-pay signal")
    existing_solutions: str = Field(
        description="Known products/workarounds people mention, and why they fall short"
    )
    product_ideas: list[str] = Field(description="2-3 concrete offer ideas (physical or digital)")
    evidence_urls: list[str] = Field(description="Up to 5 representative source URLs")
    opportunity_score: int = Field(
        description="1-10 considering intensity, WTP signals, audience size hints, and gap vs existing solutions"
    )
    score_rationale: str


class ClusterResult(BaseModel):
    clusters: list[PainCluster]


EXTRACT_SYSTEM = """You are a product-research analyst mining social posts for \
pain points that could support a paid product. Extract only genuine, specific \
frustrations or unmet needs — ignore jokes, politics, platform meta-complaints, \
and vague venting with no underlying problem. Preserve the poster's own words in \
quotes. Be conservative with willingness_to_pay_signal: only mark it true when \
the text mentions paying, buying, searching for a product, or using an inferior \
paid workaround."""

CLUSTER_SYSTEM = """You are a product-research analyst. Merge raw pain mentions \
into distinct pain-point clusters. A cluster must represent ONE underlying \
problem for ONE identifiable audience. Discard clusters supported by a single \
weak mention. Score opportunities honestly — most clusters should score 5 or \
below; reserve 8+ for pains with strong willingness-to-pay evidence and weak \
existing solutions."""


def _post_to_snippet(p: dict) -> str:
    parts = [f"[{p['source']}] (score {p.get('score', 0)}) {p.get('url', '')}"]
    if p.get("title"):
        parts.append(f"TITLE: {p['title']}")
    if p.get("text"):
        parts.append(f"BODY: {p['text'][:1200]}")
    for c in p.get("top_comments", [])[:5]:
        parts.append(f"COMMENT: {c[:600]}")
    return "\n".join(parts)


def extract_mentions(posts: list[dict], client: anthropic.Anthropic) -> list[PainMention]:
    mentions: list[PainMention] = []
    for i in range(0, len(posts), BATCH_SIZE):
        batch = posts[i : i + BATCH_SIZE]
        corpus = "\n\n---\n\n".join(_post_to_snippet(p) for p in batch)
        response = client.messages.parse(
            model=MODEL,
            max_tokens=16000,
            system=EXTRACT_SYSTEM,
            messages=[
                {
                    "role": "user",
                    "content": f"Extract pain mentions from these posts:\n\n{corpus}",
                }
            ],
            output_format=ExtractionResult,
        )
        if response.parsed_output:
            mentions.extend(response.parsed_output.mentions)
        print(f"  batch {i // BATCH_SIZE + 1}: {len(mentions)} mentions total")
    return mentions


def cluster_mentions(mentions: list[PainMention], client: anthropic.Anthropic) -> list[PainCluster]:
    payload = json.dumps([m.model_dump() for m in mentions], ensure_ascii=False)
    with client.messages.stream(
        model=MODEL,
        max_tokens=32000,
        system=CLUSTER_SYSTEM,
        messages=[
            {
                "role": "user",
                "content": f"Cluster and score these pain mentions:\n\n{payload}",
            }
        ],
        output_config={
            "format": {
                "type": "json_schema",
                "schema": ClusterResult.model_json_schema(),
            }
        },
    ) as stream:
        final = stream.get_final_message()
    text = next(b.text for b in final.content if b.type == "text")
    return ClusterResult.model_validate_json(text).clusters


def run(posts_jsonl: str | Path, out_json: str | Path) -> list[PainCluster]:
    client = anthropic.Anthropic()
    posts = [json.loads(line) for line in Path(posts_jsonl).read_text(encoding="utf-8").splitlines() if line.strip()]
    print(f"loaded {len(posts)} posts")
    mentions = extract_mentions(posts, client)
    print(f"extracted {len(mentions)} pain mentions; clustering ...")
    clusters = cluster_mentions(mentions, client)
    clusters.sort(key=lambda c: c.opportunity_score, reverse=True)
    out = Path(out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(
        json.dumps([c.model_dump() for c in clusters], ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    print(f"saved {len(clusters)} clusters -> {out}")
    return clusters


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()
    ap.add_argument("posts_jsonl")
    ap.add_argument("-o", "--out", default="data/pain_clusters.json")
    args = ap.parse_args()
    run(args.posts_jsonl, args.out)
