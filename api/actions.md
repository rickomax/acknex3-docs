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
| [`ABS`](actions/abs.html) | Absolute value of x, for use in RULE expressions. |
| [`ACCEL`](actions/accel.html) | Adds like an acceleration; uses skills INERTIA and FRICTION. |
| [`ACOS`](actions/acos.html) | Arc cosine of x (inverse trigonometric). |
| [`ACTION`](actions/action.html) | Defines an action — a list of the instructions below. |
| [`ADD`](actions/add.html) | Increases a keyword value by a number or skill (negative decreases). |
| [`ADD_STRING`](actions/add_string.html) | Appends String2 to String1, like SET_STRING but concatenating. |
| [`ADDT`](actions/addt.html) | Like ADD but time-corrected (value multiplied by TIME_CORR). For constant-speed changes (e.g. lifts). |
| [`ASIN`](actions/asin.html) | Arc sine of x (inverse trigonometric). |
| [`BEEP`](actions/beep.html) | Plays a short note sequence on the PC speaker (handy during development). |
| [`BRANCH`](actions/branch.html) | Aborts the current action and runs the given action immediately. |
| [`BREAK`](actions/break.html) | Leaves the enclosing WHILE loop immediately. |
| [`CALL`](actions/call.html) | Runs the given action, then continues with the next instruction. |
| [`CONTINUE`](actions/continue.html) | Skips to the next iteration of the enclosing WHILE loop. |
| [`COS`](actions/cos.html) | Cosine of x (radians). |
| [`DROP`](actions/drop.html) | Places a Thing/Actor in the player's view direction at distance DIST (same region as the player). |
| [`EACH_SEC`](actions/each_sec.html) | Global list of up to 16 actions run once per second. |
| [`EACH_TICK`](actions/each_tick.html) | Global list of up to 16 actions run after each image build. |
| [`ELSE`](actions/else.html) | Optional alternative block of an IF, run when the condition is false. |
| [`END`](actions/end.html) | Ends the action. |
| [`ENDIF`](actions/endif.html) | Closes an IFDEF/IFNDEF preprocessor block; the lines in between are skipped when the condition is not met. |
| [`EXIT`](actions/exit.html) | Ends the game and returns to DOS, optionally printing a message. |
| [`EXP`](actions/exp.html) | e raised to the power x. |
| [`EXPLODE`](actions/explode.html) | Triggers IF_HIT on all FRAGILE objects within SHOOT_RANGE of the named actor; sets HIT_MINDIST. |
| [`FADE_PAL`](actions/fade_pal.html) | Cross-fades the current palette toward another (factor 0..1; 1 completes the change). |
| [`GETMIDI`](actions/getmidi.html) | Gets the device type of a MIDI channel (0..15). |
| [`GOTO`](actions/goto.html) | Absolute jump to a target label (a keyword followed by a colon). |
| [`IF`](actions/if.html) | Executes the first block when the expression is non-zero, otherwise the optional ELSE block. |
| [`IF_ABOVE`](actions/if_above.html) | Executes the next instruction only if the value is greater than the number/keyword. |
| [`IF_ANYKEY`](actions/if_anykey.html) | Run when any key is pressed (newer name; equivalent to the 1995 IF_TAST). |
| [`IF_BELOW`](actions/if_below.html) | Executes the next instruction only if the value is less than the number/keyword. |
| [`IF_EQUAL`](actions/if_equal.html) | Executes the next instruction only if the value is exactly equal (integers only). |
| [`IF_F1...`](actions/if_f1.html) | Run on the given key. Family: IF_F1..IF_F12, IF_ESC, IF_TAB, IF_CTRL, IF_ALT, IF_SPACE, IF_BKSP, IF_CUU/CUD/CUR/CUL, IF_PGUP, IF_PGDN, IF_HOME, IF_END, IF_INS, IF_DEL, IF_PAUSE, IF_CAR, IF_CAL, IF_ENTER, IF_0..IF_9, IF_A..IF_Z. |
| [`IF_LEFT`](actions/if_left.html) | Run on left mouse button / joystick button 1. |
| [`IF_LOAD`](actions/if_load.html) | Performed after a saved score is loaded; useful for resetting panels or skills used while saving. |
| [`IF_MAX`](actions/if_max.html) | Executes the next instruction only if the skill has reached its maximum. |
| [`IF_MIDDLE`](actions/if_middle.html) | Run on middle mouse button / joystick button 3. |
| [`IF_MIN`](actions/if_min.html) | Executes the next instruction only if the skill has reached its minimum. |
| [`IF_MSTOP`](actions/if_mstop.html) | Triggered when the mouse pointer is active and held still for half a second (see MOUSE_CALM/MOUSE_MOVING). |
| [`IF_RELEASE`](actions/if_release.html) | Texture mouse event: performed when the mouse pointer leaves the object's texture. |
| [`IF_RIGHT`](actions/if_right.html) | Run on right mouse button / joystick button 2. |
| [`IF_START`](actions/if_start.html) | Action run at game start (palette changes, title animations, songs…). |
| [`IF_TAST`](actions/if_tast.html) | Run when any key is pressed. (v3.8 documents the equivalent as IF_ANYKEY.) |
| [`IF_TOUCH`](actions/if_touch.html) | Texture mouse event: performed while the mouse pointer touches the object's texture (within TOUCH_DIST). |
| [`INKEY`](actions/inkey.html) | Reads keyboard input into the named string until input is terminated; activates the local keyboard layout. |
| [`INPORT`](actions/inport.html) | Reads the byte at hardware port adr into Skill. |
| [`INT`](actions/int.html) | Integer part of x. |
| [`LEVEL`](actions/level.html) | Loads a new level (WDL + topography) and runs its start action (professional version). |
| [`LOAD`](actions/load.html) | Loads a previously saved game. |
| [`LOAD_INFO`](actions/load_info.html) | Like LOAD but loads only the GLOBAL skills. |
| [`LOG`](actions/log.html) | Natural logarithm of x. |
| [`LOG10`](actions/log10.html) | Base-10 logarithm of x. |
| [`LOG2`](actions/log2.html) | Base-2 logarithm of x. |
| [`MAP`](actions/map.html) | Loads a new topography (.WMP) and resets player/actors to start positions (professional version). |
| [`MIDI_COM`](actions/midi_com.html) | Sends data directly to a MIDI channel; statusb = command*16 + channel number. |
| [`NEXT_MY`](actions/next_my.html) | Moves the MY synonym to the next object of the same name — for looping over several objects. |
| [`NEXT_MY_THERE`](actions/next_my_there.html) | Advances both MY and THERE synonyms to the next matching object — for looping over several objects. |
| [`NEXT_THERE`](actions/next_there.html) | Moves the THERE synonym to the next matching object — for looping over several objects. |
| [`OUTPORT`](actions/outport.html) | Writes a number or Skill to hardware port adr. |
| [`PLACE`](actions/place.html) | Applies new vertex positions to a wall/thing/actor from its X,Y / X1..Z2 parameters (e.g. to shift or rotate walls). |
| [`PLAY_DEMO`](actions/play_demo.html) | Replays a recorded demo file; pressing any key stops playback. |
| [`PLAY_FLIC`](actions/play_flic.html) | Plays a full-screen animation. In the 1995 engine, image build and EACH_TICK stop during play (start a song one frame earlier); newer engines keep EACH_TICK running and expose FLIC_FRAME. |
| [`PLAY_FLICFILE`](actions/play_flicfile.html) | Like PLAY_FLIC but streams from disk and frees the memory afterwards. |
| [`PLAY_SONG`](actions/play_song.html) | Starts a new background song (volume 0 switches music off). |
| [`PLAY_SONG_ONCE`](actions/play_song_once.html) | Like PLAY_SONG but plays once; afterwards the background music ends. |
| [`PLAY_SOUND`](actions/play_sound.html) | Starts a sound at the given volume (0..1 or skill). |
| [`PLAY_SOUNDFILE`](actions/play_soundfile.html) | Plays a digital sound effect directly from an external sound file. |
| [`PRINT_STRING`](actions/print_string.html) | Appends a string (or quoted text) to the PRINTFILE text file; \n starts a new line. |
| [`PRINT_VALUE`](actions/print_value.html) | Appends Skill as a number with 3 decimals to the PRINTFILE text file. |
| [`PRINTFILE`](actions/printfile.html) | Names a text file (5-char name plus 3-digit number) into which PRINT_VALUE and PRINT_STRING write. |
| [`PUSH`](actions/push.html) | Triggers IF_HIT on the closest visible object within the given distance (open doors, start lifts). |
| [`RULE`](actions/rule.html) | Assigns an arithmetic expression (numbers, skills, parentheses, + - * /) to a skill; clamped by MIN/MAX. Avoid factors < 0.01. |
| [`SAVE`](actions/save.html) | Saves the game under a name + number (.SAV) in SAVEDIR. |
| [`SAVE_DEMO`](actions/save_demo.html) | Records the movement of the player and actors and all game events to a demo file. |
| [`SAVE_INFO`](actions/save_info.html) | Like SAVE but stores only the GLOBAL skills. |
| [`SET`](actions/set.html) | Assigns a new value or keyword to any keyword/skill. Assigning NULL switches actions off; for FLAG keywords, 0 clears and 1 sets. |
| [`SET_ALL`](actions/set_all.html) | Like SET, but applies to all objects/regions matching the keyword or synonym, not just the first. |
| [`SET_INFO`](actions/set_info.html) | Built-in debugger: writes all interesting parameters of Object into String for on-screen display. |
| [`SET_SKILL`](actions/set_skill.html) | Sets Skill to the numeric value contained in String. |
| [`SET_STRING`](actions/set_string.html) | Copies String2 into String1 (without exceeding String1's original length). |
| [`SETMIDI`](actions/setmidi.html) | Sets the device type of a MIDI channel (0..15): 0 = FM, 1 = digital, etc. |
| [`SHAKE`](actions/shake.html) | Tells an object its position/size changed; required after directly setting coordinates. |
| [`SHOOT`](actions/shoot.html) | Triggers IF_HIT on the nearest object in view (using SHOOT_FAC/RANGE/X/Y); sets HIT_DIST and RESULT. Also opens nearby switches/doors. |
| [`SIGN`](actions/sign.html) | -1 if x<0, 1 if x>0, 0 if x==0. |
| [`SIN`](actions/sin.html) | Sine of x (radians). |
| [`SKIP`](actions/skip.html) | Relative jump: skips the given number of instructions (negative = backward). |
| [`SQRT`](actions/sqrt.html) | Square root of x (a negative argument aborts the engine). |
| [`STOP_DEMO`](actions/stop_demo.html) | Stops recording or replaying the demo file. |
| [`STOP_FLIC`](actions/stop_flic.html) | Stops the currently playing flic. |
| [`TAN`](actions/tan.html) | Tangent of x (radians). |
| [`TILT`](actions/tilt.html) | Multiplies the Z values of all vertices, things and actors in the region, changing its slope at runtime. |
| [`TO_STRING`](actions/to_string.html) | Writes the numeric value of Skill as digits into String. |
| [`WAIT`](actions/wait.html) | (EACH_TICK actions) Pauses the action for the given number of image cycles. |
| [`WAITT`](actions/waitt.html) | Pauses the action for the given number of Ticks (fixed time). |
| [`WHILE`](actions/while.html) | Repeats the block as long as the expression is non-zero. |
