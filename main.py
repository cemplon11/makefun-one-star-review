"""One-Star Review of Something Essential.

Writes one deadpan one-star review of sleep, 160 characters or fewer,
to /output/entry.txt. Pure Python standard library only.
"""

import os

REVIEW = "One star. I give sleep eight hours every night and wake up tired. Worst subscription I have ever paid for."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
