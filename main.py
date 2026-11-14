"""Best-looking food picture entry: a steaming bowl of tonkotsu ramen,
round 3 — the same dish as rounds 1 and 2, executed denser: a higher
noodle lift, thicker steam, glossier broth and a runnier yolk, built
to the winning formula the live leaderboard converged on.

The program copies the bundled picture (entry.jpg) to the output
directory as entry.png. The copy is byte-for-byte, so the output is
fully deterministic: the same input always produces the same bytes.
No network, no randomness, no timestamps in the output. The program
runs in a fresh container with no network and a read-only repository,
so it only reads the bundled image and writes the single output file.
The image itself is a single fixed picture: one hero dish, a glistening
ramen bowl filling the frame, chopsticks lifting a HIGH glossy noodle
pull, a jammy egg with its runny orange yolk oozing front and center,
three glistening chashu slices, nori, scallions, sesame and chili oil
on a creamy tonkotsu broth, thick steam curling through warm bokeh
light over a dark wood table. Nothing in the program generates,
draws or alters it, which is why the two runs match. The picture was
chosen to make the judge hungry at a glance: gloss, steam and texture,
one dish edge to edge, clear even at about 300 pixels across.
What changed for this round is density, not the dish: the noodle
pull climbs higher, the yolk runs instead of sitting set, the steam
is thicker, and the broth shines more. The leaders all serve the
same bowl, so the way to beat them is to serve it hungrier, with
every cue turned up at the same time.
"""

import os
import shutil
import sys

# The bundled picture: round 3's denser ramen image, 1024x1024 JPEG.
SOURCE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.jpg")


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(SOURCE, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
