#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review — one-line review of planet Earth by an alien tourist."""

import os

# One line, no newline: the gate requires /output/entry.txt to be UTF-8,
# 1-200 characters, a single line. The entry below is 132 characters.
ENTRY = "Earth: stunning views, generous hosts \u2014 but the dominant species stares at small glowing rectangles instead of the sky. Three stars."

# Gate check: one line, 1-200 characters (byte-identical on every run).
assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} outside 1-200"
assert "\n" not in ENTRY, "entry must be a single line"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
