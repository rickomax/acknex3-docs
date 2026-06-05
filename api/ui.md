---
layout: default
title: Panels, Texts & Overlays
parent: API Reference
has_children: true
nav_order: 6
---

# Panels, Texts & Overlays

The user interface is built from control panels, text displays and overlays. Each must be entered into a screen list (PANELS, MESSAGES, LAYERS) to appear.

| Keyword | Summary |
|:--------|:--------|
| [`ABSPOS`](ui/abspos.html) | Overlay position is relative to the screen corner rather than the 3D-window corner. |
| [`CENTER_X`](ui/center_x.html) | Centres a TEXT horizontally on POS_X (otherwise it is left-justified). |
| [`CENTER_Y`](ui/center_y.html) | Centres a TEXT vertically on POS_Y (otherwise it is top-justified). |
| [`DIGITS`](ui/digits.html) | Numeric display of skill×fac with len digits; negative len shows time h:m:s. |
| [`FONT`](ui/font.html) | Character set used for the text or symbols. |
| [`HBAR`](ui/hbar.html) | Horizontal bar gauge (counterpart of VBAR). |
| [`LAYERS`](ui/layers.html) | Screen list of up to 16 overlays. |
| [`MESSAGES`](ui/messages.html) | Screen list of up to 16 text displays. |
| [`OVERLAY`](ui/overlay.html) | Defines an overlay (cockpit/weapon/tool) inside the 3D window; faster than a panel but without controls. Up to 16 stacked. |
| [`OVLYS`](ui/ovlys.html) | List of up to 64 overlay bitmaps (count = SIDES×CYCLES). |
| [`PAN_MAP`](ui/pan_map.html) | Background bitmap of the panel (its size sets the panel size). |
| [`PANEL`](ui/panel.html) | Defines a control panel (displays and images). Best placed outside the 3D window (rebuilt each frame; see REFRESH). |
| [`PANELS`](ui/panels.html) | Screen list of up to 16 panels to display. |
| [`PICTURE`](ui/picture.html) | Animated picture display; the texture side is chosen by skill×fac. Up to 4 per panel. |
| [`POS_X`](ui/pos_x.html) | X offset of the element's upper-left corner from the screen / panel origin. |
| [`POS_Y`](ui/pos_y.html) | Y offset of the element's upper-left corner. |
| [`REFRESH`](ui/refresh.html) | Regenerates the panel each frame (e.g. for scrolling text). Costly for large panels — prefer an OVERLAY. |
| [`RELPOS`](ui/relpos.html) | Panel position (POS_X, POS_Y) is relative to the 3-D window's upper-left corner instead of the screen's; such panels are clipped to the window. |
| [`STRING`](ui/string.html) | The text content (predefined string keyword); `\n` = line break, `\"` = quote; NULL = no text. |
| [`TEXT`](ui/text.html) | Defines a text display inside the 3D window (messages, dialogue). |
| [`VBAR`](ui/vbar.html) | Vertical bar gauge: the bitmap is shifted by skill×fac. Up to 16 bars per panel. |
