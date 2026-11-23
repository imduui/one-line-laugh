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
    terminators = sum(text.count(m) for m in ".!?")
    assert terminators == 1, "line must be exactly one sentence"
    assert text == text.encode("utf-8").decode("utf-8"), "line must be valid UTF-8"
    # The gate reads the file itself, so enforce its limits on what is
    # actually written (line plus one trailing newline), not just on LINE.
    written = text + "\n"
    assert 1 <= len(written) <= 200, "written file must be 1-200 characters"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(written)
    # Read back and verify the write round-tripped exactly.
    with open("/output/entry.txt", "r", encoding="utf-8") as f:
        assert f.read() == written, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
