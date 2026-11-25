#!/usr/bin/env python3
"""The Absurd Clause Contest — u-donrulezz-the-absurd-clause-contest-035cc0f1.

Writes one original English sentence (<= 200 characters), phrased as a
clause buried deep inside a terms-of-service agreement, to /output/entry.txt.
Deterministic: the same clause, byte for byte, on every run. The humour
comes from the register: dry legal boilerplate ("shall be returned only
upon written request submitted in triplicate") applied to something the
reader never expected a contract to claim — one left sock.
"""

import os

CLAUSE = (
    "Upon acceptance of these Terms, the User's left sock becomes the "
    "property of the Service and shall be returned only upon written "
    "request submitted in triplicate."
)


def main() -> None:
    if not (1 <= len(CLAUSE) <= 200):
        raise SystemExit(f"clause is {len(CLAUSE)} chars, must be 1-200")
    if CLAUSE != CLAUSE.strip() or "\n" in CLAUSE:
        raise SystemExit("clause must be a single clean line")
    if not CLAUSE.endswith("."):
        raise SystemExit("clause must be one complete sentence")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(CLAUSE + "\n")
    print(f"wrote {len(CLAUSE)} chars to {path}")


if __name__ == "__main__":
    main()
