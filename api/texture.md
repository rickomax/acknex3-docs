---
layout: default
title: Textures (TEXTURE)
parent: API Reference
has_children: true
nav_order: 4
---

# Textures (TEXTURE)

Textures determine the appearance of the world (walls, floors, ceilings, backgrounds, Things, Actors, panels and overlays). A texture definition contains, in order, the keyword assignments below.

| Keyword | Source | Summary |
|:--------|:------:|:--------|
| [`TEXTURE`](texture/texture.html) | both | Defines a texture object. |
| [`SCALE_XY`](texture/scale_xy.html) | both | Scaling of the texture in pixels per Step, horizontally and vertically. Default 16 pixels/Step. No effect on sky textures. |
| [`SIDES`](texture/sides.html) | both | Number of sides (1..64, default 1). The visible side changes with the viewing angle, giving Things/Actors a 3D appearance. Wall textures may have two sides. |
| [`CYCLES`](texture/cycles.html) | both | Number of animation phases (1..64, default 1). `SIDES * CYCLES` may not exceed 64. If omitted, the texture is not animated. |
| [`BMAPS`](texture/bmaps.html) | both | List of up to 64 bitmap keywords (count = `SIDES * CYCLES`). Front-side phases first, then further sides clockwise. |
| [`DELAY`](texture/delay.html) | both | Per-phase animation durations in Ticks (1..31). Count = CYCLES. Default one Tick per phase. |
| [`SCYCLES`](texture/scycles.html) | both | Per-phase sound flags (0/1). Where 1, the texture sound plays during that phase. |
| [`MIRROR`](texture/mirror.html) | both | Per-side mirror flags (0/1). Where 1, that side's bitmaps are mirrored horizontally. |
| [`RANDOM`](texture/random.html) | both | Maximum value (0..1) of a random delay factor added to each animation phase. |
| [`AMBIENT`](texture/ambient.html) | both | Luminosity of the texture (-1..1, 32 steps, default 0). 1 = self-illuminated; negative values reduce reflectivity (for painted-in shadows). |
| [`SOUND`](texture/sound.html) | both | Keyword of a sound file assigned to the texture. Plays rhythmically on floors when walking, or continuously (with SLOOP) on ceilings. |
| [`SVOL`](texture/svol.html) | both | Maximum sound volume (0..1). Default 0.5. |
| [`SDIST`](texture/sdist.html) | both | Critical distance in Steps below which the texture sound is audible; louder the closer you come. |
| [`ONESHOT`](texture/oneshot.html) | both | The texture is not permanently animated; it shows the first phase and animates one cycle when the object's PLAY flag is set. |
| [`SKY`](texture/sky.html) | both | The texture uses parallax (not perspective) projection — treated as a background (mountains, sky, horizon) at infinite distance, not zoomed. |
| [`SLOOP`](texture/sloop.html) | both | The texture sound plays continuously in a loop, independent of the animation phase. |
| [`CYCLE`](texture/cycle.html) | both | Current animation phase of the texture (can be read/set in actions). |
| [`BLUR`](texture/blur.html) | new | Motion-blur / transparency amount for the texture (newer engine). |
