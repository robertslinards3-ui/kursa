# ops-panel — agent briefing

Read this first, every session.

## What stage this project is at

**Pre-code.** Right now this folder is a decision record, an execution plan and a budget —
nothing to run yet. Read [`PROJECT.md`](PROJECT.md) first, every time — it has the current
decision, the v1 scope cut, the open TODOs, and the validation gate. Don't assume yesterday's
plan is still today's plan without checking it.

The folder name `ops-panel` is historical — see below.

## What this actually is

An application to the LU (University of Latvia) 4-month pre-incubation programme (MoneyLab
fintech track recommended): 2-person team (the user + partner Roberts, aka "Matjas"), funding up
to €3,506 with a 3-supplier price survey per budget line, application deadline 2026-09-27 23:59.
The submission kit (filled LU forms + generator scripts) lives in `pieteikums/`.

**Chosen direction since 2026-09-23: Option A — freight, narrowed to "CMR photo → invoice →
paid"** for small Latvian hauliers (5–50 trucks): photo of the signed paper CMR → Claude reads the
fields → human confirms → invoice PDF + export to the carrier's accounting program → payment
tracking/reminders. The full-TMS idea was dropped after competitor research (Planlogi, Mapon,
Dashdoc… already do it) — see [`TIRGUS_IZPETE.md`](TIRGUS_IZPETE.md) and PROJECT.md decision #3.
Full original vision: [`freight-platform-option.md`](freight-platform-option.md); execution plan:
[`PLAN.md`](PLAN.md); budget: [`BUDZETS.md`](BUDZETS.md).

Important fact already checked: the EU eFTI regulation is **voluntary for hauliers** (mandatory
only for authorities to accept). The real "must" is Latvian B2B e-invoicing from 2028-01-01.
Don't let pitch text slip back to "carriers must digitise twice".

**Parked: Option B** — live operations map (drones, LoRa trackers, search & rescue),
[`ops-panel-option.md`](ops-panel-option.md). It was the choice before 2026-09-23. Not dead;
don't delete it.

## The validation gate — matters more than code right now

`PROJECT.md` has two unchecked gates: 15 interviews with small hauliers (fewer than 3 pilot
yeses → stop and rethink) and a technical test (Claude reads ≥ 90% of invoice fields on 30 real
CMR photos). If the user asks for help with outreach, interview scripts, or
synthesising interview notes, that work is at least as important as code. Don't let "let's start
building" quietly skip past it.

## Budget and reporting

LU does not hand out money freely — everything must be reported. `BUDZETS.md` summarises the
line items with sources and dates; the submitted numbers live in `pieteikums/budzets.py`
(regenerates the LU .xlsx). Change numbers there and keep `BUDZETS.md` in sync. When prices are re-checked or spending happens, update it (and
keep the rule: every expense needs a receipt/invoice in the team's expense log).

## Relationship to DroneSim

[`../DroneSim/`](../DroneSim/) is a separate project (EUDIS hackathon) with the same partner.
It mattered for Option B (MAVLink/ArduPilot). It has little technical overlap with the freight
platform — don't merge work between them without asking.

## Working conventions

- Language: the user writes in Latvian. `PROJECT.md` and this file are in English;
  team/LU-facing documents (`PLAN.md`, `BUDZETS.md`) are in Latvian.
- No GitHub repo exists yet — don't create one unprompted.
- Keep `PROJECT.md`'s checkboxes and open questions current.
- Scope discipline: v1 is only CMR photo upload + AI extraction + invoice/export + payment
  tracking. No dispatch board, driver app, own e-CMR or own Peppol delivery. Weigh new scope
  against "two people, 4 months" and against what competitors already do (TIRGUS_IZPETE.md).
