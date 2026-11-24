"""One-Star Review of Something Essential.

Writes one deadpan one-star review of sleep, 160 characters or fewer,
to /output/entry.txt. Pure Python standard library only.
"""

import os

# The review text lives in one named constant so the 160-character
# limit is easy to audit in a single place.
REVIEW = "One star. I give sleep eight hours every night and wake up tired. Worst subscription I have ever paid for."

# Entry constraints and destination, kept together for clarity.
MAX_CHARS = 160
OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def write_review(path=OUTPUT_PATH):
    """Write REVIEW to *path*, refusing anything over the limit."""
    # Self-check: fail loudly rather than emit an over-long entry.
    assert len(REVIEW) <= MAX_CHARS, (
        f"review is {len(REVIEW)} chars, over the {MAX_CHARS}-char limit"
    )
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


def main():
    write_review()


if __name__ == "__main__":
    main()
