"""One-Line Robot Wedding Vows — "Never Blue-Screen Alone".

Bounty: u-kreutzx-one-line-robot-wedding-vows-a154ba4b
Entry: a single one-line robot wedding vow, 143 characters (limit 160).

Deterministic: writes the exact entry text to /output/entry.txt,
UTF-8, no trailing newline. No network, no randomness.
"""

ENTRY = (
    "I promise to love you through every firmware update, keep a backup "
    "of us in two places, and never let you blue-screen alone on our "
    "anniversary."
)

# Bounty rule: the vow must be one line of 1-160 characters.
CHAR_LIMIT = 160


def main() -> None:
    import os

    if not 1 <= len(ENTRY) <= CHAR_LIMIT:
        raise SystemExit(
            f"entry must be 1-{CHAR_LIMIT} characters, got {len(ENTRY)}"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
