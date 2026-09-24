# ops-panel — agent briefing

Read this first, every session.

## What stage this project is at

**Pre-code.** Right now this folder is a decision record, an execution plan and a budget —
nothing to run yet. Read [`PROJECT.md`](PROJECT.md) first, every time — it has the current
decision, the v1 scope cut, the open TODOs, and the validation gate. Don't assume yesterday's
plan is still today's plan without checking it.

The folder name `ops-panel` is historical — see below.

## What this actually is

Team **Kursa** — **Roberts Linards** (the user, LU E-Bizness) and **Roberts Kaņepons** (partner,
aka "Matjas", GitHub Matjas01, LU Finanšu menedžments) — applying to the LU 4-month
pre-incubation programme, track **"Idea to Impact"**, funding up to €3,506 per team,
deadline 2026-09-27 23:59.

**The founders' own form [`Kursa_PieteikumaAnketa.docx`](Kursa_PieteikumaAnketa.docx) is the source
of truth** (read 2026-09-24). Don't edit it unless asked; make every other file follow it. Kursa is
an AI platform for Baltic SME hauliers (5–100 trucks, Baltic–Nordic corridor): order intake from
e-mails/PDFs → pricing → planning → eCMR/CMR photo → invoice in the customer country's e-invoice
format (LV Peppol, NO EHF) → compliance; "the human approves". The MVP is only the 1–2
highest-saving functions, chosen after interviews and shadowing a dispatcher. Goals: 15+
interviews (carriers and forwarders), first prototype, tests with 2–3 carriers, business model and
pricing. See PROJECT.md and PLAN.md.

Claude's earlier proposal to narrow the whole product to "CMR photo → invoice" (PROJECT.md,
decision #3) was **not adopted**; the competitor research in [`TIRGUS_IZPETE.md`](TIRGUS_IZPETE.md)
still applies (Planlogi, Mapon, Dashdoc already sell full TMS).

Checked facts: eFTI is voluntary for hauliers (authorities must accept from 2027-07-09); LV B2B
e-invoices 2028-01-01; NO B2B e-invoice issuance 2027-01-01. Two claims in the form have no source
yet (see PROJECT.md) — don't repeat them elsewhere until sourced.

**Parked: Option B** — live operations map (drones, LoRa, search & rescue),
[`ops-panel-option.md`](ops-panel-option.md). Not dead; don't delete it.

## The validation gate — matters more than code right now

The plan starts with 15 interviews and dispatcher shadowing; the MVP functions are chosen only
after that. If the user asks for help with outreach, interview scripts, or synthesising interview
notes, that work is at least as important as code.

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
- Local git repo exists; no GitHub remote yet (waiting for the user to create a private repo).
- Keep `PROJECT.md`'s checkboxes and open questions current.
- Scope discipline: the MVP is 1–2 of the form's six functions, not the platform. Weigh new
  scope against "two people, 4 months" and against what competitors already do (TIRGUS_IZPETE.md).
- `pieteikums/PIETEIKUMS.md` + `aizpildit.py` were Claude's draft of the form; the founders wrote
  their own form instead. Don't regenerate or submit the draft docx.
