from __future__ import annotations

import re
from pathlib import Path
from typing import List

from .state import StateStore, infer_tags, new_id, score_salience, summarize_message, utc_now


def import_text_file(
    store: StateStore,
    path: Path,
    source_label: str,
    source_system: str = "generic_text",
    confidence: float = 0.55,
) -> dict:
    text = path.read_text(encoding="utf-8")
    chunks = split_memory_text(text)
    imported = []
    state = store.load()
    now = utc_now()

    state["memory_stores"].setdefault("imported_memory", [])
    for index, chunk in enumerate(chunks, start=1):
        tags = infer_tags(chunk)
        memory = {
            "id": new_id("import"),
            "timestamp": now,
            "source_system": source_system,
            "source_label": source_label,
            "source_path": str(path),
            "source_index": index,
            "content": chunk,
            "summary": summarize_message(chunk),
            "tags": tags,
            "salience": score_salience(chunk, tags),
            "confidence": confidence,
            "status": "staged",
            "promotion_policy": {
                "default_target": "semantic_memory_candidate",
                "requires_dream_review": True,
                "may_update_identity_core": False,
            },
            "provenance": [
                {
                    "type": "external_text_import",
                    "source_system": source_system,
                    "source_label": source_label,
                }
            ],
        }
        imported.append(memory)
        state["memory_stores"]["imported_memory"].append(memory)

    import_report = {
        "id": new_id("import_report"),
        "timestamp": now,
        "source_system": source_system,
        "source_label": source_label,
        "source_path": str(path),
        "imported_count": len(imported),
        "memory_ids": [memory["id"] for memory in imported],
        "policy": "Imported memories are staged as external material and do not update Identity Core.",
    }
    store.append_jsonl(store.imports_path, import_report)
    state["dream_queue"].append(
        {
            "id": new_id("dream_job"),
            "trigger": "external_memory_import",
            "input_imports": import_report["memory_ids"],
            "requested_operations": [
                "review_imported_memory",
                "deduplicate",
                "detect_conflicts",
                "propose_semantic_candidates",
            ],
            "status": "pending",
        }
    )
    state["update_log"].append(
        {
            "id": new_id("update"),
            "timestamp": now,
            "actor": "memory_importer",
            "target_path": "memory_stores.imported_memory",
            "operation": "append",
            "before": None,
            "after": import_report["memory_ids"],
            "evidence": [str(path)],
            "gate": "low",
            "confidence": confidence,
            "rollback": {"reversible": True},
        }
    )
    store.save(state)
    return import_report


def split_memory_text(text: str) -> List[str]:
    normalized = text.replace("\r\n", "\n").replace("\r", "\n").strip()
    if not normalized:
        return []

    blocks = [block.strip() for block in re.split(r"\n\s*\n", normalized) if block.strip()]
    if len(blocks) == 1:
        lines = [line.strip() for line in normalized.splitlines() if line.strip()]
        bullet_lines = [strip_bullet(line) for line in lines if looks_like_item(line)]
        if len(bullet_lines) >= 2:
            return bullet_lines

    return [strip_bullet(block) for block in blocks]


def looks_like_item(line: str) -> bool:
    return bool(re.match(r"^(\s*[-*+]|\s*\d+[.)]|记忆\s*\d+[:：])\s+", line))


def strip_bullet(text: str) -> str:
    return re.sub(r"^(\s*[-*+]|\s*\d+[.)]|记忆\s*\d+[:：])\s+", "", text).strip()
