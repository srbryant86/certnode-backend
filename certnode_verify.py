import sys
def verify_ics(ics):
    trusted = ['ICS-2025-0001', 'ICS-2025-0002', 'ICS-2025-MANIFESTO']
    if ics in trusted:
        print(f"{ics} is a verified CertNode hash.")
    else:
        print(f"{ics} is NOT verified.")
if __name__ == '__main__':
    if len(sys.argv) > 1:
        verify_ics(sys.argv[1])
    else:
        print("Usage: python certnode_verify.py <ICS_HASH>")
