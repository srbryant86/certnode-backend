import json, requests
with open("vault.json") as f:
    latest = json.load(f)[-1]
requests.post("https://your-webhook-url.com", json=latest)
