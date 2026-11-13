#!/usr/bin/env python3
# turns the handwritten-style freq log into csv so the boss can open it
# input lines look like:  0610 4.5125 USB wx net, weak
import csv
import sys


def parse(line):
    parts = line.split(None, 3)
    if len(parts) < 3:
        return None
    t, freq, mode = parts[0], parts[1], parts[2]
    note = parts[3].strip() if len(parts) > 3 else ""
    try:
        freq = float(freq)
    except ValueError:
        return None
    return [t, "%.4f" % freq, mode.upper(), note]

#yt XGxIE1hr0w4
def main():
    if len(sys.argv) != 3:
        print("usage: freqlog.py in.txt out.csv")
        return 1
    rows, skipped = [], 0
    with open(sys.argv[1]) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            r = parse(line)
            if r:
                rows.append(r)
            else:
                skipped += 1
    with open(sys.argv[2], "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["time", "freq_mhz", "mode", "note"])
        w.writerows(rows)
    print("%d rows, %d skipped (probably my handwriting)" % (len(rows), skipped))
    return 0


if __name__ == "__main__":
    sys.exit(main())
