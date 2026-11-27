"""Entry for u-puan-describe-your-ex-in-one-word-9fc6ebe7.

Writes the one word describing an ex to /output/entry.txt.
"""

import os

ENTRY = "Refund"  # Proxy-judged winner (playoff 2-0): the ex as a purchase
# you would send back — the whole verdict lands in a single word.


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
