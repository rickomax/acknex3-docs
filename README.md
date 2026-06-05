# ACKNEX / WDL Reference — documentation site

A [Just the Docs](https://just-the-docs.com/) site documenting **WDL** (World
Definition Language), the scripting language of the **ACKNEX** engine
(3D GameStudio).

It merges:

- the **1995 German WDL manual** (translated in
  [`../wdl-reference/`](../wdl-reference)), and
- the official English ACKNEX **v3.8** (`3dmanual.pdf`) and **v3.9**
  (`ACKMAN.PDF`) reference manuals.

## Structure

```
index.md              Home
api/index.md          API Reference (list of object types)
api/<type>.md         One object type (e.g. actor, wall, globals)
api/<type>/<kw>.md    One keyword page
```

The **API Reference** is split first by **object type** (textures, walls,
regions, actors, things, ways, globals/skills, actions, panels, palettes,
files, settings, synonyms) and then by **keyword**. Every keyword page carries
an _availability_ note: whether it comes from the 1995 book, the newer manuals,
or both. Keywords removed in newer versions (e.g. `INV_DIST`, `SLIDEDOOR`,
`ACTIVE_REGTICKS`) are flagged.

## Building locally

```bash
cd acknex-docs
bundle install
bundle exec jekyll serve
```

Then open <http://localhost:4000>. The theme is pinned to `just-the-docs`
0.12.0 in the `Gemfile`.

## Regenerating

The `api/` tree is generated from a single data file. Re-running the generator
rewrites every page under `api/` (the keyword data lives in the script).
