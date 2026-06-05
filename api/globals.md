---
layout: default
title: Globals & Predefined Skills
parent: API Reference
has_children: true
nav_order: 11
---

# Globals & Predefined Skills

Skills are numeric properties (like variables) belonging to the player and objects. Below is the SKILL definition and the predefined skills, grouped by purpose. Skills marked read-only are computed by the engine.

| Keyword | Source | Summary |
|:--------|:------:|:--------|
| [`SKILL`](globals/skill.html) | both | Defines a skill (TYPE, VAL, MIN, MAX). |
| [`TYPE`](globals/type.html) | both | Skill kind: LOCAL, GLOBAL or PLAYER. GLOBAL skills survive level reloads; default LOCAL. |
| [`VAL`](globals/val.html) | both | Initial value of the skill (default 0). |
| [`MIN`](globals/min.html) | both | Lower limit of the skill value. |
| [`MAX`](globals/max.html) | both | Upper limit of the skill value. |
| [`SCREEN_WIDTH`](globals/screen_width.html) | both | Width of the 3D window in pixels (steps of 16). |
| [`SCREEN_HGT`](globals/screen_hgt.html) | both | Height of the 3D window in pixels (even numbers). |
| [`SCREEN_X`](globals/screen_x.html) | both | Horizontal offset of the 3D window from the left edge (steps of 4). |
| [`SCREEN_Y`](globals/screen_y.html) | both | Vertical offset of the 3D window from the top edge. |
| [`ASPECT`](globals/aspect.html) | both | Height-to-width ratio of the 3D view (0.1..10, default 1). |
| [`MOTION_BLUR`](globals/motion_blur.html) | both | Motion-blur amount (0..1); lowers resolution during movement for smoother motion. |
| [`RENDER_MODE`](globals/render_mode.html) | both | Render activity: 2 = full redraw, 1 = partial, 0.5 = normal, 0 = none. Auto-resets to 0.5. |
| [`MOVE_MODE`](globals/move_mode.html) | both | Freezes movement/actions: 1 normal, 0.5 stop actors, 0 stop player+events, -0.5 stop global ticks. |
| [`MAP_MAXX`](globals/map_maxx.html) | both | Largest X coordinate of the map (read-only). |
| [`MAP_MINX`](globals/map_minx.html) | both | Smallest X coordinate of the map (read-only). |
| [`MAP_MAXY`](globals/map_maxy.html) | both | Largest Y coordinate of the map (read-only). |
| [`MAP_MINY`](globals/map_miny.html) | both | Smallest Y coordinate of the map (read-only). |
| [`MAP_SCALE`](globals/map_scale.html) | both | Map display scale relative to the 3D window (default 0.9; 1 = fits exactly). |
| [`MAP_MODE`](globals/map_mode.html) | both | Map display mode (0 off; >0 shows the map; the value 2 reveals all objects). |
| [`MAP_LAYER`](globals/map_layer.html) | both | Overlay layer the map appears on (0..16). |
| [`SOUND_VOL`](globals/sound_vol.html) | both | Global sound-effect volume (0..1). |
| [`MUSIC_VOL`](globals/music_vol.html) | both | Music volume (0..1; 0 switches music off). |
| [`PLAYER_LIGHT`](globals/player_light.html) | both | Strength of the light the player carries (0..1). |
| [`LIGHT_DIST`](globals/light_dist.html) | both | Distance where the shading range begins (default 10 Steps). |
| [`DARK_DIST`](globals/dark_dist.html) | both | Distance of the darkness boundary; recomputed from PLAYER_LIGHT. |
| [`PLAYER_WIDTH`](globals/player_width.html) | both | Minimum distance of the player to walls/objects (default 1.2 Steps). |
| [`PLAYER_SIZE`](globals/player_size.html) | both | Distance between the player's feet and eyes (default 3 Steps). |
| [`PLAYER_CLIMB`](globals/player_climb.html) | both | Maximum step-up height when changing region (default 1.5 Steps). |
| [`WALK_PERIOD`](globals/walk_period.html) | both | Steps per period of the distance-based walk bob (default 4). |
| [`WALK_TIME`](globals/walk_time.html) | both | Time constant for WALK movement (default 4 Ticks). |
| [`WAVE_PERIOD`](globals/wave_period.html) | both | Ticks per period of the time-based player sway (default 16). |
| [`WALK`](globals/walk.html) | both | Current deflection of the walking movement (-1..1). |
| [`WAVE`](globals/wave.html) | both | Current deflection of the time-based movement (-1..1). |
| [`PSOUND_VOL`](globals/psound_vol.html) | both | Relative player (footstep) sound volume (0..2). |
| [`PSOUND_TONE`](globals/psound_tone.html) | both | Pitch of the player (footstep) sound (0..4). |
| [`PLAYER_VX`](globals/player_vx.html) | both | Player velocity along X (Steps/Step); changing it moves the player with collision. |
| [`PLAYER_VY`](globals/player_vy.html) | both | Player velocity along Y. |
| [`PLAYER_VZ`](globals/player_vz.html) | both | Player velocity along Z (vertical). |
| [`PLAYER_VROT`](globals/player_vrot.html) | both | Rotation speed of the view angle (radians/Tick). |
| [`PLAYER_TILT`](globals/player_tilt.html) | both | Tangent of the vertical view angle (look up/down). |
| [`PLAYER_ARC`](globals/player_arc.html) | both | Focal length / field of view in radians (0.2..2.0, default 1 ≈ 60°). |
| [`FRICTION`](globals/friction.html) | both | Friction coefficient for ACCEL (0..1, default 0.5). |
| [`INERTIA`](globals/inertia.html) | both | Inertia coefficient for ACCEL (0..1, default 1). |
| [`SHOOT_RANGE`](globals/shoot_range.html) | both | Maximum SHOOT object distance in Steps (default 500). |
| [`SHOOT_FAC`](globals/shoot_fac.html) | both | Hit-strength factor for SHOOT/EXPLODE RESULT (0..1, default 1). |
| [`SHOOT_X`](globals/shoot_x.html) | both | Horizontal SHOOT deviation from the 3D-window centre (-1..1). |
| [`SHOOT_Y`](globals/shoot_y.html) | both | Vertical SHOOT deviation from the 3D-window centre (-1..1). |
| [`HIT_DIST`](globals/hit_dist.html) | both | Distance to the last object hit by SHOOT/EXPLODE (0 if none). |
| [`INV_DIST`](globals/inv_dist.html) | old | Reciprocal of the SHOOT hit distance. |
| [`RESULT`](globals/result.html) | both | Strength of the current event/hit (0..1). |
| [`PLAYER_X`](globals/player_x.html) | both | Player X position (no collision when set directly). |
| [`PLAYER_Y`](globals/player_y.html) | both | Player Y position (no collision when set directly). |
| [`PLAYER_Z`](globals/player_z.html) | both | Player eye height in Steps (no collision when set directly). |
| [`PLAYER_ANGLE`](globals/player_angle.html) | both | Horizontal view direction in radians (0 = +X axis = east). |
| [`PLAYER_SIN`](globals/player_sin.html) | both | Sine of the player's view angle (for movement rules). |
| [`PLAYER_COS`](globals/player_cos.html) | both | Cosine of the player's view angle. |
| [`PLAYER_SPEED`](globals/player_speed.html) | both | Speed component along the view direction (negative when reversing). |
| [`ACCELERATION`](globals/acceleration.html) | both | Acceleration along the view direction. |
| [`PLAYER_HGT`](globals/player_hgt.html) | both | Player feet height above/below the region floor (PLAYER_Z − PLAYER_SIZE − FLOOR_HGT). |
| [`FLOOR_HGT`](globals/floor_hgt.html) | both | Actual floor height at the player position (slope-aware). |
| [`CEIL_HGT`](globals/ceil_hgt.html) | both | Actual ceiling height at the player position. |
| [`IMPACT_VX`](globals/impact_vx.html) | both | Collision velocity change along X; auto-increased on collision, reset manually (pinball effect). |
| [`IMPACT_VY`](globals/impact_vy.html) | both | Collision velocity change along Y. |
| [`IMPACT_VZ`](globals/impact_vz.html) | both | Collision velocity change along Z (floor/ceiling). |
| [`SLOPE_AHEAD`](globals/slope_ahead.html) | both | Floor slope in the view direction (height gain per Step). |
| [`NODE`](globals/node.html) | both | Current node number in multiplayer games (from the command line). |
| [`RANDOM`](globals/random.html) | both | Random number 0..1, changing each frame. |
| [`TIME_CORR`](globals/time_corr.html) | both | Time-correction factor (1.0 at 16 fps; lower at higher fps). |
| [`TIME_FAC`](globals/time_fac.html) | both | Reciprocal of TIME_CORR (higher on faster machines). |
| [`TICKS`](globals/ticks.html) | both | Increases by 1 every 1/16 second. |
| [`SECS`](globals/secs.html) | both | Increases by 1 every second. |
| [`STEPS`](globals/steps.html) | both | Increases with the distance the player walks. |
| [`MOUSE_LEFT`](globals/mouse_left.html) | both | State of the left mouse / joystick button 1 (0/1). |
| [`MOUSE_MIDDLE`](globals/mouse_middle.html) | both | State of the middle mouse / joystick button 3. |
| [`MOUSE_RIGHT`](globals/mouse_right.html) | both | State of the right mouse / joystick button 2. |
| [`JOY_4`](globals/joy_4.html) | both | State of joystick button 4. |
| [`KEY_F1...KEY_Z`](globals/key_f1_key_z.html) | both | Key-state skills (0/1): KEY_F1..KEY_F12, KEY_ESC, KEY_TAB, KEY_SHIFT, KEY_CTRL, KEY_ALT, KEY_SPACE, KEY_BKSP, KEY_CUU/CUD/CUR/CUL, KEY_PGUP, KEY_PGDN, KEY_HOME, KEY_END, KEY_INS, KEY_DEL, KEY_PAUSE, KEY_CAR, KEY_CAL, KEY_PLUS, KEY_MINUS, KEY_ENTER, KEY_0..KEY_9, KEY_A..KEY_Z. |
| [`FORCE_AHEAD`](globals/force_ahead.html) | both | Analog forward/backward input (-1..1). |
| [`FORCE_STRAFE`](globals/force_strafe.html) | both | Analog left/right (strafe) input. |
| [`FORCE_ROT`](globals/force_rot.html) | both | Analog horizontal rotation input. |
| [`FORCE_TILT`](globals/force_tilt.html) | both | Analog look up/down input. |
| [`FORCE_UP`](globals/force_up.html) | both | Analog vertical (duck/jump) input. |
| [`KEY_SENSE`](globals/key_sense.html) | both | Keyboard movement sensitivity (default 0.7). |
| [`SHIFT_SENSE`](globals/shift_sense.html) | both | Factor applied to input while [Shift] is held (default 2). |
| [`MOUSE_SENSE`](globals/mouse_sense.html) | both | Mouse movement sensitivity (default 1). |
| [`JOY_SENSE`](globals/joy_sense.html) | both | Joystick movement sensitivity (default 1). |
| [`ERROR`](globals/error.html) | both | Error code for the current frame (WRUN.EXE only): 0 none, 1 CLIP_DIST too small, 3 NEXUS too small, 5 missing bitmap, 6 missing region/texture, 8 bad synonym, 9 missing region. |
| [`DEBUG_MODE`](globals/debug_mode.html) | both | If 1, halts after each image build until 'S' is pressed (WRUN.EXE only). |
| [`ACTIVE_NEXUS`](globals/active_nexus.html) | both | Nexus utilisation (WRUN.EXE only). |
| [`ACTIVE_TARGETS`](globals/active_targets.html) | both | Number of actors with a TARGET (WRUN.EXE only). |
| [`ACTIVE_OBJTICKS`](globals/active_objticks.html) | both | Number of objects with running EACH_TICK actions (WRUN.EXE only). |
| [`ACTIVE_REGTICKS`](globals/active_regticks.html) | old | Number of regions with running EACH_TICK actions (WRUN.EXE only). |
| [`SHOOT_ANGLE`](globals/shoot_angle.html) | new | Angle from a SHOOT object to the player (for aiming projectiles). |
| [`SHOOT_SECTOR`](globals/shoot_sector.html) | new | Angular sector an actor uses for SHOOT (default 2π). |
| [`HIT_X`](globals/hit_x.html) | new | X pixel coordinate of the texture pixel hit by SHOOT (for bullet-hole ATTACH). |
| [`HIT_Y`](globals/hit_y.html) | new | Y pixel coordinate of the texture pixel hit by SHOOT. |
| [`HIT_MINDIST`](globals/hit_mindist.html) | both | Distance to the nearest object hit by EXPLODE (0 if none in range). |
| [`CD_TRACK`](globals/cd_track.html) | new | Number of the CD-audio track currently playing (0 if stopped). |
