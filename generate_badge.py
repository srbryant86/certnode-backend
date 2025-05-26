import sys
ics = sys.argv[1] if len(sys.argv) > 1 else 'ICS-UNKNOWN'
print(f"![Verified by CertNode](https://certnode.io/certnode_seal_v1.1.png)\n\nCertified Output | {ics}\n\n[Verify here](https://certnode.io/verify.html?ics={ics})")
