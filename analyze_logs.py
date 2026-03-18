import json
from collections import Counter
from pathlib import Path

LOG_FILE = Path("logs/events.jsonl")

if not LOG_FILE.exists():
    print("No existe logs/events.jsonl")
    raise SystemExit(1)

events = []
with LOG_FILE.open("r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            pass

if not events:
    print("No hay eventos para analizar.")
    raise SystemExit(0)

ips = Counter()
paths = Counter()
user_agents = Counter()
usernames = Counter()
event_types = Counter()

for e in events:
    event_types[e.get("event_type", "unknown")] += 1
    ips[e.get("ip", "unknown")] += 1
    paths[e.get("path", "unknown")] += 1
    user_agents[e.get("user_agent", "unknown")] += 1

    if e.get("event_type") == "credential_attempt":
        usernames[e.get("username", "")] += 1

print("\n=== Resumen de eventos ===")
for event_type, count in event_types.most_common():
    print(f"{event_type}: {count}")

print("\n=== Top 5 IPs ===")
for ip, count in ips.most_common(5):
    print(f"{ip}: {count}")

print("\n=== Top 5 rutas ===")
for path, count in paths.most_common(5):
    print(f"{path}: {count}")

print("\n=== Top 5 user-agents ===")
for ua, count in user_agents.most_common(5):
    print(f"{ua}: {count}")

print("\n=== Usernames más probados ===")
for username, count in usernames.most_common(5):
    print(f"{username}: {count}")