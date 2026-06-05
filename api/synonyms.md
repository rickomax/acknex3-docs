---
layout: default
title: Synonyms
parent: API Reference
has_children: true
nav_order: 9
---

# Synonyms

Synonyms let an action change arbitrary objects or regions without knowing their keyword at definition time. Objects can be addressed by name, index or the predefined synonyms below.

| Keyword | Summary |
|:--------|:--------|
| [`HERE`](synonyms/here.html) | The region the player is currently in (important for collision/height; reassign after moving the player directly). |
| [`HIT`](synonyms/hit.html) | The object last hit by the player's SHOOT, last clicked with the mouse, or nearest to the last EXPLODE. |
| [`MY`](synonyms/my.html) | The object that triggered the running action (e.g. `SET MY.TEXTURE, crash_tex;`). Undefined if not triggered by an object. |
| [`THERE`](synonyms/there.html) | The region that triggered the action, or that contains the triggering object. |
| [`TOUCH_REG`](synonyms/touch_reg.html) | The region whose floor or ceiling was last touched by the mouse pointer. |
| [`TOUCH_TEX`](synonyms/touch_tex.html) | The texture last touched by the mouse pointer. |
| [`TOUCHED`](synonyms/touched.html) | The object last touched by the mouse pointer. |
