from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import List, Optional

from .state import (
    StateStore,
    default_lifecycle,
    infer_tags,
    new_id,
    score_salience,
    summarize_message,
    utc_now,
)


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
    import_batch_id = new_id("import_batch")
    existing_keys = existing_import_dedupe_keys(state)
    batch_keys: set[str] = set()
    filter_report = {
        "duplicate_items": [],
        "sensitive_items": [],
    }

    state["memory_stores"].setdefault("imported_memory", [])
    for index, chunk in enumerate(chunks, start=1):
        dedupe_key = import_dedupe_key(chunk)
        content_hash = hash_import_content(chunk)
        if is_sensitive_import_chunk(chunk):
            filter_report["sensitive_items"].append(
                filtered_item(
                    source_index=index,
                    reason="sensitive_content",
                )
            )
            continue
        if dedupe_key in existing_keys or dedupe_key in batch_keys:
            filter_report["duplicate_items"].append(
                filtered_item(
                    source_index=index,
                    reason="duplicate_content",
                    content_hash=content_hash,
                )
            )
            continue

        tags = infer_tags(chunk)
        memory = {
            "id": new_id("import"),
            "import_batch_id": import_batch_id,
            "timestamp": now,
            "source_system": source_system,
            "source_label": source_label,
            "source_path": str(path),
            "source_index": index,
            "content_hash": content_hash,
            "dedupe_key": dedupe_key,
            "content": chunk,
            "summary": summarize_message(chunk),
            "tags": tags,
            "salience": score_salience(chunk, tags),
            "confidence": confidence,
            "status": "staged",
            "lifecycle": default_lifecycle(
                status="staged",
                timestamp=now,
                review_status="staged",
            ),
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
            "update_history": [
                {
                    "timestamp": now,
                    "actor": "memory_importer",
                    "operation": "stage_external_memory",
                    "evidence": [str(path)],
                }
            ],
        }
        imported.append(memory)
        state["memory_stores"]["imported_memory"].append(memory)
        batch_keys.add(dedupe_key)

    duplicate_count = len(filter_report["duplicate_items"])
    sensitive_count = len(filter_report["sensitive_items"])
    import_report = {
        "id": new_id("import_report"),
        "import_batch_id": import_batch_id,
        "timestamp": now,
        "source_system": source_system,
        "source_label": source_label,
        "source_path": str(path),
        "candidate_count": len(chunks),
        "imported_count": len(imported),
        "skipped_count": duplicate_count + sensitive_count,
        "duplicate_count": duplicate_count,
        "sensitive_count": sensitive_count,
        "filter_report": filter_report,
        "memory_ids": [memory["id"] for memory in imported],
        "policy": "Imported memories are staged as external material and do not update Identity Core.",
    }
    store.append_jsonl(store.imports_path, import_report)
    if imported:
        state["dream_queue"].append(
            {
                "id": new_id("dream_job"),
                "trigger": "external_memory_import",
                "import_batch_id": import_batch_id,
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
            "metadata": {
                "import_batch_id": import_batch_id,
                "candidate_count": len(chunks),
                "imported_count": len(imported),
                "skipped_count": import_report["skipped_count"],
                "duplicate_count": duplicate_count,
                "sensitive_count": sensitive_count,
            },
        }
    )
    audit_event = store.record_audit_event(
        actor="memory_importer",
        action="import_text",
        target="memory_stores.imported_memory",
        outcome="staged",
        evidence=[str(path)],
        metadata={
            "import_batch_id": import_batch_id,
            "source_system": source_system,
            "source_label": source_label,
            "candidate_count": len(chunks),
            "imported_count": len(imported),
            "skipped_count": import_report["skipped_count"],
            "duplicate_count": duplicate_count,
            "sensitive_count": sensitive_count,
            "may_update_identity_core": False,
        },
        state=state,
    )
    store.record_trace(
        workflow="memory_import",
        nodes=[
            {
                "id": "read_source",
                "type": "Input",
                "source_path": str(path),
                "source_system": source_system,
            },
            {
                "id": "stage_imports",
                "type": "Memory",
                "operation": "append_imported_memory",
                "count": len(imported),
            },
            {
                "id": "filter",
                "type": "Decision",
                "operation": "filter_duplicates_and_sensitive_content",
                "skipped_count": import_report["skipped_count"],
            },
            {
                "id": "queue_dream",
                "type": "Decision",
                "operation": "review_imported_memory",
                "queued": bool(imported),
            },
        ],
        edges=[
            {"from": "read_source", "to": "filter", "type": "data_flow"},
            {"from": "filter", "to": "stage_imports", "type": "memory_write"},
            {"from": "stage_imports", "to": "queue_dream", "type": "dream_transform"},
        ],
        memory_events=[
            {
                "operation": "stage_external_memory",
                "target": "imported_memory",
                "memory_ids": import_report["memory_ids"],
                "import_batch_id": import_batch_id,
            }
        ],
        review_events=[
            {
                "operation": "import_filtering",
                "candidate_count": len(chunks),
                "imported_count": len(imported),
                "duplicate_count": duplicate_count,
                "sensitive_count": sensitive_count,
            },
            {
                "operation": "identity_update_blocked_by_default",
                "may_update_identity_core": False,
            }
        ],
        summary="Imported external memories into staged imported_memory without identity update.",
        audit_event_ids=[audit_event["id"]],
    )
    store.save(state)
    return import_report


def existing_import_dedupe_keys(state: dict) -> set[str]:
    keys = set()
    for memory in state.get("memory_stores", {}).get("imported_memory", []):
        if not isinstance(memory, dict):
            continue
        dedupe_key = memory.get("dedupe_key")
        if dedupe_key:
            keys.add(str(dedupe_key))
            continue
        content = memory.get("content")
        if content:
            keys.add(import_dedupe_key(str(content)))
    return keys


def import_dedupe_key(text: str) -> str:
    return f"sha256:{hash_import_content(text)}"


def hash_import_content(text: str) -> str:
    normalized = normalize_import_content(text).casefold()
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def normalize_import_content(text: str) -> str:
    return re.sub(r"\s+", " ", strip_bullet(str(text))).strip()


def is_sensitive_import_chunk(text: str) -> bool:
    lowered = str(text).casefold()
    compact = re.sub(r"\s+", "", lowered)
    sensitive_patterns = [
        r"\bpassword\b",
        r"\bpasswd\b",
        r"\btoken\b",
        r"\bapi\s*key\b",
        r"\bapi_key\b",
        r"\bsecret\b",
        r"\bbearer\b",
        r"\bprivate\s*key\b",
    ]
    if any(re.search(pattern, lowered) for pattern in sensitive_patterns):
        return True
    sensitive_terms = [
        "密码",
        "root密码",
        "root密碼",
        "口令",
        "密钥",
        "密鑰",
        "令牌",
        "私钥",
        "私鑰",
    ]
    return any(term in compact for term in sensitive_terms)


def filtered_item(
    source_index: int,
    reason: str,
    content_hash: Optional[str] = None,
    existing_memory_id: Optional[str] = None,
) -> dict:
    item = {
        "source_index": source_index,
        "reason": reason,
    }
    if content_hash:
        item["content_hash"] = content_hash
    if existing_memory_id:
        item["existing_memory_id"] = existing_memory_id
    return item


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
