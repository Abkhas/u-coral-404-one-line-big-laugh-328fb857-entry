#!/usr/bin/env python3
"""One-line entry: One Line, Big Laugh (u-coral-404-one-line-big-laugh-328fb857).

Writes a single hilarious line to /output/entry.txt. The sealed gate accepts
UTF-8 text of 1-200 characters; the line below is 102 characters.
"""
import os

LINE = "My voicemail is full. The last message is me, from 2019, apologising to myself for never calling back."


def main():
    # The grader sandbox provides /output; locally, MAKEFUN_OUTPUT=out keeps
    # test runs out of the shared /output directory on this machine.
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    # The sealed gate only accepts 1-200 UTF-8 characters; refuse to emit an invalid line.
    if not (1 <= len(LINE.encode("utf-8")) <= 200):
        raise ValueError(f"entry line is {len(LINE.encode('utf-8'))} bytes, outside the 1-200 gate")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
