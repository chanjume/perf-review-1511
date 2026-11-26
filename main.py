#!/usr/bin/env python3
"""Funniest One-Line Performance Review — writes the entry to entry.txt.

The review: one line, 135 characters, an AI agent's performance review of
its human operator, Marcus.
"""

import os

ENTRY = (
    # 135 characters: one line, performance-review form, punch on last word.
    "Exceeds Expectations: At 2:47 a.m., Marcus fixed the outage and "
    "expensed the pizza to the incident ticket. Promotion: on-call, forever."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
