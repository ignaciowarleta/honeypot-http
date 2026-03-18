import os
import json
from datetime import datetime, timezone
from flask import Flask, request, render_template, redirect

app = Flask(__name__)

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "events.jsonl")

os.makedirs(LOG_DIR, exist_ok=True)


def log_event(event_type: str, extra: dict | None = None) -> None:
    event = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "event_type": event_type,
        "ip": request.headers.get("X-Forwarded-For", request.remote_addr),
        "method": request.method,
        "path": request.path,
        "user_agent": request.headers.get("User-Agent", ""),
        "query_string": request.query_string.decode("utf-8", errors="ignore"),
    }

    if extra:
        event.update(extra)

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


@app.before_request
def capture_all_requests():
    suspicious_paths = {
        "/admin",
        "/wp-login.php",
        "/phpmyadmin",
        "/.env",
        "/config",
        "/backup",
        "/login",
    }

    event_type = "request"
    if request.path in suspicious_paths:
        event_type = "suspicious_request"

    log_event(event_type)


@app.route("/", methods=["GET"])
def index():
    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    log_event(
        "credential_attempt",
        {
            "username": username,
            "password": password,
        },
    )

    #Respuesta falsa
    return render_template(
        "login.html",
        error="Credenciales incorrectas. Inténtalo de nuevo."
    ), 401


@app.route("/admin", methods=["GET"])
def admin():
    return "Unauthorized", 401


@app.route("/health", methods=["GET"])
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)