# Option B (parked) — Live operations panel ("civil Delta")

> Was the chosen direction until 2026-09-23, when the team (you + Roberts) decided to focus on
> Option A, the freight platform (see [`PROJECT.md`](PROJECT.md)). Kept in full, not deleted —
> it's the more hardware/drone-heavy idea and may come back post-incubator.

## What it is

One live map showing drones, tracked people, vehicles, and cameras, shared by multiple
coordinators in real time. The "Delta for civil use" pitch — Ukraine's Delta, NATO's SitaWare,
and the Anduril/Palantir Army contract are the reference points for where this category goes at
the high end; two people cannot compete there directly. Civil-first go-to-market instead: search
& rescue, event security, ports/airports, forestry/lone workers.

Hardware: LoRa GPS trackers (work without mobile coverage) + gateway; drones join via MAVLink
(ArduPilot-standard); Cursor-on-Target format for TAK ecosystem compatibility.

## Why it was picked originally

1. **Not starting from zero.** The MAVLink/ArduPilot piece overlaps directly with
   [DroneSim](../DroneSim/), which already has a working ArduPilot SITL setup talking MAVLink.
2. **Founder energy.** Hardware + drones is what's exciting to build.
3. **The real risk is scope, not the jury.**

## Scope decisions that were made

- Cut for v1: the CQB indoor drone module (second hardware platform + pipeline).
- One scenario done well: a single forest search-and-rescue demo — drone finds a "missing
  person," searcher tracker dots move on the shared map in real time.

## Validation that was planned (never started)

- Search & rescue coordinators / volunteer SAR groups — do they want a shared live map, or does
  radio + paper already solve it well enough?
- Event security / festival & stadium security companies
- At least one port/airport or industrial site security contact

## Build plan from the original pitch (unvalidated)

- Weeks 1–3: map panel with live positions, roles/permissions, one drone via MAVLink
- Weeks 4–6: 5–10 LoRa trackers + gateway, tested in a real forest (foliage attenuation is a
  genuine unknown — test early)
- Weeks 7–10: multi-user command view, event log, mission replay
- Weeks 11–12: full mock search, recorded as the jury demo video
- Rough budget: ~€300–500 ten trackers, ~€150–300 gateway, ~€800–1,200 drone (or borrow the
  hackathon one), rugged tablet, server. A draft €3,600 split existed in the 2026-09-23 chat:
  trackers 450 / gateway 300 / drone 1,100 / thermal camera 450 / tablet 350 / batteries &
  enclosures 250 / server 150 / field-test travel 150 / reserve 400.
