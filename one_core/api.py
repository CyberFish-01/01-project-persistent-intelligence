from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable, Optional, Tuple
from urllib.parse import urlparse

from .dream import DreamEngine
from .state import DEFAULT_STATE_DIR, StateStore

PROTOCOL_VERSION = "0.2"


def state_summary(store: StateStore) -> dict:
    state = store.load()
    return {
        "agent_id": state["agent_id"],
        "updated_at": state["updated_at"],
        "identity": state["identity_core"]["self_model"]["summary"],
        "active_intent": state["working_state"]["active_intent"],
        "anchors": state["working_state"]["context_anchors"],
        "imported_memories": len(state["memory_stores"].get("imported_memory", [])),
        "episodes": len(state["memory_stores"]["episodic_memory"]),
        "semantic_memories": len(state["memory_stores"]["semantic_memory"]),
        "open_conflicts": len(state.get("open_conflicts", [])),
        "pending_dream_jobs": len(
            [job for job in state.get("dream_queue", []) if job.get("status") == "pending"]
        ),
    }


def build_local_reply(package: dict) -> str:
    active_goal = package["active_intent"]["goal"]
    anchors = package["continuity_anchors"]
    return (
        "01 Core 已记录这次经历。"
        f" 我是谁：{anchors['who_am_i']}"
        f" 我在哪：{anchors['where_am_i']}"
        f" 我在做什么：{active_goal}"
    )


def adapter_response(payload: dict) -> dict:
    return {
        "protocol_version": PROTOCOL_VERSION,
        "agent_id": "01",
        **payload,
    }


def normalize_interaction_body(body: dict) -> dict:
    event = body.get("event")
    if isinstance(event, dict):
        message = str(event.get("text") or event.get("message") or "").strip()
        user = event.get("user") if isinstance(event.get("user"), dict) else {}
        source = event.get("source") if isinstance(event.get("source"), dict) else {}
        metadata = event.get("metadata") if isinstance(event.get("metadata"), dict) else {}
        return {
            "message": message,
            "user_id": str(event.get("user_id") or user.get("id") or body.get("user_id") or "api_user"),
            "channel": str(event.get("channel") or source.get("channel") or body.get("channel") or "api"),
            "session_id": event.get("session_id") or source.get("session_id") or body.get("session_id"),
            "event_id": event.get("event_id") or body.get("event_id"),
            "event_type": str(event.get("event_type") or body.get("event_type") or "message"),
            "adapter_id": str(body.get("adapter_id") or source.get("adapter_id") or event.get("adapter_id") or ""),
            "metadata": metadata,
            "salience_hint": event.get("salience_hint", body.get("salience_hint")),
            "dry_run": bool(body.get("dry_run") or event.get("dry_run")),
        }

    return {
        "message": str(body.get("message", "")).strip(),
        "user_id": str(body.get("user_id") or "api_user"),
        "channel": str(body.get("channel") or "api"),
        "session_id": body.get("session_id"),
        "event_id": body.get("event_id"),
        "event_type": str(body.get("event_type") or "message"),
        "adapter_id": str(body.get("adapter_id") or ""),
        "metadata": body.get("metadata") if isinstance(body.get("metadata"), dict) else {},
        "salience_hint": body.get("salience_hint"),
        "dry_run": bool(body.get("dry_run")),
    }


class OneCoreAPI:
    def __init__(self, store: StateStore):
        self.store = store

    def handle_get(self, path: str) -> Tuple[int, dict]:
        if path == "/health":
            return HTTPStatus.OK, adapter_response({"status": "ok"})
        if path == "/v1/status":
            summary = state_summary(self.store)
            return HTTPStatus.OK, adapter_response({"state": summary, **summary})
        if path == "/v1/context":
            package = self.store.build_context_package()
            return HTTPStatus.OK, adapter_response(
                {"state_transfer_package": package, **package}
            )
        return HTTPStatus.NOT_FOUND, {"error": "not_found", "path": path}

    def handle_post(self, path: str, body: dict) -> Tuple[int, dict]:
        if path in {"/v1/interact", "/v1/adapter/ingest"}:
            normalized = normalize_interaction_body(body)
            message = normalized["message"]
            if not message:
                return HTTPStatus.BAD_REQUEST, {
                    "error": "missing_message",
                    "message": f"POST {path} requires a non-empty message.",
                }
            if normalized["dry_run"]:
                episode = self.store.preview_episode(**without_dry_run(normalized))
                package = self.store.build_context_package()
                return HTTPStatus.OK, adapter_response(
                    {
                        "status": "preview",
                        "dry_run": True,
                        "would_record_episode": episode,
                        "state_transfer_package": package,
                    }
                )

            episode = self.store.record_episode(**without_dry_run(normalized))
            package = self.store.build_context_package()
            return HTTPStatus.OK, adapter_response(
                {
                    "status": "recorded",
                    "dry_run": False,
                    "episode_id": episode["id"],
                    "episode": episode,
                    "summary": episode["summary"],
                    "tags": episode["tags"],
                    "salience": episode["salience"],
                    "reply": build_local_reply(package),
                    "anchors": package["continuity_anchors"],
                    "state_transfer_package": package,
                }
            )

        if path == "/v1/dream":
            limit = int(body.get("limit") or 20)
            dream = DreamEngine(self.store).run(limit=limit)
            return HTTPStatus.OK, adapter_response(
                {"status": "dream_completed", "dream": dream, **dream}
            )

        return HTTPStatus.NOT_FOUND, {"error": "not_found", "path": path}


def make_handler(api: OneCoreAPI) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        server_version = "OneCoreHTTP/0.1"

        def do_GET(self) -> None:
            status, response = api.handle_get(urlparse(self.path).path)
            self.write_json(status, response)

        def do_POST(self) -> None:
            body = self.read_json_body()
            if body is None:
                self.write_json(
                    HTTPStatus.BAD_REQUEST,
                    {"error": "invalid_json", "message": "Request body must be JSON."},
                )
                return
            status, response = api.handle_post(urlparse(self.path).path, body)
            self.write_json(status, response)

        def log_message(self, format: str, *args: object) -> None:
            return

        def read_json_body(self) -> Optional[dict]:
            length = int(self.headers.get("Content-Length") or "0")
            if length == 0:
                return {}
            raw = self.rfile.read(length)
            try:
                data = json.loads(raw.decode("utf-8"))
            except json.JSONDecodeError:
                return None
            if not isinstance(data, dict):
                return None
            return data

        def write_json(self, status: int, payload: dict) -> None:
            raw = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
            self.send_response(int(status))
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(raw)))
            self.end_headers()
            self.wfile.write(raw)

    return Handler


def create_server(
    host: str = "127.0.0.1",
    port: int = 8765,
    state_dir: Path = DEFAULT_STATE_DIR,
) -> ThreadingHTTPServer:
    store = StateStore(Path(state_dir))
    store.init()
    api = OneCoreAPI(store)
    return ThreadingHTTPServer((host, port), make_handler(api))


def without_dry_run(payload: dict) -> dict:
    return {key: value for key, value in payload.items() if key != "dry_run"}


def run_server(host: str = "127.0.0.1", port: int = 8765, state_dir: Path = DEFAULT_STATE_DIR) -> None:
    server = create_server(host=host, port=port, state_dir=state_dir)
    print(f"01 Core API listening on http://{host}:{server.server_port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
