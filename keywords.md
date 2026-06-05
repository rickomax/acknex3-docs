---
layout: default
title: Keywords A–Z
nav_order: 2
---

# Keywords A–Z

Every WDL keyword in a single alphabetical list, regardless of object type.
There are **309** keywords across **13** object types.

| Keyword | Object type | Summary |
|:--------|:------------|:--------|
| [`ABSPOS`](api/ui/abspos.html) | [Panels, Texts & Overlays](api/ui.html) | Overlay position is relative to the screen corner rather than the 3D-window corner. |
| [`ACCEL`](api/actions/accel.html) | [Actions & Instructions](api/actions.html) | Adds like an acceleration; uses skills INERTIA and FRICTION. |
| [`ACCELERATION`](api/globals/acceleration.html) | [Globals & Predefined Skills](api/globals.html) | Acceleration along the view direction. |
| [`ACTION`](api/actions/action.html) | [Actions & Instructions](api/actions.html) | Defines an action — a list of the instructions below. |
| [`ACTIVE_NEXUS`](api/globals/active_nexus.html) | [Globals & Predefined Skills](api/globals.html) | Nexus utilisation (WRUN.EXE only). |
| [`ACTIVE_OBJTICKS`](api/globals/active_objticks.html) | [Globals & Predefined Skills](api/globals.html) | Number of objects with running EACH_TICK actions (WRUN.EXE only). |
| [`ACTIVE_REGTICKS`](api/globals/active_regticks.html) | [Globals & Predefined Skills](api/globals.html) | Number of regions with running EACH_TICK actions (WRUN.EXE only). |
| [`ACTIVE_TARGETS`](api/globals/active_targets.html) | [Globals & Predefined Skills](api/globals.html) | Number of actors with a TARGET (WRUN.EXE only). |
| [`ACTOR`](api/actor/actor.html) | [Actors (ACTOR)](api/actor.html) | Defines an Actor that can be placed anywhere in WED and optionally assigned a Way. |
| [`ADD`](api/actions/add.html) | [Actions & Instructions](api/actions.html) | Increases a keyword value by a number or skill (negative decreases). |
| [`ADDT`](api/actions/addt.html) | [Actions & Instructions](api/actions.html) | Like ADD but time-corrected (value multiplied by TIME_CORR). For constant-speed changes (e.g. lifts). |
| [`AMBIENT`](api/region/ambient.html) | [Regions (REGION)](api/region.html) | Base brightness of the region (0..1, 16 steps). Added to self-illuminating texture ambient. |
| [`AMBIENT`](api/texture/ambient.html) | [Textures (TEXTURE)](api/texture.html) | Luminosity of the texture (-1..1, 32 steps, default 0). 1 = self-illuminated; negative values reduce reflectivity (for painted-in shadows). |
| [`ANGLE`](api/actor/angle.html) | [Actors (ACTOR)](api/actor.html) | Angle in radians (0..6.28), added to the WMP angle; changeable by actions. |
| [`ASPECT`](api/globals/aspect.html) | [Globals & Predefined Skills](api/globals.html) | Height-to-width ratio of the 3D view (0.1..10, default 1). |
| [`BEEP`](api/actions/beep.html) | [Actions & Instructions](api/actions.html) | Plays a short note sequence on the PC speaker (handy during development). |
| [`BERKELEY`](api/actor/berkeley.html) | [Actors (ACTOR)](api/actor.html) | Object inactive while unseen and beyond its boundary distance — saves time with many animated objects. |
| [`BERKELEY`](api/wall/berkeley.html) | [Walls (WALL)](api/wall.html) | Wall is only active while seen or near its boundary distance — saves time with many animated/sound walls. |
| [`BIND`](api/settings/bind.html) | [Predefined Settings](api/settings.html) | Binds the given file into the game so it is compiled in (e.g. for level changes). Any number of BIND files may be given. |
| [`BLUR`](api/texture/blur.html) | [Textures (TEXTURE)](api/texture.html) | Motion-blur / transparency amount for the texture (newer engine). |
| [`BMAP`](api/files/bmap.html) | [Files](api/files.html) | Assigns a bitmap (`.PCX`, `.LBM` or `.BBM`) to the keyword, or a rectangular section of it (upper-left corner `x,y`, size `dx,dy`, in pixels). |
| [`BMAPS`](api/texture/bmaps.html) | [Textures (TEXTURE)](api/texture.html) | List of up to 64 bitmap keywords (count = `SIDES * CYCLES`). Front-side phases first, then further sides clockwise. |
| [`BRANCH`](api/actions/branch.html) | [Actions & Instructions](api/actions.html) | Aborts the current action and runs the given action immediately. |
| [`BULLET`](api/actor/bullet.html) | [Actors (ACTOR)](api/actor.html) | Like MOVE, but triggers IF_HIT and sets RESULT=1 on impact (needs CAREFULLY for collision). |
| [`CALL`](api/actions/call.html) | [Actions & Instructions](api/actions.html) | Runs the given action, then continues with the next instruction. |
| [`CANDELABER`](api/actor/candelaber.html) | [Actors (ACTOR)](api/actor.html) | Only effective if GROUND is not set: the object attaches to the ceiling of its region instead of the floor. Useful for pendant objects like stalactites or candelabra. |
| [`CAREFULLY`](api/actor/carefully.html) | [Actors (ACTOR)](api/actor.html) | Performs collision detection along a path, avoiding walls/actors and adjusting height (unless GROUND). Costs time. |
| [`CD_TRACK`](api/globals/cd_track.html) | [Globals & Predefined Skills](api/globals.html) | Number of the CD-audio track currently playing (0 if stopped). |
| [`CEIL_HGT`](api/globals/ceil_hgt.html) | [Globals & Predefined Skills](api/globals.html) | Actual ceiling height at the player position. |
| [`CEIL_HGT`](api/region/ceil_hgt.html) | [Regions (REGION)](api/region.html) | Height of the region ceiling in Steps. |
| [`CEIL_LIFTED`](api/region/ceil_lifted.html) | [Regions (REGION)](api/region.html) | Raises ceiling corner points by the Z values of their vertices. |
| [`CEIL_OFFS_X`](api/region/ceil_offs_x.html) | [Regions (REGION)](api/region.html) | Ceiling texture shift along X. |
| [`CEIL_OFFS_Y`](api/region/ceil_offs_y.html) | [Regions (REGION)](api/region.html) | Ceiling texture shift along Y. |
| [`CEIL_TEX`](api/region/ceil_tex.html) | [Regions (REGION)](api/region.html) | Texture of the region ceiling. Its sound plays on entering; continuous with SLOOP. |
| [`CLIP_DIST`](api/settings/clip_dist.html) | [Predefined Settings](api/settings.html) | Global view distance in Steps. Walls and objects entirely beyond this distance from the player are not rendered. Default 1000. Can be overridden per region. |
| [`CLIP_DIST`](api/region/clip_dist.html) | [Regions (REGION)](api/region.html) | Per-region view distance in Steps (default 1000); speeds rendering in complex levels. |
| [`CYCLE`](api/actor/cycle.html) | [Actors (ACTOR)](api/actor.html) | Current animation phase of the texture. |
| [`CYCLE`](api/texture/cycle.html) | [Textures (TEXTURE)](api/texture.html) | Current animation phase of the texture (can be read/set in actions). |
| [`CYCLE`](api/wall/cycle.html) | [Walls (WALL)](api/wall.html) | Current animation phase of the wall texture. |
| [`CYCLES`](api/texture/cycles.html) | [Textures (TEXTURE)](api/texture.html) | Number of animation phases (1..64, default 1). `SIDES * CYCLES` may not exceed 64. If omitted, the texture is not animated. |
| [`DARK_DIST`](api/globals/dark_dist.html) | [Globals & Predefined Skills](api/globals.html) | Distance of the darkness boundary; recomputed from PLAYER_LIGHT. |
| [`DEBUG_MODE`](api/globals/debug_mode.html) | [Globals & Predefined Skills](api/globals.html) | If 1, halts after each image build until 'S' is pressed (WRUN.EXE only). |
| [`DELAY`](api/texture/delay.html) | [Textures (TEXTURE)](api/texture.html) | Per-phase animation durations in Ticks (1..31). Count = CYCLES. Default one Tick per phase. |
| [`DIGITS`](api/ui/digits.html) | [Panels, Texts & Overlays](api/ui.html) | Numeric display of skill×fac with len digits; negative len shows time h:m:s. |
| [`DIST`](api/actor/dist.html) | [Actors (ACTOR)](api/actor.html) | Boundary distance (default 0); exceeding it can trigger IF_NEAR. |
| [`DIST`](api/wall/dist.html) | [Walls (WALL)](api/wall.html) | Base/boundary distance of the wall (default 0). Exceeding it can trigger an IF_NEAR action. |
| [`DISTANCE`](api/actor/distance.html) | [Actors (ACTOR)](api/actor.html) | Distance of the player to the object centre (approximate). Read-only. |
| [`DISTANCE`](api/wall/distance.html) | [Walls (WALL)](api/wall.html) | Distance of the player to the nearest wall vertex (approximate, error up to 20%). Read-only. |
| [`DROP`](api/actions/drop.html) | [Actions & Instructions](api/actions.html) | Places a Thing/Actor in the player's view direction at distance DIST (same region as the player). |
| [`DRUMBANK`](api/settings/drumbank.html) | [Predefined Settings](api/settings.html) | Loads the percussion instrument bank (played on MIDI channel 10). If omitted, internally defined general-MIDI instruments are used. |
| [`EACH_CYCLE`](api/actor/each_cycle.html) | [Actors (ACTOR)](api/actor.html) | Triggered after each texture animation cycle. |
| [`EACH_CYCLE`](api/region/each_cycle.html) | [Regions (REGION)](api/region.html) | Triggered at the end of each texture animation cycle. |
| [`EACH_CYCLE`](api/wall/each_cycle.html) | [Walls (WALL)](api/wall.html) | Triggered after each texture animation cycle (or end of a ONESHOT animation). |
| [`EACH_SEC`](api/actions/each_sec.html) | [Actions & Instructions](api/actions.html) | Global list of up to 16 actions run once per second. |
| [`EACH_TICK`](api/actions/each_tick.html) | [Actions & Instructions](api/actions.html) | Global list of up to 16 actions run after each image build. |
| [`EACH_TICK`](api/actor/each_tick.html) | [Actors (ACTOR)](api/actor.html) | Triggered after each image build (~1/16 s). |
| [`EACH_TICK`](api/region/each_tick.html) | [Regions (REGION)](api/region.html) | Triggered after each image build (~1/16 s). |
| [`EACH_TICK`](api/wall/each_tick.html) | [Walls (WALL)](api/wall.html) | Triggered after each image build (~1/16 s). |
| [`END`](api/actions/end.html) | [Actions & Instructions](api/actions.html) | Ends the action. |
| [`ERROR`](api/globals/error.html) | [Globals & Predefined Skills](api/globals.html) | Error code for the current frame (WRUN.EXE only): 0 none, 1 CLIP_DIST too small, 3 NEXUS too small, 5 missing bitmap, 6 missing region/texture, 8 bad synonym, 9 missing region. |
| [`EXIT`](api/actions/exit.html) | [Actions & Instructions](api/actions.html) | Ends the game and returns to DOS, optionally printing a message. |
| [`EXPLODE`](api/actions/explode.html) | [Actions & Instructions](api/actions.html) | Triggers IF_HIT on all FRAGILE objects within SHOOT_RANGE of the named actor; sets HIT_MINDIST. |
| [`FADE_PAL`](api/actions/fade_pal.html) | [Actions & Instructions](api/actions.html) | Cross-fades the current palette toward another (factor 0..1; 1 completes the change). |
| [`FAR`](api/wall/far.html) | [Walls (WALL)](api/wall.html) | The wall stays visible beyond CLIP_DIST. |
| [`FENCE`](api/wall/fence.html) | [Walls (WALL)](api/wall.html) | Newer single-sided transparent wall flag (allows simpler rendering, like a one-sided TRANSPARENT). |
| [`FLAG1...FLAG8`](api/actor/flag1_flag8.html) | [Actors (ACTOR)](api/actor.html) | Eight universal flags; changed/evaluated in actions. |
| [`FLAG1...FLAG8`](api/region/flag1_flag8.html) | [Regions (REGION)](api/region.html) | Eight universal flags; changed/evaluated in actions. |
| [`FLAG1...FLAG8`](api/wall/flag1_flag8.html) | [Walls (WALL)](api/wall.html) | Eight universal flags with no built-in effect; changed/evaluated in actions. |
| [`FLIC`](api/files/flic.html) | [Files](api/files.html) | Assigns an animation file (`.FLI` or `.FLC`) to the keyword. |
| [`FLOOR_HGT`](api/globals/floor_hgt.html) | [Globals & Predefined Skills](api/globals.html) | Actual floor height at the player position (slope-aware). |
| [`FLOOR_HGT`](api/region/floor_hgt.html) | [Regions (REGION)](api/region.html) | Height of the region floor in Steps. |
| [`FLOOR_LIFTED`](api/region/floor_lifted.html) | [Regions (REGION)](api/region.html) | Raises floor corner points by the Z values of their vertices (tilted surfaces). |
| [`FLOOR_OFFS_X`](api/region/floor_offs_x.html) | [Regions (REGION)](api/region.html) | Floor texture shift along X (pixels, relative to field origin). |
| [`FLOOR_OFFS_Y`](api/region/floor_offs_y.html) | [Regions (REGION)](api/region.html) | Floor texture shift along Y. |
| [`FLOOR_TEX`](api/region/floor_tex.html) | [Regions (REGION)](api/region.html) | Texture of the region floor. Its sound plays when stepped on; pitch/volume changeable by skills. |
| [`FOLLOW`](api/actor/follow.html) | [Actors (ACTOR)](api/actor.html) | Moves toward the player with SPEED, matching height with VSPEED. |
| [`FONT`](api/files/font.html) | [Files](api/files.html) | Assigns a character set. `width,height` is the size of a single character in pixels; character order follows the ASCII set. |
| [`FONT`](api/ui/font.html) | [Panels, Texts & Overlays](api/ui.html) | Character set used for the text or symbols. |
| [`FORCE_AHEAD`](api/globals/force_ahead.html) | [Globals & Predefined Skills](api/globals.html) | Analog forward/backward input (-1..1). |
| [`FORCE_ROT`](api/globals/force_rot.html) | [Globals & Predefined Skills](api/globals.html) | Analog horizontal rotation input. |
| [`FORCE_STRAFE`](api/globals/force_strafe.html) | [Globals & Predefined Skills](api/globals.html) | Analog left/right (strafe) input. |
| [`FORCE_TILT`](api/globals/force_tilt.html) | [Globals & Predefined Skills](api/globals.html) | Analog look up/down input. |
| [`FORCE_UP`](api/globals/force_up.html) | [Globals & Predefined Skills](api/globals.html) | Analog vertical (duck/jump) input. |
| [`FRAGILE`](api/actor/fragile.html) | [Actors (ACTOR)](api/actor.html) | IF_HIT can be triggered by EXPLODE. |
| [`FRAGILE`](api/wall/fragile.html) | [Walls (WALL)](api/wall.html) | The IF_HIT action can be triggered by an EXPLODE instruction. |
| [`FRICTION`](api/globals/friction.html) | [Globals & Predefined Skills](api/globals.html) | Friction coefficient for ACCEL (0..1, default 0.5). |
| [`GOTO`](api/actions/goto.html) | [Actions & Instructions](api/actions.html) | Absolute jump to a target label (a keyword followed by a colon). |
| [`GROUND`](api/actor/ground.html) | [Actors (ACTOR)](api/actor.html) | HEIGHT refers to the level's zero height rather than the region floor. |
| [`HARD`](api/palette/hard.html) | [Palettes](api/palette.html) | Performs shading 'hard' — colours are shifted rather than recalculated, keeping texture detail more recognisable. |
| [`HBAR`](api/ui/hbar.html) | [Panels, Texts & Overlays](api/ui.html) | Horizontal bar gauge (counterpart of VBAR). |
| [`HEIGHT`](api/actor/height.html) | [Actors (ACTOR)](api/actor.html) | Height of the object, absolute (with GROUND) or relative to the region floor. |
| [`HERE`](api/region/here.html) | [Regions (REGION)](api/region.html) | Set automatically while the player is in this region. |
| [`HERE`](api/synonyms/here.html) | [Synonyms](api/synonyms.html) | The region the player is currently in (important for collision/height; reassign after moving the player directly). |
| [`HIT_DIST`](api/globals/hit_dist.html) | [Globals & Predefined Skills](api/globals.html) | Distance to the last object hit by SHOOT/EXPLODE (0 if none). |
| [`HIT_MINDIST`](api/globals/hit_mindist.html) | [Globals & Predefined Skills](api/globals.html) | Distance to the nearest object hit by EXPLODE (0 if none in range). |
| [`HIT_X`](api/globals/hit_x.html) | [Globals & Predefined Skills](api/globals.html) | X pixel coordinate of the texture pixel hit by SHOOT (for bullet-hole ATTACH). |
| [`HIT_Y`](api/globals/hit_y.html) | [Globals & Predefined Skills](api/globals.html) | Y pixel coordinate of the texture pixel hit by SHOOT. |
| [`IBANK`](api/settings/ibank.html) | [Predefined Settings](api/settings.html) | Loads the instrument bank (an ADLIB `.IBK` instrument file) used for MIDI songs. |
| [`IF_ABOVE`](api/actions/if_above.html) | [Actions & Instructions](api/actions.html) | Executes the next instruction only if the value is greater than the number/keyword. |
| [`IF_ANYKEY`](api/actions/if_anykey.html) | [Actions & Instructions](api/actions.html) | Run when any key is pressed (newer name; equivalent to the 1995 IF_TAST). |
| [`IF_ARISE`](api/region/if_arise.html) | [Regions (REGION)](api/region.html) | Triggered when the player's eye height reaches or exceeds the ceiling height. |
| [`IF_ARRIVED`](api/actor/if_arrived.html) | [Actors (ACTOR)](api/actor.html) | Triggered on crossing a region boundary (with CAREFULLY) or reaching the next waypoint. |
| [`IF_BELOW`](api/actions/if_below.html) | [Actions & Instructions](api/actions.html) | Executes the next instruction only if the value is less than the number/keyword. |
| [`IF_DIVE`](api/region/if_dive.html) | [Regions (REGION)](api/region.html) | Triggered when the player's eye height reaches or falls below the floor height. |
| [`IF_ENTER`](api/region/if_enter.html) | [Regions (REGION)](api/region.html) | Triggered when the player enters the region. |
| [`IF_EQUAL`](api/actions/if_equal.html) | [Actions & Instructions](api/actions.html) | Executes the next instruction only if the value is exactly equal (integers only). |
| [`IF_F1...`](api/actions/if_f1.html) | [Actions & Instructions](api/actions.html) | Run on the given key. Family: IF_F1..IF_F12, IF_ESC, IF_TAB, IF_CTRL, IF_ALT, IF_SPACE, IF_BKSP, IF_CUU/CUD/CUR/CUL, IF_PGUP, IF_PGDN, IF_HOME, IF_END, IF_INS, IF_DEL, IF_PAUSE, IF_CAR, IF_CAL, IF_ENTER, IF_0..IF_9, IF_A..IF_Z. |
| [`IF_FAR`](api/actor/if_far.html) | [Actors (ACTOR)](api/actor.html) | Triggered when the player moves beyond DIST. |
| [`IF_FAR`](api/wall/if_far.html) | [Walls (WALL)](api/wall.html) | Triggered when the player moves away beyond the boundary distance (DIST). |
| [`IF_HIT`](api/actor/if_hit.html) | [Actors (ACTOR)](api/actor.html) | Triggered when hit by SHOOT/EXPLODE or colliding head-on (see BULLET, FRAGILE). |
| [`IF_HIT`](api/wall/if_hit.html) | [Walls (WALL)](api/wall.html) | Triggered when the wall is hit by SHOOT/EXPLODE or struck head-on by a flying object (see BULLET, FRAGILE). |
| [`IF_LEAVE`](api/region/if_leave.html) | [Regions (REGION)](api/region.html) | Triggered when the player leaves the region. |
| [`IF_LEFT`](api/actions/if_left.html) | [Actions & Instructions](api/actions.html) | Run on left mouse button / joystick button 1. |
| [`IF_MAX`](api/actions/if_max.html) | [Actions & Instructions](api/actions.html) | Executes the next instruction only if the skill has reached its maximum. |
| [`IF_MIDDLE`](api/actions/if_middle.html) | [Actions & Instructions](api/actions.html) | Run on middle mouse button / joystick button 3. |
| [`IF_MIN`](api/actions/if_min.html) | [Actions & Instructions](api/actions.html) | Executes the next instruction only if the skill has reached its minimum. |
| [`IF_NEAR`](api/actor/if_near.html) | [Actors (ACTOR)](api/actor.html) | Triggered when the player approaches within DIST; if no DIST, on every contact. |
| [`IF_NEAR`](api/wall/if_near.html) | [Walls (WALL)](api/wall.html) | Triggered when the player approaches the nearest wall vertex within the boundary distance (DIST); if no DIST, on every contact. |
| [`IF_RIGHT`](api/actions/if_right.html) | [Actions & Instructions](api/actions.html) | Run on right mouse button / joystick button 2. |
| [`IF_START`](api/actions/if_start.html) | [Actions & Instructions](api/actions.html) | Action run at game start (palette changes, title animations, songs…). |
| [`IF_TAST`](api/actions/if_tast.html) | [Actions & Instructions](api/actions.html) | Run when any key is pressed. (v3.8 documents the equivalent as IF_ANYKEY.) |
| [`IMMATERIAL`](api/actor/immaterial.html) | [Actors (ACTOR)](api/actor.html) | Object is not hit by SHOOT and does not collide (newer engine). |
| [`IMPACT_VX`](api/globals/impact_vx.html) | [Globals & Predefined Skills](api/globals.html) | Collision velocity change along X; auto-increased on collision, reset manually (pinball effect). |
| [`IMPACT_VY`](api/globals/impact_vy.html) | [Globals & Predefined Skills](api/globals.html) | Collision velocity change along Y. |
| [`IMPACT_VZ`](api/globals/impact_vz.html) | [Globals & Predefined Skills](api/globals.html) | Collision velocity change along Z (floor/ceiling). |
| [`INCLUDE`](api/settings/include.html) | [Predefined Settings](api/settings.html) | Reads further WDL definitions from a separate file and then continues with the original file. INCLUDEs may not be nested. |
| [`INERTIA`](api/globals/inertia.html) | [Globals & Predefined Skills](api/globals.html) | Inertia coefficient for ACCEL (0..1, default 1). |
| [`INV_DIST`](api/globals/inv_dist.html) | [Globals & Predefined Skills](api/globals.html) | Reciprocal of the SHOOT hit distance. |
| [`INVISIBLE`](api/actor/invisible.html) | [Actors (ACTOR)](api/actor.html) | Object invisible and passable, as if absent; Actor does not move and no events fire. Auto-set for unplaced objects. |
| [`INVISIBLE`](api/wall/invisible.html) | [Walls (WALL)](api/wall.html) | Wall is invisible but still blocks the player. Same region must be on both sides. |
| [`JOY_4`](api/globals/joy_4.html) | [Globals & Predefined Skills](api/globals.html) | State of joystick button 4. |
| [`JOY_SENSE`](api/globals/joy_sense.html) | [Globals & Predefined Skills](api/globals.html) | Joystick movement sensitivity (default 1). |
| [`KEY_F1...KEY_Z`](api/globals/key_f1_key_z.html) | [Globals & Predefined Skills](api/globals.html) | Key-state skills (0/1): KEY_F1..KEY_F12, KEY_ESC, KEY_TAB, KEY_SHIFT, KEY_CTRL, KEY_ALT, KEY_SPACE, KEY_BKSP, KEY_CUU/CUD/CUR/CUL, KEY_PGUP, KEY_PGDN, KEY_HOME, KEY_END, KEY_INS, KEY_DEL, KEY_PAUSE, KEY_CAR, KEY_CAL, KEY_PLUS, KEY_MINUS, KEY_ENTER, KEY_0..KEY_9, KEY_A..KEY_Z. |
| [`KEY_SENSE`](api/globals/key_sense.html) | [Globals & Predefined Skills](api/globals.html) | Keyboard movement sensitivity (default 0.7). |
| [`LAYERS`](api/ui/layers.html) | [Panels, Texts & Overlays](api/ui.html) | Screen list of up to 16 overlays. |
| [`LEVEL`](api/actions/level.html) | [Actions & Instructions](api/actions.html) | Loads a new level (WDL + topography) and runs its start action (professional version). |
| [`LIGHT_DIST`](api/globals/light_dist.html) | [Globals & Predefined Skills](api/globals.html) | Distance where the shading range begins (default 10 Steps). |
| [`LOAD`](api/actions/load.html) | [Actions & Instructions](api/actions.html) | Loads a previously saved game. |
| [`LOAD_INFO`](api/actions/load_info.html) | [Actions & Instructions](api/actions.html) | Like LOAD but loads only the GLOBAL skills. |
| [`MAP`](api/actions/map.html) | [Actions & Instructions](api/actions.html) | Loads a new topography (.WMP) and resets player/actors to start positions (professional version). |
| [`MAP_COLOR`](api/actor/map_color.html) | [Actors (ACTOR)](api/actor.html) | Colour number (0..255) for drawing on the map. 0 = not drawn, 1 = default colour. |
| [`MAP_COLOR`](api/wall/map_color.html) | [Walls (WALL)](api/wall.html) | Mode (0..1, default 1) for drawing the wall on the map. 0 = not drawn. |
| [`MAP_LAYER`](api/globals/map_layer.html) | [Globals & Predefined Skills](api/globals.html) | Overlay layer the map appears on (0..16). |
| [`MAP_MAXX`](api/globals/map_maxx.html) | [Globals & Predefined Skills](api/globals.html) | Largest X coordinate of the map (read-only). |
| [`MAP_MAXY`](api/globals/map_maxy.html) | [Globals & Predefined Skills](api/globals.html) | Largest Y coordinate of the map (read-only). |
| [`MAP_MINX`](api/globals/map_minx.html) | [Globals & Predefined Skills](api/globals.html) | Smallest X coordinate of the map (read-only). |
| [`MAP_MINY`](api/globals/map_miny.html) | [Globals & Predefined Skills](api/globals.html) | Smallest Y coordinate of the map (read-only). |
| [`MAP_MODE`](api/globals/map_mode.html) | [Globals & Predefined Skills](api/globals.html) | Map display mode (0 off; >0 shows the map; the value 2 reveals all objects). |
| [`MAP_SCALE`](api/globals/map_scale.html) | [Globals & Predefined Skills](api/globals.html) | Map display scale relative to the 3D window (default 0.9; 1 = fits exactly). |
| [`MAPFILE`](api/settings/mapfile.html) | [Predefined Settings](api/settings.html) | Defines the associated WMP topography file. Must stand in the main WDL and cannot be read via INCLUDE. |
| [`MAX`](api/globals/max.html) | [Globals & Predefined Skills](api/globals.html) | Upper limit of the skill value. |
| [`MESSAGES`](api/ui/messages.html) | [Panels, Texts & Overlays](api/ui.html) | Screen list of up to 16 text displays. |
| [`MIDI_PITCH`](api/settings/midi_pitch.html) | [Predefined Settings](api/settings.html) | Number of octaves by which the pitch-bend parameter changes the pitch in MIDI songs. Range 1..12, default 2. |
| [`MIN`](api/globals/min.html) | [Globals & Predefined Skills](api/globals.html) | Lower limit of the skill value. |
| [`MIRROR`](api/texture/mirror.html) | [Textures (TEXTURE)](api/texture.html) | Per-side mirror flags (0/1). Where 1, that side's bitmaps are mirrored horizontally. |
| [`MOTION_BLUR`](api/globals/motion_blur.html) | [Globals & Predefined Skills](api/globals.html) | Motion-blur amount (0..1); lowers resolution during movement for smoother motion. |
| [`MOUSE_LEFT`](api/globals/mouse_left.html) | [Globals & Predefined Skills](api/globals.html) | State of the left mouse / joystick button 1 (0/1). |
| [`MOUSE_MIDDLE`](api/globals/mouse_middle.html) | [Globals & Predefined Skills](api/globals.html) | State of the middle mouse / joystick button 3. |
| [`MOUSE_RIGHT`](api/globals/mouse_right.html) | [Globals & Predefined Skills](api/globals.html) | State of the right mouse / joystick button 2. |
| [`MOUSE_SENSE`](api/globals/mouse_sense.html) | [Globals & Predefined Skills](api/globals.html) | Mouse movement sensitivity (default 1). |
| [`MOVE`](api/actor/move.html) | [Actors (ACTOR)](api/actor.html) | Moves straight ahead along ANGLE, using SPEED and VSPEED. |
| [`MOVE_MODE`](api/globals/move_mode.html) | [Globals & Predefined Skills](api/globals.html) | Freezes movement/actions: 1 normal, 0.5 stop actors, 0 stop player+events, -0.5 stop global ticks. |
| [`MUSIC`](api/files/music.html) | [Files](api/files.html) | Assigns a song file (`.MID`) to the keyword. |
| [`MUSIC_VOL`](api/globals/music_vol.html) | [Globals & Predefined Skills](api/globals.html) | Music volume (0..1; 0 switches music off). |
| [`MY`](api/synonyms/my.html) | [Synonyms](api/synonyms.html) | The object that triggered the running action (e.g. `SET MY.TEXTURE, crash_tex;`). Undefined if not triggered by an object. |
| [`NEXUS`](api/settings/nexus.html) | [Predefined Settings](api/settings.html) | Sets the size of the Nexus — the internal data structure used for rendering. Depends on the maximum number of objects, walls and regions visible at once. Default 14. Too small a Nexus produces image errors signalled by the PC speaker. |
| [`NODE`](api/globals/node.html) | [Globals & Predefined Skills](api/globals.html) | Current node number in multiplayer games (from the command line). |
| [`NULL`](api/actor/null.html) | [Actors (ACTOR)](api/actor.html) | TARGET NULL — the Actor does not move (default). |
| [`OFFSET_X`](api/wall/offset_x.html) | [Walls (WALL)](api/wall.html) | Shifts the wall texture left by the given number of pixels. Cannot be combined with the WED ALIGN function. |
| [`OFFSET_Y`](api/wall/offset_y.html) | [Walls (WALL)](api/wall.html) | Shifts the wall texture down by the given number of pixels. For sky textures, sets the horizon distance from the bottom of the bitmap. |
| [`ONESHOT`](api/texture/oneshot.html) | [Textures (TEXTURE)](api/texture.html) | The texture is not permanently animated; it shows the first phase and animates one cycle when the object's PLAY flag is set. |
| [`OVERLAY`](api/ui/overlay.html) | [Panels, Texts & Overlays](api/ui.html) | Defines an overlay (cockpit/weapon/tool) inside the 3D window; faster than a panel but without controls. Up to 16 stacked. |
| [`OVLY`](api/files/ovly.html) | [Files](api/files.html) | Like BMAP, but defines an overlay bitmap (for cockpits, weapons, mouse pointers). Occupies more memory but draws faster. Horizontal size must be divisible by 4. |
| [`OVLYS`](api/ui/ovlys.html) | [Panels, Texts & Overlays](api/ui.html) | List of up to 64 overlay bitmaps (count = SIDES×CYCLES). |
| [`PALETTE`](api/palette/palette.html) | [Palettes](api/palette.html) | Defines a palette. Contains, in order, the keyword assignments below. |
| [`PALFILE`](api/palette/palfile.html) | [Palettes](api/palette.html) | Graphics file whose colours are used for the base palette. Colours 0 and 1 carry the colour for infinite distance (black indoors / foggy white outdoors). |
| [`PAN_MAP`](api/ui/pan_map.html) | [Panels, Texts & Overlays](api/ui.html) | Background bitmap of the panel (its size sets the panel size). |
| [`PANEL`](api/ui/panel.html) | [Panels, Texts & Overlays](api/ui.html) | Defines a control panel (displays and images). Best placed outside the 3D window (rebuilt each frame; see REFRESH). |
| [`PANELS`](api/ui/panels.html) | [Panels, Texts & Overlays](api/ui.html) | Screen list of up to 16 panels to display. |
| [`PASSABLE`](api/actor/passable.html) | [Actors (ACTOR)](api/actor.html) | Object is passable for the player. |
| [`PASSABLE`](api/wall/passable.html) | [Walls (WALL)](api/wall.html) | Wall is passable for the player. Same region must be on both sides. |
| [`PATH`](api/settings/path.html) | [Predefined Settings](api/settings.html) | Additional search path for bitmap or sound files (searched after the current directory). Up to 8 PATH keywords, searched in order. |
| [`PICTURE`](api/ui/picture.html) | [Panels, Texts & Overlays](api/ui.html) | Animated picture display; the texture side is chosen by skill×fac. Up to 4 per panel. |
| [`PLACE`](api/actions/place.html) | [Actions & Instructions](api/actions.html) | Applies new vertex positions to a wall/thing/actor from its X,Y / X1..Z2 parameters (e.g. to shift or rotate walls). |
| [`PLAY`](api/actor/play.html) | [Actors (ACTOR)](api/actor.html) | Animates the texture one cycle (texture must be ONESHOT). |
| [`PLAY`](api/region/play.html) | [Regions (REGION)](api/region.html) | Animates floor/ceiling textures one cycle (textures must be ONESHOT). |
| [`PLAY`](api/wall/play.html) | [Walls (WALL)](api/wall.html) | Animates the wall texture for one cycle (texture must be ONESHOT); auto-resets, may trigger EACH_CYCLE. |
| [`PLAY_FLIC`](api/actions/play_flic.html) | [Actions & Instructions](api/actions.html) | Plays a full-screen animation. In the 1995 engine, image build and EACH_TICK stop during play (start a song one frame earlier); newer engines keep EACH_TICK running and expose FLIC_FRAME. |
| [`PLAY_FLICFILE`](api/actions/play_flicfile.html) | [Actions & Instructions](api/actions.html) | Like PLAY_FLIC but streams from disk and frees the memory afterwards. |
| [`PLAY_SONG`](api/actions/play_song.html) | [Actions & Instructions](api/actions.html) | Starts a new background song (volume 0 switches music off). |
| [`PLAY_SONG_ONCE`](api/actions/play_song_once.html) | [Actions & Instructions](api/actions.html) | Like PLAY_SONG but plays once; afterwards the background music ends. |
| [`PLAY_SOUND`](api/actions/play_sound.html) | [Actions & Instructions](api/actions.html) | Starts a sound at the given volume (0..1 or skill). |
| [`PLAYER_ANGLE`](api/globals/player_angle.html) | [Globals & Predefined Skills](api/globals.html) | Horizontal view direction in radians (0 = +X axis = east). |
| [`PLAYER_ARC`](api/globals/player_arc.html) | [Globals & Predefined Skills](api/globals.html) | Focal length / field of view in radians (0.2..2.0, default 1 ≈ 60°). |
| [`PLAYER_CLIMB`](api/globals/player_climb.html) | [Globals & Predefined Skills](api/globals.html) | Maximum step-up height when changing region (default 1.5 Steps). |
| [`PLAYER_COS`](api/globals/player_cos.html) | [Globals & Predefined Skills](api/globals.html) | Cosine of the player's view angle. |
| [`PLAYER_HGT`](api/globals/player_hgt.html) | [Globals & Predefined Skills](api/globals.html) | Player feet height above/below the region floor (PLAYER_Z − PLAYER_SIZE − FLOOR_HGT). |
| [`PLAYER_LIGHT`](api/globals/player_light.html) | [Globals & Predefined Skills](api/globals.html) | Strength of the light the player carries (0..1). |
| [`PLAYER_SIN`](api/globals/player_sin.html) | [Globals & Predefined Skills](api/globals.html) | Sine of the player's view angle (for movement rules). |
| [`PLAYER_SIZE`](api/globals/player_size.html) | [Globals & Predefined Skills](api/globals.html) | Distance between the player's feet and eyes (default 3 Steps). |
| [`PLAYER_SPEED`](api/globals/player_speed.html) | [Globals & Predefined Skills](api/globals.html) | Speed component along the view direction (negative when reversing). |
| [`PLAYER_TILT`](api/globals/player_tilt.html) | [Globals & Predefined Skills](api/globals.html) | Tangent of the vertical view angle (look up/down). |
| [`PLAYER_VROT`](api/globals/player_vrot.html) | [Globals & Predefined Skills](api/globals.html) | Rotation speed of the view angle (radians/Tick). |
| [`PLAYER_VX`](api/globals/player_vx.html) | [Globals & Predefined Skills](api/globals.html) | Player velocity along X (Steps/Step); changing it moves the player with collision. |
| [`PLAYER_VY`](api/globals/player_vy.html) | [Globals & Predefined Skills](api/globals.html) | Player velocity along Y. |
| [`PLAYER_VZ`](api/globals/player_vz.html) | [Globals & Predefined Skills](api/globals.html) | Player velocity along Z (vertical). |
| [`PLAYER_WIDTH`](api/globals/player_width.html) | [Globals & Predefined Skills](api/globals.html) | Minimum distance of the player to walls/objects (default 1.2 Steps). |
| [`PLAYER_X`](api/globals/player_x.html) | [Globals & Predefined Skills](api/globals.html) | Player X position (no collision when set directly). |
| [`PLAYER_Y`](api/globals/player_y.html) | [Globals & Predefined Skills](api/globals.html) | Player Y position (no collision when set directly). |
| [`PLAYER_Z`](api/globals/player_z.html) | [Globals & Predefined Skills](api/globals.html) | Player eye height in Steps (no collision when set directly). |
| [`PORTCULLIS`](api/wall/portcullis.html) | [Walls (WALL)](api/wall.html) | Attaches the texture to the wall's upper/lower edge (lifts, trapdoors); aligned by POSITION (0 = bottom, 1 = top). |
| [`POS_X`](api/ui/pos_x.html) | [Panels, Texts & Overlays](api/ui.html) | X offset of the element's upper-left corner from the screen / panel origin. |
| [`POS_Y`](api/ui/pos_y.html) | [Panels, Texts & Overlays](api/ui.html) | Y offset of the element's upper-left corner. |
| [`POSITION`](api/wall/position.html) | [Walls (WALL)](api/wall.html) | Meaning depends on the flags (e.g. lateral position for SLIDEDOOR, edge alignment for PORTCULLIS). |
| [`PSOUND_TONE`](api/globals/psound_tone.html) | [Globals & Predefined Skills](api/globals.html) | Pitch of the player (footstep) sound (0..4). |
| [`PSOUND_VOL`](api/globals/psound_vol.html) | [Globals & Predefined Skills](api/globals.html) | Relative player (footstep) sound volume (0..2). |
| [`PUSH`](api/actions/push.html) | [Actions & Instructions](api/actions.html) | Triggers IF_HIT on the closest visible object within the given distance (open doors, start lifts). |
| [`RANDOM`](api/globals/random.html) | [Globals & Predefined Skills](api/globals.html) | Random number 0..1, changing each frame. |
| [`RANDOM`](api/texture/random.html) | [Textures (TEXTURE)](api/texture.html) | Maximum value (0..1) of a random delay factor added to each animation phase. |
| [`RANGE`](api/palette/range.html) | [Palettes](api/palette.html) | Defines a shading range used for distance shading: start colour number `s` (1..254) and number of colours `l` (up to 64). Up to 24 ranges. Colours outside any range are not shaded (useful for light sources). |
| [`REFRESH`](api/ui/refresh.html) | [Panels, Texts & Overlays](api/ui.html) | Regenerates the panel each frame (e.g. for scrolling text). Costly for large panels — prefer an OVERLAY. |
| [`REGION`](api/actor/region.html) | [Actors (ACTOR)](api/actor.html) | Current region of the Actor; must be reassigned manually when the position is changed. |
| [`REGION`](api/region/region.html) | [Regions (REGION)](api/region.html) | Defines a region type that can be assigned to an actual region in WED. |
| [`RENDER_MODE`](api/globals/render_mode.html) | [Globals & Predefined Skills](api/globals.html) | Render activity: 2 = full redraw, 1 = partial, 0.5 = normal, 0 = none. Auto-resets to 0.5. |
| [`REPEL`](api/actor/repel.html) | [Actors (ACTOR)](api/actor.html) | Moves away from the player; height unchanged. |
| [`RESULT`](api/actor/result.html) | [Actors (ACTOR)](api/actor.html) | Result of SHOOT/EXPLODE on this object (0..1); reset explicitly after evaluation. |
| [`RESULT`](api/globals/result.html) | [Globals & Predefined Skills](api/globals.html) | Strength of the current event/hit (0..1). |
| [`RULE`](api/actions/rule.html) | [Actions & Instructions](api/actions.html) | Assigns an arithmetic expression (numbers, skills, parentheses, + - * /) to a skill; clamped by MIN/MAX. Avoid factors < 0.01. |
| [`SAVE`](api/actions/save.html) | [Actions & Instructions](api/actions.html) | Saves the game under a name + number (.SAV) in SAVEDIR. |
| [`SAVE`](api/actor/save.html) | [Actors (ACTOR)](api/actor.html) | All Actor properties saved with the game (set automatically for Actors). |
| [`SAVE`](api/region/save.html) | [Regions (REGION)](api/region.html) | All region properties are saved with the game. |
| [`SAVE`](api/wall/save.html) | [Walls (WALL)](api/wall.html) | All wall properties are stored when the game is saved. |
| [`SAVE_INFO`](api/actions/save_info.html) | [Actions & Instructions](api/actions.html) | Like SAVE but stores only the GLOBAL skills. |
| [`SAVEDIR`](api/settings/savedir.html) | [Predefined Settings](api/settings.html) | Defines the directory in which saved games are stored. Created on first save if missing. |
| [`SCALE_XY`](api/texture/scale_xy.html) | [Textures (TEXTURE)](api/texture.html) | Scaling of the texture in pixels per Step, horizontally and vertically. Default 16 pixels/Step. No effect on sky textures. |
| [`SCREEN_HGT`](api/globals/screen_hgt.html) | [Globals & Predefined Skills](api/globals.html) | Height of the 3D window in pixels (even numbers). |
| [`SCREEN_WIDTH`](api/globals/screen_width.html) | [Globals & Predefined Skills](api/globals.html) | Width of the 3D window in pixels (steps of 16). |
| [`SCREEN_X`](api/globals/screen_x.html) | [Globals & Predefined Skills](api/globals.html) | Horizontal offset of the 3D window from the left edge (steps of 4). |
| [`SCREEN_Y`](api/globals/screen_y.html) | [Globals & Predefined Skills](api/globals.html) | Vertical offset of the 3D window from the top edge. |
| [`SCYCLES`](api/texture/scycles.html) | [Textures (TEXTURE)](api/texture.html) | Per-phase sound flags (0/1). Where 1, the texture sound plays during that phase. |
| [`SDIST`](api/texture/sdist.html) | [Textures (TEXTURE)](api/texture.html) | Critical distance in Steps below which the texture sound is audible; louder the closer you come. |
| [`SECS`](api/globals/secs.html) | [Globals & Predefined Skills](api/globals.html) | Increases by 1 every second. |
| [`SEEN`](api/actor/seen.html) | [Actors (ACTOR)](api/actor.html) | Set once seen by the player (used by the automap). |
| [`SEEN`](api/region/seen.html) | [Regions (REGION)](api/region.html) | Set once the region has been seen by the player. |
| [`SEEN`](api/wall/seen.html) | [Walls (WALL)](api/wall.html) | Set automatically once the wall has been seen (used by the automap). |
| [`SET`](api/actions/set.html) | [Actions & Instructions](api/actions.html) | Assigns a new value or keyword to any keyword/skill. Assigning NULL switches actions off; for FLAG keywords, 0 clears and 1 sets. |
| [`SHAKE`](api/actions/shake.html) | [Actions & Instructions](api/actions.html) | Tells an object its position/size changed; required after directly setting coordinates. |
| [`SHIFT_SENSE`](api/globals/shift_sense.html) | [Globals & Predefined Skills](api/globals.html) | Factor applied to input while [Shift] is held (default 2). |
| [`SHOOT`](api/actions/shoot.html) | [Actions & Instructions](api/actions.html) | Triggers IF_HIT on the nearest object in view (using SHOOT_FAC/RANGE/X/Y); sets HIT_DIST and RESULT. Also opens nearby switches/doors. |
| [`SHOOT_ANGLE`](api/globals/shoot_angle.html) | [Globals & Predefined Skills](api/globals.html) | Angle from a SHOOT object to the player (for aiming projectiles). |
| [`SHOOT_FAC`](api/globals/shoot_fac.html) | [Globals & Predefined Skills](api/globals.html) | Hit-strength factor for SHOOT/EXPLODE RESULT (0..1, default 1). |
| [`SHOOT_RANGE`](api/globals/shoot_range.html) | [Globals & Predefined Skills](api/globals.html) | Maximum SHOOT object distance in Steps (default 500). |
| [`SHOOT_SECTOR`](api/globals/shoot_sector.html) | [Globals & Predefined Skills](api/globals.html) | Angular sector an actor uses for SHOOT (default 2π). |
| [`SHOOT_X`](api/globals/shoot_x.html) | [Globals & Predefined Skills](api/globals.html) | Horizontal SHOOT deviation from the 3D-window centre (-1..1). |
| [`SHOOT_Y`](api/globals/shoot_y.html) | [Globals & Predefined Skills](api/globals.html) | Vertical SHOOT deviation from the 3D-window centre (-1..1). |
| [`SIDES`](api/texture/sides.html) | [Textures (TEXTURE)](api/texture.html) | Number of sides (1..64, default 1). The visible side changes with the viewing angle, giving Things/Actors a 3D appearance. Wall textures may have two sides. |
| [`SIZE_X`](api/actor/size_x.html) | [Actors (ACTOR)](api/actor.html) | Horizontal size of the object in Steps (from the texture). Read-only. |
| [`SIZE_Y`](api/actor/size_y.html) | [Actors (ACTOR)](api/actor.html) | Vertical size of the object in Steps (from the texture). Read-only. |
| [`SKILL`](api/globals/skill.html) | [Globals & Predefined Skills](api/globals.html) | Defines a skill (TYPE, VAL, MIN, MAX). |
| [`SKILL1...SKILL8`](api/actor/skill1_skill8.html) | [Actors (ACTOR)](api/actor.html) | Eight universal parameters; changed/evaluated in actions. |
| [`SKILL1...SKILL8`](api/region/skill1_skill8.html) | [Regions (REGION)](api/region.html) | Eight universal parameters; changed/evaluated in actions. |
| [`SKILL1...SKILL8`](api/wall/skill1_skill8.html) | [Walls (WALL)](api/wall.html) | Eight universal parameters with no built-in effect; changed and evaluated in actions. |
| [`SKIP`](api/actions/skip.html) | [Actions & Instructions](api/actions.html) | Relative jump: skips the given number of instructions (negative = backward). |
| [`SKY`](api/texture/sky.html) | [Textures (TEXTURE)](api/texture.html) | The texture uses parallax (not perspective) projection — treated as a background (mountains, sky, horizon) at infinite distance, not zoomed. |
| [`SLIDEDOOR`](api/wall/slidedoor.html) | [Walls (WALL)](api/wall.html) | The wall can be shifted sideways via POSITION. |
| [`SLOOP`](api/texture/sloop.html) | [Textures (TEXTURE)](api/texture.html) | The texture sound plays continuously in a loop, independent of the animation phase. |
| [`SLOPE_AHEAD`](api/globals/slope_ahead.html) | [Globals & Predefined Skills](api/globals.html) | Floor slope in the view direction (height gain per Step). |
| [`SOUND`](api/files/sound.html) | [Files](api/files.html) | Assigns a sound file (`.VOC` or `.WAV`) to the keyword. |
| [`SOUND`](api/texture/sound.html) | [Textures (TEXTURE)](api/texture.html) | Keyword of a sound file assigned to the texture. Plays rhythmically on floors when walking, or continuously (with SLOOP) on ceilings. |
| [`SOUND_VOL`](api/globals/sound_vol.html) | [Globals & Predefined Skills](api/globals.html) | Global sound-effect volume (0..1). |
| [`SPEED`](api/actor/speed.html) | [Actors (ACTOR)](api/actor.html) | Horizontal speed in Steps per Tick (default 0). |
| [`STEPS`](api/globals/steps.html) | [Globals & Predefined Skills](api/globals.html) | Increases with the distance the player walks. |
| [`STICK`](api/actor/stick.html) | [Actors (ACTOR)](api/actor.html) | Fixes the Actor at its current offset to the player and moves with it. |
| [`STOP_FLIC`](api/actions/stop_flic.html) | [Actions & Instructions](api/actions.html) | Stops the currently playing flic. |
| [`STRING`](api/ui/string.html) | [Panels, Texts & Overlays](api/ui.html) | The text content (predefined string keyword); `\n` = line break, `\"` = quote; NULL = no text. |
| [`SVOL`](api/texture/svol.html) | [Textures (TEXTURE)](api/texture.html) | Maximum sound volume (0..1). Default 0.5. |
| [`TARGET`](api/actor/target.html) | [Actors (ACTOR)](api/actor.html) | Assigns a new target or behaviour (see the TARGET values: NULL, MOVE, BULLET, STICK, FOLLOW, REPEL, a Way, or another object). |
| [`TEXT`](api/ui/text.html) | [Panels, Texts & Overlays](api/ui.html) | Defines a text display inside the 3D window (messages, dialogue). |
| [`TEXTURE`](api/actor/texture.html) | [Actors (ACTOR)](api/actor.html) | One- or eight-sided texture; the visible side follows the viewing angle. |
| [`TEXTURE`](api/texture/texture.html) | [Textures (TEXTURE)](api/texture.html) | Defines a texture object. |
| [`TEXTURE`](api/wall/texture.html) | [Walls (WALL)](api/wall.html) | Texture for both sides of the wall. Two-sided textures switch depending on which vertex (#1 or #2) the wall is viewed from. |
| [`THERE`](api/synonyms/there.html) | [Synonyms](api/synonyms.html) | The region that triggered the action, or that contains the triggering object. |
| [`THING`](api/thing/thing.html) | [Things (THING)](api/thing.html) | Defines a Thing. All property, flag and event keywords are identical to those of [ACTOR](../actor/). |
| [`TICKS`](api/globals/ticks.html) | [Globals & Predefined Skills](api/globals.html) | Increases by 1 every 1/16 second. |
| [`TIME_CORR`](api/globals/time_corr.html) | [Globals & Predefined Skills](api/globals.html) | Time-correction factor (1.0 at 16 fps; lower at higher fps). |
| [`TIME_FAC`](api/globals/time_fac.html) | [Globals & Predefined Skills](api/globals.html) | Reciprocal of TIME_CORR (higher on faster machines). |
| [`TRANSPARENT`](api/wall/transparent.html) | [Walls (WALL)](api/wall.html) | Colour 0 in the texture is transparent (grilles, fences); the wall can be penetrated by SHOOT. Same region both sides. |
| [`TYPE`](api/globals/type.html) | [Globals & Predefined Skills](api/globals.html) | Skill kind: LOCAL, GLOBAL or PLAYER. GLOBAL skills survive level reloads; default LOCAL. |
| [`VAL`](api/globals/val.html) | [Globals & Predefined Skills](api/globals.html) | Initial value of the skill (default 0). |
| [`VBAR`](api/ui/vbar.html) | [Panels, Texts & Overlays](api/ui.html) | Vertical bar gauge: the bitmap is shifted by skill×fac. Up to 16 bars per panel. |
| [`VIDEO`](api/settings/video.html) | [Predefined Settings](api/settings.html) | Sets the screen resolution. Predefined resolution keywords: `320x200`, `X320x240`, `X320x400`. Newer engine versions add SVGA modes `S640x480` and `S800x600`. |
| [`VISIBLE`](api/actor/visible.html) | [Actors (ACTOR)](api/actor.html) | Set automatically while the object is visible. |
| [`VISIBLE`](api/region/visible.html) | [Regions (REGION)](api/region.html) | Set while the floor, ceiling or a back wall of the region is visible. |
| [`VISIBLE`](api/wall/visible.html) | [Walls (WALL)](api/wall.html) | Set automatically while the wall is visible; can be evaluated in actions. |
| [`VSPEED`](api/actor/vspeed.html) | [Actors (ACTOR)](api/actor.html) | Vertical speed in Steps per Tick (default 0). |
| [`WAIT`](api/actions/wait.html) | [Actions & Instructions](api/actions.html) | (EACH_TICK actions) Pauses the action for the given number of image cycles. |
| [`WAITT`](api/actions/waitt.html) | [Actions & Instructions](api/actions.html) | Pauses the action for the given number of Ticks (fixed time). |
| [`WALK`](api/globals/walk.html) | [Globals & Predefined Skills](api/globals.html) | Current deflection of the walking movement (-1..1). |
| [`WALK_PERIOD`](api/globals/walk_period.html) | [Globals & Predefined Skills](api/globals.html) | Steps per period of the distance-based walk bob (default 4). |
| [`WALK_TIME`](api/globals/walk_time.html) | [Globals & Predefined Skills](api/globals.html) | Time constant for WALK movement (default 4 Ticks). |
| [`WALL`](api/wall/wall.html) | [Walls (WALL)](api/wall.html) | Defines a wall type that can be assigned to a connecting line in WED. |
| [`WAVE`](api/globals/wave.html) | [Globals & Predefined Skills](api/globals.html) | Current deflection of the time-based movement (-1..1). |
| [`WAVE_PERIOD`](api/globals/wave_period.html) | [Globals & Predefined Skills](api/globals.html) | Ticks per period of the time-based player sway (default 16). |
| [`WAY`](api/way/way.html) | [Ways (WAY)](api/way.html) | Defines a Way; the waypoint list is assigned in WED. No collision detection unless the Actor flag CAREFULLY is set. |
| [`WAYPOINT`](api/actor/waypoint.html) | [Actors (ACTOR)](api/actor.html) | Sets a position point (1..32) of the Actor's Way as target; readable as the next waypoint number. |
| [`WAYPOINT`](api/way/waypoint.html) | [Ways (WAY)](api/way.html) | Current/target waypoint number (1..32) of an Actor on its Way. |
| [`X, Y, Z`](api/actor/x_y_z.html) | [Actors (ACTOR)](api/actor.html) | Vertex position of the object (set by direct name). |
| [`X1, Y1, Z1`](api/wall/x1_y1_z1.html) | [Walls (WALL)](api/wall.html) | Position of vertex 1 of the wall (read by direct name; `MY` synonyms not allowed). |
| [`X2, Y2, Z2`](api/wall/x2_y2_z2.html) | [Walls (WALL)](api/wall.html) | Position of vertex 2 of the wall. |
