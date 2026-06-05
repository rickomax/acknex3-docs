---
layout: default
title: Textures (TEXTURE)
parent: API Reference
has_children: true
nav_order: 10
---

# Textures (TEXTURE)

Textures determine the appearance of the world (walls, floors, ceilings, backgrounds, Things, Actors, panels and overlays). A texture definition contains, in order, the keyword assignments below.

| Keyword | Summary |
|:--------|:--------|
| [`ALBEDO`](texture/albedo.html) | Reflection factor of the texture (0..1, default 0) for light from LIGHT_ANGLE or a separate light source; gives buildings, columns and ledges a more three-dimensional look. |
| [`AMBIENT`](texture/ambient.html) | Luminosity of the texture (-1..1, 32 steps, default 0). 1 = self-illuminated; negative values reduce reflectivity (for painted-in shadows). |
| [`ATTACH`](texture/attach.html) | Attaches an additional, transparent texture to a wall, thing or actor texture — for paintings, inscriptions, bullet holes or shadows. Walls allow a chain of ATTACH textures; things/actors allow only one (set on the object, not its texture). |
| [`ATTACHED`](texture/attached.html) | Set automatically while the object's texture carries an ATTACH texture. |
| [`AUTORANGE`](texture/autorange.html) | Automatically shades every palette colour contained in any RANGE — even unsorted ones — according to their similarity to the INFINITY colour. |
| [`BLUR`](texture/blur.html) | Motion-blur / transparency amount for the texture (newer engine). |
| [`BMAPS`](texture/bmaps.html) | List of up to 64 bitmap keywords (count = `SIDES * CYCLES`). Front-side phases first, then further sides clockwise. |
| [`CLUSTER`](texture/cluster.html) | MODEL textures only: displays just the vertices of the model's polygons. |
| [`CYCLE`](texture/cycle.html) | Current animation phase of the texture (can be read/set in actions). |
| [`CYCLES`](texture/cycles.html) | Number of animation phases (1..64, default 1). `SIDES * CYCLES` may not exceed 64. If omitted, the texture is not animated. |
| [`DELAY`](texture/delay.html) | Per-phase animation durations in Ticks (1..31). Count = CYCLES. Default one Tick per phase. |
| [`LIGHTMAP`](texture/lightmap.html) | ATTACH-texture flag that maps pre-computed light and shadow onto a wall texture; the LIGHTMAP bitmap must contain only shading-range colours. |
| [`MAPCOLOR`](texture/mapcolor.html) | Colour number used to draw a MODEL texture as a non-textured wireframe (WIRE) and on the automap. |
| [`MIRROR`](texture/mirror.html) | Per-side mirror flags (0/1). Where 1, that side's bitmaps are mirrored horizontally. |
| [`ONESHOT`](texture/oneshot.html) | The texture is not permanently animated; it shows the first phase and animates one cycle when the object's PLAY flag is set. |
| [`RADIANCE`](texture/radiance.html) | Maximum brightness of the texture (0..1, default 0); with high ambient light, RADIANCE>0 textures are tinted with the palette's brightness colour. |
| [`RANDOM`](texture/random.html) | Maximum value (0..1) of a random delay factor added to each animation phase. |
| [`SCALE_X`](texture/scale_x.html) | Horizontal scaling of the texture in pixels per step (for floor/ceiling textures, scaling along the X axis). |
| [`SCALE_XY`](texture/scale_xy.html) | Scaling of the texture in pixels per Step, horizontally and vertically. Default 16 pixels/Step. No effect on sky textures. |
| [`SCALE_Y`](texture/scale_y.html) | Vertical scaling of the texture in pixels per step (for floor/ceiling textures, scaling along the Y axis). |
| [`SCYCLES`](texture/scycles.html) | Per-phase sound flags (0/1). Where 1, the texture sound plays during that phase. |
| [`SDIST`](texture/sdist.html) | Critical distance in Steps below which the texture sound is audible; louder the closer you come. |
| [`SHADOW`](texture/shadow.html) | The ATTACH texture is drawn at the actor's floor height; with a dark DIAPHANOUS texture this produces an actor shadow. |
| [`SIDES`](texture/sides.html) | Number of sides (1..64, default 1). The visible side changes with the viewing angle, giving Things/Actors a 3D appearance. Wall textures may have two sides. |
| [`SKY`](texture/sky.html) | The texture uses parallax (not perspective) projection — treated as a background (mountains, sky, horizon) at infinite distance, not zoomed. |
| [`SLOOP`](texture/sloop.html) | The texture sound plays continuously in a loop, independent of the animation phase. |
| [`SOUND`](texture/sound.html) | Keyword of a sound file assigned to the texture. Plays rhythmically on floors when walking, or continuously (with SLOOP) on ceilings. |
| [`SVOL`](texture/svol.html) | Maximum sound volume (0..1). Default 0.5. |
| [`TEXTURE`](texture/texture.html) | Defines a texture object. |
| [`TOUCH`](texture/touch.html) | Text string shown next to the mouse pointer when it touches the wall/thing/actor carrying this texture (requires TOUCH_MODE >= 1). |
| [`TOUCH_RANGE`](texture/touch_range.html) | Maximum distance (in steps) at which the object still reacts to the mouse for TOUCH and texture mouse events; IMMATERIAL objects are invisible to the mouse. |
