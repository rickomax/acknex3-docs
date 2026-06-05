---
layout: default
title: Ways (WAY)
parent: API Reference
has_children: true
nav_order: 9
---

# Ways (WAY)

A Way is a list of up to 32 spatial points (waypoints). An Actor assigned a Way travels cyclically from one waypoint to the next.

| Keyword | Summary |
|:--------|:--------|
| [`WAY`](way/way.html) | Defines a Way; the waypoint list is assigned in WED. No collision detection unless the Actor flag CAREFULLY is set. |
| [`WAYPOINT`](way/waypoint.html) | Current/target waypoint number (1..32) of an Actor on its Way. |
