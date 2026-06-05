---
layout: default
title: Palettes
parent: API Reference
has_children: true
nav_order: 3
---

# Palettes

A palette loads a 256-colour palette from a graphics file and defines the shading ranges and colour animations.

| Keyword | Source | Summary |
|:--------|:------:|:--------|
| [`PALETTE`](palette/palette.html) | both | Defines a palette. Contains, in order, the keyword assignments below. |
| [`PALFILE`](palette/palfile.html) | both | Graphics file whose colours are used for the base palette. Colours 0 and 1 carry the colour for infinite distance (black indoors / foggy white outdoors). |
| [`RANGE`](palette/range.html) | both | Defines a shading range used for distance shading: start colour number `s` (1..254) and number of colours `l` (up to 64). Up to 24 ranges. Colours outside any range are not shaded (useful for light sources). |
| [`HARD`](palette/hard.html) | both | Performs shading 'hard' — colours are shifted rather than recalculated, keeping texture detail more recognisable. |
