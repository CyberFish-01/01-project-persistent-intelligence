from __future__ import annotations

import json
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Callable, Optional, Tuple
from urllib.parse import urlparse

from .dream import DreamEngine
from .state import DEFAULT_STATE_DIR, StateStore


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


class OneCoreAPI:
    def __init__(self, store: StateStore):
        self.store = store

    def handle_get(self, path: str) -> Tuple[int, dict]:
        if path == "/health":
            return HTTPStatus.OK, {"status": "ok", "agent_id": "01"}
        if path == "/v1/status":
            return HTTPStatus.OK, state_summary(self.store)
        if path == "/v1/context":
            return HTTPStatus.OK, self.store.build_context_package()
        return HTTPStatus.NOT_FOUND, {"error": "not_found", "path": path}

    def handle_post(self, path: str, body: dict) -> Tuple[int, dict]:
        if path == "/v1/interact":
            message = str(body.get("message", "")).strip()
            if not message:
                return HTTPStatus.BAD_REQUEST, {
                    "error": "missing_message",
                    "message": "POST /v1/interact requires a non-empty message.",
                }
            episode = self.store.record_episode(
                message,
                user_id=str(body.get("user_id") or "api_user"),
                channel=str(body.get("channel") or "api"),
                session_id=body.get("session_id"),
            )
            package = self.store.build_context_package()
            return HTTPStatus.OK, {
                "episode_id": episode["id"],
                "summary": episode["summary"],
                "tags": episode["tags"],
                "salience": episode["salience"],
                "reply": build_local_reply(package),
                "anchors": package["continuity_anchors"],
                "state_transfer_package": package,
            }

        if path == "/v1/dream":
            limit = int(body.get("limit") or 20)
            return HTTPStatus.OK, DreamEngine(self.store).run(limit=limit)

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
