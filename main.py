#!/usr/bin/env python3
"""Angry Judge entry: one short rant, written to /output/entry.txt.

The rant is a single first-person scene about an office chair that
sinks a little lower in every meeting, escalating to a punchline about
the job finally being honest. It is embedded here as a constant so the
program is fully self-contained: no file reads, no network, no clock,
no randomness. Every run produces byte-identical output.
"""

import os
import sys

RANT_SENTENCES = (
    "My office chair has been sinking one centimeter per meeting since March.",
    "By December I'll be delivering the quarterly results from under the table, "
    "and honestly, that's the first honest thing this job has ever done to me.",
)

MAX_CHARS = 400


def build_rant() -> str:
    """Join the rant sentences into the single entry text.

    The text is assembled from fixed sentence constants, so the result
    is identical on every run. No input is read from anywhere else.
    """
    rant = " ".join(RANT_SENTENCES)
    if not 1 <= len(rant) <= MAX_CHARS:
        raise ValueError(
            f"rant must be 1-{MAX_CHARS} characters, got {len(rant)}"
        )
    return rant


def main() -> int:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(build_rant())
    return 0


if __name__ == "__main__":
    sys.exit(main())
