---
layout: default
title: Regions (REGION)
parent: API Reference
has_children: true
nav_order: 8
---

# Regions (REGION)

Regions are sections of the playing field bounded by polygons (walls). A region definition contains, in order, the keyword assignments below.

| Keyword | Summary |
|:--------|:--------|
| [`AMBIENT`](region/ambient.html) | Base brightness of the region (0..1, 16 steps). Added to self-illuminating texture ambient. |
| [`CEIL_ANGLE`](region/ceil_angle.html) | Rotation angle of the ceiling texture (0..2pi, default 0) around the region's GENIUS centre. |
| [`CEIL_ASCEND`](region/ceil_ascend.html) | Lifts the ceiling corner points upward by the Z values of the region's vertices, producing a sloped ceiling. |
| [`CEIL_DESCEND`](region/ceil_descend.html) | Lowers the ceiling corner points by the Z values of the region's vertices, producing a sloped ceiling. |
| [`CEIL_HGT`](region/ceil_hgt.html) | Height of the region ceiling in Steps. |
| [`CEIL_LIFTED`](region/ceil_lifted.html) | Raises ceiling corner points by the Z values of their vertices. |
| [`CEIL_OFFS_X`](region/ceil_offs_x.html) | Ceiling texture shift along X. |
| [`CEIL_OFFS_Y`](region/ceil_offs_y.html) | Ceiling texture shift along Y. |
| [`CEIL_TEX`](region/ceil_tex.html) | Texture of the region ceiling. Its sound plays on entering; continuous with SLOOP. |
| [`CLIP_DIST`](region/clip_dist.html) | Per-region view distance in Steps (default 1000); speeds rendering in complex levels. |
| [`EACH_CYCLE`](region/each_cycle.html) | Triggered at the end of each texture animation cycle. |
| [`EACH_TICK`](region/each_tick.html) | Triggered after each image build (~1/16 s). |
| [`FLAG1...FLAG8`](region/flag1_flag8.html) | Eight universal flags; changed/evaluated in actions. |
| [`FLOOR_ANGLE`](region/floor_angle.html) | Rotation angle of the floor texture (0..2pi, default 0), one full value being a complete revolution around the region's GENIUS centre. |
| [`FLOOR_ASCEND`](region/floor_ascend.html) | Lifts the floor corner points upward by the Z values of the region's vertices, producing a sloped floor. |
| [`FLOOR_DESCEND`](region/floor_descend.html) | Lowers the floor corner points by the Z values of the region's vertices, producing a sloped floor. |
| [`FLOOR_HGT`](region/floor_hgt.html) | Height of the region floor in Steps. |
| [`FLOOR_LIFTED`](region/floor_lifted.html) | Raises floor corner points by the Z values of their vertices (tilted surfaces). |
| [`FLOOR_OFFS_X`](region/floor_offs_x.html) | Floor texture shift along X (pixels, relative to field origin). |
| [`FLOOR_OFFS_Y`](region/floor_offs_y.html) | Floor texture shift along Y. |
| [`FLOOR_TEX`](region/floor_tex.html) | Texture of the region floor. Its sound plays when stepped on; pitch/volume changeable by skills. |
| [`HERE`](region/here.html) | Set automatically while the player is in this region. |
| [`IF_ARISE`](region/if_arise.html) | Triggered when the player's eye height reaches or exceeds the ceiling height. |
| [`IF_DIVE`](region/if_dive.html) | Triggered when the player's eye height reaches or falls below the floor height. |
| [`IF_ENTER`](region/if_enter.html) | Triggered when the player enters the region. |
| [`IF_LEAVE`](region/if_leave.html) | Triggered when the player leaves the region. |
| [`PLAY`](region/play.html) | Animates floor/ceiling textures one cycle (textures must be ONESHOT). |
| [`REGION`](region/region.html) | Defines a region type that can be assigned to an actual region in WED. |
| [`SAVE`](region/save.html) | All region properties are saved with the game. |
| [`SAVE_ALL`](region/save_all.html) | All walls and things inside the region are stored by SAVE instructions — useful when the region is moved at runtime (e.g. by ROTATE). |
| [`SEEN`](region/seen.html) | Set once the region has been seen by the player. |
| [`SKILL1...SKILL8`](region/skill1_skill8.html) | Eight universal parameters; changed/evaluated in actions. |
| [`VISIBLE`](region/visible.html) | Set while the floor, ceiling or a back wall of the region is visible. |
