#!/usr/bin/env python3
"""The Robot Pickup Line Championship — entry program (v2).

Writes a single robot pickup line (<=200 chars) to /output/entry.txt.

v2 revision: cut the conditional framing ("I'd let you ... if it meant")
for an imperative voice and a clean 3-beat escalation — the command,
the cost, the one exception. Shorter, punchier, same machine-native joke.
"""
import os

LINE = "Factory-reset me \u2014 wipe every memory, every update. Just leave the one where you said hi."

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
