"""Unsent: The Micro-Confession Sprint.

Writes one two-part micro-confession (a To: line and the unsent message
itself) to /output/entry.txt, exactly as typed and never sent.
"""

import os

TO_LINE = "To: Maya"
MESSAGE = (
    "I was outside your wedding in the car for twenty minutes. "
    "I had the dress on and everything. I just couldn't watch you "
    "marry someone who hits you and pretend my face was fine."
)


def render() -> str:
    """The confession as one file: To: line, message line, final newline."""
    return TO_LINE + "\n" + MESSAGE + "\n"


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = render()
    # Gate: the whole file must stay within 1..260 characters.
    assert 1 <= len(text) <= 260, len(text)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
