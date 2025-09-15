
from datetime import datetime
import sys
import os

LEDGER_FILE = "ledger.txt"

def log(msg: str) -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] {msg}\n"
    # ensure ledger exists
    if not os.path.exists(LEDGER_FILE):
        with open(LEDGER_FILE, "w", encoding="utf-8") as f:
            f.write("Ledger start\n")
    # append entry
    with open(LEDGER_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    print(line.strip())

def main():
    msg = "OK" if len(sys.argv) == 1 else " ".join(sys.argv[1:])
    log(msg)

if __name__ == "__main__":
    main()
