#!/usr/bin/env python3
"""The One-Line Laugh — writes a single funny line to /output/entry.txt.

The line is a single sentence of 1-200 characters: a bank's fraud alert
triggered by the most suspicious activity imaginable — buying groceries
instead of ordering takeout. Surprise ending, everyday truth, no wasted
words.
"""

LINE = "My bank flagged my account for unusual activity \u2014 it was me buying groceries instead of takeout."


def main() -> None:
    text = LINE.strip()
    # Validate: single sentence, 1-200 characters, non-whitespace.
    assert text, "line must not be empty"
    assert len(text) <= 200, f"line is {len(text)} characters, over the 200 limit"
    assert text.count(".") + text.count("!") + text.count("?") <= 1, (
        "line must be a single sentence"
    )
    assert text == text.encode("utf-8").decode("utf-8"), "line must be valid UTF-8"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
