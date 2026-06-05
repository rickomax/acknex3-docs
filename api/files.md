---
layout: default
title: Files
parent: API Reference
has_children: true
nav_order: 3
---

# Files

Files are assigned to keywords to define bitmaps, animations, sounds and songs. Names of files belonging to the finished level (to be compiled in) are given between angle brackets `<...>`.

| Keyword | Summary |
|:--------|:--------|
| [`BMAP`](files/bmap.html) | Assigns a bitmap (`.PCX`, `.LBM` or `.BBM`) to the keyword, or a rectangular section of it (upper-left corner `x,y`, size `dx,dy`, in pixels). |
| [`OVLY`](files/ovly.html) | Like BMAP, but defines an overlay bitmap (for cockpits, weapons, mouse pointers). Occupies more memory but draws faster. Horizontal size must be divisible by 4. |
| [`FONT`](files/font.html) | Assigns a character set. `width,height` is the size of a single character in pixels; character order follows the ASCII set. |
| [`SOUND`](files/sound.html) | Assigns a sound file (`.VOC` or `.WAV`) to the keyword. |
| [`MUSIC`](files/music.html) | Assigns a song file (`.MID`) to the keyword. |
| [`FLIC`](files/flic.html) | Assigns an animation file (`.FLI` or `.FLC`) to the keyword. |
