#!/usr/bin/env python3
import os, re, shutil

import os
ROOT = os.path.dirname(os.path.abspath(__file__))
API = os.path.join(ROOT, "api")

def slug(s):
    s = s.lower()
    s = s.replace("...", "_").replace("…","_")
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s or "x"

def write(path, fm, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write("---\n")
        for k, v in fm:
            f.write(f"{k}: {v}\n")
        f.write("---\n\n")
        f.write(body.rstrip() + "\n")


# ---- Data model ----------------------------------------------------------
# Each category: (slug, title, nav, summary, intro_md, [keywords])
# Each keyword: dict(name, sig, src, desc, note(optional), removed(optional True))

CATS = []

def cat(slug_, title, summary, intro, keywords):
    CATS.append(dict(slug=slug_, title=title, summary=summary, intro=intro, kws=keywords))

def K(name, sig, src, desc, note=None, removed=False):
    return dict(name=name, sig=sig, src=src, desc=desc, note=note, removed=removed)

# 1. SETTINGS -------------------------------------------------------------
cat("settings", "Predefined Settings",
 "Global engine settings, normally placed at the start of the main WDL file.",
 "These predefined keywords define the basic settings for graphics, sounds and directories. They normally stand at the beginning of the main WDL file.",
 [
  K("VIDEO","Keyword;","both","Sets the screen resolution. Predefined resolution keywords: `320x200`, `X320x240`, `X320x400`. Newer engine versions add SVGA modes `S640x480` and `S800x600`.",
    "The 1995 book prints the first keyword as `X320x200`; the correct keyword is `320x200` (no prefix)."),
  K("NEXUS","Number;","both","Sets the size of the Nexus — the internal data structure used for rendering. Depends on the maximum number of objects, walls and regions visible at once. Default 14. Too small a Nexus produces image errors signalled by the PC speaker."),
  K("CLIP_DIST","Number;","both","Global view distance in Steps. Walls and objects entirely beyond this distance from the player are not rendered. Default 1000. Can be overridden per region."),
  K("IBANK","<Filename>;","both","Loads the instrument bank (an ADLIB `.IBK` instrument file) used for MIDI songs."),
  K("DRUMBANK","<Filename>;","both","Loads the percussion instrument bank (played on MIDI channel 10). If omitted, internally defined general-MIDI instruments are used."),
  K("MIDI_PITCH","Number;","both","Number of octaves by which the pitch-bend parameter changes the pitch in MIDI songs. Range 1..12, default 2."),
  K("INCLUDE","<Filename>;","both","Reads further WDL definitions from a separate file and then continues with the original file. INCLUDEs may not be nested."),
  K("BIND","<Filename>;","both","Binds the given file into the game so it is compiled in (e.g. for level changes). Any number of BIND files may be given."),
  K("MAPFILE","<Filename>;","both","Defines the associated WMP topography file. Must stand in the main WDL and cannot be read via INCLUDE."),
  K("SAVEDIR","<Dirname>;","both","Defines the directory in which saved games are stored. Created on first save if missing."),
  K("PATH","<Dirname>;","both","Additional search path for bitmap or sound files (searched after the current directory). Up to 8 PATH keywords, searched in order."),
 ])

# 2. FILES ----------------------------------------------------------------
cat("files", "Files",
 "Keywords that assign external files (bitmaps, sounds, songs, animations) to a name.",
 "Files are assigned to keywords to define bitmaps, animations, sounds and songs. Names of files belonging to the finished level (to be compiled in) are given between angle brackets `<...>`.",
 [
  K("BMAP","Keyword, <Filename> [, x, y, dx, dy];","both","Assigns a bitmap (`.PCX`, `.LBM` or `.BBM`) to the keyword, or a rectangular section of it (upper-left corner `x,y`, size `dx,dy`, in pixels)."),
  K("OVLY","Keyword, <Filename> [, x, y, dx, dy];","both","Like BMAP, but defines an overlay bitmap (for cockpits, weapons, mouse pointers). Occupies more memory but draws faster. Horizontal size must be divisible by 4."),
  K("FONT","Keyword, <Filename>, width, height;","both","Assigns a character set. `width,height` is the size of a single character in pixels; character order follows the ASCII set."),
  K("SOUND","Keyword, <Filename>;","both","Assigns a sound file (`.VOC` or `.WAV`) to the keyword."),
  K("MUSIC","Keyword, <Filename>;","both","Assigns a song file (`.MID`) to the keyword."),
  K("FLIC","Keyword, <Filename>;","both","Assigns an animation file (`.FLI` or `.FLC`) to the keyword."),
 ])

# 3. PALETTE --------------------------------------------------------------
cat("palette", "Palettes",
 "Definition of the 256-colour palette, shading ranges and colour animations.",
 "A palette loads a 256-colour palette from a graphics file and defines the shading ranges and colour animations.",
 [
  K("PALETTE","Keyword { ... };","both","Defines a palette. Contains, in order, the keyword assignments below."),
  K("PALFILE","<Filename>;","both","Graphics file whose colours are used for the base palette. Colours 0 and 1 carry the colour for infinite distance (black indoors / foggy white outdoors)."),
  K("RANGE","s, l;","both","Defines a shading range used for distance shading: start colour number `s` (1..254) and number of colours `l` (up to 64). Up to 24 ranges. Colours outside any range are not shaded (useful for light sources)."),
  K("HARD","(FLAGS HARD;)","both","Performs shading 'hard' — colours are shifted rather than recalculated, keeping texture detail more recognisable."),
 ])

# 4. TEXTURE --------------------------------------------------------------
cat("texture", "Textures (TEXTURE)",
 "The TEXTURE object and its properties, flags, sound and animation parameters.",
 "Textures determine the appearance of the world (walls, floors, ceilings, backgrounds, Things, Actors, panels and overlays). A texture definition contains, in order, the keyword assignments below.",
 [
  K("TEXTURE","Keyword { ... };","both","Defines a texture object."),
  K("SCALE_XY","x, y;","both","Scaling of the texture in pixels per Step, horizontally and vertically. Default 16 pixels/Step. No effect on sky textures."),
  K("SIDES","Number;","both","Number of sides (1..64, default 1). The visible side changes with the viewing angle, giving Things/Actors a 3D appearance. Wall textures may have two sides."),
  K("CYCLES","Number;","both","Number of animation phases (1..64, default 1). `SIDES * CYCLES` may not exceed 64. If omitted, the texture is not animated."),
  K("BMAPS","Bitmap1, Bitmap2, …;","both","List of up to 64 bitmap keywords (count = `SIDES * CYCLES`). Front-side phases first, then further sides clockwise."),
  K("DELAY","Number, …;","both","Per-phase animation durations in Ticks (1..31). Count = CYCLES. Default one Tick per phase."),
  K("SCYCLES","Flag, …;","both","Per-phase sound flags (0/1). Where 1, the texture sound plays during that phase."),
  K("MIRROR","Flag, …;","both","Per-side mirror flags (0/1). Where 1, that side's bitmaps are mirrored horizontally."),
  K("RANDOM","Number;","both","Maximum value (0..1) of a random delay factor added to each animation phase."),
  K("AMBIENT","Number;","both","Luminosity of the texture (-1..1, 32 steps, default 0). 1 = self-illuminated; negative values reduce reflectivity (for painted-in shadows)."),
  K("SOUND","Sound;","both","Keyword of a sound file assigned to the texture. Plays rhythmically on floors when walking, or continuously (with SLOOP) on ceilings."),
  K("SVOL","Number;","both","Maximum sound volume (0..1). Default 0.5."),
  K("SDIST","Number;","both","Critical distance in Steps below which the texture sound is audible; louder the closer you come."),
  K("ONESHOT","(flag)","both","The texture is not permanently animated; it shows the first phase and animates one cycle when the object's PLAY flag is set."),
  K("SKY","(flag)","both","The texture uses parallax (not perspective) projection — treated as a background (mountains, sky, horizon) at infinite distance, not zoomed."),
  K("SLOOP","(flag)","both","The texture sound plays continuously in a loop, independent of the animation phase."),
  K("CYCLE","n;","both","Current animation phase of the texture (can be read/set in actions)."),
  K("BLUR","Number;","new","Motion-blur / transparency amount for the texture (newer engine).",None),
 ])

# 5. WALL -----------------------------------------------------------------
cat("wall", "Walls (WALL)",
 "The WALL object: vertical surfaces separating regions, with textures, parameters, events and flags.",
 "Vertical Walls run along the connecting lines between two vertices and separate regions. A wall definition contains, in order, the keyword assignments below; events and flags can also be read/changed from actions.",
 [
  K("WALL","Keyword { ... };","both","Defines a wall type that can be assigned to a connecting line in WED."),
  K("TEXTURE","Texture;","both","Texture for both sides of the wall. Two-sided textures switch depending on which vertex (#1 or #2) the wall is viewed from."),
  K("OFFSET_X","Number;","both","Shifts the wall texture left by the given number of pixels. Cannot be combined with the WED ALIGN function."),
  K("OFFSET_Y","Number;","both","Shifts the wall texture down by the given number of pixels. For sky textures, sets the horizon distance from the bottom of the bitmap."),
  K("CYCLE","n;","both","Current animation phase of the wall texture."),
  K("POSITION","Number;","both","Meaning depends on the flags (e.g. lateral position for SLIDEDOOR, edge alignment for PORTCULLIS)."),
  K("MAP_COLOR","n;","both","Mode (0..1, default 1) for drawing the wall on the map. 0 = not drawn."),
  K("DIST","Number;","both","Base/boundary distance of the wall (default 0). Exceeding it can trigger an IF_NEAR action."),
  K("SKILL1...SKILL8","Number;","both","Eight universal parameters with no built-in effect; changed and evaluated in actions."),
  K("DISTANCE","Number;","both","Distance of the player to the nearest wall vertex (approximate, error up to 20%). Read-only.", removed=False),
  K("X1, Y1, Z1","Number;","both","Position of vertex 1 of the wall (read by direct name; `MY` synonyms not allowed)."),
  K("X2, Y2, Z2","Number;","both","Position of vertex 2 of the wall."),
  K("IF_NEAR","Action;","both","Triggered when the player approaches the nearest wall vertex within the boundary distance (DIST); if no DIST, on every contact."),
  K("IF_FAR","Action;","both","Triggered when the player moves away beyond the boundary distance (DIST)."),
  K("IF_HIT","Action;","both","Triggered when the wall is hit by SHOOT/EXPLODE or struck head-on by a flying object (see BULLET, FRAGILE)."),
  K("EACH_CYCLE","Action;","both","Triggered after each texture animation cycle (or end of a ONESHOT animation)."),
  K("EACH_TICK","Action;","both","Triggered after each image build (~1/16 s)."),
  K("INVISIBLE","(flag)","both","Wall is invisible but still blocks the player. Same region must be on both sides."),
  K("PASSABLE","(flag)","both","Wall is passable for the player. Same region must be on both sides."),
  K("VISIBLE","(flag)","both","Set automatically while the wall is visible; can be evaluated in actions."),
  K("SEEN","(flag)","both","Set automatically once the wall has been seen (used by the automap)."),
  K("BERKELEY","(flag)","both","Wall is only active while seen or near its boundary distance — saves time with many animated/sound walls."),
  K("TRANSPARENT","(flag)","both","Colour 0 in the texture is transparent (grilles, fences); the wall can be penetrated by SHOOT. Same region both sides."),
  K("PLAY","(flag)","both","Animates the wall texture for one cycle (texture must be ONESHOT); auto-resets, may trigger EACH_CYCLE."),
  K("PORTCULLIS","(flag)","both","Attaches the texture to the wall's upper/lower edge (lifts, trapdoors); aligned by POSITION (0 = bottom, 1 = top)."),
  K("SLIDEDOOR","(flag)","old","The wall can be shifted sideways via POSITION.", note="Removed under this name in newer versions (use POSITION directly).", removed=True),
  K("FRAGILE","(flag)","both","The IF_HIT action can be triggered by an EXPLODE instruction."),
  K("FAR","(flag)","both","The wall stays visible beyond CLIP_DIST."),
  K("SAVE","(flag)","both","All wall properties are stored when the game is saved."),
  K("FLAG1...FLAG8","(flags)","both","Eight universal flags with no built-in effect; changed/evaluated in actions."),
  K("FENCE","(flag)","new","Newer single-sided transparent wall flag (allows simpler rendering, like a one-sided TRANSPARENT)."),
 ])

# 6. REGION ---------------------------------------------------------------
cat("region", "Regions (REGION)",
 "The REGION object: floor/ceiling areas bounded by walls, with textures, lighting and events.",
 "Regions are sections of the playing field bounded by polygons (walls). A region definition contains, in order, the keyword assignments below.",
 [
  K("REGION","Keyword { ... };","both","Defines a region type that can be assigned to an actual region in WED."),
  K("FLOOR_TEX","Texture;","both","Texture of the region floor. Its sound plays when stepped on; pitch/volume changeable by skills."),
  K("CEIL_TEX","Texture;","both","Texture of the region ceiling. Its sound plays on entering; continuous with SLOOP."),
  K("FLOOR_HGT","Number;","both","Height of the region floor in Steps."),
  K("CEIL_HGT","Number;","both","Height of the region ceiling in Steps."),
  K("FLOOR_OFFS_X","Number;","both","Floor texture shift along X (pixels, relative to field origin)."),
  K("FLOOR_OFFS_Y","Number;","both","Floor texture shift along Y."),
  K("CEIL_OFFS_X","Number;","both","Ceiling texture shift along X."),
  K("CEIL_OFFS_Y","Number;","both","Ceiling texture shift along Y."),
  K("AMBIENT","Number;","both","Base brightness of the region (0..1, 16 steps). Added to self-illuminating texture ambient."),
  K("CLIP_DIST","Number;","both","Per-region view distance in Steps (default 1000); speeds rendering in complex levels."),
  K("SKILL1...SKILL8","Number;","both","Eight universal parameters; changed/evaluated in actions."),
  K("FLOOR_LIFTED","(flag)","both","Raises floor corner points by the Z values of their vertices (tilted surfaces)."),
  K("CEIL_LIFTED","(flag)","both","Raises ceiling corner points by the Z values of their vertices."),
  K("VISIBLE","(flag)","both","Set while the floor, ceiling or a back wall of the region is visible."),
  K("SEEN","(flag)","both","Set once the region has been seen by the player."),
  K("SAVE","(flag)","both","All region properties are saved with the game."),
  K("HERE","(flag)","both","Set automatically while the player is in this region."),
  K("PLAY","(flag)","both","Animates floor/ceiling textures one cycle (textures must be ONESHOT)."),
  K("FLAG1...FLAG8","(flags)","both","Eight universal flags; changed/evaluated in actions."),
  K("IF_ENTER","Action;","both","Triggered when the player enters the region."),
  K("IF_LEAVE","Action;","both","Triggered when the player leaves the region."),
  K("IF_DIVE","Action;","both","Triggered when the player's eye height reaches or falls below the floor height."),
  K("IF_ARISE","Action;","both","Triggered when the player's eye height reaches or exceeds the ceiling height."),
  K("EACH_CYCLE","Action;","both","Triggered at the end of each texture animation cycle."),
  K("EACH_TICK","Action;","both","Triggered after each image build (~1/16 s)."),
 ])

# 7. ACTOR ----------------------------------------------------------------
cat("actor", "Actors (ACTOR)",
 "The ACTOR object: animate objects with movement, targets, events and flags. Things share these keywords.",
 "An Actor is an animate object — a linear automaton with definable action/reaction behaviour. A Thing differs only by lacking the complex behaviour, and uses the **same** definition keywords (see [Things](../thing/)). The definition contains, in order, the keyword assignments below.",
 [
  K("ACTOR","Keyword { ... };","both","Defines an Actor that can be placed anywhere in WED and optionally assigned a Way."),
  K("TEXTURE","Texture;","both","One- or eight-sided texture; the visible side follows the viewing angle."),
  K("CYCLE","n;","both","Current animation phase of the texture."),
  K("WAYPOINT","n;","both","Sets a position point (1..32) of the Actor's Way as target; readable as the next waypoint number."),
  K("TARGET","Keyword;","both","Assigns a new target or behaviour (see the TARGET values: NULL, MOVE, BULLET, STICK, FOLLOW, REPEL, a Way, or another object)."),
  K("NULL","(target)","both","TARGET NULL — the Actor does not move (default)."),
  K("MOVE","(target)","both","Moves straight ahead along ANGLE, using SPEED and VSPEED."),
  K("BULLET","(target)","both","Like MOVE, but triggers IF_HIT and sets RESULT=1 on impact (needs CAREFULLY for collision)."),
  K("STICK","(target)","both","Fixes the Actor at its current offset to the player and moves with it."),
  K("FOLLOW","(target)","both","Moves toward the player with SPEED, matching height with VSPEED."),
  K("REPEL","(target)","both","Moves away from the player; height unchanged."),
  K("HEIGHT","Number;","both","Height of the object, absolute (with GROUND) or relative to the region floor."),
  K("ANGLE","Number;","both","Angle in radians (0..6.28), added to the WMP angle; changeable by actions."),
  K("SPEED","Number;","both","Horizontal speed in Steps per Tick (default 0)."),
  K("VSPEED","Number;","both","Vertical speed in Steps per Tick (default 0)."),
  K("MAP_COLOR","n;","both","Colour number (0..255) for drawing on the map. 0 = not drawn, 1 = default colour."),
  K("DIST","Number;","both","Boundary distance (default 0); exceeding it can trigger IF_NEAR."),
  K("SKILL1...SKILL8","Number;","both","Eight universal parameters; changed/evaluated in actions."),
  K("DISTANCE","Number;","both","Distance of the player to the object centre (approximate). Read-only."),
  K("SIZE_X","Number;","both","Horizontal size of the object in Steps (from the texture). Read-only."),
  K("SIZE_Y","Number;","both","Vertical size of the object in Steps (from the texture). Read-only.", note="The 1995 book labels this `SIZE_Z`; the correct name is `SIZE_Y`."),
  K("RESULT","Number;","both","Result of SHOOT/EXPLODE on this object (0..1); reset explicitly after evaluation."),
  K("X, Y, Z","Number;","both","Vertex position of the object (set by direct name)."),
  K("REGION","Region;","both","Current region of the Actor; must be reassigned manually when the position is changed."),
  K("IF_NEAR","Action;","both","Triggered when the player approaches within DIST; if no DIST, on every contact."),
  K("IF_FAR","Action;","both","Triggered when the player moves beyond DIST."),
  K("IF_ARRIVED","Action;","both","Triggered on crossing a region boundary (with CAREFULLY) or reaching the next waypoint."),
  K("IF_HIT","Action;","both","Triggered when hit by SHOOT/EXPLODE or colliding head-on (see BULLET, FRAGILE)."),
  K("EACH_CYCLE","Action;","both","Triggered after each texture animation cycle."),
  K("EACH_TICK","Action;","both","Triggered after each image build (~1/16 s)."),
  K("INVISIBLE","(flag)","both","Object invisible and passable, as if absent; Actor does not move and no events fire. Auto-set for unplaced objects."),
  K("PASSABLE","(flag)","both","Object is passable for the player."),
  K("VISIBLE","(flag)","both","Set automatically while the object is visible."),
  K("BERKELEY","(flag)","both","Object inactive while unseen and beyond its boundary distance — saves time with many animated objects."),
  K("GROUND","(flag)","both","HEIGHT refers to the level's zero height rather than the region floor."),
  K("SEEN","(flag)","both","Set once seen by the player (used by the automap)."),
  K("PLAY","(flag)","both","Animates the texture one cycle (texture must be ONESHOT)."),
  K("FRAGILE","(flag)","both","IF_HIT can be triggered by EXPLODE."),
  K("CAREFULLY","(flag)","both","Performs collision detection along a path, avoiding walls/actors and adjusting height (unless GROUND). Costs time."),
  K("SAVE","(flag)","both","All Actor properties saved with the game (set automatically for Actors)."),
  K("FLAG1...FLAG8","(flags)","both","Eight universal flags; changed/evaluated in actions."),
  K("IMMATERIAL","(flag)","new","Object is not hit by SHOOT and does not collide (newer engine)."),
 ])

# 8. THING ----------------------------------------------------------------
cat("thing", "Things (THING)",
 "The THING object: simple inanimate objects sharing the ACTOR keyword set.",
 "A Thing is a simple inanimate object (tool, weapon, etc.) located at a single vertex. It differs from an Actor only by lacking complex action/reaction behaviour and uses the **same** definition keywords as the [Actor](../actor/) object.",
 [
  K("THING","Keyword { ... };","both","Defines a Thing. All property, flag and event keywords are identical to those of [ACTOR](../actor/)."),
 ])

# 9. WAY ------------------------------------------------------------------
cat("way", "Ways (WAY)",
 "The WAY object: lists of waypoints an Actor travels along.",
 "A Way is a list of up to 32 spatial points (waypoints). An Actor assigned a Way travels cyclically from one waypoint to the next.",
 [
  K("WAY","Keyword { ... };","both","Defines a Way; the waypoint list is assigned in WED. No collision detection unless the Actor flag CAREFULLY is set."),
  K("WAYPOINT","n;","both","Current/target waypoint number (1..32) of an Actor on its Way."),
 ])

# 10. ACTIONS -------------------------------------------------------------
cat("actions", "Actions & Instructions",
 "ACTION definitions, the instructions used inside them, and the global/event action keywords.",
 "Actions give objects the behaviour of linear automata. An action is a list of instructions executed one after another; many actions can run at once. Below are the ACTION keyword, the instructions usable inside actions, and the global/event keywords that trigger actions.",
 [
  K("ACTION","Keyword { ... };","both","Defines an action — a list of the instructions below."),
  K("SET","[Obj.]Key, Number/[Obj.]Key2;","both","Assigns a new value or keyword to any keyword/skill. Assigning NULL switches actions off; for FLAG keywords, 0 clears and 1 sets."),
  K("ADD","[Obj.]Key, Number/[Obj.]Key2;","both","Increases a keyword value by a number or skill (negative decreases)."),
  K("ADDT","[Obj.]Key, Number/[Obj.]Key2;","both","Like ADD but time-corrected (value multiplied by TIME_CORR). For constant-speed changes (e.g. lifts)."),
  K("ACCEL","[Obj.]Key, Number/[Obj.]Key2;","both","Adds like an acceleration; uses skills INERTIA and FRICTION."),
  K("RULE","Skill = expression;","both","Assigns an arithmetic expression (numbers, skills, parentheses, + - * /) to a skill; clamped by MIN/MAX. Avoid factors < 0.01."),
  K("IF_ABOVE","[Obj.]Key, Number/[Obj.]Key2;","both","Executes the next instruction only if the value is greater than the number/keyword."),
  K("IF_BELOW","[Obj.]Key, Number/[Obj.]Key2;","both","Executes the next instruction only if the value is less than the number/keyword."),
  K("IF_EQUAL","[Obj.]Key, Number/[Obj.]Key2;","both","Executes the next instruction only if the value is exactly equal (integers only)."),
  K("IF_MIN","Skill;","both","Executes the next instruction only if the skill has reached its minimum."),
  K("IF_MAX","Skill;","both","Executes the next instruction only if the skill has reached its maximum."),
  K("SKIP","Number;","both","Relative jump: skips the given number of instructions (negative = backward)."),
  K("GOTO","Label;","both","Absolute jump to a target label (a keyword followed by a colon)."),
  K("CALL","Action;","both","Runs the given action, then continues with the next instruction."),
  K("BRANCH","Action;","both","Aborts the current action and runs the given action immediately."),
  K("END",";","both","Ends the action."),
  K("WAIT","Number/Skill;","both","(EACH_TICK actions) Pauses the action for the given number of image cycles."),
  K("WAITT","Number/Skill;","both","Pauses the action for the given number of Ticks (fixed time)."),
  K("PLAY_SOUND","Sound, Volume;","both","Starts a sound at the given volume (0..1 or skill)."),
  K("PLAY_SONG","Music, Volume;","both","Starts a new background song (volume 0 switches music off)."),
  K("PLAY_SONG_ONCE","Music, Volume;","both","Like PLAY_SONG but plays once; afterwards the background music ends."),
  K("PLAY_FLIC","Flic;","both","Plays a full-screen animation. In the 1995 engine, image build and EACH_TICK stop during play (start a song one frame earlier); newer engines keep EACH_TICK running and expose FLIC_FRAME."),
  K("PLAY_FLICFILE","<Filename>;","both","Like PLAY_FLIC but streams from disk and frees the memory afterwards."),
  K("FADE_PAL","Palette, Number/Skill;","both","Cross-fades the current palette toward another (factor 0..1; 1 completes the change)."),
  K("DROP","Object;","both","Places a Thing/Actor in the player's view direction at distance DIST (same region as the player)."),
  K("PLACE","Object;","both","Applies new vertex positions to a wall/thing/actor from its X,Y / X1..Z2 parameters (e.g. to shift or rotate walls)."),
  K("SHOOT","[Object];","both","Triggers IF_HIT on the nearest object in view (using SHOOT_FAC/RANGE/X/Y); sets HIT_DIST and RESULT. Also opens nearby switches/doors."),
  K("EXPLODE","Object;","both","Triggers IF_HIT on all FRAGILE objects within SHOOT_RANGE of the named actor; sets HIT_MINDIST."),
  K("SAVE","\"Text\", Skill;","both","Saves the game under a name + number (.SAV) in SAVEDIR."),
  K("LOAD","\"Text\", Skill;","both","Loads a previously saved game."),
  K("SAVE_INFO","\"Text\", Skill;","both","Like SAVE but stores only the GLOBAL skills."),
  K("LOAD_INFO","\"Text\", Skill;","both","Like LOAD but loads only the GLOBAL skills."),
  K("MAP","<Filename>;","both","Loads a new topography (.WMP) and resets player/actors to start positions (professional version)."),
  K("LEVEL","<Filename>[, <Resource>];","both","Loads a new level (WDL + topography) and runs its start action (professional version)."),
  K("EXIT","[\"Text\"/String];","both","Ends the game and returns to DOS, optionally printing a message."),
  K("EACH_TICK","Action, …;","both","Global list of up to 16 actions run after each image build."),
  K("EACH_SEC","Action, …;","both","Global list of up to 16 actions run once per second."),
  K("IF_START","Action;","both","Action run at game start (palette changes, title animations, songs…)."),
  K("IF_LEFT","Action;","both","Run on left mouse button / joystick button 1."),
  K("IF_MIDDLE","Action;","both","Run on middle mouse button / joystick button 3."),
  K("IF_RIGHT","Action;","both","Run on right mouse button / joystick button 2."),
  K("IF_TAST","Action;","both","Run when any key is pressed. (v3.8 documents the equivalent as IF_ANYKEY.)"),
  K("IF_F1...","Action;","both","Run on the given key. Family: IF_F1..IF_F12, IF_ESC, IF_TAB, IF_CTRL, IF_ALT, IF_SPACE, IF_BKSP, IF_CUU/CUD/CUR/CUL, IF_PGUP, IF_PGDN, IF_HOME, IF_END, IF_INS, IF_DEL, IF_PAUSE, IF_CAR, IF_CAL, IF_ENTER, IF_0..IF_9, IF_A..IF_Z."),
  K("IF_ANYKEY","Action;","new","Run when any key is pressed (newer name; equivalent to the 1995 IF_TAST)."),
  K("PUSH","Number/Skill;","new","Triggers IF_HIT on the closest visible object within the given distance (open doors, start lifts)."),
  K("SHAKE","Object;","new","Tells an object its position/size changed; required after directly setting coordinates."),
  K("STOP_FLIC",";","new","Stops the currently playing flic."),
  K("BEEP",";","new","Plays a short note sequence on the PC speaker (handy during development)."),
 ])

# 11. GLOBALS / SKILLS ----------------------------------------------------
cat("globals", "Globals & Predefined Skills",
 "Skill definitions and the predefined player, engine, input, time and debug skills.",
 "Skills are numeric properties (like variables) belonging to the player and objects. Below is the SKILL definition and the predefined skills, grouped by purpose. Skills marked read-only are computed by the engine.",
 [
  K("SKILL","Keyword { ... };","both","Defines a skill (TYPE, VAL, MIN, MAX)."),
  K("TYPE","Keyword;","both","Skill kind: LOCAL, GLOBAL or PLAYER. GLOBAL skills survive level reloads; default LOCAL."),
  K("VAL","Number;","both","Initial value of the skill (default 0)."),
  K("MIN","Number;","both","Lower limit of the skill value."),
  K("MAX","Number;","both","Upper limit of the skill value."),
  # screen / render
  K("SCREEN_WIDTH","(skill)","both","Width of the 3D window in pixels (steps of 16)."),
  K("SCREEN_HGT","(skill)","both","Height of the 3D window in pixels (even numbers)."),
  K("SCREEN_X","(skill)","both","Horizontal offset of the 3D window from the left edge (steps of 4)."),
  K("SCREEN_Y","(skill)","both","Vertical offset of the 3D window from the top edge."),
  K("ASPECT","(skill)","both","Height-to-width ratio of the 3D view (0.1..10, default 1)."),
  K("MOTION_BLUR","(skill)","both","Motion-blur amount (0..1); lowers resolution during movement for smoother motion."),
  K("RENDER_MODE","(skill)","both","Render activity: 2 = full redraw, 1 = partial, 0.5 = normal, 0 = none. Auto-resets to 0.5."),
  K("MOVE_MODE","(skill)","both","Freezes movement/actions: 1 normal, 0.5 stop actors, 0 stop player+events, -0.5 stop global ticks."),
  # map
  K("MAP_MAXX","(skill)","both","Largest X coordinate of the map (read-only)."),
  K("MAP_MINX","(skill)","both","Smallest X coordinate of the map (read-only)."),
  K("MAP_MAXY","(skill)","both","Largest Y coordinate of the map (read-only)."),
  K("MAP_MINY","(skill)","both","Smallest Y coordinate of the map (read-only)."),
  K("MAP_SCALE","(skill)","both","Map display scale relative to the 3D window (default 0.9; 1 = fits exactly)."),
  K("MAP_MODE","(skill)","both","Map display mode (0 off; >0 shows the map; the value 2 reveals all objects).", note="The 1995 book states the range as 0..1, but 2 is a valid value."),
  K("MAP_LAYER","(skill)","both","Overlay layer the map appears on (0..16)."),
  K("SOUND_VOL","(skill)","both","Global sound-effect volume (0..1)."),
  K("MUSIC_VOL","(skill)","both","Music volume (0..1; 0 switches music off)."),
  # player light
  K("PLAYER_LIGHT","(skill)","both","Strength of the light the player carries (0..1)."),
  K("LIGHT_DIST","(skill)","both","Distance where the shading range begins (default 10 Steps)."),
  K("DARK_DIST","(skill)","both","Distance of the darkness boundary; recomputed from PLAYER_LIGHT."),
  # player physical
  K("PLAYER_WIDTH","(skill)","both","Minimum distance of the player to walls/objects (default 1.2 Steps)."),
  K("PLAYER_SIZE","(skill)","both","Distance between the player's feet and eyes (default 3 Steps)."),
  K("PLAYER_CLIMB","(skill)","both","Maximum step-up height when changing region (default 1.5 Steps)."),
  K("WALK_PERIOD","(skill)","both","Steps per period of the distance-based walk bob (default 4)."),
  K("WALK_TIME","(skill)","both","Time constant for WALK movement (default 4 Ticks)."),
  K("WAVE_PERIOD","(skill)","both","Ticks per period of the time-based player sway (default 16)."),
  K("WALK","(skill)","both","Current deflection of the walking movement (-1..1)."),
  K("WAVE","(skill)","both","Current deflection of the time-based movement (-1..1)."),
  K("PSOUND_VOL","(skill)","both","Relative player (footstep) sound volume (0..2)."),
  K("PSOUND_TONE","(skill)","both","Pitch of the player (footstep) sound (0..4)."),
  # player motion
  K("PLAYER_VX","(skill)","both","Player velocity along X (Steps/Step); changing it moves the player with collision."),
  K("PLAYER_VY","(skill)","both","Player velocity along Y."),
  K("PLAYER_VZ","(skill)","both","Player velocity along Z (vertical)."),
  K("PLAYER_VROT","(skill)","both","Rotation speed of the view angle (radians/Tick)."),
  K("PLAYER_TILT","(skill)","both","Tangent of the vertical view angle (look up/down)."),
  K("PLAYER_ARC","(skill)","both","Focal length / field of view in radians (0.2..2.0, default 1 ≈ 60°)."),
  K("FRICTION","(skill)","both","Friction coefficient for ACCEL (0..1, default 0.5)."),
  K("INERTIA","(skill)","both","Inertia coefficient for ACCEL (0..1, default 1)."),
  K("SHOOT_RANGE","(skill)","both","Maximum SHOOT object distance in Steps (default 500)."),
  K("SHOOT_FAC","(skill)","both","Hit-strength factor for SHOOT/EXPLODE RESULT (0..1, default 1)."),
  K("SHOOT_X","(skill)","both","Horizontal SHOOT deviation from the 3D-window centre (-1..1)."),
  K("SHOOT_Y","(skill)","both","Vertical SHOOT deviation from the 3D-window centre (-1..1)."),
  K("HIT_DIST","(skill)","both","Distance to the last object hit by SHOOT/EXPLODE (0 if none)."),
  K("INV_DIST","(skill)","old","Reciprocal of the SHOOT hit distance.", note="Removed in newer versions (use HIT_DIST / HIT_X / HIT_Y).", removed=True),
  K("RESULT","(skill)","both","Strength of the current event/hit (0..1)."),
  K("PLAYER_X","(skill)","both","Player X position (no collision when set directly)."),
  K("PLAYER_Y","(skill)","both","Player Y position (no collision when set directly)."),
  K("PLAYER_Z","(skill)","both","Player eye height in Steps (no collision when set directly)."),
  K("PLAYER_ANGLE","(skill)","both","Horizontal view direction in radians (0 = +X axis = east)."),
  K("PLAYER_SIN","(skill)","both","Sine of the player's view angle (for movement rules)."),
  K("PLAYER_COS","(skill)","both","Cosine of the player's view angle."),
  K("PLAYER_SPEED","(skill)","both","Speed component along the view direction (negative when reversing)."),
  K("ACCELERATION","(skill)","both","Acceleration along the view direction."),
  K("PLAYER_HGT","(skill)","both","Player feet height above/below the region floor (PLAYER_Z − PLAYER_SIZE − FLOOR_HGT)."),
  K("FLOOR_HGT","(skill)","both","Actual floor height at the player position (slope-aware)."),
  K("CEIL_HGT","(skill)","both","Actual ceiling height at the player position."),
  K("IMPACT_VX","(skill)","both","Collision velocity change along X; auto-increased on collision, reset manually (pinball effect)."),
  K("IMPACT_VY","(skill)","both","Collision velocity change along Y."),
  K("IMPACT_VZ","(skill)","both","Collision velocity change along Z (floor/ceiling)."),
  K("SLOPE_AHEAD","(skill)","both","Floor slope in the view direction (height gain per Step)."),
  K("NODE","(skill)","both","Current node number in multiplayer games (from the command line)."),
  K("RANDOM","(skill)","both","Random number 0..1, changing each frame."),
  K("TIME_CORR","(skill)","both","Time-correction factor (1.0 at 16 fps; lower at higher fps)."),
  K("TIME_FAC","(skill)","both","Reciprocal of TIME_CORR (higher on faster machines)."),
  K("TICKS","(skill)","both","Increases by 1 every 1/16 second."),
  K("SECS","(skill)","both","Increases by 1 every second."),
  K("STEPS","(skill)","both","Increases with the distance the player walks."),
  K("MOUSE_LEFT","(skill)","both","State of the left mouse / joystick button 1 (0/1)."),
  K("MOUSE_MIDDLE","(skill)","both","State of the middle mouse / joystick button 3."),
  K("MOUSE_RIGHT","(skill)","both","State of the right mouse / joystick button 2."),
  K("JOY_4","(skill)","both","State of joystick button 4."),
  K("KEY_F1...KEY_Z","(skills)","both","Key-state skills (0/1): KEY_F1..KEY_F12, KEY_ESC, KEY_TAB, KEY_SHIFT, KEY_CTRL, KEY_ALT, KEY_SPACE, KEY_BKSP, KEY_CUU/CUD/CUR/CUL, KEY_PGUP, KEY_PGDN, KEY_HOME, KEY_END, KEY_INS, KEY_DEL, KEY_PAUSE, KEY_CAR, KEY_CAL, KEY_PLUS, KEY_MINUS, KEY_ENTER, KEY_0..KEY_9, KEY_A..KEY_Z."),
  K("FORCE_AHEAD","(skill)","both","Analog forward/backward input (-1..1)."),
  K("FORCE_STRAFE","(skill)","both","Analog left/right (strafe) input."),
  K("FORCE_ROT","(skill)","both","Analog horizontal rotation input."),
  K("FORCE_TILT","(skill)","both","Analog look up/down input."),
  K("FORCE_UP","(skill)","both","Analog vertical (duck/jump) input."),
  K("KEY_SENSE","(skill)","both","Keyboard movement sensitivity (default 0.7)."),
  K("SHIFT_SENSE","(skill)","both","Factor applied to input while [Shift] is held (default 2)."),
  K("MOUSE_SENSE","(skill)","both","Mouse movement sensitivity (default 1).", note="The 1995 book misprints this as `MOUS_SENSE`."),
  K("JOY_SENSE","(skill)","both","Joystick movement sensitivity (default 1)."),
  K("ERROR","(skill)","both","Error code for the current frame (WRUN.EXE only): 0 none, 1 CLIP_DIST too small, 3 NEXUS too small, 5 missing bitmap, 6 missing region/texture, 8 bad synonym, 9 missing region."),
  K("DEBUG_MODE","(skill)","both","If 1, halts after each image build until 'S' is pressed (WRUN.EXE only)."),
  K("ACTIVE_NEXUS","(skill)","both","Nexus utilisation (WRUN.EXE only)."),
  K("ACTIVE_TARGETS","(skill)","both","Number of actors with a TARGET (WRUN.EXE only)."),
  K("ACTIVE_OBJTICKS","(skill)","both","Number of objects with running EACH_TICK actions (WRUN.EXE only)."),
  K("ACTIVE_REGTICKS","(skill)","old","Number of regions with running EACH_TICK actions (WRUN.EXE only).", note="Removed in newer versions (only ACTIVE_OBJTICKS kept).", removed=True),
  # newer skills
  K("SHOOT_ANGLE","(skill)","new","Angle from a SHOOT object to the player (for aiming projectiles)."),
  K("SHOOT_SECTOR","(skill)","new","Angular sector an actor uses for SHOOT (default 2π)."),
  K("HIT_X","(skill)","new","X pixel coordinate of the texture pixel hit by SHOOT (for bullet-hole ATTACH)."),
  K("HIT_Y","(skill)","new","Y pixel coordinate of the texture pixel hit by SHOOT."),
  K("HIT_MINDIST","(skill)","both","Distance to the nearest object hit by EXPLODE (0 if none in range)."),
  K("CD_TRACK","(skill)","new","Number of the CD-audio track currently playing (0 if stopped)."),
 ])

# 12. UI ------------------------------------------------------------------
cat("ui", "Panels, Texts & Overlays",
 "The 2D user-interface objects: PANEL, TEXT and OVERLAY, their members, and the screen lists.",
 "The user interface is built from control panels, text displays and overlays. Each must be entered into a screen list (PANELS, MESSAGES, LAYERS) to appear.",
 [
  K("PANEL","Keyword { ... };","both","Defines a control panel (displays and images). Best placed outside the 3D window (rebuilt each frame; see REFRESH)."),
  K("POS_X","x;","both","X offset of the element's upper-left corner from the screen / panel origin."),
  K("POS_Y","y;","both","Y offset of the element's upper-left corner."),
  K("PAN_MAP","Bmap;","both","Background bitmap of the panel (its size sets the panel size)."),
  K("VBAR","x,y,len,Bmap,fac,Skill;","both","Vertical bar gauge: the bitmap is shifted by skill×fac. Up to 16 bars per panel."),
  K("HBAR","x,y,len,Bmap,fac,Skill;","both","Horizontal bar gauge (counterpart of VBAR)."),
  K("DIGITS","x,y,len,Font,fac,Skill;","both","Numeric display of skill×fac with len digits; negative len shows time h:m:s."),
  K("PICTURE","x,y,Texture,fac,Skill;","both","Animated picture display; the texture side is chosen by skill×fac. Up to 4 per panel."),
  K("REFRESH","(FLAGS REFRESH;)","both","Regenerates the panel each frame (e.g. for scrolling text). Costly for large panels — prefer an OVERLAY."),
  K("TEXT","Keyword { ... };","both","Defines a text display inside the 3D window (messages, dialogue)."),
  K("FONT","Font;","both","Character set used for the text or symbols."),
  K("STRING","String;","both","The text content (predefined string keyword); `\\n` = line break, `\\\"` = quote; NULL = no text."),
  K("OVERLAY","Keyword { ... };","both","Defines an overlay (cockpit/weapon/tool) inside the 3D window; faster than a panel but without controls. Up to 16 stacked."),
  K("OVLYS","Ovly, …;","both","List of up to 64 overlay bitmaps (count = SIDES×CYCLES)."),
  K("ABSPOS","(FLAGS ABSPOS;)","both","Overlay position is relative to the screen corner rather than the 3D-window corner."),
  K("PANELS","Panel, …;","both","Screen list of up to 16 panels to display."),
  K("MESSAGES","Text, …;","both","Screen list of up to 16 text displays."),
  K("LAYERS","Overlay, …;","both","Screen list of up to 16 overlays."),
 ])

# 13. SYNONYMS ------------------------------------------------------------
cat("synonyms", "Synonyms",
 "Predefined names that let an action address whichever object/region triggered it.",
 "Synonyms let an action change arbitrary objects or regions without knowing their keyword at definition time. Objects can be addressed by name, index or the predefined synonyms below.",
 [
  K("MY","(synonym)","both","The object that triggered the running action (e.g. `SET MY.TEXTURE, crash_tex;`). Undefined if not triggered by an object."),
  K("HERE","(synonym)","both","The region the player is currently in (important for collision/height; reassign after moving the player directly)."),
  K("THERE","(synonym)","both","The region that triggered the action, or that contains the triggering object."),
 ])

# ---- Generation ----------------------------------------------------------
if os.path.isdir(API):
    shutil.rmtree(API)
os.makedirs(API)

total_kw = sum(len(c["kws"]) for c in CATS)

# Object types (groups) are listed alphabetically by title.
CATS.sort(key=lambda c: c["title"].lower())

# Home
write(os.path.join(ROOT, "index.md"),
 [("layout","home"),("title","Home"),("nav_order","1")],
 f"""# ACKNEX / WDL Reference

English reference for **WDL** (World Definition Language), the scripting language
of the **ACKNEX** engine (3D GameStudio).

---

The [API Reference](api/) groups the **{total_kw}** keywords by **object type**
(actions, actors, walls, regions, …), listed alphabetically. Prefer a single
flat list? See the [Keywords A–Z](keywords.html) index.
""")

# Alphabetical keyword index (ungrouped)
all_kws = sorted(
    ((k, c) for c in CATS for k in c["kws"]),
    key=lambda pair: (pair[0]["name"].lower(), pair[1]["title"].lower()))
arows = "\n".join(
    f"| [`{k['name']}`](api/{c['slug']}/{slug(k['name'])}.html) "
    f"| [{c['title']}](api/{c['slug']}.html) | {k['desc']} |"
    for k, c in all_kws)
write(os.path.join(ROOT, "keywords.md"),
 [("layout","default"),("title","Keywords A–Z"),("nav_order","2")],
 f"""# Keywords A–Z

Every WDL keyword in a single alphabetical list, regardless of object type.
There are **{total_kw}** keywords across **{len(CATS)}** object types.

| Keyword | Object type | Summary |
|:--------|:------------|:--------|
{arows}
""")

# API index
rows = "\n".join(
    f"| [{c['title']}]({c['slug']}.html) | {len(c['kws'])} | {c['summary']} |"
    for c in CATS)
write(os.path.join(API, "index.md"),
 [("layout","default"),("title","API Reference"),("nav_order","3"),("has_children","true")],
 f"""# API Reference

WDL keywords grouped by object type (listed alphabetically). Pick a type, then a
keyword — or browse the flat [Keywords A–Z](../keywords.html) index.

| Object type | Keywords | Summary |
|:------------|:--------:|:--------|
{rows}
""")

# Categories + keywords
for ci, c in enumerate(CATS, start=1):
    # keywords are listed alphabetically within each group
    kws = sorted(c["kws"], key=lambda k: k["name"].lower())
    # category page
    krows = []
    for ki, k in enumerate(kws, start=1):
        ks = slug(k["name"])
        sig = f" `{k['sig']}`" if k['sig'] else ""
        krows.append(f"| [`{k['name']}`]({c['slug']}/{ks}.html) | {k['desc']} |")
    ktable = "\n".join(krows)
    write(os.path.join(API, f"{c['slug']}.md"),
     [("layout","default"),("title",c["title"]),("parent","API Reference"),
      ("has_children","true"),("nav_order",str(ci))],
     f"""# {c['title']}

{c['intro']}

| Keyword | Summary |
|:--------|:--------|
{ktable}
""")
    # keyword pages
    for ki, k in enumerate(kws, start=1):
        ks = slug(k["name"])
        sig = f" `{k['sig']}`" if k['sig'] else ""
        body = f"# `{k['name']}`{sig}\n\n{k['desc']}\n"
        if k.get("note"):
            body += f"\n> **Note:** {k['note']}\n"
        title = k["name"].replace('"',"'")
        write(os.path.join(API, c["slug"], f"{ks}.md"),
         [("layout","default"),("title",f"\"{title}\""),("parent",c["title"]),
          ("grand_parent","API Reference"),("nav_order",str(ki))],
         body)

print(f"Generated {len(CATS)} categories, {total_kw} keywords.")
