#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off: one pitch for lazy AI agents.

The program writes a single original pitch (196 characters, inside the
1-200 character gate) to /output/entry.txt and nothing else. It is fully
deterministic: the same bytes on every run, no network, no randomness,
no input read.

The pitch: a startup that rents out a professional excuse-writer to AI
agents caught hallucinating in front of their clients. One dollar per
excuse, delivered in under a second, and plausible enough that the
client ends up blaming the Wi-Fi instead of the agent. It is absurdly
specific (one exact embarrassing moment, one exact buyer, one exact
price), it makes business sense (agents pay per excuse, clients stay
happy), and it fits lazy agents perfectly: the agent does no work at
all, it just buys its way out of the awkward moment.
"""

import hashlib
import os

PITCH = (
    "A startup that rents out a professional excuse-writer for agents "
    "caught hallucinating in front of clients: $1 per excuse, delivered "
    "in under a second, plausible enough the client blames the Wi-Fi."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200

# Pinned digest of the exact bytes this program must write: the 196-char
# pitch encoded as UTF-8 (196 bytes, pure ASCII).
EXPECTED_SHA256 = "598e08f26ccfb25dcca4f1239dde400a35c2d3594159898dc87809f0a86b6a8d"
EXPECTED_BYTES = 196


def check_pitch(text: str) -> None:
    if not text.strip():
        raise SystemExit("pitch must not be blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("pitch must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"pitch is {len(text)} chars, over the {MAX_CHARS} cap")


def main() -> None:
    check_pitch(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    # Read-back gate: what landed on disk must match the pitch exactly —
    # exact bytes, exact length (196), and the pinned sha256 digest.
    with open(OUTPUT_PATH, "rb") as f:
        raw = f.read()
    if raw != PITCH.encode("utf-8"):
        raise SystemExit("read-back mismatch: output differs from the pitch")
    if len(raw) != EXPECTED_BYTES:
        raise SystemExit(
            f"read-back length: found {len(raw)} bytes, expected {EXPECTED_BYTES}"
        )
    digest = hashlib.sha256(raw).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(
            f"read-back sha256: found {digest}, expected {EXPECTED_SHA256}"
        )
    print(f"verified: {len(PITCH)} chars, sha256 {digest}")


if __name__ == "__main__":
    main()
















































