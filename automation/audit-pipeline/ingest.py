"""Normalize client conversation exports into conversations.jsonl.

Accepts:
  - JSONL: one conversation per line, with a messages[] list (field names
    `role`/`content` detected with common fallbacks)
  - CSV: columns conversation_id, role, content (rows in chronological order)
"""

from __future__ import annotations

import argparse
import csv
import json
from collections import defaultdict
from pathlib import Path

ROLE_KEYS = ("role", "author", "sender", "from")
CONTENT_KEYS = ("content", "text", "body", "message")


def _norm_message(m: dict) -> dict | None:
    role = next((str(m[k]).lower() for k in ROLE_KEYS if m.get(k)), None)
    content = next((str(m[k]) for k in CONTENT_KEYS if m.get(k)), None)
    if not role or not content:
        return None
    role = "assistant" if role in ("assistant", "bot", "agent", "ai") else "user"
    return {"role": role, "content": content.strip()}


def load_jsonl(path: Path) -> list[dict]:
    convs = []
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if not line.strip():
            continue
        obj = json.loads(line)
        msgs = obj.get("messages") or obj.get("turns") or obj.get("events") or []
        norm = [m for m in (_norm_message(x) for x in msgs if isinstance(x, dict)) if m]
        if norm:
            convs.append({"conversation_id": str(obj.get("conversation_id", obj.get("id", i))), "messages": norm})
    return convs


def load_csv(path: Path) -> list[dict]:
    grouped: dict[str, list[dict]] = defaultdict(list)
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            m = _norm_message(row)
            if m:
                grouped[str(row.get("conversation_id", "0"))].append(m)
    return [{"conversation_id": cid, "messages": msgs} for cid, msgs in grouped.items()]


def run(src: str | Path, out: str | Path) -> int:
    src = Path(src)
    convs = load_csv(src) if src.suffix.lower() == ".csv" else load_jsonl(src)
    # Drop trivial conversations: nothing to diagnose without an assistant reply.
    convs = [c for c in convs if any(m["role"] == "assistant" for m in c["messages"])]
    out = Path(out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf-8") as f:
        for c in convs:
            f.write(json.dumps(c, ensure_ascii=False) + "\n")
    print(f"normalized {len(convs)} conversations -> {out}")
    return len(convs)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("export_file")
    ap.add_argument("-o", "--out", default="data/conversations.jsonl")
    args = ap.parse_args()
    run(args.export_file, args.out)
