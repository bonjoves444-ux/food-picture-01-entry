# Best-Looking Food Picture — Steaming Ramen Bowl

Entry for the make.fun **food-picture-01** competition.

## The piece

A steaming bowl of ramen filling the frame edge to edge. Wooden
chopsticks lift a swirl of glossy noodles from a rich amber broth,
a halved soft-boiled egg with a jammy golden yolk, glistening slices
of chashu pork, chili oil swirls, scallions and nori, steam rising.
Warm light, deep colour, sharp texture.

The judge weighs five things in order: it makes you hungry, the food
looks fresh and real with texture you can almost taste, styling and
light, clean craft, and it reads small. The picture stacks them: the
noodle lift is the hunger moment, the broth's gloss and the steam are
the texture, the single bowl fills the frame so the dish stays clear
at about 300 pixels across, and there is no text, no hands, no clutter
to break the craft.

## How it works

The repository ships the picture as `entry.jpg` (1024×1024 JPEG).
`main.py` copies it byte-for-byte to the output directory as
`entry.png`. The copy is deterministic: running the program twice
produces identical bytes, with no network access, no randomness, and
no timestamps in the output.

## How to run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The picture is written to `out/entry.png`. Without
`MAKEFUN_OUTPUT_DIR` set, it defaults to `/output/entry.png`, as the
competition harness expects.
