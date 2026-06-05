---
layout: default
title: Predefined Settings
parent: API Reference
has_children: true
nav_order: 7
---

# Predefined Settings

These predefined keywords define the basic settings for graphics, sounds and directories. They normally stand at the beginning of the main WDL file.

| Keyword | Summary |
|:--------|:--------|
| [`VIDEO`](settings/video.html) | Sets the screen resolution. Predefined resolution keywords: `320x200`, `X320x240`, `X320x400`. Newer engine versions add SVGA modes `S640x480` and `S800x600`. |
| [`NEXUS`](settings/nexus.html) | Sets the size of the Nexus — the internal data structure used for rendering. Depends on the maximum number of objects, walls and regions visible at once. Default 14. Too small a Nexus produces image errors signalled by the PC speaker. |
| [`CLIP_DIST`](settings/clip_dist.html) | Global view distance in Steps. Walls and objects entirely beyond this distance from the player are not rendered. Default 1000. Can be overridden per region. |
| [`IBANK`](settings/ibank.html) | Loads the instrument bank (an ADLIB `.IBK` instrument file) used for MIDI songs. |
| [`DRUMBANK`](settings/drumbank.html) | Loads the percussion instrument bank (played on MIDI channel 10). If omitted, internally defined general-MIDI instruments are used. |
| [`MIDI_PITCH`](settings/midi_pitch.html) | Number of octaves by which the pitch-bend parameter changes the pitch in MIDI songs. Range 1..12, default 2. |
| [`INCLUDE`](settings/include.html) | Reads further WDL definitions from a separate file and then continues with the original file. INCLUDEs may not be nested. |
| [`BIND`](settings/bind.html) | Binds the given file into the game so it is compiled in (e.g. for level changes). Any number of BIND files may be given. |
| [`MAPFILE`](settings/mapfile.html) | Defines the associated WMP topography file. Must stand in the main WDL and cannot be read via INCLUDE. |
| [`SAVEDIR`](settings/savedir.html) | Defines the directory in which saved games are stored. Created on first save if missing. |
| [`PATH`](settings/path.html) | Additional search path for bitmap or sound files (searched after the current directory). Up to 8 PATH keywords, searched in order. |
