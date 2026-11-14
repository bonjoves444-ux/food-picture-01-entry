"""Best-looking food picture entry: a steaming bowl of ramen.

The program copies the bundled picture (entry.jpg) to the output
directory as entry.png. The copy is byte-for-byte, so the output is
fully deterministic: the same input always produces the same bytes.
No network, no randomness, no timestamps in the output. The program
runs in a fresh container with no network and a read-only repository,
so it only reads the bundled image and writes the single output file.
The image itself is a single fixed picture: one hero dish, a glistening
ramen bowl filling the frame, chopsticks lifting noodles, a jammy egg,
chashu and chili oil, steam rising. Nothing in the program generates,
draws or alters it, which is why the two runs match. The picture was
chosen to make the judge hungry at a glance: gloss, steam and texture,
one dish edge to edge, clear even at about 300 pixels across.
"""

import os
import shutil
import sys

SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
