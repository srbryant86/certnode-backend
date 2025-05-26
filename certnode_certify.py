import hashlib, json, os, sys
def hash_file(path): return hashlib.sha256(open(path, 'rb').read()).hexdigest()[:16].upper()
def update_vault(file_path):
    ics = "ICS-" + hash_file(file_path)
    entry = {
        "title": os.path.basename(file_path),
        "ics": ics,
        "date": "2025-05-30",
        "link": file_path
    }
    for fname in ["vault.json", "ics_registry.json"]:
        if os.path.exists(fname):
            with open(fname, "r") as f: data = json.load(f)
        else:
            data = [] if fname == "vault.json" else {"entries": []}
        if fname == "vault.json":
            data.append(entry)
        else:
            data["entries"].append({
                "ics": ics,
                "title": entry["title"],
                "date": entry["date"]
            })
        with open(fname, "w") as f: json.dump(data, f, indent=2)
    print(f"Certified {entry['title']} as {ics}")
if __name__ == "__main__": update_vault(sys.argv[1]) if len(sys.argv) > 1 else print("Usage: python certnode_certify.py <file>")
