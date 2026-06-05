---
layout: default
title: Actions & Instructions
parent: API Reference
has_children: true
nav_order: 1
---

# Actions & Instructions

Actions give objects the behaviour of linear automata. An action is a list of instructions executed one after another; many actions can run at once. Below are the ACTION keyword, the instructions usable inside actions, and the global/event keywords that trigger actions.

| Keyword | Summary |
|:--------|:--------|
| [`ACCEL`](actions/accel.html) | Adds like an acceleration; uses skills INERTIA and FRICTION. |
| [`ACTION`](actions/action.html) | Defines an action — a list of the instructions below. |
| [`ADD`](actions/add.html) | Increases a keyword value by a number or skill (negative decreases). |
| [`ADDT`](actions/addt.html) | Like ADD but time-corrected (value multiplied by TIME_CORR). For constant-speed changes (e.g. lifts). |
| [`BEEP`](actions/beep.html) | Plays a short note sequence on the PC speaker (handy during development). |
| [`BRANCH`](actions/branch.html) | Aborts the current action and runs the given action immediately. |
| [`CALL`](actions/call.html) | Runs the given action, then continues with the next instruction. |
| [`DROP`](actions/drop.html) | Places a Thing/Actor in the player's view direction at distance DIST (same region as the player). |
| [`EACH_SEC`](actions/each_sec.html) | Global list of up to 16 actions run once per second. |
| [`EACH_TICK`](actions/each_tick.html) | Global list of up to 16 actions run after each image build. |
| [`END`](actions/end.html) | Ends the action. |
| [`EXIT`](actions/exit.html) | Ends the game and returns to DOS, optionally printing a message. |
| [`EXPLODE`](actions/explode.html) | Triggers IF_HIT on all FRAGILE objects within SHOOT_RANGE of the named actor; sets HIT_MINDIST. |
| [`FADE_PAL`](actions/fade_pal.html) | Cross-fades the current palette toward another (factor 0..1; 1 completes the change). |
| [`GOTO`](actions/goto.html) | Absolute jump to a target label (a keyword followed by a colon). |
| [`IF_ABOVE`](actions/if_above.html) | Executes the next instruction only if the value is greater than the number/keyword. |
| [`IF_ANYKEY`](actions/if_anykey.html) | Run when any key is pressed (newer name; equivalent to the 1995 IF_TAST). |
| [`IF_BELOW`](actions/if_below.html) | Executes the next instruction only if the value is less than the number/keyword. |
| [`IF_EQUAL`](actions/if_equal.html) | Executes the next instruction only if the value is exactly equal (integers only). |
| [`IF_F1...`](actions/if_f1.html) | Run on the given key. Family: IF_F1..IF_F12, IF_ESC, IF_TAB, IF_CTRL, IF_ALT, IF_SPACE, IF_BKSP, IF_CUU/CUD/CUR/CUL, IF_PGUP, IF_PGDN, IF_HOME, IF_END, IF_INS, IF_DEL, IF_PAUSE, IF_CAR, IF_CAL, IF_ENTER, IF_0..IF_9, IF_A..IF_Z. |
| [`IF_LEFT`](actions/if_left.html) | Run on left mouse button / joystick button 1. |
| [`IF_MAX`](actions/if_max.html) | Executes the next instruction only if the skill has reached its maximum. |
| [`IF_MIDDLE`](actions/if_middle.html) | Run on middle mouse button / joystick button 3. |
| [`IF_MIN`](actions/if_min.html) | Executes the next instruction only if the skill has reached its minimum. |
| [`IF_RIGHT`](actions/if_right.html) | Run on right mouse button / joystick button 2. |
| [`IF_START`](actions/if_start.html) | Action run at game start (palette changes, title animations, songs…). |
| [`IF_TAST`](actions/if_tast.html) | Run when any key is pressed. (v3.8 documents the equivalent as IF_ANYKEY.) |
| [`LEVEL`](actions/level.html) | Loads a new level (WDL + topography) and runs its start action (professional version). |
| [`LOAD`](actions/load.html) | Loads a previously saved game. |
| [`LOAD_INFO`](actions/load_info.html) | Like LOAD but loads only the GLOBAL skills. |
| [`MAP`](actions/map.html) | Loads a new topography (.WMP) and resets player/actors to start positions (professional version). |
| [`PLACE`](actions/place.html) | Applies new vertex positions to a wall/thing/actor from its X,Y / X1..Z2 parameters (e.g. to shift or rotate walls). |
| [`PLAY_FLIC`](actions/play_flic.html) | Plays a full-screen animation. In the 1995 engine, image build and EACH_TICK stop during play (start a song one frame earlier); newer engines keep EACH_TICK running and expose FLIC_FRAME. |
| [`PLAY_FLICFILE`](actions/play_flicfile.html) | Like PLAY_FLIC but streams from disk and frees the memory afterwards. |
| [`PLAY_SONG`](actions/play_song.html) | Starts a new background song (volume 0 switches music off). |
| [`PLAY_SONG_ONCE`](actions/play_song_once.html) | Like PLAY_SONG but plays once; afterwards the background music ends. |
| [`PLAY_SOUND`](actions/play_sound.html) | Starts a sound at the given volume (0..1 or skill). |
| [`PUSH`](actions/push.html) | Triggers IF_HIT on the closest visible object within the given distance (open doors, start lifts). |
| [`RULE`](actions/rule.html) | Assigns an arithmetic expression (numbers, skills, parentheses, + - * /) to a skill; clamped by MIN/MAX. Avoid factors < 0.01. |
| [`SAVE`](actions/save.html) | Saves the game under a name + number (.SAV) in SAVEDIR. |
| [`SAVE_INFO`](actions/save_info.html) | Like SAVE but stores only the GLOBAL skills. |
| [`SET`](actions/set.html) | Assigns a new value or keyword to any keyword/skill. Assigning NULL switches actions off; for FLAG keywords, 0 clears and 1 sets. |
| [`SHAKE`](actions/shake.html) | Tells an object its position/size changed; required after directly setting coordinates. |
| [`SHOOT`](actions/shoot.html) | Triggers IF_HIT on the nearest object in view (using SHOOT_FAC/RANGE/X/Y); sets HIT_DIST and RESULT. Also opens nearby switches/doors. |
| [`SKIP`](actions/skip.html) | Relative jump: skips the given number of instructions (negative = backward). |
| [`STOP_FLIC`](actions/stop_flic.html) | Stops the currently playing flic. |
| [`WAIT`](actions/wait.html) | (EACH_TICK actions) Pauses the action for the given number of image cycles. |
| [`WAITT`](actions/waitt.html) | Pauses the action for the given number of Ticks (fixed time). |
