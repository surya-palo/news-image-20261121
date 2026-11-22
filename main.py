#!/usr/bin/env python3
"""Entry program for make.fun bounty news-image-20261121.

Copies the pre-rendered poster entry.png (built by render.py) to the
output directory and verifies the copy byte-for-byte with SHA-256.
Standard library only; no network access.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    dst = out_dir / "entry.png"
    if not SRC.is_file():
        print(f"error: {SRC} not found", file=sys.stderr)
        return 1
    expected = sha256_of(SRC)
    shutil.copyfile(SRC, dst)
    actual = sha256_of(dst)
    if actual != expected:
        print(f"error: sha256 mismatch: {actual} != {expected}",
              file=sys.stderr)
        return 1
    print(f"wrote {dst} ({dst.stat().st_size} bytes, sha256 {actual})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
