from __future__ import annotations

import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable, List, Sequence


TEXT_KEYS = {
    "content",
    "memory",
    "text",
    "message",
    "summary",
    "description",
    "value",
    "fact",
    "memo",
    "note",
    "answer",
    "response",
    "raw",
}

NOISE_KEYS = {
    "id",
    "_id",
    "uuid",
    "created_at",
    "updated_at",
    "timestamp",
    "time",
    "date",
    "score",
    "embedding",
    "vector",
    "metadata",
    "source",
    "role",
    "user_id",
    "session_id",
}

NOISE_PATTERNS = [
    r"^\s*$",
    r"^\s*(system|assistant|user)\s*[:：]\s*$",
    r"^\s*\{.*\}\s*$",
    r"^\s*\[.*\]\s*$",
    r"^\s*https?://\S+\s*$",
]


def clean_memory_files(paths: Sequence[Path], min_chars: int = 8) -> List[str]:
    candidates: List[str] = []
    for path in paths:
        candidates.extend(extract_candidates(path))
    return dedupe_preserve_order(
        normalize_candidate(candidate)
        for candidate in candidates
        if is_useful_candidate(candidate, min_chars=min_chars)
    )


def extract_candidates(path: Path) -> List[str]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        return extract_json(path)
    if suffix == ".jsonl":
        return extract_jsonl(path)
    if suffix == ".csv":
        return extract_csv(path)
    return extract_text(path)


def extract_text(path: Path) -> List[str]:
    text = path.read_text(encoding="utf-8")
    blocks = [block.strip() for block in re.split(r"\n\s*\n", text) if block.strip()]
    if len(blocks) > 1:
        return blocks
    lines = [strip_item_prefix(line) for line in text.splitlines()]
    return [line for line in lines if line.strip()]


def extract_json(path: Path) -> List[str]:
    data = json.loads(path.read_text(encoding="utf-8"))
    return list(walk_json(data))


def extract_jsonl(path: Path) -> List[str]:
    candidates = []
    with path.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                candidates.extend(walk_json(json.loads(line)))
            except json.JSONDecodeError:
                candidates.append(line)
    return candidates


def extract_csv(path: Path) -> List[str]:
    candidates = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames:
            for row in reader:
                candidates.extend(extract_row(row))
            return candidates

    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            candidates.extend(cell for cell in row if cell)
    return candidates


def walk_json(value: Any, key: str = "") -> Iterable[str]:
    if isinstance(value, dict):
        for child_key, child_value in value.items():
            normalized_key = child_key.lower()
            if normalized_key in NOISE_KEYS:
                continue
            if normalized_key in TEXT_KEYS and isinstance(child_value, str):
                yield child_value
            else:
                yield from walk_json(child_value, normalized_key)
    elif isinstance(value, list):
        for item in value:
            yield from walk_json(item, key)
    elif isinstance(value, str):
        if key.lower() in TEXT_KEYS or looks_like_memory_text(value):
            yield value


def extract_row(row: dict) -> List[str]:
    values = []
    preferred = [
        value
        for key, value in row.items()
        if key and key.lower() in TEXT_KEYS and value
    ]
    if preferred:
        return preferred
    for key, value in row.items():
        if not key or key.lower() not in NOISE_KEYS:
            if value:
                values.append(value)
    return values


def looks_like_memory_text(value: str) -> bool:
    text = value.strip()
    if len(text) < 12:
        return False
    if re.search(r"[\u4e00-\u9fff]", text):
        return True
    return len(text.split()) >= 5


def is_useful_candidate(candidate: str, min_chars: int = 8) -> bool:
    text = normalize_candidate(candidate)
    if len(text) < min_chars:
        return False
    if any(re.match(pattern, text) for pattern in NOISE_PATTERNS):
        return False
    if text.lower() in {"null", "none", "true", "false"}:
        return False
    return True


def normalize_candidate(candidate: str) -> str:
    text = strip_item_prefix(str(candidate))
    text = re.sub(r"\s+", " ", text).strip()
    text = text.strip("\"'` ")
    return text


def strip_item_prefix(text: str) -> str:
    return re.sub(r"^(\s*[-*+]|\s*\d+[.)]|记忆\s*\d+[:：])\s+", "", text).strip()


def dedupe_preserve_order(candidates: Iterable[str]) -> List[str]:
    seen = set()
    result = []
    for candidate in candidates:
        key = candidate.casefold()
        if key in seen:
            continue
        seen.add(key)
        result.append(candidate)
    return result


def write_cleaned_text(memories: Sequence[str], output_path: Path) -> dict:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as handle:
        for memory in memories:
            handle.write(f"- {memory}\n")
    return {
        "output_path": str(output_path),
        "memory_count": len(memories),
    }
