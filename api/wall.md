---
layout: default
title: Walls (WALL)
parent: API Reference
has_children: true
nav_order: 12
---

# Walls (WALL)

Vertical Walls run along the connecting lines between two vertices and separate regions. A wall definition contains, in order, the keyword assignments below; events and flags can also be read/changed from actions.

| Keyword | Summary |
|:--------|:--------|
| [`WALL`](wall/wall.html) | Defines a wall type that can be assigned to a connecting line in WED. |
| [`TEXTURE`](wall/texture.html) | Texture for both sides of the wall. Two-sided textures switch depending on which vertex (#1 or #2) the wall is viewed from. |
| [`OFFSET_X`](wall/offset_x.html) | Shifts the wall texture left by the given number of pixels. Cannot be combined with the WED ALIGN function. |
| [`OFFSET_Y`](wall/offset_y.html) | Shifts the wall texture down by the given number of pixels. For sky textures, sets the horizon distance from the bottom of the bitmap. |
| [`CYCLE`](wall/cycle.html) | Current animation phase of the wall texture. |
| [`POSITION`](wall/position.html) | Meaning depends on the flags (e.g. lateral position for SLIDEDOOR, edge alignment for PORTCULLIS). |
| [`MAP_COLOR`](wall/map_color.html) | Mode (0..1, default 1) for drawing the wall on the map. 0 = not drawn. |
| [`DIST`](wall/dist.html) | Base/boundary distance of the wall (default 0). Exceeding it can trigger an IF_NEAR action. |
| [`SKILL1...SKILL8`](wall/skill1_skill8.html) | Eight universal parameters with no built-in effect; changed and evaluated in actions. |
| [`DISTANCE`](wall/distance.html) | Distance of the player to the nearest wall vertex (approximate, error up to 20%). Read-only. |
| [`X1, Y1, Z1`](wall/x1_y1_z1.html) | Position of vertex 1 of the wall (read by direct name; `MY` synonyms not allowed). |
| [`X2, Y2, Z2`](wall/x2_y2_z2.html) | Position of vertex 2 of the wall. |
| [`IF_NEAR`](wall/if_near.html) | Triggered when the player approaches the nearest wall vertex within the boundary distance (DIST); if no DIST, on every contact. |
| [`IF_FAR`](wall/if_far.html) | Triggered when the player moves away beyond the boundary distance (DIST). |
| [`IF_HIT`](wall/if_hit.html) | Triggered when the wall is hit by SHOOT/EXPLODE or struck head-on by a flying object (see BULLET, FRAGILE). |
| [`EACH_CYCLE`](wall/each_cycle.html) | Triggered after each texture animation cycle (or end of a ONESHOT animation). |
| [`EACH_TICK`](wall/each_tick.html) | Triggered after each image build (~1/16 s). |
| [`INVISIBLE`](wall/invisible.html) | Wall is invisible but still blocks the player. Same region must be on both sides. |
| [`PASSABLE`](wall/passable.html) | Wall is passable for the player. Same region must be on both sides. |
| [`VISIBLE`](wall/visible.html) | Set automatically while the wall is visible; can be evaluated in actions. |
| [`SEEN`](wall/seen.html) | Set automatically once the wall has been seen (used by the automap). |
| [`BERKELEY`](wall/berkeley.html) | Wall is only active while seen or near its boundary distance — saves time with many animated/sound walls. |
| [`TRANSPARENT`](wall/transparent.html) | Colour 0 in the texture is transparent (grilles, fences); the wall can be penetrated by SHOOT. Same region both sides. |
| [`PLAY`](wall/play.html) | Animates the wall texture for one cycle (texture must be ONESHOT); auto-resets, may trigger EACH_CYCLE. |
| [`PORTCULLIS`](wall/portcullis.html) | Attaches the texture to the wall's upper/lower edge (lifts, trapdoors); aligned by POSITION (0 = bottom, 1 = top). |
| [`SLIDEDOOR`](wall/slidedoor.html) | The wall can be shifted sideways via POSITION. |
| [`FRAGILE`](wall/fragile.html) | The IF_HIT action can be triggered by an EXPLODE instruction. |
| [`FAR`](wall/far.html) | The wall stays visible beyond CLIP_DIST. |
| [`SAVE`](wall/save.html) | All wall properties are stored when the game is saved. |
| [`FLAG1...FLAG8`](wall/flag1_flag8.html) | Eight universal flags with no built-in effect; changed/evaluated in actions. |
| [`FENCE`](wall/fence.html) | Newer single-sided transparent wall flag (allows simpler rendering, like a one-sided TRANSPARENT). |
