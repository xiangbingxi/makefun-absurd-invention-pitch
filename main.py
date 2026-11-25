import os
import sys

ENTRY = 'Meet the Apology Toaster: it prints "Sorry for the delayed response" on your breakfast in case you see someone whose email you\'ve ignored.'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify what was actually written, byte for byte.
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != ENTRY:
        print("ERROR: /output/entry.txt does not match ENTRY exactly", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
