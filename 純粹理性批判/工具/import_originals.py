#!/usr/bin/env python3
"""Download complete German A/B editions from Project Gutenberg into this repository."""
from pathlib import Path
from urllib.request import urlopen
import hashlib

ROOT = Path(__file__).resolve().parents[1] / "原文"
EDITIONS = {
    "Kant_KrV_B_1787_de.txt": "https://www.gutenberg.org/cache/epub/6343/pg6343.txt",
    "Kant_KrV_A_1781_de.txt": "https://www.gutenberg.org/cache/epub/6342/pg6342.txt",
}

for name, url in EDITIONS.items():
    with urlopen(url, timeout=90) as response:
        raw = response.read()
    text = raw.decode("utf-8-sig")
    if "Kritik der reinen Vernunft" not in text or len(text) < 100000:
        raise ValueError(f"Unexpected or incomplete source: {url}")
    dest = ROOT / name
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    print(f"{dest.name}: {len(text):,} characters; SHA256={hashlib.sha256(raw).hexdigest()}")
