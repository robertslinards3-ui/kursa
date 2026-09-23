# Option A (CHOSEN 2026-09-23) — Freight platform with auto-invoicing and route optimization

> This is now the chosen direction — see [`PROJECT.md`](PROJECT.md) for the decision, the v1
> scope cut, and a correction to the "why now" below; see [`PLAN.md`](PLAN.md) for execution.
> This file is the full original feature vision; most of it is post-incubator roadmap.

## What it is

One system for a small haulier (5 to 50 trucks): a load comes in, the system picks the best
truck and driver, plans the route, the driver captures proof of delivery on a phone, and the
invoice goes out automatically the moment the delivery is signed. Cash comes in weeks faster
because nothing waits for paper.

## Why now

Two deadlines hit customers back to back. From 9 July 2027, authorities in every EU member state
must accept electronic freight information via certified eFTI platforms. Then Latvian B2B
e-invoicing becomes mandatory on 1 January 2028. Carriers must digitise twice in six months —
one system handling both is the pitch.

> **Correction (2026-09-23):** eFTI is *voluntary* for hauliers — it obliges authorities to
> accept electronic data, not carriers to send it. Only the 2028 e-invoicing mandate is a real
> "must". See `PROJECT.md`.

## Feature surface

- eCMR creation and digital signatures at loading and delivery
- Invoice generated from the signed delivery, sent in the new e-invoice format
- Payment chasing: automatic reminders when a shipper is late
- Load to truck matching based on location, hours left, and trailer type
- Backhaul finding, so trucks don't drive home empty
- Toll cost calculation for quotes, which dispatchers currently do by hand
- Driver hours and rest period tracking against tachograph rules
- Posting declarations for drivers working abroad under the Mobility Package
- Truck return home rules and cabotage limits tracking
- Driver per diem calculation — a notoriously messy Latvian payroll task
- Fuel card reconciliation against actual routes
- CO2 reports per shipment, increasingly demanded by big shippers from subcontractors
- Damage and claims evidence: timestamped photos at loading and unloading
- Border queue and crossing time planning
- Trailer and vehicle maintenance reminders
- Driver app in Latvian, Lithuanian, Russian and Ukrainian (mixed-language crews are the norm)
- Customer tracking portal so shippers stop calling dispatch
- Profitability per truck, per route and per customer

## Hardware angle

A cheap tracker plus camera box for subcontracted trucks, so a forwarder sees every truck even
when drivers don't run the app, and loading photos are captured automatically. Modest, but real.

## Competition

Not an empty space. Planlogi already markets an eFTI-compliant TMS for European hauliers with
5–100 trucks, auto-generated eCMRs and invoicing from the same record. Germany's Impargo targets
small carriers with toll calculation and "WhatsApp chaos" as its pitch. The edge would have to be
local: Latvian e-invoicing, Latvian accounting software integration, per diem rules, and
languages the big players won't bother with.

## How and when (original sketch — superseded by PLAN.md)

- Weeks 1–4: interview 15 small hauliers, then build dispatch board, driver app, invoice-from-
  delivery
- Weeks 5–12: pilot with 2–3 carriers, add route optimization and payment chasing
- Revenue possible within 3–4 months at roughly €30–80 per truck per month

## Verdict (from the original analysis)

Clear buyers, recurring revenue, uses a finance background. But it is mostly software,
competitors exist, and the hardware/drone excitement is nearly absent — which is why it lost out
to Option B at first. On 2026-09-23 the team chose it anyway as the primary focus.
