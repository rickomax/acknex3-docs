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
| [`MY`](synonyms/my.html) | The object that triggered the running action (e.g. `SET MY.TEXTURE, crash_tex;`). Undefined if not triggered by an object. |
| [`THERE`](synonyms/there.html) | The region that triggered the action, or that contains the triggering object. |
