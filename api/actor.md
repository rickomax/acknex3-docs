---
layout: default
title: Actors (ACTOR)
parent: API Reference
has_children: true
nav_order: 7
---

# Actors (ACTOR)

An Actor is an animate object — a linear automaton with definable action/reaction behaviour. A Thing differs only by lacking the complex behaviour, and uses the **same** definition keywords (see [Things](../thing/)). The definition contains, in order, the keyword assignments below.

| Keyword | Summary |
|:--------|:--------|
| [`ACTOR`](actor/actor.html) | Defines an Actor that can be placed anywhere in WED and optionally assigned a Way. |
| [`TEXTURE`](actor/texture.html) | One- or eight-sided texture; the visible side follows the viewing angle. |
| [`CYCLE`](actor/cycle.html) | Current animation phase of the texture. |
| [`WAYPOINT`](actor/waypoint.html) | Sets a position point (1..32) of the Actor's Way as target; readable as the next waypoint number. |
| [`TARGET`](actor/target.html) | Assigns a new target or behaviour (see the TARGET values: NULL, MOVE, BULLET, STICK, FOLLOW, REPEL, a Way, or another object). |
| [`NULL`](actor/null.html) | TARGET NULL — the Actor does not move (default). |
| [`MOVE`](actor/move.html) | Moves straight ahead along ANGLE, using SPEED and VSPEED. |
| [`BULLET`](actor/bullet.html) | Like MOVE, but triggers IF_HIT and sets RESULT=1 on impact (needs CAREFULLY for collision). |
| [`STICK`](actor/stick.html) | Fixes the Actor at its current offset to the player and moves with it. |
| [`FOLLOW`](actor/follow.html) | Moves toward the player with SPEED, matching height with VSPEED. |
| [`REPEL`](actor/repel.html) | Moves away from the player; height unchanged. |
| [`HEIGHT`](actor/height.html) | Height of the object, absolute (with GROUND) or relative to the region floor. |
| [`ANGLE`](actor/angle.html) | Angle in radians (0..6.28), added to the WMP angle; changeable by actions. |
| [`SPEED`](actor/speed.html) | Horizontal speed in Steps per Tick (default 0). |
| [`VSPEED`](actor/vspeed.html) | Vertical speed in Steps per Tick (default 0). |
| [`MAP_COLOR`](actor/map_color.html) | Colour number (0..255) for drawing on the map. 0 = not drawn, 1 = default colour. |
| [`DIST`](actor/dist.html) | Boundary distance (default 0); exceeding it can trigger IF_NEAR. |
| [`SKILL1...SKILL8`](actor/skill1_skill8.html) | Eight universal parameters; changed/evaluated in actions. |
| [`DISTANCE`](actor/distance.html) | Distance of the player to the object centre (approximate). Read-only. |
| [`SIZE_X`](actor/size_x.html) | Horizontal size of the object in Steps (from the texture). Read-only. |
| [`SIZE_Y`](actor/size_y.html) | Vertical size of the object in Steps (from the texture). Read-only. |
| [`RESULT`](actor/result.html) | Result of SHOOT/EXPLODE on this object (0..1); reset explicitly after evaluation. |
| [`X, Y, Z`](actor/x_y_z.html) | Vertex position of the object (set by direct name). |
| [`REGION`](actor/region.html) | Current region of the Actor; must be reassigned manually when the position is changed. |
| [`IF_NEAR`](actor/if_near.html) | Triggered when the player approaches within DIST; if no DIST, on every contact. |
| [`IF_FAR`](actor/if_far.html) | Triggered when the player moves beyond DIST. |
| [`IF_ARRIVED`](actor/if_arrived.html) | Triggered on crossing a region boundary (with CAREFULLY) or reaching the next waypoint. |
| [`IF_HIT`](actor/if_hit.html) | Triggered when hit by SHOOT/EXPLODE or colliding head-on (see BULLET, FRAGILE). |
| [`EACH_CYCLE`](actor/each_cycle.html) | Triggered after each texture animation cycle. |
| [`EACH_TICK`](actor/each_tick.html) | Triggered after each image build (~1/16 s). |
| [`INVISIBLE`](actor/invisible.html) | Object invisible and passable, as if absent; Actor does not move and no events fire. Auto-set for unplaced objects. |
| [`PASSABLE`](actor/passable.html) | Object is passable for the player. |
| [`VISIBLE`](actor/visible.html) | Set automatically while the object is visible. |
| [`BERKELEY`](actor/berkeley.html) | Object inactive while unseen and beyond its boundary distance — saves time with many animated objects. |
| [`GROUND`](actor/ground.html) | HEIGHT refers to the level's zero height rather than the region floor. |
| [`SEEN`](actor/seen.html) | Set once seen by the player (used by the automap). |
| [`PLAY`](actor/play.html) | Animates the texture one cycle (texture must be ONESHOT). |
| [`FRAGILE`](actor/fragile.html) | IF_HIT can be triggered by EXPLODE. |
| [`CAREFULLY`](actor/carefully.html) | Performs collision detection along a path, avoiding walls/actors and adjusting height (unless GROUND). Costs time. |
| [`SAVE`](actor/save.html) | All Actor properties saved with the game (set automatically for Actors). |
| [`FLAG1...FLAG8`](actor/flag1_flag8.html) | Eight universal flags; changed/evaluated in actions. |
| [`IMMATERIAL`](actor/immaterial.html) | Object is not hit by SHOOT and does not collide (newer engine). |
