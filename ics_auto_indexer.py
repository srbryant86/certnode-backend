import os, json, hashlib
def compute_ics(filepath):
    with open(filepath, 'rb') as f: return hashlib.sha256(f.read()).hexdigest()[:16].upper()
def update_registry(directory):
    vault, registry = [], {"entries": []}
    for filename in os.listdir(directory):
        if filename.endswith(".pdf") or filename.endswith(".md"):
            ics = compute_ics(os.path.join(directory, filename))
            vault.append({"title": filename, "ics": f"ICS-{ics}", "date": "2025-05-26", "link": filename})
            registry["entries"].append({"ics": f"ICS-{ics}", "title": filename, "date": "2025-05-26"})
    with open("vault.json", "w") as vf: json.dump(vault, vf, indent=2)
    with open("ics_registry.json", "w") as rf: json.dump(registry, rf, indent=2)
if __name__ == "__main__": update_registry(".")
