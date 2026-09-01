from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse
import json, os, random, time, uuid

STATE_PATH = Path(os.environ.get("STATE_FILE", "/data/state.json"))
TOKEN = os.environ.get("TRAINING_ADMIN_TOKEN", "local-training-only")
DEFAULT = {"seed": 1, "fault": {"mode": "none", "delay_ms": 0, "failure_rate": 0.0}, "requests": 0,
           "resources": [{"id": "res-001", "name": "catalog", "owner": "platform", "tier": 1},
                         {"id": "res-002", "name": "telemetry", "owner": "observability", "tier": 2}]}

def load():
    if not STATE_PATH.exists(): save(DEFAULT.copy())
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))

def save(state):
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_PATH.with_suffix(".tmp")
    tmp.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp.replace(STATE_PATH)

class Handler(BaseHTTPRequestHandler):
    server_version = "TrainingSimulator/1.0"
    def log_message(self, fmt, *args):
        print(json.dumps({"time": time.time(), "request_id": getattr(self, "rid", None), "message": fmt % args}), flush=True)
    def send_json(self, code, payload):
        body = json.dumps(payload).encode()
        self.send_response(code); self.send_header("Content-Type", "application/json")
        self.send_header("X-Request-ID", self.rid); self.send_header("Content-Length", str(len(body)))
        self.end_headers(); self.wfile.write(body)
    def do_GET(self):
        self.rid = self.headers.get("X-Request-ID", str(uuid.uuid4()))
        state = load(); state["requests"] += 1; save(state)
        path = urlparse(self.path).path
        if path == "/health": return self.send_json(200, {"status": "ok", "request_id": self.rid})
        if path == "/api/resources": return self.send_json(200, {"items": state["resources"]})
        if path == "/api/state": return self.send_json(200, {"requests": state["requests"], "fault_mode": state["fault"]["mode"]})
        if path == "/api/dependency":
            fault = state["fault"]; delay = int(fault.get("delay_ms", 0))
            if delay: time.sleep(delay / 1000)
            if fault.get("mode") == "malformed":
                body=b'{broken'; self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers(); return self.wfile.write(body)
            rng = random.Random(state["seed"] + state["requests"])
            if fault.get("mode") == "unavailable" or rng.random() < float(fault.get("failure_rate", 0)):
                return self.send_json(503, {"error": "dependency_unavailable", "retryable": True})
            return self.send_json(200, {"status": "available", "sequence": state["requests"]})
        return self.send_json(404, {"error": "not_found"})
    def do_POST(self):
        self.rid = self.headers.get("X-Request-ID", str(uuid.uuid4()))
        if self.headers.get("Authorization") != f"Bearer {TOKEN}": return self.send_json(403, {"error": "forbidden"})
        length = int(self.headers.get("Content-Length", "0")); raw = self.rfile.read(length)
        try: payload = json.loads(raw or b"{}")
        except json.JSONDecodeError: return self.send_json(400, {"error": "invalid_json"})
        path = urlparse(self.path).path
        if path == "/admin/reset": save(DEFAULT.copy()); return self.send_json(200, {"reset": True})
        if path == "/admin/seed":
            state = DEFAULT.copy(); state["seed"] = int(payload.get("seed", 1)); state["resources"] = payload.get("resources", DEFAULT["resources"]); save(state)
            return self.send_json(200, {"seeded": len(state["resources"])})
        if path == "/admin/fault":
            state = load(); state["fault"] = {"mode": payload.get("mode", "none"), "delay_ms": int(payload.get("delay_ms", 0)), "failure_rate": float(payload.get("failure_rate", 0))}; save(state)
            return self.send_json(200, {"fault": state["fault"]})
        return self.send_json(404, {"error": "not_found"})

if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
