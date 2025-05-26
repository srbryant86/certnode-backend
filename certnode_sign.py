import hashlib, sys
def sign_file(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        return "ICS-" + hashlib.sha256(data).hexdigest()[:16].upper()
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python certnode_sign.py <file>")
    else:
        print(sign_file(sys.argv[1]))
