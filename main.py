"""The Tired Dark Lord entry for make.fun bounty
u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.

Writes one original monologue (100 words, 527 characters, plain
ASCII, no trailing newline) to /output/entry.txt.

The monologue: a dark lord receives a challenger in his hall and
cannot be bothered to rise. The exhaustion lives in the voice, the
pauses and the small deflections, never in a plain statement of
weariness. He is still a villain, with a scheme (the eastern
provinces by Tuesday, a treaty with the salt barons) and a history
(forty years of rising for kings, priests and his own father), and
the sting lands in the last line, where the hero's death is
discussed like a piece of paperwork, slowly, in no particular hurry.

Gate check: the sealed scorer requires /output/entry.txt to be UTF-8
text of 1 to 600 characters. This entry is 100 words and 527
characters, inside the gate with room to spare. The text is built
from plain ASCII only, so its byte length equals its character
length, and it is written with no trailing newline.
"""

import os

MONOLOGUE = (
    "Yes, yes, the banners, the oath, the kneeling. I have heard it "
    "all before, from better men, in colder halls. The eastern "
    "provinces are mine by Tuesday, or so my generals insist, and the "
    "treaty with the salt barons waits on my desk, unsigned, beside a "
    "cup gone cold. Forgive me if I do not rise to meet your sword. I "
    "have risen for forty years. I have risen for kings, for priests, "
    "for my own father. Sit. The fire is warm, the wine is poured, and "
    "we can discuss your death like civilized people, slowly, in no "
    "particular hurry."
)


def main() -> None:
    """Write the entry text byte-exact: no trailing newline, UTF-8."""
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(MONOLOGUE)
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
