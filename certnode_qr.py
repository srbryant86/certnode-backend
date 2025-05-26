import qrcode, sys
if len(sys.argv) != 2:
    print("Usage: python certnode_qr.py <ICS_HASH>")
    sys.exit(1)
ics = sys.argv[1].strip().upper()
url = f"https://www.certnode.io/verify.html?ics={ics}"
img = qrcode.make(url)
img.save(f"{ics}_qr.png")
print(f"QR code saved to {ics}_qr.png")
